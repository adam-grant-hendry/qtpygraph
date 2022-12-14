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

class QTimerEvent(PySide6.QtCore.QEvent):
    """
    https://doc.qt.io/qt-6/qtimerevent.html

    **Detailed Description**

    Timer events are sent at regular intervals to objects that have started one
    or more timers. Each timer has a unique identifier. A timer is started with
    **QObject::startTimer** ().

    The **QTimer**  class provides a high-level programming interface that uses
    signals instead of events. It also provides single-shot timers.

    The event handler **QObject::timerEvent** () receives timer events.

    **See also** **QTimer** , **QObject::timerEvent** (),
    **QObject::startTimer** (), and **QObject::killTimer** ().
    """

    @overload
    def __init__(self, arg__1: PySide6.QtCore.QTimerEvent) -> None:
        """
        https://doc.qt.io/qt-6/qtimerevent.html#QTimerEvent-2

        **QTimerEvent::QTimerEvent(int timerId )**

        Constructs a timer event object with the timer identifier set to
        **timerId**.
        """
        ...
    @overload
    def __init__(self, timerId: int) -> None:
        """
        https://doc.qt.io/qt-6/qtimerevent.html#QTimerEvent-2

        **QTimerEvent::QTimerEvent(int timerId )**

        Constructs a timer event object with the timer identifier set to
        **timerId**.
        """
        ...
    def clone(self) -> PySide6.QtCore.QTimerEvent: ...
    def timerId(self) -> int:
        """
        https://doc.qt.io/qt-6/qtimerevent.html#timerId

        **int QTimerEvent::timerId() const**

        Returns the unique timer identifier, which is the same identifier as
        returned from **QObject::startTimer** ().
        """
        ...
