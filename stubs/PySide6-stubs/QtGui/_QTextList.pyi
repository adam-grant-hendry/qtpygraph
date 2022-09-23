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
PySide6.QtGui, except for defaults which are replaced by "...".
"""
from __future__ import annotations

import PySide6.QtCore
import PySide6.QtGui

class QTextList(PySide6.QtGui.QTextBlockGroup):
    """
    https://doc.qt.io/qt-6/qtextlist.html

    **Detailed Description**

    A list contains a sequence of text blocks, each of which is marked with a
    bullet point or other symbol. Multiple levels of lists can be used, and the
    automatic numbering feature provides support for ordered numeric and
    alphabetical lists.

    Lists are created by using a text cursor to insert an empty list at the
    current position or by moving existing text into a new list. The
    **QTextCursor::insertList** () function inserts an empty block into the
    document at the cursor position, and makes it the first item in a list.

    **QTextListFormat**  listFormat;
            if (list) {
                listFormat
    = list->format();
                listFormat.setIndent(listFormat.indent() + 1);
    }

            listFormat.setStyle(**QTextListFormat** ::ListDisc);
    cursor.insertList(listFormat);

    The **QTextCursor::createList** () function takes the contents of the
    cursor's current block and turns it into the first item of a new list.

    The cursor's current list is found with **QTextCursor::currentList** ().

    The number of items in a list is given by **count** (). Each item can be
    obtained by its index in the list with the **item** () function. Similarly,
    the index of a given item can be found with **itemNumber** (). The text of
    each item can be found with the **itemText** () function.

    Note that the items in the list may not be adjacent elements in the
    document. For example, the top-level items in a multi-level list will be
    separated by the items in lower levels of the list.

    List items can be deleted by index with the **removeItem** () function.
    **remove** () deletes the specified item in the list.

    The list's format is set with **setFormat** () and read with **format** ().
    The format describes the decoration of the list itself, and not the
    individual items.

    **See also** **QTextBlock** , **QTextListFormat** , and **QTextCursor** .
    """

    def __init__(self, doc: PySide6.QtGui.QTextDocument) -> None: ...
    def add(self, block: PySide6.QtGui.QTextBlock) -> None:
        """
        https://doc.qt.io/qt-6/qtextlist.html#add

        **void QTextList::add(const QTextBlock & block )**

        Makes the given **block** part of the list.

        **See also** **remove** () and **removeItem** ().
        """
        ...
    def count(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextlist.html#count

        **int QTextList::count() const**

        Returns the number of items in the list.
        """
        ...
    def format(self) -> PySide6.QtGui.QTextListFormat:
        """
        https://doc.qt.io/qt-6/qtextlist.html#format

        **QTextListFormat QTextList::format() const**

        Returns the list's format.

        **See also** **setFormat** ().
        """
        ...
    def item(self, i: int) -> PySide6.QtGui.QTextBlock:
        """
        https://doc.qt.io/qt-6/qtextlist.html#item

        **QTextBlock QTextList::item(int i ) const**

        Returns the **i** -th text block in the list.

        **See also** **count** () and **itemText** ().
        """
        ...
    def itemNumber(self, arg__1: PySide6.QtGui.QTextBlock) -> int:
        """
        https://doc.qt.io/qt-6/qtextlist.html#itemNumber

        **int QTextList::itemNumber(const QTextBlock & block ) const**

        Returns the index of the list item that corresponds to the given
        **block**. Returns -1 if the block was not present in the list.
        """
        ...
    def itemText(self, arg__1: PySide6.QtGui.QTextBlock) -> str:
        """
        https://doc.qt.io/qt-6/qtextlist.html#itemText

        **QString QTextList::itemText(const QTextBlock & block ) const**

        Returns the text of the list item that corresponds to the given
        **block**.
        """
        ...
    def remove(self, arg__1: PySide6.QtGui.QTextBlock) -> None:
        """
        https://doc.qt.io/qt-6/qtextlist.html#remove

        **void QTextList::remove(const QTextBlock & block )**

        Removes the given **block** from the list.

        **See also** **add** () and **removeItem** ().
        """
        ...
    def removeItem(self, i: int) -> None:
        """
        https://doc.qt.io/qt-6/qtextlist.html#removeItem

        **void QTextList::removeItem(int i )**

        Removes the item at item position **i** from the list. When the last
        item in the list is removed, the list is automatically deleted by the
        **QTextDocument**  that owns it.

        **See also** **add** () and **remove** ().
        """
        ...
    def setFormat(self, format: PySide6.QtGui.QTextListFormat) -> None:
        """
        https://doc.qt.io/qt-6/qtextlist.html#setFormat

        **void QTextList::setFormat(const QTextListFormat & format )**

        Sets the list's format to **format**.

        **See also** **format** ().
        """
        ...
