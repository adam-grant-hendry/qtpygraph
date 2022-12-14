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

class QSize:
    """
    https://doc.qt.io/qt-6/qsize.html

    **Detailed Description**

    A size is specified by a **width** () and a **height** (). It can be set in
    the constructor and changed using the **setWidth** (), **setHeight** (), or
    **scale** () functions, or using arithmetic operators. A size can also be
    manipulated directly by retrieving references to the width and height using
    the **rwidth** () and **rheight** () functions. Finally, the width and
    height can be swapped using the **transpose** () function.

    The **isValid** () function determines if a size is valid (a valid size has
    both width and height greater than or equal to zero). The **isEmpty** ()
    function returns `true` if either of the width and height is less than, or
    equal to, zero, while the **isNull** () function returns `true` only if both
    the width and the height is zero.

    Use the **expandedTo** () function to retrieve a size which holds the
    maximum height and width of **this** size and a given size. Similarly, the
    **boundedTo** () function returns a size which holds the minimum height and
    width of **this** size and a given size.

    QSize objects can be streamed as well as compared.

    **See also** **QSizeF** , **QPoint** , and **QRect** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qsize.html#QSize

        **QSize::QSize()**

        Constructs a size with an invalid width and height (i.e., **isValid** ()
        returns `false`).

        **See also** **isValid** ().
        """
        ...
    @overload
    def __init__(self, QSize: PySide6.QtCore.QSize) -> None:
        """
        https://doc.qt.io/qt-6/qsize.html#QSize-1

        **QSize::QSize(int width , int height )**

        Constructs a size with the given **width** and **height**.

        **See also** **setWidth** () and **setHeight** ().
        """
        ...
    @overload
    def __init__(self, w: int, h: int) -> None:
        """
        https://doc.qt.io/qt-6/qsize.html#QSize

        **QSize::QSize()**

        Constructs a size with an invalid width and height (i.e., **isValid** ()
        returns `false`).

        **See also** **isValid** ().
        """
        ...
    def __add__(self, s2: PySide6.QtCore.QSize) -> PySide6.QtCore.QSize: ...
    @staticmethod
    def __copy__() -> None: ...
    def __iadd__(self, arg__1: PySide6.QtCore.QSize) -> PySide6.QtCore.QSize: ...
    def __imul__(self, c: float) -> PySide6.QtCore.QSize: ...
    def __isub__(self, arg__1: PySide6.QtCore.QSize) -> PySide6.QtCore.QSize: ...
    def __mul__(self, c: float) -> PySide6.QtCore.QSize: ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def __sub__(self, s2: PySide6.QtCore.QSize) -> PySide6.QtCore.QSize: ...
    def boundedTo(self, arg__1: PySide6.QtCore.QSize) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qsize.html#boundedTo

        **QSize QSize::boundedTo(const QSize & otherSize ) const**

        Returns a size holding the minimum width and height of this size and the
        given **otherSize**.

        **See also** **expandedTo** () and **scale** ().
        """
        ...
    def expandedTo(self, arg__1: PySide6.QtCore.QSize) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qsize.html#expandedTo

        **QSize QSize::expandedTo(const QSize & otherSize ) const**

        Returns a size holding the maximum width and height of this size and the
        given **otherSize**.

        **See also** **boundedTo** () and **scale** ().
        """
        ...
    def grownBy(self, m: PySide6.QtCore.QMargins) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qsize.html#grownBy

        **[since 5.14] QSize QSize::grownBy(QMargins margins ) const**

        Returns the size that results from growing this size by **margins**.

        This function was introduced in Qt 5.14.

        **See also** **shrunkBy** ().
        """
        ...
    def height(self) -> int:
        """
        https://doc.qt.io/qt-6/qsize.html#height

        **int QSize::height() const**

        Returns the height.

        **See also** **width** () and **setHeight** ().
        """
        ...
    def isEmpty(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsize.html#isEmpty

        **bool QSize::isEmpty() const**

        Returns `true` if either of the width and height is less than or equal
        to 0; otherwise returns `false`.

        **See also** **isNull** () and **isValid** ().
        """
        ...
    def isNull(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsize.html#isNull

        **bool QSize::isNull() const**

        Returns `true` if both the width and height is 0; otherwise returns
        false.

        **See also** **isValid** () and **isEmpty** ().
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsize.html#isValid

        **bool QSize::isValid() const**

        Returns `true` if both the width and height is equal to or greater than
        0; otherwise returns `false`.

        **See also** **isNull** () and **isEmpty** ().
        """
        ...
    @overload
    def scale(
        self, s: PySide6.QtCore.QSize, mode: PySide6.QtCore.Qt.AspectRatioMode
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsize.html#scale

        **void QSize::scale(int width , int height , Qt::AspectRatioMode mode
        )**

        Scales the size to a rectangle with the given **width** and **height** ,
        according to the specified **mode** :

        * If **mode** is **Qt::IgnoreAspectRatio** , the size is set to (
        **width** , **height** ).
          * If **mode** is **Qt::KeepAspectRatio** ,
        the current size is scaled to a rectangle as large as possible inside (
        **width** , **height** ), preserving the aspect ratio.
          * If **mode**
        is **Qt::KeepAspectRatioByExpanding** , the current size is scaled to a
        rectangle as small as possible outside ( **width** , **height** ),
        preserving the aspect ratio.

        Example:

        **QSize**  t1(10, 12);
            t1.scale(60, 60, Qt::IgnoreAspectRatio);
        // t1 is (60, 60)

            **QSize**  t2(10, 12);
            t2.scale(60, 60,
        Qt::KeepAspectRatio);
            // t2 is (50, 60)

            **QSize**  t3(10,
        12);
            t3.scale(60, 60, Qt::KeepAspectRatioByExpanding);
            // t3 is
        (60, 72)

        **See also** **setWidth** (), **setHeight** (), and **scaled** ().
        """
        ...
    @overload
    def scale(self, w: int, h: int, mode: PySide6.QtCore.Qt.AspectRatioMode) -> None:
        """
        https://doc.qt.io/qt-6/qsize.html#scale-1

        **void QSize::scale(const QSize & size , Qt::AspectRatioMode mode )**

        This is an overloaded function.

        Scales the size to a rectangle with the given **size** , according to
        the specified **mode**.
        """
        ...
    @overload
    def scaled(
        self, s: PySide6.QtCore.QSize, mode: PySide6.QtCore.Qt.AspectRatioMode
    ) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qsize.html#scaled

        **[since 5.0] QSize QSize::scaled(int width , int height ,
        Qt::AspectRatioMode mode ) const**

        Return a size scaled to a rectangle with the given **width** and
        **height** , according to the specified **mode**.

        This function was introduced in Qt 5.0.

        **See also** **scale** ().
        """
        ...
    @overload
    def scaled(
        self, w: int, h: int, mode: PySide6.QtCore.Qt.AspectRatioMode
    ) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qsize.html#scaled-1

        **[since 5.0] QSize QSize::scaled(const QSize & s , Qt::AspectRatioMode
        mode ) const**

        This is an overloaded function.

        Return a size scaled to a rectangle with the given size **s** ,
        according to the specified **mode**.

        This function was introduced in Qt 5.0.
        """
        ...
    def setHeight(self, h: int) -> None:
        """
        https://doc.qt.io/qt-6/qsize.html#setHeight

        **void QSize::setHeight(int height )**

        Sets the height to the given **height**.

        **See also** **rheight** (), **height** (), and **setWidth** ().
        """
        ...
    def setWidth(self, w: int) -> None:
        """
        https://doc.qt.io/qt-6/qsize.html#setWidth

        **void QSize::setWidth(int width )**

        Sets the width to the given **width**.

        **See also** **rwidth** (), **width** (), and **setHeight** ().
        """
        ...
    def shrunkBy(self, m: PySide6.QtCore.QMargins) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qsize.html#shrunkBy

        **[since 5.14] QSize QSize::shrunkBy(QMargins margins ) const**

        Returns the size that results from shrinking this size by **margins**.

        This function was introduced in Qt 5.14.

        **See also** **grownBy** ().
        """
        ...
    def toTuple(self) -> object: ...
    def transpose(self) -> None:
        """
        https://doc.qt.io/qt-6/qsize.html#transpose

        **void QSize::transpose()**

        Swaps the width and height values.

        **See also** **setWidth** (), **setHeight** (), and **transposed** ().
        """
        ...
    def transposed(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qsize.html#transposed

        **[since 5.0] QSize QSize::transposed() const**

        Returns a **QSize**  with width and height swapped.

        This function was introduced in Qt 5.0.

        **See also** **transpose** ().
        """
        ...
    def width(self) -> int:
        """
        https://doc.qt.io/qt-6/qsize.html#width

        **int QSize::width() const**

        Returns the width.

        **See also** **height** () and **setWidth** ().
        """
        ...
