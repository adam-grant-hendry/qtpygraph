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

from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QGraphicsRotation(PySide6.QtWidgets.QGraphicsTransform):
    """
    https://doc.qt.io/qt-6/qgraphicsrotation.html

    **Detailed Description**

    You can provide the desired axis by assigning a **QVector3D**  to the axis
    property or by passing a member if **Qt::Axis**  to the **setAxis**
    convenience function. By default the axis is (0, 0, 1) i.e., rotation around
    the Z axis.

    The angle property, which is provided by QGraphicsRotation, now describes
    the number of degrees to rotate around this axis.

    QGraphicsRotation provides certain parameters to help control how the
    rotation should be applied.

    The origin is the point that the item is rotated around (i.e., it stays
    fixed relative to the parent as the rest of the item is rotated). By default
    the origin is **QPointF** (0, 0).

    The angle property provides the number of degrees to rotate the item
    clockwise around the origin. This value also be negative, indicating a
    counter-clockwise rotation. For animation purposes it may also be useful to
    provide rotation angles exceeding (-360, 360) degrees, for instance to
    animate how an item rotates several times.

    Note: the final rotation is the combined effect of a rotation in 3D space
    followed by a projection back to 2D. If several rotations are performed in
    succession, they will not behave as expected unless they were all around the
    Z axis.

    **See also** **QGraphicsTransform** , **QGraphicsItem::setRotation** (), and
    **QTransform::rotate** ().
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsrotation.html#QGraphicsRotation

        **QGraphicsRotation::QGraphicsRotation(QObject * parent = nullptr)**

        Constructs a new QGraphicsRotation with the given **parent**.
        """
        ...
    def angle(self) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsrotation.html#angle-prop

        **angle : qreal**

        This property holds the angle for clockwise rotation, in degrees.

        The angle can be any real number; the default value is 0.0. A value of
        180 will rotate 180 degrees, clockwise. If you provide a negative
        number, the item will be rotated counter-clockwise. Normally the
        rotation angle will be in the range (-360, 360), but you can also
        provide numbers outside of this range (e.g., a angle of 370 degrees
        gives the same result as 10 degrees). Setting the angle to NaN results
        in no rotation.

        **Access functions:**

        qreal **angle** () const
        void **setAngle** (qreal)

        **Notifier signal:**

        void ****angleChanged** ** ()

        **See also** **origin** .
        """
        ...
    def applyTo(
        self, matrix: PySide6.QtGui.QMatrix4x4 | PySide6.QtGui.QTransform
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsrotation.html#applyTo

        **[override virtual] void QGraphicsRotation::applyTo(QMatrix4x4 * matrix
        ) const**

        Reimplements: **QGraphicsTransform::applyTo(QMatrix4x4 *matrix) const**
        .
        """
        ...
    def axis(self) -> PySide6.QtGui.QVector3D:
        """
        https://doc.qt.io/qt-6/qgraphicsrotation.html#axis-prop

        **axis : QVector3D**

        This property holds a rotation axis, specified by a vector in 3D space.

        This can be any axis in 3D space. By default the axis is (0, 0, 1),
        which is aligned with the Z axis. If you provide another axis,
        **QGraphicsRotation**  will provide a transformation that rotates around
        this axis. For example, if you would like to rotate an item around its X
        axis, you could pass (1, 0, 0) as the axis.

        **Access functions:**

        QVector3D **axis** () const
        void **setAxis** (const QVector3D &
        **axis** )
        void ****setAxis** ** (Qt::Axis **axis** )

        **Notifier signal:**

        void ****axisChanged** ** ()

        **See also** **QTransform**  and **QGraphicsRotation::angle** .
        """
        ...
    def origin(self) -> PySide6.QtGui.QVector3D:
        """
        https://doc.qt.io/qt-6/qgraphicsrotation.html#origin-prop

        **origin : QVector3D**

        This property holds the origin of the rotation in 3D space.

        All rotations will be done relative to this point (i.e., this point will
        stay fixed, relative to the parent, when the item is rotated).

        **Access functions:**

        QVector3D **origin** () const
        void **setOrigin** (const QVector3D &
        **point** )

        **Notifier signal:**

        void ****originChanged** ** ()

        **See also** **angle** .

        **Member Function Documentation**
        """
        ...
    def setAngle(self, arg__1: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsrotation.html#angle-prop

        **angle : qreal**

        This property holds the angle for clockwise rotation, in degrees.

        The angle can be any real number; the default value is 0.0. A value of
        180 will rotate 180 degrees, clockwise. If you provide a negative
        number, the item will be rotated counter-clockwise. Normally the
        rotation angle will be in the range (-360, 360), but you can also
        provide numbers outside of this range (e.g., a angle of 370 degrees
        gives the same result as 10 degrees). Setting the angle to NaN results
        in no rotation.

        **Access functions:**

        qreal **angle** () const
        void **setAngle** (qreal)

        **Notifier signal:**

        void ****angleChanged** ** ()

        **See also** **origin** .
        """
        ...
    @overload
    def setAxis(self, axis: PySide6.QtCore.Qt.Axis) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsrotation.html#setAxis-1

        **void QGraphicsRotation::setAxis(Qt::Axis axis )**

        Convenience function to set the axis to **axis**.

        Note: the **Qt::YAxis**  rotation for **QTransform**  is inverted from
        the correct mathematical rotation in 3D space. The **QGraphicsRotation**
        class implements a correct mathematical rotation. The following two
        sequences of code will perform the same transformation:

        **QTransform**  t;
            t.rotate(45, Qt::YAxis);
        **QGraphicsRotation**  r;
            r.setAxis(Qt::YAxis);
            r.setAngle(-45);

        **Note:** Setter function for property **axis** .
        """
        ...
    @overload
    def setAxis(self, axis: PySide6.QtGui.QVector3D) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsrotation.html#setAxis-1

        **void QGraphicsRotation::setAxis(Qt::Axis axis )**

        Convenience function to set the axis to **axis**.

        Note: the **Qt::YAxis**  rotation for **QTransform**  is inverted from
        the correct mathematical rotation in 3D space. The **QGraphicsRotation**
        class implements a correct mathematical rotation. The following two
        sequences of code will perform the same transformation:

        **QTransform**  t;
            t.rotate(45, Qt::YAxis);
        **QGraphicsRotation**  r;
            r.setAxis(Qt::YAxis);
            r.setAngle(-45);

        **Note:** Setter function for property **axis** .
        """
        ...
    def setOrigin(self, point: PySide6.QtGui.QVector3D) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsrotation.html#origin-prop

        **origin : QVector3D**

        This property holds the origin of the rotation in 3D space.

        All rotations will be done relative to this point (i.e., this point will
        stay fixed, relative to the parent, when the item is rotated).

        **Access functions:**

        QVector3D **origin** () const
        void **setOrigin** (const QVector3D &
        **point** )

        **Notifier signal:**

        void ****originChanged** ** ()

        **See also** **angle** .

        **Member Function Documentation**
        """
        ...
    @property
    def angleChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qgraphicsrotation.html#angleChanged

        **[signal] void QGraphicsRotation::angleChanged()**

        This signal is emitted whenever the angle has changed.

        **Note:** Notifier signal for property **angle** .

        **See also** **QGraphicsRotation::angle** .
        """
        ...
    @property
    def axisChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qgraphicsrotation.html#axisChanged

        **[signal] void QGraphicsRotation::axisChanged()**

        This signal is emitted whenever the axis of the object changes.

        **Note:** Notifier signal for property **axis** .

        **See also** **QGraphicsRotation::axis** .
        """
        ...
    @property
    def originChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qgraphicsrotation.html#originChanged

        **[signal] void QGraphicsRotation::originChanged()**

        This signal is emitted whenever the origin has changed.

        **Note:** Notifier signal for property **origin** .

        **See also** **QGraphicsRotation::origin** .
        """
        ...
