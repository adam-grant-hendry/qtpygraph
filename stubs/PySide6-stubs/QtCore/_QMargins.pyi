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

class QMargins:
    """
    https://doc.qt.io/qt-6/qmargins.html

    **Detailed Description**

    QMargin defines a set of four margins; left, top, right, and bottom, that
    describe the size of the borders surrounding a rectangle.

    The **isNull** () function returns `true` only if all margins are set to
    zero.

    QMargin objects can be streamed as well as compared.
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qmargins.html#QMargins

        **QMargins::QMargins()**

        Constructs a margins object with all margins set to 0.

        **See also** **isNull** ().
        """
        ...
    @overload
    def __init__(self, QMargins: PySide6.QtCore.QMargins) -> None:
        """
        https://doc.qt.io/qt-6/qmargins.html#QMargins-1

        **QMargins::QMargins(int left , int top , int right , int bottom )**

        Constructs margins with the given **left** , **top** , **right** , and
        **bottom**

        **See also** **setLeft** (), **setRight** (), **setTop** (), and
        **setBottom** ().
        """
        ...
    @overload
    def __init__(self, left: int, top: int, right: int, bottom: int) -> None:
        """
        https://doc.qt.io/qt-6/qmargins.html#QMargins

        **QMargins::QMargins()**

        Constructs a margins object with all margins set to 0.

        **See also** **isNull** ().
        """
        ...
    @overload
    def __add__(self, lhs: int) -> PySide6.QtCore.QMargins: ...
    @overload
    def __add__(self, m2: PySide6.QtCore.QMargins) -> PySide6.QtCore.QMargins: ...
    @overload
    def __add__(self, rhs: int) -> PySide6.QtCore.QMargins: ...
    @staticmethod
    def __copy__() -> None: ...
    @overload
    def __iadd__(self, arg__1: int) -> PySide6.QtCore.QMargins: ...
    @overload
    def __iadd__(self, margins: PySide6.QtCore.QMargins) -> PySide6.QtCore.QMargins: ...
    @overload
    def __imul__(self, arg__1: int) -> PySide6.QtCore.QMargins: ...
    @overload
    def __imul__(self, arg__1: float) -> PySide6.QtCore.QMargins: ...
    @overload
    def __isub__(self, arg__1: int) -> PySide6.QtCore.QMargins: ...
    @overload
    def __isub__(self, margins: PySide6.QtCore.QMargins) -> PySide6.QtCore.QMargins: ...
    @overload
    def __mul__(self, factor: int) -> PySide6.QtCore.QMargins: ...
    @overload
    def __mul__(self, factor: float) -> PySide6.QtCore.QMargins: ...
    def __neg__(self) -> PySide6.QtCore.QMargins: ...
    def __or__(self, m2: PySide6.QtCore.QMargins) -> PySide6.QtCore.QMargins: ...
    def __pos__(self) -> PySide6.QtCore.QMargins: ...
    @overload
    def __sub__(self, m2: PySide6.QtCore.QMargins) -> PySide6.QtCore.QMargins: ...
    @overload
    def __sub__(self, rhs: int) -> PySide6.QtCore.QMargins: ...
    def bottom(self) -> int:
        """
        https://doc.qt.io/qt-6/qmargins.html#bottom

        **int QMargins::bottom() const**

        Returns the bottom margin.

        **See also** **setBottom** ().
        """
        ...
    def isNull(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmargins.html#isNull

        **bool QMargins::isNull() const**

        Returns `true` if all margins are is 0; otherwise returns false.
        """
        ...
    def left(self) -> int:
        """
        https://doc.qt.io/qt-6/qmargins.html#left

        **int QMargins::left() const**

        Returns the left margin.

        **See also** **setLeft** ().
        """
        ...
    def right(self) -> int:
        """
        https://doc.qt.io/qt-6/qmargins.html#right

        **int QMargins::right() const**

        Returns the right margin.

        **See also** **setRight** ().
        """
        ...
    def setBottom(self, bottom: int) -> None:
        """
        https://doc.qt.io/qt-6/qmargins.html#setBottom

        **void QMargins::setBottom(int bottom )**

        Sets the bottom margin to **bottom**.

        **See also** **bottom** ().
        """
        ...
    def setLeft(self, left: int) -> None:
        """
        https://doc.qt.io/qt-6/qmargins.html#setLeft

        **void QMargins::setLeft(int left )**

        Sets the left margin to **left**.

        **See also** **left** ().
        """
        ...
    def setRight(self, right: int) -> None:
        """
        https://doc.qt.io/qt-6/qmargins.html#setRight

        **void QMargins::setRight(int right )**

        Sets the right margin to **right**.

        **See also** **right** ().
        """
        ...
    def setTop(self, top: int) -> None:
        """
        https://doc.qt.io/qt-6/qmargins.html#setTop

        **void QMargins::setTop(int Top )**

        Sets the Top margin to **Top**.

        **See also** **top** ().
        """
        ...
    def top(self) -> int:
        """
        https://doc.qt.io/qt-6/qmargins.html#top

        **int QMargins::top() const**

        Returns the top margin.

        **See also** **setTop** ().
        """
        ...
