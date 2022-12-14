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
PySide6.QtWebEngineQuick, except for defaults which are replaced by "...".
"""

from __future__ import annotations

class QtWebEngineQuick:
    """
    https://doc.qt.io/qt-6/qtwebenginequick.html

    **Detailed Description**

    The **QtWebEngineQuick**  namespace is part of the Qt WebEngine module.
    """

    @staticmethod
    def initialize() -> None:
        """
        https://doc.qt.io/qt-6/qtwebenginequick.html#initialize

        **void QtWebEngineQuick::initialize()**

        Sets up an OpenGL Context that can be shared between threads. This has
        to be done before **QGuiApplication**  is created and before window's
        QPlatformOpenGLContext is created.

        This has the same effect as setting the **Qt::AA_ShareOpenGLContexts**
        attribute with **QCoreApplication::setAttribute**  before constructing
        **QGuiApplication** .
        """
        ...
