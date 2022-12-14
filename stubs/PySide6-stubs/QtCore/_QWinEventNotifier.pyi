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
PySide6.QtCore, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore

class QWinEventNotifier(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qwineventnotifier.html

    **Detailed Description**

    The QWinEventNotifier class makes it possible to use the wait functions on
    windows in a asynchronous manner. With this class, you can register a HANDLE
    to an event and get notification when that event becomes signalled. The
    state of the event is not modified in the process so if it is a manual reset
    event you will need to reset it after the notification.

    Once you have created a event object using Windows API such as CreateEvent()
    or OpenEvent(), you can create an event notifier to monitor the event
    handle. If the event notifier is enabled, it will emit the **activated** ()
    signal whenever the corresponding event object is signalled.

    The **setEnabled** () function allows you to disable as well as enable the
    event notifier. It is generally advisable to explicitly enable or disable
    the event notifier. A disabled notifier does nothing when the event object
    is signalled (the same effect as not creating the event notifier). Use the
    **isEnabled** () function to determine the notifier's current status.

    Finally, you can use the **setHandle** () function to register a new event
    object, and the **handle** () function to retrieve the event handle.

    **Further information:** Although the class is called QWinEventNotifier, it
    can be used for certain other objects which are so-called synchronization
    objects, such as Processes, Threads, Waitable timers.

    **Warning:** This class is only available on Windows.
    """

    @overload
    def __init__(self, hEvent: int, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qwineventnotifier.html#QWinEventNotifier

        **QWinEventNotifier::QWinEventNotifier(QObject * parent = nullptr)**

        Constructs an event notifier with the given **parent**.
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qwineventnotifier.html#QWinEventNotifier-1

        **QWinEventNotifier::QWinEventNotifier(QWinEventNotifier::HANDLE hEvent
        , QObject * parent = nullptr)**

        Constructs an event notifier with the given **parent**. It enables the
        notifier, and watches for the event **hEvent**.

        The notifier is enabled by default, i.e. it emits the **activated** ()
        signal whenever the corresponding event is signalled. However, it is
        generally advisable to explicitly enable or disable the event notifier.

        **See also** **setEnabled** () and **isEnabled** ().
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qwineventnotifier.html#event

        **[override virtual protected] bool QWinEventNotifier::event(QEvent * e
        )**

        Reimplements: **QObject::event** (QEvent *e).
        """
        ...
    def handle(self) -> int:
        """
        https://doc.qt.io/qt-6/qwineventnotifier.html#handle

        **QWinEventNotifier::HANDLE QWinEventNotifier::handle() const**

        Returns the HANDLE that has been registered in the notifier.

        **See also** **setHandle** ().
        """
        ...
    def isEnabled(self) -> bool:
        """
        https://doc.qt.io/qt-6/qwineventnotifier.html#isEnabled

        **bool QWinEventNotifier::isEnabled() const**

        Returns `true` if the notifier is enabled; otherwise returns `false`.

        **See also** **setEnabled** ().
        """
        ...
    def setEnabled(self, enable: bool) -> None:
        """
        https://doc.qt.io/qt-6/qwineventnotifier.html#setEnabled

        **[slot] void QWinEventNotifier::setEnabled(bool enable )**

        If **enable** is true, the notifier is enabled; otherwise the notifier
        is disabled.

        **See also** **isEnabled** () and **activated** ().
        """
        ...
    def setHandle(self, hEvent: int) -> None:
        """
        https://doc.qt.io/qt-6/qwineventnotifier.html#setHandle

        **void QWinEventNotifier::setHandle(QWinEventNotifier::HANDLE hEvent )**

        Register the HANDLE **hEvent**. The old HANDLE will be automatically
        unregistered.

        **Note** : The notifier will be disabled as a side effect and needs to
        be re-enabled.

        **See also** **handle** () and **setEnabled** ().
        """
        ...
    @property
    def activated(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qwineventnotifier.html#activated

        **[private signal] void
        QWinEventNotifier::activated(QWinEventNotifier::HANDLE hEvent )**

        This signal is emitted whenever the event notifier is enabled and the
        corresponding HANDLE is signalled.

        The state of the event is not modified in the process, so if it is a
        manual reset event, you will need to reset it after the notification.

        The object is passed in the **hEvent** parameter.

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.

        **See also** **handle** ().
        """
        ...
