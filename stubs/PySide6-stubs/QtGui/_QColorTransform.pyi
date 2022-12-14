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

from typing import Any, overload

import PySide6.QtCore
import PySide6.QtGui

class QColorTransform:
    """
    https://doc.qt.io/qt-6/qcolortransform.html

    **Detailed Description**

    QColorTransform is an instantiation of a transformation between color
    spaces. It can be applied on color and pixels to convert them from one color
    space to another.

    Setting up a QColorTransform takes some preprocessing, so keeping around
    QColorTransforms that you need often is recommended, instead of generating
    them on the fly.
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, colorTransform: PySide6.QtGui.QColorTransform) -> None: ...
    @staticmethod
    def __copy__() -> None: ...
    @overload
    def map(self, argb: int) -> int:
        """
        https://doc.qt.io/qt-6/qcolortransform.html#map

        **QRgb QColorTransform::map(QRgb argb ) const**

        Applies the color transformation on the **QRgb**  value **argb**.

        The input should be opaque or unpremultiplied.
        """
        ...
    @overload
    def map(
        self,
        color: (
            PySide6.QtGui.QColor
            | PySide6.QtGui.QRgba64
            | Any
            | PySide6.QtCore.Qt.GlobalColor
            | str
            | int
        ),
    ) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qcolortransform.html#map-1

        **QRgba64 QColorTransform::map(QRgba64 rgba64 ) const**

        Applies the color transformation on the **QRgba64**  value **rgba64**.

        The input should be opaque or unpremultiplied.
        """
        ...
    @overload
    def map(self, rgba64: PySide6.QtGui.QRgba64) -> PySide6.QtGui.QRgba64:
        """
        https://doc.qt.io/qt-6/qcolortransform.html#map-2

        **QColor QColorTransform::map(const QColor & color ) const**

        Applies the color transformation on the **QColor**  value **color**.
        """
        ...
    def swap(self, other: PySide6.QtGui.QColorTransform) -> None: ...
