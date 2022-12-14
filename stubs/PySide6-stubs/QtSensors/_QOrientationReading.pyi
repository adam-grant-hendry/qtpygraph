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

from enum import IntFlag

import PySide6.QtCore
import PySide6.QtSensors

class QOrientationReading(PySide6.QtSensors.QSensorReading):
    """
    https://doc.qt.io/qt-6/qorientationreading.html

    **Detailed Description**

    The orientation sensor reports the orientation of the device. As it operates
    below the UI level it does not report on or even know how the UI is rotated.
    Most importantly this means that this sensor cannot be used to detect if a
    device is in portrait or landscape mode.

    This sensor is useful to detect that a particular side of the device is
    pointing up.

    **QOrientationReading Units**

    The orientation sensor returns the orientation of the device using the pre-
    defined values found in the **QOrientationReading::Orientation**  enum.
    """

    Undefined: QOrientationReading.Orientation = ...
    TopUp: QOrientationReading.Orientation = ...
    TopDown: QOrientationReading.Orientation = ...
    LeftUp: QOrientationReading.Orientation = ...
    RightUp: QOrientationReading.Orientation = ...
    FaceUp: QOrientationReading.Orientation = ...
    FaceDown: QOrientationReading.Orientation = ...

    class Orientation(IntFlag):
        Undefined: QOrientationReading.Orientation = ...
        TopUp: QOrientationReading.Orientation = ...
        TopDown: QOrientationReading.Orientation = ...
        LeftUp: QOrientationReading.Orientation = ...
        RightUp: QOrientationReading.Orientation = ...
        FaceUp: QOrientationReading.Orientation = ...
        FaceDown: QOrientationReading.Orientation = ...
    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...
    def copyValuesFrom(self, other: PySide6.QtSensors.QSensorReading) -> None: ...
    def orientation(self) -> PySide6.QtSensors.QOrientationReading.Orientation:
        """
        https://doc.qt.io/qt-6/qorientationreading.html#orientation-prop

        **[read-only] orientation : const Orientation**

        This property holds the orientation of the device.

        The unit is an enumeration describing the orientation of the device.

        **Access functions:**

        QOrientationReading::Orientation **orientation** () const

        **See also** **QOrientationReading Units** .

        **Member Function Documentation**
        """
        ...
    def setOrientation(
        self, orientation: PySide6.QtSensors.QOrientationReading.Orientation
    ) -> None:
        """
        https://doc.qt.io/qt-6/qorientationreading.html#setOrientation

        **void
        QOrientationReading::setOrientation(QOrientationReading::Orientation
        orientation )**

        Sets the **orientation** for the reading.

        **See also** **orientation** ().
        """
        ...
