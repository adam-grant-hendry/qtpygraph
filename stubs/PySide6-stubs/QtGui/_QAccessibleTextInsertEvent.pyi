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

class QAccessibleTextInsertEvent(PySide6.QtGui.QAccessibleTextCursorEvent):
    """
    https://doc.qt.io/qt-6/qaccessibletextinsertevent.html

    **Detailed Description**

    This class is used with **QAccessible::updateAccessibility** ().
    """

    @overload
    def __init__(
        self, iface: PySide6.QtGui.QAccessibleInterface, position: int, text: str
    ) -> None:
        """
        https://doc.qt.io/qt-6/qaccessibletextinsertevent.html#QAccessibleTextIn
        sertEvent

        **QAccessibleTextInsertEvent::QAccessibleTextInsertEvent(QObject *
        object , int position , const QString & text )**

        Constructs a new QAccessibleTextInsertEvent event for **object**. The
        **text** has been inserted at **position**. By default, it is assumed
        that the cursor has moved to the end of the selection. If that is not
        the case, one needs to manually set it with
        **QAccessibleTextCursorEvent::setCursorPosition** () for this event.
        """
        ...
    @overload
    def __init__(self, obj: PySide6.QtCore.QObject, position: int, text: str) -> None:
        """
        https://doc.qt.io/qt-6/qaccessibletextinsertevent.html#QAccessibleTextIn
        sertEvent-1

        **QAccessibleTextInsertEvent::QAccessibleTextInsertEvent(QAccessibleInte
        rface * iface , int position , const QString & text )**

        Constructs a new QAccessibleTextInsertEvent event for **iface**. The
        text has been inserted at **position**.
        """
        ...
    def changePosition(self) -> int:
        """
        https://doc.qt.io/qt-6/qaccessibletextinsertevent.html#changePosition

        **int QAccessibleTextInsertEvent::changePosition() const**

        Returns the position where the text was inserted.
        """
        ...
    def textInserted(self) -> str:
        """
        https://doc.qt.io/qt-6/qaccessibletextinsertevent.html#textInserted

        **QString QAccessibleTextInsertEvent::textInserted() const**

        Returns the text that has been inserted.
        """
        ...
