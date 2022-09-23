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
PySide6.QtQml, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtNetwork
import PySide6.QtQml

class QQmlExtensionPlugin(PySide6.QtCore.QObject, PySide6.QtQml.QQmlExtensionInterface):
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None: ...
    def baseUrl(self) -> PySide6.QtCore.QUrl: ...
    def initializeEngine(self, engine: PySide6.QtQml.QQmlEngine, uri: bytes) -> None: ...
    def registerTypes(self, uri: bytes) -> None: ...
    def unregisterTypes(self) -> None: ...
