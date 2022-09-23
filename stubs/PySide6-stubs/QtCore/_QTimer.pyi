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

from collections.abc import Callable
from typing import overload

import PySide6.QtCore

class QTimer(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qtimer.html

    **Detailed Description**

    The QTimer class provides a high-level programming interface for timers. To
    use it, create a QTimer, connect its **timeout** () signal to the
    appropriate slots, and call **start** (). From then on, it will emit the
    **timeout** () signal at constant intervals.

    Example for a one second (1000 millisecond) timer (from the **Analog Clock**
    example):

    **QTimer**  *timer = new **QTimer** (this);
            connect(timer,
    &**QTimer** ::timeout, this, QOverload<>::of(&AnalogClock::update));
    timer->start(1000);

    From then on, the `update()` slot is called every second.

    You can set a timer to time out only once by calling **setSingleShot**
    (true). You can also use the static **QTimer::singleShot** () function to
    call a slot after a specified interval:

    **QTimer** ::singleShot(200, this, &Foo::updateCaption);

    In multithreaded applications, you can use QTimer in any thread that has an
    event loop. To start an event loop from a non-GUI thread, use
    **QThread::exec** (). Qt uses the timer's **thread affinity**  to determine
    which thread will emit the **timeout** () signal. Because of this, you must
    start and stop the timer in its thread; it is not possible to start a timer
    from another thread.

    As a special case, a QTimer with a timeout of 0 will time out as soon as
    possible, though the ordering between zero timers and other sources of
    events is unspecified. Zero timers can be used to do some work while still
    providing a snappy user interface:

    **QTimer**  *timer = new **QTimer** (this);
            connect(timer,
    &**QTimer** ::timeout, this, &Foo::processOneThing);
            timer->start();

    From then on, `processOneThing()` will be called repeatedly. It should be
    written in such a way that it always returns quickly (typically after
    processing one data item) so that Qt can deliver events to the user
    interface and stop the timer as soon as it has done all its work. This is
    the traditional way of implementing heavy work in GUI applications, but as
    multithreading is nowadays becoming available on more and more platforms, we
    expect that zero-millisecond QTimer objects will gradually be replaced by
    **QThread** s.

    **Accuracy and Timer Resolution**

    The accuracy of timers depends on the underlying operating system and
    hardware. Most platforms support a resolution of 1 millisecond, though the
    accuracy of the timer will not equal this resolution in many real-world
    situations.

    The accuracy also depends on the **timer type** . For **Qt::PreciseTimer** ,
    QTimer will try to keep the accuracy at 1 millisecond. Precise timers will
    also never time out earlier than expected.

    For **Qt::CoarseTimer**  and **Qt::VeryCoarseTimer**  types, QTimer may wake
    up earlier than expected, within the margins for those types: 5% of the
    interval for **Qt::CoarseTimer**  and 500 ms for **Qt::VeryCoarseTimer** .

    All timer types may time out later than expected if the system is busy or
    unable to provide the requested accuracy. In such a case of timeout overrun,
    Qt will emit **timeout** () only once, even if multiple timeouts have
    expired, and then will resume the original interval.

    **Alternatives to QTimer**

    An alternative to using QTimer is to call **QObject::startTimer** () for
    your object and reimplement the **QObject::timerEvent** () event handler in
    your class (which must inherit **QObject** ). The disadvantage is that
    **timerEvent** () does not support such high-level features as single-shot
    timers or signals.

    Another alternative is **QBasicTimer** . It is typically less cumbersome
    than using **QObject::startTimer** () directly. See **Timers**  for an
    overview of all three approaches.

    Some operating systems limit the number of timers that may be used; Qt tries
    to work around these limitations.

    **See also** **QBasicTimer** , **QTimerEvent** , **QObject::timerEvent** (),
    **Timers** , **Analog Clock Example** , and **Wiggly Example** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qtimer.html#QTimer

        **QTimer::QTimer(QObject * parent = nullptr)**

        Constructs a timer with the given **parent**.
        """
        ...
    def interval(self) -> int:
        """
        https://doc.qt.io/qt-6/qtimer.html#interval-prop

        **[bindable] interval : int**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the timeout interval in milliseconds

        The default value for this property is 0. A **QTimer**  with a timeout
        interval of 0 will time out as soon as all the events in the window
        system's event queue have been processed.

        Setting the interval of an active timer changes its **timerId** ().

        **See also** **singleShot** .
        """
        ...
    def isActive(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtimer.html#isActive

        **bool QTimer::isActive() const**

        Returns `true` if the timer is running (pending); otherwise returns
        false.

        **Note:** Getter function for property **active** .
        """
        ...
    def isSingleShot(self) -> bool: ...
    def killTimer(self, arg__1: int) -> None: ...
    def remainingTime(self) -> int:
        """
        https://doc.qt.io/qt-6/qtimer.html#remainingTime-prop

        **[read-only, since 5.0] remainingTime : const int**

        This property holds the remaining time in milliseconds

        Returns the timer's remaining value in milliseconds left until the
        timeout. If the timer is inactive, the returned value will be -1. If the
        timer is overdue, the returned value will be 0.

        This property was introduced in Qt 5.0.

        **Access functions:**

        int **remainingTime** () const

        **See also** **interval** .
        """
        ...
    def setInterval(self, msec: int) -> None:
        """
        https://doc.qt.io/qt-6/qtimer.html#interval-prop

        **[bindable] interval : int**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the timeout interval in milliseconds

        The default value for this property is 0. A **QTimer**  with a timeout
        interval of 0 will time out as soon as all the events in the window
        system's event queue have been processed.

        Setting the interval of an active timer changes its **timerId** ().

        **See also** **singleShot** .
        """
        ...
    def setSingleShot(self, singleShot: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtimer.html#singleShot

        **[static] void QTimer::singleShot(int msec , const QObject * receiver ,
        const char * member )**

        This static function calls a slot after a given time interval.

        It is very convenient to use this function because you do not need to
        bother with a **timerEvent**  or create a local **QTimer**  object.

        Example:

        #include <QApplication>
            #include <QTimer>

            int main(int
        argc, char *argv[])
            {
                **QApplication**  app(argc, argv);
        **QTimer** ::singleShot(600000, &app, SLOT(quit()));
                ...
        return app.exec();
            }

        This sample program automatically terminates after 10 minutes (600,000
        milliseconds).

        The **receiver** is the receiving object and the **member** is the slot.
        The time interval is **msec** milliseconds.

        **Note:** This function is **reentrant** .

        **See also** **setSingleShot** () and **start** ().
        """
        ...
    def setTimerType(self, atype: PySide6.QtCore.Qt.TimerType) -> None:
        """
        https://doc.qt.io/qt-6/qtimer.html#timerType-prop

        **[bindable] timerType : Qt::TimerType**

        **Note:** This property supports **QProperty**  bindings.

        controls the accuracy of the timer

        The default value for this property is `Qt::CoarseTimer`.

        **See also** **Qt::TimerType** .

        **Member Function Documentation**
        """
        ...
    @overload
    @staticmethod
    def singleShot(arg__1: int, arg__2: Callable) -> None:
        """
        https://doc.qt.io/qt-6/qtimer.html#singleShot-prop

        **[bindable] singleShot : bool**

        **Note:** This property supports **QProperty**  bindings.

        This property holds whether the timer is a single-shot timer

        A single-shot timer fires only once, non-single-shot timers fire every
        **interval**  milliseconds.

        The default value for this property is `false`.

        **See also** **interval**  and **singleShot** ().
        """
        ...
    @overload
    @staticmethod
    def singleShot(msec: int, receiver: PySide6.QtCore.QObject, member: bytes) -> None:
        """
        https://doc.qt.io/qt-6/qtimer.html#singleShot-1

        **[static] void QTimer::singleShot(int msec , Qt::TimerType timerType ,
        const QObject * receiver , const char * member )**

        This is an overloaded function.

        This static function calls a slot after a given time interval.

        It is very convenient to use this function because you do not need to
        bother with a **timerEvent**  or create a local **QTimer**  object.

        The **receiver** is the receiving object and the **member** is the slot.
        The time interval is **msec** milliseconds. The **timerType** affects
        the accuracy of the timer.

        **Note:** This function is **reentrant** .

        **See also** **start** ().
        """
        ...
    @overload
    @staticmethod
    def singleShot(
        msec: int,
        timerType: PySide6.QtCore.Qt.TimerType,
        receiver: PySide6.QtCore.QObject,
        member: bytes,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtimer.html#singleShot-2

        **[static, since 5.4] template <typename PointerToMemberFunction> void
        QTimer::singleShot(int msec , const QObject * receiver ,
        PointerToMemberFunction method )**

        This is an overloaded function.

        This static function calls a member function of a **QObject**  after a
        given time interval.

        It is very convenient to use this function because you do not need to
        bother with a **timerEvent**  or create a local **QTimer**  object.

        The **receiver** is the receiving object and the **method** is the
        member function. The time interval is **msec** milliseconds.

        If **receiver** is destroyed before the interval occurs, the method will
        not be called. The function will be run in the thread of **receiver**.
        The receiver's thread must have a running Qt event loop.

        **Note:** This function is **reentrant** .

        This function was introduced in Qt 5.4.

        **See also** **start** ().
        """
        ...
    @overload
    def start(self) -> None:
        """
        https://doc.qt.io/qt-6/qtimer.html#start

        **[slot] void QTimer::start(int msec )**

        Starts or restarts the timer with a timeout interval of **msec**
        milliseconds.

        If the timer is already running, it will be **stopped**  and restarted.

        If **singleShot**  is true, the timer will be activated only once.
        """
        ...
    @overload
    def start(self, msec: int) -> None:
        """
        https://doc.qt.io/qt-6/qtimer.html#start-1

        **[slot] void QTimer::start()**

        This function overloads start().

        Starts or restarts the timer with the timeout specified in **interval**
        .

        If the timer is already running, it will be **stopped**  and restarted.

        If **singleShot**  is true, the timer will be activated only once.
        """
        ...
    def stop(self) -> None:
        """
        https://doc.qt.io/qt-6/qtimer.html#stop

        **[slot] void QTimer::stop()**

        Stops the timer.

        **See also** **start** ().
        """
        ...
    def timerEvent(self, arg__1: PySide6.QtCore.QTimerEvent) -> None:
        """
        https://doc.qt.io/qt-6/qtimer.html#timerEvent

        **[override virtual protected] void QTimer::timerEvent(QTimerEvent * e
        )**

        Reimplements: **QObject::timerEvent** (QTimerEvent *event).
        """
        ...
    def timerId(self) -> int:
        """
        https://doc.qt.io/qt-6/qtimer.html#timerId

        **int QTimer::timerId() const**

        Returns the ID of the timer if the timer is running; otherwise returns
        -1.
        """
        ...
    def timerType(self) -> PySide6.QtCore.Qt.TimerType:
        """
        https://doc.qt.io/qt-6/qtimer.html#timerType-prop

        **[bindable] timerType : Qt::TimerType**

        **Note:** This property supports **QProperty**  bindings.

        controls the accuracy of the timer

        The default value for this property is `Qt::CoarseTimer`.

        **See also** **Qt::TimerType** .

        **Member Function Documentation**
        """
        ...
    @property
    def timeout(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtimer.html#timeout

        **[private signal] void QTimer::timeout()**

        This signal is emitted when the timer times out.

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.

        **See also** **interval** , **start** (), and **stop** ().
        """
        ...
