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
PySide6.QtSensors, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore
import PySide6.QtSensors

class QGyroscopeFilter(PySide6.QtSensors.QSensorFilter):
    """
    https://doc.qt.io/qt-6/qgyroscopefilter.html

    **Detailed Description**

    The only difference is that the **filter** () method features a pointer to
    **QGyroscopeReading**  instead of **QSensorReading** .
    """

    @overload
    def filter(self, reading: PySide6.QtSensors.QGyroscopeReading) -> bool:
        """
        https://doc.qt.io/qt-6/qgyroscopefilter.html#filter

        **[pure virtual] bool QGyroscopeFilter::filter(QGyroscopeReading *
        reading )**

        Called when **reading** changes. Returns false to prevent the reading
        from propagating.

        **See also** **QSensorFilter::filter** ().
        """
        ...
    @overload
    def filter(self, reading: PySide6.QtSensors.QSensorReading) -> bool:
        """
        https://doc.qt.io/qt-6/qgyroscopefilter.html#filter

        **[pure virtual] bool QGyroscopeFilter::filter(QGyroscopeReading *
        reading )**

        Called when **reading** changes. Returns false to prevent the reading
        from propagating.

        **See also** **QSensorFilter::filter** ().
        """
        ...
