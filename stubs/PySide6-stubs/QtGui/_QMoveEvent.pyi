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

class QMoveEvent(PySide6.QtCore.QEvent):
    """
    https://doc.qt.io/qt-6/qmoveevent.html

    **Detailed Description**

    Move events are sent to widgets that have been moved to a new position
    relative to their parent.

    The event handler **QWidget::moveEvent** () receives move events.

    **See also** **QWidget::move** () and **QWidget::setGeometry** ().
    """

    @overload
    def __init__(self, arg__1: PySide6.QtGui.QMoveEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmoveevent.html#QMoveEvent-2

        **QMoveEvent::QMoveEvent(const QPoint & pos , const QPoint & oldPos )**

        Constructs a move event with the new and old widget positions, **pos**
        and **oldPos** respectively.
        """
        ...
    @overload
    def __init__(self, pos: PySide6.QtCore.QPoint, oldPos: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/qmoveevent.html#QMoveEvent-2

        **QMoveEvent::QMoveEvent(const QPoint & pos , const QPoint & oldPos )**

        Constructs a move event with the new and old widget positions, **pos**
        and **oldPos** respectively.
        """
        ...
    def clone(self) -> PySide6.QtGui.QMoveEvent: ...
    def oldPos(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qmoveevent.html#oldPos

        **const QPoint &QMoveEvent::oldPos() const**

        Returns the old position of the widget.
        """
        ...
    def pos(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qmoveevent.html#pos

        **const QPoint &QMoveEvent::pos() const**

        Returns the new position of the widget. This excludes the window frame
        for top level widgets.
        """
        ...
