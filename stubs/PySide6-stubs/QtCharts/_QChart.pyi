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

from collections.abc import Sequence
from enum import IntFlag
from typing import overload

import PySide6.QtCharts
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QChart(PySide6.QtWidgets.QGraphicsWidget):
    """
    https://doc.qt.io/qt-6/qchart.html

    **Detailed Description**

    QChart is a **QGraphicsWidget**  that you can show in a **QGraphicsScene** .
    It manages the graphical representation of different types of series and
    other chart related objects like legend and axes. To simply show a chart in
    a layout, the convenience class **QChartView**  can be used instead of
    QChart. In addition, line, spline, area, and scatter series can be presented
    as polar charts by using the **QPolarChart**  class.

    **See also** **QChartView**  and **QPolarChart** .
    """

    NoAnimation: QChart.AnimationOption = ...
    GridAxisAnimations: QChart.AnimationOption = ...
    SeriesAnimations: QChart.AnimationOption = ...
    AllAnimations: QChart.AnimationOption = ...
    ChartThemeLight: QChart.ChartTheme = ...
    ChartThemeBlueCerulean: QChart.ChartTheme = ...
    ChartThemeDark: QChart.ChartTheme = ...
    ChartThemeBrownSand: QChart.ChartTheme = ...
    ChartThemeBlueNcs: QChart.ChartTheme = ...
    ChartThemeHighContrast: QChart.ChartTheme = ...
    ChartThemeBlueIcy: QChart.ChartTheme = ...
    ChartThemeQt: QChart.ChartTheme = ...
    ChartTypeUndefined: QChart.ChartType = ...
    ChartTypeCartesian: QChart.ChartType = ...
    ChartTypePolar: QChart.ChartType = ...

    class AnimationOption(IntFlag):
        NoAnimation: QChart.AnimationOption = ...
        GridAxisAnimations: QChart.AnimationOption = ...
        SeriesAnimations: QChart.AnimationOption = ...
        AllAnimations: QChart.AnimationOption = ...

    class AnimationOptions: ...

    class ChartTheme(IntFlag):
        ChartThemeLight: QChart.ChartTheme = ...
        ChartThemeBlueCerulean: QChart.ChartTheme = ...
        ChartThemeDark: QChart.ChartTheme = ...
        ChartThemeBrownSand: QChart.ChartTheme = ...
        ChartThemeBlueNcs: QChart.ChartTheme = ...
        ChartThemeHighContrast: QChart.ChartTheme = ...
        ChartThemeBlueIcy: QChart.ChartTheme = ...
        ChartThemeQt: QChart.ChartTheme = ...

    class ChartType(IntFlag):
        ChartTypeUndefined: QChart.ChartType = ...
        ChartTypeCartesian: QChart.ChartType = ...
        ChartTypePolar: QChart.ChartType = ...
    @overload
    def __init__(
        self,
        parent: PySide6.QtWidgets.QGraphicsItem | None = ...,
        wFlags: PySide6.QtCore.Qt.WindowFlags = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#QChart

        **QChart::QChart(QGraphicsItem * parent = nullptr, Qt::WindowFlags
        wFlags = Qt::WindowFlags())**

        Constructs a chart object that is a child of **parent**. The properties
        specified by **wFlags** are passed to the **QGraphicsWidget**
        constructor.
        """
        ...
    @overload
    def __init__(
        self,
        type: PySide6.QtCharts.QChart.ChartType,
        parent: PySide6.QtWidgets.QGraphicsItem,
        wFlags: PySide6.QtCore.Qt.WindowFlags,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#QChart

        **QChart::QChart(QGraphicsItem * parent = nullptr, Qt::WindowFlags
        wFlags = Qt::WindowFlags())**

        Constructs a chart object that is a child of **parent**. The properties
        specified by **wFlags** are passed to the **QGraphicsWidget**
        constructor.
        """
        ...
    def addAxis(
        self,
        axis: PySide6.QtCharts.QAbstractAxis,
        alignment: PySide6.QtCore.Qt.Alignment,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#addAxis

        **void QChart::addAxis(QAbstractAxis * axis , Qt::Alignment alignment
        )**

        Adds the axis **axis** to the chart aligned as specified by
        **alignment**. The chart takes the ownership of the axis.

        **See also** **removeAxis** (), **createDefaultAxes** (), and
        **QAbstractSeries::attachAxis** ().
        """
        ...
    def addSeries(self, series: PySide6.QtCharts.QAbstractSeries) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#addSeries

        **void QChart::addSeries(QAbstractSeries * series )**

        Adds the series **series** to the chart and takes ownership of it.

        **Note:** A newly added series is not attached to any axes by default,
        not even those that might have been created for the chart using
        **createDefaultAxes** () before the series was added to the chart. If no
        axes are attached to the newly added series before the chart is shown,
        the series will get drawn as if it had axes with ranges that exactly fit
        the series to the plot area of the chart. This can be confusing if the
        same chart also displays other series that have properly attached axes,
        so always make sure you either call **createDefaultAxes** () after a
        series has been added or explicitly attach axes for the series.

        **See also** **removeSeries** (), **removeAllSeries** (),
        **createDefaultAxes** (), and **QAbstractSeries::attachAxis** ().
        """
        ...
    def animationDuration(self) -> int:
        """
        https://doc.qt.io/qt-6/qchart.html#animationDuration-prop

        **animationDuration : int**

        This property holds the duration of the animation for the chart.

        **Access functions:**

        int **animationDuration** () const
        void **setAnimationDuration** (int
        **msecs** )
        """
        ...
    def animationEasingCurve(self) -> PySide6.QtCore.QEasingCurve:
        """
        https://doc.qt.io/qt-6/qchart.html#animationEasingCurve-prop

        **animationEasingCurve : QEasingCurve**

        This property holds the easing curve of the animation for the chart.

        **Access functions:**

        QEasingCurve **animationEasingCurve** () const
        void
        **setAnimationEasingCurve** (const QEasingCurve & **curve** )
        """
        ...
    def animationOptions(self) -> PySide6.QtCharts.QChart.AnimationOptions:
        """
        https://doc.qt.io/qt-6/qchart.html#animationOptions-prop

        **animationOptions : QChart::AnimationOptions**

        This property holds the animation options for the chart.

        Animations are enabled or disabled based on this setting.

        **Access functions:**

        QChart::AnimationOptions **animationOptions** () const
        void
        **setAnimationOptions** (QChart::AnimationOptions **options** )
        """
        ...
    def axes(
        self,
        orientation: PySide6.QtCore.Qt.Orientations = ...,
        series: PySide6.QtCharts.QAbstractSeries | None = ...,
    ) -> list[PySide6.QtCharts.QAbstractAxis]:
        """
        https://doc.qt.io/qt-6/qchart.html#axes

        **QList<QAbstractAxis *> QChart::axes(Qt::Orientations orientation =
        Qt::Horizontal|Qt::Vertical, QAbstractSeries * series = nullptr) const**

        Returns the axes attached to the series **series** with the orientation
        specified by **orientation**. If no series is specified, all axes added
        to the chart with the specified orientation are returned.

        **See also** **addAxis** () and **createDefaultAxes** ().
        """
        ...
    def axisX(
        self, series: PySide6.QtCharts.QAbstractSeries | None = ...
    ) -> PySide6.QtCharts.QAbstractAxis: ...
    def axisY(
        self, series: PySide6.QtCharts.QAbstractSeries | None = ...
    ) -> PySide6.QtCharts.QAbstractAxis: ...
    def backgroundBrush(self) -> PySide6.QtGui.QBrush:
        """
        https://doc.qt.io/qt-6/qchart.html#backgroundBrush

        **QBrush QChart::backgroundBrush() const**

        Gets the brush that is used for painting the background of the chart
        area.

        **See also** **setBackgroundBrush** ().
        """
        ...
    def backgroundPen(self) -> PySide6.QtGui.QPen:
        """
        https://doc.qt.io/qt-6/qchart.html#backgroundPen

        **QPen QChart::backgroundPen() const**

        Gets the pen that is used for painting the background of the chart area.

        **See also** **setBackgroundPen** ().
        """
        ...
    def backgroundRoundness(self) -> float:
        """
        https://doc.qt.io/qt-6/qchart.html#backgroundRoundness-prop

        **backgroundRoundness : qreal**

        This property holds the diameter of the rounding circle at the corners
        of the chart background.

        **Access functions:**

        qreal **backgroundRoundness** () const
        void **setBackgroundRoundness**
        (qreal **diameter** )
        """
        ...
    def chartType(self) -> PySide6.QtCharts.QChart.ChartType:
        """
        https://doc.qt.io/qt-6/qchart.html#chartType-prop

        **[read-only] chartType : const QChart::ChartType**

        This property holds whether the chart is a cartesian chart or a polar
        chart.

        This property is set internally and it is read only.

        **Access functions:**

        QChart::ChartType **chartType** () const

        **See also** **QPolarChart** .
        """
        ...
    def createDefaultAxes(self) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#createDefaultAxes

        **void QChart::createDefaultAxes()**

        Creates axes for the chart based on the series that have already been
        added to the chart. Any axes previously added to the chart will be
        deleted.

        **Note:** This function has to be called after all series have been
        added to the chart. The axes created by this function will NOT get
        automatically attached to any series added to the chart after this
        function has been called. A series with no axes attached will by default
        scale to utilize the entire plot area of the chart, which can be
        confusing if there are other series with properly attached axes also
        present.

        Series typeHorizontal axis (X)Vertical axis (Y)
        **QXYSeries**
        **QValueAxis** **QValueAxis**
        **QBarSeries** **QBarCategoryAxis**
        **QValueAxis**
        **QPieSeries** NoneNone

        If there are several **QXYSeries**  derived series added to the chart
        and no series of other types have been added, then only one pair of axes
        is created. If there are several series of different types added to the
        chart, then each series gets its own axes pair.

        The axes specific to the series can be later obtained from the chart by
        providing the series as the parameter for the **axes** () function call.
        **QPieSeries**  does not create any axes.

        **See also** **axes** () and **QAbstractSeries::attachAxis** ().
        """
        ...
    def isBackgroundVisible(self) -> bool: ...
    def isDropShadowEnabled(self) -> bool: ...
    def isPlotAreaBackgroundVisible(self) -> bool: ...
    def isZoomed(self) -> bool:
        """
        https://doc.qt.io/qt-6/qchart.html#isZoomed

        **bool QChart::isZoomed()**

        Returns `true` if any series has a zoomed domain.
        """
        ...
    def legend(self) -> PySide6.QtCharts.QLegend:
        """
        https://doc.qt.io/qt-6/qchart.html#legend

        **QLegend *QChart::legend() const**

        Returns the legend object of the chart. Ownership stays with the chart.
        """
        ...
    def locale(self) -> PySide6.QtCore.QLocale:
        """
        https://doc.qt.io/qt-6/qchart.html#locale-prop

        **locale : QLocale**

        This property holds the locale used to format various chart labels.

        Labels are localized only when **localizeNumbers**  is `true`, except
        for **QDateTimeAxis**  labels, which always use the **QLocale**  set
        with this property.

        Defaults to the application default locale at the time when the chart is
        constructed.

        **Access functions:**

        QLocale **locale** () const
        void **setLocale** (const QLocale &
        **locale** )

        **See also** **localizeNumbers** .
        """
        ...
    def localizeNumbers(self) -> bool:
        """
        https://doc.qt.io/qt-6/qchart.html#localizeNumbers-prop

        **localizeNumbers : bool**

        This property holds whether numbers are localized.

        When `true`, all generated numbers appearing in various series and axis
        labels will be localized using the **QLocale**  set with the **locale**
        property. When `false`, the **C** locale is always used. Defaults to
        `false`.

        **Note:** This property does not affect **QDateTimeAxis**  labels, which
        always use the **QLocale**  set with the locale property.

        **Access functions:**

        bool **localizeNumbers** () const
        void **setLocalizeNumbers** (bool
        **localize** )

        **See also** **locale** .
        """
        ...
    def mapToPosition(
        self,
        value: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        series: PySide6.QtCharts.QAbstractSeries | None = ...,
    ) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qchart.html#mapToPosition

        **QPointF QChart::mapToPosition(const QPointF & value , QAbstractSeries
        * series = nullptr)**

        Returns the position on the chart that corresponds to the value
        **value** in the series specified by **series**.
        """
        ...
    def mapToValue(
        self,
        position: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        series: PySide6.QtCharts.QAbstractSeries | None = ...,
    ) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qchart.html#mapToValue

        **QPointF QChart::mapToValue(const QPointF & position , QAbstractSeries
        * series = nullptr)**

        Returns the value in the series specified by **series** at the position
        specified by **position** in a chart.
        """
        ...
    def margins(self) -> PySide6.QtCore.QMargins:
        """
        https://doc.qt.io/qt-6/qchart.html#margins-prop

        **margins : QMargins**

        This property holds the minimum margins allowed between the edge of the
        chart rectangle and the plot area.

        The margins are used for drawing the title, axes, and legend.

        **Access functions:**

        QMargins **margins** () const
        void **setMargins** (const QMargins &
        **margins** )
        """
        ...
    def plotArea(self) -> PySide6.QtCore.QRectF:
        """
        https://doc.qt.io/qt-6/qchart.html#plotArea-prop

        **plotArea : QRectF**

        This property holds the rectangle within which the chart is drawn.

        The plot area does not include the area defined by margins. By default
        this will resize if inside a **QChartView** . If an explicit size is set
        for the plot area then it will respect this, to revert back to the
        default behavior, then calling `setPlotArea(QRectF());` will achieve
        this.

        **Access functions:**

        QRectF **plotArea** () const
        void **setPlotArea** (const QRectF &
        **rect** )

        **Notifier signal:**

        void **plotAreaChanged** (const QRectF & **plotArea** )
        """
        ...
    def plotAreaBackgroundBrush(self) -> PySide6.QtGui.QBrush:
        """
        https://doc.qt.io/qt-6/qchart.html#plotAreaBackgroundBrush

        **QBrush QChart::plotAreaBackgroundBrush() const**

        Returns the brush used to fill the background of the plot area of the
        chart.

        **See also** **plotArea** (), **plotAreaBackgroundVisible** ,
        **plotAreaBackgroundPen** (), and **setPlotAreaBackgroundBrush** ().
        """
        ...
    def plotAreaBackgroundPen(self) -> PySide6.QtGui.QPen:
        """
        https://doc.qt.io/qt-6/qchart.html#plotAreaBackgroundPen

        **QPen QChart::plotAreaBackgroundPen() const**

        Returns the pen used to draw the background of the plot area of the
        chart.

        **See also** **plotArea** (), **plotAreaBackgroundVisible** ,
        **plotAreaBackgroundBrush** (), and **setPlotAreaBackgroundPen** ().
        """
        ...
    def removeAllSeries(self) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#removeAllSeries

        **void QChart::removeAllSeries()**

        Removes and deletes all series objects that have been added to the
        chart.

        **See also** **addSeries** () and **removeSeries** ().
        """
        ...
    def removeAxis(self, axis: PySide6.QtCharts.QAbstractAxis) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#removeAxis

        **void QChart::removeAxis(QAbstractAxis * axis )**

        Removes the axis **axis** from the chart. The chart releases the
        ownership of the specified **axis** object.

        **See also** **addAxis** (), **createDefaultAxes** (), and
        **QAbstractSeries::detachAxis** ().
        """
        ...
    def removeSeries(self, series: PySide6.QtCharts.QAbstractSeries) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#removeSeries

        **void QChart::removeSeries(QAbstractSeries * series )**

        Removes the series **series** from the chart. The chart releases the
        ownership of the specified **series** object.

        **See also** **addSeries** () and **removeAllSeries** ().
        """
        ...
    def scroll(self, dx: float, dy: float) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#scroll

        **void QChart::scroll(qreal dx , qreal dy )**

        Scrolls the visible area of the chart by the distance specified by
        **dx** and **dy**.

        For polar charts, **dx** indicates the angle along the angular axis
        instead of distance.
        """
        ...
    def series(self) -> list[PySide6.QtCharts.QAbstractSeries]:
        """
        https://doc.qt.io/qt-6/qchart.html#series

        **QList<QAbstractSeries *> QChart::series() const**

        Returns all series that are added to the chart.

        **See also** **addSeries** (), **removeSeries** (), and
        **removeAllSeries** ().
        """
        ...
    def setAnimationDuration(self, msecs: int) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#animationDuration-prop

        **animationDuration : int**

        This property holds the duration of the animation for the chart.

        **Access functions:**

        int **animationDuration** () const
        void **setAnimationDuration** (int
        **msecs** )
        """
        ...
    def setAnimationEasingCurve(
        self,
        curve: PySide6.QtCore.QEasingCurve | PySide6.QtCore.QEasingCurve.Type,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#animationEasingCurve-prop

        **animationEasingCurve : QEasingCurve**

        This property holds the easing curve of the animation for the chart.

        **Access functions:**

        QEasingCurve **animationEasingCurve** () const
        void
        **setAnimationEasingCurve** (const QEasingCurve & **curve** )
        """
        ...
    def setAnimationOptions(
        self, options: PySide6.QtCharts.QChart.AnimationOptions
    ) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#animationOptions-prop

        **animationOptions : QChart::AnimationOptions**

        This property holds the animation options for the chart.

        Animations are enabled or disabled based on this setting.

        **Access functions:**

        QChart::AnimationOptions **animationOptions** () const
        void
        **setAnimationOptions** (QChart::AnimationOptions **options** )
        """
        ...
    def setAxisX(
        self,
        axis: PySide6.QtCharts.QAbstractAxis,
        series: PySide6.QtCharts.QAbstractSeries | None = ...,
    ) -> None: ...
    def setAxisY(
        self,
        axis: PySide6.QtCharts.QAbstractAxis,
        series: PySide6.QtCharts.QAbstractSeries | None = ...,
    ) -> None: ...
    def setBackgroundBrush(
        self,
        brush: (
            PySide6.QtGui.QBrush
            | PySide6.QtCore.Qt.BrushStyle
            | PySide6.QtCore.Qt.GlobalColor
            | PySide6.QtGui.QColor
            | PySide6.QtGui.QGradient
            | PySide6.QtGui.QImage
            | PySide6.QtGui.QPixmap
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#setBackgroundBrush

        **void QChart::setBackgroundBrush(const QBrush & brush )**

        Sets the brush that is used for painting the background of the chart
        area to **brush**.

        **See also** **backgroundBrush** ().
        """
        ...
    def setBackgroundPen(
        self,
        pen: PySide6.QtGui.QPen | PySide6.QtCore.Qt.PenStyle | PySide6.QtGui.QColor,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#setBackgroundPen

        **void QChart::setBackgroundPen(const QPen & pen )**

        Sets the pen that is used for painting the background of the chart area
        to **pen**.

        **See also** **backgroundPen** ().
        """
        ...
    def setBackgroundRoundness(self, diameter: float) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#backgroundRoundness-prop

        **backgroundRoundness : qreal**

        This property holds the diameter of the rounding circle at the corners
        of the chart background.

        **Access functions:**

        qreal **backgroundRoundness** () const
        void **setBackgroundRoundness**
        (qreal **diameter** )
        """
        ...
    def setBackgroundVisible(self, visible: bool = ...) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#backgroundVisible-prop

        **backgroundVisible : bool**

        This property holds whether the chart background is visible.

        **Access functions:**

        bool **isBackgroundVisible** () const
        void **setBackgroundVisible**
        (bool **visible** = true)

        **See also** **setBackgroundBrush** (), **setBackgroundPen** (), and
        **plotAreaBackgroundVisible** .
        """
        ...
    def setDropShadowEnabled(self, enabled: bool = ...) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#dropShadowEnabled-prop

        **dropShadowEnabled : bool**

        This property holds whether the background drop shadow effect is
        enabled.

        If set to `true`, the background drop shadow effect is enabled. If set
        to `false`, it is disabled.

        **Note:** The drop shadow effect depends on the theme, and therefore the
        setting may change if the theme is changed.

        **Access functions:**

        bool **isDropShadowEnabled** () const
        void **setDropShadowEnabled**
        (bool **enabled** = true)
        """
        ...
    def setLocale(
        self, locale: PySide6.QtCore.QLocale | PySide6.QtCore.QLocale.Language
    ) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#locale-prop

        **locale : QLocale**

        This property holds the locale used to format various chart labels.

        Labels are localized only when **localizeNumbers**  is `true`, except
        for **QDateTimeAxis**  labels, which always use the **QLocale**  set
        with this property.

        Defaults to the application default locale at the time when the chart is
        constructed.

        **Access functions:**

        QLocale **locale** () const
        void **setLocale** (const QLocale &
        **locale** )

        **See also** **localizeNumbers** .
        """
        ...
    def setLocalizeNumbers(self, localize: bool) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#localizeNumbers-prop

        **localizeNumbers : bool**

        This property holds whether numbers are localized.

        When `true`, all generated numbers appearing in various series and axis
        labels will be localized using the **QLocale**  set with the **locale**
        property. When `false`, the **C** locale is always used. Defaults to
        `false`.

        **Note:** This property does not affect **QDateTimeAxis**  labels, which
        always use the **QLocale**  set with the locale property.

        **Access functions:**

        bool **localizeNumbers** () const
        void **setLocalizeNumbers** (bool
        **localize** )

        **See also** **locale** .
        """
        ...
    def setMargins(self, margins: PySide6.QtCore.QMargins) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#margins-prop

        **margins : QMargins**

        This property holds the minimum margins allowed between the edge of the
        chart rectangle and the plot area.

        The margins are used for drawing the title, axes, and legend.

        **Access functions:**

        QMargins **margins** () const
        void **setMargins** (const QMargins &
        **margins** )
        """
        ...
    def setPlotArea(self, rect: PySide6.QtCore.QRectF | PySide6.QtCore.QRect) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#plotArea-prop

        **plotArea : QRectF**

        This property holds the rectangle within which the chart is drawn.

        The plot area does not include the area defined by margins. By default
        this will resize if inside a **QChartView** . If an explicit size is set
        for the plot area then it will respect this, to revert back to the
        default behavior, then calling `setPlotArea(QRectF());` will achieve
        this.

        **Access functions:**

        QRectF **plotArea** () const
        void **setPlotArea** (const QRectF &
        **rect** )

        **Notifier signal:**

        void **plotAreaChanged** (const QRectF & **plotArea** )
        """
        ...
    def setPlotAreaBackgroundBrush(
        self,
        brush: (
            PySide6.QtGui.QBrush
            | PySide6.QtCore.Qt.BrushStyle
            | PySide6.QtCore.Qt.GlobalColor
            | PySide6.QtGui.QColor
            | PySide6.QtGui.QGradient
            | PySide6.QtGui.QImage
            | PySide6.QtGui.QPixmap
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#setPlotAreaBackgroundBrush

        **void QChart::setPlotAreaBackgroundBrush(const QBrush & brush )**

        Sets the brush used to fill the background of the plot area of the chart
        to **brush**.

        **See also** **plotArea** (), **plotAreaBackgroundVisible** ,
        **setPlotAreaBackgroundPen** (), and **plotAreaBackgroundBrush** ().
        """
        ...
    def setPlotAreaBackgroundPen(
        self,
        pen: PySide6.QtGui.QPen | PySide6.QtCore.Qt.PenStyle | PySide6.QtGui.QColor,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#setPlotAreaBackgroundPen

        **void QChart::setPlotAreaBackgroundPen(const QPen & pen )**

        Sets the pen used to draw the background of the plot area of the chart
        to **pen**.

        **See also** **plotArea** (), **plotAreaBackgroundVisible** ,
        **setPlotAreaBackgroundBrush** (), and **plotAreaBackgroundPen** ().
        """
        ...
    def setPlotAreaBackgroundVisible(self, visible: bool = ...) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#plotAreaBackgroundVisible-prop

        **plotAreaBackgroundVisible : bool**

        This property holds whether the chart plot area background is visible.

        **Note:** By default, the plot area background is invisible and the plot
        area uses the general chart background.

        **Access functions:**

        bool **isPlotAreaBackgroundVisible** () const
        void
        **setPlotAreaBackgroundVisible** (bool **visible** = true)

        **See also** **setPlotAreaBackgroundBrush** (),
        **setPlotAreaBackgroundPen** (), and **backgroundVisible** .
        """
        ...
    def setTheme(self, theme: PySide6.QtCharts.QChart.ChartTheme) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#theme-prop

        **theme : QChart::ChartTheme**

        This property holds the theme used for the chart.

        **Access functions:**

        QChart::ChartTheme **theme** () const
        void **setTheme**
        (QChart::ChartTheme **theme** )
        """
        ...
    def setTitle(self, title: str) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#title-prop

        **title : QString**

        This property holds the title of the chart.

        The title is shown as a headline on top of the chart. Chart titles
        support HTML formatting.

        **Access functions:**

        QString **title** () const
        void **setTitle** (const QString &
        **title** )

        **Member Function Documentation**
        """
        ...
    def setTitleBrush(
        self,
        brush: (
            PySide6.QtGui.QBrush
            | PySide6.QtCore.Qt.BrushStyle
            | PySide6.QtCore.Qt.GlobalColor
            | PySide6.QtGui.QColor
            | PySide6.QtGui.QGradient
            | PySide6.QtGui.QImage
            | PySide6.QtGui.QPixmap
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#setTitleBrush

        **void QChart::setTitleBrush(const QBrush & brush )**

        Sets the brush used for drawing the title text to **brush**.

        **See also** **titleBrush** ().
        """
        ...
    def setTitleFont(self, font: PySide6.QtGui.QFont | str | Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#setTitleFont

        **void QChart::setTitleFont(const QFont & font )**

        Sets the font that is used for drawing the chart title to **font**.

        **See also** **titleFont** ().
        """
        ...
    def theme(self) -> PySide6.QtCharts.QChart.ChartTheme:
        """
        https://doc.qt.io/qt-6/qchart.html#theme-prop

        **theme : QChart::ChartTheme**

        This property holds the theme used for the chart.

        **Access functions:**

        QChart::ChartTheme **theme** () const
        void **setTheme**
        (QChart::ChartTheme **theme** )
        """
        ...
    def title(self) -> str:
        """
        https://doc.qt.io/qt-6/qchart.html#title-prop

        **title : QString**

        This property holds the title of the chart.

        The title is shown as a headline on top of the chart. Chart titles
        support HTML formatting.

        **Access functions:**

        QString **title** () const
        void **setTitle** (const QString &
        **title** )

        **Member Function Documentation**
        """
        ...
    def titleBrush(self) -> PySide6.QtGui.QBrush:
        """
        https://doc.qt.io/qt-6/qchart.html#titleBrush

        **QBrush QChart::titleBrush() const**

        Returns the brush used for drawing the title text.

        **See also** **setTitleBrush** ().
        """
        ...
    def titleFont(self) -> PySide6.QtGui.QFont:
        """
        https://doc.qt.io/qt-6/qchart.html#titleFont

        **QFont QChart::titleFont() const**

        Gets the font that is used for drawing the chart title.

        **See also** **setTitleFont** ().
        """
        ...
    def zoom(self, factor: float) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#zoom

        **void QChart::zoom(qreal factor )**

        Zooms into the view by the custom factor **factor**.

        A factor over 1.0 zooms into the view and a factor between 0.0 and 1.0
        zooms out of it.
        """
        ...
    @overload
    def zoomIn(self) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#zoomIn

        **void QChart::zoomIn()**

        Zooms into the view by a factor of two.
        """
        ...
    @overload
    def zoomIn(self, rect: PySide6.QtCore.QRectF | PySide6.QtCore.QRect) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#zoomIn-1

        **void QChart::zoomIn(const QRectF & rect )**

        Zooms into the view to a maximum level at which the rectangle **rect**
        is still fully visible.

        **Note:** Applying a zoom may modify properties of attached axes, for
        instance QAbstractAxis::min and QAbstractAxis::max.

        **Note:** This is not supported for polar charts.
        """
        ...
    def zoomOut(self) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#zoomOut

        **void QChart::zoomOut()**

        Zooms out of the view by a factor of two.

        **Note:** This will do nothing if the result would contain an invalid
        logarithmic axis range.
        """
        ...
    def zoomReset(self) -> None:
        """
        https://doc.qt.io/qt-6/qchart.html#zoomReset

        **void QChart::zoomReset()**

        Resets the series domains to what they were before any zoom method was
        called.

        **Note:** This will also reset scrolling and explicit axis range
        settings specified between the first zoom operation and calling this
        method. If no zoom operation has been performed, this method does
        nothing.
        """
        ...
    @property
    def plotAreaChanged(self) -> PySide6.QtCore.SignalInstance: ...
