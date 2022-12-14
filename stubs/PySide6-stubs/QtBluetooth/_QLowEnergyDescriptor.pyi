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

from typing import overload

import PySide6.QtBluetooth
import PySide6.QtCore

class QLowEnergyDescriptor:
    """
    https://doc.qt.io/qt-6/qlowenergydescriptor.html

    **Detailed Description**

    QLowEnergyDescriptor provides information about a Bluetooth Low Energy
    descriptor's **name** (), **uuid** (), and **value** (). Descriptors are
    encapsulated by Bluetooth Low Energy characteristics and provide additional
    contextual information about the characteristic (data format, notification
    activation and so on).

    The descriptor value may be written via the **QLowEnergyService**  instance
    that manages the service to which this descriptor belongs. The
    **QLowEnergyService::writeDescriptor** () function writes the new value. The
    **QLowEnergyService::descriptorWritten** () signal is emitted upon success.
    The cached **value** () of this object is updated accordingly.

    **See also** **QLowEnergyService**  and **QLowEnergyCharacteristic** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergydescriptor.html#QLowEnergyDescriptor

        **QLowEnergyDescriptor::QLowEnergyDescriptor()**

        Construct a new QLowEnergyDescriptor. A default-constructed instance of
        this class is always invalid.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtBluetooth.QLowEnergyDescriptor) -> None:
        """
        https://doc.qt.io/qt-6/qlowenergydescriptor.html#QLowEnergyDescriptor-1

        **QLowEnergyDescriptor::QLowEnergyDescriptor(const QLowEnergyDescriptor
        & other )**

        Construct a new QLowEnergyDescriptor that is a copy of **other**.

        The two copies continue to share the same underlying data which does not
        detach upon write.
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qlowenergydescriptor.html#isValid

        **bool QLowEnergyDescriptor::isValid() const**

        Returns `true` if the **QLowEnergyDescriptor**  object is valid,
        otherwise returns `false`.

        An invalid descriptor instance is not associated with any service
        (default-constructed) or the associated service is no longer valid due
        to a disconnect from the underlying Bluetooth Low Energy device, for
        example. Once the object is invalid it cannot become valid anymore.

        **Note:** If a **QLowEnergyDescriptor**  instance turns invalid due to a
        disconnect from the underlying device, the information encapsulated by
        the current instance remains as it was at the time of the disconnect.
        Therefore it can be retrieved after the disconnect event.
        """
        ...
    def name(self) -> str:
        """
        https://doc.qt.io/qt-6/qlowenergydescriptor.html#name

        **QString QLowEnergyDescriptor::name() const**

        Returns the human-readable name of the descriptor.

        The name is based on the descriptor's **type** (). The complete list of
        descriptor types can be found under **Bluetooth.org Descriptors** .

        The returned string is empty if the **type** () is unknown.

        **See also** **type** () and **QBluetoothUuid::descriptorToString** ().
        """
        ...
    def type(self) -> PySide6.QtBluetooth.QBluetoothUuid.DescriptorType:
        """
        https://doc.qt.io/qt-6/qlowenergydescriptor.html#type

        **QBluetoothUuid::DescriptorType QLowEnergyDescriptor::type() const**

        Returns the type of the descriptor.

        **See also** **name** ().
        """
        ...
    def uuid(self) -> PySide6.QtBluetooth.QBluetoothUuid:
        """
        https://doc.qt.io/qt-6/qlowenergydescriptor.html#uuid

        **QBluetoothUuid QLowEnergyDescriptor::uuid() const**

        Returns the UUID of this descriptor if **isValid** () returns `true`;
        otherwise a **null**  UUID.
        """
        ...
    def value(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qlowenergydescriptor.html#value

        **QByteArray QLowEnergyDescriptor::value() const**

        Returns the cached value of the descriptor.

        The cached descriptor value may be updated using
        **QLowEnergyService::writeDescriptor** () or
        **QLowEnergyService::readDescriptor** ().
        """
        ...
