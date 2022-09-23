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
PySide6.QtWidgets, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag
from typing import Any

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QColormap:
    """
    https://doc.qt.io/qt-6/qcolormap.html

    **Detailed Description**
    """

    Direct: QColormap.Mode = ...
    Indexed: QColormap.Mode = ...
    Gray: QColormap.Mode = ...

    class Mode(IntFlag):
        Direct: QColormap.Mode = ...
        Indexed: QColormap.Mode = ...
        Gray: QColormap.Mode = ...
    def __init__(self, colormap: PySide6.QtWidgets.QColormap) -> None:
        """
        https://doc.qt.io/qt-6/qcolormap.html#QColormap

        **QColormap::QColormap(const QColormap & colormap )**

        Constructs a copy of another **colormap**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    @staticmethod
    def cleanup() -> None: ...
    def colorAt(self, pixel: int) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qcolormap.html#colorAt

        **const QColor QColormap::colorAt(uint pixel ) const**

        Returns a **QColor**  for the **pixel**.

        **See also** **pixel** ().
        """
        ...
    def colormap(self) -> list[PySide6.QtGui.QColor]:
        """
        https://doc.qt.io/qt-6/qcolormap.html#colormap

        **const QList<QColor> QColormap::colormap() const**

        Returns a list of colors which represents the devices colormap for
        `Indexed` and `Gray` modes. This function returns an empty list for
        `Direct` mode.

        **See also** **size** ().
        """
        ...
    def depth(self) -> int:
        """
        https://doc.qt.io/qt-6/qcolormap.html#depth

        **int QColormap::depth() const**

        Returns the depth of the device.

        **See also** **size** ().
        """
        ...
    @staticmethod
    def initialize() -> None: ...
    @staticmethod
    def instance(screen: int = ...) -> PySide6.QtWidgets.QColormap:
        """
        https://doc.qt.io/qt-6/qcolormap.html#instance

        **[static] QColormap QColormap::instance(int screen = -1)**

        Returns the colormap for the specified **screen**. If **screen** is -1,
        this function returns the colormap for the default screen.
        """
        ...
    def mode(self) -> PySide6.QtWidgets.QColormap.Mode:
        """
        https://doc.qt.io/qt-6/qcolormap.html#mode

        **QColormap::Mode QColormap::mode() const**

        Returns the mode of this colormap.

        **See also** **QColormap::Mode** .
        """
        ...
    def pixel(
        self,
        color: (
            PySide6.QtGui.QColor
            | PySide6.QtGui.QRgba64
            | Any
            | PySide6.QtCore.Qt.GlobalColor
            | str
            | int
        ),
    ) -> int:
        """
        https://doc.qt.io/qt-6/qcolormap.html#pixel

        **uint QColormap::pixel(const QColor & color ) const**

        Returns a device dependent pixel value for the **color**.

        **See also** **colorAt** ().
        """
        ...
    def size(self) -> int:
        """
        https://doc.qt.io/qt-6/qcolormap.html#size

        **int QColormap::size() const**

        Returns the size of the colormap for `Indexed` and `Gray` modes; Returns
        -1 for `Direct` mode.

        **See also** **colormap** ().
        """
        ...
