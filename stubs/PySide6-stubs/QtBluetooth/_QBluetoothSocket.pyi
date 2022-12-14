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

class QBluetoothSocket(PySide6.QtCore.QIODevice):
    """
    https://doc.qt.io/qt-6/qbluetoothsocket.html

    **Detailed Description**

    QBluetoothSocket supports two socket types, **L2CAP**  and **RFCOMM** .

    **L2CAP**  is a low level datagram-oriented Bluetooth socket. Android does
    not support **L2CAP**  for socket connections.

    **RFCOMM**  is a reliable, stream-oriented socket. RFCOMM sockets emulate an
    RS-232 serial port.

    To create a connection to a Bluetooth service, create a socket of the
    appropriate type and call **connectToService** () passing the Bluetooth
    address and port number. QBluetoothSocket will emit the **connected** ()
    signal when the connection is established.

    If the **Protocol**  is not supported on a platform, calling
    **connectToService** () will emit a **UnsupportedProtocolError**  error.

    **Note:** QBluetoothSocket does not support synchronous read and write
    operations. Functions such as **waitForReadyRead** () and
    **waitForBytesWritten** () are not implemented. I/O operations should be
    performed using **readyRead** (), **read** () and **write** ().

    On iOS, this class cannot be used because the platform does not expose an
    API which may permit access to QBluetoothSocket related features.
    """

    class SocketError(IntFlag):
        NoSocketError: QBluetoothSocket.SocketError = ...
        UnknownSocketError: QBluetoothSocket.SocketError = ...
        RemoteHostClosedError: QBluetoothSocket.SocketError = ...
        HostNotFoundError: QBluetoothSocket.SocketError = ...
        ServiceNotFoundError: QBluetoothSocket.SocketError = ...
        NetworkError: QBluetoothSocket.SocketError = ...
        UnsupportedProtocolError: QBluetoothSocket.SocketError = ...
        OperationError: QBluetoothSocket.SocketError = ...

    class SocketState(IntFlag):
        UnconnectedState: QBluetoothSocket.SocketState = ...
        ServiceLookupState: QBluetoothSocket.SocketState = ...
        ConnectingState: QBluetoothSocket.SocketState = ...
        ConnectedState: QBluetoothSocket.SocketState = ...
        BoundState: QBluetoothSocket.SocketState = ...
        ClosingState: QBluetoothSocket.SocketState = ...
        ListeningState: QBluetoothSocket.SocketState = ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#QBluetoothSocket

        **QBluetoothSocket::QBluetoothSocket(QBluetoothServiceInfo::Protocol
        socketType , QObject * parent = nullptr)**

        Constructs a Bluetooth socket of **socketType** type, with **parent**.
        """
        ...
    @overload
    def __init__(
        self,
        socketType: PySide6.QtBluetooth.QBluetoothServiceInfo.Protocol,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#QBluetoothSocket-1

        **QBluetoothSocket::QBluetoothSocket(QObject * parent = nullptr)**

        Constructs a Bluetooth socket with **parent**.
        """
        ...
    def abort(self) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#abort

        **void QBluetoothSocket::abort()**

        Aborts the current connection and resets the socket. Unlike
        **disconnectFromService** (), this function immediately closes the
        socket, discarding any pending data in the write buffer.

        **Note:** On Android, aborting the socket requires asynchronous
        interaction with Android threads. Therefore the associated
        **disconnected** () and **stateChanged** () signals are delayed until
        the threads have finished the closure.

        **See also** **disconnectFromService** () and **close** ().
        """
        ...
    def bytesAvailable(self) -> int:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#bytesAvailable

        **[override virtual] qint64 QBluetoothSocket::bytesAvailable() const**

        Reimplements: **QIODevice::bytesAvailable() const** .

        Returns the number of incoming bytes that are waiting to be read.

        **See also** **bytesToWrite** () and **read** ().
        """
        ...
    def bytesToWrite(self) -> int:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#bytesToWrite

        **[override virtual] qint64 QBluetoothSocket::bytesToWrite() const**

        Reimplements: **QIODevice::bytesToWrite() const** .

        Returns the number of bytes that are waiting to be written. The bytes
        are written when control goes back to the event loop.
        """
        ...
    def canReadLine(self) -> bool:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#canReadLine

        **[override virtual] bool QBluetoothSocket::canReadLine() const**

        Reimplements: **QIODevice::canReadLine() const** .

        Returns true if you can read at least one line from the device
        """
        ...
    def close(self) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#close

        **[override virtual] void QBluetoothSocket::close()**

        Reimplements: **QIODevice::close** ().

        Disconnects the socket's connection with the device.

        **Note:** On Android, closing the socket requires asynchronous
        interaction with Android threads. Therefore the associated
        **disconnected** () and **stateChanged** () signals are delayed until
        the threads have finished the closure.
        """
        ...
    @overload
    def connectToService(
        self,
        address: PySide6.QtBluetooth.QBluetoothAddress,
        port: int,
        openMode: PySide6.QtCore.QIODeviceBase.OpenMode = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#connectToService

        **void QBluetoothSocket::connectToService(const QBluetoothServiceInfo &
        service , QIODeviceBase::OpenMode openMode = ReadWrite)**

        Attempts to connect to the service described by **service**.

        The socket is opened in the given **openMode**. The **socketType** () is
        ignored if **service** specifies a differing
        **QBluetoothServiceInfo::socketProtocol** ().

        The socket first enters **ConnectingState**  and attempts to connect to
        the device providing **service**. If a connection is established,
        **QBluetoothSocket**  enters **ConnectedState**  and emits **connected**
        ().

        At any point, the socket can emit **error** () to signal that an error
        occurred.

        Note that most platforms require a pairing prior to connecting to the
        remote device. Otherwise the connection process may fail.

        On Android, only RFCOMM connections are possible. This function ignores
        any socket protocol indicator and assumes RFCOMM.

        **See also** **state** () and **disconnectFromService** ().
        """
        ...
    @overload
    def connectToService(
        self,
        address: PySide6.QtBluetooth.QBluetoothAddress,
        uuid: PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid,
        mode: PySide6.QtCore.QIODeviceBase.OpenMode = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#connectToService-1

        **void QBluetoothSocket::connectToService(const QBluetoothAddress &
        address , const QBluetoothUuid & uuid , QIODeviceBase::OpenMode openMode
        = ReadWrite)**

        Attempts to make a connection to the service identified by **uuid** on
        the device with address **address**.

        The socket is opened in the given **openMode**.

        For BlueZ, the socket first enters the **ServiceLookupState**  and
        queries the connection parameters for **uuid**. If the service
        parameters are successfully retrieved the socket enters
        **ConnectingState** , and attempts to connect to **address**. If a
        connection is established, **QBluetoothSocket**  enters
        **ConnectedState**  and emits **connected** ().

        On Android, the service connection can directly be established using the
        UUID of the remote service. Therefore the platform does not require the
        **ServiceLookupState**  and **socketType** () is always set to
        **QBluetoothServiceInfo::RfcommProtocol** .

        At any point, the socket can emit **error** () to signal that an error
        occurred.

        Note that most platforms require a pairing prior to connecting to the
        remote device. Otherwise the connection process may fail.

        **See also** **state** () and **disconnectFromService** ().
        """
        ...
    @overload
    def connectToService(
        self,
        address: PySide6.QtBluetooth.QBluetoothAddress,
        uuid: (
            PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType
            | PySide6.QtBluetooth.QBluetoothUuid.DescriptorType
            | PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid
            | PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid
            | PySide6.QtCore.QUuid
        ),
        openMode: PySide6.QtCore.QIODeviceBase.OpenMode = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#connectToService-2

        **void QBluetoothSocket::connectToService(const QBluetoothAddress &
        address , quint16 port , QIODeviceBase::OpenMode openMode = ReadWrite)**

        Attempts to make a connection with **address** on the given **port**.

        The socket is opened in the given **openMode**.

        The socket first enters **ConnectingState** , and attempts to connect to
        **address**. If a connection is established, **QBluetoothSocket**
        enters **ConnectedState**  and emits **connected** ().

        At any point, the socket can emit **error** () to signal that an error
        occurred.

        On Android and BlueZ (version 5.46 or above), a connection to a service
        can not be established using a port. Calling this function will emit a
        **ServiceNotFoundError** .

        Note that most platforms require a pairing prior to connecting to the
        remote device. Otherwise the connection process may fail.

        **See also** **state** () and **disconnectFromService** ().
        """
        ...
    @overload
    def connectToService(
        self,
        service: PySide6.QtBluetooth.QBluetoothServiceInfo,
        openMode: PySide6.QtCore.QIODeviceBase.OpenMode = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#connectToService

        **void QBluetoothSocket::connectToService(const QBluetoothServiceInfo &
        service , QIODeviceBase::OpenMode openMode = ReadWrite)**

        Attempts to connect to the service described by **service**.

        The socket is opened in the given **openMode**. The **socketType** () is
        ignored if **service** specifies a differing
        **QBluetoothServiceInfo::socketProtocol** ().

        The socket first enters **ConnectingState**  and attempts to connect to
        the device providing **service**. If a connection is established,
        **QBluetoothSocket**  enters **ConnectedState**  and emits **connected**
        ().

        At any point, the socket can emit **error** () to signal that an error
        occurred.

        Note that most platforms require a pairing prior to connecting to the
        remote device. Otherwise the connection process may fail.

        On Android, only RFCOMM connections are possible. This function ignores
        any socket protocol indicator and assumes RFCOMM.

        **See also** **state** () and **disconnectFromService** ().
        """
        ...
    def disconnectFromService(self) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#disconnectFromService

        **void QBluetoothSocket::disconnectFromService()**

        Attempts to close the socket. If there is pending data waiting to be
        written **QBluetoothSocket**  will enter **ClosingState**  and wait
        until all data has been written. Eventually, it will enter
        **UnconnectedState**  and emit the **disconnected** () signal.

        **See also** **connectToService** ().
        """
        ...
    def doDeviceDiscovery(
        self,
        service: PySide6.QtBluetooth.QBluetoothServiceInfo,
        openMode: PySide6.QtCore.QIODeviceBase.OpenMode,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#doDeviceDiscovery

        **[protected] void QBluetoothSocket::doDeviceDiscovery(const
        QBluetoothServiceInfo & service , QIODeviceBase::OpenMode openMode )**

        Start device discovery for **service** and open the socket with
        **openMode**. If the socket is created with a service uuid device
        address, use service discovery to find the port number to connect to.
        """
        ...
    def error(self) -> PySide6.QtBluetooth.QBluetoothSocket.SocketError:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#error

        **QBluetoothSocket::SocketError QBluetoothSocket::error() const**

        Returns the last error.
        """
        ...
    def errorString(self) -> str:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#errorString

        **QString QBluetoothSocket::errorString() const**

        Returns a user displayable text string for the error.
        """
        ...
    def isSequential(self) -> bool:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#isSequential

        **[override virtual] bool QBluetoothSocket::isSequential() const**

        Reimplements: **QIODevice::isSequential() const** .
        """
        ...
    def localAddress(self) -> PySide6.QtBluetooth.QBluetoothAddress:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#localAddress

        **QBluetoothAddress QBluetoothSocket::localAddress() const**

        Returns the address of the local device.

        Although some platforms may differ the socket must generally be
        connected to guarantee the return of a valid address. In particular,
        this is true when dealing with platforms that support multiple local
        Bluetooth adapters.
        """
        ...
    def localName(self) -> str:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#localName

        **QString QBluetoothSocket::localName() const**

        Returns the name of the local device.

        Although some platforms may differ the socket must generally be
        connected to guarantee the return of a valid name. In particular, this
        is true when dealing with platforms that support multiple local
        Bluetooth adapters.
        """
        ...
    def localPort(self) -> int:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#localPort

        **quint16 QBluetoothSocket::localPort() const**

        Returns the port number of the local socket if available, otherwise
        returns 0. Although some platforms may differ the socket must generally
        be connected to guarantee the return of a valid port number.

        On Android and macOS, this feature is not supported and returns 0.
        """
        ...
    def peerAddress(self) -> PySide6.QtBluetooth.QBluetoothAddress:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#peerAddress

        **QBluetoothAddress QBluetoothSocket::peerAddress() const**

        Returns the address of the peer device.
        """
        ...
    def peerName(self) -> str:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#peerName

        **QString QBluetoothSocket::peerName() const**

        Returns the name of the peer device.
        """
        ...
    def peerPort(self) -> int:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#peerPort

        **quint16 QBluetoothSocket::peerPort() const**

        Return the port number of the peer socket if available, otherwise
        returns 0. On Android, this feature is not supported.
        """
        ...
    def preferredSecurityFlags(self) -> PySide6.QtBluetooth.QBluetooth.SecurityFlags:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#preferredSecurityFlags

        **[since 5.6] QBluetooth::SecurityFlags
        QBluetoothSocket::preferredSecurityFlags() const**

        Returns the security parameters used for the initial connection attempt.

        The security parameters may be renegotiated between the two parties
        during or after the connection has been established. If such a change
        happens it is not reflected in the value of this flag.

        On macOS, this flag is always set to **QBluetooth::Security::Secure** .

        This function was introduced in Qt 5.6.

        **See also** **setPreferredSecurityFlags** ().
        """
        ...
    def readData(self, data: bytes, maxSize: int) -> object:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#readData

        **[override virtual protected] qint64 QBluetoothSocket::readData(char *
        data , qint64 maxSize )**

        Reimplements: **QIODevice::readData** (char *data, qint64 maxSize).
        """
        ...
    def setPreferredSecurityFlags(
        self, flags: PySide6.QtBluetooth.QBluetooth.SecurityFlags
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#setPreferredSecurityFlags

        **[since 5.6] void
        QBluetoothSocket::setPreferredSecurityFlags(QBluetooth::SecurityFlags
        flags )**

        Sets the preferred security parameter for the connection attempt to
        **flags**. This value is incorporated when calling **connectToService**
        (). Therefore it is required to reconnect to change this parameter for
        an existing connection.

        On Bluez this property is set to **QBluetooth::Security::Authorization**
        by default.

        On macOS, this value is ignored as the platform does not permit access
        to the security parameter of the socket. By default the platform prefers
        secure/encrypted connections though and therefore this function always
        returns **QBluetooth::Security::Secure** .

        Android only supports two levels of security (secure and non-secure). If
        this flag is set to **QBluetooth::Security::NoSecurity**  the socket
        object will not employ any authentication or encryption. Any other
        security flag combination will trigger a secure Bluetooth connection.
        This flag is set to **QBluetooth::Security::Secure**  by default.

        **Note:** A secure connection requires a pairing between the two
        devices. On some platforms, the pairing is automatically initiated
        during the establishment of the connection. Other platforms require the
        application to manually trigger the pairing before attempting to
        connect.

        This function was introduced in Qt 5.6.

        **See also** **preferredSecurityFlags** ().
        """
        ...
    def setSocketDescriptor(
        self,
        socketDescriptor: int,
        socketType: PySide6.QtBluetooth.QBluetoothServiceInfo.Protocol,
        socketState: PySide6.QtBluetooth.QBluetoothSocket.SocketState = ...,
        openMode: PySide6.QtCore.QIODeviceBase.OpenMode = ...,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#setSocketDescriptor

        **bool QBluetoothSocket::setSocketDescriptor(int socketDescriptor ,
        QBluetoothServiceInfo::Protocol socketType ,
        QBluetoothSocket::SocketState socketState = SocketState::ConnectedState,
        QIODeviceBase::OpenMode openMode = ReadWrite)**

        Set the socket to use **socketDescriptor** with a type of **socketType**
        , which is in state, **socketState** , and mode, **openMode**.

        Returns true on success

        **See also** **socketDescriptor** ().
        """
        ...
    def setSocketError(
        self, error: PySide6.QtBluetooth.QBluetoothSocket.SocketError
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#setSocketError

        **[protected] void
        QBluetoothSocket::setSocketError(QBluetoothSocket::SocketError error_
        )**

        Sets the type of error that last occurred to **error_**.
        """
        ...
    def setSocketState(
        self, state: PySide6.QtBluetooth.QBluetoothSocket.SocketState
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#setSocketState

        **[protected] void
        QBluetoothSocket::setSocketState(QBluetoothSocket::SocketState state )**

        Sets the socket state to **state**.
        """
        ...
    def socketDescriptor(self) -> int:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#socketDescriptor

        **int QBluetoothSocket::socketDescriptor() const**

        Returns the platform-specific socket descriptor, if available. This
        function returns -1 if the descriptor is not available or an error has
        occurred.

        **See also** **setSocketDescriptor** ().
        """
        ...
    def socketType(self) -> PySide6.QtBluetooth.QBluetoothServiceInfo.Protocol:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#socketType

        **QBluetoothServiceInfo::Protocol QBluetoothSocket::socketType() const**

        Returns the socket type. The socket automatically adjusts to the
        protocol offered by the remote service.

        Android only support **RFCOMM**  based sockets.
        """
        ...
    def state(self) -> PySide6.QtBluetooth.QBluetoothSocket.SocketState:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#state

        **QBluetoothSocket::SocketState QBluetoothSocket::state() const**

        Returns the current state of the socket.
        """
        ...
    def writeData(self, data: bytes, maxSize: int) -> int:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#writeData

        **[override virtual protected] qint64 QBluetoothSocket::writeData(const
        char * data , qint64 maxSize )**

        Reimplements: **QIODevice::writeData** (const char *data, qint64
        maxSize).
        """
        ...
    @property
    def connected(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#connected

        **[signal] void QBluetoothSocket::connected()**

        This signal is emitted when a connection is established.

        **See also** **QBluetoothSocket::SocketState::ConnectedState**  and
        **stateChanged** ().
        """
        ...
    @property
    def disconnected(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#disconnected

        **[signal] void QBluetoothSocket::disconnected()**

        This signal is emitted when the socket is disconnected.

        **See also** **QBluetoothSocket::SocketState::UnconnectedState**  and
        **stateChanged** ().
        """
        ...
    @property
    def errorOccurred(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#errorOccurred

        **[signal, since 6.2] void
        QBluetoothSocket::errorOccurred(QBluetoothSocket::SocketError error )**

        This signal is emitted when an **error** occurs.

        This function was introduced in Qt 6.2.

        **See also** **error** ().
        """
        ...
    @property
    def stateChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qbluetoothsocket.html#stateChanged

        **[signal] void
        QBluetoothSocket::stateChanged(QBluetoothSocket::SocketState state )**

        This signal is emitted when the socket state changes to **state**.

        **See also** **connected** (), **disconnected** (), **state** (), and
        **QBluetoothSocket::SocketState** .
        """
        ...
