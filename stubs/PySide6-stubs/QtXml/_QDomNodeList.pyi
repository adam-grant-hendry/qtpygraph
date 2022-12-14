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
PySide6.QtXml, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore
import PySide6.QtXml

class QDomNodeList:
    """
    https://doc.qt.io/qt-6/qdomnodelist.html

    **Detailed Description**

    Lists can be obtained by **QDomDocument::elementsByTagName** () and
    **QDomNode::childNodes** (). The Document Object Model (DOM) requires these
    lists to be "live": whenever you change the underlying document, the
    contents of the list will get updated.

    You can get a particular node from the list with **item** (). The number of
    items in the list is returned by **length** ().

    For further information about the Document Object Model see **Level 1**  and
    **Level 2 Core** . For a more general introduction of the DOM implementation
    see the **QDomDocument**  documentation.

    **See also** **QDomNode::childNodes** () and
    **QDomDocument::elementsByTagName** ().
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qdomnodelist.html#QDomNodeList

        **QDomNodeList::QDomNodeList()**

        Creates an empty node list.
        """
        ...
    @overload
    def __init__(self, arg__1: PySide6.QtXml.QDomNodeList) -> None:
        """
        https://doc.qt.io/qt-6/qdomnodelist.html#QDomNodeList-1

        **QDomNodeList::QDomNodeList(const QDomNodeList & n )**

        Constructs a copy of **n**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def at(self, index: int) -> PySide6.QtXml.QDomNode:
        """
        https://doc.qt.io/qt-6/qdomnodelist.html#at

        **QDomNode QDomNodeList::at(int index ) const**

        This function is provided for Qt API consistency. It is equivalent to
        **item** ().

        If **index** is negative or if **index** >= **length** () then a null
        node is returned (i.e. a node for which **QDomNode::isNull** () returns
        true).
        """
        ...
    def count(self) -> int:
        """
        https://doc.qt.io/qt-6/qdomnodelist.html#count

        **int QDomNodeList::count() const**

        This function is provided for Qt API consistency. It is equivalent to
        **length** ().
        """
        ...
    def isEmpty(self) -> bool:
        """
        https://doc.qt.io/qt-6/qdomnodelist.html#isEmpty

        **bool QDomNodeList::isEmpty() const**

        Returns `true` if the list contains no items; otherwise returns `false`.
        This function is provided for Qt API consistency.
        """
        ...
    def item(self, index: int) -> PySide6.QtXml.QDomNode:
        """
        https://doc.qt.io/qt-6/qdomnodelist.html#item

        **QDomNode QDomNodeList::item(int index ) const**

        Returns the node at position **index**.

        If **index** is negative or if **index** >= **length** () then a null
        node is returned (i.e. a node for which **QDomNode::isNull** () returns
        true).

        **See also** **length** ().
        """
        ...
    def length(self) -> int:
        """
        https://doc.qt.io/qt-6/qdomnodelist.html#length

        **int QDomNodeList::length() const**

        Returns the number of nodes in the list.
        """
        ...
    def size(self) -> int:
        """
        https://doc.qt.io/qt-6/qdomnodelist.html#size

        **int QDomNodeList::size() const**

        This function is provided for Qt API consistency. It is equivalent to
        **length** ().
        """
        ...
