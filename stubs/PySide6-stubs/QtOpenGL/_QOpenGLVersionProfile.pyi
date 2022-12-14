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
PySide6.QtOpenGL, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtOpenGL

class QOpenGLVersionProfile:
    """
    https://doc.qt.io/qt-6/qopenglversionprofile.html

    **Detailed Description**

    An object of this class can be passed to QOpenGLContext::versionFunctions()
    to request a functions object for a specific version and profile of OpenGL.

    It also contains some helper functions to check if a version supports
    profiles or is a legacy version.
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglversionprofile.html#QOpenGLVersionProfile

        **QOpenGLVersionProfile::QOpenGLVersionProfile()**

        Creates a default invalid QOpenGLVersionProfile object.
        """
        ...
    @overload
    def __init__(
        self,
        format: (
            PySide6.QtGui.QSurfaceFormat | PySide6.QtGui.QSurfaceFormat.FormatOptions
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qopenglversionprofile.html#QOpenGLVersionProfile-
        1

        **QOpenGLVersionProfile::QOpenGLVersionProfile(const QSurfaceFormat &
        format )**

        Creates a QOpenGLVersionProfile object initialised with the version and
        profile from **format**.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtOpenGL.QOpenGLVersionProfile) -> None:
        """
        https://doc.qt.io/qt-6/qopenglversionprofile.html#QOpenGLVersionProfile-
        2

        **QOpenGLVersionProfile::QOpenGLVersionProfile(const
        QOpenGLVersionProfile & other )**

        Constructs a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def hasProfiles(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglversionprofile.html#hasProfiles

        **bool QOpenGLVersionProfile::hasProfiles() const**

        Returns `true` if profiles are supported by the OpenGL version returned
        by **version** (). Only OpenGL versions >= 3.2 support profiles.

        **See also** **profile** () and **version** ().
        """
        ...
    def isLegacyVersion(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglversionprofile.html#isLegacyVersion

        **bool QOpenGLVersionProfile::isLegacyVersion() const**

        Returns `true` is the OpenGL version returned by **version** () contains
        deprecated functions and does not support profiles i.e. if the OpenGL
        version is <= 3.1.
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglversionprofile.html#isValid

        **bool QOpenGLVersionProfile::isValid() const**

        Returns `true` if the version number is valid. Note that for a default
        constructed **QOpenGLVersionProfile**  object this function will return
        `false`.

        **See also** **setVersion** () and **version** ().
        """
        ...
    def profile(self) -> PySide6.QtGui.QSurfaceFormat.OpenGLContextProfile:
        """
        https://doc.qt.io/qt-6/qopenglversionprofile.html#profile

        **QSurfaceFormat::OpenGLContextProfile QOpenGLVersionProfile::profile()
        const**

        Returns the OpenGL profile. Only makes sense if profiles are supported
        by this version.

        **See also** **setProfile** ().
        """
        ...
    def setProfile(
        self, profile: PySide6.QtGui.QSurfaceFormat.OpenGLContextProfile
    ) -> None:
        """
        https://doc.qt.io/qt-6/qopenglversionprofile.html#setProfile

        **void
        QOpenGLVersionProfile::setProfile(QSurfaceFormat::OpenGLContextProfile
        profile )**

        Sets the OpenGL profile **profile**. Only makes sense if profiles are
        supported by this version.

        **See also** **profile** ().
        """
        ...
    def setVersion(self, majorVersion: int, minorVersion: int) -> None:
        """
        https://doc.qt.io/qt-6/qopenglversionprofile.html#setVersion

        **void QOpenGLVersionProfile::setVersion(int majorVersion , int
        minorVersion )**

        Sets the major and minor version numbers to **majorVersion** and
        **minorVersion** respectively.

        **See also** **version** ().
        """
        ...
    def version(self) -> tuple[int, int]:
        """
        https://doc.qt.io/qt-6/qopenglversionprofile.html#version

        **QPair<int, int> QOpenGLVersionProfile::version() const**

        Returns a QPair<int,int> where the components represent the major and
        minor OpenGL version numbers respectively.

        **See also** **setVersion** ().
        """
        ...
