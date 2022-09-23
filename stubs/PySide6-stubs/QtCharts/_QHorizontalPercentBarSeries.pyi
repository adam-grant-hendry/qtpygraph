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

class QHorizontalPercentBarSeries(PySide6.QtCharts.QAbstractBarSeries):
    """
    https://doc.qt.io/qt-6/qhorizontalpercentbarseries.html

    **Detailed Description**

    This class draws data as a series of uniformly sized horizontally stacked
    bars, with one bar per category. Each bar set added to the series
    contributes a single segment to each stacked bar. The segment size
    corresponds to the percentage of the segment value compared with the total
    value of all segments in the stack. Bars with zero value are not drawn.

    See the **horizontal percent bar chart example**  to learn how to create a
    horizontal percent bar chart.

    ![](images/examples_horizontalpercentbarchart.png)

    **See also** **QBarSet** , **QBarSeries** , **QPercentBarSeries** ,
    **QAbstractBarSeries** , **QStackedBarSeries** ,
    **QHorizontalStackedBarSeries** , and **QHorizontalBarSeries** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qhorizontalpercentbarseries.html#QHorizontalPerce
        ntBarSeries

        **QHorizontalPercentBarSeries::QHorizontalPercentBarSeries(QObject *
        parent = nullptr)**

        Constructs an empty horizontal percent bar series that is a **QObject**
        and a child of **parent**.
        """
        ...
    def type(self) -> PySide6.QtCharts.QAbstractSeries.SeriesType:
        """
        https://doc.qt.io/qt-6/qhorizontalpercentbarseries.html#type

        **[override virtual] QAbstractSeries::SeriesType
        QHorizontalPercentBarSeries::type() const**

        Reimplements an access function for property: **QAbstractSeries::type**
        .

        Returns the horizontal percent bar series.
        """
        ...
