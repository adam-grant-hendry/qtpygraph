"""Utility script to change (add/remove) lines matching provided regular expressions."""

from __future__ import annotations

import os
from pathlib import Path

from tqdm import tqdm


def replace_str(path: Path, match: str, replace: str) -> None:
    """Remove the line ``match`` in files under ``path``.

    Parameters
    ----------
    path : Path
        Path containing files to change
    match : str
        The string to match
    replace : str
        String to 'match' with.
    """
    for root, _, files in tqdm(os.walk(path)):
        for file_ in files:
            if file_.endswith('.pyi'):
                pth = os.path.join(root, file_)
                with open(pth, encoding='utf-8') as reader:
                    lines = reader.readlines()
                    with open(pth, 'w', encoding='utf-8') as writer:
                        for line in lines:
                            writer.write(line.replace(match, replace))


if __name__ == '__main__':
    replace_str(Path('./PySide6-stubs'), 'bytes = str', '')
    replace_str(
        Path('./PySide6-stubs/QtCore/_Qt.pyi'),
        'from enum import Enum',
        'from enum import IntFlag',
    )
    replace_str(
        Path('./PySide6-stubs/QtCore/_Qt.pyi'),
        '(Enum)',
        '(IntFlag)',
    )
