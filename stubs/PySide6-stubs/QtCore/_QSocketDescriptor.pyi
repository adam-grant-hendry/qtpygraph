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

from typing import overload

import PySide6.QtCore

class QSocketDescriptor:
    @overload
    def __init__(
        self, QSocketDescriptor: PySide6.QtCore.QSocketDescriptor | int
    ) -> None: ...
    @overload
    def __init__(self, desc: int) -> None: ...
    @overload
    def __init__(self, descriptor: int = ...) -> None: ...
    @staticmethod
    def __copy__() -> None: ...
    def isValid(self) -> bool: ...
    def winHandle(self) -> int: ...
