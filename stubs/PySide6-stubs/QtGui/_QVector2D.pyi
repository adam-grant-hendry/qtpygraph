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

from typing import overload

import PySide6.QtCore
import PySide6.QtGui

class QVector2D:
    """
    https://doc.qt.io/qt-6/qvector2d.html

    **Detailed Description**

    Vectors are one of the main building blocks of 2D representation and
    drawing. They consist of two finite floating-point coordinates,
    traditionally called x and y.

    The QVector2D class can also be used to represent vertices in 2D space. We
    therefore do not need to provide a separate vertex class.

    **See also** **QVector3D** , **QVector4D** , and **QQuaternion** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qvector2d.html#QVector2D

        **QVector2D::QVector2D()**

        Constructs a null vector, i.e. with coordinates (0, 0).
        """
        ...
    @overload
    def __init__(self, point: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/qvector2d.html#QVector2D-2

        **QVector2D::QVector2D(float xpos , float ypos )**

        Constructs a vector with coordinates ( **xpos** , **ypos** ). Both
        coordinates must be finite.
        """
        ...
    @overload
    def __init__(
        self,
        point: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qvector2d.html#QVector2D-3

        **QVector2D::QVector2D(QPoint point )**

        Constructs a vector with x and y coordinates from a 2D **point**.
        """
        ...
    @overload
    def __init__(self, vector: PySide6.QtGui.QVector3D) -> None:
        """
        https://doc.qt.io/qt-6/qvector2d.html#QVector2D-4

        **QVector2D::QVector2D(QPointF point )**

        Constructs a vector with x and y coordinates from a 2D **point**.
        """
        ...
    @overload
    def __init__(self, vector: PySide6.QtGui.QVector4D) -> None:
        """
        https://doc.qt.io/qt-6/qvector2d.html#QVector2D-5

        **QVector2D::QVector2D(QVector3D vector )**

        Constructs a vector with x and y coordinates from a 3D **vector**. The z
        coordinate of **vector** is dropped.

        **See also** **toVector3D** ().
        """
        ...
    @overload
    def __init__(self, xpos: float, ypos: float) -> None:
        """
        https://doc.qt.io/qt-6/qvector2d.html#QVector2D-6

        **QVector2D::QVector2D(QVector4D vector )**

        Constructs a vector with x and y coordinates from a 3D **vector**. The z
        and w coordinates of **vector** are dropped.

        **See also** **toVector4D** ().
        """
        ...
    def __add__(self, v2: PySide6.QtGui.QVector2D) -> PySide6.QtGui.QVector2D: ...
    @staticmethod
    def __copy__() -> None: ...
    def __iadd__(self, vector: PySide6.QtGui.QVector2D) -> PySide6.QtGui.QVector2D: ...
    @overload
    def __imul__(self, factor: float) -> PySide6.QtGui.QVector2D: ...
    @overload
    def __imul__(self, vector: PySide6.QtGui.QVector2D) -> PySide6.QtGui.QVector2D: ...
    def __isub__(self, vector: PySide6.QtGui.QVector2D) -> PySide6.QtGui.QVector2D: ...
    def __lshift__(
        self, arg__1: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    @overload
    def __mul__(self, factor: float) -> PySide6.QtGui.QVector2D: ...
    @overload
    def __mul__(self, v2: PySide6.QtGui.QVector2D) -> PySide6.QtGui.QVector2D: ...
    def __neg__(self) -> PySide6.QtGui.QVector2D: ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def __rshift__(
        self, arg__1: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    def __sub__(self, v2: PySide6.QtGui.QVector2D) -> PySide6.QtGui.QVector2D: ...
    def distanceToLine(
        self, point: PySide6.QtGui.QVector2D, direction: PySide6.QtGui.QVector2D
    ) -> float:
        """
        https://doc.qt.io/qt-6/qvector2d.html#distanceToLine

        **[since 5.1] float QVector2D::distanceToLine(QVector2D point ,
        QVector2D direction ) const**

        Returns the distance that this vertex is from a line defined by
        **point** and the unit vector **direction**.

        If **direction** is a null vector, then it does not define a line. In
        that case, the distance from **point** to this vertex is returned.

        This function was introduced in Qt 5.1.

        **See also** **distanceToPoint** ().
        """
        ...
    def distanceToPoint(self, point: PySide6.QtGui.QVector2D) -> float:
        """
        https://doc.qt.io/qt-6/qvector2d.html#distanceToPoint

        **[since 5.1] float QVector2D::distanceToPoint(QVector2D point ) const**

        Returns the distance from this vertex to a point defined by the vertex
        **point**.

        This function was introduced in Qt 5.1.

        **See also** **distanceToLine** ().
        """
        ...
    @staticmethod
    def dotProduct(v1: PySide6.QtGui.QVector2D, v2: PySide6.QtGui.QVector2D) -> float:
        """
        https://doc.qt.io/qt-6/qvector2d.html#dotProduct

        **[static] float QVector2D::dotProduct(QVector2D v1 , QVector2D v2 )**

        Returns the dot product of **v1** and **v2**.
        """
        ...
    def isNull(self) -> bool:
        """
        https://doc.qt.io/qt-6/qvector2d.html#isNull

        **bool QVector2D::isNull() const**

        Returns `true` if the x and y coordinates are set to 0.0, otherwise
        returns `false`.
        """
        ...
    def length(self) -> float:
        """
        https://doc.qt.io/qt-6/qvector2d.html#length

        **float QVector2D::length() const**

        Returns the length of the vector from the origin.

        **See also** **lengthSquared** () and **normalized** ().
        """
        ...
    def lengthSquared(self) -> float:
        """
        https://doc.qt.io/qt-6/qvector2d.html#lengthSquared

        **float QVector2D::lengthSquared() const**

        Returns the squared length of the vector from the origin. This is
        equivalent to the dot product of the vector with itself.

        **See also** **length** () and **dotProduct** ().
        """
        ...
    def normalize(self) -> None:
        """
        https://doc.qt.io/qt-6/qvector2d.html#normalize

        **void QVector2D::normalize()**

        Normalizes the currect vector in place. Nothing happens if this vector
        is a null vector or the length of the vector is very close to 1.

        **See also** **length** () and **normalized** ().
        """
        ...
    def normalized(self) -> PySide6.QtGui.QVector2D:
        """
        https://doc.qt.io/qt-6/qvector2d.html#normalized

        **QVector2D QVector2D::normalized() const**

        Returns the normalized unit vector form of this vector.

        If this vector is null, then a null vector is returned. If the length of
        the vector is very close to 1, then the vector will be returned as-is.
        Otherwise the normalized form of the vector of length 1 will be
        returned.

        **See also** **length** () and **normalize** ().
        """
        ...
    def setX(self, x: float) -> None:
        """
        https://doc.qt.io/qt-6/qvector2d.html#setX

        **void QVector2D::setX(float x )**

        Sets the x coordinate of this point to the given finite **x**
        coordinate.

        **See also** **x** () and **setY** ().
        """
        ...
    def setY(self, y: float) -> None:
        """
        https://doc.qt.io/qt-6/qvector2d.html#setY

        **void QVector2D::setY(float y )**

        Sets the y coordinate of this point to the given finite **y**
        coordinate.

        **See also** **y** () and **setX** ().
        """
        ...
    def toPoint(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qvector2d.html#toPoint

        **QPoint QVector2D::toPoint() const**

        Returns the **QPoint**  form of this 2D vector. Each coordinate is
        rounded to the nearest integer.

        **See also** **toPointF** () and **toVector3D** ().
        """
        ...
    def toPointF(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qvector2d.html#toPointF

        **QPointF QVector2D::toPointF() const**

        Returns the **QPointF**  form of this 2D vector.

        **See also** **toPoint** () and **toVector3D** ().
        """
        ...
    def toTuple(self) -> object: ...
    def toVector3D(self) -> PySide6.QtGui.QVector3D:
        """
        https://doc.qt.io/qt-6/qvector2d.html#toVector3D

        **QVector3D QVector2D::toVector3D() const**

        Returns the 3D form of this 2D vector, with the z coordinate set to
        zero.

        **See also** **toVector4D** () and **toPoint** ().
        """
        ...
    def toVector4D(self) -> PySide6.QtGui.QVector4D:
        """
        https://doc.qt.io/qt-6/qvector2d.html#toVector4D

        **QVector4D QVector2D::toVector4D() const**

        Returns the 4D form of this 2D vector, with the z and w coordinates set
        to zero.

        **See also** **toVector3D** () and **toPoint** ().
        """
        ...
    def x(self) -> float:
        """
        https://doc.qt.io/qt-6/qvector2d.html#x

        **float QVector2D::x() const**

        Returns the x coordinate of this point.

        **See also** **setX** () and **y** ().
        """
        ...
    def y(self) -> float:
        """
        https://doc.qt.io/qt-6/qvector2d.html#y

        **float QVector2D::y() const**

        Returns the y coordinate of this point.

        **See also** **setY** () and **x** ().
        """
        ...
