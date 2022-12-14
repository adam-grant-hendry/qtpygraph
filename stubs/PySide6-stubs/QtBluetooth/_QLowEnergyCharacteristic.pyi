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

from enum import IntFlag
from typing import overload

import PySide6.QtBluetooth
import PySide6.QtCore

class QLowEnergyCharacteristic:
    """
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html

    **Detailed Description**

    QLowEnergyCharacteristic provides information about a Bluetooth Low Energy
    service characteristic's **name** (), **uuid** (), **value** (),
    **properties** (), and **descriptors** (). To obtain the characteristic's
    specification and information, it is necessary to connect to the device
    using the **QLowEnergyService**  and **QLowEnergyController**  classes.

    The characteristic value may be written via the **QLowEnergyService**
    instance that manages the service to which this characteristic belongs. The
    **QLowEnergyService::writeCharacteristic** () function writes the new value.
    The **QLowEnergyService::characteristicWritten** () signal is emitted upon
    success. The **value** () of this object is automatically updated
    accordingly.

    Characteristics may contain none, one or more descriptors. They can be
    individually retrieved using the **descriptor** () function. The
    **descriptors** () function returns all descriptors as a list. The general
    purpose of a descriptor is to add contextual information to the
    characteristic. For example, the descriptor might provide format or range
    information specifying how the characteristic's value is to be interpreted.

    **See also** **QLowEnergyService**  and **QLowEnergyDescriptor** .
    """

    Unknown: QLowEnergyCharacteristic.PropertyType = ...
    Broadcasting: QLowEnergyCharacteristic.PropertyType = ...
    Read: QLowEnergyCharacteristic.PropertyType = ...
    WriteNoResponse: QLowEnergyCharacteristic.PropertyType = ...
    Write: QLowEnergyCharacteristic.PropertyType = ...
    Notify: QLowEnergyCharacteristic.PropertyType = ...
    Indicate: QLowEnergyCharacteristic.PropertyType = ...
    WriteSigned: QLowEnergyCharacteristic.PropertyType = ...
    ExtendedProperty: QLowEnergyCharacteristic.PropertyType = ...

    class PropertyType(IntFlag):
        Unknown: QLowEnergyCharacteristic.PropertyType = ...
        Broadcasting: QLowEnergyCharacteristic.PropertyType = ...
        Read: QLowEnergyCharacteristic.PropertyType = ...
        WriteNoResponse: QLowEnergyCharacteristic.PropertyType = ...
        Write: QLowEnergyCharacteristic.PropertyType = ...
        Notify: QLowEnergyCharacteristic.PropertyType = ...
        Indicate: QLowEnergyCharacteristic.PropertyType = ...
        WriteSigned: QLowEnergyCharacteristic.PropertyType = ...
        ExtendedProperty: QLowEnergyCharacteristic.PropertyType = ...

    class PropertyTypes: ...

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergycharacteristic.html#QLowEnergyCharacter
        istic

        **QLowEnergyCharacteristic::QLowEnergyCharacteristic()**

        Construct a new QLowEnergyCharacteristic. A default-constructed instance
        of this class is always invalid.

        **See also** **isValid** ().
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QLowEnergyCharacteristic) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergycharacteristic.html#QLowEnergyCharacter
        istic-1

        **QLowEnergyCharacteristic::QLowEnergyCharacteristic(const
        QLowEnergyCharacteristic & other )**

        Construct a new QLowEnergyCharacteristic that is a copy of **other**.

        The two copies continue to share the same underlying data which does not
        detach upon write.
        """
        ...
    def clientCharacteristicConfiguration(
        self,
    ) -> PySide6.QtBluetooth.QLowEnergyDescriptor:
        """
        https://doc.qt.io/qt-6/qlowenergycharacteristic.html#clientCharacteristi
        cConfiguration

        **[since 6.2] QLowEnergyDescriptor
        QLowEnergyCharacteristic::clientCharacteristicConfiguration() const**

        Returns the Client Characteristic Configuration Descriptor or an invalid
        **QLowEnergyDescriptor**  instance if no Client Characteristic
        Configuration Descriptor exists.

        BTLE characteristics can support notifications and/or indications. In
        both cases, the peripheral will inform the central on each change of the
        characteristic's value. In the BTLE attribute protocol, notification
        messages are not confirmed by the central, while indications are
        confirmed. Notifications are considered faster, but unreliable, while
        indications are slower and more reliable.

        If a characteristic supports notification or indication, these can be
        enabled by writing special bit patterns to the Client Characteristic
        Configuration Descriptor. For convenience, these bit patterns are
        provided as **QLowEnergyCharacteristic::CCCDDisable** ,
        **QLowEnergyCharacteristic::CCCDEnableNotification** , and
        **QLowEnergyCharacteristic::CCCDEnableIndication** .

        Enabling e.g. notification for a characteristic named `mycharacteristic`
        in a service called `myservice` could be done using the following code.

        auto cccd = mycharacteristic.clientCharacteristicConfiguration();
            if
        (!cccd.isValid()) {
                // your error handling
                return error;
        }
            myservice->writeDescriptor(cccd, **QLowEnergyCharacteristic**
        ::CCCDEnableNotification);

        **Note:** Calling `characteristic.clientCharacteristicConfiguration()`
        is equivalent to calling `characteristic.descriptor(QBluetoothUuid::Desc
        riptorType::ClientCharacteristicConfiguration)`.

        **Note:** It is not recommended to use both notifications and
        indications on the same characteristic. This applies to both server-side
        when setting up the characteristics, as well as client-side when
        enabling them. The bluetooth stack behavior differs from platform to
        platform and the cross-platform behavior will likely be inconsistent. As
        an example a Bluez Linux client might unconditionally try to enable both
        mechanisms if both are supported, whereas a macOS client might
        unconditionally enable just the notifications. If both are needed
        consider creating two separate characteristics.

        This function was introduced in Qt 6.2.

        **See also** **descriptor** ().
        """
        ...
    def descriptor(
        self,
        uuid: (
            PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType
            | PySide6.QtBluetooth.QBluetoothUuid.DescriptorType
            | PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid
            | PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid
            | PySide6.QtCore.QUuid
        ),
    ) -> PySide6.QtBluetooth.QLowEnergyDescriptor:
        """
        https://doc.qt.io/qt-6/qlowenergycharacteristic.html#descriptor

        **QLowEnergyDescriptor QLowEnergyCharacteristic::descriptor(const
        QBluetoothUuid & uuid ) const**

        Returns the descriptor for **uuid** or an invalid
        **QLowEnergyDescriptor**  instance.

        **See also** **descriptors** ().
        """
        ...
    def descriptors(self) -> list[PySide6.QtBluetooth.QLowEnergyDescriptor]:
        """
        https://doc.qt.io/qt-6/qlowenergycharacteristic.html#descriptors

        **QList<QLowEnergyDescriptor> QLowEnergyCharacteristic::descriptors()
        const**

        Returns the list of descriptors belonging to this characteristic;
        otherwise an empty list.

        **See also** **descriptor** ().
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qlowenergycharacteristic.html#isValid

        **bool QLowEnergyCharacteristic::isValid() const**

        Returns `true` if the **QLowEnergyCharacteristic**  object is valid,
        otherwise returns `false`.

        An invalid characteristic object is not associated with any service
        (default-constructed) or the associated service is no longer valid due
        to a disconnect from the underlying Bluetooth Low Energy device, for
        example. Once the object is invalid it cannot become valid anymore.

        **Note:** If a **QLowEnergyCharacteristic**  instance turns invalid due
        to a disconnect from the underlying device, the information encapsulated
        by the current instance remains as it was at the time of the disconnect.
        Therefore it can be retrieved after the disconnect event.
        """
        ...
    def name(self) -> str:
        """
        https://doc.qt.io/qt-6/qlowenergycharacteristic.html#name

        **QString QLowEnergyCharacteristic::name() const**

        Returns the human-readable name of the characteristic.

        The name is based on the characteristic's **uuid** () which must have
        been standardized. The complete list of characteristic types can be
        found under **Bluetooth.org Characteristics** .

        The returned string is empty if the **uuid** () is unknown.

        **See also** **QBluetoothUuid::characteristicToString** ().
        """
        ...
    def properties(self) -> PySide6.QtBluetooth.QLowEnergyCharacteristic.PropertyTypes:
        """
        https://doc.qt.io/qt-6/qlowenergycharacteristic.html#properties

        **QLowEnergyCharacteristic::PropertyTypes
        QLowEnergyCharacteristic::properties() const**

        Returns the properties of the characteristic.

        The properties define the access permissions for the characteristic.
        """
        ...
    def uuid(self) -> PySide6.QtBluetooth.QBluetoothUuid:
        """
        https://doc.qt.io/qt-6/qlowenergycharacteristic.html#uuid

        **QBluetoothUuid QLowEnergyCharacteristic::uuid() const**

        Returns the UUID of the characteristic if **isValid** () returns `true`;
        otherwise a **null**  UUID.
        """
        ...
    def value(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qlowenergycharacteristic.html#value

        **QByteArray QLowEnergyCharacteristic::value() const**

        Returns the cached value of the characteristic.

        If the characteristic's **properties** () permit writing of new values,
        the value can be updated using
        **QLowEnergyService::writeCharacteristic** ().

        The cache is updated during the associated service's **detail
        discovery** , a successful **read** /**write**  operation or when an
        update notification is received.

        The returned **QByteArray**  always remains empty if the characteristic
        does not have the **read permission** . In such cases only the
        **QLowEnergyService::characteristicChanged** () or
        **QLowEnergyService::characteristicWritten** () may provice information
        about the value of this characteristic.
        """
        ...
