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
PySide6.QtBluetooth, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from collections.abc import Sequence
from enum import IntFlag
from typing import overload

import PySide6.QtBluetooth
import PySide6.QtCore

class QLowEnergyAdvertisingData:
    """
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html

    **Detailed Description**

    This data can include the device name, GATT services offered by the device,
    and so on. The data set via this class will be used when advertising is
    started by calling **QLowEnergyController::startAdvertising** (). Objects of
    this class can represent an Advertising Data packet or a Scan Response
    packet.

    **Note:** The actual data packets sent over the advertising channel cannot
    contain more than 31 bytes. If the variable-length data set via this class
    exceeds that limit, it will be left out of the packet or truncated,
    depending on the type.

    **See also** **QLowEnergyAdvertisingParameters**  and
    **QLowEnergyController::startAdvertising** ().
    """

    DiscoverabilityNone: QLowEnergyAdvertisingData.Discoverability = ...
    DiscoverabilityLimited: QLowEnergyAdvertisingData.Discoverability = ...
    DiscoverabilityGeneral: QLowEnergyAdvertisingData.Discoverability = ...

    class Discoverability(IntFlag):
        DiscoverabilityNone: QLowEnergyAdvertisingData.Discoverability = ...
        DiscoverabilityLimited: QLowEnergyAdvertisingData.Discoverability = ...
        DiscoverabilityGeneral: QLowEnergyAdvertisingData.Discoverability = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#QLowEnergyAdvertis
        ingData

        **QLowEnergyAdvertisingData::QLowEnergyAdvertisingData()**

        Creates a new object of this class. All values are initialized to their
        defaults according to the Bluetooth Low Energy specification.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QLowEnergyAdvertisingData) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#QLowEnergyAdvertis
        ingData-1

        **QLowEnergyAdvertisingData::QLowEnergyAdvertisingData(const
        QLowEnergyAdvertisingData & other )**

        Constructs a new object of this class that is a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def discoverability(
        self,
    ) -> PySide6.QtBluetooth.QLowEnergyAdvertisingData.Discoverability:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#discoverability

        **QLowEnergyAdvertisingData::Discoverability
        QLowEnergyAdvertisingData::discoverability() const**

        Returns the discoverability mode of the advertising device. The default
        is **DiscoverabilityNone** .

        **See also** **setDiscoverability** ().
        """
        ...
    def includePowerLevel(self) -> bool:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#includePowerLevel

        **bool QLowEnergyAdvertisingData::includePowerLevel() const**

        Returns whether to include the device's transmit power level in the
        advertising data. The default is `false`.

        **See also** **setIncludePowerLevel** ().
        """
        ...
    @staticmethod
    def invalidManufacturerId() -> int:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#invalidManufacture
        rId

        **[static] quint16 QLowEnergyAdvertisingData::invalidManufacturerId()**

        Returns an invalid manufacturer id. If this value is set as the
        manufacturer id (which it is by default), no manufacturer data will be
        present in the advertising data.
        """
        ...
    def localName(self) -> str:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#localName

        **QString QLowEnergyAdvertisingData::localName() const**

        Returns the name of the local device that is to be advertised.

        **See also** **setLocalName** ().
        """
        ...
    def manufacturerData(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#manufacturerData

        **QByteArray QLowEnergyAdvertisingData::manufacturerData() const**

        Returns the manufacturer data. The default is an empty byte array.

        **See also** **setManufacturerData** ().
        """
        ...
    def manufacturerId(self) -> int:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#manufacturerId

        **quint16 QLowEnergyAdvertisingData::manufacturerId() const**

        Returns the manufacturer id. The default is
        **QLowEnergyAdvertisingData::invalidManufacturerId** (), which means the
        data will not be advertised.
        """
        ...
    def rawData(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#rawData

        **QByteArray QLowEnergyAdvertisingData::rawData() const**

        Returns the user-supplied raw data to be advertised. The default is an
        empty byte array.

        **See also** **setRawData** ().
        """
        ...
    def services(self) -> list[PySide6.QtBluetooth.QBluetoothUuid]:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#services

        **QList<QBluetoothUuid> QLowEnergyAdvertisingData::services() const**

        Returns the list of service UUIDs to be advertised. By default, this
        list is empty.

        **See also** **setServices** ().
        """
        ...
    def setDiscoverability(
        self, mode: PySide6.QtBluetooth.QLowEnergyAdvertisingData.Discoverability
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#setDiscoverability

        **void QLowEnergyAdvertisingData::setDiscoverability(QLowEnergyAdvertisi
        ngData::Discoverability mode )**

        Sets the discoverability type of the advertising device to **mode**.

        **Note:** Discoverability information can only appear in an actual
        advertising data packet. If this object acts as scan response data, a
        call to this function will have no effect on the scan response sent.

        **See also** **discoverability** ().
        """
        ...
    def setIncludePowerLevel(self, doInclude: bool) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#setIncludePowerLev
        el

        **void QLowEnergyAdvertisingData::setIncludePowerLevel(bool doInclude
        )**

        Specifies whether to include the device's transmit power level in the
        advertising data. If **doInclude** is `true`, the data will be included,
        otherwise it will not.

        **See also** **includePowerLevel** ().
        """
        ...
    def setLocalName(self, name: str) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#setLocalName

        **void QLowEnergyAdvertisingData::setLocalName(const QString & name )**

        Specifies that **name** should be broadcast as the name of the device.
        If the full name does not fit into the advertising data packet, an
        abbreviated name is sent, as described by the Bluetooth Low Energy
        specification.

        On Android, the local name cannot be changed. Android always uses the
        device name. If this local name is not empty, the Android implementation
        includes the device name in the advertisement packet; otherwise the
        device name is omitted from the advertisement packet.

        **See also** **localName** ().
        """
        ...
    def setManufacturerData(
        self, id: int, data: PySide6.QtCore.QByteArray | bytes
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#setManufacturerDat
        a

        **void QLowEnergyAdvertisingData::setManufacturerData(quint16 id , const
        QByteArray & data )**

        Sets the manufacturer id and data. The **id** parameter is a company
        identifier as assigned by the Bluetooth SIG. The **data** parameter is
        an arbitrary value.

        **See also** **manufacturerData** ().
        """
        ...
    def setRawData(self, data: PySide6.QtCore.QByteArray | bytes) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#setRawData

        **void QLowEnergyAdvertisingData::setRawData(const QByteArray & data )**

        Sets the data to be advertised to **data**. If the value is not an empty
        byte array, it will be sent as-is as the advertising data and all other
        data in this object will be ignored. This can be used to send non-
        standard data.

        **Note:** If **data** is longer than 31 bytes, it will be truncated. It
        is the caller's responsibility to ensure that **data** is well-formed.

        **See also** **rawData** ().
        """
        ...
    def setServices(self, services: Sequence[PySide6.QtBluetooth.QBluetoothUuid]) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#setServices

        **void QLowEnergyAdvertisingData::setServices(const
        QList<QBluetoothUuid> & services )**

        Specifies that the service UUIDs in **services** should be advertised.
        If the entire list does not fit into the packet, an incomplete list is
        sent as specified by the Bluetooth Low Energy specification.

        **See also** **services** ().
        """
        ...
    def swap(self, other: PySide6.QtBluetooth.QLowEnergyAdvertisingData) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#swap

        **void QLowEnergyAdvertisingData::swap(QLowEnergyAdvertisingData & other
        )**

        Swaps this object with **other**.
        """
        ...
