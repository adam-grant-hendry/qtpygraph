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

class QPieLegendMarker(PySide6.QtCharts.QLegendMarker):
    """
    https://doc.qt.io/qt-6/qpielegendmarker.html

    **Detailed Description**

    A pie legend marker is related to **QPieSeries** . With a pie series, each
    slice of the pie is related to one marker in the legend.

    **See also** **QLegend** , **QPieSeries** , and **QPieSlice** .
    """

    def __init__(
        self,
        series: PySide6.QtCharts.QPieSeries,
        slice: PySide6.QtCharts.QPieSlice,
        legend: PySide6.QtCharts.QLegend,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None: ...
    def series(self) -> PySide6.QtCharts.QPieSeries:
        """
        https://doc.qt.io/qt-6/qpielegendmarker.html#series

        **[override virtual] QPieSeries *QPieLegendMarker::series()**

        Reimplements: **QLegendMarker::series** ().
        """
        ...
    def slice(self) -> PySide6.QtCharts.QPieSlice:
        """
        https://doc.qt.io/qt-6/qpielegendmarker.html#slice

        **QPieSlice *QPieLegendMarker::slice()**

        Returns the slice of the pie related to the marker.
        """
        ...
    def type(self) -> PySide6.QtCharts.QLegendMarker.LegendMarkerType:
        """
        https://doc.qt.io/qt-6/qpielegendmarker.html#type

        **[override virtual] QLegendMarker::LegendMarkerType
        QPieLegendMarker::type()**

        Reimplements: **QLegendMarker::type** ().
        """
        ...