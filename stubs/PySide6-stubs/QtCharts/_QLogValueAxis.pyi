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
PySide6.QtCharts, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCharts
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QLogValueAxis(PySide6.QtCharts.QAbstractAxis):
    """
    https://doc.qt.io/qt-6/qlogvalueaxis.html

    **Detailed Description**

    A logarithmic scale is a nonlinear scale that is based on orders of
    magnitude, so that each tick mark on the axis is the previous tick mark
    multiplied by a value.

    **Note:** If QLogValueAxis is attached to a series with one or more points
    with negative or zero values on the associated dimension, the series will
    not be plotted at all. This is particularly relevant when XYModelMappers are
    used, since empty cells in models typically contain zero values.
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#QLogValueAxis

        **QLogValueAxis::QLogValueAxis(QObject * parent = nullptr)**

        Constructs an axis object that is a child of **parent**.
        """
        ...
    def base(self) -> float:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#base-prop

        **base : qreal**

        This property holds the base of the logarithm.

        The value has to be greater than 0 and cannot equal 1.

        **Access functions:**

        qreal **base** () const
        void **setBase** (qreal **base** )

        **Notifier signal:**

        void ****baseChanged** ** (qreal **base** )
        """
        ...
    def labelFormat(self) -> str:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#labelFormat-prop

        **labelFormat : QString**

        This property holds the label format of the axis.

        The format string supports the following conversion specifiers, length
        modifiers, and flags provided by `printf()` in the standard C++ library:
        d, i, o, x, X, f, F, e, E, g, G, c.

        If **QChart::localizeNumbers**  is `true`, the supported specifiers are
        limited to: d, e, E, f, g, G, and i. Also, only the precision modifier
        is supported. The rest of the formatting comes from the default
        **QLocale**  of the application.

        **Access functions:**

        QString **labelFormat** () const
        void **setLabelFormat** (const
        QString & **format** )

        **Notifier signal:**

        void ****labelFormatChanged** ** (const QString & **format** )

        **See also** **QString::asprintf** ().
        """
        ...
    def max(self) -> float:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#max-prop

        **max : qreal**

        This property holds the maximum value on the axis.

        When setting this property, the minimum value is adjusted if necessary,
        to ensure that the range remains valid. The value has to be greater than
        0.

        **Access functions:**

        qreal **max** () const
        void **setMax** (qreal **max** )

        **Notifier signal:**

        void ****maxChanged** ** (qreal **max** )
        """
        ...
    def min(self) -> float:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#min-prop

        **min : qreal**

        This property holds the minimum value on the axis.

        When setting this property, the maximum value is adjusted if necessary,
        to ensure that the range remains valid. The value has to be greater than
        0.

        **Access functions:**

        qreal **min** () const
        void **setMin** (qreal **min** )

        **Notifier signal:**

        void ****minChanged** ** (qreal **min** )
        """
        ...
    def minorTickCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#minorTickCount-prop

        **minorTickCount : int**

        This property holds the number of minor tick marks on the axis. This
        indicates how many grid lines are drawn between major ticks on the
        chart. Labels are not drawn for minor ticks. The default value is 0. Set
        the value to -1 and the number of grid lines between major ticks will be
        calculated automatically.

        **Access functions:**

        int **minorTickCount** () const
        void **setMinorTickCount** (int
        **minorTickCount** )

        **Notifier signal:**

        void ****minorTickCountChanged** ** (int **minorTickCount** )
        """
        ...
    def setBase(self, base: float) -> None:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#base-prop

        **base : qreal**

        This property holds the base of the logarithm.

        The value has to be greater than 0 and cannot equal 1.

        **Access functions:**

        qreal **base** () const
        void **setBase** (qreal **base** )

        **Notifier signal:**

        void ****baseChanged** ** (qreal **base** )
        """
        ...
    def setLabelFormat(self, format: str) -> None:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#labelFormat-prop

        **labelFormat : QString**

        This property holds the label format of the axis.

        The format string supports the following conversion specifiers, length
        modifiers, and flags provided by `printf()` in the standard C++ library:
        d, i, o, x, X, f, F, e, E, g, G, c.

        If **QChart::localizeNumbers**  is `true`, the supported specifiers are
        limited to: d, e, E, f, g, G, and i. Also, only the precision modifier
        is supported. The rest of the formatting comes from the default
        **QLocale**  of the application.

        **Access functions:**

        QString **labelFormat** () const
        void **setLabelFormat** (const
        QString & **format** )

        **Notifier signal:**

        void ****labelFormatChanged** ** (const QString & **format** )

        **See also** **QString::asprintf** ().
        """
        ...
    def setMax(self, max: float) -> None:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#max-prop

        **max : qreal**

        This property holds the maximum value on the axis.

        When setting this property, the minimum value is adjusted if necessary,
        to ensure that the range remains valid. The value has to be greater than
        0.

        **Access functions:**

        qreal **max** () const
        void **setMax** (qreal **max** )

        **Notifier signal:**

        void ****maxChanged** ** (qreal **max** )
        """
        ...
    def setMin(self, min: float) -> None:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#min-prop

        **min : qreal**

        This property holds the minimum value on the axis.

        When setting this property, the maximum value is adjusted if necessary,
        to ensure that the range remains valid. The value has to be greater than
        0.

        **Access functions:**

        qreal **min** () const
        void **setMin** (qreal **min** )

        **Notifier signal:**

        void ****minChanged** ** (qreal **min** )
        """
        ...
    def setMinorTickCount(self, minorTickCount: int) -> None:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#minorTickCount-prop

        **minorTickCount : int**

        This property holds the number of minor tick marks on the axis. This
        indicates how many grid lines are drawn between major ticks on the
        chart. Labels are not drawn for minor ticks. The default value is 0. Set
        the value to -1 and the number of grid lines between major ticks will be
        calculated automatically.

        **Access functions:**

        int **minorTickCount** () const
        void **setMinorTickCount** (int
        **minorTickCount** )

        **Notifier signal:**

        void ****minorTickCountChanged** ** (int **minorTickCount** )
        """
        ...
    def setRange(self, min: float, max: float) -> None:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#setRange

        **void QLogValueAxis::setRange(qreal min , qreal max )**

        Sets the range from **min** to **max** on the axis. If **min** is
        greater than **max** , this function returns without making any changes.
        """
        ...
    def tickCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#tickCount-prop

        **[read-only] tickCount : const int**

        This property holds the number of tick marks on the axis. This indicates
        how many grid lines are drawn on the chart. This value is read-only.

        **Access functions:**

        int **tickCount** () const

        **Notifier signal:**

        void ****tickCountChanged** ** (int **tickCount** )

        **Member Function Documentation**
        """
        ...
    def type(self) -> PySide6.QtCharts.QAbstractAxis.AxisType:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#type

        **[override virtual] QAbstractAxis::AxisType QLogValueAxis::type()
        const**

        Reimplements: **QAbstractAxis::type() const** .

        Returns the type of the axis.
        """
        ...
    @property
    def baseChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#baseChanged

        **[signal] void QLogValueAxis::baseChanged(qreal base )**

        This signal is emitted when the **base** of the logarithm of the axis
        changes.

        **Note:** Notifier signal for property **base** .
        """
        ...
    @property
    def labelFormatChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#labelFormatChanged

        **[signal] void QLogValueAxis::labelFormatChanged(const QString & format
        )**

        This signal is emitted when the **format** of axis labels changes.

        **Note:** Notifier signal for property **labelFormat** .
        """
        ...
    @property
    def maxChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#maxChanged

        **[signal] void QLogValueAxis::maxChanged(qreal max )**

        This signal is emitted when the maximum value of the axis, specified by
        **max** , changes.

        **Note:** Notifier signal for property **max** .
        """
        ...
    @property
    def minChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#minChanged

        **[signal] void QLogValueAxis::minChanged(qreal min )**

        This signal is emitted when the minimum value of the axis, specified by
        **min** , changes.

        **Note:** Notifier signal for property **min** .
        """
        ...
    @property
    def minorTickCountChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#minorTickCountChanged

        **[signal] void QLogValueAxis::minorTickCountChanged(int minorTickCount
        )**

        This signal is emitted when the number of minor tick marks on the axis,
        specified by **minorTickCount** , changes.

        **Note:** Notifier signal for property **minorTickCount** .
        """
        ...
    @property
    def rangeChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#rangeChanged

        **[signal] void QLogValueAxis::rangeChanged(qreal min , qreal max )**

        This signal is emitted when the minimum or maximum value of the axis,
        specified by **min** and **max** , changes.
        """
        ...
    @property
    def tickCountChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlogvalueaxis.html#tickCountChanged

        **[signal] void QLogValueAxis::tickCountChanged(int tickCount )**

        This signal is emitted when the number of tick marks on the axis,
        specified by **tickCount** , changes.

        **Note:** Notifier signal for property **tickCount** .
        """
        ...
