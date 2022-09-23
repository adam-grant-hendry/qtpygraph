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

class QBarLegendMarker(PySide6.QtCharts.QLegendMarker):
    """
    https://doc.qt.io/qt-6/qbarlegendmarker.html

    **Detailed Description**

    A bar legend marker is related to **QAbstractBarSeries**  derived classes.
    With a bar series, each marker is related to one **QBarSet** .

    **See also** **QLegend** , **QAbstractBarSeries** , and **QBarSet** .
    """

    def __init__(
        self,
        series: PySide6.QtCharts.QAbstractBarSeries,
        barset: PySide6.QtCharts.QBarSet,
        legend: PySide6.QtCharts.QLegend,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None: ...
    def barset(self) -> PySide6.QtCharts.QBarSet:
        """
        https://doc.qt.io/qt-6/qbarlegendmarker.html#barset

        **QBarSet *QBarLegendMarker::barset()**

        Returns the bar set related to the marker.
        """
        ...
    def series(self) -> PySide6.QtCharts.QAbstractBarSeries:
        """
        https://doc.qt.io/qt-6/qbarlegendmarker.html#series

        **[override virtual] QAbstractBarSeries *QBarLegendMarker::series()**

        Reimplements: **QLegendMarker::series** ().
        """
        ...
    def type(self) -> PySide6.QtCharts.QLegendMarker.LegendMarkerType:
        """
        https://doc.qt.io/qt-6/qbarlegendmarker.html#type

        **[override virtual] QLegendMarker::LegendMarkerType
        QBarLegendMarker::type()**

        Reimplements: **QLegendMarker::type** ().
        """
        ...
