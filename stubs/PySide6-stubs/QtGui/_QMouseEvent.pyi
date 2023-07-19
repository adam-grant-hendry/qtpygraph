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

class QMouseEvent(PySide6.QtGui.QSinglePointEvent):
    """
    https://doc.qt.io/qt-6/qmouseevent.html

    **Detailed Description**

    Mouse events occur when a mouse button is pressed or released inside a
    widget, or when the mouse cursor is moved.

    Mouse move events will occur only when a mouse button is pressed down,
    unless mouse tracking has been enabled with **QWidget::setMouseTracking**
    ().

    Qt automatically grabs the mouse when a mouse button is pressed inside a
    widget; the widget will continue to receive mouse events until the last
    mouse button is released.

    A mouse event contains a special accept flag that indicates whether the
    receiver wants the event. You should call **ignore** () if the mouse event
    is not handled by your widget. A mouse event is propagated up the parent
    widget chain until a widget accepts it with **accept** (), or an event
    filter consumes it.

    **Note:** If a mouse event is propagated to a **widget**  for which
    **Qt::WA_NoMousePropagation**  has been set, that mouse event will not be
    propagated further up the parent widget chain.

    The state of the keyboard modifier keys can be found by calling the
    **modifiers** () function, inherited from **QInputEvent** .

    The **position** () function gives the cursor position relative to the
    widget or item that receives the mouse event. If you move the widget as a
    result of the mouse event, use the global position returned by
    **globalPosition** () to avoid a shaking motion.

    The **QWidget::setEnabled** () function can be used to enable or disable
    mouse and keyboard events for a widget.

    Reimplement the **QWidget**  event handlers, **QWidget::mousePressEvent**
    (), **QWidget::mouseReleaseEvent** (), **QWidget::mouseDoubleClickEvent**
    (), and **QWidget::mouseMoveEvent** () to receive mouse events in your own
    widgets.

    **See also** **QWidget::setMouseTracking** (), **QWidget::grabMouse** (),
    and **QCursor::pos** ().
    """

    @overload
    def __init__(self, arg__1: PySide6.QtGui.QMouseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmouseevent.html#QMouseEvent-2

        **QMouseEvent::QMouseEvent(QEvent::Type type , const QPointF & localPos
        , Qt::MouseButton button , Qt::MouseButtons buttons ,
        Qt::KeyboardModifiers modifiers , const QPointingDevice * device =
        QPointingDevice::primaryPointingDevice())**

        Constructs a mouse event object originating from **device**.

        The **type** parameter must be one of **QEvent::MouseButtonPress** ,
        **QEvent::MouseButtonRelease** , **QEvent::MouseButtonDblClick** , or
        **QEvent::MouseMove** .

        The **localPos** is the mouse cursor's position relative to the
        receiving widget or item. The window position is set to the same value
        as **localPos**. The **button** that caused the event is given as a
        value from the **Qt::MouseButton**  enum. If the event **type** is
        **MouseMove** , the appropriate button for this event is
        **Qt::NoButton** . The mouse and keyboard states at the time of the
        event are specified by **buttons** and **modifiers**.

        The **globalPosition** () is initialized to **QCursor::pos** (), which
        may not be appropriate. Use the other constructor to specify the global
        position explicitly.
        """
        ...
    @overload
    def __init__(
        self,
        type: PySide6.QtCore.QEvent.Type,
        localPos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        button: PySide6.QtCore.Qt.MouseButton,
        buttons: PySide6.QtCore.Qt.MouseButtons,
        modifiers: PySide6.QtCore.Qt.KeyboardModifiers,
        device: PySide6.QtGui.QPointingDevice = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmouseevent.html#QMouseEvent-3

        **QMouseEvent::QMouseEvent(QEvent::Type type , const QPointF & localPos
        , const QPointF & globalPos , Qt::MouseButton button , Qt::MouseButtons
        buttons , Qt::KeyboardModifiers modifiers , const QPointingDevice *
        device = QPointingDevice::primaryPointingDevice())**

        Constructs a mouse event object originating from **device**.

        The **type** parameter must be **QEvent::MouseButtonPress** ,
        **QEvent::MouseButtonRelease** , **QEvent::MouseButtonDblClick** , or
        **QEvent::MouseMove** .

        The **localPos** is the mouse cursor's position relative to the
        receiving widget or item. The cursor's position in screen coordinates is
        specified by **globalPos**. The window position is set to the same value
        as **localPos**. The **button** that caused the event is given as a
        value from the **Qt::MouseButton**  enum. If the event **type** is
        **MouseMove** , the appropriate button for this event is
        **Qt::NoButton** . **buttons** is the state of all buttons at the time
        of the event, **modifiers** the state of all keyboard modifiers.
        """
        ...
    @overload
    def __init__(
        self,
        type: PySide6.QtCore.QEvent.Type,
        localPos: (
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
        device: PySide6.QtGui.QPointingDevice = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmouseevent.html#QMouseEvent-4

        **QMouseEvent::QMouseEvent(QEvent::Type type , const QPointF & localPos
        , const QPointF & scenePos , const QPointF & globalPos , Qt::MouseButton
        button , Qt::MouseButtons buttons , Qt::KeyboardModifiers modifiers ,
        const QPointingDevice * device =
        QPointingDevice::primaryPointingDevice())**

        Constructs a mouse event object.

        The **type** parameter must be **QEvent::MouseButtonPress** ,
        **QEvent::MouseButtonRelease** , **QEvent::MouseButtonDblClick** , or
        **QEvent::MouseMove** .

        The points **localPos** , **scenePos** and **globalPos** specify the
        mouse cursor's position relative to the receiving widget or item,
        window, and screen or desktop, respectively.

        The **button** that caused the event is given as a value from the
        **Qt::MouseButton**  enum. If the event **type** is **MouseMove** , the
        appropriate button for this event is **Qt::NoButton** . **buttons** is
        the state of all buttons at the time of the event, **modifiers** is the
        state of all keyboard modifiers.
        """
        ...
    @overload
    def __init__(
        self,
        type: PySide6.QtCore.QEvent.Type,
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
        device: PySide6.QtGui.QPointingDevice = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmouseevent.html#QMouseEvent-2

        **QMouseEvent::QMouseEvent(QEvent::Type type , const QPointF & localPos
        , Qt::MouseButton button , Qt::MouseButtons buttons ,
        Qt::KeyboardModifiers modifiers , const QPointingDevice * device =
        QPointingDevice::primaryPointingDevice())**

        Constructs a mouse event object originating from **device**.

        The **type** parameter must be one of **QEvent::MouseButtonPress** ,
        **QEvent::MouseButtonRelease** , **QEvent::MouseButtonDblClick** , or
        **QEvent::MouseMove** .

        The **localPos** is the mouse cursor's position relative to the
        receiving widget or item. The window position is set to the same value
        as **localPos**. The **button** that caused the event is given as a
        value from the **Qt::MouseButton**  enum. If the event **type** is
        **MouseMove** , the appropriate button for this event is
        **Qt::NoButton** . The mouse and keyboard states at the time of the
        event are specified by **buttons** and **modifiers**.

        The **globalPosition** () is initialized to **QCursor::pos** (), which
        may not be appropriate. Use the other constructor to specify the global
        position explicitly.
        """
        ...
    @overload
    def __init__(
        self,
        type: PySide6.QtCore.QEvent.Type,
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
        source: PySide6.QtCore.Qt.MouseEventSource,
        device: PySide6.QtGui.QPointingDevice = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmouseevent.html#QMouseEvent-2

        **QMouseEvent::QMouseEvent(QEvent::Type type , const QPointF & localPos
        , Qt::MouseButton button , Qt::MouseButtons buttons ,
        Qt::KeyboardModifiers modifiers , const QPointingDevice * device =
        QPointingDevice::primaryPointingDevice())**

        Constructs a mouse event object originating from **device**.

        The **type** parameter must be one of **QEvent::MouseButtonPress** ,
        **QEvent::MouseButtonRelease** , **QEvent::MouseButtonDblClick** , or
        **QEvent::MouseMove** .

        The **localPos** is the mouse cursor's position relative to the
        receiving widget or item. The window position is set to the same value
        as **localPos**. The **button** that caused the event is given as a
        value from the **Qt::MouseButton**  enum. If the event **type** is
        **MouseMove** , the appropriate button for this event is
        **Qt::NoButton** . The mouse and keyboard states at the time of the
        event are specified by **buttons** and **modifiers**.

        The **globalPosition** () is initialized to **QCursor::pos** (), which
        may not be appropriate. Use the other constructor to specify the global
        position explicitly.
        """
        ...
    def clone(self) -> PySide6.QtGui.QMouseEvent: ...
    def flags(self) -> PySide6.QtCore.Qt.MouseEventFlags:
        """
        https://doc.qt.io/qt-6/qmouseevent.html#flags

        **[since 5.3] Qt::MouseEventFlags QMouseEvent::flags() const**

        Returns the mouse event flags.

        The mouse event flags provide additional information about a mouse
        event.

        This function was introduced in Qt 5.3.

        **See also** **Qt::MouseEventFlag**  and
        **QGraphicsSceneMouseEvent::flags** ().
        """
        ...
    def globalPos(self) -> PySide6.QtCore.QPoint: ...
    def globalX(self) -> int: ...
    def globalY(self) -> int: ...
    def localPos(self) -> PySide6.QtCore.QPointF: ...
    def pos(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qmouseevent.html#pos

        **QPoint QMouseEvent::pos() const**

        Returns the position of the mouse cursor, relative to the widget that
        received the event.

        If you move the widget as a result of the mouse event, use the global
        position returned by globalPos() to avoid a shaking motion.

        **See also** **x** (), **y** (), and **globalPos** ().
        """
        ...
    def screenPos(self) -> PySide6.QtCore.QPointF: ...
    def source(self) -> PySide6.QtCore.Qt.MouseEventSource: ...
    def windowPos(self) -> PySide6.QtCore.QPointF: ...
    def x(self) -> int: ...
    def y(self) -> int: ...