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

import PySide6.QtCharts
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QLegendMarker(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qlegendmarker.html

    **Detailed Description**

    A legend marker consists of an icon and a label. The icon color corresponds
    to the color used to draw a series and the label displays the name of the
    series (or the label of the slice for a pie series or bar set for a bar
    series). A legend marker is always related to one series, slice, or bar set.

    ![](images/examples_percentbarchart_legend.png)

    **See also** **QLegend** .
    """

    LegendMarkerTypeArea: QLegendMarker.LegendMarkerType = ...
    LegendMarkerTypeBar: QLegendMarker.LegendMarkerType = ...
    LegendMarkerTypePie: QLegendMarker.LegendMarkerType = ...
    LegendMarkerTypeXY: QLegendMarker.LegendMarkerType = ...
    LegendMarkerTypeBoxPlot: QLegendMarker.LegendMarkerType = ...
    LegendMarkerTypeCandlestick: QLegendMarker.LegendMarkerType = ...

    class LegendMarkerType(IntFlag):
        LegendMarkerTypeArea: QLegendMarker.LegendMarkerType = ...
        LegendMarkerTypeBar: QLegendMarker.LegendMarkerType = ...
        LegendMarkerTypePie: QLegendMarker.LegendMarkerType = ...
        LegendMarkerTypeXY: QLegendMarker.LegendMarkerType = ...
        LegendMarkerTypeBoxPlot: QLegendMarker.LegendMarkerType = ...
        LegendMarkerTypeCandlestick: QLegendMarker.LegendMarkerType = ...
    def brush(self) -> PySide6.QtGui.QBrush:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#brush

        **QBrush QLegendMarker::brush() const**

        Returns the brush used to fill the icon.

        **Note:** Getter function for property brush.

        **See also** **setBrush** ().
        """
        ...
    def font(self) -> PySide6.QtGui.QFont:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#font

        **QFont QLegendMarker::font() const**

        Retuns the font of the label.

        **Note:** Getter function for property font.

        **See also** **setFont** ().
        """
        ...
    def isVisible(self) -> bool:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#isVisible

        **bool QLegendMarker::isVisible() const**

        Returns the visibility of the marker.

        **Note:** Getter function for property **visible** .
        """
        ...
    def label(self) -> str:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#label

        **QString QLegendMarker::label() const**

        Returns the label of the marker.

        **Note:** Getter function for property label.

        **See also** **setLabel** ().
        """
        ...
    def labelBrush(self) -> PySide6.QtGui.QBrush:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#labelBrush

        **QBrush QLegendMarker::labelBrush() const**

        Returns the brush that is used to draw the label.

        **Note:** Getter function for property labelBrush.

        **See also** **setLabelBrush** ().
        """
        ...
    def pen(self) -> PySide6.QtGui.QPen:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#pen

        **QPen QLegendMarker::pen() const**

        Returns the pen used to draw the outline of the icon.

        **Note:** Getter function for property pen.

        **See also** **setPen** ().
        """
        ...
    def series(self) -> PySide6.QtCharts.QAbstractSeries:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#series

        **[pure virtual] QAbstractSeries *QLegendMarker::series()**

        Returns a pointer to the series that is related to this legend marker. A
        legend marker is always related to a series.
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
        https://doc.qt.io/qt-6/qlegendmarker.html#setBrush

        **void QLegendMarker::setBrush(const QBrush & brush )**

        Sets the brush used to fill the icon to **brush**.

        **Note:** Changing the color of the series also changes the color of the
        icon.

        **Note:** Setter function for property **brush** .

        **See also** **brush** ().
        """
        ...
    def setFont(self, font: PySide6.QtGui.QFont | str | Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#setFont

        **void QLegendMarker::setFont(const QFont & font )**

        Sets the font of the label to **font**.

        **Note:** Setter function for property **font** .

        **See also** **font** ().
        """
        ...
    def setLabel(self, label: str) -> None:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#setLabel

        **void QLegendMarker::setLabel(const QString & label )**

        Sets the label of the marker to **label**.

        **Note:** Changing the name of a series also changes the label of its
        marker.

        **Note:** Setter function for property **label** .

        **See also** **label** ().
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
        https://doc.qt.io/qt-6/qlegendmarker.html#setLabelBrush

        **void QLegendMarker::setLabelBrush(const QBrush & brush )**

        Sets the the brush used to draw to label to **brush**.

        **Note:** Setter function for property **labelBrush** .

        **See also** **labelBrush** ().
        """
        ...
    def setPen(
        self,
        pen: PySide6.QtGui.QPen | PySide6.QtCore.Qt.PenStyle | PySide6.QtGui.QColor,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#setPen

        **void QLegendMarker::setPen(const QPen & pen )**

        Sets the **pen** used to draw the outline of the icon to **pen**.

        **Note:** Setter function for property **pen** .

        **See also** **pen** ().
        """
        ...
    def setShape(self, shape: PySide6.QtCharts.QLegend.MarkerShape) -> None:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#shape-prop

        **shape : QLegend::MarkerShape**

        The shape of the legend marker. Defaults to
        **QLegend::MarkerShapeDefault** , which indicates the shape is
        determined by **QLegend::markerShape**  property.

        **Access functions:**

        QLegend::MarkerShape **shape** () const
        void **setShape**
        (QLegend::MarkerShape **shape** )

        **Notifier signal:**

        void **shapeChanged** ()
        """
        ...
    def setVisible(self, visible: bool) -> None:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#setVisible

        **void QLegendMarker::setVisible(bool visible )**

        Sets the marker's visibility to **visible**.

        **Note:** Setter function for property **visible** .

        **See also** **isVisible** ().
        """
        ...
    def shape(self) -> PySide6.QtCharts.QLegend.MarkerShape:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#shape-prop

        **shape : QLegend::MarkerShape**

        The shape of the legend marker. Defaults to
        **QLegend::MarkerShapeDefault** , which indicates the shape is
        determined by **QLegend::markerShape**  property.

        **Access functions:**

        QLegend::MarkerShape **shape** () const
        void **setShape**
        (QLegend::MarkerShape **shape** )

        **Notifier signal:**

        void **shapeChanged** ()
        """
        ...
    def type(self) -> PySide6.QtCharts.QLegendMarker.LegendMarkerType:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#type

        **[pure virtual] QLegendMarker::LegendMarkerType QLegendMarker::type()**

        Returns the type of the legend marker for the related series, pie slice,
        or bar set.

        **See also** **LegendMarkerType** .
        """
        ...
    @property
    def brushChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#brushChanged

        **[signal] void QLegendMarker::brushChanged()**

        This signal is emitted when the brush of the legend marker has changed.

        **Note:** Notifier signal for property **brush** .
        """
        ...
    @property
    def clicked(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#clicked

        **[signal] void QLegendMarker::clicked()**

        This signal is emitted when the legend marker is clicked.
        """
        ...
    @property
    def fontChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#fontChanged

        **[signal] void QLegendMarker::fontChanged()**

        This signal is emitted when the (label) font of the legend marker has
        changed.

        **Note:** Notifier signal for property **font** .
        """
        ...
    @property
    def hovered(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#hovered

        **[signal] void QLegendMarker::hovered(bool status )**

        This signal is emitted when a mouse is hovered over the legend marker.
        When the mouse moves over the marker, **status** turns `true`, and when
        the mouse moves away again, it turns `false`.
        """
        ...
    @property
    def labelBrushChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#labelBrushChanged

        **[signal] void QLegendMarker::labelBrushChanged()**

        This signal is emitted when the label brush of the legend marker has
        changed.

        **Note:** Notifier signal for property **labelBrush** .
        """
        ...
    @property
    def labelChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#labelChanged

        **[signal] void QLegendMarker::labelChanged()**

        This signal is emitted when the label of the legend marker has changed.

        **Note:** Notifier signal for property **label** .
        """
        ...
    @property
    def penChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#penChanged

        **[signal] void QLegendMarker::penChanged()**

        This signal is emitted when the pen of the legend marker has changed.

        **Note:** Notifier signal for property **pen** .
        """
        ...
    @property
    def shapeChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def visibleChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlegendmarker.html#visibleChanged

        **[signal] void QLegendMarker::visibleChanged()**

        This signal is emitted when the visibility of the legend marker has
        changed.

        **Note:** Notifier signal for property **visible** .
        """
        ...
