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
PySide6.QtConcurrent, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtConcurrent
import PySide6.QtCore

class QFutureQString:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QFutureQString: PySide6.QtConcurrent.QFutureQString) -> None: ...
    @staticmethod
    def __copy__() -> None: ...
    def cancel(self) -> None: ...
    def isCanceled(self) -> bool: ...
    def isFinished(self) -> bool: ...
    def isPaused(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def isStarted(self) -> bool: ...
    def isSuspended(self) -> bool: ...
    def isSuspending(self) -> bool: ...
    def isValid(self) -> bool: ...
    def pause(self) -> None: ...
    def progressMaximum(self) -> int: ...
    def progressMinimum(self) -> int: ...
    def progressText(self) -> str: ...
    def progressValue(self) -> int: ...
    def resultCount(self) -> int: ...
    def resume(self) -> None: ...
    def setPaused(self, paused: bool) -> None: ...
    def setSuspended(self, suspend: bool) -> None: ...
    def suspend(self) -> None: ...
    def togglePaused(self) -> None: ...
    def toggleSuspended(self) -> None: ...
    def waitForFinished(self) -> None: ...
