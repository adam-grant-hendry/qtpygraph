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

class QSinglePointEvent(PySide6.QtGui.QPointerEvent):
    """
    https://doc.qt.io/qt-6/qsinglepointevent.html

    **Detailed Description**
    """

    @overload
    def __init__(self, arg__1: PySide6.QtGui.QSinglePointEvent) -> None: ...
    @overload
    def __init__(
        self,
        type: PySide6.QtCore.QEvent.Type,
        dev: PySide6.QtGui.QPointingDevice,
        localPos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        scenePos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        globalPos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        button: PySide6.QtCore.Qt.MouseButton,
        buttons: PySide6.QtCore.Qt.MouseButtons,
        modifiers: PySide6.QtCore.Qt.KeyboardModifiers,
        source: PySide6.QtCore.Qt.MouseEventSource = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        type: PySide6.QtCore.QEvent.Type,
        dev: PySide6.QtGui.QPointingDevice,
        point: PySide6.QtGui.QEventPoint,
        button: PySide6.QtCore.Qt.MouseButton,
        buttons: PySide6.QtCore.Qt.MouseButtons,
        modifiers: PySide6.QtCore.Qt.KeyboardModifiers,
        source: PySide6.QtCore.Qt.MouseEventSource,
    ) -> None: ...
    def button(self) -> PySide6.QtCore.Qt.MouseButton:
        """
        https://doc.qt.io/qt-6/qsinglepointevent.html#button

        **Qt::MouseButton QSinglePointEvent::button() const**

        Returns the button that caused the event.

        The returned value is always **Qt::NoButton**  for mouse move events, as
        well as **TabletMove** , **TabletEnterProximity** , and
        **TabletLeaveProximity**  events.

        **See also** **buttons** ().
        """
        ...
    def buttons(self) -> PySide6.QtCore.Qt.MouseButtons:
        """
        https://doc.qt.io/qt-6/qsinglepointevent.html#buttons

        **Qt::MouseButtons QSinglePointEvent::buttons() const**

        Returns the button state when the event was generated.

        The button state is a combination of **Qt::LeftButton** ,
        **Qt::RightButton** , and **Qt::MiddleButton**  using the OR operator.

        For mouse move or **TabletMove**  events, this is all buttons that are
        pressed down.

        For mouse press, double click, or **TabletPress**  events, this includes
        the button that caused the event.

        For mouse release or **TabletRelease**  events, this excludes the button
        that caused the event.

        **See also** **button** ().
        """
        ...
    def clone(self) -> PySide6.QtGui.QSinglePointEvent: ...
    def exclusivePointGrabber(self) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qsinglepointevent.html#exclusivePointGrabber-prop

        **exclusivePointGrabber : QObject***

        This property holds the object that will receive future updates

        The exclusive grabber is an object that has chosen to receive all future
        update events and the release event containing the same point that this
        event carries.

        Setting the exclusivePointGrabber property is a convenience equivalent
        to:

        setExclusiveGrabber(points().first(), exclusiveGrabber);

        **Access functions:**

        QObject * **exclusivePointGrabber** () const
        void
        **setExclusivePointGrabber** (QObject * **exclusiveGrabber** )

        **Member Function Documentation**
        """
        ...
    def globalPosition(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qsinglepointevent.html#globalPosition

        **QPointF QSinglePointEvent::globalPosition() const**

        Returns the position of the point in this event on the screen or virtual
        desktop.

        **Note:** The global position of a mouse pointer is recorded **at the
        time of the event**. This is important on asynchronous window systems
        such as X11; whenever you move your widgets around in response to mouse
        events, globalPosition() can differ a lot from the current cursor
        position returned by **QCursor::pos** ().

        **See also** **position** ().
        """
        ...
    def isBeginEvent(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsinglepointevent.html#isBeginEvent

        **[override virtual] bool QSinglePointEvent::isBeginEvent() const**

        Returns `true` if this event represents a **button**  being pressed.
        """
        ...
    def isEndEvent(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsinglepointevent.html#isEndEvent

        **[override virtual] bool QSinglePointEvent::isEndEvent() const**

        Returns `true` if this event represents a **button**  being released.
        """
        ...
    def isUpdateEvent(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsinglepointevent.html#isUpdateEvent

        **[override virtual] bool QSinglePointEvent::isUpdateEvent() const**

        Returns `true` if this event does not include a change in **button
        state** .
        """
        ...
    def position(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qsinglepointevent.html#position

        **QPointF QSinglePointEvent::position() const**

        Returns the position of the point in this event, relative to the widget
        or item that received the event.

        If you move your widgets around in response to mouse events, use
        **globalPosition** () instead.

        **See also** **globalPosition** ().
        """
        ...
    def scenePosition(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qsinglepointevent.html#scenePosition

        **QPointF QSinglePointEvent::scenePosition() const**

        Returns the position of the point in this event, relative to the window
        or scene.

        **See also** **QEventPoint::scenePosition** .
        """
        ...
    def setExclusivePointGrabber(self, exclusiveGrabber: PySide6.QtCore.QObject) -> None:
        """
        https://doc.qt.io/qt-6/qsinglepointevent.html#exclusivePointGrabber-prop

        **exclusivePointGrabber : QObject***

        This property holds the object that will receive future updates

        The exclusive grabber is an object that has chosen to receive all future
        update events and the release event containing the same point that this
        event carries.

        Setting the exclusivePointGrabber property is a convenience equivalent
        to:

        setExclusiveGrabber(points().first(), exclusiveGrabber);

        **Access functions:**

        QObject * **exclusivePointGrabber** () const
        void
        **setExclusivePointGrabber** (QObject * **exclusiveGrabber** )

        **Member Function Documentation**
        """
        ...
