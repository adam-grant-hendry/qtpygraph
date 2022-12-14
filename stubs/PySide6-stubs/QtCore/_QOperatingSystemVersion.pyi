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
from typing import overload

import PySide6.QtCore

class QOperatingSystemVersion:
    """
    https://doc.qt.io/qt-6/qoperatingsystemversion.html

    **Detailed Description**

    Unlike other version functions in **QSysInfo** , QOperatingSystemVersion
    provides access to the full version number that **developers** typically use
    to vary behavior or determine whether to enable APIs or features based on
    the operating system version (as opposed to the kernel version number or
    marketing version).

    Presently, Android, Apple Platforms (iOS, macOS, tvOS, and watchOS), and
    Windows are supported.

    The **majorVersion()** , **minorVersion()** , and **microVersion()**
    functions return the parts of the operating system version number based on:

    PlatformsValue
    Androidresult of parsing
    **android.os.Build.VERSION.RELEASE**  using **QVersionNumber** , with a
    fallback to **android.os.Build.VERSION.SDK_INT**  to determine the major and
    minor version component if the former fails
    Apple
    Platforms**majorVersion** , **minorVersion** , and patchVersion from
    **NSProcessInfo.operatingSystemVersion**
    WindowsdwMajorVersion,
    dwMinorVersion, and dwBuildNumber from **RtlGetVersion**  \\- note that this
    function ALWAYS return the version number of the underlying operating
    system, as opposed to the shim underneath GetVersionEx that hides the real
    version number if the application is not manifested for that version of the
    OS

    Because QOperatingSystemVersion stores both a version number and an OS type,
    the OS type can be taken into account when performing comparisons. For
    example, on a macOS system running macOS Sierra (v10.12), the following
    expression will return `false` even though the major version number
    component of the object on the left hand side of the expression (10) is
    greater than that of the object on the right (9):

    **QOperatingSystemVersion** ::current() >= **QOperatingSystemVersion**
    (**QOperatingSystemVersion** ::IOS, 9)

    This allows expressions for multiple operating systems to be joined with a
    logical OR operator and still work as expected. For example:

    auto current = **QOperatingSystemVersion** ::current();
            if (current
    >= **QOperatingSystemVersion** ::OSXYosemite ||
                current >=
    **QOperatingSystemVersion** (**QOperatingSystemVersion** ::IOS, 8)) {
    // returns true on macOS >= 10.10 and iOS >= 8.0, but false on macOS < 10.10
    and iOS < 8.0
            }

    A more naive comparison algorithm might incorrectly return true on all
    versions of macOS, including Mac OS 9. This behavior is achieved by
    overloading the comparison operators to return `false` whenever the OS types
    of the QOperatingSystemVersion instances being compared do not match. Be
    aware that due to this it can be the case `x` >= y and `x` < y are BOTH
    `false` for the same instances of `x` and `y`.
    """

    Unknown: QOperatingSystemVersion.OSType = ...
    Windows: QOperatingSystemVersion.OSType = ...
    MacOS: QOperatingSystemVersion.OSType = ...
    IOS: QOperatingSystemVersion.OSType = ...
    TvOS: QOperatingSystemVersion.OSType = ...
    WatchOS: QOperatingSystemVersion.OSType = ...
    Android: QOperatingSystemVersion.OSType = ...

    class OSType(IntFlag):
        Unknown: QOperatingSystemVersion.OSType = ...
        Windows: QOperatingSystemVersion.OSType = ...
        MacOS: QOperatingSystemVersion.OSType = ...
        IOS: QOperatingSystemVersion.OSType = ...
        TvOS: QOperatingSystemVersion.OSType = ...
        WatchOS: QOperatingSystemVersion.OSType = ...
        Android: QOperatingSystemVersion.OSType = ...
    @overload
    def __init__(
        self, QOperatingSystemVersion: PySide6.QtCore.QOperatingSystemVersion
    ) -> None:
        """
        https://doc.qt.io/qt-6/qoperatingsystemversion.html#QOperatingSystemVers
        ion

        **QOperatingSystemVersion::QOperatingSystemVersion(QOperatingSystemVersi
        on::OSType osType , int vmajor , int vminor = -1, int vmicro = -1)**

        Constructs a QOperatingSystemVersion consisting of the OS type
        **osType** , and major, minor, and micro version numbers **vmajor** ,
        **vminor** and **vmicro** , respectively.
        """
        ...
    @overload
    def __init__(
        self,
        osType: PySide6.QtCore.QOperatingSystemVersion.OSType,
        vmajor: int,
        vminor: int = ...,
        vmicro: int = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qoperatingsystemversion.html#QOperatingSystemVers
        ion

        **QOperatingSystemVersion::QOperatingSystemVersion(QOperatingSystemVersi
        on::OSType osType , int vmajor , int vminor = -1, int vmicro = -1)**

        Constructs a QOperatingSystemVersion consisting of the OS type
        **osType** , and major, minor, and micro version numbers **vmajor** ,
        **vminor** and **vmicro** , respectively.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    @staticmethod
    def current() -> PySide6.QtCore.QOperatingSystemVersion:
        """
        https://doc.qt.io/qt-6/qoperatingsystemversion.html#current

        **[static] QOperatingSystemVersion QOperatingSystemVersion::current()**

        Returns a **QOperatingSystemVersion**  indicating the current OS and its
        version number.

        **See also** **currentType** ().
        """
        ...
    @staticmethod
    def currentType() -> PySide6.QtCore.QOperatingSystemVersion.OSType:
        """
        https://doc.qt.io/qt-6/qoperatingsystemversion.html#currentType

        **[static, since 5.10] QOperatingSystemVersion::OSType
        QOperatingSystemVersion::currentType()**

        Returns the current OS type without constructing a
        **QOperatingSystemVersion**  instance.

        This function was introduced in Qt 5.10.

        **See also** **current** ().
        """
        ...
    def majorVersion(self) -> int:
        """
        https://doc.qt.io/qt-6/qoperatingsystemversion.html#majorVersion

        **int QOperatingSystemVersion::majorVersion() const**

        Returns the major version number, that is, the first segment of the
        operating system's version number.

        See the main class documentation for what the major version number is on
        a given operating system.

        -1 indicates an unknown or absent version number component.

        **See also** **version** (), **minorVersion** (), and **microVersion**
        ().
        """
        ...
    def microVersion(self) -> int:
        """
        https://doc.qt.io/qt-6/qoperatingsystemversion.html#microVersion

        **int QOperatingSystemVersion::microVersion() const**

        Returns the micro version number, that is, the third segment of the
        operating system's version number.

        See the main class documentation for what the micro version number is on
        a given operating system.

        -1 indicates an unknown or absent version number component.

        **See also** **version** (), **majorVersion** (), and **minorVersion**
        ().
        """
        ...
    def minorVersion(self) -> int:
        """
        https://doc.qt.io/qt-6/qoperatingsystemversion.html#minorVersion

        **int QOperatingSystemVersion::minorVersion() const**

        Returns the minor version number, that is, the second segment of the
        operating system's version number.

        See the main class documentation for what the minor version number is on
        a given operating system.

        -1 indicates an unknown or absent version number component.

        **See also** **version** (), **majorVersion** (), and **microVersion**
        ().
        """
        ...
    def name(self) -> str:
        """
        https://doc.qt.io/qt-6/qoperatingsystemversion.html#name

        **QString QOperatingSystemVersion::name() const**

        Returns a string representation of the OS type identified by the
        **QOperatingSystemVersion** .

        **See also** **type** ().
        """
        ...
    def segmentCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qoperatingsystemversion.html#segmentCount

        **int QOperatingSystemVersion::segmentCount() const**

        Returns the number of integers stored in the version number.
        """
        ...
    def type(self) -> PySide6.QtCore.QOperatingSystemVersion.OSType:
        """
        https://doc.qt.io/qt-6/qoperatingsystemversion.html#type

        **QOperatingSystemVersion::OSType QOperatingSystemVersion::type()
        const**

        Returns the OS type identified by the **QOperatingSystemVersion** .

        **See also** **name** ().
        """
        ...
    def version(self) -> PySide6.QtCore.QVersionNumber:
        """
        https://doc.qt.io/qt-6/qoperatingsystemversion.html#version

        **[since 6.1] QVersionNumber QOperatingSystemVersion::version() const**

        Returns the operating system's version number.

        See the main class documentation for what the version number is on a
        given operating system.

        This function was introduced in Qt 6.1.

        **See also** **majorVersion** (), **minorVersion** (), and
        **microVersion** ().
        """
        ...
