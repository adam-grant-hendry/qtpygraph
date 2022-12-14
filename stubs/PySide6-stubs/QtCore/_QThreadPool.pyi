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

class QThreadPool(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qthreadpool.html

    **Detailed Description**

    QThreadPool manages and recycles individual **QThread**  objects to help
    reduce thread creation costs in programs that use threads. Each Qt
    application has one global QThreadPool object, which can be accessed by
    calling **globalInstance** ().

    To use one of the QThreadPool threads, subclass **QRunnable**  and implement
    the run() virtual function. Then create an object of that class and pass it
    to **QThreadPool::start** ().

    class HelloWorldTask : public **QRunnable**
        {
            void run()
    override
            {
                **qDebug** () << "Hello world from thread" <<
    **QThread** ::currentThread();
            }
        };

        HelloWorldTask
    *hello = new HelloWorldTask();
        // QThreadPool takes ownership and
    deletes 'hello' automatically
        **QThreadPool**
    ::globalInstance()->start(hello);

    QThreadPool deletes the **QRunnable**  automatically by default. Use
    **QRunnable::setAutoDelete** () to change the auto-deletion flag.

    QThreadPool supports executing the same **QRunnable**  more than once by
    calling **tryStart** (this) from within **QRunnable::run** (). If autoDelete
    is enabled the **QRunnable**  will be deleted when the last thread exits the
    run function. Calling **start** () multiple times with the same
    **QRunnable**  when autoDelete is enabled creates a race condition and is
    not recommended.

    Threads that are unused for a certain amount of time will expire. The
    default expiry timeout is 30000 milliseconds (30 seconds). This can be
    changed using **setExpiryTimeout** (). Setting a negative expiry timeout
    disables the expiry mechanism.

    Call **maxThreadCount** () to query the maximum number of threads to be
    used. If needed, you can change the limit with **setMaxThreadCount** (). The
    default **maxThreadCount** () is **QThread::idealThreadCount** (). The
    **activeThreadCount** () function returns the number of threads currently
    doing work.

    The **reserveThread** () function reserves a thread for external use. Use
    **releaseThread** () when your are done with the thread, so that it may be
    reused. Essentially, these functions temporarily increase or reduce the
    active thread count and are useful when implementing time-consuming
    operations that are not visible to the QThreadPool.

    Note that QThreadPool is a low-level class for managing threads, see the Qt
    Concurrent module for higher level alternatives.

    **See also** **QRunnable** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#QThreadPool

        **QThreadPool::QThreadPool(QObject * parent = nullptr)**

        Constructs a thread pool with the given **parent**.
        """
        ...
    def activeThreadCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#activeThreadCount-prop

        **[read-only] activeThreadCount : const int**

        This property holds the number of active threads in the thread pool.

        **Note:** It is possible for this function to return a value that is
        greater than **maxThreadCount** (). See **reserveThread** () for more
        details.

        **Access functions:**

        int **activeThreadCount** () const

        **See also** **reserveThread** () and **releaseThread** ().
        """
        ...
    def clear(self) -> None:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#clear

        **[since 5.2] void QThreadPool::clear()**

        Removes the runnables that are not yet started from the queue. The
        runnables for which **runnable->autoDelete** () returns `true` are
        deleted.

        This function was introduced in Qt 5.2.

        **See also** **start** ().
        """
        ...
    def contains(self, thread: PySide6.QtCore.QThread) -> bool:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#contains

        **[since 6.0] bool QThreadPool::contains(const QThread * thread )
        const**

        Returns `true` if **thread** is a thread managed by this thread pool.

        This function was introduced in Qt 6.0.
        """
        ...
    def expiryTimeout(self) -> int:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#expiryTimeout-prop

        **expiryTimeout : int**

        This property holds the thread expiry timeout value in milliseconds.

        Threads that are unused for **expiryTimeout** milliseconds are
        considered to have expired and will exit. Such threads will be restarted
        as needed. The default **expiryTimeout** is 30000 milliseconds (30
        seconds). If **expiryTimeout** is negative, newly created threads will
        not expire, e.g., they will not exit until the thread pool is destroyed.

        Note that setting **expiryTimeout** has no effect on already running
        threads. Only newly created threads will use the new **expiryTimeout**.
        We recommend setting the **expiryTimeout** immediately after creating
        the thread pool, but before calling **start** ().

        **Access functions:**

        int **expiryTimeout** () const
        void **setExpiryTimeout** (int
        **expiryTimeout** )
        """
        ...
    @staticmethod
    def globalInstance() -> PySide6.QtCore.QThreadPool:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#globalInstance

        **[static] QThreadPool *QThreadPool::globalInstance()**

        Returns the global **QThreadPool**  instance.
        """
        ...
    def maxThreadCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#maxThreadCount-prop

        **maxThreadCount : int**

        This property holds the maximum number of threads used by the thread
        pool. This property will default to the value of
        **QThread::idealThreadCount** () at the moment the **QThreadPool**
        object is created.

        **Note:** The thread pool will always use at least 1 thread, even if
        **maxThreadCount** limit is zero or negative.

        The default **maxThreadCount** is **QThread::idealThreadCount** ().

        **Access functions:**

        int **maxThreadCount** () const
        void **setMaxThreadCount** (int
        **maxThreadCount** )
        """
        ...
    def releaseThread(self) -> None:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#releaseThread

        **void QThreadPool::releaseThread()**

        Releases a thread previously reserved by a call to **reserveThread** ().

        **Note:** Calling this function without previously reserving a thread
        temporarily increases **maxThreadCount** (). This is useful when a
        thread goes to sleep waiting for more work, allowing other threads to
        continue. Be sure to call **reserveThread** () when done waiting, so
        that the thread pool can correctly maintain the **activeThreadCount**
        ().

        **See also** **reserveThread** ().
        """
        ...
    def reserveThread(self) -> None:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#reserveThread

        **void QThreadPool::reserveThread()**

        Reserves one thread, disregarding **activeThreadCount** () and
        **maxThreadCount** ().

        Once you are done with the thread, call **releaseThread** () to allow it
        to be reused.

        **Note:** Even if reserving **maxThreadCount** () threads or more, the
        thread pool will still allow a minimum of one thread.

        **Note:** This function will increase the reported number of active
        threads. This means that by using this function, it is possible for
        **activeThreadCount** () to return a value greater than
        **maxThreadCount** () .

        **See also** **releaseThread** ().
        """
        ...
    def setExpiryTimeout(self, expiryTimeout: int) -> None:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#expiryTimeout-prop

        **expiryTimeout : int**

        This property holds the thread expiry timeout value in milliseconds.

        Threads that are unused for **expiryTimeout** milliseconds are
        considered to have expired and will exit. Such threads will be restarted
        as needed. The default **expiryTimeout** is 30000 milliseconds (30
        seconds). If **expiryTimeout** is negative, newly created threads will
        not expire, e.g., they will not exit until the thread pool is destroyed.

        Note that setting **expiryTimeout** has no effect on already running
        threads. Only newly created threads will use the new **expiryTimeout**.
        We recommend setting the **expiryTimeout** immediately after creating
        the thread pool, but before calling **start** ().

        **Access functions:**

        int **expiryTimeout** () const
        void **setExpiryTimeout** (int
        **expiryTimeout** )
        """
        ...
    def setMaxThreadCount(self, maxThreadCount: int) -> None:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#maxThreadCount-prop

        **maxThreadCount : int**

        This property holds the maximum number of threads used by the thread
        pool. This property will default to the value of
        **QThread::idealThreadCount** () at the moment the **QThreadPool**
        object is created.

        **Note:** The thread pool will always use at least 1 thread, even if
        **maxThreadCount** limit is zero or negative.

        The default **maxThreadCount** is **QThread::idealThreadCount** ().

        **Access functions:**

        int **maxThreadCount** () const
        void **setMaxThreadCount** (int
        **maxThreadCount** )
        """
        ...
    def setStackSize(self, stackSize: int) -> None:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#stackSize-prop

        **[since 5.10] stackSize : uint**

        This property holds the stack size for the thread pool worker threads.

        The value of the property is only used when the thread pool creates new
        threads. Changing it has no effect for already created or running
        threads.

        The default value is 0, which makes **QThread**  use the operating
        system default stack size.

        This property was introduced in Qt 5.10.

        **Access functions:**

        uint **stackSize** () const
        void **setStackSize** (uint **stackSize**
        )
        """
        ...
    def setThreadPriority(self, priority: PySide6.QtCore.QThread.Priority) -> None:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#threadPriority-prop

        **[since 6.2] threadPriority : QThread::Priority**

        This property holds the thread priority for new worker threads.

        The value of the property is only used when the thread pool starts new
        threads. Changing it has no effect for already running threads.

        The default value is **QThread::InheritPriority** , which makes
        **QThread**  use the same priority as the one the **QThreadPool**
        object lives in.

        This property was introduced in Qt 6.2.

        **Access functions:**

        QThread::Priority **threadPriority** () const
        void
        **setThreadPriority** (QThread::Priority **priority** )

        **See also** **QThread::Priority** .

        **Member Function Documentation**
        """
        ...
    def stackSize(self) -> int:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#stackSize-prop

        **[since 5.10] stackSize : uint**

        This property holds the stack size for the thread pool worker threads.

        The value of the property is only used when the thread pool creates new
        threads. Changing it has no effect for already created or running
        threads.

        The default value is 0, which makes **QThread**  use the operating
        system default stack size.

        This property was introduced in Qt 5.10.

        **Access functions:**

        uint **stackSize** () const
        void **setStackSize** (uint **stackSize**
        )
        """
        ...
    @overload
    def start(self, arg__1: Callable, priority: int = ...) -> None:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#start

        **void QThreadPool::start(QRunnable * runnable , int priority = 0)**

        Reserves a thread and uses it to run **runnable** , unless this thread
        will make the current thread count exceed **maxThreadCount** (). In that
        case, **runnable** is added to a run queue instead. The **priority**
        argument can be used to control the run queue's order of execution.

        Note that the thread pool takes ownership of the **runnable** if
        **runnable->autoDelete** () returns `true`, and the **runnable** will be
        deleted automatically by the thread pool after the **runnable->run** ()
        returns. If **runnable->autoDelete** () returns `false`, ownership of
        **runnable** remains with the caller. Note that changing the auto-
        deletion on **runnable** after calling this functions results in
        undefined behavior.
        """
        ...
    @overload
    def start(self, runnable: PySide6.QtCore.QRunnable, priority: int = ...) -> None:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#start-1

        **[since 5.15] void QThreadPool::start(std::function<void ()>
        functionToRun , int priority = 0)**

        This is an overloaded function.

        Reserves a thread and uses it to run **functionToRun** , unless this
        thread will make the current thread count exceed **maxThreadCount** ().
        In that case, **functionToRun** is added to a run queue instead. The
        **priority** argument can be used to control the run queue's order of
        execution.

        This function was introduced in Qt 5.15.
        """
        ...
    def threadPriority(self) -> PySide6.QtCore.QThread.Priority:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#threadPriority-prop

        **[since 6.2] threadPriority : QThread::Priority**

        This property holds the thread priority for new worker threads.

        The value of the property is only used when the thread pool starts new
        threads. Changing it has no effect for already running threads.

        The default value is **QThread::InheritPriority** , which makes
        **QThread**  use the same priority as the one the **QThreadPool**
        object lives in.

        This property was introduced in Qt 6.2.

        **Access functions:**

        QThread::Priority **threadPriority** () const
        void
        **setThreadPriority** (QThread::Priority **priority** )

        **See also** **QThread::Priority** .

        **Member Function Documentation**
        """
        ...
    @overload
    def tryStart(self, arg__1: Callable) -> bool:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#tryStart

        **bool QThreadPool::tryStart(QRunnable * runnable )**

        Attempts to reserve a thread to run **runnable**.

        If no threads are available at the time of calling, then this function
        does nothing and returns `false`. Otherwise, **runnable** is run
        immediately using one available thread and this function returns `true`.

        Note that on success the thread pool takes ownership of the **runnable**
        if **runnable->autoDelete** () returns `true`, and the **runnable** will
        be deleted automatically by the thread pool after the **runnable->run**
        () returns. If **runnable->autoDelete** () returns `false`, ownership of
        **runnable** remains with the caller. Note that changing the auto-
        deletion on **runnable** after calling this function results in
        undefined behavior.
        """
        ...
    @overload
    def tryStart(self, runnable: PySide6.QtCore.QRunnable) -> bool:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#tryStart-1

        **[since 5.15] bool QThreadPool::tryStart(std::function<void ()>
        functionToRun )**

        This is an overloaded function.

        Attempts to reserve a thread to run **functionToRun**.

        If no threads are available at the time of calling, then this function
        does nothing and returns `false`. Otherwise, **functionToRun** is run
        immediately using one available thread and this function returns `true`.

        This function was introduced in Qt 5.15.
        """
        ...
    def tryTake(self, runnable: PySide6.QtCore.QRunnable) -> bool:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#tryTake

        **[since 5.9] bool QThreadPool::tryTake(QRunnable * runnable )**

        Attempts to remove the specified **runnable** from the queue if it is
        not yet started. If the runnable had not been started, returns `true`,
        and ownership of **runnable** is transferred to the caller (even when
        `runnable->autoDelete() == true`). Otherwise returns `false`.

        **Note:** If `runnable->autoDelete() == true`, this function may remove
        the wrong runnable. This is known as the **ABA problem** : the original
        **runnable** may already have executed and has since been deleted. The
        memory is re-used for another runnable, which then gets removed instead
        of the intended one. For this reason, we recommend calling this function
        only for runnables that are not auto-deleting.

        This function was introduced in Qt 5.9.

        **See also** **start** () and **QRunnable::autoDelete** ().
        """
        ...
    def waitForDone(self, msecs: int = ...) -> bool:
        """
        https://doc.qt.io/qt-6/qthreadpool.html#waitForDone

        **bool QThreadPool::waitForDone(int msecs = -1)**

        Waits up to **msecs** milliseconds for all threads to exit and removes
        all threads from the thread pool. Returns `true` if all threads were
        removed; otherwise it returns `false`. If **msecs** is -1 (the default),
        the timeout is ignored (waits for the last thread to exit).
        """
        ...
