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

from enum import IntFlag
from typing import overload

import PySide6.QtCore

class QEventLoop(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qeventloop.html

    **Detailed Description**

    At any time, you can create a QEventLoop object and call **exec** () on it
    to start a local event loop. From within the event loop, calling **exit** ()
    will force **exec** () to return.

    **See also** **QAbstractEventDispatcher** .
    """

    AllEvents: QEventLoop.ProcessEventsFlag = ...
    ExcludeUserInputEvents: QEventLoop.ProcessEventsFlag = ...
    ExcludeSocketNotifiers: QEventLoop.ProcessEventsFlag = ...
    WaitForMoreEvents: QEventLoop.ProcessEventsFlag = ...
    X11ExcludeTimers: QEventLoop.ProcessEventsFlag = ...
    EventLoopExec: QEventLoop.ProcessEventsFlag = ...
    DialogExec: QEventLoop.ProcessEventsFlag = ...

    class ProcessEventsFlag(IntFlag):
        AllEvents: QEventLoop.ProcessEventsFlag = ...
        ExcludeUserInputEvents: QEventLoop.ProcessEventsFlag = ...
        ExcludeSocketNotifiers: QEventLoop.ProcessEventsFlag = ...
        WaitForMoreEvents: QEventLoop.ProcessEventsFlag = ...
        X11ExcludeTimers: QEventLoop.ProcessEventsFlag = ...
        EventLoopExec: QEventLoop.ProcessEventsFlag = ...
        DialogExec: QEventLoop.ProcessEventsFlag = ...

    class ProcessEventsFlags: ...

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qeventloop.html#QEventLoop

        **QEventLoop::QEventLoop(QObject * parent = nullptr)**

        Constructs an event loop object with the given **parent**.
        """
        ...
    def event(self, event: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qeventloop.html#event

        **[override virtual] bool QEventLoop::event(QEvent * event )**

        Reimplements: **QObject::event** (QEvent *e).
        """
        ...
    def exec(self, flags: PySide6.QtCore.QEventLoop.ProcessEventsFlags = ...) -> int:
        """
        https://doc.qt.io/qt-6/qeventloop.html#exec

        **int QEventLoop::exec(QEventLoop::ProcessEventsFlags flags =
        AllEvents)**

        Enters the main event loop and waits until **exit** () is called.
        Returns the value that was passed to **exit** ().

        If **flags** are specified, only events of the types allowed by the
        **flags** will be processed.

        It is necessary to call this function to start event handling. The main
        event loop receives events from the window system and dispatches these
        to the application widgets.

        Generally speaking, no user interaction can take place before calling
        exec(). As a special case, modal widgets like **QMessageBox**  can be
        used before calling exec(), because modal widgets use their own local
        event loop.

        To make your application perform idle processing (i.e. executing a
        special function whenever there are no pending events), use a **QTimer**
        with 0 timeout. More sophisticated idle processing schemes can be
        achieved using **processEvents** ().

        **See also** **QCoreApplication::quit** (), **exit** (), and
        **processEvents** ().
        """
        ...
    def exec_(self, flags: PySide6.QtCore.QEventLoop.ProcessEventsFlags = ...) -> int:
        """
        https://doc.qt.io/qt-6/qeventloop.html#exec

        **int QEventLoop::exec(QEventLoop::ProcessEventsFlags flags =
        AllEvents)**

        Enters the main event loop and waits until **exit** () is called.
        Returns the value that was passed to **exit** ().

        If **flags** are specified, only events of the types allowed by the
        **flags** will be processed.

        It is necessary to call this function to start event handling. The main
        event loop receives events from the window system and dispatches these
        to the application widgets.

        Generally speaking, no user interaction can take place before calling
        exec(). As a special case, modal widgets like **QMessageBox**  can be
        used before calling exec(), because modal widgets use their own local
        event loop.

        To make your application perform idle processing (i.e. executing a
        special function whenever there are no pending events), use a **QTimer**
        with 0 timeout. More sophisticated idle processing schemes can be
        achieved using **processEvents** ().

        **See also** **QCoreApplication::quit** (), **exit** (), and
        **processEvents** ().
        """
        ...
    def exit(self, returnCode: int = ...) -> None:
        """
        https://doc.qt.io/qt-6/qeventloop.html#exit

        **[slot] void QEventLoop::exit(int returnCode = 0)**

        Tells the event loop to exit with a return code.

        After this function has been called, the event loop returns from the
        call to **exec** (). The **exec** () function returns **returnCode**.

        By convention, a **returnCode** of 0 means success, and any non-zero
        value indicates an error.

        Note that unlike the C library function of the same name, this function
        **does** return to the caller -- it is event processing that stops.

        **See also** **QCoreApplication::quit** (), **quit** (), and **exec**
        ().
        """
        ...
    def isRunning(self) -> bool:
        """
        https://doc.qt.io/qt-6/qeventloop.html#isRunning

        **bool QEventLoop::isRunning() const**

        Returns `true` if the event loop is running; otherwise returns false.
        The event loop is considered running from the time when **exec** () is
        called until **exit** () is called.

        **See also** **exec** () and **exit** ().
        """
        ...
    @overload
    def processEvents(
        self, flags: PySide6.QtCore.QEventLoop.ProcessEventsFlags, maximumTime: int
    ) -> None:
        """
        https://doc.qt.io/qt-6/qeventloop.html#processEvents

        **bool QEventLoop::processEvents(QEventLoop::ProcessEventsFlags flags =
        AllEvents)**

        Processes some pending events that match **flags**. Returns `true` if
        pending events were handled; otherwise returns `false`.

        This function is especially useful if you have a long running operation
        and want to show its progress without allowing user input; i.e. by using
        the **ExcludeUserInputEvents**  flag.

        This function is simply a wrapper for
        **QAbstractEventDispatcher::processEvents** (). See the documentation
        for that function for details.
        """
        ...
    @overload
    def processEvents(
        self, flags: PySide6.QtCore.QEventLoop.ProcessEventsFlags = ...
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qeventloop.html#processEvents-1

        **void QEventLoop::processEvents(QEventLoop::ProcessEventsFlags flags ,
        int maxTime )**

        Process pending events that match **flags** for a maximum of **maxTime**
        milliseconds, or until there are no more events to process, whichever is
        shorter. This function is especially useful if you have a long running
        operation and want to show its progress without allowing user input,
        i.e. by using the **ExcludeUserInputEvents**  flag.

        **Notes:**

        * This function does not process events continuously; it returns after
        all available events are processed.
          * Specifying the
        **WaitForMoreEvents**  flag makes no sense and will be ignored.
        """
        ...
    def quit(self) -> None:
        """
        https://doc.qt.io/qt-6/qeventloop.html#quit

        **[slot] void QEventLoop::quit()**

        Tells the event loop to exit normally.

        Same as exit(0).

        **See also** **QCoreApplication::quit** () and **exit** ().
        """
        ...
    def wakeUp(self) -> None:
        """
        https://doc.qt.io/qt-6/qeventloop.html#wakeUp

        **void QEventLoop::wakeUp()**

        Wakes up the event loop.

        **See also** **QAbstractEventDispatcher::wakeUp** ().
        """
        ...
