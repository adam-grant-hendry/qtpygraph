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

from collections.abc import Callable

import PySide6.QtCore

class Property:
    def __init__(
        self,
        type: type,
        fget: Callable | None = ...,
        fset: Callable | None = ...,
        freset: Callable | None = ...,
        fdel: Callable | None = ...,
        doc: str = ...,
        notify: Callable | None = ...,
        designable: bool = ...,
        scriptable: bool = ...,
        stored: bool = ...,
        user: bool = ...,
        constant: bool = ...,
        final: bool = ...,
    ) -> PySide6.QtCore.Property: ...
    def deleter(self, fdel: Callable) -> PySide6.QtCore.Property: ...
    def getter(self, fget: Callable) -> PySide6.QtCore.Property: ...
    def read(self, fget: Callable) -> PySide6.QtCore.Property: ...
    def setter(self, fset: Callable) -> PySide6.QtCore.Property: ...
    def write(self, fset: Callable) -> PySide6.QtCore.Property: ...
