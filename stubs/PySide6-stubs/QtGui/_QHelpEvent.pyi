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

class QHelpEvent(PySide6.QtCore.QEvent):
    """
    https://doc.qt.io/qt-6/qhelpevent.html

    **Detailed Description**

    This event can be intercepted in applications to provide tooltips or "What's
    This?" help for custom widgets. The **type** () can be either
    **QEvent::ToolTip**  or **QEvent::WhatsThis** .

    **See also** **QToolTip** , **QWhatsThis** , **QStatusTipEvent** , and
    **QWhatsThisClickedEvent** .
    """

    @overload
    def __init__(self, arg__1: PySide6.QtGui.QHelpEvent) -> None:
        """
        https://doc.qt.io/qt-6/qhelpevent.html#QHelpEvent-2

        **QHelpEvent::QHelpEvent(QEvent::Type type , const QPoint & pos , const
        QPoint & globalPos )**

        Constructs a help event with the given **type** corresponding to the
        widget-relative position specified by **pos** and the global position
        specified by **globalPos**.

        **type** must be either **QEvent::ToolTip**  or **QEvent::WhatsThis** .

        **See also** **pos** () and **globalPos** ().
        """
        ...
    @overload
    def __init__(
        self,
        type: PySide6.QtCore.QEvent.Type,
        pos: PySide6.QtCore.QPoint,
        globalPos: PySide6.QtCore.QPoint,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qhelpevent.html#QHelpEvent-2

        **QHelpEvent::QHelpEvent(QEvent::Type type , const QPoint & pos , const
        QPoint & globalPos )**

        Constructs a help event with the given **type** corresponding to the
        widget-relative position specified by **pos** and the global position
        specified by **globalPos**.

        **type** must be either **QEvent::ToolTip**  or **QEvent::WhatsThis** .

        **See also** **pos** () and **globalPos** ().
        """
        ...
    def clone(self) -> PySide6.QtGui.QHelpEvent: ...
    def globalPos(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qhelpevent.html#globalPos

        **const QPoint &QHelpEvent::globalPos() const**

        Returns the mouse cursor position when the event was generated in global
        coordinates.

        **See also** **pos** (), **globalX** (), and **globalY** ().
        """
        ...
    def globalX(self) -> int:
        """
        https://doc.qt.io/qt-6/qhelpevent.html#globalX

        **int QHelpEvent::globalX() const**

        Same as **globalPos** ().**x** ().

        **See also** **x** (), **globalY** (), and **globalPos** ().
        """
        ...
    def globalY(self) -> int:
        """
        https://doc.qt.io/qt-6/qhelpevent.html#globalY

        **int QHelpEvent::globalY() const**

        Same as **globalPos** ().**y** ().

        **See also** **y** (), **globalX** (), and **globalPos** ().
        """
        ...
    def pos(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qhelpevent.html#pos

        **const QPoint &QHelpEvent::pos() const**

        Returns the mouse cursor position when the event was generated, relative
        to the widget to which the event is dispatched.

        **See also** **globalPos** (), **x** (), and **y** ().
        """
        ...
    def x(self) -> int:
        """
        https://doc.qt.io/qt-6/qhelpevent.html#x

        **int QHelpEvent::x() const**

        Same as **pos** ().x().

        **See also** **y** (), **pos** (), and **globalPos** ().
        """
        ...
    def y(self) -> int:
        """
        https://doc.qt.io/qt-6/qhelpevent.html#y

        **int QHelpEvent::y() const**

        Same as **pos** ().y().

        **See also** **x** (), **pos** (), and **globalPos** ().
        """
        ...