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
PySide6.QtDataVisualization, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtDataVisualization
import PySide6.QtGui

class QValue3DAxis(PySide6.QtDataVisualization.QAbstract3DAxis):
    """
    https://doc.qt.io/qt-6/qvalue3daxis.html

    **Detailed Description**

    A value axis can be given a range of values and segment and subsegment
    counts to divide the range into.

    Labels are drawn between each segment. Grid lines are drawn between each
    segment and each subsegment.

    **Note:** If visible, there will always be at least two grid lines and
    labels indicating the minimum and the maximum values of the range, as there
    is always at least one segment.
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qvalue3daxis.html#QValue3DAxis

        **QValue3DAxis::QValue3DAxis(QObject * parent = nullptr)**

        Constructs QValue3DAxis with the given **parent**.
        """
        ...
    def formatter(self) -> PySide6.QtDataVisualization.QValue3DAxisFormatter:
        """
        https://doc.qt.io/qt-6/qvalue3daxis.html#formatter-prop

        **[since QtDataVisualization 1.1] formatter : QValue3DAxisFormatter***

        This property holds the axis formatter to be used.

        Any existing formatter is deleted when a new formatter is set.

        This property was introduced in QtDataVisualization 1.1.

        **Access functions:**

        QValue3DAxisFormatter * **formatter** () const
        void **setFormatter**
        (QValue3DAxisFormatter * **formatter** )

        **Notifier signal:**

        void **formatterChanged** (QValue3DAxisFormatter * **formatter** )
        """
        ...
    def labelFormat(self) -> str:
        """
        https://doc.qt.io/qt-6/qvalue3daxis.html#labelFormat-prop

        **labelFormat : QString**

        This property holds the label format to be used for the labels on this
        axis.

        The format string supports the following conversion specifiers, length
        modifiers, and flags provided by `printf()` in the standard C++ library:
        d, i, o, x, X, f, F, e, E, g, G, c.

        If **QAbstract3DGraph::locale**  is anything else than `"C"`, the
        supported specifiers are limited to: d, e, E, f, g, G, and i. Also, only
        the precision modifier is supported. The rest of the formatting comes
        from the default **QLocale**  of the application.

        Usage example:

        `axis->setLabelFormat("%.2f mm");`

        **Access functions:**

        QString **labelFormat** () const
        void **setLabelFormat** (const
        QString & **format** )

        **Notifier signal:**

        void **labelFormatChanged** (const QString & **format** )

        **See also** **formatter**  and **QAbstract3DGraph::locale** .
        """
        ...
    def reversed(self) -> bool:
        """
        https://doc.qt.io/qt-6/qvalue3daxis.html#reversed-prop

        **[since QtDataVisualization 1.1] reversed : bool**

        This property holds whether the axis is rendered in reverse.

        If `true`, the axis will be rendered in reverse, i.e. the positions of
        minimum and maximum values are swapped when the graph is rendered. This
        property doesn't affect the actual minimum and maximum values of the
        axis.

        This property was introduced in QtDataVisualization 1.1.

        **Access functions:**

        bool **reversed** () const
        void **setReversed** (bool **enable** )

        **Notifier signal:**

        void **reversedChanged** (bool **enable** )
        """
        ...
    def segmentCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qvalue3daxis.html#segmentCount-prop

        **segmentCount : int**

        This property holds the number of segments on the axis.

        This indicates how many labels are drawn. The number of grid lines to be
        drawn is calculated with formula: `segments * subsegments + 1`. The
        preset default is `5`. The value cannot be below `1`.

        **Access functions:**

        int **segmentCount** () const
        void **setSegmentCount** (int **count**
        )

        **Notifier signal:**

        void **segmentCountChanged** (int **count** )

        **See also** **setSubSegmentCount** ().
        """
        ...
    def setFormatter(
        self, formatter: PySide6.QtDataVisualization.QValue3DAxisFormatter
    ) -> None:
        """
        https://doc.qt.io/qt-6/qvalue3daxis.html#formatter-prop

        **[since QtDataVisualization 1.1] formatter : QValue3DAxisFormatter***

        This property holds the axis formatter to be used.

        Any existing formatter is deleted when a new formatter is set.

        This property was introduced in QtDataVisualization 1.1.

        **Access functions:**

        QValue3DAxisFormatter * **formatter** () const
        void **setFormatter**
        (QValue3DAxisFormatter * **formatter** )

        **Notifier signal:**

        void **formatterChanged** (QValue3DAxisFormatter * **formatter** )
        """
        ...
    def setLabelFormat(self, format: str) -> None:
        """
        https://doc.qt.io/qt-6/qvalue3daxis.html#labelFormat-prop

        **labelFormat : QString**

        This property holds the label format to be used for the labels on this
        axis.

        The format string supports the following conversion specifiers, length
        modifiers, and flags provided by `printf()` in the standard C++ library:
        d, i, o, x, X, f, F, e, E, g, G, c.

        If **QAbstract3DGraph::locale**  is anything else than `"C"`, the
        supported specifiers are limited to: d, e, E, f, g, G, and i. Also, only
        the precision modifier is supported. The rest of the formatting comes
        from the default **QLocale**  of the application.

        Usage example:

        `axis->setLabelFormat("%.2f mm");`

        **Access functions:**

        QString **labelFormat** () const
        void **setLabelFormat** (const
        QString & **format** )

        **Notifier signal:**

        void **labelFormatChanged** (const QString & **format** )

        **See also** **formatter**  and **QAbstract3DGraph::locale** .
        """
        ...
    def setReversed(self, enable: bool) -> None:
        """
        https://doc.qt.io/qt-6/qvalue3daxis.html#reversed-prop

        **[since QtDataVisualization 1.1] reversed : bool**

        This property holds whether the axis is rendered in reverse.

        If `true`, the axis will be rendered in reverse, i.e. the positions of
        minimum and maximum values are swapped when the graph is rendered. This
        property doesn't affect the actual minimum and maximum values of the
        axis.

        This property was introduced in QtDataVisualization 1.1.

        **Access functions:**

        bool **reversed** () const
        void **setReversed** (bool **enable** )

        **Notifier signal:**

        void **reversedChanged** (bool **enable** )
        """
        ...
    def setSegmentCount(self, count: int) -> None:
        """
        https://doc.qt.io/qt-6/qvalue3daxis.html#segmentCount-prop

        **segmentCount : int**

        This property holds the number of segments on the axis.

        This indicates how many labels are drawn. The number of grid lines to be
        drawn is calculated with formula: `segments * subsegments + 1`. The
        preset default is `5`. The value cannot be below `1`.

        **Access functions:**

        int **segmentCount** () const
        void **setSegmentCount** (int **count**
        )

        **Notifier signal:**

        void **segmentCountChanged** (int **count** )

        **See also** **setSubSegmentCount** ().
        """
        ...
    def setSubSegmentCount(self, count: int) -> None:
        """
        https://doc.qt.io/qt-6/qvalue3daxis.html#subSegmentCount-prop

        **subSegmentCount : int**

        This property holds the number of subsegments inside each segment on the
        axis.

        Grid lines are drawn between each subsegment, in addition to each
        segment. The preset default is `1`. The value cannot be below `1`.

        **Access functions:**

        int **subSegmentCount** () const
        void **setSubSegmentCount** (int
        **count** )

        **Notifier signal:**

        void **subSegmentCountChanged** (int **count** )

        **See also** **setSegmentCount** ().

        **Member Function Documentation**
        """
        ...
    def subSegmentCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qvalue3daxis.html#subSegmentCount-prop

        **subSegmentCount : int**

        This property holds the number of subsegments inside each segment on the
        axis.

        Grid lines are drawn between each subsegment, in addition to each
        segment. The preset default is `1`. The value cannot be below `1`.

        **Access functions:**

        int **subSegmentCount** () const
        void **setSubSegmentCount** (int
        **count** )

        **Notifier signal:**

        void **subSegmentCountChanged** (int **count** )

        **See also** **setSegmentCount** ().

        **Member Function Documentation**
        """
        ...
    @property
    def formatterChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def labelFormatChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def reversedChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def segmentCountChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def subSegmentCountChanged(self) -> PySide6.QtCore.SignalInstance: ...
