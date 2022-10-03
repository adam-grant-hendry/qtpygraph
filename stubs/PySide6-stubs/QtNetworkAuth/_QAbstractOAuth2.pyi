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
PySide6.QtNetworkAuth, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import Any, overload

import PySide6.QtCore
import PySide6.QtNetwork
import PySide6.QtNetworkAuth

class QAbstractOAuth2(PySide6.QtNetworkAuth.QAbstractOAuth):
    """
    https://doc.qt.io/qt-6/qabstractoauth2.html

    **Detailed Description**

    The class defines the basic interface of the OAuth 2 authentication classes.
    By inheriting this class, you can create custom authentication methods using
    the OAuth 2 standard for different web services.

    A description of how OAuth 2 works can be found in: **The OAuth 2.0
    Authorization Framework**
    """

    @overload
    def __init__(
        self,
        manager: PySide6.QtNetwork.QNetworkAccessManager,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#QAbstractOAuth2

        **QAbstractOAuth2::QAbstractOAuth2(QObject * parent = nullptr)**

        Constructs a QAbstractOAuth2 object using **parent** as parent.
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#QAbstractOAuth2-1

        **QAbstractOAuth2::QAbstractOAuth2(QNetworkAccessManager * manager ,
        QObject * parent = nullptr)**

        Constructs a QAbstractOAuth2 object using **parent** as parent and sets
        **manager** as the network access manager.
        """
        ...
    def clientIdentifierSharedKey(self) -> str:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#clientIdentifierSharedKey-
        prop

        **clientIdentifierSharedKey : QString**

        This property holds the client shared key used as a password if the
        server requires authentication to request the token.

        **Access functions:**

        QString **clientIdentifierSharedKey** () const
        void
        **setClientIdentifierSharedKey** (const QString &
        **clientIdentifierSharedKey** )

        **Notifier signal:**

        void **clientIdentifierSharedKeyChanged** (const QString &
        **clientIdentifierSharedKey** )
        """
        ...
    def createAuthenticatedUrl(
        self, url: PySide6.QtCore.QUrl | str, parameters: dict[str, Any] = ...
    ) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#createAuthenticatedUrl

        **[virtual invokable] QUrl QAbstractOAuth2::createAuthenticatedUrl(const
        QUrl & url , const QVariantMap & parameters = QVariantMap())**

        The returned URL is based on **url** , combining it with the given
        **parameters** and the access token.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def deleteResource(
        self, url: PySide6.QtCore.QUrl | str, parameters: dict[str, Any] = ...
    ) -> PySide6.QtNetwork.QNetworkReply:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#deleteResource

        **[override virtual invokable] QNetworkReply
        *QAbstractOAuth2::deleteResource(const QUrl & url , const QVariantMap &
        parameters = QVariantMap())**

        Reimplements: **QAbstractOAuth::deleteResource** (const QUrl &url, const
        QVariantMap &parameters).

        Sends an authenticated DELETE request and returns a new
        **QNetworkReply** . The **url** and **parameters** are used to create
        the request.

        **See also**  : **Hypertext Transfer Protocol -- HTTP/1.1: DELETE**

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def expirationAt(self) -> PySide6.QtCore.QDateTime: ...
    def get(
        self, url: PySide6.QtCore.QUrl | str, parameters: dict[str, Any] = ...
    ) -> PySide6.QtNetwork.QNetworkReply:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#get

        **[override virtual invokable] QNetworkReply *QAbstractOAuth2::get(const
        QUrl & url , const QVariantMap & parameters = QVariantMap())**

        Reimplements: **QAbstractOAuth::get** (const QUrl &url, const
        QVariantMap &parameters).

        Sends an authenticated GET request and returns a new **QNetworkReply** .
        The **url** and **parameters** are used to create the request.

        **See also**  : **Hypertext Transfer Protocol -- HTTP/1.1: GET**

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def head(
        self, url: PySide6.QtCore.QUrl | str, parameters: dict[str, Any] = ...
    ) -> PySide6.QtNetwork.QNetworkReply:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#head

        **[override virtual invokable] QNetworkReply
        *QAbstractOAuth2::head(const QUrl & url , const QVariantMap & parameters
        = QVariantMap())**

        Reimplements: **QAbstractOAuth::head** (const QUrl &url, const
        QVariantMap &parameters).

        Sends an authenticated HEAD request and returns a new **QNetworkReply**
        . The **url** and **parameters** are used to create the request.

        **See also**  : **Hypertext Transfer Protocol -- HTTP/1.1: HEAD**

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    @overload
    def post(
        self,
        url: PySide6.QtCore.QUrl | str,
        data: PySide6.QtCore.QByteArray | bytes,
    ) -> PySide6.QtNetwork.QNetworkReply:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#post

        **[override virtual invokable] QNetworkReply
        *QAbstractOAuth2::post(const QUrl & url , const QVariantMap & parameters
        = QVariantMap())**

        Reimplements: **QAbstractOAuth::post** (const QUrl &url, const
        QVariantMap &parameters).

        Sends an authenticated POST request and returns a new **QNetworkReply**
        . The **url** and **parameters** are used to create the request.

        **See also**  : **Hypertext Transfer Protocol -- HTTP/1.1: POST**

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    @overload
    def post(
        self,
        url: PySide6.QtCore.QUrl | str,
        multiPart: PySide6.QtNetwork.QHttpMultiPart,
    ) -> PySide6.QtNetwork.QNetworkReply:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#post-1

        **[virtual invokable, since 5.10] QNetworkReply
        *QAbstractOAuth2::post(const QUrl & url , const QByteArray & data )**

        This is an overloaded function.

        Sends an authenticated POST request and returns a new **QNetworkReply**
        . The **url** and **data** are used to create the request.

        {Hypertext Transfer Protocol -- HTTP/1.1: POST}

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.10.

        **See also** **post** () and
        <https://tools.ietf.org/html/rfc2616#section-9.6>.
        """
        ...
    @overload
    def post(
        self, url: PySide6.QtCore.QUrl | str, parameters: dict[str, Any] = ...
    ) -> PySide6.QtNetwork.QNetworkReply:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#post-2

        **[virtual invokable, since 5.10] QNetworkReply
        *QAbstractOAuth2::post(const QUrl & url , QHttpMultiPart * multiPart )**

        This is an overloaded function.

        Sends an authenticated POST request and returns a new **QNetworkReply**
        . The **url** and **multiPart** are used to create the request.

        {Hypertext Transfer Protocol -- HTTP/1.1: POST}

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.10.

        **See also** **post** (), **QHttpMultiPart** , and
        <https://tools.ietf.org/html/rfc2616#section-9.6>.
        """
        ...
    def prepareRequest(
        self,
        request: PySide6.QtNetwork.QNetworkRequest,
        verb: PySide6.QtCore.QByteArray | bytes,
        body: PySide6.QtCore.QByteArray | bytes = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#prepareRequest

        **[override virtual] void
        QAbstractOAuth2::prepareRequest(QNetworkRequest * request , const
        QByteArray & verb , const QByteArray & body = QByteArray())**

        Reimplements: **QAbstractOAuth::prepareRequest** (QNetworkRequest
        *request, const QByteArray &verb, const QByteArray &body).
        """
        ...
    @overload
    def put(
        self,
        url: PySide6.QtCore.QUrl | str,
        data: PySide6.QtCore.QByteArray | bytes,
    ) -> PySide6.QtNetwork.QNetworkReply:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#put

        **[override virtual invokable] QNetworkReply *QAbstractOAuth2::put(const
        QUrl & url , const QVariantMap & parameters = QVariantMap())**

        Reimplements: **QAbstractOAuth::put** (const QUrl &url, const
        QVariantMap &parameters).

        Sends an authenticated PUT request and returns a new **QNetworkReply** .
        The **url** and **parameters** are used to create the request.

        **See also**  : **Hypertext Transfer Protocol -- HTTP/1.1: PUT**

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    @overload
    def put(
        self,
        url: PySide6.QtCore.QUrl | str,
        multiPart: PySide6.QtNetwork.QHttpMultiPart,
    ) -> PySide6.QtNetwork.QNetworkReply:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#put-1

        **[virtual invokable, since 5.10] QNetworkReply
        *QAbstractOAuth2::put(const QUrl & url , const QByteArray & data )**

        This is an overloaded function.

        Sends an authenticated PUT request and returns a new **QNetworkReply** .
        The **url** and **data** are used to create the request.

        {Hypertext Transfer Protocol -- HTTP/1.1: PUT}

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.10.

        **See also** **put** () and
        <https://tools.ietf.org/html/rfc2616#section-9.6>.
        """
        ...
    @overload
    def put(
        self, url: PySide6.QtCore.QUrl | str, parameters: dict[str, Any] = ...
    ) -> PySide6.QtNetwork.QNetworkReply:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#put-2

        **[virtual invokable, since 5.10] QNetworkReply
        *QAbstractOAuth2::put(const QUrl & url , QHttpMultiPart * multiPart )**

        This is an overloaded function.

        Sends an authenticated PUT request and returns a new **QNetworkReply** .
        The **url** and **multiPart** are used to create the request.

        {Hypertext Transfer Protocol -- HTTP/1.1: PUT}

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.10.

        **See also** **put** (), **QHttpMultiPart** , and
        <https://tools.ietf.org/html/rfc2616#section-9.6>.
        """
        ...
    def refreshToken(self) -> str:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#refreshToken

        **QString QAbstractOAuth2::refreshToken() const**

        Gets the current refresh token.

        Refresh tokens usually have longer lifespans than access tokens, so it
        makes sense to save them for later use.

        Returns the current refresh token or an empty string, if there is no
        refresh token available.

        **Note:** Getter function for property refreshToken.

        **See also** **setRefreshToken** ().
        """
        ...
    def responseType(self) -> str:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#responseType

        **QString QAbstractOAuth2::responseType() const**

        Returns the **response_type**  used.
        """
        ...
    def scope(self) -> str:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#scope-prop

        **scope : QString**

        This property holds the desired scope which defines the permissions
        requested by the client.

        **Access functions:**

        QString **scope** () const
        void **setScope** (const QString &
        **scope** )

        **Notifier signal:**

        void **scopeChanged** (const QString & **scope** )
        """
        ...
    def setClientIdentifierSharedKey(self, clientIdentifierSharedKey: str) -> None:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#clientIdentifierSharedKey-
        prop

        **clientIdentifierSharedKey : QString**

        This property holds the client shared key used as a password if the
        server requires authentication to request the token.

        **Access functions:**

        QString **clientIdentifierSharedKey** () const
        void
        **setClientIdentifierSharedKey** (const QString &
        **clientIdentifierSharedKey** )

        **Notifier signal:**

        void **clientIdentifierSharedKeyChanged** (const QString &
        **clientIdentifierSharedKey** )
        """
        ...
    def setRefreshToken(self, refreshToken: str) -> None:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#setRefreshToken

        **void QAbstractOAuth2::setRefreshToken(const QString & refreshToken )**

        Sets the new refresh token **refreshToken** to be used.

        A custom refresh token can be used to refresh the access token via this
        method and then the access token can be refreshed via
        **QOAuth2AuthorizationCodeFlow::refreshAccessToken** ().

        **Note:** Setter function for property **refreshToken** .

        **See also** **refreshToken** ().
        """
        ...
    def setResponseType(self, responseType: str) -> None:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#responseType

        **QString QAbstractOAuth2::responseType() const**

        Returns the **response_type**  used.
        """
        ...
    def setScope(self, scope: str) -> None:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#scope-prop

        **scope : QString**

        This property holds the desired scope which defines the permissions
        requested by the client.

        **Access functions:**

        QString **scope** () const
        void **setScope** (const QString &
        **scope** )

        **Notifier signal:**

        void **scopeChanged** (const QString & **scope** )
        """
        ...
    def setState(self, state: str) -> None:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#state-prop

        **state : QString**

        This property holds the string sent to the server during authentication.
        The state is used to identify and validate the request when the callback
        is received.

        **Access functions:**

        QString **state** () const
        void **setState** (const QString &
        **state** )

        **Notifier signal:**

        void **stateChanged** (const QString & **state** )
        """
        ...
    def setUserAgent(self, userAgent: str) -> None:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#userAgent-prop

        **userAgent : QString**

        This property holds the User-Agent header used to create the network
        requests.

        The default value is "QtOAuth/1.0 (+https://www.qt.io)".

        **Access functions:**

        QString **userAgent** () const
        void **setUserAgent** (const QString &
        **userAgent** )

        **Notifier signal:**

        void **userAgentChanged** (const QString & **userAgent** )

        **Member Function Documentation**
        """
        ...
    def state(self) -> str:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#state-prop

        **state : QString**

        This property holds the string sent to the server during authentication.
        The state is used to identify and validate the request when the callback
        is received.

        **Access functions:**

        QString **state** () const
        void **setState** (const QString &
        **state** )

        **Notifier signal:**

        void **stateChanged** (const QString & **state** )
        """
        ...
    def userAgent(self) -> str:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#userAgent-prop

        **userAgent : QString**

        This property holds the User-Agent header used to create the network
        requests.

        The default value is "QtOAuth/1.0 (+https://www.qt.io)".

        **Access functions:**

        QString **userAgent** () const
        void **setUserAgent** (const QString &
        **userAgent** )

        **Notifier signal:**

        void **userAgentChanged** (const QString & **userAgent** )

        **Member Function Documentation**
        """
        ...
    @property
    def authorizationCallbackReceived(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#authorizationCallbackReceive
        d

        **[signal] void QAbstractOAuth2::authorizationCallbackReceived(const
        QVariantMap & data )**

        Signal emitted when the reply server receives the authorization callback
        from the server: **data** contains the values received from the server.
        """
        ...
    @property
    def clientIdentifierSharedKeyChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def error(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qabstractoauth2.html#error

        **[signal] void QAbstractOAuth2::error(const QString & error , const
        QString & errorDescription , const QUrl & uri )**

        Signal emitted when the server responds to the request with an error:
        **error** is the name of the error; **errorDescription** describes the
        error and **uri** is an optional URI containing more information about
        the error.
        """
        ...
    @property
    def expirationAtChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def scopeChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def stateChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def userAgentChanged(self) -> PySide6.QtCore.SignalInstance: ...