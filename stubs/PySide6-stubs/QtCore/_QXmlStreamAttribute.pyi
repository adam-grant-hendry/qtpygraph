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

from typing import overload

import PySide6.QtCore

class QXmlStreamAttribute:
    """
    https://doc.qt.io/qt-6/qxmlstreamattribute.html

    **Detailed Description**

    An attribute consists of an optionally empty **namespaceUri** (), a **name**
    (), a **value** (), and an **isDefault** () attribute.

    The raw XML attribute name is returned as **qualifiedName** ().
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qxmlstreamattribute.html#QXmlStreamAttribute

        **QXmlStreamAttribute::QXmlStreamAttribute()**

        Creates an empty attribute.
        """
        ...
    @overload
    def __init__(self, QXmlStreamAttribute: PySide6.QtCore.QXmlStreamAttribute) -> None:
        """
        https://doc.qt.io/qt-6/qxmlstreamattribute.html#QXmlStreamAttribute-1

        **QXmlStreamAttribute::QXmlStreamAttribute(const QString & qualifiedName
        , const QString & value )**

        Constructs an attribute with qualified name **qualifiedName** and value
        **value**.
        """
        ...
    @overload
    def __init__(self, namespaceUri: str, name: str, value: str) -> None:
        """
        https://doc.qt.io/qt-6/qxmlstreamattribute.html#QXmlStreamAttribute-2

        **QXmlStreamAttribute::QXmlStreamAttribute(const QString & namespaceUri
        , const QString & name , const QString & value )**

        Constructs an attribute in the namespace described with **namespaceUri**
        with **name** and value **value**.
        """
        ...
    @overload
    def __init__(self, qualifiedName: str, value: str) -> None:
        """
        https://doc.qt.io/qt-6/qxmlstreamattribute.html#QXmlStreamAttribute

        **QXmlStreamAttribute::QXmlStreamAttribute()**

        Creates an empty attribute.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def isDefault(self) -> bool:
        """
        https://doc.qt.io/qt-6/qxmlstreamattribute.html#isDefault

        **bool QXmlStreamAttribute::isDefault() const**

        Returns `true` if the parser added this attribute with a default value
        following an ATTLIST declaration in the DTD; otherwise returns `false`.
        """
        ...
    def name(self) -> str:
        """
        https://doc.qt.io/qt-6/qxmlstreamattribute.html#name

        **QStringView QXmlStreamAttribute::name() const**

        Returns the attribute's local name.
        """
        ...
    def namespaceUri(self) -> str:
        """
        https://doc.qt.io/qt-6/qxmlstreamattribute.html#namespaceUri

        **QStringView QXmlStreamAttribute::namespaceUri() const**

        Returns the attribute's resolved namespaceUri, or an empty string
        reference if the attribute does not have a defined namespace.
        """
        ...
    def prefix(self) -> str:
        """
        https://doc.qt.io/qt-6/qxmlstreamattribute.html#prefix

        **QStringView QXmlStreamAttribute::prefix() const**

        Returns the attribute's namespace prefix.

        **See also** **name** () and **qualifiedName** ().
        """
        ...
    def qualifiedName(self) -> str:
        """
        https://doc.qt.io/qt-6/qxmlstreamattribute.html#qualifiedName

        **QStringView QXmlStreamAttribute::qualifiedName() const**

        Returns the attribute's qualified name.

        A qualified name is the raw name of an attribute in the XML data. It
        consists of the namespace **prefix** (), followed by colon, followed by
        the attribute's local **name** (). Since the namespace prefix is not
        unique (the same prefix can point to different namespaces and different
        prefixes can point to the same namespace), you shouldn't use
        qualifiedName(), but the resolved **namespaceUri** () and the
        attribute's local **name** ().
        """
        ...
    def value(self) -> str:
        """
        https://doc.qt.io/qt-6/qxmlstreamattribute.html#value

        **QStringView QXmlStreamAttribute::value() const**

        Returns the attribute's value.
        """
        ...
