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

import PySide6.QtCore
import PySide6.QtSensors

class QCompassReading(PySide6.QtSensors.QSensorReading):
    """
    https://doc.qt.io/qt-6/qcompassreading.html

    **Detailed Description**

    **QCompassReading Units**

    The compass returns the azimuth of the device as degrees from magnetic north
    in a clockwise direction based on the top of the device, as defined by
    **QScreen::nativeOrientation** . There is also a value to indicate the
    calibration status of the device. If the device is not calibrated the
    azimuth may not be accurate.

    Digital compasses are susceptible to magnetic interference and may need
    calibration after being placed near anything that emits a magnetic force.
    Accuracy of the compass can be affected by any ferrous materials that are
    nearby.

    The calibration status of the device is measured as a number from 0 to 1. A
    value of 1 is the highest level that the device can support and 0 is the
    worst.
    """

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...
    def azimuth(self) -> float:
        """
        https://doc.qt.io/qt-6/qcompassreading.html#azimuth-prop

        **[read-only] azimuth : const qreal**

        This property holds the azimuth of the device.

        Measured in degrees from magnetic north in a clockwise direction based
        on the top of the device, as defined by **QScreen::nativeOrientation** .

        **Access functions:**

        qreal **azimuth** () const

        **See also** **QCompassReading Units** .
        """
        ...
    def calibrationLevel(self) -> float:
        """
        https://doc.qt.io/qt-6/qcompassreading.html#calibrationLevel-prop

        **[read-only] calibrationLevel : const qreal**

        This property holds the calibration level of the reading.

        Measured as a value from 0 to 1 with higher values being better.

        **Access functions:**

        qreal **calibrationLevel** () const

        **See also** **QCompassReading Units** .

        **Member Function Documentation**
        """
        ...
    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def setAzimuth(self, azimuth: float) -> None:
        """
        https://doc.qt.io/qt-6/qcompassreading.html#setAzimuth

        **void QCompassReading::setAzimuth(qreal azimuth )**

        Sets the **azimuth** of the device.

        **See also** **azimuth** () and **QCompassReading Units** .
        """
        ...
    def setCalibrationLevel(self, calibrationLevel: float) -> None:
        """
        https://doc.qt.io/qt-6/qcompassreading.html#setCalibrationLevel

        **void QCompassReading::setCalibrationLevel(qreal calibrationLevel )**

        Sets the calibration level of the reading to **calibrationLevel**.

        **See also** **calibrationLevel** ().
        """
        ...
