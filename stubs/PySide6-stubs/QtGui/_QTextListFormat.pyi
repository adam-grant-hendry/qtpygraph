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

from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtGui

class QTextListFormat(PySide6.QtGui.QTextFormat):
    """
    https://doc.qt.io/qt-6/qtextlistformat.html

    **Detailed Description**

    A list is composed of one or more items, represented as text blocks. The
    list's format specifies the appearance of items in the list. In particular,
    it determines the indentation and the style of each item.

    The indentation of the items is an integer value that causes each item to be
    offset from the left margin by a certain amount. This value is read with
    **indent** () and set with **setIndent** ().

    The style used to decorate each item is set with **setStyle** () and can be
    read with the **style** () function. The style controls the type of bullet
    points and numbering scheme used for items in the list. Note that lists that
    use the decimal numbering scheme begin counting at 1 rather than 0.

    Style properties can be set to further configure the appearance of list
    items; for example, the ListNumberPrefix and ListNumberSuffix properties can
    be used to customize the numbers used in an ordered list so that they appear
    as (1), (2), (3), etc.:

    **QTextListFormat**  listFormat;
    listFormat.setStyle(**QTextListFormat** ::ListDecimal);
    listFormat.setNumberPrefix("(");
        listFormat.setNumberSuffix(")");
    cursor.insertList(listFormat);

    **See also** **QTextList** .
    """

    ListUpperRoman: QTextListFormat.Style = ...
    ListLowerRoman: QTextListFormat.Style = ...
    ListUpperAlpha: QTextListFormat.Style = ...
    ListLowerAlpha: QTextListFormat.Style = ...
    ListDecimal: QTextListFormat.Style = ...
    ListSquare: QTextListFormat.Style = ...
    ListCircle: QTextListFormat.Style = ...
    ListDisc: QTextListFormat.Style = ...
    ListStyleUndefined: QTextListFormat.Style = ...

    class Style(IntFlag):
        ListUpperRoman: QTextListFormat.Style = ...
        ListLowerRoman: QTextListFormat.Style = ...
        ListUpperAlpha: QTextListFormat.Style = ...
        ListLowerAlpha: QTextListFormat.Style = ...
        ListDecimal: QTextListFormat.Style = ...
        ListSquare: QTextListFormat.Style = ...
        ListCircle: QTextListFormat.Style = ...
        ListDisc: QTextListFormat.Style = ...
        ListStyleUndefined: QTextListFormat.Style = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qtextlistformat.html#QTextListFormat

        **QTextListFormat::QTextListFormat()**

        Constructs a new list format object.
        """
        ...
    @overload
    def __init__(self, QTextListFormat: PySide6.QtGui.QTextListFormat) -> None:
        """
        https://doc.qt.io/qt-6/qtextlistformat.html#QTextListFormat

        **QTextListFormat::QTextListFormat()**

        Constructs a new list format object.
        """
        ...
    @overload
    def __init__(self, fmt: PySide6.QtGui.QTextFormat) -> None:
        """
        https://doc.qt.io/qt-6/qtextlistformat.html#QTextListFormat

        **QTextListFormat::QTextListFormat()**

        Constructs a new list format object.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def indent(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextlistformat.html#indent

        **int QTextListFormat::indent() const**

        Returns the list format's indentation. The indentation is multiplied by
        the **QTextDocument::indentWidth**  property to get the effective indent
        in pixels.

        **See also** **setIndent** ().
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextlistformat.html#isValid

        **bool QTextListFormat::isValid() const**

        Returns `true` if this list format is valid; otherwise returns `false`.
        """
        ...
    def numberPrefix(self) -> str:
        """
        https://doc.qt.io/qt-6/qtextlistformat.html#numberPrefix

        **QString QTextListFormat::numberPrefix() const**

        Returns the list format's number prefix.

        **See also** **setNumberPrefix** ().
        """
        ...
    def numberSuffix(self) -> str:
        """
        https://doc.qt.io/qt-6/qtextlistformat.html#numberSuffix

        **QString QTextListFormat::numberSuffix() const**

        Returns the list format's number suffix.

        **See also** **setNumberSuffix** ().
        """
        ...
    def setIndent(self, indent: int) -> None:
        """
        https://doc.qt.io/qt-6/qtextlistformat.html#setIndent

        **void QTextListFormat::setIndent(int indentation )**

        Sets the list format's **indentation**. The indentation is multiplied by
        the **QTextDocument::indentWidth**  property to get the effective indent
        in pixels.

        **See also** **indent** ().
        """
        ...
    def setNumberPrefix(self, numberPrefix: str) -> None:
        """
        https://doc.qt.io/qt-6/qtextlistformat.html#setNumberPrefix

        **void QTextListFormat::setNumberPrefix(const QString & numberPrefix )**

        Sets the list format's number prefix to the string specified by
        **numberPrefix**. This can be used with all sorted list types. It does
        not have any effect on unsorted list types.

        The default prefix is an empty string.

        **See also** **numberPrefix** ().
        """
        ...
    def setNumberSuffix(self, numberSuffix: str) -> None:
        """
        https://doc.qt.io/qt-6/qtextlistformat.html#setNumberSuffix

        **void QTextListFormat::setNumberSuffix(const QString & numberSuffix )**

        Sets the list format's number suffix to the string specified by
        **numberSuffix**. This can be used with all sorted list types. It does
        not have any effect on unsorted list types.

        The default suffix is ".".

        **See also** **numberSuffix** ().
        """
        ...
    def setStyle(self, style: PySide6.QtGui.QTextListFormat.Style) -> None:
        """
        https://doc.qt.io/qt-6/qtextlistformat.html#setStyle

        **void QTextListFormat::setStyle(QTextListFormat::Style style )**

        Sets the list format's **style**.

        **See also** **style** () and **Style** .
        """
        ...
    def style(self) -> PySide6.QtGui.QTextListFormat.Style:
        """
        https://doc.qt.io/qt-6/qtextlistformat.html#style

        **QTextListFormat::Style QTextListFormat::style() const**

        Returns the list format's style.

        **See also** **setStyle** () and **Style** .
        """
        ...