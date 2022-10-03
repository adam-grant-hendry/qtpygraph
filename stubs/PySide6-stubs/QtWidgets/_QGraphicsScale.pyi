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

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QGraphicsScale(PySide6.QtWidgets.QGraphicsTransform):
    """
    https://doc.qt.io/qt-6/qgraphicsscale.html

    **Detailed Description**

    **QGraphicsScene**  provides certain parameters to help control how the
    scale should be applied.

    The origin is the point that the item is scaled from (i.e., it stays fixed
    relative to the parent as the rest of the item grows). By default the origin
    is **QPointF** (0, 0).

    The parameters **xScale** , **yScale** , and **zScale**  describe the scale
    factors to apply in horizontal, vertical, and depth directions. They can
    take on any value, including 0 (to collapse the item to a point) or negative
    value. A negative **xScale**  value will mirror the item horizontally. A
    negative **yScale**  value will flip the item vertically. A negative
    **zScale**  will flip the item end for end.

    **See also** **QGraphicsTransform** , **QGraphicsItem::setScale** (), and
    **QTransform::scale** ().
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#QGraphicsScale

        **QGraphicsScale::QGraphicsScale(QObject * parent = nullptr)**

        Constructs an empty QGraphicsScale object with the given **parent**.
        """
        ...
    def applyTo(
        self, matrix: PySide6.QtGui.QMatrix4x4 | PySide6.QtGui.QTransform
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#applyTo

        **[override virtual] void QGraphicsScale::applyTo(QMatrix4x4 * matrix )
        const**

        Reimplements: **QGraphicsTransform::applyTo(QMatrix4x4 *matrix) const**
        .
        """
        ...
    def origin(self) -> PySide6.QtGui.QVector3D:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#origin-prop

        **origin : QVector3D**

        This property holds the origin of the scale in 3D space.

        All scaling will be done relative to this point (i.e., this point will
        stay fixed, relative to the parent, when the item is scaled).

        **Access functions:**

        QVector3D **origin** () const
        void **setOrigin** (const QVector3D &
        **point** )

        **Notifier signal:**

        void ****originChanged** ** ()

        **See also** **xScale** , **yScale** , and **zScale** .
        """
        ...
    def setOrigin(self, point: PySide6.QtGui.QVector3D) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#origin-prop

        **origin : QVector3D**

        This property holds the origin of the scale in 3D space.

        All scaling will be done relative to this point (i.e., this point will
        stay fixed, relative to the parent, when the item is scaled).

        **Access functions:**

        QVector3D **origin** () const
        void **setOrigin** (const QVector3D &
        **point** )

        **Notifier signal:**

        void ****originChanged** ** ()

        **See also** **xScale** , **yScale** , and **zScale** .
        """
        ...
    def setXScale(self, arg__1: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#xScale-prop

        **xScale : qreal**

        This property holds the horizontal scale factor.

        The scale factor can be any real number; the default value is 1.0. If
        you set the factor to 0.0, the item will be collapsed to a single point.
        If you provide a negative value, the item will be mirrored horizontally
        around its origin.

        **Access functions:**

        qreal **xScale** () const
        void **setXScale** (qreal)

        **Notifier signal:**

        void ****xScaleChanged** ** ()

        **See also** **yScale** , **zScale** , and **origin** .
        """
        ...
    def setYScale(self, arg__1: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#yScale-prop

        **yScale : qreal**

        This property holds the vertical scale factor.

        The scale factor can be any real number; the default value is 1.0. If
        you set the factor to 0.0, the item will be collapsed to a single point.
        If you provide a negative value, the item will be flipped vertically
        around its origin.

        **Access functions:**

        qreal **yScale** () const
        void **setYScale** (qreal)

        **Notifier signal:**

        void ****yScaleChanged** ** ()

        **See also** **xScale** , **zScale** , and **origin** .
        """
        ...
    def setZScale(self, arg__1: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#zScale-prop

        **zScale : qreal**

        This property holds the depth scale factor.

        The scale factor can be any real number; the default value is 1.0. If
        you set the factor to 0.0, the item will be collapsed to a single point.
        If you provide a negative value, the item will be flipped end for end
        around its origin.

        **Access functions:**

        qreal **zScale** () const
        void **setZScale** (qreal)

        **Notifier signal:**

        void ****zScaleChanged** ** ()

        **See also** **xScale** , **yScale** , and **origin** .

        **Member Function Documentation**
        """
        ...
    def xScale(self) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#xScale-prop

        **xScale : qreal**

        This property holds the horizontal scale factor.

        The scale factor can be any real number; the default value is 1.0. If
        you set the factor to 0.0, the item will be collapsed to a single point.
        If you provide a negative value, the item will be mirrored horizontally
        around its origin.

        **Access functions:**

        qreal **xScale** () const
        void **setXScale** (qreal)

        **Notifier signal:**

        void ****xScaleChanged** ** ()

        **See also** **yScale** , **zScale** , and **origin** .
        """
        ...
    def yScale(self) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#yScale-prop

        **yScale : qreal**

        This property holds the vertical scale factor.

        The scale factor can be any real number; the default value is 1.0. If
        you set the factor to 0.0, the item will be collapsed to a single point.
        If you provide a negative value, the item will be flipped vertically
        around its origin.

        **Access functions:**

        qreal **yScale** () const
        void **setYScale** (qreal)

        **Notifier signal:**

        void ****yScaleChanged** ** ()

        **See also** **xScale** , **zScale** , and **origin** .
        """
        ...
    def zScale(self) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#zScale-prop

        **zScale : qreal**

        This property holds the depth scale factor.

        The scale factor can be any real number; the default value is 1.0. If
        you set the factor to 0.0, the item will be collapsed to a single point.
        If you provide a negative value, the item will be flipped end for end
        around its origin.

        **Access functions:**

        qreal **zScale** () const
        void **setZScale** (qreal)

        **Notifier signal:**

        void ****zScaleChanged** ** ()

        **See also** **xScale** , **yScale** , and **origin** .

        **Member Function Documentation**
        """
        ...
    @property
    def originChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#originChanged

        **[signal] void QGraphicsScale::originChanged()**

        **QGraphicsScale**  emits this signal when its origin changes.

        **Note:** Notifier signal for property **origin** .

        **See also** **QGraphicsScale::origin** .
        """
        ...
    @property
    def scaleChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#scaleChanged

        **[signal] void QGraphicsScale::scaleChanged()**

        This signal is emitted whenever the **xScale** , **yScale** , or
        **zScale**  of the object changes.

        **See also** **QGraphicsScale::xScale** , **QGraphicsScale::yScale** ,
        and **QGraphicsScale::zScale** .
        """
        ...
    @property
    def xScaleChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#xScaleChanged

        **[signal] void QGraphicsScale::xScaleChanged()**

        This signal is emitted whenever the **xScale**  property changes.

        **Note:** Notifier signal for property **xScale** .
        """
        ...
    @property
    def yScaleChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#yScaleChanged

        **[signal] void QGraphicsScale::yScaleChanged()**

        This signal is emitted whenever the **yScale**  property changes.

        **Note:** Notifier signal for property **yScale** .
        """
        ...
    @property
    def zScaleChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qgraphicsscale.html#zScaleChanged

        **[signal] void QGraphicsScale::zScaleChanged()**

        This signal is emitted whenever the **zScale**  property changes.

        **Note:** Notifier signal for property **zScale** .
        """
        ...