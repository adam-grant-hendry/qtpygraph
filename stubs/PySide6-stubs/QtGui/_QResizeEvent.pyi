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

class QResizeEvent(PySide6.QtCore.QEvent):
    """
    https://doc.qt.io/qt-6/qresizeevent.html

    **Detailed Description**

    Resize events are sent to widgets that have been resized.

    The event handler **QWidget::resizeEvent** () receives resize events.

    **See also** **QWidget::resize** () and **QWidget::setGeometry** ().
    """

    @overload
    def __init__(self, arg__1: PySide6.QtGui.QResizeEvent) -> None:
        """
        https://doc.qt.io/qt-6/qresizeevent.html#QResizeEvent-2

        **QResizeEvent::QResizeEvent(const QSize & size , const QSize & oldSize
        )**

        Constructs a resize event with the new and old widget sizes, **size**
        and **oldSize** respectively.
        """
        ...
    @overload
    def __init__(self, size: PySide6.QtCore.QSize, oldSize: PySide6.QtCore.QSize) -> None:
        """
        https://doc.qt.io/qt-6/qresizeevent.html#QResizeEvent-2

        **QResizeEvent::QResizeEvent(const QSize & size , const QSize & oldSize
        )**

        Constructs a resize event with the new and old widget sizes, **size**
        and **oldSize** respectively.
        """
        ...
    def clone(self) -> PySide6.QtGui.QResizeEvent: ...
    def oldSize(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qresizeevent.html#oldSize

        **const QSize &QResizeEvent::oldSize() const**

        Returns the old size of the widget.
        """
        ...
    def size(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qresizeevent.html#size

        **const QSize &QResizeEvent::size() const**

        Returns the new size of the widget. This is the same as
        **QWidget::size** ().
        """
        ...