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

class QDnsLookup(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qdnslookup.html

    **Detailed Description**

    QDnsLookup uses the mechanisms provided by the operating system to perform
    DNS lookups. To perform a lookup you need to specify a **name**  and
    **type**  then invoke the **lookup** () slot. The **finished** () signal
    will be emitted upon completion.

    For example, you can determine which servers an XMPP chat client should
    connect to for a given domain with:

    void MyObject::lookupServers()
        {
            // Create a DNS lookup.
    dns = new **QDnsLookup** (this);
            connect(dns, SIGNAL(finished()),
    this, SLOT(handleServers()));

            // Find the XMPP servers for
    gmail.com
            dns->setType(**QDnsLookup** ::SRV);
    dns->setName("_xmpp-client._tcp.gmail.com");
            dns->lookup();
        }

    Once the request finishes you can handle the results with:

    void MyObject::handleServers()
        {
            // Check the lookup succeeded.
    if (dns->error() != **QDnsLookup** ::NoError) {
                **qWarning**
    ("DNS lookup failed");
                dns->deleteLater();
                return;
    }

            // Handle the results.
            const auto records =
    dns->serviceRecords();
            for (const **QDnsServiceRecord**  &record :
    records) {
                ...
            }
            dns->deleteLater();
        }

    **Note:** If you simply want to find the IP address(es) associated with a
    host name, or the host name associated with an IP address you should use
    **QHostInfo**  instead.
    """

    NoError: QDnsLookup.Error = ...
    ResolverError: QDnsLookup.Error = ...
    OperationCancelledError: QDnsLookup.Error = ...
    InvalidRequestError: QDnsLookup.Error = ...
    InvalidReplyError: QDnsLookup.Error = ...
    ServerFailureError: QDnsLookup.Error = ...
    ServerRefusedError: QDnsLookup.Error = ...
    NotFoundError: QDnsLookup.Error = ...
    A: QDnsLookup.Type = ...
    NS: QDnsLookup.Type = ...
    CNAME: QDnsLookup.Type = ...
    PTR: QDnsLookup.Type = ...
    MX: QDnsLookup.Type = ...
    TXT: QDnsLookup.Type = ...
    AAAA: QDnsLookup.Type = ...
    SRV: QDnsLookup.Type = ...
    ANY: QDnsLookup.Type = ...

    class Error(IntFlag):
        NoError: QDnsLookup.Error = ...
        ResolverError: QDnsLookup.Error = ...
        OperationCancelledError: QDnsLookup.Error = ...
        InvalidRequestError: QDnsLookup.Error = ...
        InvalidReplyError: QDnsLookup.Error = ...
        ServerFailureError: QDnsLookup.Error = ...
        ServerRefusedError: QDnsLookup.Error = ...
        NotFoundError: QDnsLookup.Error = ...

    class Type(IntFlag):
        A: QDnsLookup.Type = ...
        NS: QDnsLookup.Type = ...
        CNAME: QDnsLookup.Type = ...
        PTR: QDnsLookup.Type = ...
        MX: QDnsLookup.Type = ...
        TXT: QDnsLookup.Type = ...
        AAAA: QDnsLookup.Type = ...
        SRV: QDnsLookup.Type = ...
        ANY: QDnsLookup.Type = ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#QDnsLookup

        **QDnsLookup::QDnsLookup(QObject * parent = nullptr)**

        Constructs a QDnsLookup object and sets **parent** as the parent object.

        The **type**  property will default to **QDnsLookup::A** .
        """
        ...
    @overload
    def __init__(
        self,
        type: PySide6.QtNetwork.QDnsLookup.Type,
        name: str,
        nameserver: (
            PySide6.QtNetwork.QHostAddress | PySide6.QtNetwork.QHostAddress.SpecialAddress
        ),
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#QDnsLookup-1

        **QDnsLookup::QDnsLookup(QDnsLookup::Type type , const QString & name ,
        QObject * parent = nullptr)**

        Constructs a QDnsLookup object for the given **type** and **name** and
        sets **parent** as the parent object.
        """
        ...
    @overload
    def __init__(
        self,
        type: PySide6.QtNetwork.QDnsLookup.Type,
        name: str,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#QDnsLookup-2

        **[since 5.4] QDnsLookup::QDnsLookup(QDnsLookup::Type type , const
        QString & name , const QHostAddress & nameserver , QObject * parent =
        nullptr)**

        Constructs a QDnsLookup object for the given **type** , **name** and
        **nameserver** and sets **parent** as the parent object.

        This function was introduced in Qt 5.4.
        """
        ...
    def abort(self) -> None:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#abort

        **[slot] void QDnsLookup::abort()**

        Aborts the DNS lookup operation.

        If the lookup is already finished, does nothing.
        """
        ...
    def canonicalNameRecords(self) -> list[PySide6.QtNetwork.QDnsDomainNameRecord]:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#canonicalNameRecords

        **QList<QDnsDomainNameRecord> QDnsLookup::canonicalNameRecords() const**

        Returns the list of canonical name records associated with this lookup.
        """
        ...
    def error(self) -> PySide6.QtNetwork.QDnsLookup.Error:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#error-prop

        **[read-only] error : const Error**

        This property holds the type of error that occurred if the DNS lookup
        failed, or **NoError** .

        **Access functions:**

        QDnsLookup::Error **error** () const

        **Notifier signal:**

        void ****finished** ** ()
        """
        ...
    def errorString(self) -> str:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#errorString-prop

        **[read-only] errorString : const QString**

        This property holds a human-readable description of the error if the DNS
        lookup failed.

        **Access functions:**

        QString **errorString** () const

        **Notifier signal:**

        void ****finished** ** ()
        """
        ...
    def hostAddressRecords(self) -> list[PySide6.QtNetwork.QDnsHostAddressRecord]:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#hostAddressRecords

        **QList<QDnsHostAddressRecord> QDnsLookup::hostAddressRecords() const**

        Returns the list of host address records associated with this lookup.
        """
        ...
    def isFinished(self) -> bool:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#isFinished

        **bool QDnsLookup::isFinished() const**

        Returns whether the reply has finished or was aborted.
        """
        ...
    def lookup(self) -> None:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#lookup

        **[slot] void QDnsLookup::lookup()**

        Performs the DNS lookup.

        The **finished** () signal is emitted upon completion.
        """
        ...
    def mailExchangeRecords(self) -> list[PySide6.QtNetwork.QDnsMailExchangeRecord]:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#mailExchangeRecords

        **QList<QDnsMailExchangeRecord> QDnsLookup::mailExchangeRecords()
        const**

        Returns the list of mail exchange records associated with this lookup.

        The records are sorted according to **RFC 5321** , so if you use them to
        connect to servers, you should try them in the order they are listed.
        """
        ...
    def name(self) -> str:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#name-prop

        **[bindable] name : QString**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the name to lookup.

        **Note:** The name will be encoded using IDNA, which means it's
        unsuitable for querying SRV records compatible with the DNS-SD
        specification.
        """
        ...
    def nameServerRecords(self) -> list[PySide6.QtNetwork.QDnsDomainNameRecord]:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#nameServerRecords

        **QList<QDnsDomainNameRecord> QDnsLookup::nameServerRecords() const**

        Returns the list of name server records associated with this lookup.
        """
        ...
    def nameserver(self) -> PySide6.QtNetwork.QHostAddress:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#nameserver-prop

        **[bindable] nameserver : QHostAddress**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the nameserver to use for DNS lookup.
        """
        ...
    def pointerRecords(self) -> list[PySide6.QtNetwork.QDnsDomainNameRecord]:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#pointerRecords

        **QList<QDnsDomainNameRecord> QDnsLookup::pointerRecords() const**

        Returns the list of pointer records associated with this lookup.
        """
        ...
    def serviceRecords(self) -> list[PySide6.QtNetwork.QDnsServiceRecord]:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#serviceRecords

        **QList<QDnsServiceRecord> QDnsLookup::serviceRecords() const**

        Returns the list of service records associated with this lookup.

        The records are sorted according to **RFC 2782** , so if you use them to
        connect to servers, you should try them in the order they are listed.
        """
        ...
    def setName(self, name: str) -> None:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#name-prop

        **[bindable] name : QString**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the name to lookup.

        **Note:** The name will be encoded using IDNA, which means it's
        unsuitable for querying SRV records compatible with the DNS-SD
        specification.
        """
        ...
    def setNameserver(
        self,
        nameserver: (
            PySide6.QtNetwork.QHostAddress | PySide6.QtNetwork.QHostAddress.SpecialAddress
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#nameserver-prop

        **[bindable] nameserver : QHostAddress**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the nameserver to use for DNS lookup.
        """
        ...
    def setType(self, arg__1: PySide6.QtNetwork.QDnsLookup.Type) -> None:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#type-prop

        **[bindable] type : Type**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the type of DNS lookup.

        **Member Function Documentation**
        """
        ...
    def textRecords(self) -> list[PySide6.QtNetwork.QDnsTextRecord]:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#textRecords

        **QList<QDnsTextRecord> QDnsLookup::textRecords() const**

        Returns the list of text records associated with this lookup.
        """
        ...
    def type(self) -> PySide6.QtNetwork.QDnsLookup.Type:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#type-prop

        **[bindable] type : Type**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the type of DNS lookup.

        **Member Function Documentation**
        """
        ...
    @property
    def finished(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#finished

        **[signal] void QDnsLookup::finished()**

        This signal is emitted when the reply has finished processing.

        **Note:** Notifier signal for property **error** . Notifier signal for
        property **errorString** .
        """
        ...
    @property
    def nameChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#nameChanged

        **[signal] void QDnsLookup::nameChanged(const QString & name )**

        This signal is emitted when the lookup **name**  changes. **name** is
        the new lookup name.

        **Note:** Notifier signal for property **name** .
        """
        ...
    @property
    def nameserverChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def typeChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdnslookup.html#typeChanged

        **[signal] void QDnsLookup::typeChanged(QDnsLookup::Type type )**

        This signal is emitted when the lookup **type**  changes. **type** is
        the new lookup type.

        **Note:** Notifier signal for property **type** .
        """
        ...
