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

class QSslCertificateExtension:
    """
    https://doc.qt.io/qt-6/qsslcertificateextension.html

    **Detailed Description**

    QSslCertificateExtension provides access to an extension stored in an X509
    certificate. The information available depends on the type of extension
    being accessed.

    All X509 certificate extensions have the following properties:

    PropertyDescription
    nameThe human readable name of the extension, eg.
    'basicConstraints'.
    criticalityThis is a boolean value indicating if the
    extension is critical to correctly interpreting the certificate.
    oidThe
    ASN.1 object identifier that specifies which extension this is.
    supportedIf this is true the structure of the extension's value will not
    change between Qt versions.
    valueA **QVariant**  with a structure
    dependent on the type of extension.

    Whilst this class provides access to any type of extension, only some are
    guaranteed to be returned in a format that will remain unchanged between
    releases. The **isSupported** () method returns `true` for extensions where
    this is the case.

    The extensions currently supported, and the structure of the value returned
    are as follows:

    NameOIDDetails
    basicConstraints2.5.29.19Returned as a QVariantMap. The key
    'ca' contains a boolean value, the optional key 'pathLenConstraint' contains
    an integer.
    authorityInfoAccess1.3.6.1.5.5.7.1.1Returned as a QVariantMap.
    There is a key for each access method, with the value being a URI.
    subjectKeyIdentifier2.5.29.14Returned as a **QVariant**  containing a
    **QString** . The string is the key identifier.
    authorityKeyIdentifier2.5.29.35Returned as a QVariantMap. The optional key
    'keyid' contains the key identifier as a hex string stored in a
    **QByteArray** . The optional key 'serial' contains the authority key serial
    number as a qlonglong. Currently there is no support for the general names
    field of this extension.

    In addition to the supported extensions above, many other common extensions
    will be returned in a reasonably structured way. Extensions that the SSL
    backend has no support for at all will be returned as a **QByteArray** .

    Further information about the types of extensions certificates can contain
    can be found in RFC 5280.

    **See also** **QSslCertificate::extensions** ().
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qsslcertificateextension.html#QSslCertificateExte
        nsion

        **QSslCertificateExtension::QSslCertificateExtension()**

        Constructs a QSslCertificateExtension.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtNetwork.QSslCertificateExtension) -> None:
        """
        https://doc.qt.io/qt-6/qsslcertificateextension.html#QSslCertificateExte
        nsion-1

        **QSslCertificateExtension::QSslCertificateExtension(const
        QSslCertificateExtension & other )**

        Constructs a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def isCritical(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsslcertificateextension.html#isCritical

        **bool QSslCertificateExtension::isCritical() const**

        Returns the criticality of the extension.
        """
        ...
    def isSupported(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsslcertificateextension.html#isSupported

        **bool QSslCertificateExtension::isSupported() const**

        Returns the true if this extension is supported. In this case, supported
        simply means that the structure of the **QVariant**  returned by the
        **value** () accessor will remain unchanged between versions.
        Unsupported extensions can be freely used, however there is no guarantee
        that the returned data will have the same structure between versions.
        """
        ...
    def name(self) -> str:
        """
        https://doc.qt.io/qt-6/qsslcertificateextension.html#name

        **QString QSslCertificateExtension::name() const**

        Returns the name of the extension. If no name is known for the extension
        then the OID will be returned.
        """
        ...
    def oid(self) -> str:
        """
        https://doc.qt.io/qt-6/qsslcertificateextension.html#oid

        **QString QSslCertificateExtension::oid() const**

        Returns the ASN.1 OID of this extension.
        """
        ...
    def swap(self, other: PySide6.QtNetwork.QSslCertificateExtension) -> None:
        """
        https://doc.qt.io/qt-6/qsslcertificateextension.html#swap

        **void QSslCertificateExtension::swap(QSslCertificateExtension & other
        )**

        Swaps this certificate extension instance with **other**. This function
        is very fast and never fails.
        """
        ...
    def value(self) -> Any:
        """
        https://doc.qt.io/qt-6/qsslcertificateextension.html#value

        **QVariant QSslCertificateExtension::value() const**

        Returns the value of the extension. The structure of the value returned
        depends on the extension type.
        """
        ...
