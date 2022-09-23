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

class QTime:
    """
    https://doc.qt.io/qt-6/qtime.html

    **Detailed Description**

    A QTime object contains a clock time, which it can express as the numbers of
    hours, minutes, seconds, and milliseconds since midnight. It provides
    functions for comparing times and for manipulating a time by adding a number
    of milliseconds. QTime objects should be passed by value rather than by
    reference to const; they simply package `int`.

    QTime uses the 24-hour clock format; it has no concept of AM/PM. Unlike
    **QDateTime** , QTime knows nothing about time zones or daylight-saving time
    (DST).

    A QTime object is typically created either by giving the number of hours,
    minutes, seconds, and milliseconds explicitly, or by using the static
    function **currentTime** (), which creates a QTime object that represents
    the system's local time.

    The **hour** (), **minute** (), **second** (), and **msec** () functions
    provide access to the number of hours, minutes, seconds, and milliseconds of
    the time. The same information is provided in textual format by the
    **toString** () function.

    The **addSecs** () and **addMSecs** () functions provide the time a given
    number of seconds or milliseconds later than a given time. Correspondingly,
    the number of seconds or milliseconds between two times can be found using
    **secsTo** () or **msecsTo** ().

    QTime provides a full set of operators to compare two QTime objects; an
    earlier time is considered smaller than a later one; if A.**msecsTo** (B) is
    positive, then A < B.

    QTime objects can also be created from a text representation using
    **fromString** () and converted to a string representation using
    **toString** (). All conversion to and from string formats is done using the
    C locale. For localized conversions, see **QLocale** .

    **See also** **QDate**  and **QDateTime** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qtime.html#QTime-1

        **QTime::QTime()**

        Constructs a null time object. For a null time, **isNull** () returns
        `true` and **isValid** () returns `false`. If you need a zero time, use
        QTime(0, 0). For the start of a day, see **QDate::startOfDay** ().

        **See also** **isNull** () and **isValid** ().
        """
        ...
    @overload
    def __init__(self, QTime: PySide6.QtCore.QTime) -> None:
        """
        https://doc.qt.io/qt-6/qtime.html#QTime-2

        **QTime::QTime(int h , int m , int s = 0, int ms = 0)**

        Constructs a time with hour **h** , minute **m** , seconds **s** and
        milliseconds **ms**.

        **h** must be in the range 0 to 23, **m** and **s** must be in the range
        0 to 59, and **ms** must be in the range 0 to 999.

        **See also** **isValid** ().
        """
        ...
    @overload
    def __init__(self, h: int, m: int, s: int = ..., ms: int = ...) -> None:
        """
        https://doc.qt.io/qt-6/qtime.html#QTime-1

        **QTime::QTime()**

        Constructs a null time object. For a null time, **isNull** () returns
        `true` and **isValid** () returns `false`. If you need a zero time, use
        QTime(0, 0). For the start of a day, see **QDate::startOfDay** ().

        **See also** **isNull** () and **isValid** ().
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def addMSecs(self, ms: int) -> PySide6.QtCore.QTime:
        """
        https://doc.qt.io/qt-6/qtime.html#addMSecs

        **QTime QTime::addMSecs(int ms ) const**

        Returns a **QTime**  object containing a time **ms** milliseconds later
        than the time of this object (or earlier if **ms** is negative).

        Note that the time will wrap if it passes midnight. See **addSecs** ()
        for an example.

        Returns a null time if this time is invalid.

        **See also** **addSecs** (), **msecsTo** (), and **QDateTime::addMSecs**
        ().
        """
        ...
    def addSecs(self, secs: int) -> PySide6.QtCore.QTime:
        """
        https://doc.qt.io/qt-6/qtime.html#addSecs

        **QTime QTime::addSecs(int s ) const**

        Returns a **QTime**  object containing a time **s** seconds later than
        the time of this object (or earlier if **s** is negative).

        Note that the time will wrap if it passes midnight.

        Returns a null time if this time is invalid.

        Example:

        QTime n(14, 0, 0);                // n == 14:00:00
            QTime t;
            t =
        n.addSecs(70);                // t == 14:01:10
            t = n.addSecs(-70);
        // t == 13:58:50
            t = n.addSecs(10 * 60 * 60 + 5);  // t == 00:00:05
        t = n.addSecs(-15 * 60 * 60);     // t == 23:00:00

        **See also** **addMSecs** (), **secsTo** (), and **QDateTime::addSecs**
        ().
        """
        ...
    @staticmethod
    def currentTime() -> PySide6.QtCore.QTime:
        """
        https://doc.qt.io/qt-6/qtime.html#currentTime

        **[static] QTime QTime::currentTime()**

        Returns the current time as reported by the system clock.

        Note that the accuracy depends on the accuracy of the underlying
        operating system; not all systems provide 1-millisecond accuracy.

        Furthermore, currentTime() only increases within each day; it shall drop
        by 24 hours each time midnight passes; and, beside this, changes in it
        may not correspond to elapsed time, if a daylight-saving transition
        intervenes.

        **See also** **QDateTime::currentDateTime** () and
        **QDateTime::currentDateTimeUtc** ().
        """
        ...
    @staticmethod
    def fromMSecsSinceStartOfDay(msecs: int) -> PySide6.QtCore.QTime:
        """
        https://doc.qt.io/qt-6/qtime.html#fromMSecsSinceStartOfDay

        **[static] QTime QTime::fromMSecsSinceStartOfDay(int msecs )**

        Returns a new **QTime**  instance with the time set to the number of
        **msecs** since the start of the day, i.e. since 00:00:00.

        If **msecs** falls outside the valid range an invalid **QTime**  will be
        returned.

        **See also** **msecsSinceStartOfDay** ().
        """
        ...
    @overload
    @staticmethod
    def fromString(
        string: str, format: PySide6.QtCore.Qt.DateFormat = ...
    ) -> PySide6.QtCore.QTime:
        """
        https://doc.qt.io/qt-6/qtime.html#fromString

        **[static] QTime QTime::fromString(const QString & string ,
        Qt::DateFormat format = Qt::TextDate)**

        Returns the time represented in the **string** as a **QTime**  using the
        **format** given, or an invalid time if this is not possible.

        **See also** **toString** () and **QLocale::toTime** ().
        """
        ...
    @overload
    @staticmethod
    def fromString(string: str, format: str) -> PySide6.QtCore.QTime:
        """
        https://doc.qt.io/qt-6/qtime.html#fromString-1

        **[static, since 6.0] QTime QTime::fromString(QStringView string ,
        Qt::DateFormat format = Qt::TextDate)**

        This is an overloaded function.

        This function was introduced in Qt 6.0.
        """
        ...
    def hour(self) -> int:
        """
        https://doc.qt.io/qt-6/qtime.html#hour

        **int QTime::hour() const**

        Returns the hour part (0 to 23) of the time.

        Returns -1 if the time is invalid.

        **See also** **minute** (), **second** (), and **msec** ().
        """
        ...
    def isNull(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtime.html#isNull

        **bool QTime::isNull() const**

        Returns `true` if the time is null (i.e., the **QTime**  object was
        constructed using the default constructor); otherwise returns false. A
        null time is also an invalid time.

        **See also** **isValid** ().
        """
        ...
    @overload
    @staticmethod
    def isValid(h: int, m: int, s: int, ms: int = ...) -> bool:
        """
        https://doc.qt.io/qt-6/qtime.html#isValid

        **bool QTime::isValid() const**

        Returns `true` if the time is valid; otherwise returns `false`. For
        example, the time 23:30:55.746 is valid, but 24:12:30 is invalid.

        **See also** **isNull** ().
        """
        ...
    @overload
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtime.html#isValid-1

        **[static] bool QTime::isValid(int h , int m , int s , int ms = 0)**

        This is an overloaded function.

        Returns `true` if the specified time is valid; otherwise returns false.

        The time is valid if **h** is in the range 0 to 23, **m** and **s** are
        in the range 0 to 59, and **ms** is in the range 0 to 999.

        Example:

        QTime::isValid(21, 10, 30); // returns true
            QTime::isValid(22, 5,
        62); // returns false
        """
        ...
    def minute(self) -> int:
        """
        https://doc.qt.io/qt-6/qtime.html#minute

        **int QTime::minute() const**

        Returns the minute part (0 to 59) of the time.

        Returns -1 if the time is invalid.

        **See also** **hour** (), **second** (), and **msec** ().
        """
        ...
    def msec(self) -> int:
        """
        https://doc.qt.io/qt-6/qtime.html#msec

        **int QTime::msec() const**

        Returns the millisecond part (0 to 999) of the time.

        Returns -1 if the time is invalid.

        **See also** **hour** (), **minute** (), and **second** ().
        """
        ...
    def msecsSinceStartOfDay(self) -> int:
        """
        https://doc.qt.io/qt-6/qtime.html#msecsSinceStartOfDay

        **int QTime::msecsSinceStartOfDay() const**

        Returns the number of msecs since the start of the day, i.e. since
        00:00:00.

        **See also** **fromMSecsSinceStartOfDay** ().
        """
        ...
    def msecsTo(self, t: PySide6.QtCore.QTime) -> int:
        """
        https://doc.qt.io/qt-6/qtime.html#msecsTo

        **int QTime::msecsTo(QTime t ) const**

        Returns the number of milliseconds from this time to **t**. If **t** is
        earlier than this time, the number of milliseconds returned is negative.

        Because **QTime**  measures time within a day and there are 86400
        seconds in a day, the result is always between -86400000 and 86400000
        ms.

        Returns 0 if either time is invalid.

        **See also** **secsTo** (), **addMSecs** (), and **QDateTime::msecsTo**
        ().
        """
        ...
    def second(self) -> int:
        """
        https://doc.qt.io/qt-6/qtime.html#second

        **int QTime::second() const**

        Returns the second part (0 to 59) of the time.

        Returns -1 if the time is invalid.

        **See also** **hour** (), **minute** (), and **msec** ().
        """
        ...
    def secsTo(self, t: PySide6.QtCore.QTime) -> int:
        """
        https://doc.qt.io/qt-6/qtime.html#secsTo

        **int QTime::secsTo(QTime t ) const**

        Returns the number of seconds from this time to **t**. If **t** is
        earlier than this time, the number of seconds returned is negative.

        Because **QTime**  measures time within a day and there are 86400
        seconds in a day, the result is always between -86400 and 86400.

        secsTo() does not take into account any milliseconds.

        Returns 0 if either time is invalid.

        **See also** **addSecs** () and **QDateTime::secsTo** ().
        """
        ...
    def setHMS(self, h: int, m: int, s: int, ms: int = ...) -> bool:
        """
        https://doc.qt.io/qt-6/qtime.html#setHMS

        **bool QTime::setHMS(int h , int m , int s , int ms = 0)**

        Sets the time to hour **h** , minute **m** , seconds **s** and
        milliseconds **ms**.

        **h** must be in the range 0 to 23, **m** and **s** must be in the range
        0 to 59, and **ms** must be in the range 0 to 999. Returns `true` if the
        set time is valid; otherwise returns `false`.

        **See also** **isValid** ().
        """
        ...
    def toPython(self) -> object: ...
    @overload
    def toString(self, f: PySide6.QtCore.Qt.DateFormat = ...) -> str:
        """
        https://doc.qt.io/qt-6/qtime.html#toString-1

        **QString QTime::toString(Qt::DateFormat format = Qt::TextDate) const**

        This is an overloaded function.

        Returns the time as a string. The **format** parameter determines the
        format of the string.

        If **format** is **Qt::TextDate** , the string format is HH:mm:ss; e.g.
        1 second before midnight would be "23:59:59".

        If **format** is **Qt::ISODate** , the string format corresponds to the
        ISO 8601 extended specification for representations of dates,
        represented by HH:mm:ss. To include milliseconds in the ISO 8601 date,
        use the **format** **Qt::ISODateWithMs** , which corresponds to
        HH:mm:ss.zzz.

        If the **format** is **Qt::RFC2822Date** , the string is formatted in an
        **RFC 2822**  compatible way. An example of this formatting is
        "23:59:20".

        If the time is invalid, an empty string will be returned.

        **See also** **fromString** (), **QDate::toString** (),
        **QDateTime::toString** (), and **QLocale::toString** ().
        """
        ...
    @overload
    def toString(self, format: str) -> str:
        """
        https://doc.qt.io/qt-6/qtime.html#toString-1

        **QString QTime::toString(Qt::DateFormat format = Qt::TextDate) const**

        This is an overloaded function.

        Returns the time as a string. The **format** parameter determines the
        format of the string.

        If **format** is **Qt::TextDate** , the string format is HH:mm:ss; e.g.
        1 second before midnight would be "23:59:59".

        If **format** is **Qt::ISODate** , the string format corresponds to the
        ISO 8601 extended specification for representations of dates,
        represented by HH:mm:ss. To include milliseconds in the ISO 8601 date,
        use the **format** **Qt::ISODateWithMs** , which corresponds to
        HH:mm:ss.zzz.

        If the **format** is **Qt::RFC2822Date** , the string is formatted in an
        **RFC 2822**  compatible way. An example of this formatting is
        "23:59:20".

        If the time is invalid, an empty string will be returned.

        **See also** **fromString** (), **QDate::toString** (),
        **QDateTime::toString** (), and **QLocale::toString** ().
        """
        ...
