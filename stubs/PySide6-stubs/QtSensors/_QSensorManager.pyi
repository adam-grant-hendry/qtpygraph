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

class QSensorManager:
    """
    https://doc.qt.io/qt-6/qsensormanager.html

    **Detailed Description**

    Sensor plugins register backends using the **registerBackend** () function.

    When **QSensor::connectToBackend** () is called, the **createBackend** ()
    function will be called.
    """

    def __init__(self) -> None: ...
    @staticmethod
    def createBackend(
        sensor: PySide6.QtSensors.QSensor,
    ) -> PySide6.QtSensors.QSensorBackend:
        """
        https://doc.qt.io/qt-6/qsensormanager.html#createBackend

        **[static] QSensorBackend *QSensorManager::createBackend(QSensor *
        sensor )**

        Create a backend for **sensor**. Returns null if no suitable backend
        exists.
        """
        ...
    @staticmethod
    def isBackendRegistered(
        type: PySide6.QtCore.QByteArray | bytes,
        identifier: PySide6.QtCore.QByteArray | bytes,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qsensormanager.html#isBackendRegistered

        **[static] bool QSensorManager::isBackendRegistered(const QByteArray &
        type , const QByteArray & identifier )**

        Returns true if the backend identified by **type** and **identifier** is
        registered.

        This is a convenience method that helps out plugins doing dynamic
        registration.
        """
        ...
    @staticmethod
    def registerBackend(
        type: PySide6.QtCore.QByteArray | bytes,
        identifier: PySide6.QtCore.QByteArray | bytes,
        factory: PySide6.QtSensors.QSensorBackendFactory,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsensormanager.html#registerBackend

        **[static] void QSensorManager::registerBackend(const QByteArray & type
        , const QByteArray & identifier , QSensorBackendFactory * factory )**

        Register a sensor for **type**. The **identifier** must be unique.

        The **factory** will be asked to create instances of the backend.

        Sensor identifiers starting with `generic` or `dummy` are given lower
        priority when choosing the default sensor if other sensors are found.
        """
        ...
    @staticmethod
    def setDefaultBackend(
        type: PySide6.QtCore.QByteArray | bytes,
        identifier: PySide6.QtCore.QByteArray | bytes,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsensormanager.html#setDefaultBackend

        **[static] void QSensorManager::setDefaultBackend(const QByteArray &
        type , const QByteArray & identifier )**

        Sets or overwrite the sensor **type** with the backend **identifier**.
        """
        ...
    @staticmethod
    def unregisterBackend(
        type: PySide6.QtCore.QByteArray | bytes,
        identifier: PySide6.QtCore.QByteArray | bytes,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsensormanager.html#unregisterBackend

        **[static] void QSensorManager::unregisterBackend(const QByteArray &
        type , const QByteArray & identifier )**

        Unregister the backend for **type** with **identifier**.

        Note that this only prevents new instance of the backend from being
        created. It does not invalidate the existing instances of the backend.
        The backend code should handle the disappearance of the underlying
        hardware itself.
        """
        ...
