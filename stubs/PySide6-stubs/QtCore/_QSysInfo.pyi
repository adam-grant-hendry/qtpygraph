"""
PySide stub files generated by **IceSpringPySideStubs**

Home: https://baijifeilong.github.io/2022/01/06/ice-spring-pyside-stubs/index.html

Github: https://github.com/baijifeilong/IceSpringPySideStubs

PyPI(PySide2): https://pypi.org/project/IceSpringPySideStubs-PySide2

PyPI(PySide6): https://pypi.org/project/IceSpringPySideStubs-PySide6

PyPI(PyQt5): https://pypi.org/project/IceSpringPySideStubs-PyQt5

PyPI(PyQt6): https://pypi.org/project/IceSpringPySideStubs-PyQt6

Generated by BaiJiFeiLong@gmail.com

License: MIT
"""
"""
This file contains the exact signatures for all functions in module
PySide6.QtCore, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag

import PySide6.QtCore

class QSysInfo:
    """
    https://doc.qt.io/qt-6/qsysinfo.html

    **Detailed Description**

    * **WordSize**  specifies the size of a pointer for the platform on which
    the application is compiled.
      * **ByteOrder**  specifies whether the
    platform is big-endian or little-endian.

    Some constants are defined only on certain platforms. You can use the
    preprocessor symbols **Q_OS_WIN**  and **Q_OS_MACOS**  to test that the
    application is compiled under Windows or macOS.

    **See also** **QLibraryInfo** .
    """

    BigEndian: QSysInfo.Endian = ...
    ByteOrder: QSysInfo.Endian = ...
    LittleEndian: QSysInfo.Endian = ...
    WordSize: QSysInfo.Sizes = ...

    class Endian(IntFlag):
        BigEndian: QSysInfo.Endian = ...
        ByteOrder: QSysInfo.Endian = ...
        LittleEndian: QSysInfo.Endian = ...

    class Sizes(IntFlag):
        WordSize: QSysInfo.Sizes = ...
    def __init__(self) -> None: ...
    @staticmethod
    def bootUniqueId() -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qsysinfo.html#bootUniqueId

        **[static, since 5.11] QByteArray QSysInfo::bootUniqueId()**

        Returns a unique ID for this machine's boot, if one can be determined.
        If no unique ID could be determined, this function returns an empty byte
        array. This value is expected to change after every boot and can be
        considered globally unique.

        This function is currently only implemented for Linux and Apple
        operating systems.

        This function was introduced in Qt 5.11.

        **See also** **machineUniqueId** ().
        """
        ...
    @staticmethod
    def buildAbi() -> str:
        """
        https://doc.qt.io/qt-6/qsysinfo.html#buildAbi

        **[static, since 5.4] QString QSysInfo::buildAbi()**

        Returns the full architecture string that Qt was compiled for. This
        string is useful for identifying different, incompatible builds. For
        example, it can be used as an identifier to request an upgrade package
        from a server.

        The values returned from this function are kept stable as follows: the
        mandatory components of the result will not change in future versions of
        Qt, but optional suffixes may be added.

        The returned value is composed of three or more parts, separated by
        dashes ("-"). They are:

        ComponentValue
        CPU ArchitectureThe same as
        **QSysInfo::buildCpuArchitecture** (), such as "arm", "i386", "mips" or
        "x86_64"
        Endianness"little_endian" or "big_endian"
        Word sizeWhether
        it's a 32- or 64-bit application. Possible values are: "llp64" (Windows
        64-bit), "lp64" (Unix 64-bit), "ilp32" (32-bit)
        (Optional) ABIZero or
        more components identifying different ABIs possible in this
        architecture. Currently, Qt has optional ABI components for ARM and MIPS
        processors: one component is the main ABI (such as "eabi", "o32", "n32",
        "o64"); another is whether the calling convention is using hardware
        floating point registers ("hardfloat" is present).

        Additionally, if Qt
        was configured with `-qreal float`, the ABI option tag "qreal_float"
        will be present. If Qt was configured with another type as qreal, that
        type is present after "qreal_", with all characters other than letters
        and digits escaped by an underscore, followed by two hex digits. For
        example, `-qreal long double` becomes "qreal_long_20double".

        This function was introduced in Qt 5.4.

        **See also** **QSysInfo::buildCpuArchitecture** ().
        """
        ...
    @staticmethod
    def buildCpuArchitecture() -> str:
        """
        https://doc.qt.io/qt-6/qsysinfo.html#buildCpuArchitecture

        **[static, since 5.4] QString QSysInfo::buildCpuArchitecture()**

        Returns the architecture of the CPU that Qt was compiled for, in text
        format. Note that this may not match the actual CPU that the application
        is running on if there's an emulation layer or if the CPU supports
        multiple architectures (like x86-64 processors supporting i386
        applications). To detect that, use **currentCpuArchitecture** ().

        Values returned by this function are stable and will not change over
        time, so applications can rely on the returned value as an identifier,
        except that new CPU types may be added over time.

        Typical returned values are (note: list not exhaustive):

        * "arm"
          * "arm64"
          * "i386"
          * "ia64"
          * "mips"
          * "mips64"
          *
        "power"
          * "power64"
          * "sparc"
          * "sparcv9"
          * "x86_64"

        This function was introduced in Qt 5.4.

        **See also** **QSysInfo::buildAbi** () and
        **QSysInfo::currentCpuArchitecture** ().
        """
        ...
    @staticmethod
    def currentCpuArchitecture() -> str:
        """
        https://doc.qt.io/qt-6/qsysinfo.html#currentCpuArchitecture

        **[static, since 5.4] QString QSysInfo::currentCpuArchitecture()**

        Returns the architecture of the CPU that the application is running on,
        in text format. Note that this function depends on what the OS will
        report and may not detect the actual CPU architecture if the OS hides
        that information or is unable to provide it. For example, a 32-bit OS
        running on a 64-bit CPU is usually unable to determine the CPU is
        actually capable of running 64-bit programs.

        Values returned by this function are mostly stable: an attempt will be
        made to ensure that they stay constant over time and match the values
        returned by QSysInfo::builldCpuArchitecture(). However, due to the
        nature of the operating system functions being used, there may be
        discrepancies.

        Typical returned values are (note: list not exhaustive):

        * "arm"
          * "arm64"
          * "i386"
          * "ia64"
          * "mips"
          * "mips64"
          *
        "power"
          * "power64"
          * "sparc"
          * "sparcv9"
          * "x86_64"

        This function was introduced in Qt 5.4.

        **See also** **QSysInfo::buildAbi** () and
        **QSysInfo::buildCpuArchitecture** ().
        """
        ...
    @staticmethod
    def kernelType() -> str:
        """
        https://doc.qt.io/qt-6/qsysinfo.html#kernelType

        **[static, since 5.4] QString QSysInfo::kernelType()**

        Returns the type of the operating system kernel Qt was compiled for.
        It's also the kernel the application is running on, unless the host
        operating system is running a form of compatibility or virtualization
        layer.

        Values returned by this function are stable and will not change over
        time, so applications can rely on the returned value as an identifier,
        except that new OS kernel types may be added over time.

        On Windows, this function returns the type of Windows kernel, like
        "winnt". On Unix systems, it returns the same as the output of `uname
        -s` (lowercased).

        **Note:** This function may return surprising values: it returns "linux"
        for all operating systems running Linux (including Android), "qnx" for
        all operating systems running QNX, "freebsd" for Debian/kFreeBSD, and
        "darwin" for macOS and iOS. For information on the type of product the
        application is running on, see **productType** ().

        This function was introduced in Qt 5.4.

        **See also** **QFileSelector** , **kernelVersion** (), **productType**
        (), **productVersion** (), and **prettyProductName** ().
        """
        ...
    @staticmethod
    def kernelVersion() -> str:
        """
        https://doc.qt.io/qt-6/qsysinfo.html#kernelVersion

        **[static, since 5.4] QString QSysInfo::kernelVersion()**

        Returns the release version of the operating system kernel. On Windows,
        it returns the version of the NT kernel. On Unix systems, including
        Android and macOS, it returns the same as the `uname -r` command would
        return.

        If the version could not be determined, this function may return an
        empty string.

        This function was introduced in Qt 5.4.

        **See also** **kernelType** (), **productType** (), **productVersion**
        (), and **prettyProductName** ().
        """
        ...
    @staticmethod
    def machineHostName() -> str:
        """
        https://doc.qt.io/qt-6/qsysinfo.html#machineHostName

        **[static, since 5.6] QString QSysInfo::machineHostName()**

        Returns this machine's host name, if one is configured. Note that
        hostnames are not guaranteed to be globally unique, especially if they
        were configured automatically.

        This function does not guarantee the returned host name is a Fully
        Qualified Domain Name (FQDN). For that, use **QHostInfo**  to resolve
        the returned name to an FQDN.

        This function returns the same as **QHostInfo::localHostName** ().

        This function was introduced in Qt 5.6.

        **See also** **QHostInfo::localDomainName**  and **machineUniqueId** ().
        """
        ...
    @staticmethod
    def machineUniqueId() -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qsysinfo.html#machineUniqueId

        **[static, since 5.11] QByteArray QSysInfo::machineUniqueId()**

        Returns a unique ID for this machine, if one can be determined. If no
        unique ID could be determined, this function returns an empty byte
        array. Unlike **machineHostName** (), the value returned by this
        function is likely globally unique.

        A unique ID is useful in network operations to identify this machine for
        an extended period of time, when the IP address could change or if this
        machine could have more than one IP address. For example, the ID could
        be used when communicating with a server or when storing device-specific
        data in shared network storage.

        Note that on some systems, this value will persist across reboots and on
        some it will not. Applications should not blindly depend on this fact
        without verifying the OS capabilities. In particular, on Linux systems,
        this ID is usually permanent and it matches the D-Bus machine ID, except
        for nodes without their own storage (replicated nodes).

        This function was introduced in Qt 5.11.

        **See also** **machineHostName** () and **bootUniqueId** ().
        """
        ...
    @staticmethod
    def prettyProductName() -> str:
        """
        https://doc.qt.io/qt-6/qsysinfo.html#prettyProductName

        **[static, since 5.4] QString QSysInfo::prettyProductName()**

        Returns a prettier form of **productType** () and **productVersion** (),
        containing other tokens like the operating system type, codenames and
        other information. The result of this function is suitable for
        displaying to the user, but not for long-term storage, as the string may
        change with updates to Qt.

        If **productType** () is "unknown", this function will instead use the
        **kernelType** () and **kernelVersion** () functions.

        This function was introduced in Qt 5.4.

        **See also** **kernelType** (), **kernelVersion** (), **productType**
        (), and **productVersion** ().
        """
        ...
    @staticmethod
    def productType() -> str:
        """
        https://doc.qt.io/qt-6/qsysinfo.html#productType

        **[static, since 5.4] QString QSysInfo::productType()**

        Returns the product name of the operating system this application is
        running in. If the application is running on some sort of emulation or
        virtualization layer (such as WINE on a Unix system), this function will
        inspect the emulation / virtualization layer.

        Values returned by this function are stable and will not change over
        time, so applications can rely on the returned value as an identifier,
        except that new OS types may be added over time.

        **Linux and Android note** : this function returns "android" for Linux
        systems running Android userspace, notably when using the Bionic
        library. For all other Linux systems, regardless of C library being
        used, it tries to determine the distribution name and returns that. If
        determining the distribution name failed, it returns "unknown".

        **macOS note** : this function returns "osx" for all macOS systems,
        regardless of Apple naming convention. The returned string will be
        updated for Qt 6. Note that this function erroneously returned "macos"
        for macOS 10.12 in Qt versions 5.6.2, 5.7.1, and 5.8.0.

        **Darwin, iOS, tvOS, and watchOS note** : this function returns "ios"
        for iOS systems, "tvos" for tvOS systems, "watchos" for watchOS systems,
        and "darwin" in case the system could not be determined.

        **FreeBSD note** : this function returns "debian" for Debian/kFreeBSD
        and "unknown" otherwise.

        **Windows note** : this function return "windows"

        For other Unix-type systems, this function usually returns "unknown".

        This function was introduced in Qt 5.4.

        **See also** **QFileSelector** , **kernelType** (), **kernelVersion**
        (), **productVersion** (), and **prettyProductName** ().
        """
        ...
    @staticmethod
    def productVersion() -> str:
        """
        https://doc.qt.io/qt-6/qsysinfo.html#productVersion

        **[static, since 5.4] QString QSysInfo::productVersion()**

        Returns the product version of the operating system in string form. If
        the version could not be determined, this function returns "unknown".

        It will return the Android, iOS, macOS, Windows full-product versions on
        those systems.

        Typical returned values are (note: list not exhaustive):

        * "2016.09" (Amazon Linux AMI 2016.09)
          * "7.1" (Android Nougat)
          *
        "25" (Fedora 25)
          * "10.1" (iOS 10.1)
          * "10.12" (macOS Sierra)
          *
        "10.0" (tvOS 10)
          * "16.10" (Ubuntu 16.10)
          * "3.1" (watchOS 3.1)
          *
        "10" (Windows 10)
          * "Server 2016" (Windows Server 2016)

        On Linux systems, it will try to determine the distribution version and
        will return that. This is also done on Debian/kFreeBSD, so this function
        will return Debian version in that case.

        In all other Unix-type systems, this function always returns "unknown".

        **Note:** The version string returned from this function is not
        guaranteed to be orderable. On Linux, the version of the distribution
        may jump unexpectedly, please refer to the distribution's documentation
        for versioning practices.

        This function was introduced in Qt 5.4.

        **See also** **kernelType** (), **kernelVersion** (), **productType**
        (), and **prettyProductName** ().
        """
        ...