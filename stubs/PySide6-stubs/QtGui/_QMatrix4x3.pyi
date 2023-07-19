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
PySide6.QtGui, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from collections.abc import Iterable
from typing import overload

import PySide6.QtCore
import PySide6.QtGui

class QMatrix4x3:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QMatrix4x3: PySide6.QtGui.QMatrix4x3) -> None: ...
    @overload
    def __init__(self, arg__1: Iterable) -> None: ...
    def __call__(self, row: int, column: int) -> float: ...
    @staticmethod
    def __copy__() -> None: ...
    def __iadd__(self, other: PySide6.QtGui.QMatrix4x3) -> PySide6.QtGui.QMatrix4x3: ...
    def __imul__(self, factor: float) -> PySide6.QtGui.QMatrix4x3: ...
    def __isub__(self, other: PySide6.QtGui.QMatrix4x3) -> PySide6.QtGui.QMatrix4x3: ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def data(self) -> float: ...
    def fill(self, value: float) -> None: ...
    def isIdentity(self) -> bool: ...
    def setToIdentity(self) -> None: ...
    def transposed(self) -> PySide6.QtGui.QMatrix3x4: ...