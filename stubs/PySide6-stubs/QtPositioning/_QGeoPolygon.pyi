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
PySide6.QtPositioning, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from collections.abc import Sequence
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtPositioning

class QGeoPolygon(PySide6.QtPositioning.QGeoShape):
    """
    https://doc.qt.io/qt-6/qgeopolygon.html

    **Detailed Description**

    The polygon is defined by an ordered list of **QGeoCoordinate**  objects
    representing its perimeter.

    Each two adjacent elements in this list are intended to be connected
    together by the shortest line segment of constant bearing passing through
    both elements. This type of connection can cross the date line in the
    longitudinal direction, but never crosses the poles.

    This is relevant for the calculation of the bounding box returned by
    **QGeoShape::boundingGeoRectangle** () for this shape, which will have the
    latitude of the top left corner set to the maximum latitude in the path
    point set. Similarly, the latitude of the bottom right corner will be the
    minimum latitude in the path point set.

    This class is a **Q_GADGET** . It can be **directly used from C++ and QML**
    .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#QGeoPolygon

        **QGeoPolygon::QGeoPolygon()**

        Constructs a new, empty geo polygon.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoShape) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#QGeoPolygon-1

        **QGeoPolygon::QGeoPolygon(const QList<QGeoCoordinate> & path )**

        Constructs a new geo polygon from the coordinates specified in **path**.
        """
        ...
    @overload
    def __init__(
        self,
        other: (
            PySide6.QtPositioning.QGeoShape
            | Sequence[PySide6.QtPositioning.QGeoCoordinate]
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#QGeoPolygon-2

        **QGeoPolygon::QGeoPolygon(const QGeoPolygon & other )**

        Constructs a new geo polygon from the contents of **other**.
        """
        ...
    @overload
    def __init__(self, path: Sequence[PySide6.QtPositioning.QGeoCoordinate]) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#QGeoPolygon-3

        **QGeoPolygon::QGeoPolygon(const QGeoShape & other )**

        Constructs a new geo polygon from the contents of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def addCoordinate(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#addCoordinate

        **[invokable] void QGeoPolygon::addCoordinate(const QGeoCoordinate &
        coordinate )**

        Appends **coordinate** to the polygon.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    @overload
    def addHole(self, holePath: Sequence[PySide6.QtPositioning.QGeoCoordinate]) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#addHole

        **[invokable, since 5.12] void QGeoPolygon::addHole(const QVariant &
        holePath )**

        Sets the **holePath** for a hole inside the polygon. The hole is a
        **QVariant**  containing a **QList** <**QGeoCoordinate** >.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.12.
        """
        ...
    @overload
    def addHole(self, holePath: Any) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#addHole-1

        **[since 5.12] void QGeoPolygon::addHole(const QList<QGeoCoordinate> &
        holePath )**

        Overloaded method. Sets the **holePath** for a hole inside the polygon.
        The hole is a **QList** <**QGeoCoordinate** >.

        This function was introduced in Qt 5.12.
        """
        ...
    def containsCoordinate(
        self, coordinate: PySide6.QtPositioning.QGeoCoordinate
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#containsCoordinate

        **[invokable] bool QGeoPolygon::containsCoordinate(const QGeoCoordinate
        & coordinate ) const**

        Returns true if the polygon's perimeter contains **coordinate** as one
        of the elements.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def coordinateAt(self, index: int) -> PySide6.QtPositioning.QGeoCoordinate:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#coordinateAt

        **[invokable] QGeoCoordinate QGeoPolygon::coordinateAt(qsizetype index )
        const**

        Returns the coordinate at **index** .

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def hole(self, index: int) -> list[Any]:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#hole

        **[invokable, since 5.12] const QVariantList QGeoPolygon::hole(qsizetype
        index ) const**

        Returns a **QVariant**  containing a **QList** <**QGeoCoordinate** >
        which represents the hole at **index**.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.12.
        """
        ...
    def holePath(self, index: int) -> list[PySide6.QtPositioning.QGeoCoordinate]:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#holePath

        **[since 5.12] const QList<QGeoCoordinate>
        QGeoPolygon::holePath(qsizetype index ) const**

        Returns a **QList** <**QGeoCoordinate** > which represents the hole at
        **index**.

        This function was introduced in Qt 5.12.
        """
        ...
    def holesCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#holesCount

        **[invokable, since 5.12] qsizetype QGeoPolygon::holesCount() const**

        Returns the number of holes.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.12.
        """
        ...
    def insertCoordinate(
        self, index: int, coordinate: PySide6.QtPositioning.QGeoCoordinate
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#insertCoordinate

        **[invokable] void QGeoPolygon::insertCoordinate(qsizetype index , const
        QGeoCoordinate & coordinate )**

        Inserts **coordinate** at the specified **index**.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def length(self, indexFrom: int = ..., indexTo: int = ...) -> float:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#length

        **[invokable] double QGeoPolygon::length(qsizetype indexFrom = 0,
        qsizetype indexTo = -1) const**

        Returns the length of the polygon's perimeter, in meters, from the
        element **indexFrom** to the element **indexTo**. The length is intended
        to be the sum of the shortest distances for each pair of adjacent
        points.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def perimeter(self) -> list[PySide6.QtPositioning.QGeoCoordinate]:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#perimeter

        **[since QtPositioning 5.12] const QList<QGeoCoordinate>
        &QGeoPolygon::perimeter() const**

        Returns all the elements of the polygon's perimeter.

        **Note:** Getter function for property perimeter.

        This function was introduced in QtPositioning 5.12.

        **See also** **setPerimeter** ().
        """
        ...
    @overload
    def removeCoordinate(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#removeCoordinate

        **[invokable] void QGeoPolygon::removeCoordinate(const QGeoCoordinate &
        coordinate )**

        Removes the last occurrence of **coordinate** from the polygon.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    @overload
    def removeCoordinate(self, index: int) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#removeCoordinate-1

        **[invokable] void QGeoPolygon::removeCoordinate(qsizetype index )**

        Removes element at position **index** from the polygon.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def removeHole(self, index: int) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#removeHole

        **[invokable, since 5.12] void QGeoPolygon::removeHole(qsizetype index
        )**

        Removes element at position **index** from the list of holes.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.12.
        """
        ...
    def replaceCoordinate(
        self, index: int, coordinate: PySide6.QtPositioning.QGeoCoordinate
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#replaceCoordinate

        **[invokable] void QGeoPolygon::replaceCoordinate(qsizetype index ,
        const QGeoCoordinate & coordinate )**

        Replaces the path element at the specified **index** with
        **coordinate**.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def setPerimeter(self, path: Sequence[PySide6.QtPositioning.QGeoCoordinate]) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#setPerimeter

        **[since QtPositioning 5.12] void QGeoPolygon::setPerimeter(const
        QList<QGeoCoordinate> & path )**

        Sets the perimeter of the polygon based on a list of coordinates
        **path**.

        **Note:** Setter function for property **perimeter** .

        This function was introduced in QtPositioning 5.12.

        **See also** **perimeter** ().
        """
        ...
    def size(self) -> int:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#size

        **[invokable, since 5.10] qsizetype QGeoPolygon::size() const**

        Returns the number of elements in the polygon.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.10.
        """
        ...
    def toString(self) -> str:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#toString

        **[invokable] QString QGeoPolygon::toString() const**

        Returns the geo polygon properties as a string.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def translate(self, degreesLatitude: float, degreesLongitude: float) -> None:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#translate

        **[invokable] void QGeoPolygon::translate(double degreesLatitude ,
        double degreesLongitude )**

        Translates this geo polygon by **degreesLatitude** northwards and
        **degreesLongitude** eastwards.

        Negative values of **degreesLatitude** and **degreesLongitude**
        correspond to southward and westward translation respectively.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def translated(
        self, degreesLatitude: float, degreesLongitude: float
    ) -> PySide6.QtPositioning.QGeoPolygon:
        """
        https://doc.qt.io/qt-6/qgeopolygon.html#translated

        **[invokable] QGeoPolygon QGeoPolygon::translated(double degreesLatitude
        , double degreesLongitude ) const**

        Returns a copy of this geo polygon translated by **degreesLatitude**
        northwards and **degreesLongitude** eastwards.

        Negative values of **degreesLatitude** and **degreesLongitude**
        correspond to southward and westward translation respectively.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        **See also** **translate** ().
        """
        ...