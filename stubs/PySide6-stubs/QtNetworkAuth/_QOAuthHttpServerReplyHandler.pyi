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
PySide6.QtNetworkAuth, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore
import PySide6.QtNetwork
import PySide6.QtNetworkAuth

class QOAuthHttpServerReplyHandler(PySide6.QtNetworkAuth.QOAuthOobReplyHandler):
    @overload
    def __init__(
        self,
        address: (
            PySide6.QtNetwork.QHostAddress | PySide6.QtNetwork.QHostAddress.SpecialAddress
        ),
        port: int,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None: ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None: ...
    @overload
    def __init__(
        self, port: int, parent: PySide6.QtCore.QObject | None = ...
    ) -> None: ...
    def callback(self) -> str: ...
    def callbackPath(self) -> str: ...
    def callbackText(self) -> str: ...
    def close(self) -> None: ...
    def isListening(self) -> bool: ...
    def listen(
        self,
        address: (
            PySide6.QtNetwork.QHostAddress | PySide6.QtNetwork.QHostAddress.SpecialAddress
        ) = ...,
        port: int = ...,
    ) -> bool: ...
    def port(self) -> int: ...
    def setCallbackPath(self, path: str) -> None: ...
    def setCallbackText(self, text: str) -> None: ...
