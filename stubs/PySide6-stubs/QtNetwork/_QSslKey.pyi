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

class QSslKey:
    """
    https://doc.qt.io/qt-6/qsslkey.html

    **Detailed Description**

    QSslKey provides a simple API for managing keys.

    **See also** **QSslSocket** , **QSslCertificate** , and **QSslCipher** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qsslkey.html#QSslKey

        **QSslKey::QSslKey()**

        Constructs a null key.

        **See also** **isNull** ().
        """
        ...
    @overload
    def __init__(
        self,
        device: PySide6.QtCore.QIODevice,
        algorithm: PySide6.QtNetwork.QSsl.KeyAlgorithm,
        format: PySide6.QtNetwork.QSsl.EncodingFormat = ...,
        type: PySide6.QtNetwork.QSsl.KeyType = ...,
        passPhrase: PySide6.QtCore.QByteArray | bytes = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsslkey.html#QSslKey-1

        **QSslKey::QSslKey(const QByteArray & encoded , QSsl::KeyAlgorithm
        algorithm , QSsl::EncodingFormat encoding = QSsl::Pem, QSsl::KeyType
        type = QSsl::PrivateKey, const QByteArray & passPhrase = QByteArray())**

        Constructs a QSslKey by decoding the string in the byte array
        **encoded** using a specified **algorithm** and **encoding** format.
        **type** specifies whether the key is public or private.

        If the key is encrypted then **passPhrase** is used to decrypt it.

        After construction, use **isNull** () to check if **encoded** contained
        a valid key.
        """
        ...
    @overload
    def __init__(
        self,
        encoded: PySide6.QtCore.QByteArray | bytes,
        algorithm: PySide6.QtNetwork.QSsl.KeyAlgorithm,
        format: PySide6.QtNetwork.QSsl.EncodingFormat = ...,
        type: PySide6.QtNetwork.QSsl.KeyType = ...,
        passPhrase: PySide6.QtCore.QByteArray | bytes = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsslkey.html#QSslKey-2

        **QSslKey::QSslKey(QIODevice * device , QSsl::KeyAlgorithm algorithm ,
        QSsl::EncodingFormat encoding = QSsl::Pem, QSsl::KeyType type =
        QSsl::PrivateKey, const QByteArray & passPhrase = QByteArray())**

        Constructs a QSslKey by reading and decoding data from a **device**
        using a specified **algorithm** and **encoding** format. **type**
        specifies whether the key is public or private.

        If the key is encrypted then **passPhrase** is used to decrypt it.

        After construction, use **isNull** () to check if **device** provided a
        valid key.
        """
        ...
    @overload
    def __init__(self, handle: int, type: PySide6.QtNetwork.QSsl.KeyType = ...) -> None:
        """
        https://doc.qt.io/qt-6/qsslkey.html#QSslKey-3

        **[since 5.0] QSslKey::QSslKey(Qt::HANDLE handle , QSsl::KeyType type =
        QSsl::PrivateKey)**

        Constructs a QSslKey from a valid native key **handle**. **type**
        specifies whether the key is public or private.

        QSslKey will take ownership for this key and you must not free the key
        using the native library.

        This function was introduced in Qt 5.0.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtNetwork.QSslKey | int) -> None:
        """
        https://doc.qt.io/qt-6/qsslkey.html#QSslKey-4

        **QSslKey::QSslKey(const QSslKey & other )**

        Constructs an identical copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def algorithm(self) -> PySide6.QtNetwork.QSsl.KeyAlgorithm:
        """
        https://doc.qt.io/qt-6/qsslkey.html#algorithm

        **QSsl::KeyAlgorithm QSslKey::algorithm() const**

        Returns the key algorithm.
        """
        ...
    def clear(self) -> None:
        """
        https://doc.qt.io/qt-6/qsslkey.html#clear

        **void QSslKey::clear()**

        Clears the contents of this key, making it a null key.

        **See also** **isNull** ().
        """
        ...
    def handle(self) -> int:
        """
        https://doc.qt.io/qt-6/qsslkey.html#handle

        **Qt::HANDLE QSslKey::handle() const**

        Returns a pointer to the native key handle, if there is one, else
        `nullptr`.

        You can use this handle together with the native API to access extended
        information about the key.

        **Warning:** Use of this function has a high probability of being non-
        portable, and its return value may vary across platforms, and between
        minor Qt releases.
        """
        ...
    def isNull(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsslkey.html#isNull

        **bool QSslKey::isNull() const**

        Returns `true` if this is a null key; otherwise false.

        **See also** **clear** ().
        """
        ...
    def length(self) -> int:
        """
        https://doc.qt.io/qt-6/qsslkey.html#length

        **int QSslKey::length() const**

        Returns the length of the key in bits, or -1 if the key is null.
        """
        ...
    def swap(self, other: PySide6.QtNetwork.QSslKey | int) -> None:
        """
        https://doc.qt.io/qt-6/qsslkey.html#swap

        **[since 5.0] void QSslKey::swap(QSslKey & other )**

        Swaps this ssl key with **other**. This function is very fast and never
        fails.

        This function was introduced in Qt 5.0.
        """
        ...
    def toDer(
        self, passPhrase: PySide6.QtCore.QByteArray | bytes = ...
    ) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qsslkey.html#toDer

        **QByteArray QSslKey::toDer(const QByteArray & passPhrase =
        QByteArray()) const**

        Returns the key in DER encoding.

        The **passPhrase** argument should be omitted as DER cannot be
        encrypted. It will be removed in a future version of Qt.
        """
        ...
    def toPem(
        self, passPhrase: PySide6.QtCore.QByteArray | bytes = ...
    ) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qsslkey.html#toPem

        **QByteArray QSslKey::toPem(const QByteArray & passPhrase =
        QByteArray()) const**

        Returns the key in PEM encoding. The result is encrypted with
        **passPhrase** if the key is a private key and **passPhrase** is non-
        empty.
        """
        ...
    def type(self) -> PySide6.QtNetwork.QSsl.KeyType:
        """
        https://doc.qt.io/qt-6/qsslkey.html#type

        **QSsl::KeyType QSslKey::type() const**

        Returns the type of the key (i.e., PublicKey or PrivateKey).
        """
        ...
