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

class QGraphicsLineItem(PySide6.QtWidgets.QGraphicsItem):
    """
    https://doc.qt.io/qt-6/qgraphicslineitem.html

    **Detailed Description**

    To set the item's line, pass a **QLineF**  to QGraphicsLineItem's
    constructor, or call the **setLine** () function. The **line** () function
    returns the current line. By default the line is black with a width of 0,
    but you can change this by calling **setPen** ().

    ![](images/graphicsview-lineitem.png)

    QGraphicsLineItem uses the line and the pen width to provide a reasonable
    implementation of **boundingRect** (), **shape** (), and **contains** ().
    The **paint** () function draws the line using the item's associated pen.

    **See also** **QGraphicsPathItem** , **QGraphicsRectItem** ,
    **QGraphicsEllipseItem** , **QGraphicsTextItem** , **QGraphicsPolygonItem**
    , **QGraphicsPixmapItem** , and **Graphics View Framework** .
    """

    @overload
    def __init__(
        self,
        line: PySide6.QtCore.QLineF | PySide6.QtCore.QLine,
        parent: PySide6.QtWidgets.QGraphicsItem | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#QGraphicsLineItem

        **QGraphicsLineItem::QGraphicsLineItem(QGraphicsItem * parent =
        nullptr)**

        Constructs a QGraphicsLineItem. **parent** is passed to
        **QGraphicsItem** 's constructor.

        **See also** **QGraphicsScene::addItem** ().
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtWidgets.QGraphicsItem | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#QGraphicsLineItem-1

        **QGraphicsLineItem::QGraphicsLineItem(const QLineF & line ,
        QGraphicsItem * parent = nullptr)**

        Constructs a QGraphicsLineItem, using **line** as the default line.
        **parent** is passed to **QGraphicsItem** 's constructor.

        **See also** **QGraphicsScene::addItem** ().
        """
        ...
    @overload
    def __init__(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        parent: PySide6.QtWidgets.QGraphicsItem | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#QGraphicsLineItem-2

        **QGraphicsLineItem::QGraphicsLineItem(qreal x1 , qreal y1 , qreal x2 ,
        qreal y2 , QGraphicsItem * parent = nullptr)**

        Constructs a QGraphicsLineItem, using the line between ( **x1** , **y1**
        ) and ( **x2** , **y2** ) as the default line. **parent** is passed to
        **QGraphicsItem** 's constructor.

        **See also** **QGraphicsScene::addItem** ().
        """
        ...
    def boundingRect(self) -> PySide6.QtCore.QRectF:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#boundingRect

        **[override virtual] QRectF QGraphicsLineItem::boundingRect() const**

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
        https://doc.qt.io/qt-6/qgraphicslineitem.html#contains

        **[override virtual] bool QGraphicsLineItem::contains(const QPointF &
        point ) const**

        Reimplements: **QGraphicsItem::contains(const QPointF &point) const** .
        """
        ...
    def extension(self, variant: Any) -> Any: ...
    def isObscuredBy(self, item: PySide6.QtWidgets.QGraphicsItem) -> bool:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#isObscuredBy

        **[override virtual] bool QGraphicsLineItem::isObscuredBy(const
        QGraphicsItem * item ) const**

        Reimplements: **QGraphicsItem::isObscuredBy(const QGraphicsItem *item)
        const** .
        """
        ...
    def line(self) -> PySide6.QtCore.QLineF:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#line

        **QLineF QGraphicsLineItem::line() const**

        Returns the item's line, or a null line if no line has been set.

        **See also** **setLine** ().
        """
        ...
    def opaqueArea(self) -> PySide6.QtGui.QPainterPath:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#opaqueArea

        **[override virtual] QPainterPath QGraphicsLineItem::opaqueArea()
        const**

        Reimplements: **QGraphicsItem::opaqueArea() const** .
        """
        ...
    def paint(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionGraphicsItem,
        widget: PySide6.QtWidgets.QWidget | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#paint

        **[override virtual] void QGraphicsLineItem::paint(QPainter * painter ,
        const QStyleOptionGraphicsItem * option , QWidget * widget = nullptr)**

        Reimplements: **QGraphicsItem::paint** (QPainter *painter, const
        QStyleOptionGraphicsItem *option, QWidget *widget).
        """
        ...
    def pen(self) -> PySide6.QtGui.QPen:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#pen

        **QPen QGraphicsLineItem::pen() const**

        Returns the item's pen, or a black solid 0-width pen if no pen has been
        set.

        **See also** **setPen** ().
        """
        ...
    @overload
    def setLine(self, line: PySide6.QtCore.QLineF | PySide6.QtCore.QLine) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#setLine

        **void QGraphicsLineItem::setLine(const QLineF & line )**

        Sets the item's line to be the given **line**.

        **See also** **line** ().
        """
        ...
    @overload
    def setLine(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#setLine-1

        **void QGraphicsLineItem::setLine(qreal x1 , qreal y1 , qreal x2 , qreal
        y2 )**

        This is an overloaded function.

        Sets the item's line to be the line between ( **x1** , **y1** ) and (
        **x2** , **y2** ).

        This is the same as calling `setLine(QLineF(x1, y1, x2, y2))`.
        """
        ...
    def setPen(
        self,
        pen: PySide6.QtGui.QPen | PySide6.QtCore.Qt.PenStyle | PySide6.QtGui.QColor,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#setPen

        **void QGraphicsLineItem::setPen(const QPen & pen )**

        Sets the item's pen to **pen**. If no pen is set, the line will be
        painted using a black solid 0-width pen.

        **See also** **pen** ().
        """
        ...
    def shape(self) -> PySide6.QtGui.QPainterPath:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#shape

        **[override virtual] QPainterPath QGraphicsLineItem::shape() const**

        Reimplements: **QGraphicsItem::shape() const** .
        """
        ...
    def type(self) -> int:
        """
        https://doc.qt.io/qt-6/qgraphicslineitem.html#type

        **[override virtual] int QGraphicsLineItem::type() const**

        Reimplements: **QGraphicsItem::type() const** .
        """
        ...
