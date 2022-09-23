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

from enum import IntFlag
from typing import Any

import PySide6.QtCharts
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QScatterSeries(PySide6.QtCharts.QXYSeries):
    """
    https://doc.qt.io/qt-6/qscatterseries.html

    **Detailed Description**

    The scatter data is displayed as a collection of points on the chart. For
    each point, two values are specified that determine its position on the
    horizontal axis and the vertical axis.

    ![](images/examples_scatterchart.png)

    The following code snippet illustrates how to create a basic scatter chart:

    **QScatterSeries** * series = new **QScatterSeries** ();
    series->append(0, 6);
        series->append(2, 4);
        ...
    chart->addSeries(series);

    For more information, see **ScatterChart Example**  and **Scatter
    Interactions Example** .
    """

    MarkerShapeCircle: QScatterSeries.MarkerShape = ...
    MarkerShapeRectangle: QScatterSeries.MarkerShape = ...
    MarkerShapeRotatedRectangle: QScatterSeries.MarkerShape = ...
    MarkerShapeTriangle: QScatterSeries.MarkerShape = ...
    MarkerShapeStar: QScatterSeries.MarkerShape = ...
    MarkerShapePentagon: QScatterSeries.MarkerShape = ...

    class MarkerShape(IntFlag):
        MarkerShapeCircle: QScatterSeries.MarkerShape = ...
        MarkerShapeRectangle: QScatterSeries.MarkerShape = ...
        MarkerShapeRotatedRectangle: QScatterSeries.MarkerShape = ...
        MarkerShapeTriangle: QScatterSeries.MarkerShape = ...
        MarkerShapeStar: QScatterSeries.MarkerShape = ...
        MarkerShapePentagon: QScatterSeries.MarkerShape = ...
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#QScatterSeries

        **QScatterSeries::QScatterSeries(QObject * parent = nullptr)**

        Constructs a series object that is a child of **parent**.
        """
        ...
    def borderColor(self) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#borderColor-prop

        **borderColor : QColor**

        This property holds the color used to draw the marker borders.

        This is a convenience property for modifying the color of the pen.

        **Access functions:**

        QColor **borderColor** () const
        void **setBorderColor** (const QColor
        & **color** )

        **Notifier signal:**

        void ****borderColorChanged** ** (QColor **color** )

        **See also** **QScatterSeries::pen** ().
        """
        ...
    def brush(self) -> PySide6.QtGui.QBrush:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#brush-prop

        **brush : QBrush**

        This property holds the brush used to draw the scatter series markers.

        The brush can be an image that can be created using **QPainterPath** ,
        for example.

        **Access functions:**

        QBrush **brush** () const
        virtual void ****setBrush** ** (const QBrush
        & **brush** ) override
        """
        ...
    def color(self) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#color-prop

        **color : QColor**

        This property holds the color used to fill the series markers.

        This is a convenience property for modifying the color of the brush.

        **Access functions:**

        virtual QColor **color** () const override
        virtual void **setColor**
        (const QColor & **color** ) override

        **Notifier signal:**

        void ****colorChanged** ** (QColor **color** )

        **See also** **QScatterSeries::brush** ().
        """
        ...
    def markerShape(self) -> PySide6.QtCharts.QScatterSeries.MarkerShape:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#markerShape-prop

        **markerShape : MarkerShape**

        This property holds the shape of the marker used to render the points in
        the series.

        The default shape is **MarkerShapeCircle** .

        **Access functions:**

        QScatterSeries::MarkerShape **markerShape** () const
        void
        **setMarkerShape** (QScatterSeries::MarkerShape **shape** )

        **Notifier signal:**

        void ****markerShapeChanged** ** (QScatterSeries::MarkerShape **shape**
        )

        **See also** **MarkerShape** .
        """
        ...
    def markerSize(self) -> float:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#markerSize-prop

        **markerSize : qreal**

        This property holds the size of the marker used to render the points in
        the series.

        **Access functions:**

        qreal **markerSize** () const
        void **setMarkerSize** (qreal **size** )

        **Notifier signal:**

        void ****markerSizeChanged** ** (qreal **size** )

        **See also** **QXYSeries::setMarkerSize** .

        **Member Function Documentation**
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
        https://doc.qt.io/qt-6/qscatterseries.html#borderColor-prop

        **borderColor : QColor**

        This property holds the color used to draw the marker borders.

        This is a convenience property for modifying the color of the pen.

        **Access functions:**

        QColor **borderColor** () const
        void **setBorderColor** (const QColor
        & **color** )

        **Notifier signal:**

        void ****borderColorChanged** ** (QColor **color** )

        **See also** **QScatterSeries::pen** ().
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
        https://doc.qt.io/qt-6/qscatterseries.html#setBrush

        **[override virtual] void QScatterSeries::setBrush(const QBrush & brush
        )**

        Reimplements: **QXYSeries::setBrush** (const QBrush &brush).

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
        https://doc.qt.io/qt-6/qscatterseries.html#color-prop

        **color : QColor**

        This property holds the color used to fill the series markers.

        This is a convenience property for modifying the color of the brush.

        **Access functions:**

        virtual QColor **color** () const override
        virtual void **setColor**
        (const QColor & **color** ) override

        **Notifier signal:**

        void ****colorChanged** ** (QColor **color** )

        **See also** **QScatterSeries::brush** ().
        """
        ...
    def setMarkerShape(self, shape: PySide6.QtCharts.QScatterSeries.MarkerShape) -> None:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#markerShape-prop

        **markerShape : MarkerShape**

        This property holds the shape of the marker used to render the points in
        the series.

        The default shape is **MarkerShapeCircle** .

        **Access functions:**

        QScatterSeries::MarkerShape **markerShape** () const
        void
        **setMarkerShape** (QScatterSeries::MarkerShape **shape** )

        **Notifier signal:**

        void ****markerShapeChanged** ** (QScatterSeries::MarkerShape **shape**
        )

        **See also** **MarkerShape** .
        """
        ...
    def setMarkerSize(self, size: float) -> None:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#markerSize-prop

        **markerSize : qreal**

        This property holds the size of the marker used to render the points in
        the series.

        **Access functions:**

        qreal **markerSize** () const
        void **setMarkerSize** (qreal **size** )

        **Notifier signal:**

        void ****markerSizeChanged** ** (qreal **size** )

        **See also** **QXYSeries::setMarkerSize** .

        **Member Function Documentation**
        """
        ...
    def setPen(
        self,
        pen: PySide6.QtGui.QPen | PySide6.QtCore.Qt.PenStyle | PySide6.QtGui.QColor,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#setPen

        **[override virtual] void QScatterSeries::setPen(const QPen & pen )**

        Reimplements: **QXYSeries::setPen** (const QPen &pen).
        """
        ...
    def type(self) -> PySide6.QtCharts.QAbstractSeries.SeriesType:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#type

        **[override virtual] QAbstractSeries::SeriesType QScatterSeries::type()
        const**

        Reimplements an access function for property: **QAbstractSeries::type**
        .
        """
        ...
    @property
    def borderColorChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#borderColorChanged

        **[signal] void QScatterSeries::borderColorChanged(QColor color )**

        This signal is emitted when the line (pen) color changes to **color**.

        **Note:** Notifier signal for property **borderColor** .
        """
        ...
    @property
    def colorChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#colorChanged

        **[signal] void QScatterSeries::colorChanged(QColor color )**

        This signal is emitted when the fill (brush) color changes to **color**.

        **Note:** Notifier signal for property **color** .
        """
        ...
    @property
    def markerShapeChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#markerShapeChanged

        **[signal] void
        QScatterSeries::markerShapeChanged(QScatterSeries::MarkerShape shape )**

        This signal is emitted when the marker shape changes to **shape**.

        **Note:** Notifier signal for property **markerShape** .
        """
        ...
    @property
    def markerSizeChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qscatterseries.html#markerSizeChanged

        **[signal] void QScatterSeries::markerSizeChanged(qreal size )**

        This signal is emitted when the marker size changes to **size**.

        **Note:** Notifier signal for property **markerSize** .
        """
        ...
