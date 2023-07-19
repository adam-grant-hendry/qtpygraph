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

class QTextObject(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qtextobject.html

    **Detailed Description**

    The common grouping text objects are lists (**QTextList** ), frames
    (**QTextFrame** ), and tables (**QTextTable** ). A text object has an
    associated **format** () and **document** ().

    There are essentially two kinds of text objects: those that are used with
    blocks (block formats), and those that are used with characters (character
    formats). The first kind are derived from **QTextBlockGroup** , and the
    second kind from **QTextFrame** .

    You rarely need to use this class directly. When creating custom text
    objects, you will also need to reimplement **QTextDocument::createObject**
    () which acts as a factory method for creating text objects.

    **See also** **QTextDocument**  and **Text Object Example** .
    """

    def __init__(self, doc: PySide6.QtGui.QTextDocument) -> None:
        """
        https://doc.qt.io/qt-6/qtextobject.html#QTextObject

        **[protected] QTextObject::QTextObject(QTextDocument * document )**

        Creates a new QTextObject for the given **document**.

        **Warning:** This function should never be called directly, but only
        from **QTextDocument::createObject** ().
        """
        ...
    def document(self) -> PySide6.QtGui.QTextDocument:
        """
        https://doc.qt.io/qt-6/qtextobject.html#document

        **QTextDocument *QTextObject::document() const**

        Returns the document this object belongs to.

        **See also** **format** ().
        """
        ...
    def format(self) -> PySide6.QtGui.QTextFormat:
        """
        https://doc.qt.io/qt-6/qtextobject.html#format

        **QTextFormat QTextObject::format() const**

        Returns the text object's format.

        **See also** **setFormat** () and **document** ().
        """
        ...
    def formatIndex(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextobject.html#formatIndex

        **int QTextObject::formatIndex() const**

        Returns the index of the object's format in the document's internal list
        of formats.

        **See also** **QTextDocument::allFormats** ().
        """
        ...
    def objectIndex(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextobject.html#objectIndex

        **int QTextObject::objectIndex() const**

        Returns the object index of this object. This can be used together with
        **QTextFormat::setObjectIndex** ().
        """
        ...
    def setFormat(self, format: PySide6.QtGui.QTextFormat) -> None:
        """
        https://doc.qt.io/qt-6/qtextobject.html#setFormat

        **[protected] void QTextObject::setFormat(const QTextFormat & format )**

        Sets the text object's **format**.

        **See also** **format** ().
        """
        ...