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

class QAccelerometerReading(PySide6.QtSensors.QSensorReading):
    """
    https://doc.qt.io/qt-6/qaccelerometerreading.html

    **Detailed Description**

    **QAccelerometerReading Units**

    The scale of the values is meters per second squared. The axes are arranged
    as follows.

    ![](images/sensors-coordinates2.jpg)

    A monoblock device sitting at rest, face up on a desk will experience a
    force of approximately 9.8 on the Z axis (ie. towards the roof). This is the
    proper acceleration the device experiences relative to freefall.
    """

    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...
    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def setX(self, x: float) -> None:
        """
        https://doc.qt.io/qt-6/qaccelerometerreading.html#setX

        **void QAccelerometerReading::setX(qreal x )**

        Sets the acceleration on the X axis to **x**.

        **See also** **x** ().
        """
        ...
    def setY(self, y: float) -> None:
        """
        https://doc.qt.io/qt-6/qaccelerometerreading.html#setY

        **void QAccelerometerReading::setY(qreal y )**

        Sets the acceleration on the Y axis to **y**.

        **See also** **y** ().
        """
        ...
    def setZ(self, z: float) -> None:
        """
        https://doc.qt.io/qt-6/qaccelerometerreading.html#setZ

        **void QAccelerometerReading::setZ(qreal z )**

        Sets the acceleration on the Z axis to **z**.

        **See also** **z** ().
        """
        ...
    def x(self) -> float:
        """
        https://doc.qt.io/qt-6/qaccelerometerreading.html#x-prop

        **[read-only] x : const qreal**

        This property holds the acceleration on the X axis.

        The scale of the values is meters per second squared.

        **Access functions:**

        qreal **x** () const

        **See also** **QAccelerometerReading Units** .
        """
        ...
    def y(self) -> float:
        """
        https://doc.qt.io/qt-6/qaccelerometerreading.html#y-prop

        **[read-only] y : const qreal**

        This property holds the acceleration on the Y axis.

        The scale of the values is meters per second squared.

        **Access functions:**

        qreal **y** () const

        **See also** **QAccelerometerReading Units** .
        """
        ...
    def z(self) -> float:
        """
        https://doc.qt.io/qt-6/qaccelerometerreading.html#z-prop

        **[read-only] z : const qreal**

        This property holds the acceleration on the Z axis.

        The scale of the values is meters per second squared.

        **Access functions:**

        qreal **z** () const

        **See also** **QAccelerometerReading Units** .

        **Member Function Documentation**
        """
        ...