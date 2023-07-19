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

class QLineSeries(PySide6.QtCharts.QXYSeries):
    """
    https://doc.qt.io/qt-6/qlineseries.html

    **Detailed Description**

    A line chart is used to show information as a series of data points
    connected by straight lines.

    ![](images/examples_linechart.png)

    Creating a basic line chart is simple:

    **QLineSeries** * series = new **QLineSeries** ();
        series->append(0, 6);
    series->append(2, 4);
        ...
        chart->addSeries(series);
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qlineseries.html#QLineSeries

        **QLineSeries::QLineSeries(QObject * parent = nullptr)**

        Constructs an empty series object that is a child of **parent**. When
        the series object is added to a **QChartView**  or **QChart**  instance,
        the ownership is transferred.
        """
        ...
    def type(self) -> PySide6.QtCharts.QAbstractSeries.SeriesType:
        """
        https://doc.qt.io/qt-6/qlineseries.html#type

        **[override virtual] QAbstractSeries::SeriesType QLineSeries::type()
        const**

        Reimplements an access function for property: **QAbstractSeries::type**
        .
        """
        ...