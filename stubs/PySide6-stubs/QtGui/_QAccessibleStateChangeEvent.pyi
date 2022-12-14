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

class QAccessibleStateChangeEvent(PySide6.QtGui.QAccessibleEvent):
    """
    https://doc.qt.io/qt-6/qaccessiblestatechangeevent.html

    **Detailed Description**

    This class is used with **QAccessible::updateAccessibility** ().

    **See also** **QAccessibleInterface::state** ().
    """

    @overload
    def __init__(
        self,
        iface: PySide6.QtGui.QAccessibleInterface,
        state: PySide6.QtGui.QAccessible.State,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qaccessiblestatechangeevent.html#QAccessibleState
        ChangeEvent

        **QAccessibleStateChangeEvent::QAccessibleStateChangeEvent(QObject *
        object , QAccessible::State state )**

        Constructs a new QAccessibleStateChangeEvent for **object**. The
        difference to the object's previous state is in **state**.
        """
        ...
    @overload
    def __init__(
        self, obj: PySide6.QtCore.QObject, state: PySide6.QtGui.QAccessible.State
    ) -> None:
        """
        https://doc.qt.io/qt-6/qaccessiblestatechangeevent.html#QAccessibleState
        ChangeEvent-1

        **QAccessibleStateChangeEvent::QAccessibleStateChangeEvent(QAccessibleIn
        terface * iface , QAccessible::State state )**

        Constructs a new QAccessibleStateChangeEvent. **iface** is the interface
        associated with the event **state** is the state of the accessible
        object.
        """
        ...
    def changedStates(self) -> PySide6.QtGui.QAccessible.State:
        """
        https://doc.qt.io/qt-6/qaccessiblestatechangeevent.html#changedStates

        **QAccessible::State QAccessibleStateChangeEvent::changedStates()
        const**

        Returns the states that have been changed.

        Keep in mind that the returned states are the ones that have changed. To
        find out about the state of an object, use
        **QAccessibleInterface::state** ().

        For example, if an object used to have the focus but loses it, the
        object's state will have focused set to `false`. This event on the other
        hand tells about the change and has focused set to `true` since the
        focus state is changed from `true` to `false`.
        """
        ...
