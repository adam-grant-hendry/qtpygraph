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

class QAccessibleEvent:
    """
    https://doc.qt.io/qt-6/qaccessibleevent.html

    **Detailed Description**

    This class is used with **QAccessible::updateAccessibility** ().

    The event type is one of the values of **QAccessible::Event** . There are a
    number of subclasses that should be used to provide more details about the
    event.

    For example to notify about a focus change when re-implementing
    **QWidget::setFocus** , the event could be used as follows:

    void MyWidget::setFocus(Qt::FocusReason reason)
        {
            // handle
    custom focus setting...
            QAccessibleEvent event(f, **QAccessible**
    ::Focus);
            **QAccessible** ::updateAccessibility(&event);
        }

    To enable in process screen readers, all events must be sent after the
    change has happened.
    """

    @overload
    def __init__(
        self,
        iface: PySide6.QtGui.QAccessibleInterface,
        typ: PySide6.QtGui.QAccessible.Event,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qaccessibleevent.html#QAccessibleEvent-1

        **QAccessibleEvent::QAccessibleEvent(QObject * object ,
        QAccessible::Event type )**

        Constructs a QAccessibleEvent to notify that **object** has changed. The
        event **type** describes what changed.
        """
        ...
    @overload
    def __init__(
        self, obj: PySide6.QtCore.QObject, typ: PySide6.QtGui.QAccessible.Event
    ) -> None:
        """
        https://doc.qt.io/qt-6/qaccessibleevent.html#QAccessibleEvent-2

        **QAccessibleEvent::QAccessibleEvent(QAccessibleInterface * interface ,
        QAccessible::Event type )**

        Constructs a QAccessibleEvent to notify that **interface** has changed.
        The event **type** describes what changed. Use this function if you
        already have a **QAccessibleInterface**  or no **QObject** , otherwise
        consider the overload taking a **QObject**  parameter as it might be
        cheaper.
        """
        ...
    def accessibleInterface(self) -> PySide6.QtGui.QAccessibleInterface:
        """
        https://doc.qt.io/qt-6/qaccessibleevent.html#accessibleInterface

        **[virtual] QAccessibleInterface
        *QAccessibleEvent::accessibleInterface() const**

        Returns the **QAccessibleInterface**  associated with the event.
        """
        ...
    def child(self) -> int:
        """
        https://doc.qt.io/qt-6/qaccessibleevent.html#child

        **int QAccessibleEvent::child() const**

        Returns the child index.

        **See also** **setChild** ().
        """
        ...
    def object(self) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qaccessibleevent.html#object

        **QObject *QAccessibleEvent::object() const**

        Returns the event object.
        """
        ...
    def setChild(self, chld: int) -> None:
        """
        https://doc.qt.io/qt-6/qaccessibleevent.html#setChild

        **void QAccessibleEvent::setChild(int child )**

        Sets the child index to **child**.

        **See also** **child** ().
        """
        ...
    def type(self) -> PySide6.QtGui.QAccessible.Event:
        """
        https://doc.qt.io/qt-6/qaccessibleevent.html#type

        **QAccessible::Event QAccessibleEvent::type() const**

        Returns the event type.
        """
        ...
    def uniqueId(self) -> int: ...