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

from typing import Any, overload

import PySide6.QtCore
import PySide6.QtNetwork

class QAuthenticator:
    """
    https://doc.qt.io/qt-6/qauthenticator.html

    **Detailed Description**

    The QAuthenticator class is usually used in the **authenticationRequired**
    () and **proxyAuthenticationRequired** () signals of
    **QNetworkAccessManager**  and **QAbstractSocket** . The class provides a
    way to pass back the required authentication information to the socket when
    accessing services that require authentication.

    QAuthenticator supports the following authentication methods:

    * Basic
      * NTLM version 2
      * Digest-MD5
      * SPNEGO/Negotiate

    **Options**

    In addition to the username and password required for authentication, a
    QAuthenticator object can also contain additional options. The **options**
    () function can be used to query incoming options sent by the server; the
    **setOption** () function can be used to set outgoing options, to be
    processed by the authenticator calculation. The options accepted and
    provided depend on the authentication type (see method()).

    The following tables list known incoming options as well as accepted
    outgoing options. The list of incoming options is not exhaustive, since
    servers may include additional information at any time. The list of outgoing
    options is exhaustive, however, and no unknown options will be treated or
    sent back to the server.

    **Basic**

    OptionDirectionTypeDescription
    `realm`Incoming**QString** Contains the
    realm of the authentication, the same as **realm** ()

    The Basic authentication mechanism supports no outgoing options.

    **NTLM version 2**

    The NTLM authentication mechanism currently supports no incoming or outgoing
    options. On Windows, if no **user** has been set, domain\\user credentials
    will be searched for on the local system to enable Single-Sign-On
    functionality.

    **Digest-MD5**

    OptionDirectionTypeDescription
    `realm`Incoming**QString** Contains the
    realm of the authentication, the same as **realm** ()

    The Digest-MD5 authentication mechanism supports no outgoing options.

    **SPNEGO/Negotiate**

    This authentication mechanism currently supports no incoming or outgoing
    options.

    **See also** **QSslSocket** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qauthenticator.html#QAuthenticator

        **QAuthenticator::QAuthenticator()**

        Constructs an empty authentication object.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtNetwork.QAuthenticator) -> None:
        """
        https://doc.qt.io/qt-6/qauthenticator.html#QAuthenticator-1

        **QAuthenticator::QAuthenticator(const QAuthenticator & other )**

        Constructs a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def isNull(self) -> bool:
        """
        https://doc.qt.io/qt-6/qauthenticator.html#isNull

        **bool QAuthenticator::isNull() const**

        Returns `true` if the object has not been initialized. Returns `false`
        if non-const member functions have been called, or the content was
        constructed or copied from another initialized **QAuthenticator**
        object.
        """
        ...
    def option(self, opt: str) -> Any:
        """
        https://doc.qt.io/qt-6/qauthenticator.html#option

        **QVariant QAuthenticator::option(const QString & opt ) const**

        Returns the value related to option **opt** if it was set by the server.
        See the **Options section**  for more information on incoming options.
        If option **opt** isn't found, an invalid **QVariant**  will be
        returned.

        **See also** **setOption** (), **options** (), and **QAuthenticator
        options** .
        """
        ...
    def options(self) -> dict[str, Any]:
        """
        https://doc.qt.io/qt-6/qauthenticator.html#options

        **QVariantHash QAuthenticator::options() const**

        Returns all incoming options set in this **QAuthenticator**  object by
        parsing the server reply. See the **Options section**  for more
        information on incoming options.

        **See also** **option** () and **QAuthenticator options** .
        """
        ...
    def password(self) -> str:
        """
        https://doc.qt.io/qt-6/qauthenticator.html#password

        **QString QAuthenticator::password() const**

        Returns the password used for authentication.

        **See also** **setPassword** ().
        """
        ...
    def realm(self) -> str:
        """
        https://doc.qt.io/qt-6/qauthenticator.html#realm

        **QString QAuthenticator::realm() const**

        Returns the realm requiring authentication.
        """
        ...
    def setOption(self, opt: str, value: Any) -> None:
        """
        https://doc.qt.io/qt-6/qauthenticator.html#setOption

        **void QAuthenticator::setOption(const QString & opt , const QVariant &
        value )**

        Sets the outgoing option **opt** to value **value**. See the **Options
        section**  for more information on outgoing options.

        **See also** **options** (), **option** (), and **QAuthenticator
        options** .
        """
        ...
    def setPassword(self, password: str) -> None:
        """
        https://doc.qt.io/qt-6/qauthenticator.html#setPassword

        **void QAuthenticator::setPassword(const QString & password )**

        Sets the **password** used for authentication.

        **See also** **password** () and
        **QNetworkAccessManager::authenticationRequired** ().
        """
        ...
    def setRealm(self, realm: str) -> None:
        """
        https://doc.qt.io/qt-6/qauthenticator.html#realm

        **QString QAuthenticator::realm() const**

        Returns the realm requiring authentication.
        """
        ...
    def setUser(self, user: str) -> None:
        """
        https://doc.qt.io/qt-6/qauthenticator.html#setUser

        **void QAuthenticator::setUser(const QString & user )**

        Sets the **user** used for authentication.

        **See also** **user** () and
        **QNetworkAccessManager::authenticationRequired** ().
        """
        ...
    def user(self) -> str:
        """
        https://doc.qt.io/qt-6/qauthenticator.html#user

        **QString QAuthenticator::user() const**

        Returns the user used for authentication.

        **See also** **setUser** ().
        """
        ...
