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

class QMutexLocker:
    """
    https://doc.qt.io/qt-6/qmutexlocker.html

    **Detailed Description**

    Locking and unlocking a **QMutex**  or **QRecursiveMutex**  in complex
    functions and statements or in exception handling code is error-prone and
    difficult to debug. QMutexLocker can be used in such situations to ensure
    that the state of the mutex is always well-defined.

    QMutexLocker should be created within a function where a **QMutex**  needs
    to be locked. The mutex is locked when QMutexLocker is created. You can
    unlock and relock the mutex with `unlock()` and `relock()`. If locked, the
    mutex will be unlocked when the QMutexLocker is destroyed.

    For example, this complex function locks a **QMutex**  upon entering the
    function and unlocks the mutex at all the exit points:

    int complexFunction(int flag)
        {
            mutex.lock();

            int
    retVal = 0;

            switch (flag) {
            case 0:
            case 1:
    retVal = moreComplexFunction(flag);
                break;
            case 2:
    {
                    int status = anotherFunction();
                    if (status
    < 0) {
                        mutex.unlock();
                        return -2;
    }
                    retVal = status + flag;
                }
                break;
    default:
                if (flag > 10) {
                    mutex.unlock();
    return -1;
                }
                break;
            }
    mutex.unlock();
            return retVal;
        }

    This example function will get more complicated as it is developed, which
    increases the likelihood that errors will occur.

    Using QMutexLocker greatly simplifies the code, and makes it more readable:

    int complexFunction(int flag)
        {
            **QMutexLocker**
    locker(&mutex);

            int retVal = 0;

            switch (flag) {
    case 0:
            case 1:
                return moreComplexFunction(flag);
    case 2:
                {
                    int status = anotherFunction();
    if (status < 0)
                        return -2;
                    retVal =
    status + flag;
                }
                break;
            default:
    if (flag > 10)
                    return -1;
                break;
            }
    return retVal;
        }

    Now, the mutex will always be unlocked when the QMutexLocker object is
    destroyed (when the function returns since `locker` is an auto variable).

    The same principle applies to code that throws and catches exceptions. An
    exception that is not caught in the function that has locked the mutex has
    no way of unlocking the mutex before the exception is passed up the stack to
    the calling function.

    QMutexLocker also provides a `mutex()` member function that returns the
    mutex on which the QMutexLocker is operating. This is useful for code that
    needs access to the mutex, such as **QWaitCondition::wait** (). For example:

    class SignalWaiter
        {
        private:
            **QMutexLocker** <**QMutex** >
    locker;

        public:
            SignalWaiter(**QMutex**  *mutex)
    : locker(mutex)
            {
            }

            void waitForSignal()
    {
                ...
                while (!signalled)
    waitCondition.wait(locker.mutex());
                ...
            }
        };

    **See also** **QReadLocker** , **QWriteLocker** , and **QMutex** .
    """

    @overload
    def __init__(self, m: PySide6.QtCore.QMutex) -> None:
        """
        https://doc.qt.io/qt-6/qmutexlocker.html#QMutexLocker

        **QMutexLocker::QMutexLocker(Mutex * mutex )**

        Constructs a QMutexLocker and locks **mutex**. The mutex will be
        unlocked when the QMutexLocker is destroyed. If **mutex** is `nullptr`,
        QMutexLocker does nothing.

        **See also** **QMutex::lock** ().
        """
        ...
    @overload
    def __init__(self, m: PySide6.QtCore.QRecursiveMutex) -> None:
        """
        https://doc.qt.io/qt-6/qmutexlocker.html#QMutexLocker

        **QMutexLocker::QMutexLocker(Mutex * mutex )**

        Constructs a QMutexLocker and locks **mutex**. The mutex will be
        unlocked when the QMutexLocker is destroyed. If **mutex** is `nullptr`,
        QMutexLocker does nothing.

        **See also** **QMutex::lock** ().
        """
        ...
    def __enter__(self) -> None: ...
    def __exit__(self, arg__1: object, arg__2: object, arg__3: object) -> None: ...
    def mutex(self) -> PySide6.QtCore.QMutex:
        """
        https://doc.qt.io/qt-6/qmutexlocker.html#mutex

        **Mutex *QMutexLocker::mutex() const**

        Returns the mutex on which the **QMutexLocker**  is operating.
        """
        ...
    def recursiveMutex(self) -> PySide6.QtCore.QRecursiveMutex: ...
    def relock(self) -> None:
        """
        https://doc.qt.io/qt-6/qmutexlocker.html#relock

        **void QMutexLocker::relock()**

        Relocks an unlocked mutex locker.

        **See also** **unlock** ().
        """
        ...
    def unlock(self) -> None:
        """
        https://doc.qt.io/qt-6/qmutexlocker.html#unlock

        **void QMutexLocker::unlock()**

        Unlocks this mutex locker. You can use `relock()` to lock it again. It
        does not need to be locked when destroyed.

        **See also** **relock** ().
        """
        ...
