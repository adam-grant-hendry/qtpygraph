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

from collections.abc import Sequence
from typing import overload

import PySide6.QtCore
import PySide6.QtGui

class QPolygon:
    """
    https://doc.qt.io/qt-6/qpolygon.html

    **Detailed Description**

    A QPolygon object is a **QList** <**QPoint** >. The easiest way to add
    points to a QPolygon is to use **QList** 's streaming operator, as
    illustrated below:

    **QPolygon**  polygon;
        polygon << **QPoint** (10, 20) << **QPoint** (20,
    30);

    In addition to the functions provided by **QList** , QPolygon provides some
    point-specific functions.

    Each point in a polygon can be retrieved by passing its index to the
    **point** () function. To populate the polygon, QPolygon provides the
    **setPoint** () function to set the point at a given index, the
    **setPoints** () function to set all the points in the polygon (resizing it
    to the given number of points), and the **putPoints** () function which
    copies a number of given points into the polygon from a specified index
    (resizing the polygon if necessary).

    QPolygon provides the **boundingRect** () and **translate** () functions for
    geometry functions. Use the **QTransform::map** () function for more general
    transformations of QPolygons.

    The QPolygon class is **implicitly shared** .

    **See also** **QList** , **QPolygonF** , and **QLine** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qpolygon.html#QPolygon

        **QPolygon::QPolygon()**

        Constructs a polygon with no points.

        **See also** **QList::isEmpty** ().
        """
        ...
    @overload
    def __init__(
        self,
        QPolygon: (
            PySide6.QtGui.QPolygon
            | Sequence[PySide6.QtCore.QPoint]
            | PySide6.QtCore.QRect
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpolygon.html#QPolygon-1

        **QPolygon::QPolygon(const QList<QPoint> & points )**

        Constructs a polygon containing the specified **points**.

        **See also** **setPoints** ().
        """
        ...
    @overload
    def __init__(self, r: PySide6.QtCore.QRect, closed: bool = ...) -> None:
        """
        https://doc.qt.io/qt-6/qpolygon.html#QPolygon-3

        **QPolygon::QPolygon(const QRect & rectangle , bool closed = false)**

        Constructs a polygon from the given **rectangle**. If **closed** is
        false, the polygon just contains the four points of the rectangle
        ordered clockwise, otherwise the polygon's fifth point is set to
        **rectangle**.topLeft().

        Note that the bottom-right corner of the rectangle is located at
        (rectangle.x() + rectangle.width(), rectangle.y() + rectangle.height()).

        **See also** **setPoints** ().
        """
        ...
    @overload
    def __init__(self, v: Sequence[PySide6.QtCore.QPoint]) -> None:
        """
        https://doc.qt.io/qt-6/qpolygon.html#QPolygon

        **QPolygon::QPolygon()**

        Constructs a polygon with no points.

        **See also** **QList::isEmpty** ().
        """
        ...
    def __add__(
        self, l: Sequence[PySide6.QtCore.QPoint]
    ) -> list[PySide6.QtCore.QPoint]: ...
    @staticmethod
    def __copy__() -> None: ...
    @overload
    def __lshift__(self, arg__1: PySide6.QtCore.QPoint) -> None: ...
    @overload
    def __lshift__(self, arg__1: Sequence[PySide6.QtCore.QPoint]) -> None: ...
    @overload
    def __lshift__(
        self, stream: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    def __mul__(self, m: PySide6.QtGui.QTransform) -> PySide6.QtGui.QPolygon: ...
    def __reduce__(self) -> object: ...
    def __rshift__(
        self, stream: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    @overload
    def append(self, arg__1: PySide6.QtCore.QPoint) -> None: ...
    @overload
    def append(self, l: Sequence[PySide6.QtCore.QPoint]) -> None: ...
    def at(self, i: int) -> PySide6.QtCore.QPoint: ...
    def back(self) -> PySide6.QtCore.QPoint: ...
    def boundingRect(self) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/qpolygon.html#boundingRect

        **QRect QPolygon::boundingRect() const**

        Returns the bounding rectangle of the polygon, or **QRect** (0, 0, 0, 0)
        if the polygon is empty.

        **See also** **QList::isEmpty** ().
        """
        ...
    def capacity(self) -> int: ...
    def clear(self) -> None: ...
    def constData(self) -> PySide6.QtCore.QPoint: ...
    def constFirst(self) -> PySide6.QtCore.QPoint: ...
    def constLast(self) -> PySide6.QtCore.QPoint: ...
    def containsPoint(
        self, pt: PySide6.QtCore.QPoint, fillRule: PySide6.QtCore.Qt.FillRule
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qpolygon.html#containsPoint

        **bool QPolygon::containsPoint(const QPoint & point , Qt::FillRule
        fillRule ) const**

        Returns `true` if the given **point** is inside the polygon according to
        the specified **fillRule** ; otherwise returns `false`.
        """
        ...
    def count(self) -> int: ...
    def data(self) -> PySide6.QtCore.QPoint: ...
    def empty(self) -> bool: ...
    @overload
    def first(self) -> PySide6.QtCore.QPoint: ...
    @overload
    def first(self, n: int) -> list[PySide6.QtCore.QPoint]: ...
    @staticmethod
    def fromList(
        list: Sequence[PySide6.QtCore.QPoint],
    ) -> list[PySide6.QtCore.QPoint]: ...
    @staticmethod
    def fromVector(
        vector: Sequence[PySide6.QtCore.QPoint],
    ) -> list[PySide6.QtCore.QPoint]: ...
    def front(self) -> PySide6.QtCore.QPoint: ...
    def insert(self, arg__1: int, arg__2: PySide6.QtCore.QPoint) -> None: ...
    def intersected(
        self,
        r: (
            PySide6.QtGui.QPolygon
            | Sequence[PySide6.QtCore.QPoint]
            | PySide6.QtCore.QRect
        ),
    ) -> PySide6.QtGui.QPolygon:
        """
        https://doc.qt.io/qt-6/qpolygon.html#intersected

        **QPolygon QPolygon::intersected(const QPolygon & r ) const**

        Returns a polygon which is the intersection of this polygon and **r**.

        Set operations on polygons will treat the polygons as areas. Non-closed
        polygons will be treated as implicitly closed.

        **See also** **intersects** ().
        """
        ...
    def intersects(
        self,
        r: (
            PySide6.QtGui.QPolygon
            | Sequence[PySide6.QtCore.QPoint]
            | PySide6.QtCore.QRect
        ),
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qpolygon.html#intersects

        **[since 5.10] bool QPolygon::intersects(const QPolygon & p ) const**

        Returns `true` if the current polygon intersects at any point the given
        polygon **p**. Also returns `true` if the current polygon contains or is
        contained by any part of **p**.

        Set operations on polygons will treat the polygons as areas. Non-closed
        polygons will be treated as implicitly closed.

        This function was introduced in Qt 5.10.

        **See also** **intersected** ().
        """
        ...
    def isEmpty(self) -> bool: ...
    def isSharedWith(self, other: Sequence[PySide6.QtCore.QPoint]) -> bool: ...
    @overload
    def last(self) -> PySide6.QtCore.QPoint: ...
    @overload
    def last(self, n: int) -> list[PySide6.QtCore.QPoint]: ...
    def length(self) -> int: ...
    def mid(self, pos: int, len: int = ...) -> list[PySide6.QtCore.QPoint]: ...
    def move(self, from_: int, to: int) -> None: ...
    def pop_back(self) -> None: ...
    def pop_front(self) -> None: ...
    def prepend(self, arg__1: PySide6.QtCore.QPoint) -> None: ...
    def push_back(self, arg__1: PySide6.QtCore.QPoint) -> None: ...
    def push_front(self, arg__1: PySide6.QtCore.QPoint) -> None: ...
    def remove(self, i: int, n: int = ...) -> None: ...
    def removeAll(self, arg__1: PySide6.QtCore.QPoint) -> None: ...
    def removeAt(self, i: int) -> None: ...
    def removeFirst(self) -> None: ...
    def removeLast(self) -> None: ...
    def removeOne(self, arg__1: PySide6.QtCore.QPoint) -> None: ...
    def reserve(self, size: int) -> None: ...
    def resize(self, size: int) -> None: ...
    def shrink_to_fit(self) -> None: ...
    def size(self) -> int: ...
    @overload
    def sliced(self, pos: int) -> list[PySide6.QtCore.QPoint]: ...
    @overload
    def sliced(self, pos: int, n: int) -> list[PySide6.QtCore.QPoint]: ...
    def squeeze(self) -> None: ...
    def subtracted(
        self,
        r: (
            PySide6.QtGui.QPolygon
            | Sequence[PySide6.QtCore.QPoint]
            | PySide6.QtCore.QRect
        ),
    ) -> PySide6.QtGui.QPolygon:
        """
        https://doc.qt.io/qt-6/qpolygon.html#subtracted

        **QPolygon QPolygon::subtracted(const QPolygon & r ) const**

        Returns a polygon which is **r** subtracted from this polygon.

        Set operations on polygons will treat the polygons as areas. Non-closed
        polygons will be treated as implicitly closed.
        """
        ...
    def swap(
        self,
        other: (
            PySide6.QtGui.QPolygon
            | Sequence[PySide6.QtCore.QPoint]
            | PySide6.QtCore.QRect
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpolygon.html#swap

        **void QPolygon::swap(QPolygon & other )**

        Swaps polygon **other** with this polygon. This operation is very fast
        and never fails.
        """
        ...
    def swapItemsAt(self, i: int, j: int) -> None: ...
    def takeAt(self, i: int) -> PySide6.QtCore.QPoint: ...
    def toList(self) -> list[PySide6.QtCore.QPoint]: ...
    def toVector(self) -> list[PySide6.QtCore.QPoint]: ...
    @overload
    def translate(self, dx: int, dy: int) -> None:
        """
        https://doc.qt.io/qt-6/qpolygon.html#translate

        **void QPolygon::translate(int dx , int dy )**

        Translates all points in the polygon by ( **dx** , **dy** ).

        **See also** **translated** ().
        """
        ...
    @overload
    def translate(self, offset: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/qpolygon.html#translate-1

        **void QPolygon::translate(const QPoint & offset )**

        This is an overloaded function.

        Translates all points in the polygon by the given **offset**.

        **See also** **translated** ().
        """
        ...
    @overload
    def translated(self, dx: int, dy: int) -> PySide6.QtGui.QPolygon:
        """
        https://doc.qt.io/qt-6/qpolygon.html#translated

        **QPolygon QPolygon::translated(int dx , int dy ) const**

        Returns a copy of the polygon that is translated by ( **dx** , **dy** ).

        **See also** **translate** ().
        """
        ...
    @overload
    def translated(self, offset: PySide6.QtCore.QPoint) -> PySide6.QtGui.QPolygon:
        """
        https://doc.qt.io/qt-6/qpolygon.html#translated-1

        **QPolygon QPolygon::translated(const QPoint & offset ) const**

        This is an overloaded function.

        Returns a copy of the polygon that is translated by the given
        **offset**.

        **See also** **translate** ().
        """
        ...
    def united(
        self,
        r: (
            PySide6.QtGui.QPolygon
            | Sequence[PySide6.QtCore.QPoint]
            | PySide6.QtCore.QRect
        ),
    ) -> PySide6.QtGui.QPolygon:
        """
        https://doc.qt.io/qt-6/qpolygon.html#united

        **QPolygon QPolygon::united(const QPolygon & r ) const**

        Returns a polygon which is the union of this polygon and **r**.

        Set operations on polygons, will treat the polygons as areas, and
        implicitly close the polygon.

        **See also** **intersected** () and **subtracted** ().
        """
        ...
    def value(self, i: int) -> PySide6.QtCore.QPoint: ...
