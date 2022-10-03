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
PySide6.QtPositioning, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag

import PySide6.QtCore
import PySide6.QtPositioning

class QNmeaPositionInfoSource(PySide6.QtPositioning.QGeoPositionInfoSource):
    """
    https://doc.qt.io/qt-6/qnmeapositioninfosource.html

    **Detailed Description**

    NMEA is a commonly used protocol for the specification of one's global
    position at a certain point in time. The QNmeaPositionInfoSource class reads
    NMEA data and uses it to provide positional data in the form of
    **QGeoPositionInfo**  objects.

    A QNmeaPositionInfoSource instance operates in either **RealTimeMode**  or
    **SimulationMode** . These modes allow NMEA data to be read from either a
    live source of positional data, or replayed for simulation purposes from
    previously recorded NMEA data.

    The source of NMEA data is set with **setDevice** ().

    Use **startUpdates** () to start receiving regular position updates and
    **stopUpdates** () to stop these updates. If you only require updates
    occasionally, you can call **requestUpdate** () to request a single update.

    In both cases the position information is received via the
    **positionUpdated** () signal and the last known position can be accessed
    with **lastKnownPosition** ().

    QNmeaPositionInfoSource supports reporting the accuracy of the horizontal
    and vertical position. To enable position accuracy reporting an estimate of
    the User Equivalent Range Error associated with the NMEA source must be set
    with **setUserEquivalentRangeError** ().
    """

    RealTimeMode: QNmeaPositionInfoSource.UpdateMode = ...
    SimulationMode: QNmeaPositionInfoSource.UpdateMode = ...

    class UpdateMode(IntFlag):
        RealTimeMode: QNmeaPositionInfoSource.UpdateMode = ...
        SimulationMode: QNmeaPositionInfoSource.UpdateMode = ...
    def __init__(
        self,
        updateMode: PySide6.QtPositioning.QNmeaPositionInfoSource.UpdateMode,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#QNmeaPositionInfoSou
        rce

        **QNmeaPositionInfoSource::QNmeaPositionInfoSource(QNmeaPositionInfoSour
        ce::UpdateMode updateMode , QObject * parent = nullptr)**

        Constructs a QNmeaPositionInfoSource instance with the given **parent**
        and **updateMode**.
        """
        ...
    def device(self) -> PySide6.QtCore.QIODevice:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#device

        **QIODevice *QNmeaPositionInfoSource::device() const**

        Returns the NMEA data source.

        **See also** **setDevice** ().
        """
        ...
    def error(self) -> PySide6.QtPositioning.QGeoPositionInfoSource.Error:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#error

        **[override virtual] QGeoPositionInfoSource::Error
        QNmeaPositionInfoSource::error() const**

        Reimplements: **QGeoPositionInfoSource::error() const** .
        """
        ...
    def lastKnownPosition(
        self, fromSatellitePositioningMethodsOnly: bool = ...
    ) -> PySide6.QtPositioning.QGeoPositionInfo:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#lastKnownPosition

        **[override virtual] QGeoPositionInfo
        QNmeaPositionInfoSource::lastKnownPosition(bool
        fromSatellitePositioningMethodsOnly = false) const**

        Reimplements: **QGeoPositionInfoSource::lastKnownPosition(bool
        fromSatellitePositioningMethodsOnly) const** .
        """
        ...
    def minimumUpdateInterval(self) -> int:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#minimumUpdateInterva
        l

        **[override virtual] int
        QNmeaPositionInfoSource::minimumUpdateInterval() const**

        Reimplements an access function for property:
        **QGeoPositionInfoSource::minimumUpdateInterval** .
        """
        ...
    def parsePosInfoFromNmeaData(
        self, data: bytes, size: int, posInfo: PySide6.QtPositioning.QGeoPositionInfo
    ) -> tuple[bool, bool]:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#parsePosInfoFromNmea
        Data

        **[virtual protected] bool
        QNmeaPositionInfoSource::parsePosInfoFromNmeaData(const char * data ,
        int size , QGeoPositionInfo * posInfo , bool * hasFix )**

        Parses an NMEA sentence string into a **QGeoPositionInfo** .

        The default implementation will parse standard NMEA sentences. This
        method should be reimplemented in a subclass whenever the need to deal
        with non-standard NMEA sentences arises.

        The parser reads **size** bytes from **data** and uses that information
        to setup **posInfo** and **hasFix**. If **hasFix** is set to false then
        **posInfo** may contain only the time or the date and the time.

        Returns true if the sentence was successfully parsed, otherwise returns
        false and should not modifiy **posInfo** or **hasFix**.
        """
        ...
    def requestUpdate(self, timeout: int = ...) -> None:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#requestUpdate

        **[override virtual slot] void
        QNmeaPositionInfoSource::requestUpdate(int msec = 0)**

        Reimplements: **QGeoPositionInfoSource::requestUpdate** (int timeout).
        """
        ...
    def setDevice(self, source: PySide6.QtCore.QIODevice) -> None:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#setDevice

        **void QNmeaPositionInfoSource::setDevice(QIODevice * device )**

        Sets the NMEA data source to **device**. If the device is not open, it
        will be opened in QIODevice::ReadOnly mode.

        The source device can only be set once and must be set before calling
        **startUpdates** () or **requestUpdate** ().

        **Note:** The **device** must emit **QIODevice::readyRead** () for the
        source to be notified when data is available for reading.
        **QNmeaPositionInfoSource**  does not assume the ownership of the
        device, and hence does not deallocate it upon destruction.

        **See also** **device** ().
        """
        ...
    def setError(
        self, positionError: PySide6.QtPositioning.QGeoPositionInfoSource.Error
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#error

        **[override virtual] QGeoPositionInfoSource::Error
        QNmeaPositionInfoSource::error() const**

        Reimplements: **QGeoPositionInfoSource::error() const** .
        """
        ...
    def setUpdateInterval(self, msec: int) -> None:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#setUpdateInterval

        **[override virtual] void QNmeaPositionInfoSource::setUpdateInterval(int
        msec )**

        Reimplements an access function for property:
        **QGeoPositionInfoSource::updateInterval** .
        """
        ...
    def setUserEquivalentRangeError(self, uere: float) -> None:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#setUserEquivalentRan
        geError

        **[since 5.3] void
        QNmeaPositionInfoSource::setUserEquivalentRangeError(double uere )**

        Sets the User Equivalent Range Error (UERE) to **uere**. The UERE is
        used in calculating an estimate of the accuracy of the position
        information reported by the position info source. The UERE should be set
        to a value appropriate for the GPS device which generated the NMEA
        stream.

        The true UERE value is calculated from multiple error sources including
        errors introduced by the satellites and signal propogation delays
        through the atmosphere as well as errors introduced by the receiving GPS
        equipment. For details on GPS accuracy see **Sam J. Wormley, GPS Errors
        & Estimating Your Reveiver's Accuracy** .

        A typical value for UERE is approximately 5.1.

        This function was introduced in Qt 5.3.

        **See also** **userEquivalentRangeError** ().
        """
        ...
    def startUpdates(self) -> None:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#startUpdates

        **[override virtual slot] void QNmeaPositionInfoSource::startUpdates()**

        Reimplements: **QGeoPositionInfoSource::startUpdates** ().
        """
        ...
    def stopUpdates(self) -> None:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#stopUpdates

        **[override virtual slot] void QNmeaPositionInfoSource::stopUpdates()**

        Reimplements: **QGeoPositionInfoSource::stopUpdates** ().
        """
        ...
    def supportedPositioningMethods(
        self,
    ) -> PySide6.QtPositioning.QGeoPositionInfoSource.PositioningMethods:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#supportedPositioning
        Methods

        **[override virtual] QGeoPositionInfoSource::PositioningMethods
        QNmeaPositionInfoSource::supportedPositioningMethods() const**

        Reimplements: **QGeoPositionInfoSource::supportedPositioningMethods()
        const** .
        """
        ...
    def updateMode(self) -> PySide6.QtPositioning.QNmeaPositionInfoSource.UpdateMode:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#updateMode

        **QNmeaPositionInfoSource::UpdateMode
        QNmeaPositionInfoSource::updateMode() const**

        Returns the update mode.
        """
        ...
    def userEquivalentRangeError(self) -> float:
        """
        https://doc.qt.io/qt-6/qnmeapositioninfosource.html#userEquivalentRangeE
        rror

        **[since 5.3] double QNmeaPositionInfoSource::userEquivalentRangeError()
        const**

        Returns the current User Equivalent Range Error (UERE). The UERE is used
        in calculating an estimate of the accuracy of the position information
        reported by the position info source. The default value is NaN which
        means no accuracy information will be provided.

        This function was introduced in Qt 5.3.

        **See also** **setUserEquivalentRangeError** ().
        """
        ...