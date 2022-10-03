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

from enum import IntFlag
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtNetwork

class QNetworkProxy:
    """
    https://doc.qt.io/qt-6/qnetworkproxy.html

    **Detailed Description**

    QNetworkProxy provides the method for configuring network layer proxy
    support to the Qt network classes. The currently supported classes are
    **QAbstractSocket** , **QTcpSocket** , **QUdpSocket** , **QTcpServer**  and
    **QNetworkAccessManager** . The proxy support is designed to be as
    transparent as possible. This means that existing network-enabled
    applications that you have written should automatically support network
    proxy using the following code.

    **QNetworkProxy**  proxy;
        proxy.setType(**QNetworkProxy**
    ::Socks5Proxy);
        proxy.setHostName("proxy.example.com");
    proxy.setPort(1080);
        proxy.setUser("username");
    proxy.setPassword("password");
        **QNetworkProxy**
    ::setApplicationProxy(proxy);

    An alternative to setting an application wide proxy is to specify the proxy
    for individual sockets using **QAbstractSocket::setProxy** () and
    **QTcpServer::setProxy** (). In this way, it is possible to disable the use
    of a proxy for specific sockets using the following code:

    serverSocket->setProxy(**QNetworkProxy** ::NoProxy);

    Network proxy is not used if the address used in **connectToHost** (),
    **bind** () or **listen** () is equivalent to **QHostAddress::LocalHost**
    or **QHostAddress::LocalHostIPv6** .

    Each type of proxy support has certain restrictions associated with it. You
    should read the **ProxyType**  documentation carefully before selecting a
    proxy type to use.

    **Note:** Changes made to currently connected sockets do not take effect. If
    you need to change a connected socket, you should reconnect it.

    **SOCKS5**

    The SOCKS5 support since Qt 4 is based on **RFC 1928**  and **RFC 1929** .
    The supported authentication methods are no authentication and
    username/password authentication. Both IPv4 and IPv6 are supported. Domain
    names are resolved through the SOCKS5 server if the
    **QNetworkProxy::HostNameLookupCapability**  is enabled, otherwise they are
    resolved locally and the IP address is sent to the server. There are several
    things to remember when using SOCKS5 with **QUdpSocket**  and **QTcpServer**
    :

    With **QUdpSocket** , a call to **bind** () may fail with a timeout error.
    If a port number other than 0 is passed to **bind** (), it is not guaranteed
    that it is the specified port that will be used. Use **localPort** () and
    **localAddress** () to get the actual address and port number in use.
    Because proxied UDP goes through two UDP connections, it is more likely that
    packets will be dropped.

    With **QTcpServer**  a call to **listen** () may fail with a timeout error.
    If a port number other than 0 is passed to **listen** (), then it is not
    guaranteed that it is the specified port that will be used. Use
    **serverPort** () and **serverAddress** () to get the actual address and
    port used to listen for connections. SOCKS5 only supports one accepted
    connection per call to **listen** (), and each call is likely to result in a
    different **serverPort** () being used.

    **See also** **QAbstractSocket**  and **QTcpServer** .
    """

    TunnelingCapability: QNetworkProxy.Capability = ...
    ListeningCapability: QNetworkProxy.Capability = ...
    UdpTunnelingCapability: QNetworkProxy.Capability = ...
    CachingCapability: QNetworkProxy.Capability = ...
    HostNameLookupCapability: QNetworkProxy.Capability = ...
    SctpTunnelingCapability: QNetworkProxy.Capability = ...
    SctpListeningCapability: QNetworkProxy.Capability = ...
    DefaultProxy: QNetworkProxy.ProxyType = ...
    Socks5Proxy: QNetworkProxy.ProxyType = ...
    NoProxy: QNetworkProxy.ProxyType = ...
    HttpProxy: QNetworkProxy.ProxyType = ...
    HttpCachingProxy: QNetworkProxy.ProxyType = ...
    FtpCachingProxy: QNetworkProxy.ProxyType = ...

    class Capabilities: ...

    class Capability(IntFlag):
        TunnelingCapability: QNetworkProxy.Capability = ...
        ListeningCapability: QNetworkProxy.Capability = ...
        UdpTunnelingCapability: QNetworkProxy.Capability = ...
        CachingCapability: QNetworkProxy.Capability = ...
        HostNameLookupCapability: QNetworkProxy.Capability = ...
        SctpTunnelingCapability: QNetworkProxy.Capability = ...
        SctpListeningCapability: QNetworkProxy.Capability = ...

    class ProxyType(IntFlag):
        DefaultProxy: QNetworkProxy.ProxyType = ...
        Socks5Proxy: QNetworkProxy.ProxyType = ...
        NoProxy: QNetworkProxy.ProxyType = ...
        HttpProxy: QNetworkProxy.ProxyType = ...
        HttpCachingProxy: QNetworkProxy.ProxyType = ...
        FtpCachingProxy: QNetworkProxy.ProxyType = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#QNetworkProxy

        **QNetworkProxy::QNetworkProxy()**

        Constructs a QNetworkProxy with **DefaultProxy**  type.

        The proxy type is determined by **applicationProxy** (), which defaults
        to **NoProxy**  or a system-wide proxy if one is configured.

        **See also** **setType** () and **setApplicationProxy** ().
        """
        ...
    @overload
    def __init__(
        self,
        other: (
            PySide6.QtNetwork.QNetworkProxy | PySide6.QtNetwork.QNetworkProxy.ProxyType
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#QNetworkProxy-1

        **QNetworkProxy::QNetworkProxy(QNetworkProxy::ProxyType type , const
        QString & hostName = QString(), quint16 port = 0, const QString & user =
        QString(), const QString & password = QString())**

        Constructs a QNetworkProxy with **type** , **hostName** , **port** ,
        **user** and **password**.

        The default capabilities for proxy type **type** are set automatically.

        **See also** **capabilities** ().
        """
        ...
    @overload
    def __init__(
        self,
        type: PySide6.QtNetwork.QNetworkProxy.ProxyType,
        hostName: str = ...,
        port: int = ...,
        user: str = ...,
        password: str = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#QNetworkProxy-2

        **QNetworkProxy::QNetworkProxy(const QNetworkProxy & other )**

        Constructs a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    @staticmethod
    def applicationProxy() -> PySide6.QtNetwork.QNetworkProxy:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#applicationProxy

        **[static] QNetworkProxy QNetworkProxy::applicationProxy()**

        Returns the application level network proxying.

        If a **QAbstractSocket**  or **QTcpSocket**  has the
        **QNetworkProxy::DefaultProxy**  type, then the **QNetworkProxy**
        returned by this function is used.

        **See also** **QNetworkProxyFactory** , **setApplicationProxy** (),
        **QAbstractSocket::proxy** (), and **QTcpServer::proxy** ().
        """
        ...
    def capabilities(self) -> PySide6.QtNetwork.QNetworkProxy.Capabilities:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#capabilities

        **QNetworkProxy::Capabilities QNetworkProxy::capabilities() const**

        Returns the capabilities of this proxy server.

        **See also** **setCapabilities** () and **type** ().
        """
        ...
    def hasRawHeader(self, headerName: PySide6.QtCore.QByteArray | bytes) -> bool:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#hasRawHeader

        **[since 5.0] bool QNetworkProxy::hasRawHeader(const QByteArray &
        headerName ) const**

        Returns `true` if the raw header **headerName** is in use for this
        proxy. Returns `false` if the proxy is not of type **HttpProxy**  or
        **HttpCachingProxy** .

        This function was introduced in Qt 5.0.

        **See also** **rawHeader** () and **setRawHeader** ().
        """
        ...
    def header(self, header: PySide6.QtNetwork.QNetworkRequest.KnownHeaders) -> Any:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#header

        **[since 5.0] QVariant
        QNetworkProxy::header(QNetworkRequest::KnownHeaders header ) const**

        Returns the value of the known network header **header** if it is in use
        for this proxy. If it is not present, returns QVariant() (i.e., an
        invalid variant).

        This function was introduced in Qt 5.0.

        **See also** **QNetworkRequest::KnownHeaders** , **rawHeader** (), and
        **setHeader** ().
        """
        ...
    def hostName(self) -> str:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#hostName

        **QString QNetworkProxy::hostName() const**

        Returns the host name of the proxy host.

        **See also** **setHostName** (), **setPort** (), and **port** ().
        """
        ...
    def isCachingProxy(self) -> bool:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#isCachingProxy

        **bool QNetworkProxy::isCachingProxy() const**

        Returns `true` if this proxy supports the
        **QNetworkProxy::CachingCapability**  capability.

        In Qt 4.4, the capability was tied to the proxy type, but since Qt 4.5
        it is possible to remove the capability of caching from a proxy by
        calling **setCapabilities** ().

        **See also** **capabilities** (), **type** (), and
        **isTransparentProxy** ().
        """
        ...
    def isTransparentProxy(self) -> bool:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#isTransparentProxy

        **bool QNetworkProxy::isTransparentProxy() const**

        Returns `true` if this proxy supports transparent tunneling of TCP
        connections. This matches the **QNetworkProxy::TunnelingCapability**
        capability.

        In Qt 4.4, the capability was tied to the proxy type, but since Qt 4.5
        it is possible to remove the capability of caching from a proxy by
        calling **setCapabilities** ().

        **See also** **capabilities** (), **type** (), and **isCachingProxy**
        ().
        """
        ...
    def password(self) -> str:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#password

        **QString QNetworkProxy::password() const**

        Returns the password used for authentication.

        **See also** **user** (), **setPassword** (), and **setUser** ().
        """
        ...
    def port(self) -> int:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#port

        **quint16 QNetworkProxy::port() const**

        Returns the port of the proxy host.

        **See also** **setHostName** (), **setPort** (), and **hostName** ().
        """
        ...
    def rawHeader(
        self, headerName: PySide6.QtCore.QByteArray | bytes
    ) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#rawHeader

        **[since 5.0] QByteArray QNetworkProxy::rawHeader(const QByteArray &
        headerName ) const**

        Returns the raw form of header **headerName**. If no such header is
        present or the proxy is not of type **HttpProxy**  or
        **HttpCachingProxy** , an empty **QByteArray**  is returned, which may
        be indistinguishable from a header that is present but has no content
        (use **hasRawHeader** () to find out if the header exists or not).

        Raw headers can be set with **setRawHeader** () or with **setHeader**
        ().

        This function was introduced in Qt 5.0.

        **See also** **header** () and **setRawHeader** ().
        """
        ...
    def rawHeaderList(self) -> list[PySide6.QtCore.QByteArray]:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#rawHeaderList

        **[since 5.0] QList<QByteArray> QNetworkProxy::rawHeaderList() const**

        Returns a list of all raw headers that are set in this network proxy.
        The list is in the order that the headers were set.

        If the proxy is not of type **HttpProxy**  or **HttpCachingProxy**  an
        empty **QList**  is returned.

        This function was introduced in Qt 5.0.

        **See also** **hasRawHeader** () and **rawHeader** ().
        """
        ...
    @staticmethod
    def setApplicationProxy(
        proxy: (
            PySide6.QtNetwork.QNetworkProxy | PySide6.QtNetwork.QNetworkProxy.ProxyType
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#setApplicationProxy

        **[static] void QNetworkProxy::setApplicationProxy(const QNetworkProxy &
        networkProxy )**

        Sets the application level network proxying to be **networkProxy**.

        If a **QAbstractSocket**  or **QTcpSocket**  has the
        **QNetworkProxy::DefaultProxy**  type, then the **QNetworkProxy**  set
        with this function is used. If you want more flexibility in determining
        which proxy is used, use the **QNetworkProxyFactory**  class.

        Setting a default proxy value with this function will override the
        application proxy factory set with
        **QNetworkProxyFactory::setApplicationProxyFactory** , and disable the
        use of a system proxy.

        **See also** **QNetworkProxyFactory** , **applicationProxy** (),
        **QAbstractSocket::setProxy** (), and **QTcpServer::setProxy** ().
        """
        ...
    def setCapabilities(
        self, capab: PySide6.QtNetwork.QNetworkProxy.Capabilities
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#setCapabilities

        **void QNetworkProxy::setCapabilities(QNetworkProxy::Capabilities
        capabilities )**

        Sets the capabilities of this proxy to **capabilities**.

        **See also** **setType** () and **capabilities** ().
        """
        ...
    def setHeader(
        self, header: PySide6.QtNetwork.QNetworkRequest.KnownHeaders, value: Any
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#setHeader

        **[since 5.0] void
        QNetworkProxy::setHeader(QNetworkRequest::KnownHeaders header , const
        QVariant & value )**

        Sets the value of the known header **header** to be **value** ,
        overriding any previously set headers. This operation also sets the
        equivalent raw HTTP header.

        If the proxy is not of type **HttpProxy**  or **HttpCachingProxy**  this
        has no effect.

        This function was introduced in Qt 5.0.

        **See also** **QNetworkRequest::KnownHeaders** , **setRawHeader** (),
        and **header** ().
        """
        ...
    def setHostName(self, hostName: str) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#setHostName

        **void QNetworkProxy::setHostName(const QString & hostName )**

        Sets the host name of the proxy host to be **hostName**.

        **See also** **hostName** (), **setPort** (), and **port** ().
        """
        ...
    def setPassword(self, password: str) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#setPassword

        **void QNetworkProxy::setPassword(const QString & password )**

        Sets the password for proxy authentication to be **password**.

        **See also** **user** (), **setUser** (), and **password** ().
        """
        ...
    def setPort(self, port: int) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#setPort

        **void QNetworkProxy::setPort(quint16 port )**

        Sets the port of the proxy host to be **port**.

        **See also** **hostName** (), **setHostName** (), and **port** ().
        """
        ...
    def setRawHeader(
        self,
        headerName: PySide6.QtCore.QByteArray | bytes,
        value: PySide6.QtCore.QByteArray | bytes,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#setRawHeader

        **[since 5.0] void QNetworkProxy::setRawHeader(const QByteArray &
        headerName , const QByteArray & headerValue )**

        Sets the header **headerName** to be of value **headerValue**. If
        **headerName** corresponds to a known header (see
        **QNetworkRequest::KnownHeaders** ), the raw format will be parsed and
        the corresponding "cooked" header will be set as well.

        For example:

        request.setRawHeader(**QByteArray** ("Last-Modified"), **QByteArray**
        ("Sun, 06 Nov 1994 08:49:37 GMT"));

        will also set the known header LastModifiedHeader to be the
        **QDateTime**  object of the parsed date.

        **Note:** Setting the same header twice overrides the previous setting.
        To accomplish the behaviour of multiple HTTP headers of the same name,
        you should concatenate the two values, separating them with a comma
        (",") and set one single raw header.

        If the proxy is not of type **HttpProxy**  or **HttpCachingProxy**  this
        has no effect.

        This function was introduced in Qt 5.0.

        **See also** **QNetworkRequest::KnownHeaders** , **setHeader** (),
        **hasRawHeader** (), and **rawHeader** ().
        """
        ...
    def setType(self, type: PySide6.QtNetwork.QNetworkProxy.ProxyType) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#setType

        **void QNetworkProxy::setType(QNetworkProxy::ProxyType type )**

        Sets the proxy type for this instance to be **type**.

        Note that changing the type of a proxy does not change the set of
        capabilities this **QNetworkProxy**  object holds if any capabilities
        have been set with **setCapabilities** ().

        **See also** **type** () and **setCapabilities** ().
        """
        ...
    def setUser(self, userName: str) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#setUser

        **void QNetworkProxy::setUser(const QString & user )**

        Sets the user name for proxy authentication to be **user**.

        **See also** **user** (), **setPassword** (), and **password** ().
        """
        ...
    def swap(
        self,
        other: (
            PySide6.QtNetwork.QNetworkProxy | PySide6.QtNetwork.QNetworkProxy.ProxyType
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#swap

        **[since 5.0] void QNetworkProxy::swap(QNetworkProxy & other )**

        Swaps this network proxy instance with **other**. This function is very
        fast and never fails.

        This function was introduced in Qt 5.0.
        """
        ...
    def type(self) -> PySide6.QtNetwork.QNetworkProxy.ProxyType:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#type

        **QNetworkProxy::ProxyType QNetworkProxy::type() const**

        Returns the proxy type for this instance.

        **See also** **setType** ().
        """
        ...
    def user(self) -> str:
        """
        https://doc.qt.io/qt-6/qnetworkproxy.html#user

        **QString QNetworkProxy::user() const**

        Returns the user name used for authentication.

        **See also** **setUser** (), **setPassword** (), and **password** ().
        """
        ...