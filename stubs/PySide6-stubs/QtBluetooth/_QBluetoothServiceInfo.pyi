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
from typing import Any, overload

import PySide6.QtBluetooth
import PySide6.QtCore

class QBluetoothServiceInfo:
    """
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html

    **Detailed Description**

    QBluetoothServiceInfo provides information about a service offered by a
    Bluetooth device. In addition it can be used to register new services on the
    local device. Note that such a registration only affects the Bluetooth SDP
    entries. Any server listening for incoming connections (e.g an RFCOMM
    server) must be started before **registerService** () is called.
    Deregistration must happen in the reverse order.

    QBluetoothServiceInfo is not a value type in the traditional sense. All
    copies of the same service info object share the same data as they do not
    detach upon changing them. This ensures that two copies can (de)register the
    same Bluetooth service.

    On iOS, this class cannot be used because the platform does not expose an
    API which may permit access to QBluetoothServiceInfo related features.
    """

    ServiceRecordHandle: QBluetoothServiceInfo.AttributeId = ...
    ServiceClassIds: QBluetoothServiceInfo.AttributeId = ...
    ServiceRecordState: QBluetoothServiceInfo.AttributeId = ...
    ServiceId: QBluetoothServiceInfo.AttributeId = ...
    ProtocolDescriptorList: QBluetoothServiceInfo.AttributeId = ...
    BrowseGroupList: QBluetoothServiceInfo.AttributeId = ...
    LanguageBaseAttributeIdList: QBluetoothServiceInfo.AttributeId = ...
    ServiceInfoTimeToLive: QBluetoothServiceInfo.AttributeId = ...
    ServiceAvailability: QBluetoothServiceInfo.AttributeId = ...
    BluetoothProfileDescriptorList: QBluetoothServiceInfo.AttributeId = ...
    DocumentationUrl: QBluetoothServiceInfo.AttributeId = ...
    ClientExecutableUrl: QBluetoothServiceInfo.AttributeId = ...
    IconUrl: QBluetoothServiceInfo.AttributeId = ...
    AdditionalProtocolDescriptorList: QBluetoothServiceInfo.AttributeId = ...
    PrimaryLanguageBase: QBluetoothServiceInfo.AttributeId = ...
    ServiceName: QBluetoothServiceInfo.AttributeId = ...
    ServiceDescription: QBluetoothServiceInfo.AttributeId = ...
    ServiceProvider: QBluetoothServiceInfo.AttributeId = ...
    UnknownProtocol: QBluetoothServiceInfo.Protocol = ...
    L2capProtocol: QBluetoothServiceInfo.Protocol = ...
    RfcommProtocol: QBluetoothServiceInfo.Protocol = ...

    class Alternative:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(
            self,
            Alternative: (
                PySide6.QtBluetooth.QBluetoothServiceInfo.Alternative | Sequence[Any]
            ),
        ) -> None: ...
        @overload
        def __init__(self, list: Sequence[Any]) -> None: ...
        def __add__(self, l: Sequence[Any]) -> list[Any]: ...
        @staticmethod
        def __copy__() -> None: ...
        def __iadd__(self, l: Sequence[Any]) -> list[Any]: ...
        def __lshift__(self, l: Sequence[Any]) -> list[Any]: ...
        @overload
        def append(self, arg__1: Any) -> None: ...
        @overload
        def append(self, l: Sequence[Any]) -> None: ...
        def at(self, i: int) -> Any: ...
        def back(self) -> Any: ...
        def capacity(self) -> int: ...
        def clear(self) -> None: ...
        def constData(self) -> object: ...
        def constFirst(self) -> Any: ...
        def constLast(self) -> Any: ...
        def count(self) -> int: ...
        def data(self) -> object: ...
        def empty(self) -> bool: ...
        @overload
        def first(self) -> Any: ...
        @overload
        def first(self, n: int) -> list[Any]: ...
        @staticmethod
        def fromList(list: Sequence[Any]) -> list[Any]: ...
        @staticmethod
        def fromVector(vector: Sequence[Any]) -> list[Any]: ...
        def front(self) -> Any: ...
        def insert(self, arg__1: int, arg__2: Any) -> None: ...
        def isEmpty(self) -> bool: ...
        def isSharedWith(self, other: Sequence[Any]) -> bool: ...
        @overload
        def last(self) -> Any: ...
        @overload
        def last(self, n: int) -> list[Any]: ...
        def length(self) -> int: ...
        def mid(self, pos: int, len: int = ...) -> list[Any]: ...
        def move(self, from_: int, to: int) -> None: ...
        def pop_back(self) -> None: ...
        def pop_front(self) -> None: ...
        def prepend(self, arg__1: Any) -> None: ...
        def push_back(self, arg__1: Any) -> None: ...
        def push_front(self, arg__1: Any) -> None: ...
        def remove(self, i: int, n: int = ...) -> None: ...
        def removeAll(self, arg__1: Any) -> None: ...
        def removeAt(self, i: int) -> None: ...
        def removeFirst(self) -> None: ...
        def removeLast(self) -> None: ...
        def removeOne(self, arg__1: Any) -> None: ...
        def reserve(self, size: int) -> None: ...
        def resize(self, size: int) -> None: ...
        def shrink_to_fit(self) -> None: ...
        def size(self) -> int: ...
        @overload
        def sliced(self, pos: int) -> list[Any]: ...
        @overload
        def sliced(self, pos: int, n: int) -> list[Any]: ...
        def squeeze(self) -> None: ...
        def swap(self, other: Sequence[Any]) -> None: ...
        def swapItemsAt(self, i: int, j: int) -> None: ...
        def takeAt(self, i: int) -> Any: ...
        def toList(self) -> list[Any]: ...
        def toVector(self) -> list[Any]: ...
        def value(self, i: int) -> Any: ...

    class AttributeId(IntFlag):
        ServiceRecordHandle: QBluetoothServiceInfo.AttributeId = ...
        ServiceClassIds: QBluetoothServiceInfo.AttributeId = ...
        ServiceRecordState: QBluetoothServiceInfo.AttributeId = ...
        ServiceId: QBluetoothServiceInfo.AttributeId = ...
        ProtocolDescriptorList: QBluetoothServiceInfo.AttributeId = ...
        BrowseGroupList: QBluetoothServiceInfo.AttributeId = ...
        LanguageBaseAttributeIdList: QBluetoothServiceInfo.AttributeId = ...
        ServiceInfoTimeToLive: QBluetoothServiceInfo.AttributeId = ...
        ServiceAvailability: QBluetoothServiceInfo.AttributeId = ...
        BluetoothProfileDescriptorList: QBluetoothServiceInfo.AttributeId = ...
        DocumentationUrl: QBluetoothServiceInfo.AttributeId = ...
        ClientExecutableUrl: QBluetoothServiceInfo.AttributeId = ...
        IconUrl: QBluetoothServiceInfo.AttributeId = ...
        AdditionalProtocolDescriptorList: QBluetoothServiceInfo.AttributeId = ...
        PrimaryLanguageBase: QBluetoothServiceInfo.AttributeId = ...
        ServiceName: QBluetoothServiceInfo.AttributeId = ...
        ServiceDescription: QBluetoothServiceInfo.AttributeId = ...
        ServiceProvider: QBluetoothServiceInfo.AttributeId = ...

    class Protocol(IntFlag):
        UnknownProtocol: QBluetoothServiceInfo.Protocol = ...
        L2capProtocol: QBluetoothServiceInfo.Protocol = ...
        RfcommProtocol: QBluetoothServiceInfo.Protocol = ...

    class Sequence:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(
            self,
            Sequence: (
                PySide6.QtBluetooth.QBluetoothServiceInfo.Sequence | Sequence[Any]
            ),
        ) -> None: ...
        @overload
        def __init__(self, list: Sequence[Any]) -> None: ...
        def __add__(self, l: Sequence[Any]) -> list[Any]: ...
        @staticmethod
        def __copy__() -> None: ...
        def __iadd__(self, l: Sequence[Any]) -> list[Any]: ...
        def __lshift__(self, l: Sequence[Any]) -> list[Any]: ...
        @overload
        def append(self, arg__1: Any) -> None: ...
        @overload
        def append(self, l: Sequence[Any]) -> None: ...
        def at(self, i: int) -> Any: ...
        def back(self) -> Any: ...
        def capacity(self) -> int: ...
        def clear(self) -> None: ...
        def constData(self) -> object: ...
        def constFirst(self) -> Any: ...
        def constLast(self) -> Any: ...
        def count(self) -> int: ...
        def data(self) -> object: ...
        def empty(self) -> bool: ...
        @overload
        def first(self) -> Any: ...
        @overload
        def first(self, n: int) -> list[Any]: ...
        @staticmethod
        def fromList(list: Sequence[Any]) -> list[Any]: ...
        @staticmethod
        def fromVector(vector: Sequence[Any]) -> list[Any]: ...
        def front(self) -> Any: ...
        def insert(self, arg__1: int, arg__2: Any) -> None: ...
        def isEmpty(self) -> bool: ...
        def isSharedWith(self, other: Sequence[Any]) -> bool: ...
        @overload
        def last(self) -> Any: ...
        @overload
        def last(self, n: int) -> list[Any]: ...
        def length(self) -> int: ...
        def mid(self, pos: int, len: int = ...) -> list[Any]: ...
        def move(self, from_: int, to: int) -> None: ...
        def pop_back(self) -> None: ...
        def pop_front(self) -> None: ...
        def prepend(self, arg__1: Any) -> None: ...
        def push_back(self, arg__1: Any) -> None: ...
        def push_front(self, arg__1: Any) -> None: ...
        def remove(self, i: int, n: int = ...) -> None: ...
        def removeAll(self, arg__1: Any) -> None: ...
        def removeAt(self, i: int) -> None: ...
        def removeFirst(self) -> None: ...
        def removeLast(self) -> None: ...
        def removeOne(self, arg__1: Any) -> None: ...
        def reserve(self, size: int) -> None: ...
        def resize(self, size: int) -> None: ...
        def shrink_to_fit(self) -> None: ...
        def size(self) -> int: ...
        @overload
        def sliced(self, pos: int) -> list[Any]: ...
        @overload
        def sliced(self, pos: int, n: int) -> list[Any]: ...
        def squeeze(self) -> None: ...
        def swap(self, other: Sequence[Any]) -> None: ...
        def swapItemsAt(self, i: int, j: int) -> None: ...
        def takeAt(self, i: int) -> Any: ...
        def toList(self) -> list[Any]: ...
        def toVector(self) -> list[Any]: ...
        def value(self, i: int) -> Any: ...

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#QBluetoothServiceInfo

        **QBluetoothServiceInfo::QBluetoothServiceInfo()**

        Construct a new invalid QBluetoothServiceInfo;
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QBluetoothServiceInfo) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#QBluetoothServiceInfo-
        1

        **QBluetoothServiceInfo::QBluetoothServiceInfo(const
        QBluetoothServiceInfo & other )**

        Construct a new QBluetoothServiceInfo that is a copy of **other**.

        The two copies continue to share the same underlying data which does not
        detach upon write.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def attribute(self, attributeId: int) -> Any:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#attribute

        **QVariant QBluetoothServiceInfo::attribute(quint16 attributeId )
        const**

        Returns the value of the attribute **attributeId**.

        **See also** **setAttribute** ().
        """
        ...
    def attributes(self) -> list[int]:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#attributes

        **QList<quint16> QBluetoothServiceInfo::attributes() const**

        Returns a list of all attribute ids that the **QBluetoothServiceInfo**
        object has.
        """
        ...
    def contains(self, attributeId: int) -> bool:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#contains

        **bool QBluetoothServiceInfo::contains(quint16 attributeId ) const**

        Returns true if the **QBluetoothServiceInfo**  object contains the
        attribute **attributeId** , otherwise returns false.
        """
        ...
    def device(self) -> PySide6.QtBluetooth.QBluetoothDeviceInfo:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#device

        **QBluetoothDeviceInfo QBluetoothServiceInfo::device() const**

        Returns the address of the Bluetooth device that provides this service.

        **See also** **setDevice** ().
        """
        ...
    def isComplete(self) -> bool:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#isComplete

        **bool QBluetoothServiceInfo::isComplete() const**

        Returns true if the **QBluetoothServiceInfo**  object is considered
        complete, otherwise returns false.

        A complete **QBluetoothServiceInfo**  object contains a
        **ProtocolDescriptorList**  attribute.
        """
        ...
    def isRegistered(self) -> bool:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#isRegistered

        **bool QBluetoothServiceInfo::isRegistered() const**

        Returns true if the service information is registered with the
        platform's Service Discovery Protocol (SDP) implementation, otherwise
        returns false.
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#isValid

        **bool QBluetoothServiceInfo::isValid() const**

        Returns true if the **QBluetoothServiceInfo**  object is valid,
        otherwise returns false.

        An invalid **QBluetoothServiceInfo**  object will have no attributes.
        """
        ...
    def protocolDescriptor(
        self, protocol: PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid
    ) -> PySide6.QtBluetooth.QBluetoothServiceInfo.Sequence:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#protocolDescriptor

        **QBluetoothServiceInfo::Sequence
        QBluetoothServiceInfo::protocolDescriptor(QBluetoothUuid::ProtocolUuid
        protocol ) const**

        Returns the protocol parameters as a **QBluetoothServiceInfo::Sequence**
        for protocol **protocol**.

        An empty **QBluetoothServiceInfo::Sequence**  is returned if
        **protocol** is not supported.
        """
        ...
    def protocolServiceMultiplexer(self) -> int:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#protocolServiceMultipl
        exer

        **int QBluetoothServiceInfo::protocolServiceMultiplexer() const**

        This is a convenience function. Returns the protocol/service multiplexer
        for services which support the L2CAP protocol, otherwise returns -1.

        This function is equivalent to extracting the information from
        **QBluetoothServiceInfo::Sequence**  returned by
        **QBluetoothServiceInfo::attribute**
        (**QBluetoothServiceInfo::ProtocolDescriptorList** ).
        """
        ...
    def registerService(
        self, localAdapter: PySide6.QtBluetooth.QBluetoothAddress = ...
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#registerService

        **bool QBluetoothServiceInfo::registerService(const QBluetoothAddress &
        localAdapter = QBluetoothAddress())**

        Registers this service with the platform's Service Discovery Protocol
        (SDP) implementation, making it findable by other devices when they
        perform service discovery. Returns true if the service is successfully
        registered, otherwise returns false. Once registered changes to the
        record cannot be made. The service must be unregistered and registered
        again with the changes.

        The **localAdapter** parameter determines the local Bluetooth adapter
        under which the service should be registered. If **localAdapter** is
        `null` the default Bluetooth adapter will be used. If this service info
        object is already registered via a local adapter and this is function is
        called using a different local adapter, the previous registration is
        removed and the service reregistered using the new adapter.
        """
        ...
    def removeAttribute(self, attributeId: int) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#removeAttribute

        **void QBluetoothServiceInfo::removeAttribute(quint16 attributeId )**

        Removes the attribute **attributeId** from the **QBluetoothServiceInfo**
        object.

        If the service information is already registered with the platforms SDP
        database, the database entry will not be updated until
        **registerService** () was called again.
        """
        ...
    def serverChannel(self) -> int:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serverChannel

        **int QBluetoothServiceInfo::serverChannel() const**

        This is a convenience function. Returns the server channel for services
        which support the RFCOMM protocol, otherwise returns -1.

        This function is equivalent to extracting the information from
        **QBluetoothServiceInfo::Sequence**  returned by
        **QBluetoothServiceInfo::attribute**
        (QBluetootherServiceInfo::ProtocolDescriptorList).
        """
        ...
    def serviceAvailability(self) -> int:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serviceAvailability

        **quint8 QBluetoothServiceInfo::serviceAvailability() const**

        This is a convenience function. It is equivalent to calling
        attribute(**QBluetoothServiceInfo::ServiceAvailability** ).toUInt().

        Returns the availability of the service.

        **See also** **setServiceAvailability** () and **attribute** ().
        """
        ...
    def serviceClassUuids(self) -> list[PySide6.QtBluetooth.QBluetoothUuid]:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serviceClassUuids

        **QList<QBluetoothUuid> QBluetoothServiceInfo::serviceClassUuids()
        const**

        Returns a list of UUIDs describing the service classes that this service
        conforms to.

        This is a convenience function. It is equivalent to calling
        attribute(**QBluetoothServiceInfo::ServiceClassIds**
        ).value<**QBluetoothServiceInfo::Sequence** >() and subsequently
        iterating over its **QBluetoothUuid**  entries.

        **See also** **attribute** ().
        """
        ...
    def serviceDescription(self) -> str:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serviceDescription

        **QString QBluetoothServiceInfo::serviceDescription() const**

        This is a convenience function. It is equivalent to calling
        attribute(**QBluetoothServiceInfo::ServiceDescription** ).toString().

        Returns the service description in the primary language.

        **See also** **setServiceDescription** () and **attribute** ().
        """
        ...
    def serviceName(self) -> str:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serviceName

        **QString QBluetoothServiceInfo::serviceName() const**

        This is a convenience function. It is equivalent to calling
        attribute(**QBluetoothServiceInfo::ServiceName** ).toString().

        Returns the service name in the primary language.

        **See also** **setServiceName** () and **attribute** ().
        """
        ...
    def serviceProvider(self) -> str:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serviceProvider

        **QString QBluetoothServiceInfo::serviceProvider() const**

        This is a convenience function. It is equivalent to calling
        attribute(**QBluetoothServiceInfo::ServiceProvider** ).toString().

        Returns the service provider in the primary language.

        **See also** **setServiceProvider** () and **attribute** ().
        """
        ...
    def serviceUuid(self) -> PySide6.QtBluetooth.QBluetoothUuid:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serviceUuid

        **QBluetoothUuid QBluetoothServiceInfo::serviceUuid() const**

        This is a convenience function. It is equivalent to calling
        attribute(**QBluetoothServiceInfo::ServiceId**
        ).value<**QBluetoothUuid** >().

        Returns the custom UUID of the service. This UUID may be null. UUIDs
        based on **Bluetooth SIG standards**  should be retrieved via
        **serviceClassUuids** ().

        **See also** **setServiceUuid** () and **attribute** ().
        """
        ...
    @overload
    def setAttribute(self, attributeId: int, value: Any) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setAttribute

        **void QBluetoothServiceInfo::setAttribute(quint16 attributeId , const
        QVariant & value )**

        Sets the attribute identified by **attributeId** to **value**.

        If the service information is already registered with the platform's SDP
        database, the database entry will not be updated until
        **registerService** () was called again.

        **Note:** If an attribute expectes a byte-encoded value (e.g. Bluetooth
        HID services), it should be set as **QByteArray** .

        **See also** **attribute** (), **isRegistered** (), and
        **registerService** ().
        """
        ...
    @overload
    def setAttribute(
        self,
        attributeId: int,
        value: (PySide6.QtBluetooth.QBluetoothServiceInfo.Alternative | Sequence[Any]),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setAttribute-1

        **void QBluetoothServiceInfo::setAttribute(quint16 attributeId , const
        QBluetoothUuid & value )**

        This is a convenience function.

        Sets the attribute identified by **attributeId** to **value**.

        If the service information is already registered with the platform's SDP
        database, the database entry will not be updated until
        **registerService** () was called again.
        """
        ...
    @overload
    def setAttribute(
        self,
        attributeId: int,
        value: PySide6.QtBluetooth.QBluetoothServiceInfo.Sequence | Sequence[Any],
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setAttribute-2

        **void QBluetoothServiceInfo::setAttribute(quint16 attributeId , const
        QBluetoothServiceInfo::Sequence & value )**

        This is a convenience function.

        Sets the attribute identified by **attributeId** to **value**.

        If the service information is already registered with the platform's SDP
        database, the database entry will not be updated until
        **registerService** () was called again.
        """
        ...
    @overload
    def setAttribute(
        self,
        attributeId: int,
        value: (
            PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType
            | PySide6.QtBluetooth.QBluetoothUuid.DescriptorType
            | PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid
            | PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid
            | PySide6.QtCore.QUuid
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setAttribute-3

        **void QBluetoothServiceInfo::setAttribute(quint16 attributeId , const
        QBluetoothServiceInfo::Alternative & value )**

        This is a convenience function.

        Sets the attribute identified by **attributeId** to **value**.

        If the service information is already registered with the platform's SDP
        database, the database entry will not be updated until
        **registerService** () was called again.
        """
        ...
    def setDevice(self, info: PySide6.QtBluetooth.QBluetoothDeviceInfo) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setDevice

        **void QBluetoothServiceInfo::setDevice(const QBluetoothDeviceInfo &
        device )**

        Sets the Bluetooth device that provides this service to **device**.

        **See also** **device** ().
        """
        ...
    def setServiceAvailability(self, availability: int) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setServiceAvailability

        **void QBluetoothServiceInfo::setServiceAvailability(quint8 availability
        )**

        This is a convenience function. It is equivalent to calling
        **setAttribute** (**QBluetoothServiceInfo::ServiceAvailability** ,
        availability).

        Sets the availabiltiy of the service to **availability**.

        **See also** **serviceAvailability** () and **setAttribute** ().
        """
        ...
    def setServiceDescription(self, description: str) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setServiceDescription

        **void QBluetoothServiceInfo::setServiceDescription(const QString &
        description )**

        This is a convenience function. It is equivalent to calling
        **setAttribute** (**QBluetoothServiceInfo::ServiceDescription** ,
        description).

        Sets the service description in the primary language to **description**.

        **See also** **serviceDescription** () and **setAttribute** ().
        """
        ...
    def setServiceName(self, name: str) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setServiceName

        **void QBluetoothServiceInfo::setServiceName(const QString & name )**

        This is a convenience function. It is equivalent to calling
        **setAttribute** (**QBluetoothServiceInfo::ServiceName** , name).

        Sets the service name in the primary language to **name**.

        **See also** **serviceName** () and **setAttribute** ().
        """
        ...
    def setServiceProvider(self, provider: str) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setServiceProvider

        **void QBluetoothServiceInfo::setServiceProvider(const QString &
        provider )**

        This is a convenience function. It is equivalent to calling
        **setAttribute** (**QBluetoothServiceInfo::ServiceProvider** ,
        provider).

        Sets the service provider in the primary language to **provider**.

        **See also** **serviceProvider** () and **setAttribute** ().
        """
        ...
    def setServiceUuid(
        self,
        uuid: (
            PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType
            | PySide6.QtBluetooth.QBluetoothUuid.DescriptorType
            | PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid
            | PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid
            | PySide6.QtCore.QUuid
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setServiceUuid

        **void QBluetoothServiceInfo::setServiceUuid(const QBluetoothUuid & uuid
        )**

        This is a convenience function. It is equivalent to calling
        **setAttribute** (**QBluetoothServiceInfo::ServiceId** , uuid).

        Sets the custom service UUID to **uuid**. This function should not be
        used to set a standardized service UUID.

        **See also** **serviceUuid** () and **setAttribute** ().
        """
        ...
    def socketProtocol(self) -> PySide6.QtBluetooth.QBluetoothServiceInfo.Protocol:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#socketProtocol

        **QBluetoothServiceInfo::Protocol
        QBluetoothServiceInfo::socketProtocol() const**

        Returns the protocol that the **QBluetoothServiceInfo**  object uses.
        """
        ...
    def unregisterService(self) -> bool:
        """
        https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#unregisterService

        **bool QBluetoothServiceInfo::unregisterService()**

        Unregisters this service with the platform's Service Discovery Protocol
        (SDP) implementation. After this, the service will no longer be findable
        by other devices through service discovery.

        Returns true if the service is successfully unregistered, otherwise
        returns false.
        """
        ...
