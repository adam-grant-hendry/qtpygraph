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
from typing import overload

import PySide6.QtCore
import PySide6.QtNetwork

class QNetworkProxyQuery:
    """
    https://doc.qt.io/qt-6/qnetworkproxyquery.html

    **Detailed Description**

    QNetworkProxyQuery holds the details of a socket being created or request
    being made. It is used by **QNetworkProxy**  and **QNetworkProxyFactory**
    to allow applications to have a more fine-grained control over which proxy
    servers are used, depending on the details of the query. This allows an
    application to apply different settings, according to the protocol or
    destination hostname, for instance.

    QNetworkProxyQuery supports the following criteria for selecting the proxy:

    * the type of query
      * the local port number to use
      * the destination
    host name
      * the destination port number
      * the protocol name, such as
    "http" or "ftp"
      * the URL being requested

    The destination host name is the host in the connection in the case of
    outgoing connection sockets. It is the `hostName` parameter passed to
    **QTcpSocket::connectToHost** () or the host component of a URL requested
    with **QNetworkRequest** .

    The destination port number is the requested port to connect to in the case
    of outgoing sockets, while the local port number is the port the socket
    wishes to use locally before attempting the external connection. In most
    cases, the local port number is used by listening sockets only
    (**QTcpSocket** ) or by datagram sockets (**QUdpSocket** ).

    The protocol name is an arbitrary string that indicates the type of
    connection being attempted. For example, it can match the scheme of a URL,
    like "http", "https" and "ftp". In most cases, the proxy selection will not
    change depending on the protocol, but this information is provided in case a
    better choice can be made, like choosing an caching HTTP proxy for HTTP-
    based connections, but a more powerful SOCKSv5 proxy for all others.

    Some of the criteria may not make sense in all of the types of query. The
    following table lists the criteria that are most commonly used, according to
    the type of query.

    Query typeDescription
    **TcpSocket** Normal sockets requesting a connection
    to a remote server, like **QTcpSocket** . The peer hostname and peer port
    match the values passed to **QTcpSocket::connectToHost** (). The local port
    is usually -1, indicating the socket has no preference in which port should
    be used. The URL component is not used.
    **UdpSocket** Datagram-based
    sockets, which can both send and receive. The local port, remote host or
    remote port fields can all be used or be left unused, depending on the
    characteristics of the socket. The URL component is not used.
    **SctpSocket** Message-oriented sockets requesting a connection to a remote
    server. The peer hostname and peer port match the values passed to
    **QSctpSocket::connectToHost** (). The local port is usually -1, indicating
    the socket has no preference in which port should be used. The URL component
    is not used.
    **TcpServer** Passive server sockets that listen on a port
    and await incoming connections from the network. Normally, only the local
    port is used, but the remote address could be used in specific
    circumstances, for example to indicate which remote host a connection is
    expected from. The URL component is not used.
    **UrlRequest** A more high-
    level request, such as those coming from **QNetworkAccessManager** . These
    requests will inevitably use an outgoing TCP socket, but the this query type
    is provided to indicate that more detailed information is present in the URL
    component. For ease of implementation, the URL's host and port are set as
    the destination address.
    **SctpServer** Passive server sockets that listen
    on an SCTP port and await incoming connections from the network. Normally,
    only the local port is used, but the remote address could be used in
    specific circumstances, for example to indicate which remote host a
    connection is expected from. The URL component is not used.

    It should be noted that any of the criteria may be missing or unknown (an
    empty **QString**  for the hostname or protocol name, -1 for the port
    numbers). If that happens, the functions executing the query should make
    their best guess or apply some implementation-defined default values.

    **See also** **QNetworkProxy** , **QNetworkProxyFactory** ,
    **QNetworkAccessManager** , and **QAbstractSocket::setProxy** ().
    """

    TcpSocket: QNetworkProxyQuery.QueryType = ...
    UdpSocket: QNetworkProxyQuery.QueryType = ...
    SctpSocket: QNetworkProxyQuery.QueryType = ...
    TcpServer: QNetworkProxyQuery.QueryType = ...
    UrlRequest: QNetworkProxyQuery.QueryType = ...
    SctpServer: QNetworkProxyQuery.QueryType = ...

    class QueryType(IntFlag):
        TcpSocket: QNetworkProxyQuery.QueryType = ...
        UdpSocket: QNetworkProxyQuery.QueryType = ...
        SctpSocket: QNetworkProxyQuery.QueryType = ...
        TcpServer: QNetworkProxyQuery.QueryType = ...
        UrlRequest: QNetworkProxyQuery.QueryType = ...
        SctpServer: QNetworkProxyQuery.QueryType = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#QNetworkProxyQuery

        **QNetworkProxyQuery::QNetworkProxyQuery()**

        Constructs a default QNetworkProxyQuery object. By default, the query
        type will be **QNetworkProxyQuery::TcpSocket** .
        """
        ...
    @overload
    def __init__(
        self,
        bindPort: int,
        protocolTag: str = ...,
        queryType: PySide6.QtNetwork.QNetworkProxyQuery.QueryType = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#QNetworkProxyQuery-1

        **QNetworkProxyQuery::QNetworkProxyQuery(const QUrl & requestUrl ,
        QNetworkProxyQuery::QueryType queryType = UrlRequest)**

        Constructs a QNetworkProxyQuery with the URL **requestUrl** and sets the
        query type to **queryType**.

        **See also** **protocolTag** (), **peerHostName** (), and **peerPort**
        ().
        """
        ...
    @overload
    def __init__(
        self,
        hostname: str,
        port: int,
        protocolTag: str = ...,
        queryType: PySide6.QtNetwork.QNetworkProxyQuery.QueryType = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#QNetworkProxyQuery-2

        **QNetworkProxyQuery::QNetworkProxyQuery(const QString & hostname , int
        port , const QString & protocolTag = QString(),
        QNetworkProxyQuery::QueryType queryType = TcpSocket)**

        Constructs a QNetworkProxyQuery of type **queryType** and sets the
        protocol tag to be **protocolTag**. This constructor is suitable for
        **QNetworkProxyQuery::TcpSocket**  queries, because it sets the peer
        hostname to **hostname** and the peer's port number to **port**.
        """
        ...
    @overload
    def __init__(
        self,
        other: PySide6.QtNetwork.QNetworkProxyQuery | PySide6.QtCore.QUrl | int,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#QNetworkProxyQuery-3

        **QNetworkProxyQuery::QNetworkProxyQuery(quint16 bindPort , const
        QString & protocolTag = QString(), QNetworkProxyQuery::QueryType
        queryType = TcpServer)**

        Constructs a QNetworkProxyQuery of type **queryType** and sets the
        protocol tag to be **protocolTag**. This constructor is suitable for
        **QNetworkProxyQuery::TcpSocket**  queries because it sets the local
        port number to **bindPort**.

        Note that **bindPort** is of type quint16 to indicate the exact port
        number that is requested. The value of -1 (unknown) is not allowed in
        this context.

        **See also** **localPort** ().
        """
        ...
    @overload
    def __init__(
        self,
        requestUrl: PySide6.QtCore.QUrl | str,
        queryType: PySide6.QtNetwork.QNetworkProxyQuery.QueryType = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#QNetworkProxyQuery-4

        **QNetworkProxyQuery::QNetworkProxyQuery(const QNetworkProxyQuery &
        other )**

        Constructs a QNetworkProxyQuery object that is a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def localPort(self) -> int:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#localPort

        **int QNetworkProxyQuery::localPort() const**

        Returns the port number of the socket that will accept incoming packets
        from remote servers or -1 if the port is not known.

        **See also** **peerPort** (), **peerHostName** (), and **setLocalPort**
        ().
        """
        ...
    def peerHostName(self) -> str:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#peerHostName

        **QString QNetworkProxyQuery::peerHostName() const**

        Returns the host name or IP address being of the outgoing connection
        being requested, or an empty string if the remote hostname is not known.

        If the query type is **QNetworkProxyQuery::UrlRequest** , this function
        returns the host component of the URL being requested.

        **See also** **peerPort** (), **localPort** (), and **setPeerHostName**
        ().
        """
        ...
    def peerPort(self) -> int:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#peerPort

        **int QNetworkProxyQuery::peerPort() const**

        Returns the port number for the outgoing request or -1 if the port
        number is not known.

        If the query type is **QNetworkProxyQuery::UrlRequest** , this function
        returns the port number of the URL being requested. In general,
        frameworks will fill in the port number from their default values.

        **See also** **peerHostName** (), **localPort** (), and **setPeerPort**
        ().
        """
        ...
    def protocolTag(self) -> str:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#protocolTag

        **QString QNetworkProxyQuery::protocolTag() const**

        Returns the protocol tag for this **QNetworkProxyQuery**  object, or an
        empty **QString**  in case the protocol tag is unknown.

        In the case of queries of type **QNetworkProxyQuery::UrlRequest** , this
        function returns the value of the scheme component of the URL.

        **See also** **setProtocolTag** () and **url** ().
        """
        ...
    def queryType(self) -> PySide6.QtNetwork.QNetworkProxyQuery.QueryType:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#queryType

        **QNetworkProxyQuery::QueryType QNetworkProxyQuery::queryType() const**

        Returns the query type.

        **See also** **setQueryType** ().
        """
        ...
    def setLocalPort(self, port: int) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#setLocalPort

        **void QNetworkProxyQuery::setLocalPort(int port )**

        Sets the port number that the socket wishes to use locally to accept
        incoming packets from remote servers to **port**. The local port is most
        often used with the **QNetworkProxyQuery::TcpServer**  and
        **QNetworkProxyQuery::UdpSocket**  query types.

        Valid values are 0 to 65535 (with 0 indicating that any port number will
        be acceptable) or -1, which means the local port number is unknown or
        not applicable.

        In some circumstances, for special protocols, it's the local port number
        can also be used with a query of type **QNetworkProxyQuery::TcpSocket**
        . When that happens, the socket is indicating it wishes to use the port
        number **port** when connecting to a remote host.

        **See also** **localPort** (), **setPeerPort** (), and
        **setPeerHostName** ().
        """
        ...
    def setPeerHostName(self, hostname: str) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#setPeerHostName

        **void QNetworkProxyQuery::setPeerHostName(const QString & hostname )**

        Sets the hostname of the outgoing connection being requested to
        **hostname**. An empty hostname can be used to indicate that the remote
        host is unknown.

        The peer host name can also be used to indicate the expected source
        address of an incoming connection in the case of
        **QNetworkProxyQuery::UdpSocket**  or **QNetworkProxyQuery::TcpServer**
        query types.

        **See also** **peerHostName** (), **setPeerPort** (), and
        **setLocalPort** ().
        """
        ...
    def setPeerPort(self, port: int) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#setPeerPort

        **void QNetworkProxyQuery::setPeerPort(int port )**

        Sets the requested port number for the outgoing connection to be
        **port**. Valid values are 1 to 65535, or -1 to indicate that the remote
        port number is unknown.

        The peer port number can also be used to indicate the expected port
        number of an incoming connection in the case of
        **QNetworkProxyQuery::UdpSocket**  or **QNetworkProxyQuery::TcpServer**
        query types.

        **See also** **peerPort** (), **setPeerHostName** (), and
        **setLocalPort** ().
        """
        ...
    def setProtocolTag(self, protocolTag: str) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#setProtocolTag

        **void QNetworkProxyQuery::setProtocolTag(const QString & protocolTag
        )**

        Sets the protocol tag for this **QNetworkProxyQuery**  object to be
        **protocolTag**.

        The protocol tag is an arbitrary string that indicates which protocol is
        being talked over the socket, such as "http", "xmpp", "telnet", etc. The
        protocol tag is used by the backend to return a request that is more
        specific to the protocol in question: for example, a HTTP connection
        could be use a caching HTTP proxy server, while all other connections
        use a more powerful SOCKSv5 proxy server.

        **See also** **protocolTag** ().
        """
        ...
    def setQueryType(self, type: PySide6.QtNetwork.QNetworkProxyQuery.QueryType) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#setQueryType

        **void QNetworkProxyQuery::setQueryType(QNetworkProxyQuery::QueryType
        type )**

        Sets the query type of this object to be **type**.

        **See also** **queryType** ().
        """
        ...
    def setUrl(self, url: PySide6.QtCore.QUrl | str) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#setUrl

        **void QNetworkProxyQuery::setUrl(const QUrl & url )**

        Sets the URL component of this **QNetworkProxyQuery**  object to be
        **url**. Setting the URL will also set the protocol tag, the remote host
        name and port number. This is done so as to facilitate the
        implementation of the code that determines the proxy server to be used.

        **See also** **url** (), **peerHostName** (), and **peerPort** ().
        """
        ...
    def swap(
        self,
        other: PySide6.QtNetwork.QNetworkProxyQuery | PySide6.QtCore.QUrl | int,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#swap

        **[since 5.0] void QNetworkProxyQuery::swap(QNetworkProxyQuery & other
        )**

        Swaps this network proxy query instance with **other**. This function is
        very fast and never fails.

        This function was introduced in Qt 5.0.
        """
        ...
    def url(self) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qnetworkproxyquery.html#url

        **QUrl QNetworkProxyQuery::url() const**

        Returns the URL component of this **QNetworkProxyQuery**  object in case
        of a query of type **QNetworkProxyQuery::UrlRequest** .

        **See also** **setUrl** ().
        """
        ...