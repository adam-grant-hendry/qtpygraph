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

class QGraphicsSceneWheelEvent(PySide6.QtWidgets.QGraphicsSceneEvent):
    """
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html

    **Detailed Description**

    **QWheelEvent** s received by a **QGraphicsView**  are translated into
    QGraphicsSceneWheelEvents; it translates the QWheelEvent::globalPos() into
    item, scene, and screen coordinates (**pos** (), **scenePos** (), and
    **screenPos** ()).

    **See also** **QGraphicsSceneMouseEvent** ,
    **QGraphicsSceneContextMenuEvent** , **QGraphicsSceneHoverEvent** , and
    **QWheelEvent** .
    """

    def __init__(self, type: PySide6.QtCore.QEvent.Type | None = ...) -> None: ...
    def buttons(self) -> PySide6.QtCore.Qt.MouseButtons:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#buttons

        **Qt::MouseButtons QGraphicsSceneWheelEvent::buttons() const**

        Returns the mouse buttons that were pressed when the wheel event
        occurred.

        **See also** **modifiers** ().
        """
        ...
    def delta(self) -> int:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#delta

        **int QGraphicsSceneWheelEvent::delta() const**

        Returns the distance that the wheel is rotated, in eighths (1/8s) of a
        degree. A positive value indicates that the wheel was rotated forwards
        away from the user; a negative value indicates that the wheel was
        rotated backwards toward the user.

        Most mouse types work in steps of 15 degrees, in which case the delta
        value is a multiple of 120 (== 15 * 8).
        """
        ...
    def isInverted(self) -> bool:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#isInverted

        **[since 6.2] bool QGraphicsSceneWheelEvent::isInverted() const**

        Returns whether the delta values delivered with the event are inverted.

        This function was introduced in Qt 6.2.
        """
        ...
    def modifiers(self) -> PySide6.QtCore.Qt.KeyboardModifiers:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#modifiers

        **Qt::KeyboardModifiers QGraphicsSceneWheelEvent::modifiers() const**

        Returns the keyboard modifiers that were active when the wheel event
        occurred.

        **See also** **buttons** ().
        """
        ...
    def orientation(self) -> PySide6.QtCore.Qt.Orientation:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#orientation

        **Qt::Orientation QGraphicsSceneWheelEvent::orientation() const**

        Returns the wheel orientation.
        """
        ...
    def phase(self) -> PySide6.QtCore.Qt.ScrollPhase:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#phase

        **[since 6.2] Qt::ScrollPhase QGraphicsSceneWheelEvent::phase() const**

        Returns the scrolling phase of this wheel event.

        This function was introduced in Qt 6.2.

        **See also** **QWheelEvent::phase** .
        """
        ...
    def pixelDelta(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#pixelDelta

        **[since 6.2] QPoint QGraphicsSceneWheelEvent::pixelDelta() const**

        Returns the scrolling distance in pixels on screen. This value is
        provided on platforms that support high-resolution pixel-based delta
        values, such as macOS. The value should be used directly to scroll
        content on screen.

        This function was introduced in Qt 6.2.

        **See also** **QWheelEvent::pixelDelta** .
        """
        ...
    def pos(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#pos

        **QPointF QGraphicsSceneWheelEvent::pos() const**

        Returns the position of the cursor in item coordinates when the wheel
        event occurred.

        **See also** **scenePos** () and **screenPos** ().
        """
        ...
    def scenePos(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#scenePos

        **QPointF QGraphicsSceneWheelEvent::scenePos() const**

        Returns the position of the cursor in scene coordinates when the wheel
        event occurred.

        **See also** **pos** () and **screenPos** ().
        """
        ...
    def screenPos(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#screenPos

        **QPoint QGraphicsSceneWheelEvent::screenPos() const**

        Returns the position of the cursor in screen coordinates when the wheel
        event occurred.

        **See also** **pos** () and **scenePos** ().
        """
        ...
    def setButtons(self, buttons: PySide6.QtCore.Qt.MouseButtons) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#buttons

        **Qt::MouseButtons QGraphicsSceneWheelEvent::buttons() const**

        Returns the mouse buttons that were pressed when the wheel event
        occurred.

        **See also** **modifiers** ().
        """
        ...
    def setDelta(self, delta: int) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#delta

        **int QGraphicsSceneWheelEvent::delta() const**

        Returns the distance that the wheel is rotated, in eighths (1/8s) of a
        degree. A positive value indicates that the wheel was rotated forwards
        away from the user; a negative value indicates that the wheel was
        rotated backwards toward the user.

        Most mouse types work in steps of 15 degrees, in which case the delta
        value is a multiple of 120 (== 15 * 8).
        """
        ...
    def setInverted(self, inverted: bool) -> None: ...
    def setModifiers(self, modifiers: PySide6.QtCore.Qt.KeyboardModifiers) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#modifiers

        **Qt::KeyboardModifiers QGraphicsSceneWheelEvent::modifiers() const**

        Returns the keyboard modifiers that were active when the wheel event
        occurred.

        **See also** **buttons** ().
        """
        ...
    def setOrientation(self, orientation: PySide6.QtCore.Qt.Orientation) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#orientation

        **Qt::Orientation QGraphicsSceneWheelEvent::orientation() const**

        Returns the wheel orientation.
        """
        ...
    def setPhase(self, scrollPhase: PySide6.QtCore.Qt.ScrollPhase) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#phase

        **[since 6.2] Qt::ScrollPhase QGraphicsSceneWheelEvent::phase() const**

        Returns the scrolling phase of this wheel event.

        This function was introduced in Qt 6.2.

        **See also** **QWheelEvent::phase** .
        """
        ...
    def setPixelDelta(self, delta: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#pixelDelta

        **[since 6.2] QPoint QGraphicsSceneWheelEvent::pixelDelta() const**

        Returns the scrolling distance in pixels on screen. This value is
        provided on platforms that support high-resolution pixel-based delta
        values, such as macOS. The value should be used directly to scroll
        content on screen.

        This function was introduced in Qt 6.2.

        **See also** **QWheelEvent::pixelDelta** .
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
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#pos

        **QPointF QGraphicsSceneWheelEvent::pos() const**

        Returns the position of the cursor in item coordinates when the wheel
        event occurred.

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
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#scenePos

        **QPointF QGraphicsSceneWheelEvent::scenePos() const**

        Returns the position of the cursor in scene coordinates when the wheel
        event occurred.

        **See also** **pos** () and **screenPos** ().
        """
        ...
    def setScreenPos(self, pos: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#screenPos

        **QPoint QGraphicsSceneWheelEvent::screenPos() const**

        Returns the position of the cursor in screen coordinates when the wheel
        event occurred.

        **See also** **pos** () and **scenePos** ().
        """
        ...