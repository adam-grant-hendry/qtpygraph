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
PySide6.QtNetwork, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from collections.abc import Sequence
from enum import IntFlag

import PySide6.QtCore
import PySide6.QtNetwork

class QDtls(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qdtls.html

    **Detailed Description**

    The QDtls class can be used to establish a secure connection with a network
    peer using User Datagram Protocol (UDP). DTLS connection over essentially
    connectionless UDP means that two peers first have to successfully complete
    a TLS handshake by calling **doHandshake** (). After the handshake has
    completed, encrypted datagrams can be sent to the peer using
    **writeDatagramEncrypted** (). Encrypted datagrams coming from the peer can
    be decrypted by **decryptDatagram** ().

    QDtls is designed to work with **QUdpSocket** . Since **QUdpSocket**  can
    receive datagrams coming from different peers, an application must implement
    demultiplexing, forwarding datagrams coming from different peers to their
    corresponding instances of QDtls. An association between a network peer and
    its QDtls object can be established using the peer's address and port
    number. Before starting a handshake, the application must set the peer's
    address and port number using **setPeer** ().

    QDtls does not read datagrams from **QUdpSocket** , this is expected to be
    done by the application, for example, in a slot attached to the
    **QUdpSocket::readyRead** () signal. Then, these datagrams must be processed
    by QDtls.

    **Note:** QDtls does **not** take ownership of the **QUdpSocket**  object.

    Normally, several datagrams are to be received and sent by both peers during
    the handshake phase. Upon reading datagrams, server and client must pass
    these datagrams to **doHandshake** () until some error is found or
    **handshakeState** () returns **HandshakeComplete** :

    // A client initiates a handshake:
        **QUdpSocket**  clientSocket;
    **QDtls**  clientDtls;
        clientDtls.setPeer(address, port, peerName);
    clientDtls.doHandshake(&clientSocket);

        // A server accepting an
    incoming connection; address, port, clientHello are
        // read by
    QUdpSocket::readDatagram():
        **QByteArray**
    clientHello(serverSocket.pendingDatagramSize(), Qt::Uninitialized);
    **QHostAddress**  address;
        quin16 port = {};
    serverSocket.readDatagram(clientHello.data(), clientHello.size(), &address,
    &port);

        **QDtls**  serverDtls;
        serverDtls.setPeer(address,
    port);
        serverDtls.doHandshake(&serverSocket, clientHello);

        //
    Handshake completion, both for server and client:
        void
    DtlsConnection::continueHandshake(const **QByteArray**  &datagram)
        {
    if (dtls.doHandshake(&udpSocket, datagram)) {
                // Check handshake
    status:
                if (dtls.handshakeStatus() == QDlts::HandshakeComplete)
    {
                    // Secure DTLS connection is now established.
    }
            } else {
                // Error handling.
            }
        }

    For a server, the first call to **doHandshake** () requires a non-empty
    datagram containing a ClientHello message. If the server also deploys
    **QDtlsClientVerifier** , the first ClientHello message is expected to be
    the one verified by **QDtlsClientVerifier** .

    In case the peer's identity cannot be validated during the handshake, the
    application must inspect errors returned by **peerVerificationErrors** ()
    and then either ignore errors by calling **ignoreVerificationErrors** () or
    abort the handshake by calling **abortHandshake** (). If errors were
    ignored, the handshake can be resumed by calling **resumeHandshake** ().

    After the handshake has been completed, datagrams can be sent to and
    received from the network peer securely:

    // Sending an encrypted datagram:
    dtlsConnection.writeDatagramEncrypted(&clientSocket, "Hello DTLS server!");
    // Decryption:
        **QByteArray**  encryptedMessage(dgramSize);
    socket.readDatagram(encryptedMessage.data(), dgramSize);
        const
    **QByteArray**  plainText = dtlsConnection.decryptDatagram(&socket,
    encryptedMessage);

    A DTLS connection may be closed using **shutdown** ().

    DtlsClient::~DtlsClient()
        {
            clientDtls.shutdown(&clientSocket);
    }

    **Warning:** It's recommended to call **shutdown** () before destroying the
    client's QDtls object if you are planning to re-use the same port number to
    connect to the server later. Otherwise, the server may drop incoming
    ClientHello messages, see **RFC 6347, section 4.2.8**  for more details and
    implementation hints.

    If the server does not use **QDtlsClientVerifier** , it **must** configure
    its QDtls objects to disable the cookie verification procedure:

    auto config = **QSslConfiguration** ::defaultDtlsConfiguration();
    config.setDtlsCookieVerificationEnabled(false);
        // Some other
    customization ...
        dtlsConnection.setDtlsConfiguration(config);

    A server that uses cookie verification with non-default generator parameters
    **must** set the same parameters for its QDtls object before starting the
    handshake.

    **Note:** The DTLS protocol leaves Path Maximum Transmission Unit (PMTU)
    discovery to the application. The application may provide QDtls with the MTU
    using **setMtuHint** (). This hint affects only the handshake phase, since
    only handshake messages can be fragmented and reassembled by the DTLS. All
    other messages sent by the application must fit into a single datagram.

    **Note:** DTLS-specific headers add some overhead to application data
    further reducing the possible message size.

    **Warning:** A server configured to reply with HelloVerifyRequest will drop
    all fragmented ClientHello messages, never starting a handshake.

    The **DTLS server**  and **DTLS client**  examples illustrate how to use
    QDtls in applications.

    **See also** **QUdpSocket** , **QDtlsClientVerifier** , **HandshakeState** ,
    **QDtlsError** , and **QSslConfiguration** .
    """

    HandshakeNotStarted: QDtls.HandshakeState = ...
    HandshakeInProgress: QDtls.HandshakeState = ...
    PeerVerificationFailed: QDtls.HandshakeState = ...
    HandshakeComplete: QDtls.HandshakeState = ...

    class HandshakeState(IntFlag):
        HandshakeNotStarted: QDtls.HandshakeState = ...
        HandshakeInProgress: QDtls.HandshakeState = ...
        PeerVerificationFailed: QDtls.HandshakeState = ...
        HandshakeComplete: QDtls.HandshakeState = ...
    def __init__(
        self,
        mode: PySide6.QtNetwork.QSslSocket.SslMode,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdtls.html#QDtls

        **QDtls::QDtls(QSslSocket::SslMode mode , QObject * parent = nullptr)**

        Creates a QDtls object, **parent** is passed to the **QObject**
        constructor. **mode** is **QSslSocket::SslServerMode**  for a server-
        side DTLS connection or **QSslSocket::SslClientMode**  for a client.

        **See also** **sslMode** () and **QSslSocket::SslMode** .
        """
        ...
    def abortHandshake(self, socket: PySide6.QtNetwork.QUdpSocket) -> bool:
        """
        https://doc.qt.io/qt-6/qdtls.html#abortHandshake

        **bool QDtls::abortHandshake(QUdpSocket * socket )**

        Aborts the ongoing handshake. Returns true if one was on-going on
        **socket** ; otherwise, sets a suitable error and returns false.

        **See also** **doHandshake** () and **resumeHandshake** ().
        """
        ...
    def decryptDatagram(
        self,
        socket: PySide6.QtNetwork.QUdpSocket,
        dgram: PySide6.QtCore.QByteArray | bytes,
    ) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qdtls.html#decryptDatagram

        **QByteArray QDtls::decryptDatagram(QUdpSocket * socket , const
        QByteArray & dgram )**

        Decrypts **dgram** and returns its contents as plain text. The handshake
        must be completed before datagrams can be decrypted. Depending on the
        type of the TLS message the connection may write into **socket** , which
        must be a valid pointer.
        """
        ...
    def doHandshake(
        self,
        socket: PySide6.QtNetwork.QUdpSocket,
        dgram: PySide6.QtCore.QByteArray | bytes = ...,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qdtls.html#doHandshake

        **bool QDtls::doHandshake(QUdpSocket * socket , const QByteArray & dgram
        = {})**

        Starts or continues a DTLS handshake. **socket** must be a valid
        pointer. When starting a server-side DTLS handshake, **dgram** must
        contain the initial ClientHello message read from **QUdpSocket** . This
        function returns `true` if no error was found. Handshake state can be
        tested using **handshakeState** (). `false` return means some error
        occurred, use **dtlsError** () for more detailed information.

        **Note:** If the identity of the peer can't be established, the error is
        set to **QDtlsError::PeerVerificationError** . If you want to ignore
        verification errors and continue connecting, you must call
        **ignoreVerificationErrors** () and then **resumeHandshake** (). If the
        errors cannot be ignored, you must call **abortHandshake** ().

        if (!dtls.doHandshake(&socket, dgram)) {
                if (dtls.dtlsError() ==
        **QDtlsError** ::PeerVerificationError)
        dtls.abortAfterError(&socket);
            }

        **See also** **handshakeState** (), **dtlsError** (),
        **ignoreVerificationErrors** (), **resumeHandshake** (), and
        **abortHandshake** ().
        """
        ...
    def dtlsConfiguration(self) -> PySide6.QtNetwork.QSslConfiguration:
        """
        https://doc.qt.io/qt-6/qdtls.html#dtlsConfiguration

        **QSslConfiguration QDtls::dtlsConfiguration() const**

        Returns either the default DTLS configuration or the configuration set
        by an earlier call to **setDtlsConfiguration** ().

        **See also** **setDtlsConfiguration** () and
        **QSslConfiguration::defaultDtlsConfiguration** ().
        """
        ...
    def dtlsError(self) -> PySide6.QtNetwork.QDtlsError:
        """
        https://doc.qt.io/qt-6/qdtls.html#dtlsError

        **QDtlsError QDtls::dtlsError() const**

        Returns the last error encountered by the connection or
        **QDtlsError::NoError** .

        **See also** **dtlsErrorString** () and **QDtlsError** .
        """
        ...
    def dtlsErrorString(self) -> str:
        """
        https://doc.qt.io/qt-6/qdtls.html#dtlsErrorString

        **QString QDtls::dtlsErrorString() const**

        Returns a textual description for the last error encountered by the
        connection or empty string.

        **See also** **dtlsError** ().
        """
        ...
    def handleTimeout(self, socket: PySide6.QtNetwork.QUdpSocket) -> bool:
        """
        https://doc.qt.io/qt-6/qdtls.html#handleTimeout

        **bool QDtls::handleTimeout(QUdpSocket * socket )**

        If a timeout occurs during the handshake, the **handshakeTimeout** ()
        signal is emitted. The application must call handleTimeout() to
        retransmit handshake messages; handleTimeout() returns `true` if a
        timeout has occurred, false otherwise. **socket** must be a valid
        pointer.

        **See also** **handshakeTimeout** ().
        """
        ...
    def handshakeState(self) -> PySide6.QtNetwork.QDtls.HandshakeState:
        """
        https://doc.qt.io/qt-6/qdtls.html#handshakeState

        **QDtls::HandshakeState QDtls::handshakeState() const**

        Returns the current handshake state for this **QDtls** .

        **See also** **doHandshake** () and **QDtls::HandshakeState** .
        """
        ...
    def ignoreVerificationErrors(
        self, errorsToIgnore: Sequence[PySide6.QtNetwork.QSslError]
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdtls.html#ignoreVerificationErrors

        **void QDtls::ignoreVerificationErrors(const QList<QSslError> &
        errorsToIgnore )**

        This method tells **QDtls**  to ignore only the errors given in
        **errorsToIgnore**.

        If, for instance, you want to connect to a server that uses a self-
        signed certificate, consider the following snippet:

        **QList** <**QSslCertificate** > cert = **QSslCertificate**
        ::fromPath(QLatin1String("server-certificate.pem"));
            **QSslError**
        error(**QSslError** ::SelfSignedCertificate, cert.at(0));
            **QList**
        <**QSslError** > expectedSslErrors;
            expectedSslErrors.append(error);
        **QDtls**  dtls;
            dtls.ignoreVerificationErrors(expectedSslErrors);
        dtls.doHandshake(udpSocket);

        You can also call this function after **doHandshake** () encountered the
        **QDtlsError::PeerVerificationError**  error, and then resume the
        handshake by calling **resumeHandshake** ().

        Later calls to this function will replace the list of errors that were
        passed in previous calls. You can clear the list of errors you want to
        ignore by calling this function with an empty list.

        **See also** **doHandshake** (), **resumeHandshake** (), and
        **QSslError** .
        """
        ...
    def isConnectionEncrypted(self) -> bool:
        """
        https://doc.qt.io/qt-6/qdtls.html#isConnectionEncrypted

        **bool QDtls::isConnectionEncrypted() const**

        Returns `true` if DTLS handshake completed successfully.

        **See also** **doHandshake** () and **handshakeState** ().
        """
        ...
    def mtuHint(self) -> int:
        """
        https://doc.qt.io/qt-6/qdtls.html#mtuHint

        **quint16 QDtls::mtuHint() const**

        Returns the value previously set by **setMtuHint** (). The default value
        is 0.

        **See also** **setMtuHint** ().
        """
        ...
    def peerAddress(self) -> PySide6.QtNetwork.QHostAddress:
        """
        https://doc.qt.io/qt-6/qdtls.html#peerAddress

        **QHostAddress QDtls::peerAddress() const**

        Returns the peer's address, set by **setPeer** (), or
        **QHostAddress::Null** .

        **See also** **setPeer** ().
        """
        ...
    def peerPort(self) -> int:
        """
        https://doc.qt.io/qt-6/qdtls.html#peerPort

        **quint16 QDtls::peerPort() const**

        Returns the peer's port number, set by **setPeer** (), or 0.

        **See also** **setPeer** ().
        """
        ...
    def peerVerificationErrors(self) -> list[PySide6.QtNetwork.QSslError]:
        """
        https://doc.qt.io/qt-6/qdtls.html#peerVerificationErrors

        **QList<QSslError> QDtls::peerVerificationErrors() const**

        Returns errors found while establishing the identity of the peer.

        If you want to continue connecting despite the errors that have
        occurred, you must call **ignoreVerificationErrors** ().
        """
        ...
    def peerVerificationName(self) -> str:
        """
        https://doc.qt.io/qt-6/qdtls.html#peerVerificationName

        **QString QDtls::peerVerificationName() const**

        Returns the host name set by **setPeer** () or
        **setPeerVerificationName** (). The default value is an empty string.

        **See also** **setPeerVerificationName** () and **setPeer** ().
        """
        ...
    def resumeHandshake(self, socket: PySide6.QtNetwork.QUdpSocket) -> bool:
        """
        https://doc.qt.io/qt-6/qdtls.html#resumeHandshake

        **bool QDtls::resumeHandshake(QUdpSocket * socket )**

        If peer verification errors were ignored during the handshake,
        resumeHandshake() resumes and completes the handshake and returns
        `true`. **socket** must be a valid pointer. Returns `false` if the
        handshake could not be resumed.

        **See also** **doHandshake** (), **abortHandshake** (),
        **peerVerificationErrors** (), and **ignoreVerificationErrors** ().
        """
        ...
    def sessionCipher(self) -> PySide6.QtNetwork.QSslCipher:
        """
        https://doc.qt.io/qt-6/qdtls.html#sessionCipher

        **QSslCipher QDtls::sessionCipher() const**

        Returns the cryptographic **cipher**  used by this connection, or a null
        cipher if the connection isn't encrypted. The cipher for the session is
        selected during the handshake phase. The cipher is used to encrypt and
        decrypt data.

        **QSslConfiguration**  provides functions for setting the ordered list
        of ciphers from which the handshake phase will eventually select the
        session cipher. This ordered list must be in place before the handshake
        phase begins.

        **See also** **QSslConfiguration** , **setDtlsConfiguration** (), and
        **dtlsConfiguration** ().
        """
        ...
    def sessionProtocol(self) -> PySide6.QtNetwork.QSsl.SslProtocol:
        """
        https://doc.qt.io/qt-6/qdtls.html#sessionProtocol

        **QSsl::SslProtocol QDtls::sessionProtocol() const**

        Returns the DTLS protocol version used by this connection, or
        UnknownProtocol if the connection isn't encrypted yet. The protocol for
        the connection is selected during the handshake phase.

        **setDtlsConfiguration** () can set the preferred version before the
        handshake starts.

        **See also** **setDtlsConfiguration** (), **QSslConfiguration** ,
        **QSslConfiguration::defaultDtlsConfiguration** (), and
        **QSslConfiguration::setProtocol** ().
        """
        ...
    def setDtlsConfiguration(
        self, configuration: PySide6.QtNetwork.QSslConfiguration
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qdtls.html#setDtlsConfiguration

        **bool QDtls::setDtlsConfiguration(const QSslConfiguration &
        configuration )**

        Sets the connection's TLS configuration from **configuration** and
        returns `true` if successful.

        **Note:** This function must be called before the handshake starts.

        **See also** **dtlsConfiguration** () and **doHandshake** ().
        """
        ...
    def setMtuHint(self, mtuHint: int) -> None:
        """
        https://doc.qt.io/qt-6/qdtls.html#setMtuHint

        **void QDtls::setMtuHint(quint16 mtuHint )**

        **mtuHint** is the maximum transmission unit (MTU), either discovered or
        guessed by the application. The application is not required to set this
        value.

        **See also** **mtuHint** () and **QAbstractSocket::PathMtuSocketOption**
        .
        """
        ...
    def setPeer(
        self,
        address: (
            PySide6.QtNetwork.QHostAddress | PySide6.QtNetwork.QHostAddress.SpecialAddress
        ),
        port: int,
        verificationName: str = ...,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qdtls.html#setPeer

        **bool QDtls::setPeer(const QHostAddress & address , quint16 port ,
        const QString & verificationName = {})**

        Sets the peer's address, **port** , and host name and returns `true` if
        successful. **address** must not be null, multicast, or broadcast.
        **verificationName** is the host name used for the certificate
        validation.

        **See also** **peerAddress** (), **peerPort** (), and
        **peerVerificationName** ().
        """
        ...
    def setPeerVerificationName(self, name: str) -> bool:
        """
        https://doc.qt.io/qt-6/qdtls.html#setPeerVerificationName

        **bool QDtls::setPeerVerificationName(const QString & name )**

        Sets the host **name** that will be used for the certificate validation
        and returns `true` if successful.

        **Note:** This function must be called before the handshake starts.

        **See also** **peerVerificationName** () and **setPeer** ().
        """
        ...
    def shutdown(self, socket: PySide6.QtNetwork.QUdpSocket) -> bool:
        """
        https://doc.qt.io/qt-6/qdtls.html#shutdown

        **bool QDtls::shutdown(QUdpSocket * socket )**

        Sends an encrypted shutdown alert message and closes the DTLS
        connection. Handshake state changes to **QDtls::HandshakeNotStarted** .
        **socket** must be a valid pointer. This function returns `true` on
        success.

        **See also** **doHandshake** ().
        """
        ...
    def sslMode(self) -> PySide6.QtNetwork.QSslSocket.SslMode:
        """
        https://doc.qt.io/qt-6/qdtls.html#sslMode

        **QSslSocket::SslMode QDtls::sslMode() const**

        Returns **QSslSocket::SslServerMode**  for a server-side connection and
        **QSslSocket::SslClientMode**  for a client.

        **See also** **QDtls** () and **QSslSocket::SslMode** .
        """
        ...
    def writeDatagramEncrypted(
        self,
        socket: PySide6.QtNetwork.QUdpSocket,
        dgram: PySide6.QtCore.QByteArray | bytes,
    ) -> int:
        """
        https://doc.qt.io/qt-6/qdtls.html#writeDatagramEncrypted

        **qint64 QDtls::writeDatagramEncrypted(QUdpSocket * socket , const
        QByteArray & dgram )**

        Encrypts **dgram** and writes the encrypted data into **socket**.
        Returns the number of bytes written, or -1 in case of error. The
        handshake must be completed before writing encrypted data. **socket**
        must be a valid pointer.

        **See also** **doHandshake** (), **handshakeState** (),
        **isConnectionEncrypted** (), and **dtlsError** ().
        """
        ...
    @property
    def handshakeTimeout(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdtls.html#handshakeTimeout

        **[signal] void QDtls::handshakeTimeout()**

        Packet loss can result in timeouts during the handshake phase. In this
        case **QDtls**  emits a handshakeTimeout() signal. Call
        **handleTimeout** () to retransmit the handshake messages:

        DtlsClient::DtlsClient()
            {
                // Some initialization code here
        ...
                connect(&clientDtls, &**QDtls** ::handshakeTimeout, this,
        &DtlsClient::handleTimeout);
            }

            void
        DtlsClient::handleTimeout()
            {
        clientDtls.handleTimeout(&clientSocket);
            }

        **See also** **handleTimeout** ().
        """
        ...
    @property
    def pskRequired(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdtls.html#pskRequired

        **[signal] void QDtls::pskRequired(QSslPreSharedKeyAuthenticator *
        authenticator )**

        **QDtls**  emits this signal when it negotiates a PSK ciphersuite, and
        therefore a PSK authentication is then required.

        When using PSK, the client must send to the server a valid identity and
        a valid pre shared key, in order for the TLS handshake to continue.
        Applications can provide this information in a slot connected to this
        signal, by filling in the passed **authenticator** object according to
        their needs.

        **Note:** Ignoring this signal, or failing to provide the required
        credentials, will cause the handshake to fail, and therefore the
        connection to be aborted.

        **Note:** The **authenticator** object is owned by **QDtls**  and must
        not be deleted by the application.

        **See also** **QSslPreSharedKeyAuthenticator** .
        """
        ...
