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
PySide6.QtMultimedia, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtMultimedia

class QMediaTimeRange:
    """
    https://doc.qt.io/qt-6/qmediatimerange.html

    **Detailed Description**

    The **earliestTime** (), **latestTime** (), **intervals** () and **isEmpty**
    () methods are used to get information about the current time range.

    The **addInterval** (), **removeInterval** () and **clear** () methods are
    used to modify the current time range.

    When adding or removing intervals from the time range, existing intervals
    within the range may be expanded, trimmed, deleted, merged or split to
    ensure that all intervals within the time range remain distinct and
    disjoint. As a consequence, all intervals added or removed from a time range
    must be **normal** .

    **See also** **QMediaTimeRange::Interval** .
    """

    class Interval:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(
            self, Interval: PySide6.QtMultimedia.QMediaTimeRange.Interval
        ) -> None: ...
        @overload
        def __init__(self, start: int, end: int) -> None: ...
        @staticmethod
        def __copy__() -> None: ...
        def contains(self, time: int) -> bool: ...
        def end(self) -> int: ...
        def isNormal(self) -> bool: ...
        def normalized(self) -> PySide6.QtMultimedia.QMediaTimeRange.Interval: ...
        def start(self) -> int: ...
        def translated(
            self, offset: int
        ) -> PySide6.QtMultimedia.QMediaTimeRange.Interval: ...

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#QMediaTimeRange

        **QMediaTimeRange::QMediaTimeRange()**

        Constructs an empty time range.
        """
        ...
    @overload
    def __init__(self, arg__1: PySide6.QtMultimedia.QMediaTimeRange.Interval) -> None:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#QMediaTimeRange-1

        **QMediaTimeRange::QMediaTimeRange(qint64 start , qint64 end )**

        Constructs a time range that contains an initial interval from **start**
        to **end** inclusive.

        If the interval is not **normal** , the resulting time range will be
        empty.

        **See also** **addInterval** ().
        """
        ...
    @overload
    def __init__(
        self,
        range: (
            PySide6.QtMultimedia.QMediaTimeRange
            | PySide6.QtMultimedia.QMediaTimeRange.Interval
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#QMediaTimeRange-2

        **QMediaTimeRange::QMediaTimeRange(const QMediaTimeRange::Interval &
        interval )**

        Constructs a time range that contains an initial interval, **interval**.

        If **interval** is not **normal** , the resulting time range will be
        empty.

        **See also** **addInterval** ().
        """
        ...
    @overload
    def __init__(self, start: int, end: int) -> None:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#QMediaTimeRange-3

        **QMediaTimeRange::QMediaTimeRange(const QMediaTimeRange & range )**

        Constructs a time range by copying another time **range**.
        """
        ...
    def __add__(
        self,
        r2: (
            PySide6.QtMultimedia.QMediaTimeRange
            | PySide6.QtMultimedia.QMediaTimeRange.Interval
        ),
    ) -> PySide6.QtMultimedia.QMediaTimeRange: ...
    @staticmethod
    def __copy__() -> None: ...
    @overload
    def __iadd__(
        self, arg__1: PySide6.QtMultimedia.QMediaTimeRange.Interval
    ) -> PySide6.QtMultimedia.QMediaTimeRange: ...
    @overload
    def __iadd__(
        self,
        arg__1: (
            PySide6.QtMultimedia.QMediaTimeRange
            | PySide6.QtMultimedia.QMediaTimeRange.Interval
        ),
    ) -> PySide6.QtMultimedia.QMediaTimeRange: ...
    @overload
    def __isub__(
        self, arg__1: PySide6.QtMultimedia.QMediaTimeRange.Interval
    ) -> PySide6.QtMultimedia.QMediaTimeRange: ...
    @overload
    def __isub__(
        self,
        arg__1: (
            PySide6.QtMultimedia.QMediaTimeRange
            | PySide6.QtMultimedia.QMediaTimeRange.Interval
        ),
    ) -> PySide6.QtMultimedia.QMediaTimeRange: ...
    def __sub__(
        self,
        r2: (
            PySide6.QtMultimedia.QMediaTimeRange
            | PySide6.QtMultimedia.QMediaTimeRange.Interval
        ),
    ) -> PySide6.QtMultimedia.QMediaTimeRange: ...
    @overload
    def addInterval(
        self, interval: PySide6.QtMultimedia.QMediaTimeRange.Interval
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#addInterval

        **void QMediaTimeRange::addInterval(const QMediaTimeRange::Interval &
        interval )**

        Adds the specified **interval** to the time range.

        Adding intervals which are not **normal**  is invalid, and will be
        ignored.

        If the specified interval is adjacent to, or overlaps existing intervals
        within the time range, these intervals will be merged.

        This operation takes linear time.

        **See also** **removeInterval** ().
        """
        ...
    @overload
    def addInterval(self, start: int, end: int) -> None:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#addInterval-1

        **void QMediaTimeRange::addInterval(qint64 start , qint64 end )**

        This is an overloaded function.

        Adds the interval specified by **start** and **end** to the time range.

        **See also** **addInterval** ().
        """
        ...
    def addTimeRange(
        self,
        arg__1: (
            PySide6.QtMultimedia.QMediaTimeRange
            | PySide6.QtMultimedia.QMediaTimeRange.Interval
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#addTimeRange

        **void QMediaTimeRange::addTimeRange(const QMediaTimeRange & range )**

        Adds each of the intervals in **range** to this time range.

        Equivalent to calling **addInterval** () for each interval in **range**.
        """
        ...
    def clear(self) -> None:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#clear

        **void QMediaTimeRange::clear()**

        Removes all intervals from the time range.

        **See also** **removeInterval** ().
        """
        ...
    def contains(self, time: int) -> bool:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#contains

        **bool QMediaTimeRange::contains(qint64 time ) const**

        Returns true if the specified **time** lies within the time range.
        """
        ...
    def earliestTime(self) -> int:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#earliestTime

        **qint64 QMediaTimeRange::earliestTime() const**

        Returns the earliest time within the time range.

        For empty time ranges, this value is equal to zero.

        **See also** **latestTime** ().
        """
        ...
    def intervals(self) -> list[PySide6.QtMultimedia.QMediaTimeRange.Interval]:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#intervals

        **QList<QMediaTimeRange::Interval> QMediaTimeRange::intervals() const**

        Returns the list of intervals covered by this time range.
        """
        ...
    def isContinuous(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#isContinuous

        **bool QMediaTimeRange::isContinuous() const**

        Returns true if the time range consists of a continuous interval. That
        is, there is one or fewer disjoint intervals within the time range.
        """
        ...
    def isEmpty(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#isEmpty

        **bool QMediaTimeRange::isEmpty() const**

        Returns true if there are no intervals within the time range.

        **See also** **intervals** ().
        """
        ...
    def latestTime(self) -> int:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#latestTime

        **qint64 QMediaTimeRange::latestTime() const**

        Returns the latest time within the time range.

        For empty time ranges, this value is equal to zero.

        **See also** **earliestTime** ().
        """
        ...
    @overload
    def removeInterval(
        self, interval: PySide6.QtMultimedia.QMediaTimeRange.Interval
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#removeInterval

        **void QMediaTimeRange::removeInterval(const QMediaTimeRange::Interval &
        interval )**

        Removes the specified **interval** from the time range.

        Removing intervals which are not **normal**  is invalid, and will be
        ignored.

        Intervals within the time range will be trimmed, split or deleted such
        that no intervals within the time range include any part of the target
        interval.

        This operation takes linear time.

        **See also** **addInterval** ().
        """
        ...
    @overload
    def removeInterval(self, start: int, end: int) -> None:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#removeInterval-1

        **void QMediaTimeRange::removeInterval(qint64 start , qint64 end )**

        This is an overloaded function.

        Removes the interval specified by **start** and **end** from the time
        range.

        **See also** **removeInterval** ().
        """
        ...
    def removeTimeRange(
        self,
        arg__1: (
            PySide6.QtMultimedia.QMediaTimeRange
            | PySide6.QtMultimedia.QMediaTimeRange.Interval
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmediatimerange.html#removeTimeRange

        **void QMediaTimeRange::removeTimeRange(const QMediaTimeRange & range
        )**

        Removes each of the intervals in **range** from this time range.

        Equivalent to calling **removeInterval** () for each interval in
        **range**.
        """
        ...
    def swap(
        self,
        other: (
            PySide6.QtMultimedia.QMediaTimeRange
            | PySide6.QtMultimedia.QMediaTimeRange.Interval
        ),
    ) -> None: ...
