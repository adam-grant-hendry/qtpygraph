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

class QBluetoothServer(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qbluetoothserver.html

    **Detailed Description**

    QBluetoothServer is used to implement Bluetooth services over RFCOMM or
    L2cap.

    Start listening for incoming connections with **listen** (). Wait till the
    **newConnection** () signal is emitted when a new connection is established,
    and call **nextPendingConnection** () to get a **QBluetoothSocket**  for the
    new connection.

    To enable other devices to find your service, create a
    **QBluetoothServiceInfo**  with the applicable attributes for your service
    and register it using **QBluetoothServiceInfo::registerService** (). Call
    **serverPort** () to get the channel number that is being used.

    If the **QBluetoothServiceInfo::Protocol**  is not supported by a platform,
    **listen** () will return `false`. Android and WinRT only support RFCOMM for
    example.

    On iOS, this class cannot be used because the platform does not expose an
    API which may permit access to QBluetoothServer related features.

    **See also** **QBluetoothServiceInfo**  and **QBluetoothSocket** .
    """

    NoError: QBluetoothServer.Error = ...
    UnknownError: QBluetoothServer.Error = ...
    PoweredOffError: QBluetoothServer.Error = ...
    InputOutputError: QBluetoothServer.Error = ...
    ServiceAlreadyRegisteredError: QBluetoothServer.Error = ...
    UnsupportedProtocolError: QBluetoothServer.Error = ...

    class Error(IntFlag):
        NoError: QBluetoothServer.Error = ...
        UnknownError: QBluetoothServer.Error = ...
        PoweredOffError: QBluetoothServer.Error = ...
        InputOutputError: QBluetoothServer.Error = ...
        ServiceAlreadyRegisteredError: QBluetoothServer.Error = ...
        UnsupportedProtocolError: QBluetoothServer.Error = ...
    def __init__(
        self,
        serverType: PySide6.QtBluetooth.QBluetoothServiceInfo.Protocol,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#QBluetoothServer

        **QBluetoothServer::QBluetoothServer(QBluetoothServiceInfo::Protocol
        serverType , QObject * parent = nullptr)**

        Constructs a bluetooth server with **parent** and **serverType**.
        """
        ...
    def close(self) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#close

        **void QBluetoothServer::close()**

        Closes and resets the listening socket. Any already established
        **QBluetoothSocket**  continues to operate and must be separately
        **closed** .
        """
        ...
    def error(self) -> PySide6.QtBluetooth.QBluetoothServer.Error:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#error

        **QBluetoothServer::Error QBluetoothServer::error() const**

        Returns the last error of the **QBluetoothServer** .
        """
        ...
    def hasPendingConnections(self) -> bool:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#hasPendingConnections

        **bool QBluetoothServer::hasPendingConnections() const**

        Returns true if a connection is pending, otherwise false.
        """
        ...
    def isListening(self) -> bool:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#isListening

        **bool QBluetoothServer::isListening() const**

        Returns true if the server is listening for incoming connections,
        otherwise false.
        """
        ...
    @overload
    def listen(
        self, address: PySide6.QtBluetooth.QBluetoothAddress = ..., port: int = ...
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#listen

        **bool QBluetoothServer::listen(const QBluetoothAddress & address =
        QBluetoothAddress(), quint16 port = 0)**

        Start listening for incoming connections to **address** on **port**.
        **address** must be a local Bluetooth adapter address and **port** must
        be larger than zero and not be taken already by another Bluetooth server
        object. It is recommended to avoid setting a port number to enable the
        system to automatically choose a port.

        Returns `true` if the operation succeeded and the server is listening
        for incoming connections, otherwise returns `false`.

        If the server object is already listening for incoming connections this
        function always returns `false`. **close** () should be called before
        calling this function.

        **See also** **isListening** () and **newConnection** ().
        """
        ...
    @overload
    def listen(
        self,
        uuid: (
            PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType
            | PySide6.QtBluetooth.QBluetoothUuid.DescriptorType
            | PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid
            | PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid
            | PySide6.QtCore.QUuid
        ),
        serviceName: str = ...,
    ) -> PySide6.QtBluetooth.QBluetoothServiceInfo:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#listen-1

        **QBluetoothServiceInfo QBluetoothServer::listen(const QBluetoothUuid &
        uuid , const QString & serviceName = QString())**

        Convenience function for registering an SPP service with **uuid** and
        **serviceName**. Because this function already registers the service,
        the **QBluetoothServiceInfo**  object which is returned can not be
        changed any more. To shutdown the server later on it is required to call
        **QBluetoothServiceInfo::unregisterService** () and **close** () on this
        server object.

        Returns a registered **QBluetoothServiceInfo**  instance if successful
        otherwise an invalid **QBluetoothServiceInfo** . This function always
        assumes that the default Bluetooth adapter should be used.

        If the server object is already listening for incoming connections this
        function returns an invalid **QBluetoothServiceInfo** .

        For an RFCOMM server this function is equivalent to following code
        snippet.

        **QBluetoothServiceInfo**  serviceInfo;
        serviceInfo.setAttribute(**QBluetoothServiceInfo** ::ServiceName,
        serviceName);
                **QBluetoothServiceInfo** ::Sequence
        browseSequence;
                browseSequence << **QVariant**
        ::fromValue(**QBluetoothUuid** (**QBluetoothUuid**
        ::ServiceClassUuid::PublicBrowseGroup));
        serviceInfo.setAttribute(**QBluetoothServiceInfo** ::BrowseGroupList,
        browseSequence);

                **QBluetoothServiceInfo** ::Sequence
        profileSequence;
                **QBluetoothServiceInfo** ::Sequence classId;
        classId << **QVariant** ::fromValue(**QBluetoothUuid**
        (**QBluetoothUuid** ::ServiceClassUuid::SerialPort));
                classId <<
        **QVariant** ::fromValue(**quint16** (0x100));
        profileSequence.append(**QVariant** ::fromValue(classId));
        serviceInfo.setAttribute(**QBluetoothServiceInfo**
        ::BluetoothProfileDescriptorList,
        profileSequence);

                classId.clear();
                //Android
        requires custom uuid to be set as service class
                classId <<
        **QVariant** ::fromValue(uuid);
                classId << **QVariant**
        ::fromValue(**QBluetoothUuid** (**QBluetoothUuid**
        ::ServiceClassUuid::SerialPort));
        serviceInfo.setAttribute(**QBluetoothServiceInfo** ::ServiceClassIds,
        classId);
                serviceInfo.setServiceUuid(uuid);
        **QBluetoothServiceInfo** ::Sequence protocolDescriptorList;
        **QBluetoothServiceInfo** ::Sequence protocol;
                protocol <<
        **QVariant** ::fromValue(**QBluetoothUuid** (**QBluetoothUuid**
        ::ProtocolUuid::L2cap));
                if (d->serverType ==
        **QBluetoothServiceInfo** ::L2capProtocol)
                    protocol <<
        **QVariant** ::fromValue(serverPort());
        protocolDescriptorList.append(**QVariant** ::fromValue(protocol));
        protocol.clear();
                protocol << **QVariant**
        ::fromValue(**QBluetoothUuid** (**QBluetoothUuid**
        ::ProtocolUuid::Rfcomm))
                         << **QVariant**
        ::fromValue(**quint8** (serverPort()));
        protocolDescriptorList.append(**QVariant** ::fromValue(protocol));
        serviceInfo.setAttribute(**QBluetoothServiceInfo**
        ::ProtocolDescriptorList,
        protocolDescriptorList);
                bool result =
        serviceInfo.registerService();

        **See also** **isListening** (), **newConnection** (), and **listen**
        ().
        """
        ...
    def maxPendingConnections(self) -> int:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#maxPendingConnections

        **int QBluetoothServer::maxPendingConnections() const**

        Returns the maximum number of pending connections.

        **See also** **setMaxPendingConnections** ().
        """
        ...
    def nextPendingConnection(self) -> PySide6.QtBluetooth.QBluetoothSocket:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#nextPendingConnection

        **QBluetoothSocket *QBluetoothServer::nextPendingConnection()**

        Returns a pointer to the **QBluetoothSocket**  for the next pending
        connection. It is the callers responsibility to delete the pointer.
        """
        ...
    def securityFlags(self) -> PySide6.QtBluetooth.QBluetooth.SecurityFlags:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#securityFlags

        **QBluetooth::SecurityFlags QBluetoothServer::securityFlags() const**

        Returns the Bluetooth security flags.

        **See also** **setSecurityFlags** ().
        """
        ...
    def serverAddress(self) -> PySide6.QtBluetooth.QBluetoothAddress:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#serverAddress

        **QBluetoothAddress QBluetoothServer::serverAddress() const**

        Returns the server address.
        """
        ...
    def serverPort(self) -> int:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#serverPort

        **quint16 QBluetoothServer::serverPort() const**

        Returns the server port number.
        """
        ...
    def serverType(self) -> PySide6.QtBluetooth.QBluetoothServiceInfo.Protocol:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#serverType

        **QBluetoothServiceInfo::Protocol QBluetoothServer::serverType() const**

        Returns the type of the **QBluetoothServer** .
        """
        ...
    def setMaxPendingConnections(self, numConnections: int) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#setMaxPendingConnections

        **void QBluetoothServer::setMaxPendingConnections(int numConnections )**

        Sets the maximum number of pending connections to **numConnections**. If
        the number of pending sockets exceeds this limit new sockets will be
        rejected.

        **See also** **maxPendingConnections** ().
        """
        ...
    def setSecurityFlags(
        self, security: PySide6.QtBluetooth.QBluetooth.SecurityFlags
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#setSecurityFlags

        **void QBluetoothServer::setSecurityFlags(QBluetooth::SecurityFlags
        security )**

        Sets the Bluetooth security flags to **security**. This function must be
        called before calling **listen** (). The Bluetooth link will always be
        encrypted when using Bluetooth 2.1 devices as encryption is mandatory.

        Android only supports two levels of security (secure and non-secure). If
        this flag is set to **QBluetooth::Security::NoSecurity**  the server
        object will not employ any authentication or encryption. Any other
        security flag combination will trigger a secure Bluetooth connection.

        On macOS, security flags are not supported and will be ignored.

        **See also** **securityFlags** ().
        """
        ...
    @property
    def errorOccurred(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#errorOccurred

        **[signal, since 6.2] void
        QBluetoothServer::errorOccurred(QBluetoothServer::Error error )**

        This signal is emitted when an **error** occurs.

        This function was introduced in Qt 6.2.

        **See also** **error** () and **QBluetoothServer::Error** .
        """
        ...
    @property
    def newConnection(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qbluetoothserver.html#newConnection

        **[signal] void QBluetoothServer::newConnection()**

        This signal is emitted when a new connection is available.

        The connected slot should call **nextPendingConnection** () to get a
        **QBluetoothSocket**  object to send and receive data over the
        connection.

        **See also** **nextPendingConnection** () and **hasPendingConnections**
        ().
        """
        ...
