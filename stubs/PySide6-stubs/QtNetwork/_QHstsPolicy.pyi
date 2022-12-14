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

class QHstsPolicy:
    """
    https://doc.qt.io/qt-6/qhstspolicy.html

    **Detailed Description**

    HSTS policy defines a period of time during which **QNetworkAccessManager**
    should only access a host in a secure fashion. HSTS policy is defined by
    RFC6797.

    You can set expiry time and host name for this policy, and control whether
    it applies to subdomains, either in the constructor or by calling
    **setExpiry** (), **setHost** () and setIncludesSubdomains().

    **See also** **QNetworkAccessManager::setStrictTransportSecurityEnabled**
    ().
    """

    IncludeSubDomains: QHstsPolicy.PolicyFlag = ...

    class PolicyFlag(IntFlag):
        IncludeSubDomains: QHstsPolicy.PolicyFlag = ...

    class PolicyFlags: ...

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qhstspolicy.html#QHstsPolicy

        **QHstsPolicy::QHstsPolicy()**

        Constructs an invalid (expired) policy with empty host name and
        subdomains not included.
        """
        ...
    @overload
    def __init__(
        self,
        expiry: PySide6.QtCore.QDateTime,
        flags: PySide6.QtNetwork.QHstsPolicy.PolicyFlags,
        host: str,
        mode: PySide6.QtCore.QUrl.ParsingMode = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qhstspolicy.html#QHstsPolicy-1

        **QHstsPolicy::QHstsPolicy(const QDateTime & expiry ,
        QHstsPolicy::PolicyFlags flags , const QString & host ,
        QUrl::ParsingMode mode = QUrl::DecodedMode)**

        Constructs QHstsPolicy with **expiry** (in UTC); **flags** is a value
        indicating whether this policy must also include subdomains, **host**
        data is interpreted according to **mode**.

        **See also** **QUrl::setHost** (), **QUrl::ParsingMode** , and
        **QHstsPolicy::PolicyFlag** .
        """
        ...
    @overload
    def __init__(self, rhs: PySide6.QtNetwork.QHstsPolicy) -> None:
        """
        https://doc.qt.io/qt-6/qhstspolicy.html#QHstsPolicy-2

        **QHstsPolicy::QHstsPolicy(const QHstsPolicy & other )**

        Creates a copy of **other** object.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def expiry(self) -> PySide6.QtCore.QDateTime:
        """
        https://doc.qt.io/qt-6/qhstspolicy.html#expiry

        **QDateTime QHstsPolicy::expiry() const**

        Returns the expiration date for the policy (in UTC).

        **See also** **setExpiry** ().
        """
        ...
    def host(self, options: PySide6.QtCore.QUrl.ComponentFormattingOption = ...) -> str:
        """
        https://doc.qt.io/qt-6/qhstspolicy.html#host

        **QString QHstsPolicy::host(QUrl::ComponentFormattingOptions options =
        QUrl::FullyDecoded) const**

        Returns a host for a given policy, formatted according to **options**.

        **See also** **setHost** (), **QUrl::host** (), and
        **QUrl::ComponentFormattingOptions** .
        """
        ...
    def includesSubDomains(self) -> bool:
        """
        https://doc.qt.io/qt-6/qhstspolicy.html#includesSubDomains

        **bool QHstsPolicy::includesSubDomains() const**

        Returns `true` if this policy also includes subdomains.

        **See also** **setIncludesSubDomains** ().
        """
        ...
    def isExpired(self) -> bool:
        """
        https://doc.qt.io/qt-6/qhstspolicy.html#isExpired

        **bool QHstsPolicy::isExpired() const**

        Return `true` if this policy has a valid expiration date and this date
        is greater than QDateTime::currentGetDateTimeUtc().

        **See also** **setExpiry** () and **expiry** ().
        """
        ...
    def setExpiry(self, expiry: PySide6.QtCore.QDateTime) -> None:
        """
        https://doc.qt.io/qt-6/qhstspolicy.html#setExpiry

        **void QHstsPolicy::setExpiry(const QDateTime & expiry )**

        Sets the expiration date for the policy (in UTC) to **expiry**.

        **See also** **expiry** ().
        """
        ...
    def setHost(self, host: str, mode: PySide6.QtCore.QUrl.ParsingMode = ...) -> None:
        """
        https://doc.qt.io/qt-6/qhstspolicy.html#setHost

        **void QHstsPolicy::setHost(const QString & host , QUrl::ParsingMode
        mode = QUrl::DecodedMode)**

        Sets a host, **host** data is interpreted according to **mode**
        parameter.

        **See also** **host** (), **QUrl::setHost** (), and
        **QUrl::ParsingMode** .
        """
        ...
    def setIncludesSubDomains(self, include: bool) -> None:
        """
        https://doc.qt.io/qt-6/qhstspolicy.html#setIncludesSubDomains

        **void QHstsPolicy::setIncludesSubDomains(bool include )**

        Sets whether subdomains are included for this policy to **include**.

        **See also** **includesSubDomains** ().
        """
        ...
    def swap(self, other: PySide6.QtNetwork.QHstsPolicy) -> None:
        """
        https://doc.qt.io/qt-6/qhstspolicy.html#swap

        **void QHstsPolicy::swap(QHstsPolicy & other )**

        Swaps this policy with the **other** policy.
        """
        ...
