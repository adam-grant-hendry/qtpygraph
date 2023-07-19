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

class QCandlestickLegendMarker(PySide6.QtCharts.QLegendMarker):
    """
    https://doc.qt.io/qt-6/qcandlesticklegendmarker.html

    **Detailed Description**

    QCandlestickLegendMarker is related to **QCandlestickSeries** , so that one
    candlestick series results in one marker.

    **See also** **QLegend**  and **QCandlestickSeries** .
    """

    def __init__(
        self,
        series: PySide6.QtCharts.QCandlestickSeries,
        legend: PySide6.QtCharts.QLegend,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None: ...
    def series(self) -> PySide6.QtCharts.QCandlestickSeries:
        """
        https://doc.qt.io/qt-6/qcandlesticklegendmarker.html#series

        **[override virtual] QCandlestickSeries
        *QCandlestickLegendMarker::series()**

        Reimplements: **QLegendMarker::series** ().
        """
        ...
    def type(self) -> PySide6.QtCharts.QLegendMarker.LegendMarkerType:
        """
        https://doc.qt.io/qt-6/qcandlesticklegendmarker.html#type

        **[override virtual] QLegendMarker::LegendMarkerType
        QCandlestickLegendMarker::type()**

        Reimplements: **QLegendMarker::type** ().
        """
        ...