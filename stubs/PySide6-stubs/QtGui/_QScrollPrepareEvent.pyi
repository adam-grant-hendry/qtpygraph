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

class QScrollPrepareEvent(PySide6.QtCore.QEvent):
    """
    https://doc.qt.io/qt-6/qscrollprepareevent.html

    **Detailed Description**

    The scroll prepare event is sent before scrolling (usually by **QScroller**
    ) is started. The object receiving this event should set **viewportSize** ,
    maxContentPos and **contentPos** . It also should accept this event to
    indicate that scrolling should be started.

    It is not guaranteed that a **QScrollEvent**  will be sent after an accepted
    QScrollPrepareEvent, e.g. in a case where the maximum content position is
    (0, 0).

    **See also** **QScrollEvent**  and **QScroller** .
    """

    @overload
    def __init__(self, arg__1: PySide6.QtGui.QScrollPrepareEvent) -> None:
        """
        https://doc.qt.io/qt-6/qscrollprepareevent.html#QScrollPrepareEvent-2

        **QScrollPrepareEvent::QScrollPrepareEvent(const QPointF & startPos )**

        Creates new QScrollPrepareEvent The **startPos** is the position of a
        touch or mouse event that started the scrolling.
        """
        ...
    @overload
    def __init__(
        self,
        startPos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qscrollprepareevent.html#QScrollPrepareEvent-2

        **QScrollPrepareEvent::QScrollPrepareEvent(const QPointF & startPos )**

        Creates new QScrollPrepareEvent The **startPos** is the position of a
        touch or mouse event that started the scrolling.
        """
        ...
    def clone(self) -> PySide6.QtGui.QScrollPrepareEvent: ...
    def contentPos(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qscrollprepareevent.html#contentPos

        **QPointF QScrollPrepareEvent::contentPos() const**

        Returns the current position of the content as set by **setContentPos**
        .

        **See also** **setContentPos** ().
        """
        ...
    def contentPosRange(self) -> PySide6.QtCore.QRectF:
        """
        https://doc.qt.io/qt-6/qscrollprepareevent.html#contentPosRange

        **QRectF QScrollPrepareEvent::contentPosRange() const**

        Returns the range of coordinates for the content as set by
        **setContentPosRange** ().

        **See also** **setContentPosRange** ().
        """
        ...
    def setContentPos(
        self,
        pos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qscrollprepareevent.html#setContentPos

        **void QScrollPrepareEvent::setContentPos(const QPointF & pos )**

        Sets the current content position to **pos**.

        **See also** **contentPos** ().
        """
        ...
    def setContentPosRange(
        self, rect: PySide6.QtCore.QRectF | PySide6.QtCore.QRect
    ) -> None:
        """
        https://doc.qt.io/qt-6/qscrollprepareevent.html#setContentPosRange

        **void QScrollPrepareEvent::setContentPosRange(const QRectF & rect )**

        Sets the range of content coordinates to **rect**.

        **See also** **contentPosRange** ().
        """
        ...
    def setViewportSize(self, size: PySide6.QtCore.QSizeF | PySide6.QtCore.QSize) -> None:
        """
        https://doc.qt.io/qt-6/qscrollprepareevent.html#setViewportSize

        **void QScrollPrepareEvent::setViewportSize(const QSizeF & size )**

        Sets the size of the area that is to be scrolled to **size**.

        **See also** **viewportSize** ().
        """
        ...
    def startPos(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qscrollprepareevent.html#startPos

        **QPointF QScrollPrepareEvent::startPos() const**

        Returns the position of the touch or mouse event that started the
        scrolling.
        """
        ...
    def viewportSize(self) -> PySide6.QtCore.QSizeF:
        """
        https://doc.qt.io/qt-6/qscrollprepareevent.html#viewportSize

        **QSizeF QScrollPrepareEvent::viewportSize() const**

        Returns size of the area that is to be scrolled as set by
        **setViewportSize**

        **See also** **setViewportSize** ().
        """
        ...
