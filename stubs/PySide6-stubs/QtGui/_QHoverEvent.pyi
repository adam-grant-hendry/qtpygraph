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

class QHoverEvent(PySide6.QtGui.QSinglePointEvent):
    """
    https://doc.qt.io/qt-6/qhoverevent.html

    **Detailed Description**

    Mouse events occur when a mouse cursor is moved into, out of, or within a
    widget, and if the widget has the **Qt::WA_Hover**  attribute.

    The function pos() gives the current cursor position, while **oldPos** ()
    gives the old mouse position.

    There are a few similarities between the events **QEvent::HoverEnter**  and
    **QEvent::HoverLeave** , and the events **QEvent::Enter**  and
    **QEvent::Leave** . However, they are slightly different because we do an
    update() in the event handler of HoverEnter and HoverLeave.

    **QEvent::HoverMove**  is also slightly different from **QEvent::MouseMove**
    . Let us consider a top-level window A containing a child B which in turn
    contains a child C (all with mouse tracking enabled):

    ![](images/hoverevents.png)

    Now, if you move the cursor from the top to the bottom in the middle of A,
    you will get the following **QEvent::MouseMove**  events:

    1. A::MouseMove
      2. B::MouseMove
      3. C::MouseMove

    You will get the same events for **QEvent::HoverMove** , except that the
    event always propagates to the top-level regardless whether the event is
    accepted or not. It will only stop propagating with the
    **Qt::WA_NoMousePropagation**  attribute.

    In this case the events will occur in the following way:

    1. A::HoverMove
      2. A::HoverMove, B::HoverMove
      3. A::HoverMove,
    B::HoverMove, C::HoverMove
    """

    @overload
    def __init__(self, arg__1: PySide6.QtGui.QHoverEvent) -> None:
        """
        https://doc.qt.io/qt-6/qhoverevent.html#QHoverEvent-2

        **QHoverEvent::QHoverEvent(QEvent::Type type , const QPointF & pos ,
        const QPointF & oldPos , Qt::KeyboardModifiers modifiers =
        Qt::NoModifier, const QPointingDevice * device =
        QPointingDevice::primaryPointingDevice())**

        Constructs a hover event object originating from **device**.

        The **type** parameter must be **QEvent::HoverEnter** ,
        **QEvent::HoverLeave** , or **QEvent::HoverMove** .

        The **pos** is the current mouse cursor's position relative to the
        receiving widget, while **oldPos** is its previous such position.
        **modifiers** hold the state of all keyboard modifiers at the time of
        the event.
        """
        ...
    @overload
    def __init__(
        self,
        type: PySide6.QtCore.QEvent.Type,
        pos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        oldPos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        modifiers: PySide6.QtCore.Qt.KeyboardModifiers = ...,
        device: PySide6.QtGui.QPointingDevice = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qhoverevent.html#QHoverEvent-2

        **QHoverEvent::QHoverEvent(QEvent::Type type , const QPointF & pos ,
        const QPointF & oldPos , Qt::KeyboardModifiers modifiers =
        Qt::NoModifier, const QPointingDevice * device =
        QPointingDevice::primaryPointingDevice())**

        Constructs a hover event object originating from **device**.

        The **type** parameter must be **QEvent::HoverEnter** ,
        **QEvent::HoverLeave** , or **QEvent::HoverMove** .

        The **pos** is the current mouse cursor's position relative to the
        receiving widget, while **oldPos** is its previous such position.
        **modifiers** hold the state of all keyboard modifiers at the time of
        the event.
        """
        ...
    def clone(self) -> PySide6.QtGui.QHoverEvent: ...
    def isUpdateEvent(self) -> bool: ...
    def oldPos(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qhoverevent.html#oldPos

        **QPoint QHoverEvent::oldPos() const**

        Returns the previous position of the mouse cursor, relative to the
        widget that received the event. If there is no previous position,
        oldPos() will return the same position as pos().

        On **QEvent::HoverEnter**  events, this position will always be
        **QPoint** (-1, -1).

        **See also** **pos** ().
        """
        ...
    def oldPosF(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qhoverevent.html#oldPosF

        **QPointF QHoverEvent::oldPosF() const**

        Returns the previous position of the mouse cursor, relative to the
        widget that received the event. If there is no previous position,
        oldPosF() will return the same position as posF().

        On **QEvent::HoverEnter**  events, this position will always be
        **QPointF** (-1, -1).

        **See also** **posF** ().
        """
        ...
    def pos(self) -> PySide6.QtCore.QPoint: ...
    def posF(self) -> PySide6.QtCore.QPointF: ...