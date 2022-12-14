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
PySide6.QtWebEngineCore, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtNetwork
import PySide6.QtWebChannel
import PySide6.QtWebEngineCore

class QWebEngineCertificateError:
    """
    https://doc.qt.io/qt-6/qwebenginecertificateerror.html

    **Detailed Description**

    Provides information about a certificate error. This class is used as a
    parameter of **QWebEnginePage::certificateError** ().
    """

    SslObsoleteVersion: QWebEngineCertificateError.Type = ...
    CertificateKnownInterceptionBlocked: QWebEngineCertificateError.Type = ...
    CertificateSymantecLegacy: QWebEngineCertificateError.Type = ...
    CertificateTransparencyRequired: QWebEngineCertificateError.Type = ...
    CertificateValidityTooLong: QWebEngineCertificateError.Type = ...
    CertificateNameConstraintViolation: QWebEngineCertificateError.Type = ...
    CertificateWeakKey: QWebEngineCertificateError.Type = ...
    CertificateNonUniqueName: QWebEngineCertificateError.Type = ...
    CertificateWeakSignatureAlgorithm: QWebEngineCertificateError.Type = ...
    CertificateInvalid: QWebEngineCertificateError.Type = ...
    CertificateRevoked: QWebEngineCertificateError.Type = ...
    CertificateUnableToCheckRevocation: QWebEngineCertificateError.Type = ...
    CertificateNoRevocationMechanism: QWebEngineCertificateError.Type = ...
    CertificateContainsErrors: QWebEngineCertificateError.Type = ...
    CertificateAuthorityInvalid: QWebEngineCertificateError.Type = ...
    CertificateDateInvalid: QWebEngineCertificateError.Type = ...
    CertificateCommonNameInvalid: QWebEngineCertificateError.Type = ...
    SslPinnedKeyNotInCertificateChain: QWebEngineCertificateError.Type = ...

    class Type(IntFlag):
        SslObsoleteVersion: QWebEngineCertificateError.Type = ...
        CertificateKnownInterceptionBlocked: QWebEngineCertificateError.Type = ...
        CertificateSymantecLegacy: QWebEngineCertificateError.Type = ...
        CertificateTransparencyRequired: QWebEngineCertificateError.Type = ...
        CertificateValidityTooLong: QWebEngineCertificateError.Type = ...
        CertificateNameConstraintViolation: QWebEngineCertificateError.Type = ...
        CertificateWeakKey: QWebEngineCertificateError.Type = ...
        CertificateNonUniqueName: QWebEngineCertificateError.Type = ...
        CertificateWeakSignatureAlgorithm: QWebEngineCertificateError.Type = ...
        CertificateInvalid: QWebEngineCertificateError.Type = ...
        CertificateRevoked: QWebEngineCertificateError.Type = ...
        CertificateUnableToCheckRevocation: QWebEngineCertificateError.Type = ...
        CertificateNoRevocationMechanism: QWebEngineCertificateError.Type = ...
        CertificateContainsErrors: QWebEngineCertificateError.Type = ...
        CertificateAuthorityInvalid: QWebEngineCertificateError.Type = ...
        CertificateDateInvalid: QWebEngineCertificateError.Type = ...
        CertificateCommonNameInvalid: QWebEngineCertificateError.Type = ...
        SslPinnedKeyNotInCertificateChain: QWebEngineCertificateError.Type = ...
    def __init__(
        self, other: PySide6.QtWebEngineCore.QWebEngineCertificateError
    ) -> None: ...
    def acceptCertificate(self) -> None:
        """
        https://doc.qt.io/qt-6/qwebenginecertificateerror.html#acceptCertificate

        **[invokable, since 5.14] void
        QWebEngineCertificateError::acceptCertificate()**

        Accepts the certificate and continues the loading of the requested URL.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.14.
        """
        ...
    def certificateChain(self) -> list[PySide6.QtNetwork.QSslCertificate]:
        """
        https://doc.qt.io/qt-6/qwebenginecertificateerror.html#certificateChain

        **[since 5.14] QList<QSslCertificate>
        QWebEngineCertificateError::certificateChain() const**

        Returns the peer's chain of digital certificates.

        Chain starts with the peer's immediate certificate and ending with the
        CA's certificate.

        This function was introduced in Qt 5.14.
        """
        ...
    def defer(self) -> None:
        """
        https://doc.qt.io/qt-6/qwebenginecertificateerror.html#defer

        **[invokable, since 5.14] void QWebEngineCertificateError::defer()**

        Marks the certificate error for delayed handling.

        This function should be called when there is a need to postpone the
        decision whether to accept a certificate, for example, while waiting for
        user input. When called, the function pauses the URL request until
        **acceptCertificate** () or **rejectCertificate** () is called.

        **Note:** It is only possible to defer overridable certificate errors.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.14.

        **See also** **isOverridable** ().
        """
        ...
    def description(self) -> str:
        """
        https://doc.qt.io/qt-6/qwebenginecertificateerror.html#description

        **QString QWebEngineCertificateError::description() const**

        Returns a short localized human-readable description of the error.

        **Note:** Getter function for property description.

        **See also** **url** () and **isOverridable** ().
        """
        ...
    def isOverridable(self) -> bool: ...
    def rejectCertificate(self) -> None:
        """
        https://doc.qt.io/qt-6/qwebenginecertificateerror.html#rejectCertificate

        **[invokable, since 5.14] void
        QWebEngineCertificateError::rejectCertificate()**

        Rejects the certificate and aborts the loading of the requested URL.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.14.
        """
        ...
    def type(self) -> PySide6.QtWebEngineCore.QWebEngineCertificateError.Type:
        """
        https://doc.qt.io/qt-6/qwebenginecertificateerror.html#type

        **QWebEngineCertificateError::Type QWebEngineCertificateError::type()
        const**

        Returns the type of the error.

        **Note:** Getter function for property type.

        **See also** **description** () and **isOverridable** ().
        """
        ...
    def url(self) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qwebenginecertificateerror.html#url

        **QUrl QWebEngineCertificateError::url() const**

        Returns the URL that triggered the error.

        **Note:** Getter function for property url.

        **See also** **description** ().
        """
        ...
