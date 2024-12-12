"""Utility functions for debugging."""

from __future__ import annotations

import platform
import sys

import psutil


def SI2ibi(mem: float) -> tuple[float, str]:
    """Convert from SI bytes to ibibytes.

    Computers use powers of 2, so memory is represented in ibibytes, but
    SI prefixes are powers of 1000)

    kibi (KiB) = (2^10)^1, kilo (KB) = (10^3)^1 (1.024 KiB = 1 KB)
    mebi (MiB) = (2^10)^2, mega (MB) = (10^3)^2 (1.048576 MiB = 1 MB)
    gibi (GiB) = (2^10)^3, giga (GB) = (10^3)^3 (1.073741824 GiB = 1 GB)

    Parameters
    ----------
    mem : float
        Memory size in bytes

    Returns
    -------
    tuple[float, str]
        The memory in ibibytes in float and string form
    """
    factor = 1024
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:  # noqa: B007
        if mem < factor:
            break
        mem /= factor

    return mem, f'{unit}iB'


def system_info() -> None:
    """Print the computer system information."""
    # ruff: noqa: T201  # Method to be used by GitHub Issue creators
    header_width = 80

    python_major, python_minor, python_patch, _, _ = sys.version_info
    uname = platform.uname()

    print(f"{' System Info ':=^{header_width}}")

    print(f'OS: {sys.platform}')
    if sys.platform in {'win32', 'cygwin'}:
        major, minor, build, _, _ = sys.getwindowsversion()  # type: ignore[attr-defined,unused-ignore]  # See https://github.com/python/mypy/issues/9025
        print(f'Version: {major}.{minor}, Build {build}')
    else:
        print(f'Release: {uname.release}')
        print(f'Version: {uname.version}')
    print(f'Machine: {uname.machine}')

    print(f"{' CPU Info ':=^{header_width}}")

    print(f'Processor: {uname.processor}')
    print(f'Physical Cores: {psutil.cpu_count(logical=False)}')
    print(f'Total Cores: {psutil.cpu_count(logical=True)}')

    print(f"{' Virtual Memory ':=^{header_width}}")

    svmem = psutil.virtual_memory()

    total, units = SI2ibi(svmem.total)
    print(f'Total: {total:.2f} {units}')

    avail, units = SI2ibi(svmem.available)
    print(f'Available: {avail:.2f} {units}')

    print(f"{' Swap Memory ':=^{header_width}}")

    swap = psutil.swap_memory()

    total, units = SI2ibi(swap.total)
    print(f'Total: {total:.2f} {units}')

    free, units = SI2ibi(swap.free)
    print(f'Available: {free:.2f} {units}')

    print(f"{' Python ':=^{header_width}}")
    print(f'Python: {python_major}.{python_minor}.{python_patch}')


if __name__ == '__main__':
    system_info()
