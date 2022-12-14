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

from typing import Any, overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QGraphicsRectItem(PySide6.QtWidgets.QAbstractGraphicsShapeItem):
    """
    https://doc.qt.io/qt-6/qgraphicsrectitem.html

    **Detailed Description**

    To set the item's rectangle, pass a **QRectF**  to QGraphicsRectItem's
    constructor, or call the **setRect** () function. The **rect** () function
    returns the current rectangle.

    ![](images/graphicsview-rectitem.png)

    QGraphicsRectItem uses the rectangle and the pen width to provide a
    reasonable implementation of **boundingRect** (), **shape** (), and
    **contains** (). The **paint** () function draws the rectangle using the
    item's associated pen and brush, which you can set by calling the **setPen**
    () and **setBrush** () functions.

    **Note:** The rendering of invalid rectangles, such as those with negative
    widths or heights, is undefined. If you cannot be sure that you are using
    valid rectangles (for example, if you are creating rectangles using data
    from an unreliable source) then you should use **QRectF::normalized** () to
    create normalized rectangles, and use those instead.

    **See also** **QGraphicsPathItem** , **QGraphicsEllipseItem** ,
    **QGraphicsPolygonItem** , **QGraphicsTextItem** , **QGraphicsLineItem** ,
    **QGraphicsPixmapItem** , and **Graphics View Framework** .
    """

    @overload
    def __init__(self, parent: PySide6.QtWidgets.QGraphicsItem | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#QGraphicsRectItem

        **QGraphicsRectItem::QGraphicsRectItem(QGraphicsItem * parent =
        nullptr)**

        Constructs a QGraphicsRectItem. **parent** is passed to
        **QAbstractGraphicsShapeItem** 's constructor.

        **See also** **QGraphicsScene::addItem** ().
        """
        ...
    @overload
    def __init__(
        self,
        rect: PySide6.QtCore.QRectF | PySide6.QtCore.QRect,
        parent: PySide6.QtWidgets.QGraphicsItem | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#QGraphicsRectItem-1

        **QGraphicsRectItem::QGraphicsRectItem(const QRectF & rect ,
        QGraphicsItem * parent = nullptr)**

        Constructs a QGraphicsRectItem, using **rect** as the default rectangle.
        **parent** is passed to **QAbstractGraphicsShapeItem** 's constructor.

        **See also** **QGraphicsScene::addItem** ().
        """
        ...
    @overload
    def __init__(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        parent: PySide6.QtWidgets.QGraphicsItem | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#QGraphicsRectItem-2

        **QGraphicsRectItem::QGraphicsRectItem(qreal x , qreal y , qreal width ,
        qreal height , QGraphicsItem * parent = nullptr)**

        Constructs a QGraphicsRectItem with a default rectangle defined by (
        **x** , **y** ) and the given **width** and **height**.

        **parent** is passed to **QAbstractGraphicsShapeItem** 's constructor.

        **See also** **QGraphicsScene::addItem** ().
        """
        ...
    def boundingRect(self) -> PySide6.QtCore.QRectF:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#boundingRect

        **[override virtual] QRectF QGraphicsRectItem::boundingRect() const**

        Reimplements: **QGraphicsItem::boundingRect() const** .
        """
        ...
    def contains(
        self,
        point: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#contains

        **[override virtual] bool QGraphicsRectItem::contains(const QPointF &
        point ) const**

        Reimplements: **QGraphicsItem::contains(const QPointF &point) const** .
        """
        ...
    def extension(self, variant: Any) -> Any: ...
    def isObscuredBy(self, item: PySide6.QtWidgets.QGraphicsItem) -> bool:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#isObscuredBy

        **[override virtual] bool QGraphicsRectItem::isObscuredBy(const
        QGraphicsItem * item ) const**

        Reimplements: **QAbstractGraphicsShapeItem::isObscuredBy(const
        QGraphicsItem *item) const** .
        """
        ...
    def opaqueArea(self) -> PySide6.QtGui.QPainterPath:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#opaqueArea

        **[override virtual] QPainterPath QGraphicsRectItem::opaqueArea()
        const**

        Reimplements: **QAbstractGraphicsShapeItem::opaqueArea() const** .
        """
        ...
    def paint(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionGraphicsItem,
        widget: PySide6.QtWidgets.QWidget | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#paint

        **[override virtual] void QGraphicsRectItem::paint(QPainter * painter ,
        const QStyleOptionGraphicsItem * option , QWidget * widget = nullptr)**

        Reimplements: **QGraphicsItem::paint** (QPainter *painter, const
        QStyleOptionGraphicsItem *option, QWidget *widget).
        """
        ...
    def rect(self) -> PySide6.QtCore.QRectF:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#rect

        **QRectF QGraphicsRectItem::rect() const**

        Returns the item's rectangle.

        **See also** **setRect** ().
        """
        ...
    @overload
    def setRect(self, rect: PySide6.QtCore.QRectF | PySide6.QtCore.QRect) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#setRect

        **void QGraphicsRectItem::setRect(const QRectF & rectangle )**

        Sets the item's rectangle to be the given **rectangle**.

        **See also** **rect** ().
        """
        ...
    @overload
    def setRect(self, x: float, y: float, w: float, h: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#setRect-1

        **void QGraphicsRectItem::setRect(qreal x , qreal y , qreal width ,
        qreal height )**

        Sets the item's rectangle to the rectangle defined by ( **x** , **y** )
        and the given **width** and **height**.

        This convenience function is equivalent to calling `setRect(QRectF(x, y,
        width, height))`

        **See also** **rect** ().
        """
        ...
    def shape(self) -> PySide6.QtGui.QPainterPath:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#shape

        **[override virtual] QPainterPath QGraphicsRectItem::shape() const**

        Reimplements: **QGraphicsItem::shape() const** .
        """
        ...
    def type(self) -> int:
        """
        https://doc.qt.io/qt-6/qgraphicsrectitem.html#type

        **[override virtual] int QGraphicsRectItem::type() const**

        Reimplements: **QGraphicsItem::type() const** .
        """
        ...
