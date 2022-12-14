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

class QGraphicsSceneHoverEvent(PySide6.QtWidgets.QGraphicsSceneEvent):
    """
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html

    **Detailed Description**

    When a **QGraphicsView**  receives a **QHoverEvent**  event, it translates
    it into QGraphicsSceneHoverEvent. The event is then forwarded to the
    **QGraphicsScene**  associated with the view.

    **See also** **QGraphicsSceneMouseEvent** ,
    **QGraphicsSceneContextMenuEvent** , **QGraphicsSceneWheelEvent** , and
    **QHoverEvent** .
    """

    def __init__(self, type: PySide6.QtCore.QEvent.Type | None = ...) -> None: ...
    def lastPos(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#lastPos

        **QPointF QGraphicsSceneHoverEvent::lastPos() const**

        Returns the last recorded mouse cursor position in item coordinates.

        **See also** **lastScenePos** (), **lastScreenPos** (), and **pos** ().
        """
        ...
    def lastScenePos(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#lastScenePos

        **QPointF QGraphicsSceneHoverEvent::lastScenePos() const**

        Returns the last recorded, the scene coordinates of the previous mouse
        or hover event received by the view, that created the event mouse cursor
        position in scene coordinates.

        **See also** **lastPos** (), **lastScreenPos** (), and **scenePos** ().
        """
        ...
    def lastScreenPos(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#lastScreenPos

        **QPoint QGraphicsSceneHoverEvent::lastScreenPos() const**

        Returns the last recorded mouse cursor position in screen coordinates.
        The last recorded position is the position of the previous mouse or
        hover event received by the view that created the event.

        **See also** **lastPos** (), **lastScenePos** (), and **screenPos** ().
        """
        ...
    def modifiers(self) -> PySide6.QtCore.Qt.KeyboardModifiers:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#modifiers

        **Qt::KeyboardModifiers QGraphicsSceneHoverEvent::modifiers() const**

        Returns the keyboard modifiers at the moment the hover event was sent.
        """
        ...
    def pos(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#pos

        **QPointF QGraphicsSceneHoverEvent::pos() const**

        Returns the position of the mouse cursor in item coordinates at the
        moment the hover event was sent.

        **See also** **scenePos** () and **screenPos** ().
        """
        ...
    def scenePos(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#scenePos

        **QPointF QGraphicsSceneHoverEvent::scenePos() const**

        Returns the position of the mouse cursor in scene coordinates at the
        moment the hover event was sent.

        **See also** **pos** () and **screenPos** ().
        """
        ...
    def screenPos(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#screenPos

        **QPoint QGraphicsSceneHoverEvent::screenPos() const**

        Returns the position of the mouse cursor in screen coordinates at the
        moment the hover event was sent.

        **See also** **pos** () and **scenePos** ().
        """
        ...
    def setLastPos(
        self,
        pos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#lastPos

        **QPointF QGraphicsSceneHoverEvent::lastPos() const**

        Returns the last recorded mouse cursor position in item coordinates.

        **See also** **lastScenePos** (), **lastScreenPos** (), and **pos** ().
        """
        ...
    def setLastScenePos(
        self,
        pos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#lastScenePos

        **QPointF QGraphicsSceneHoverEvent::lastScenePos() const**

        Returns the last recorded, the scene coordinates of the previous mouse
        or hover event received by the view, that created the event mouse cursor
        position in scene coordinates.

        **See also** **lastPos** (), **lastScreenPos** (), and **scenePos** ().
        """
        ...
    def setLastScreenPos(self, pos: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#lastScreenPos

        **QPoint QGraphicsSceneHoverEvent::lastScreenPos() const**

        Returns the last recorded mouse cursor position in screen coordinates.
        The last recorded position is the position of the previous mouse or
        hover event received by the view that created the event.

        **See also** **lastPos** (), **lastScenePos** (), and **screenPos** ().
        """
        ...
    def setModifiers(self, modifiers: PySide6.QtCore.Qt.KeyboardModifiers) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#modifiers

        **Qt::KeyboardModifiers QGraphicsSceneHoverEvent::modifiers() const**

        Returns the keyboard modifiers at the moment the hover event was sent.
        """
        ...
    def setPos(
        self,
        pos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#pos

        **QPointF QGraphicsSceneHoverEvent::pos() const**

        Returns the position of the mouse cursor in item coordinates at the
        moment the hover event was sent.

        **See also** **scenePos** () and **screenPos** ().
        """
        ...
    def setScenePos(
        self,
        pos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#scenePos

        **QPointF QGraphicsSceneHoverEvent::scenePos() const**

        Returns the position of the mouse cursor in scene coordinates at the
        moment the hover event was sent.

        **See also** **pos** () and **screenPos** ().
        """
        ...
    def setScreenPos(self, pos: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#screenPos

        **QPoint QGraphicsSceneHoverEvent::screenPos() const**

        Returns the position of the mouse cursor in screen coordinates at the
        moment the hover event was sent.

        **See also** **pos** () and **scenePos** ().
        """
        ...
