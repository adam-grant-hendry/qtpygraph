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
from typing import Any

import PySide6.QtCharts
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QLegend(PySide6.QtWidgets.QGraphicsWidget):
    """
    https://doc.qt.io/qt-6/qlegend.html

    **Detailed Description**

    A legend is a graphical object that displays the legend of a chart. The
    legend state is updated by **QChart**  when series change. By default, the
    legend is attached to the chart, but it can be detached to make it
    independent of chart layout. Legend objects cannot be created or deleted,
    but they can be referenced via the **QChart**  class.

    ![](images/examples_percentbarchart_legend.png)

    **See also** **QChart** .
    """

    MarkerShapeDefault: QLegend.MarkerShape = ...
    MarkerShapeRectangle: QLegend.MarkerShape = ...
    MarkerShapeCircle: QLegend.MarkerShape = ...
    MarkerShapeFromSeries: QLegend.MarkerShape = ...
    MarkerShapeRotatedRectangle: QLegend.MarkerShape = ...
    MarkerShapeTriangle: QLegend.MarkerShape = ...
    MarkerShapeStar: QLegend.MarkerShape = ...
    MarkerShapePentagon: QLegend.MarkerShape = ...

    class MarkerShape(IntFlag):
        MarkerShapeDefault: QLegend.MarkerShape = ...
        MarkerShapeRectangle: QLegend.MarkerShape = ...
        MarkerShapeCircle: QLegend.MarkerShape = ...
        MarkerShapeFromSeries: QLegend.MarkerShape = ...
        MarkerShapeRotatedRectangle: QLegend.MarkerShape = ...
        MarkerShapeTriangle: QLegend.MarkerShape = ...
        MarkerShapeStar: QLegend.MarkerShape = ...
        MarkerShapePentagon: QLegend.MarkerShape = ...
    def alignment(self) -> PySide6.QtCore.Qt.Alignment:
        """
        https://doc.qt.io/qt-6/qlegend.html#alignment-prop

        **alignment : Qt::Alignment**

        How the legend is aligned with the chart.

        Can be **Qt::AlignTop** , **Qt::AlignBottom** , **Qt::AlignLeft** ,
        **Qt::AlignRight** . If you set more than one flag, the result is
        undefined.

        **Access functions:**

        Qt::Alignment **alignment** () const
        void **setAlignment**
        (Qt::Alignment **alignment** )
        """
        ...
    def attachToChart(self) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#attachToChart

        **void QLegend::attachToChart()**

        Attaches the legend to a chart. The chart may adjust the layout of the
        legend.
        """
        ...
    def borderColor(self) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qlegend.html#borderColor-prop

        **borderColor : QColor**

        This property holds the line color of the legend.

        **Access functions:**

        QColor **borderColor** ()
        void **setBorderColor** (QColor **color** )

        **Notifier signal:**

        void ****borderColorChanged** ** (QColor **color** )
        """
        ...
    def brush(self) -> PySide6.QtGui.QBrush:
        """
        https://doc.qt.io/qt-6/qlegend.html#brush

        **QBrush QLegend::brush() const**

        Returns the brush used by the legend.

        **See also** **setBrush** ().
        """
        ...
    def color(self) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qlegend.html#color-prop

        **color : QColor**

        This property holds the background (brush) color of the legend.

        If you change the color of the legend, the style of the legend brush is
        set to **Qt::SolidPattern** .

        **Access functions:**

        QColor **color** ()
        void **setColor** (QColor **color** )

        **Notifier signal:**

        void ****colorChanged** ** (QColor **color** )
        """
        ...
    def detachFromChart(self) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#detachFromChart

        **void QLegend::detachFromChart()**

        Detaches the legend from the chart. The chart will no longer adjust the
        layout of the legend.
        """
        ...
    def font(self) -> PySide6.QtGui.QFont:
        """
        https://doc.qt.io/qt-6/qlegend.html#font-prop

        **font : QFont**

        This property holds the font of the markers used by the legend.

        **Access functions:**

        QFont **font** () const
        void **setFont** (const QFont & **font** )

        **Notifier signal:**

        void ****fontChanged** ** (QFont **font** )
        """
        ...
    def hideEvent(self, event: PySide6.QtGui.QHideEvent) -> None: ...
    def isAttachedToChart(self) -> bool:
        """
        https://doc.qt.io/qt-6/qlegend.html#isAttachedToChart

        **bool QLegend::isAttachedToChart()**

        Returns `true`, if the legend is attached to a chart.
        """
        ...
    def isBackgroundVisible(self) -> bool:
        """
        https://doc.qt.io/qt-6/qlegend.html#isBackgroundVisible

        **bool QLegend::isBackgroundVisible() const**

        Returns the visibility of the legend background.

        **Note:** Getter function for property **backgroundVisible** .
        """
        ...
    def isInteractive(self) -> bool:
        """
        https://doc.qt.io/qt-6/qlegend.html#isInteractive

        **[since 6.2] bool QLegend::isInteractive() const**

        Returns whether the legend can be dragged or resized using a mouse when
        it is detached.

        This function was introduced in Qt 6.2.

        **See also** **QLegend::setInteractive** ().
        """
        ...
    def labelBrush(self) -> PySide6.QtGui.QBrush:
        """
        https://doc.qt.io/qt-6/qlegend.html#labelBrush

        **QBrush QLegend::labelBrush() const**

        Returns the brush used to draw labels.

        **See also** **setLabelBrush** ().
        """
        ...
    def labelColor(self) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qlegend.html#labelColor-prop

        **labelColor : QColor**

        This property holds the color of the brush used to draw labels.

        **Access functions:**

        QColor **labelColor** () const
        void **setLabelColor** (QColor
        **color** )

        **Notifier signal:**

        void ****labelColorChanged** ** (QColor **color** )
        """
        ...
    def markerShape(self) -> PySide6.QtCharts.QLegend.MarkerShape:
        """
        https://doc.qt.io/qt-6/qlegend.html#markerShape-prop

        **[since 5.9] markerShape : MarkerShape**

        The default shape of the legend markers. The default value is
        `MarkerShapeRectangle`.

        This property was introduced in Qt 5.9.

        **Access functions:**

        QLegend::MarkerShape **markerShape** () const
        void **setMarkerShape**
        (QLegend::MarkerShape **shape** )

        **Notifier signal:**

        void **markerShapeChanged** (QLegend::MarkerShape **shape** )
        """
        ...
    def markers(
        self, series: PySide6.QtCharts.QAbstractSeries | None = ...
    ) -> list[PySide6.QtCharts.QLegendMarker]:
        """
        https://doc.qt.io/qt-6/qlegend.html#markers

        **QList<QLegendMarker *> QLegend::markers(QAbstractSeries * series =
        nullptr) const**

        Returns the list of markers in the legend. The list can be filtered by
        specifying the **series** for which the markers are returned.
        """
        ...
    def paint(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionGraphicsItem,
        widget: PySide6.QtWidgets.QWidget | None = ...,
    ) -> None: ...
    def pen(self) -> PySide6.QtGui.QPen:
        """
        https://doc.qt.io/qt-6/qlegend.html#pen

        **QPen QLegend::pen() const**

        Returns the pen used by the legend.

        **See also** **setPen** ().
        """
        ...
    def reverseMarkers(self) -> bool:
        """
        https://doc.qt.io/qt-6/qlegend.html#reverseMarkers-prop

        **reverseMarkers : bool**

        This property holds whether reverse order is used for the markers in the
        legend.

        This property is `false` by default.

        **Access functions:**

        bool **reverseMarkers** ()
        void **setReverseMarkers** (bool
        **reverseMarkers** = true)

        **Notifier signal:**

        void ****reverseMarkersChanged** ** (bool **reverseMarkers** )
        """
        ...
    def setAlignment(self, alignment: PySide6.QtCore.Qt.Alignment) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#alignment-prop

        **alignment : Qt::Alignment**

        How the legend is aligned with the chart.

        Can be **Qt::AlignTop** , **Qt::AlignBottom** , **Qt::AlignLeft** ,
        **Qt::AlignRight** . If you set more than one flag, the result is
        undefined.

        **Access functions:**

        Qt::Alignment **alignment** () const
        void **setAlignment**
        (Qt::Alignment **alignment** )
        """
        ...
    def setBackgroundVisible(self, visible: bool = ...) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#setBackgroundVisible

        **void QLegend::setBackgroundVisible(bool visible = true)**

        Sets the visibility of the legend background to **visible**.

        **Note:** Setter function for property **backgroundVisible** .

        **See also** **isBackgroundVisible** ().
        """
        ...
    def setBorderColor(
        self,
        color: (
            PySide6.QtGui.QColor
            | PySide6.QtGui.QRgba64
            | Any
            | PySide6.QtCore.Qt.GlobalColor
            | str
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#borderColor-prop

        **borderColor : QColor**

        This property holds the line color of the legend.

        **Access functions:**

        QColor **borderColor** ()
        void **setBorderColor** (QColor **color** )

        **Notifier signal:**

        void ****borderColorChanged** ** (QColor **color** )
        """
        ...
    def setBrush(
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
        https://doc.qt.io/qt-6/qlegend.html#setBrush

        **void QLegend::setBrush(const QBrush & brush )**

        Sets the **brush** that is used to draw the background of the legend.

        **See also** **brush** ().
        """
        ...
    def setColor(
        self,
        color: (
            PySide6.QtGui.QColor
            | PySide6.QtGui.QRgba64
            | Any
            | PySide6.QtCore.Qt.GlobalColor
            | str
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#color-prop

        **color : QColor**

        This property holds the background (brush) color of the legend.

        If you change the color of the legend, the style of the legend brush is
        set to **Qt::SolidPattern** .

        **Access functions:**

        QColor **color** ()
        void **setColor** (QColor **color** )

        **Notifier signal:**

        void ****colorChanged** ** (QColor **color** )
        """
        ...
    def setFont(self, font: PySide6.QtGui.QFont | str | Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#font-prop

        **font : QFont**

        This property holds the font of the markers used by the legend.

        **Access functions:**

        QFont **font** () const
        void **setFont** (const QFont & **font** )

        **Notifier signal:**

        void ****fontChanged** ** (QFont **font** )
        """
        ...
    def setInteractive(self, interactive: bool) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#setInteractive

        **[since 6.2] void QLegend::setInteractive(bool interactive )**

        When **interactive** is `true` and the legend is detached, the legend is
        able to be moved and resized with a mouse in a similar way to a window.

        The legend will automatically attach to an edge of the chart by dragging
        it off of that edge. Double clicking an attached legend will detach it.
        This is `false` by default.

        This function was introduced in Qt 6.2.

        **See also** **QLegend::isInteractive** ().
        """
        ...
    def setLabelBrush(
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
        https://doc.qt.io/qt-6/qlegend.html#setLabelBrush

        **void QLegend::setLabelBrush(const QBrush & brush )**

        Sets the brush used to draw the legend labels to **brush**.

        **See also** **labelBrush** ().
        """
        ...
    def setLabelColor(
        self,
        color: (
            PySide6.QtGui.QColor
            | PySide6.QtGui.QRgba64
            | Any
            | PySide6.QtCore.Qt.GlobalColor
            | str
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#labelColor-prop

        **labelColor : QColor**

        This property holds the color of the brush used to draw labels.

        **Access functions:**

        QColor **labelColor** () const
        void **setLabelColor** (QColor
        **color** )

        **Notifier signal:**

        void ****labelColorChanged** ** (QColor **color** )
        """
        ...
    def setMarkerShape(self, shape: PySide6.QtCharts.QLegend.MarkerShape) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#markerShape-prop

        **[since 5.9] markerShape : MarkerShape**

        The default shape of the legend markers. The default value is
        `MarkerShapeRectangle`.

        This property was introduced in Qt 5.9.

        **Access functions:**

        QLegend::MarkerShape **markerShape** () const
        void **setMarkerShape**
        (QLegend::MarkerShape **shape** )

        **Notifier signal:**

        void **markerShapeChanged** (QLegend::MarkerShape **shape** )
        """
        ...
    def setPen(
        self,
        pen: PySide6.QtGui.QPen | PySide6.QtCore.Qt.PenStyle | PySide6.QtGui.QColor,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#setPen

        **void QLegend::setPen(const QPen & pen )**

        Sets the **pen** that is used to draw the legend borders.

        **See also** **pen** ().
        """
        ...
    def setReverseMarkers(self, reverseMarkers: bool = ...) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#reverseMarkers-prop

        **reverseMarkers : bool**

        This property holds whether reverse order is used for the markers in the
        legend.

        This property is `false` by default.

        **Access functions:**

        bool **reverseMarkers** ()
        void **setReverseMarkers** (bool
        **reverseMarkers** = true)

        **Notifier signal:**

        void ****reverseMarkersChanged** ** (bool **reverseMarkers** )
        """
        ...
    def setShowToolTips(self, show: bool) -> None:
        """
        https://doc.qt.io/qt-6/qlegend.html#setShowToolTips

        **void QLegend::setShowToolTips(bool show )**

        When **show** is `true`, the legend labels will show a tooltip when the
        mouse hovers over them if the label itself is shown elided. This is
        `false` by default.

        **Note:** Setter function for property **showToolTips** .

        **See also** **showToolTips** ().
        """
        ...
    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None: ...
    def showToolTips(self) -> bool:
        """
        https://doc.qt.io/qt-6/qlegend.html#showToolTips

        **bool QLegend::showToolTips() const**

        Returns whether the tooltips are shown for the legend labels when they
        are elided.

        **Note:** Getter function for property showToolTips.

        **See also** **setShowToolTips** ().
        """
        ...
    @property
    def attachedToChartChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegend.html#attachedToChartChanged

        **[signal, since 6.2] void QLegend::attachedToChartChanged(bool attached
        )**

        This signal is emitted when the legend is **attached** to or detached
        from the chart.

        This function was introduced in Qt 6.2.
        """
        ...
    @property
    def backgroundVisibleChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegend.html#backgroundVisibleChanged

        **[signal] void QLegend::backgroundVisibleChanged(bool visible )**

        This signal is emitted when the visibility of the legend background
        changes to **visible**.

        **Note:** Notifier signal for property **backgroundVisible** .
        """
        ...
    @property
    def borderColorChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegend.html#borderColorChanged

        **[signal] void QLegend::borderColorChanged(QColor color )**

        This signal is emitted when the border color of the legend background
        changes to **color**.

        **Note:** Notifier signal for property **borderColor** .
        """
        ...
    @property
    def colorChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegend.html#colorChanged

        **[signal] void QLegend::colorChanged(QColor color )**

        This signal is emitted when the color of the legend background changes
        to **color**.

        **Note:** Notifier signal for property **color** .
        """
        ...
    @property
    def fontChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegend.html#fontChanged

        **[signal] void QLegend::fontChanged(QFont font )**

        This signal is emitted when the font of the markers of the legend
        changes to **font**.

        **Note:** Notifier signal for property **font** .
        """
        ...
    @property
    def labelColorChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegend.html#labelColorChanged

        **[signal] void QLegend::labelColorChanged(QColor color )**

        This signal is emitted when the color of the brush used to draw the
        legend labels changes to **color**.

        **Note:** Notifier signal for property **labelColor** .
        """
        ...
    @property
    def markerShapeChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def reverseMarkersChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegend.html#reverseMarkersChanged

        **[signal] void QLegend::reverseMarkersChanged(bool reverseMarkers )**

        This signal is emitted when the use of reverse order for the markers in
        the legend is changed to **reverseMarkers**.

        **Note:** Notifier signal for property **reverseMarkers** .
        """
        ...
    @property
    def showToolTipsChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegend.html#showToolTipsChanged

        **[signal] void QLegend::showToolTipsChanged(bool showToolTips )**

        This signal is emitted when the visibility of tooltips is changed to
        **showToolTips**.

        **Note:** Notifier signal for property **showToolTips** .
        """
        ...