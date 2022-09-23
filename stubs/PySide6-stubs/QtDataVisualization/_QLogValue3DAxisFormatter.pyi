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

class QLogValue3DAxisFormatter(PySide6.QtDataVisualization.QValue3DAxisFormatter):
    """
    https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html

    **Detailed Description**

    When a formatter is attached to a value axis, the axis range cannot include
    negative values or the zero.

    **See also** **QValue3DAxisFormatter** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#QLogValue3DAxisForm
        atter-1

        **QLogValue3DAxisFormatter::QLogValue3DAxisFormatter(QObject * parent =
        nullptr)**

        Constructs a new logarithmic value 3D axis formatter with the optional
        parent **parent**.
        """
        ...
    def autoSubGrid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#autoSubGrid-prop

        **autoSubGrid : bool**

        This property holds whether sub-grid positions are generated
        automatically.

        If this property value is set to `true`, the parent axis sub-segment
        count is ignored when calculating sub-grid line positions. The sub-grid
        positions are generated automatically according to the **base**
        property value. The number of sub-grid lines is set to the base value
        minus one, rounded down. This property is ignored when the base value is
        zero. Defaults to `true`.

        **Access functions:**

        bool **autoSubGrid** () const
        void **setAutoSubGrid** (bool
        **enabled** )

        **Notifier signal:**

        void **autoSubGridChanged** (bool **enabled** )

        **See also** **base**  and **QValue3DAxis::subSegmentCount** .
        """
        ...
    def base(self) -> float:
        """
        https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#base-prop

        **base : qreal**

        This property holds the base of the logarithm used to map axis values.

        If the base is non-zero, the parent axis segment count will be ignored
        when the grid line and label positions are calculated. If you want the
        range to be divided into equal segments like a normal value axis, set
        this property value to zero.

        The base has to be zero or a positive value and it cannot be equal to
        one. Defaults to ten.

        **Access functions:**

        qreal **base** () const
        void **setBase** (qreal **base** )

        **Notifier signal:**

        void **baseChanged** (qreal **base** )

        **See also** **QValue3DAxis::segmentCount** .
        """
        ...
    def createNewInstance(self) -> PySide6.QtDataVisualization.QValue3DAxisFormatter: ...
    def populateCopy(
        self, copy: PySide6.QtDataVisualization.QValue3DAxisFormatter
    ) -> None: ...
    def positionAt(self, value: float) -> float: ...
    def recalculate(self) -> None: ...
    def setAutoSubGrid(self, enabled: bool) -> None:
        """
        https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#autoSubGrid-prop

        **autoSubGrid : bool**

        This property holds whether sub-grid positions are generated
        automatically.

        If this property value is set to `true`, the parent axis sub-segment
        count is ignored when calculating sub-grid line positions. The sub-grid
        positions are generated automatically according to the **base**
        property value. The number of sub-grid lines is set to the base value
        minus one, rounded down. This property is ignored when the base value is
        zero. Defaults to `true`.

        **Access functions:**

        bool **autoSubGrid** () const
        void **setAutoSubGrid** (bool
        **enabled** )

        **Notifier signal:**

        void **autoSubGridChanged** (bool **enabled** )

        **See also** **base**  and **QValue3DAxis::subSegmentCount** .
        """
        ...
    def setBase(self, base: float) -> None:
        """
        https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#base-prop

        **base : qreal**

        This property holds the base of the logarithm used to map axis values.

        If the base is non-zero, the parent axis segment count will be ignored
        when the grid line and label positions are calculated. If you want the
        range to be divided into equal segments like a normal value axis, set
        this property value to zero.

        The base has to be zero or a positive value and it cannot be equal to
        one. Defaults to ten.

        **Access functions:**

        qreal **base** () const
        void **setBase** (qreal **base** )

        **Notifier signal:**

        void **baseChanged** (qreal **base** )

        **See also** **QValue3DAxis::segmentCount** .
        """
        ...
    def setShowEdgeLabels(self, enabled: bool) -> None:
        """
        https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#showEdgeLabels-prop

        **showEdgeLabels : bool**

        This property holds whether the first and last label on the axis are
        visible.

        When the **base**  property value is non-zero, the whole axis range is
        often not equally divided into segments. The first and last segments are
        often smaller than the other segments. In extreme cases, this can lead
        to overlapping labels on the first and last two grid lines. By setting
        this property to `false`, you can suppress showing the minimum and
        maximum labels for the axis in cases where the segments do not exactly
        fit the axis. Defaults to `true`.

        **Access functions:**

        bool **showEdgeLabels** () const
        void **setShowEdgeLabels** (bool
        **enabled** )

        **Notifier signal:**

        void **showEdgeLabelsChanged** (bool **enabled** )

        **See also** **base**  and **QAbstract3DAxis::labels** .

        **Member Function Documentation**
        """
        ...
    def showEdgeLabels(self) -> bool:
        """
        https://doc.qt.io/qt-6/qlogvalue3daxisformatter.html#showEdgeLabels-prop

        **showEdgeLabels : bool**

        This property holds whether the first and last label on the axis are
        visible.

        When the **base**  property value is non-zero, the whole axis range is
        often not equally divided into segments. The first and last segments are
        often smaller than the other segments. In extreme cases, this can lead
        to overlapping labels on the first and last two grid lines. By setting
        this property to `false`, you can suppress showing the minimum and
        maximum labels for the axis in cases where the segments do not exactly
        fit the axis. Defaults to `true`.

        **Access functions:**

        bool **showEdgeLabels** () const
        void **setShowEdgeLabels** (bool
        **enabled** )

        **Notifier signal:**

        void **showEdgeLabelsChanged** (bool **enabled** )

        **See also** **base**  and **QAbstract3DAxis::labels** .

        **Member Function Documentation**
        """
        ...
    def valueAt(self, position: float) -> float: ...
    @property
    def autoSubGridChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def baseChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def showEdgeLabelsChanged(self) -> PySide6.QtCore.SignalInstance: ...
