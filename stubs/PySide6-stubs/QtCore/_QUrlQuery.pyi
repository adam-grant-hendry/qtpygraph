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
PySide6.QtCore, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from collections.abc import Sequence
from typing import overload

import PySide6.QtCore

class QUrlQuery:
    """
    https://doc.qt.io/qt-6/qurlquery.html

    **Detailed Description**

    It is used to parse the query strings found in URLs like the following:

    ![](images/qurl-querystring.png)

    Query strings like the above are used to transmit options in the URL and are
    usually decoded into multiple key-value pairs. The one above would contain
    two entries in its list, with keys "type" and "color". QUrlQuery can also be
    used to create a query string suitable for use in **QUrl::setQuery** () from
    the individual components of the query.

    The most common way of parsing a query string is to initialize it in the
    constructor by passing it the query string. Otherwise, the **setQuery** ()
    method can be used to set the query to be parsed. That method can also be
    used to parse a query with non-standard delimiters, after having set them
    using the **setQueryDelimiters** () function.

    The encoded query string can be obtained again using **query** (). This will
    take all the internally-stored items and encode the string using the
    delimiters.

    **Encoding**

    All of the getter methods in QUrlQuery support an optional parameter of type
    **QUrl::ComponentFormattingOptions** , including **query** (), which dictate
    how to encode the data in question. Except for **QUrl::FullyDecoded** , the
    returned value must still be considered a percent-encoded string, as there
    are certain values which cannot be expressed in decoded form (like control
    characters, byte sequences not decodable to UTF-8). For that reason, the
    percent character is always represented by the string "%25".

    **Handling of spaces and plus ("+")**

    Web browsers usually encode spaces found in HTML FORM elements to a plus
    sign ("+") and plus signs to its percent-encoded form (%2B). However, the
    Internet specifications governing URLs do not consider spaces and the plus
    character equivalent.

    For that reason, QUrlQuery never encodes the space character to "+" and will
    never decode "+" to a space character. Instead, space characters will be
    rendered "%20" in encoded form.

    To support encoding like that of HTML forms, QUrlQuery also never decodes
    the "%2B" sequence to a plus sign nor encode a plus sign. In fact, any "%2B"
    or "+" sequences found in the keys, values, or query string are left exactly
    like written (except for the uppercasing of "%2b" to "%2B").

    **Full decoding**

    With **QUrl::FullyDecoded**  formatting, all percent-encoded sequences will
    be decoded fully and the '%' character is used to represent itself.
    **QUrl::FullyDecoded**  should be used with care, since it may cause data
    loss. See the documentation of **QUrl::FullyDecoded**  for information on
    what data may be lost.

    This formatting mode should be used only when dealing with text presented to
    the user in contexts where percent-encoding is not desired. Note that
    QUrlQuery setters and query methods do not support the counterpart
    **QUrl::DecodedMode**  parsing, so using **QUrl::FullyDecoded**  to obtain a
    listing of keys may result in keys not found in the object.

    **Non-standard delimiters**

    By default, QUrlQuery uses an equal sign ("=") to separate a key from its
    value, and an ampersand ("&") to separate key-value pairs from each other.
    It is possible to change the delimiters that QUrlQuery uses for parsing and
    for reconstructing the query by calling **setQueryDelimiters** ().

    Non-standard delimiters should be chosen from among what RFC 3986 calls
    "sub-delimiters". They are:

    sub-delims    = "!" / "$" / "&" / "'" / "(" / ")"
                      / "*" /
    "+" / "," / ";" / "="

    Use of other characters is not supported and may result in unexpected
    behaviour. QUrlQuery does not verify that you passed a valid delimiter.

    **See also** **QUrl** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qurlquery.html#QUrlQuery

        **QUrlQuery::QUrlQuery()**

        Constructs an empty QUrlQuery object. A query can be set afterwards by
        calling **setQuery** () or items can be added by using **addQueryItem**
        ().

        **See also** **setQuery** () and **addQueryItem** ().
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtCore.QUrlQuery) -> None:
        """
        https://doc.qt.io/qt-6/qurlquery.html#QUrlQuery-1

        **QUrlQuery::QUrlQuery(const QUrl & url )**

        Constructs a QUrlQuery object and parses the query string found in the
        **url** URL, using the default query delimiters. To parse a query string
        using other delimiters, you should first set them using
        **setQueryDelimiters** () and then set the query with **setQuery** ().

        **See also** **QUrl::query** ().
        """
        ...
    @overload
    def __init__(self, queryString: str) -> None:
        """
        https://doc.qt.io/qt-6/qurlquery.html#QUrlQuery-2

        **QUrlQuery::QUrlQuery(const QString & queryString )**

        Constructs a QUrlQuery object and parses the **queryString** query
        string, using the default query delimiters. To parse a query string
        using other delimiters, you should first set them using
        **setQueryDelimiters** () and then set the query with **setQuery** ().
        """
        ...
    @overload
    def __init__(self, url: PySide6.QtCore.QUrl | str) -> None:
        """
        https://doc.qt.io/qt-6/qurlquery.html#QUrlQuery-3

        **[since 5.13] QUrlQuery::QUrlQuery(std::initializer_list<QPair<QString,
        QString> > list )**

        Constructs a QUrlQuery object from the **list** of key/value pair.

        This function was introduced in Qt 5.13.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def addQueryItem(self, key: str, value: str) -> None:
        """
        https://doc.qt.io/qt-6/qurlquery.html#addQueryItem

        **void QUrlQuery::addQueryItem(const QString & key , const QString &
        value )**

        Appends the pair **key** = **value** to the end of the query string of
        the URL. This method does not overwrite existing items that might exist
        with the same key.

        **Note:** This method does not treat spaces (ASCII 0x20) and plus ("+")
        signs as the same, like HTML forms do. If you need spaces to be
        represented as plus signs, use actual plus signs.

        **See also** **hasQueryItem** () and **queryItemValue** ().
        """
        ...
    def allQueryItemValues(
        self, key: str, encoding: PySide6.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> list[str]:
        """
        https://doc.qt.io/qt-6/qurlquery.html#allQueryItemValues

        **QStringList QUrlQuery::allQueryItemValues(const QString & key ,
        QUrl::ComponentFormattingOptions encoding = QUrl::PrettyDecoded) const**

        Returns the a list of query string values whose key is equal to **key**
        from the URL, using the options specified in **encoding** to encode the
        return value. If the key **key** is not found, this function returns an
        empty list.

        **See also** **queryItemValue** () and **addQueryItem** ().
        """
        ...
    def clear(self) -> None:
        """
        https://doc.qt.io/qt-6/qurlquery.html#clear

        **void QUrlQuery::clear()**

        Clears this **QUrlQuery**  object by removing all of the key-value pairs
        currently stored. If the query delimiters have been changed, this
        function will leave them with their changed values.

        **See also** **isEmpty** () and **setQueryDelimiters** ().
        """
        ...
    def hasQueryItem(self, key: str) -> bool:
        """
        https://doc.qt.io/qt-6/qurlquery.html#hasQueryItem

        **bool QUrlQuery::hasQueryItem(const QString & key ) const**

        Returns `true` if there is a query string pair whose key is equal to
        **key** from the URL.

        **See also** **addQueryItem** () and **queryItemValue** ().
        """
        ...
    def isEmpty(self) -> bool:
        """
        https://doc.qt.io/qt-6/qurlquery.html#isEmpty

        **bool QUrlQuery::isEmpty() const**

        Returns `true` if this **QUrlQuery**  object contains no key-value
        pairs, such as after being default-constructed or after parsing an empty
        query string.

        **See also** **setQuery** () and **clear** ().
        """
        ...
    def query(self, encoding: PySide6.QtCore.QUrl.ComponentFormattingOption = ...) -> str:
        """
        https://doc.qt.io/qt-6/qurlquery.html#query

        **QString QUrlQuery::query(QUrl::ComponentFormattingOptions encoding =
        QUrl::PrettyDecoded) const**

        Returns the reconstructed query string, formed from the key-value pairs
        currently stored in this **QUrlQuery**  object and separated by the
        query delimiters chosen for this object. The keys and values are encoded
        using the options given by the **encoding** parameter.

        For this function, the only ambiguous delimiter is the hash ("#"), as in
        URLs it is used to separate the query string from the fragment that may
        follow.

        The order of the key-value pairs in the returned string is exactly the
        same as in the original query.

        **See also** **setQuery** (), **QUrl::setQuery** (), **QUrl::fragment**
        (), and **Encoding** .
        """
        ...
    def queryItemValue(
        self, key: str, encoding: PySide6.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str:
        """
        https://doc.qt.io/qt-6/qurlquery.html#queryItemValue

        **QString QUrlQuery::queryItemValue(const QString & key ,
        QUrl::ComponentFormattingOptions encoding = QUrl::PrettyDecoded) const**

        Returns the query value associated with key **key** from the URL, using
        the options specified in **encoding** to encode the return value. If the
        key **key** is not found, this function returns an empty string. If you
        need to distinguish between an empty value and a non-existent key, you
        should check for the key's presence first using **hasQueryItem** ().

        If the key **key** is multiply defined, this function will return the
        first one found, in the order they were present in the query string or
        added using **addQueryItem** ().

        **See also** **addQueryItem** (), **allQueryItemValues** (), and
        **Encoding** .
        """
        ...
    def queryItems(
        self, encoding: PySide6.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> list[tuple[str, str]]:
        """
        https://doc.qt.io/qt-6/qurlquery.html#queryItems

        **QList<QPair<QString, QString> >
        QUrlQuery::queryItems(QUrl::ComponentFormattingOptions encoding =
        QUrl::PrettyDecoded) const**

        Returns the query string of the URL, as a map of keys and values, using
        the options specified in **encoding** to encode the items. The order of
        the elements is the same as the one found in the query string or set
        with **setQueryItems** ().

        **See also** **setQueryItems** () and **Encoding** .
        """
        ...
    def queryPairDelimiter(self) -> str:
        """
        https://doc.qt.io/qt-6/qurlquery.html#queryPairDelimiter

        **QChar QUrlQuery::queryPairDelimiter() const**

        Returns the character used to delimit between keys-value pairs when
        reconstructing the query string in **query** () or when parsing in
        **setQuery** ().

        **See also** **setQueryDelimiters** () and **queryValueDelimiter** ().
        """
        ...
    def queryValueDelimiter(self) -> str:
        """
        https://doc.qt.io/qt-6/qurlquery.html#queryValueDelimiter

        **QChar QUrlQuery::queryValueDelimiter() const**

        Returns the character used to delimit between keys and values when
        reconstructing the query string in **query** () or when parsing in
        **setQuery** ().

        **See also** **setQueryDelimiters** () and **queryPairDelimiter** ().
        """
        ...
    def removeAllQueryItems(self, key: str) -> None:
        """
        https://doc.qt.io/qt-6/qurlquery.html#removeAllQueryItems

        **void QUrlQuery::removeAllQueryItems(const QString & key )**

        Removes all the query string pairs whose key is equal to **key** from
        the URL.

        **See also** **removeQueryItem** ().
        """
        ...
    def removeQueryItem(self, key: str) -> None:
        """
        https://doc.qt.io/qt-6/qurlquery.html#removeQueryItem

        **void QUrlQuery::removeQueryItem(const QString & key )**

        Removes the query string pair whose key is equal to **key** from the
        URL. If there are multiple items with a key equal to **key** , it
        removes the first item in the order they were present in the query
        string or added with **addQueryItem** ().

        **See also** **removeAllQueryItems** ().
        """
        ...
    def setQuery(self, queryString: str) -> None:
        """
        https://doc.qt.io/qt-6/qurlquery.html#setQuery

        **void QUrlQuery::setQuery(const QString & queryString )**

        Parses the query string in **queryString** and sets the internal items
        to the values found there. If any delimiters have been specified with
        **setQueryDelimiters** (), this function will use them instead of the
        default delimiters to parse the string.

        **See also** **query** ().
        """
        ...
    def setQueryDelimiters(self, valueDelimiter: str, pairDelimiter: str) -> None:
        """
        https://doc.qt.io/qt-6/qurlquery.html#setQueryDelimiters

        **void QUrlQuery::setQueryDelimiters(QChar valueDelimiter , QChar
        pairDelimiter )**

        Sets the characters used for delimiting between keys and values, and
        between key-value pairs in the URL's query string. The default value
        delimiter is '=' and the default pair delimiter is '&'.

        ![](images/qurl-querystring.png)

        **valueDelimiter** will be used for separating keys from values, and
        **pairDelimiter** will be used to separate key-value pairs. Any
        occurrences of these delimiting characters in the encoded representation
        of the keys and values of the query string are percent encoded when
        returned in **query** ().

        If **valueDelimiter** is set to '(' and **pairDelimiter** is ')', the
        above query string would instead be represented like this:

        http://www.example.com/cgi-bin/drawgraph.cgi?type(pie)color(green)

        **Note:** Non-standard delimiters should be chosen from among what RFC
        3986 calls "sub-delimiters". They are:

        sub-delims    = "!" / "$" / "&" / "'" / "(" / ")"
                          /
        "*" / "+" / "," / ";" / "="

        Use of other characters is not supported and may result in unexpected
        behaviour. This method does not verify that you passed a valid
        delimiter.

        **See also** **queryValueDelimiter** () and **queryPairDelimiter** ().
        """
        ...
    def setQueryItems(self, query: Sequence[tuple[str, str]]) -> None:
        """
        https://doc.qt.io/qt-6/qurlquery.html#setQueryItems

        **void QUrlQuery::setQueryItems(const QList<QPair<QString, QString> > &
        query )**

        Sets the items in this **QUrlQuery**  object to **query**. The order of
        the elements in **query** is preserved.

        **Note:** This method does not treat spaces (ASCII 0x20) and plus ("+")
        signs as the same, like HTML forms do. If you need spaces to be
        represented as plus signs, use actual plus signs.

        **See also** **queryItems** () and **isEmpty** ().
        """
        ...
    def swap(self, other: PySide6.QtCore.QUrlQuery) -> None:
        """
        https://doc.qt.io/qt-6/qurlquery.html#swap

        **void QUrlQuery::swap(QUrlQuery & other )**

        Swaps this URL query instance with **other**. This function is very fast
        and never fails.
        """
        ...
    def toString(
        self, encoding: PySide6.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str:
        """
        https://doc.qt.io/qt-6/qurlquery.html#toString

        **QString QUrlQuery::toString(QUrl::ComponentFormattingOptions encoding
        = QUrl::PrettyDecoded) const**

        Returns this **QUrlQuery**  as a **QString** . **encoding** can be used
        to specify the URL string encoding of the return value.
        """
        ...
