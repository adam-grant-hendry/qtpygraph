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

from enum import IntFlag
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtNetwork
import PySide6.QtNetworkAuth

class QOAuth1Signature:
    """
    https://doc.qt.io/qt-6/qoauth1signature.html

    **Detailed Description**

    OAuth-authenticated requests can have two sets of credentials: those passed
    via the "oauth_consumer_key" parameter and those in the "oauth_token"
    parameter. In order for the server to verify the authenticity of the request
    and prevent unauthorized access, the client needs to prove that it is the
    rightful owner of the credentials. This is accomplished using the shared-
    secret (or RSA key) part of each set of credentials.

    OAuth specifies three methods for the client to establish its rightful
    ownership of the credentials: "HMAC-SHA1", "RSA-SHA1", and "PLAINTEXT". Each
    generates a "signature" with which the request is "signed"; the first two
    use a digest of the data signed in generating this, though the last does
    not. The "RSA-SHA1" method is not supported here; it would use an RSA key
    rather than the shared-secret associated with the client credentials.
    """

    class HttpRequestMethod(IntFlag):
        Unknown: QOAuth1Signature.HttpRequestMethod = ...
        Head: QOAuth1Signature.HttpRequestMethod = ...
        Get: QOAuth1Signature.HttpRequestMethod = ...
        Put: QOAuth1Signature.HttpRequestMethod = ...
        Post: QOAuth1Signature.HttpRequestMethod = ...
        Delete: QOAuth1Signature.HttpRequestMethod = ...
        Custom: QOAuth1Signature.HttpRequestMethod = ...
    @overload
    def __init__(self, other: PySide6.QtNetworkAuth.QOAuth1Signature) -> None:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#QOAuth1Signature

        **QOAuth1Signature::QOAuth1Signature(const QUrl & url = QUrl(),
        QOAuth1Signature::HttpRequestMethod method = HttpRequestMethod::Post,
        const QMultiMap<QString, QVariant> & parameters = {})**

        Creates a QOAuth1Signature using

        * **url** as the target address
          * **method** as the HTTP method used
        to send the request
          * and the given user **parameters** to augment the
        request.
        """
        ...
    @overload
    def __init__(
        self,
        url: PySide6.QtCore.QUrl | str,
        clientSharedKey: str,
        tokenSecret: str,
        method: PySide6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod = ...,
        parameters: dict[str, Any] = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#QOAuth1Signature-1

        **QOAuth1Signature::QOAuth1Signature(const QUrl & url , const QString &
        clientSharedKey , const QString & tokenSecret ,
        QOAuth1Signature::HttpRequestMethod method = HttpRequestMethod::Post,
        const QMultiMap<QString, QVariant> & parameters = {})**

        Creates a QOAuth1Signature using

        * **url** as the target address
          * **clientSharedKey** as the user
        token used to verify the signature
          * **tokenSecret** as the negotiated
        token used to verify the signature
          * **method** as the HTTP method
        used to send the request
          * and the given user **parameters** to
        augment the request.
        """
        ...
    @overload
    def __init__(
        self,
        url: PySide6.QtCore.QUrl | str = ...,
        method: PySide6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod = ...,
        parameters: dict[str, Any] = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#QOAuth1Signature-2

        **QOAuth1Signature::QOAuth1Signature(const QOAuth1Signature & other )**

        Creates a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def addRequestBody(self, body: PySide6.QtCore.QUrlQuery) -> None:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#addRequestBody

        **void QOAuth1Signature::addRequestBody(const QUrlQuery & body )**

        Adds the request **body** to the signature. When a POST request body
        contains arguments they should be included in the signed data.
        """
        ...
    def clientSharedKey(self) -> str:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#clientSharedKey

        **QString QOAuth1Signature::clientSharedKey() const**

        Returns the user secret used to generate the signature.

        **See also** **setClientSharedKey** ().
        """
        ...
    def customMethodString(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#customMethodString

        **[since 5.13] QByteArray QOAuth1Signature::customMethodString() const**

        Returns the custom method string.

        This function was introduced in Qt 5.13.

        **See also** **setCustomMethodString** () and **httpRequestMethod** ().
        """
        ...
    def hmacSha1(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#hmacSha1

        **QByteArray QOAuth1Signature::hmacSha1() const**

        Generates the HMAC-SHA1 signature using the client shared secret and,
        where available, token secret.
        """
        ...
    def httpRequestMethod(
        self,
    ) -> PySide6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#httpRequestMethod

        **QOAuth1Signature::HttpRequestMethod
        QOAuth1Signature::httpRequestMethod() const**

        Returns the request method.

        **See also** **setHttpRequestMethod** ().
        """
        ...
    def insert(self, key: str, value: Any) -> None:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#insert

        **void QOAuth1Signature::insert(const QString & key , const QVariant &
        value )**

        Inserts a new pair **key** , **value** into the signature. When a POST
        request body contains arguments they should be included in the signed
        data.
        """
        ...
    def keys(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#keys

        **QList<QString> QOAuth1Signature::keys() const**

        Retrieves the list of keys of parameters included in the signed data.
        """
        ...
    def parameters(self) -> dict[str, Any]:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#parameters

        **QMultiMap<QString, QVariant> QOAuth1Signature::parameters() const**

        Returns the parameters.

        **See also** **setParameters** ().
        """
        ...
    @overload
    @staticmethod
    def plainText(clientSharedSecret: str, tokenSecret: str) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#plainText

        **QByteArray QOAuth1Signature::plainText() const**

        Generates the PLAINTEXT signature.
        """
        ...
    @overload
    def plainText(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#plainText-1

        **[static] QByteArray QOAuth1Signature::plainText(const QString &
        clientSharedKey , const QString & tokenSecret )**

        Generates a PLAINTEXT signature from the client secret
        **clientSharedKey** and the token secret **tokenSecret**.
        """
        ...
    def rsaSha1(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#rsaSha1

        **QByteArray QOAuth1Signature::rsaSha1() const**

        Generates the RSA-SHA1 signature.

        **Note:** Currently this method is not supported.
        """
        ...
    def setClientSharedKey(self, secret: str) -> None:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#setClientSharedKey

        **void QOAuth1Signature::setClientSharedKey(const QString & secret )**

        Sets **secret** as the user secret used to generate the signature.

        **See also** **clientSharedKey** ().
        """
        ...
    def setCustomMethodString(self, verb: PySide6.QtCore.QByteArray | bytes) -> None:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#setCustomMethodString

        **[since 5.13] void QOAuth1Signature::setCustomMethodString(const
        QByteArray & verb )**

        Sets a custom request method. Will set the **httpRequestMethod**  to
        **QOAuth1Signature::HttpRequestMethod::Custom**  and store the **verb**
        to use it for the generation of the signature.

        **Note:** Using this method is required when working with custom verbs.
        Setting only the request method will fail, as the signure needs to know
        the actual verb.

        This function was introduced in Qt 5.13.

        **See also** **customMethodString** (), **setHttpRequestMethod** (), and
        **HttpRequestMethod** .
        """
        ...
    def setHttpRequestMethod(
        self, method: PySide6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod
    ) -> None:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#setHttpRequestMethod

        **void QOAuth1Signature::setHttpRequestMethod(QOAuth1Signature::HttpRequ
        estMethod method )**

        Sets the request **method**.

        **See also** **httpRequestMethod** ().
        """
        ...
    def setParameters(self, parameters: dict[str, Any]) -> None:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#setParameters

        **void QOAuth1Signature::setParameters(const QMultiMap<QString,
        QVariant> & parameters )**

        Sets the **parameters**.

        **See also** **parameters** ().
        """
        ...
    def setTokenSecret(self, secret: str) -> None:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#setTokenSecret

        **void QOAuth1Signature::setTokenSecret(const QString & secret )**

        Sets **secret** as the negotiated secret used to generate the signature.

        **See also** **tokenSecret** ().
        """
        ...
    def setUrl(self, url: PySide6.QtCore.QUrl | str) -> None:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#setUrl

        **void QOAuth1Signature::setUrl(const QUrl & url )**

        Sets the URL to **url**.

        **See also** **url** ().
        """
        ...
    def swap(self, other: PySide6.QtNetworkAuth.QOAuth1Signature) -> None:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#swap

        **void QOAuth1Signature::swap(QOAuth1Signature & other )**

        Swaps signature **other** with this signature. This operation is very
        fast and never fails.
        """
        ...
    def take(self, key: str) -> Any:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#take

        **QVariant QOAuth1Signature::take(const QString & key )**

        Removes **key** and any associated value from the signed data.
        """
        ...
    def tokenSecret(self) -> str:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#tokenSecret

        **QString QOAuth1Signature::tokenSecret() const**

        Returns the negotiated secret used to generate the signature.

        **See also** **setTokenSecret** ().
        """
        ...
    def url(self) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#url

        **QUrl QOAuth1Signature::url() const**

        Returns the URL.

        **See also** **setUrl** ().
        """
        ...
    def value(self, key: str, defaultValue: Any = ...) -> Any:
        """
        https://doc.qt.io/qt-6/qoauth1signature.html#value

        **QVariant QOAuth1Signature::value(const QString & key , const QVariant
        & defaultValue = QVariant()) const**

        Returns the value associated with **key** , if present in the signed
        data, otherwise **defaultValue**.
        """
        ...
