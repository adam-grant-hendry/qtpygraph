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

from collections.abc import Sequence
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtNetwork

class QNetworkCacheMetaData:
    """
    https://doc.qt.io/qt-6/qnetworkcachemetadata.html

    **Detailed Description**

    QNetworkCacheMetaData provides information about a cache file including the
    url, when it was last modified, when the cache file was created, headers for
    file and if the file should be saved onto a disk.

    **See also** **QAbstractNetworkCache** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#QNetworkCacheMetaData

        **QNetworkCacheMetaData::QNetworkCacheMetaData()**

        Constructs an invalid network cache meta data.

        **See also** **isValid** ().
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtNetwork.QNetworkCacheMetaData) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#QNetworkCacheMetaData-
        1

        **QNetworkCacheMetaData::QNetworkCacheMetaData(const
        QNetworkCacheMetaData & other )**

        Constructs a copy of the **other** QNetworkCacheMetaData.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(
        self, arg__1: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(
        self, arg__1: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    def attributes(self) -> dict[PySide6.QtNetwork.QNetworkRequest.Attribute, Any]:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#attributes

        **QNetworkCacheMetaData::AttributesMap
        QNetworkCacheMetaData::attributes() const**

        Returns all the attributes stored with this cache item.

        **See also** **setAttributes** () and **QNetworkRequest::Attribute** .
        """
        ...
    def expirationDate(self) -> PySide6.QtCore.QDateTime:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#expirationDate

        **QDateTime QNetworkCacheMetaData::expirationDate() const**

        Returns the date and time when the meta data expires.

        **See also** **setExpirationDate** ().
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#isValid

        **bool QNetworkCacheMetaData::isValid() const**

        Returns `true` if this network cache meta data has attributes that have
        been set otherwise false.
        """
        ...
    def lastModified(self) -> PySide6.QtCore.QDateTime:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#lastModified

        **QDateTime QNetworkCacheMetaData::lastModified() const**

        Returns the date and time when the meta data was last modified.

        **See also** **setLastModified** ().
        """
        ...
    def rawHeaders(
        self,
    ) -> list[tuple[PySide6.QtCore.QByteArray, PySide6.QtCore.QByteArray]]:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#rawHeaders

        **QNetworkCacheMetaData::RawHeaderList
        QNetworkCacheMetaData::rawHeaders() const**

        Returns a list of all raw headers that are set in this meta data. The
        list is in the same order that the headers were set.

        **See also** **setRawHeaders** ().
        """
        ...
    def saveToDisk(self) -> bool:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#saveToDisk

        **bool QNetworkCacheMetaData::saveToDisk() const**

        Returns is this cache should be allowed to be stored on disk.

        Some cache implementations can keep these cache items in memory for
        performance reasons, but for security reasons they should not be written
        to disk.

        Specifically with http, documents with Cache-control set to no-store or
        any https document that doesn't have "Cache-control: public" set will
        set the saveToDisk to false.

        **See also** **setSaveToDisk** ().
        """
        ...
    def setAttributes(
        self, attributes: dict[PySide6.QtNetwork.QNetworkRequest.Attribute, Any]
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#setAttributes

        **void QNetworkCacheMetaData::setAttributes(const
        QNetworkCacheMetaData::AttributesMap & attributes )**

        Sets all attributes of this cache item to be the map **attributes**.

        **See also** **attributes** () and **QNetworkRequest::setAttribute** ().
        """
        ...
    def setExpirationDate(self, dateTime: PySide6.QtCore.QDateTime) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#setExpirationDate

        **void QNetworkCacheMetaData::setExpirationDate(const QDateTime &
        dateTime )**

        Sets the date and time when the meta data expires to **dateTime**.

        **See also** **expirationDate** ().
        """
        ...
    def setLastModified(self, dateTime: PySide6.QtCore.QDateTime) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#setLastModified

        **void QNetworkCacheMetaData::setLastModified(const QDateTime & dateTime
        )**

        Sets the date and time when the meta data was last modified to
        **dateTime**.

        **See also** **lastModified** ().
        """
        ...
    def setRawHeaders(
        self,
        headers: Sequence[tuple[PySide6.QtCore.QByteArray, PySide6.QtCore.QByteArray]],
    ) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#setRawHeaders

        **void QNetworkCacheMetaData::setRawHeaders(const
        QNetworkCacheMetaData::RawHeaderList & list )**

        Sets the raw headers to **list**.

        **See also** **rawHeaders** ().
        """
        ...
    def setSaveToDisk(self, allow: bool) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#setSaveToDisk

        **void QNetworkCacheMetaData::setSaveToDisk(bool allow )**

        Sets whether this network cache meta data and associated content should
        be allowed to be stored on disk to **allow**.

        **See also** **saveToDisk** ().
        """
        ...
    def setUrl(self, url: PySide6.QtCore.QUrl | str) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#setUrl

        **void QNetworkCacheMetaData::setUrl(const QUrl & url )**

        Sets the URL this network cache meta data to be **url**.

        The password and fragment are removed from the url.

        **See also** **url** ().
        """
        ...
    def swap(self, other: PySide6.QtNetwork.QNetworkCacheMetaData) -> None:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#swap

        **[since 5.0] void QNetworkCacheMetaData::swap(QNetworkCacheMetaData &
        other )**

        Swaps this metadata instance with **other**. This function is very fast
        and never fails.

        This function was introduced in Qt 5.0.
        """
        ...
    def url(self) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qnetworkcachemetadata.html#url

        **QUrl QNetworkCacheMetaData::url() const**

        Returns the URL this network cache meta data is referring to.

        **See also** **setUrl** ().
        """
        ...
