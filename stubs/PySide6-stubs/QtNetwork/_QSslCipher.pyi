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

from typing import overload

import PySide6.QtCore
import PySide6.QtNetwork

class QSslCipher:
    """
    https://doc.qt.io/qt-6/qsslcipher.html

    **Detailed Description**

    QSslCipher stores information about one cryptographic cipher. It is most
    commonly used with **QSslSocket** , either for configuring which ciphers the
    socket can use, or for displaying the socket's ciphers to the user.

    **See also** **QSslSocket**  and **QSslKey** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#QSslCipher

        **QSslCipher::QSslCipher()**

        Constructs an empty QSslCipher object.
        """
        ...
    @overload
    def __init__(self, name: str) -> None:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#QSslCipher-1

        **[since 5.3] QSslCipher::QSslCipher(const QString & name )**

        Constructs a QSslCipher object for the cipher determined by **name**.
        The constructor accepts only supported ciphers (i.e., the **name** must
        identify a cipher in the list of ciphers returned by
        QSslSocket::supportedCiphers()).

        You can call **isNull** () after construction to check if **name**
        correctly identified a supported cipher.

        This function was introduced in Qt 5.3.
        """
        ...
    @overload
    def __init__(self, name: str, protocol: PySide6.QtNetwork.QSsl.SslProtocol) -> None:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#QSslCipher-2

        **QSslCipher::QSslCipher(const QString & name , QSsl::SslProtocol
        protocol )**

        Constructs a QSslCipher object for the cipher determined by **name** and
        **protocol**. The constructor accepts only supported ciphers (i.e., the
        **name** and **protocol** must identify a cipher in the list of ciphers
        returned by QSslSocket::supportedCiphers()).

        You can call **isNull** () after construction to check if **name** and
        **protocol** correctly identified a supported cipher.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtNetwork.QSslCipher) -> None:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#QSslCipher-3

        **QSslCipher::QSslCipher(const QSslCipher & other )**

        Constructs an identical copy of the **other** cipher.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def authenticationMethod(self) -> str:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#authenticationMethod

        **QString QSslCipher::authenticationMethod() const**

        Returns the cipher's authentication method as a **QString** .
        """
        ...
    def encryptionMethod(self) -> str:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#encryptionMethod

        **QString QSslCipher::encryptionMethod() const**

        Returns the cipher's encryption method as a **QString** .
        """
        ...
    def isNull(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#isNull

        **bool QSslCipher::isNull() const**

        Returns `true` if this is a null cipher; otherwise returns `false`.
        """
        ...
    def keyExchangeMethod(self) -> str:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#keyExchangeMethod

        **QString QSslCipher::keyExchangeMethod() const**

        Returns the cipher's key exchange method as a **QString** .
        """
        ...
    def name(self) -> str:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#name

        **QString QSslCipher::name() const**

        Returns the name of the cipher, or an empty **QString**  if this is a
        null cipher.

        **See also** **isNull** ().
        """
        ...
    def protocol(self) -> PySide6.QtNetwork.QSsl.SslProtocol:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#protocol

        **QSsl::SslProtocol QSslCipher::protocol() const**

        Returns the cipher's protocol type, or **QSsl::UnknownProtocol**  if
        **QSslCipher**  is unable to determine the protocol (**protocolString**
        () may contain more information).

        **See also** **protocolString** ().
        """
        ...
    def protocolString(self) -> str:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#protocolString

        **QString QSslCipher::protocolString() const**

        Returns the cipher's protocol as a **QString** .

        **See also** **protocol** ().
        """
        ...
    def supportedBits(self) -> int:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#supportedBits

        **int QSslCipher::supportedBits() const**

        Returns the number of bits supported by the cipher.

        **See also** **usedBits** ().
        """
        ...
    def swap(self, other: PySide6.QtNetwork.QSslCipher) -> None:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#swap

        **[since 5.0] void QSslCipher::swap(QSslCipher & other )**

        Swaps this cipher instance with **other**. This function is very fast
        and never fails.

        This function was introduced in Qt 5.0.
        """
        ...
    def usedBits(self) -> int:
        """
        https://doc.qt.io/qt-6/qsslcipher.html#usedBits

        **int QSslCipher::usedBits() const**

        Returns the number of bits used by the cipher.

        **See also** **supportedBits** ().
        """
        ...