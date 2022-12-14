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

from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtPositioning

class QGeoShape:
    """
    https://doc.qt.io/qt-6/qgeoshape.html

    **Detailed Description**

    This class is the base class for classes which specify a geographic area.

    For the sake of consistency, subclasses should describe the specific details
    of the associated areas in terms of **QGeoCoordinate**  instances and
    distances in meters.

    This class is a **Q_GADGET**  since Qt 5.5. It can be **directly used from
    C++ and QML** .
    """

    UnknownType: QGeoShape.ShapeType = ...
    RectangleType: QGeoShape.ShapeType = ...
    CircleType: QGeoShape.ShapeType = ...
    PathType: QGeoShape.ShapeType = ...
    PolygonType: QGeoShape.ShapeType = ...

    class ShapeType(IntFlag):
        UnknownType: QGeoShape.ShapeType = ...
        RectangleType: QGeoShape.ShapeType = ...
        CircleType: QGeoShape.ShapeType = ...
        PathType: QGeoShape.ShapeType = ...
        PolygonType: QGeoShape.ShapeType = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qgeoshape.html#QGeoShape

        **QGeoShape::QGeoShape()**

        Constructs a new invalid geo shape of **UnknownType** .
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtPositioning.QGeoShape) -> None:
        """
        https://doc.qt.io/qt-6/qgeoshape.html#QGeoShape-1

        **QGeoShape::QGeoShape(const QGeoShape & other )**

        Constructs a new geo shape which is a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(
        self, stream: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(
        self, stream: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    def boundingGeoRectangle(self) -> PySide6.QtPositioning.QGeoRectangle:
        """
        https://doc.qt.io/qt-6/qgeoshape.html#boundingGeoRectangle

        **[invokable, since 5.9] QGeoRectangle QGeoShape::boundingGeoRectangle()
        const**

        Returns a **QGeoRectangle**  representing the geographical bounding
        rectangle of the geo shape, that defines the latitudinal/longitudinal
        bounds of the geo shape.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.9.
        """
        ...
    def center(self) -> PySide6.QtPositioning.QGeoCoordinate:
        """
        https://doc.qt.io/qt-6/qgeoshape.html#center

        **[since 5.5] QGeoCoordinate QGeoShape::center() const**

        Returns the coordinate located at the geometric center of the geo shape.

        **Note:** Getter function for property **center** .

        This function was introduced in Qt 5.5.
        """
        ...
    def contains(self, coordinate: PySide6.QtPositioning.QGeoCoordinate) -> bool:
        """
        https://doc.qt.io/qt-6/qgeoshape.html#contains

        **[invokable] bool QGeoShape::contains(const QGeoCoordinate & coordinate
        ) const**

        Returns whether the coordinate **coordinate** is contained within this
        geo shape.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def isEmpty(self) -> bool:
        """
        https://doc.qt.io/qt-6/qgeoshape.html#isEmpty

        **bool QGeoShape::isEmpty() const**

        Returns whether this geo shape is empty.

        An empty geo shape is a region which has a geometrical area of 0.

        **Note:** Getter function for property **isEmpty** .
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qgeoshape.html#isValid

        **bool QGeoShape::isValid() const**

        Returns whether this geo shape is valid.

        **Note:** Getter function for property **isValid** .
        """
        ...
    def toString(self) -> str:
        """
        https://doc.qt.io/qt-6/qgeoshape.html#toString

        **[invokable, since 5.5] QString QGeoShape::toString() const**

        Returns a string representation of this geo shape.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.5.
        """
        ...
    def type(self) -> PySide6.QtPositioning.QGeoShape.ShapeType:
        """
        https://doc.qt.io/qt-6/qgeoshape.html#type

        **QGeoShape::ShapeType QGeoShape::type() const**

        Returns the type of this geo shape.

        **Note:** Getter function for property **type** .
        """
        ...
