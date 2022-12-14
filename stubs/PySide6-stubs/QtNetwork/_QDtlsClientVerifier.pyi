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

import PySide6.QtCore
import PySide6.QtNetwork

class QDtlsClientVerifier(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qdtlsclientverifier.html

    **Detailed Description**

    The QDtlsClientVerifier class implements server-side DTLS cookie generation
    and verification. Datagram security protocols are highly susceptible to a
    variety of Denial-of-Service attacks. According to **RFC 6347, section
    4.2.1** , these are two of the more common types of attack:

    * An attacker transmits a series of handshake initiation requests, causing a
    server to allocate excessive resources and potentially perform expensive
    cryptographic operations.
      * An attacker transmits a series of handshake
    initiation requests with a forged source of the victim, making the server
    act as an amplifier. Normally, the server would reply to the victim machine
    with a Certificate message, which can be quite large, thus flooding the
    victim machine with datagrams.

    As a countermeasure to these attacks, **RFC 6347, section 4.2.1**  proposes
    a stateless cookie technique that a server may deploy:

    * In response to the initial ClientHello message, the server sends a
    HelloVerifyRequest, which contains a cookie. This cookie is a cryptographic
    hash and is generated using the client's address, port number, and the
    server's secret (which is a cryptographically strong pseudo-random sequence
    of bytes).
      * A reachable DTLS client is expected to reply with a new
    ClientHello message containing this cookie.
      * When the server receives the
    ClientHello message with a cookie, it generates a new cookie as described
    above. This new cookie is compared to the one found in the ClientHello
    message.
      * In the cookies are equal, the client is considered to be real,
    and the server can continue with a TLS handshake procedure.

    **Note:** A DTLS server is not required to use DTLS cookies.

    QDtlsClientVerifier is designed to work in pair with **QUdpSocket** , as
    shown in the following code-excerpt:

    class DtlsServer : public **QObject**
        {
        public:
            bool
    listen(const **QHostAddress**  &address, **quint16**  port);
            // ...
    private:
            void readyRead();
            // ...
    **QUdpSocket**  serverSocket;
            **QDtlsClientVerifier**  verifier;
    // ...
        };

        bool DtlsServer::listen(const **QHostAddress**
    &serverAddress, **quint16**  serverPort)
        {
            if
    (serverSocket.bind(serverAddress, serverPort))
    connect(&serverSocket, &**QUdpSocket** ::readyRead, this,
    &DtlsServer::readyRead);
            return serverSocket.state() ==
    **QAbstractSocket** ::BoundState;
        }

        void
    DtlsServer::readyRead()
        {
            **QByteArray**
    dgram(serverSocket.pendingDatagramSize(), Qt::Uninitialized);
    **QHostAddress**  address;
            **quint16**  port = {};
    serverSocket.readDatagram(dgram.data(), dgram.size(), &address, &port);
    if (verifiedClients.contains({address, port}) {
                // This client
    was verified previously, we either continue the
                // handshake or
    decrypt the incoming message.
            } else if
    (verifier.verifyClient(&serverSocket, dgram, address, port)) {
    // Apparently we have a real DTLS client who wants to send us
                //
    encrypted datagrams. Remember this client as verified
                // and
    proceed with a handshake.
            } else {
                // No matching cookie
    was found in the incoming datagram,
                // verifyClient() has sent a
    ClientVerify message.
                // We'll hear from the client again soon,
    if they're real.
            }
        }

    QDtlsClientVerifier does not impose any restrictions on how the application
    uses **QUdpSocket** . For example, it is possible to have a server with a
    single **QUdpSocket**  in state **QAbstractSocket::BoundState** , handling
    multiple DTLS clients simultaneously:

    * Testing if new clients are real DTLS-capable clients.
      * Completing TLS
    handshakes with the verified clients (see **QDtls** ).
      * Decrypting
    datagrams coming from the connected clients (see **QDtls** ).
      * Sending
    encrypted datagrams to the connected clients (see **QDtls** ).

    This implies that QDtlsClientVerifier does not read directly from a socket,
    instead it expects the application to read an incoming datagram, extract the
    sender's address, and port, and then pass this data to **verifyClient** ().
    To send a HelloVerifyRequest message, **verifyClient** () can write to the
    **QUdpSocket** .

    **Note:** QDtlsClientVerifier does not take ownership of the **QUdpSocket**
    object.

    By default QDtlsClientVerifier obtains its secret from a cryptographically
    strong pseudorandom number generator.

    **Note:** The default secret is shared by all objects of the classes
    QDtlsClientVerifier and **QDtls** . Since this can impose security risks,
    RFC 6347 recommends to change the server's secret frequently. Please see
    **RFC 6347, section 4.2.1**  for hints about possible server
    implementations. Cookie generator parameters can be set using the class
    **QDtlsClientVerifier::GeneratorParameters**  and
    **setCookieGeneratorParameters** ():

    void DtlsServer::updateServerSecret()
        {
            const **QByteArray**
    newSecret(generateCryptoStrongSecret());
            if (newSecret.size()) {
    usedCookies.append(newSecret);
    verifier.setCookieGeneratorParameters({**QCryptographicHash** ::Sha1,
    newSecret});
            }
        }

    The **DTLS server**  example illustrates how to use QDtlsClientVerifier in a
    server application.

    **See also** **QUdpSocket** , **QAbstractSocket::BoundState** , **QDtls** ,
    **verifyClient** (), **GeneratorParameters** ,
    **setCookieGeneratorParameters** (), **cookieGeneratorParameters** (),
    **QDtls::setCookieGeneratorParameters** (),
    **QDtls::cookieGeneratorParameters** (), **QCryptographicHash::Algorithm** ,
    **QDtlsError** , **dtlsError** (), and **dtlsErrorString** ().
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qdtlsclientverifier.html#QDtlsClientVerifier

        **QDtlsClientVerifier::QDtlsClientVerifier(QObject * parent = nullptr)**

        Constructs a QDtlsClientVerifier object, **parent** is passed to
        **QObject** 's constructor.
        """
        ...
    def dtlsError(self) -> PySide6.QtNetwork.QDtlsError:
        """
        https://doc.qt.io/qt-6/qdtlsclientverifier.html#dtlsError

        **QDtlsError QDtlsClientVerifier::dtlsError() const**

        Returns the last error that occurred or **QDtlsError::NoError** .

        **See also** **QDtlsError**  and **dtlsErrorString** ().
        """
        ...
    def dtlsErrorString(self) -> str:
        """
        https://doc.qt.io/qt-6/qdtlsclientverifier.html#dtlsErrorString

        **QString QDtlsClientVerifier::dtlsErrorString() const**

        Returns a textual description of the last error, or an empty string.

        **See also** **dtlsError** ().
        """
        ...
    def verifiedHello(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qdtlsclientverifier.html#verifiedHello

        **QByteArray QDtlsClientVerifier::verifiedHello() const**

        Convenience function. Returns the last ClientHello message that was
        successfully verified, or an empty **QByteArray**  if no verification
        has completed.

        **See also** **verifyClient** ().
        """
        ...
    def verifyClient(
        self,
        socket: PySide6.QtNetwork.QUdpSocket,
        dgram: PySide6.QtCore.QByteArray | bytes,
        address: (
            PySide6.QtNetwork.QHostAddress | PySide6.QtNetwork.QHostAddress.SpecialAddress
        ),
        port: int,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qdtlsclientverifier.html#verifyClient

        **bool QDtlsClientVerifier::verifyClient(QUdpSocket * socket , const
        QByteArray & dgram , const QHostAddress & address , quint16 port )**

        **socket** must be a valid pointer, **dgram** must be a non-empty
        datagram, **address** cannot be null, broadcast, or multicast. **port**
        is the remote peer's port. This function returns `true` if **dgram**
        contains a ClientHello message with a valid cookie. If no matching
        cookie is found, verifyClient() will send a HelloVerifyRequest message
        using **socket** and return `false`.

        The following snippet shows how a server application may check for
        errors:

        if (!verifier.verifyClient(&socket, message, address, port)) {
        switch (verifyClient.dtlsError()) {
                case **QDtlsError**
        ::NoError:
                    // Not verified yet, but no errors found and we
        have to wait for the next
                    // message from this client.
        return;
                case **QDtlsError** ::TlsInitializationError:
        // This error is fatal, nothing we can do about it.
                    //
        Probably, quit the server after reporting the error.
                    return;
        case **QDtlsError** ::UnderlyingSocketError:
                    // There is
        some problem in QUdpSocket, handle it (see QUdpSocket::error())
        return;
                case **QDtlsError** ::InvalidInputParameters:
        default:
                    Q_UNREACHABLE();
                }
            }

        **See also** **QHostAddress::isNull** (), **QHostAddress::isBroadcast**
        (), **QHostAddress::isMulticast** (), **setCookieGeneratorParameters**
        (), and **cookieGeneratorParameters** ().
        """
        ...
