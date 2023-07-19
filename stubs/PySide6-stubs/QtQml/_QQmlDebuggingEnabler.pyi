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

from collections.abc import Sequence
from enum import IntFlag
from typing import Any

import PySide6.QtCore
import PySide6.QtNetwork
import PySide6.QtQml

class QQmlDebuggingEnabler:
    DoNotWaitForClient: QQmlDebuggingEnabler.StartMode = ...
    WaitForClient: QQmlDebuggingEnabler.StartMode = ...

    class StartMode(IntFlag):
        DoNotWaitForClient: QQmlDebuggingEnabler.StartMode = ...
        WaitForClient: QQmlDebuggingEnabler.StartMode = ...
    def __init__(self, printWarning: bool = ...) -> None: ...
    @staticmethod
    def connectToLocalDebugger(
        socketFileName: str, mode: PySide6.QtQml.QQmlDebuggingEnabler.StartMode = ...
    ) -> bool: ...
    @staticmethod
    def debuggerServices() -> list[str]: ...
    @staticmethod
    def inspectorServices() -> list[str]: ...
    @staticmethod
    def nativeDebuggerServices() -> list[str]: ...
    @staticmethod
    def profilerServices() -> list[str]: ...
    @staticmethod
    def setServices(services: Sequence[str]) -> None: ...
    @staticmethod
    def startDebugConnector(
        pluginName: str, configuration: dict[str, Any] = ...
    ) -> bool: ...
    @staticmethod
    def startTcpDebugServer(
        port: int,
        mode: PySide6.QtQml.QQmlDebuggingEnabler.StartMode = ...,
        hostName: str = ...,
    ) -> bool: ...