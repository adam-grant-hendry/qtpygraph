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

class QAccessibleTextInterface:
    """
    https://doc.qt.io/qt-6/qaccessibletextinterface.html

    **Detailed Description**

    This interface corresponds to the IAccessibleText interface. It should be
    implemented for widgets that display more text than a plain label. Labels
    should be represented by only **QAccessibleInterface**  and return their
    text as name (**QAccessibleInterface::text** () with **QAccessible::Name**
    as type). The QAccessibleTextInterface is typically for text that a screen
    reader might want to read line by line, and for widgets that support text
    selection and input. This interface is, for example, implemented for
    **QLineEdit** .

    **IAccessible2 Specification**
    """

    def __init__(self) -> None: ...
    def addSelection(self, startOffset: int, endOffset: int) -> None:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#addSelection

        **[pure virtual] void QAccessibleTextInterface::addSelection(int
        startOffset , int endOffset )**

        Select the text from **startOffset** to **endOffset**. The
        **startOffset** is the first character that will be selected. The
        **endOffset** is the first character that will not be selected.

        When the object supports multiple selections (e.g. in a word processor),
        this adds a new selection, otherwise it replaces the previous selection.

        The selection will be **endOffset** \\- **startOffset** characters long.
        """
        ...
    def attributes(self, offset: int) -> tuple[str, int, int]:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#attributes

        **[pure virtual] QString QAccessibleTextInterface::attributes(int offset
        , int * startOffset , int * endOffset ) const**

        Returns the text attributes at the position **offset**. In addition the
        range of the attributes is returned in **startOffset** and
        **endOffset**.
        """
        ...
    def characterCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#characterCount

        **[pure virtual] int QAccessibleTextInterface::characterCount() const**

        Returns the length of the text (total size including spaces).
        """
        ...
    def characterRect(self, offset: int) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#characterRect

        **[pure virtual] QRect QAccessibleTextInterface::characterRect(int
        offset ) const**

        Returns the position and size of the character at position **offset** in
        screen coordinates.
        """
        ...
    def cursorPosition(self) -> int:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#cursorPosition

        **[pure virtual] int QAccessibleTextInterface::cursorPosition() const**

        Returns the current cursor position.

        **See also** **setCursorPosition** ().
        """
        ...
    def offsetAtPoint(self, point: PySide6.QtCore.QPoint) -> int:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#offsetAtPoint

        **[pure virtual] int QAccessibleTextInterface::offsetAtPoint(const
        QPoint & point ) const**

        Returns the offset of the character at the **point** in screen
        coordinates.
        """
        ...
    def removeSelection(self, selectionIndex: int) -> None:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#removeSelection

        **[pure virtual] void QAccessibleTextInterface::removeSelection(int
        selectionIndex )**

        Clears the selection with index **selectionIndex**.
        """
        ...
    def scrollToSubstring(self, startIndex: int, endIndex: int) -> None:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#scrollToSubstring

        **[pure virtual] void QAccessibleTextInterface::scrollToSubstring(int
        startIndex , int endIndex )**

        Ensures that the text between **startIndex** and **endIndex** is
        visible.
        """
        ...
    def selection(self, selectionIndex: int) -> tuple[int, int]:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#selection

        **[pure virtual] void QAccessibleTextInterface::selection(int
        selectionIndex , int * startOffset , int * endOffset ) const**

        Returns a selection. The size of the selection is returned in
        **startOffset** and **endOffset**. If there is no selection both
        **startOffset** and **endOffset** are `nullptr`.

        The accessibility APIs support multiple selections. For most widgets
        though, only one selection is supported with **selectionIndex** equal to
        0.

        **See also** **setSelection** ().
        """
        ...
    def selectionCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#selectionCount

        **[pure virtual] int QAccessibleTextInterface::selectionCount() const**

        Returns the number of selections in this text.
        """
        ...
    def setCursorPosition(self, position: int) -> None:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#setCursorPosition

        **[pure virtual] void QAccessibleTextInterface::setCursorPosition(int
        position )**

        Moves the cursor to **position**.

        **See also** **cursorPosition** ().
        """
        ...
    def setSelection(self, selectionIndex: int, startOffset: int, endOffset: int) -> None:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#setSelection

        **[pure virtual] void QAccessibleTextInterface::setSelection(int
        selectionIndex , int startOffset , int endOffset )**

        Set the selection **selectionIndex** to the range from **startOffset**
        to **endOffset**.

        **See also** **selection** (), **addSelection** (), and
        **removeSelection** ().
        """
        ...
    def text(self, startOffset: int, endOffset: int) -> str:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#text

        **[pure virtual] QString QAccessibleTextInterface::text(int startOffset
        , int endOffset ) const**

        Returns the text from **startOffset** to **endOffset**. The
        **startOffset** is the first character that will be returned. The
        **endOffset** is the first character that will not be returned.
        """
        ...
    def textAfterOffset(
        self, offset: int, boundaryType: PySide6.QtGui.QAccessible.TextBoundaryType
    ) -> tuple[str, int, int]:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#textAfterOffset

        **[virtual] QString QAccessibleTextInterface::textAfterOffset(int offset
        , QAccessible::TextBoundaryType boundaryType , int * startOffset , int *
        endOffset ) const**

        Returns the text item of type **boundaryType** that is right after
        offset **offset** and sets **startOffset** and **endOffset** values to
        the start and end positions of that item; returns an empty string if
        there is no such an item. Sets **startOffset** and **endOffset** values
        to -1 on error.

        This default implementation is provided for small text edits. A word
        processor or text editor should provide their own efficient
        implementations. This function makes no distinction between paragraphs
        and lines.

        **Note:** this function can not take the cursor position into account.
        By convention an **offset** of -2 means that this function should use
        the cursor position as offset. Thus an offset of -2 must be converted to
        the cursor position before calling this function. An offset of -1 is
        used for the text length and custom implementations of this function
        have to return the result as if the length was passed in as offset.
        """
        ...
    def textAtOffset(
        self, offset: int, boundaryType: PySide6.QtGui.QAccessible.TextBoundaryType
    ) -> tuple[str, int, int]:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#textAtOffset

        **[virtual] QString QAccessibleTextInterface::textAtOffset(int offset ,
        QAccessible::TextBoundaryType boundaryType , int * startOffset , int *
        endOffset ) const**

        Returns the text item of type **boundaryType** at offset **offset** and
        sets **startOffset** and **endOffset** values to the start and end
        positions of that item; returns an empty string if there is no such an
        item. Sets **startOffset** and **endOffset** values to -1 on error.

        This default implementation is provided for small text edits. A word
        processor or text editor should provide their own efficient
        implementations. This function makes no distinction between paragraphs
        and lines.

        **Note:** this function can not take the cursor position into account.
        By convention an **offset** of -2 means that this function should use
        the cursor position as offset. Thus an offset of -2 must be converted to
        the cursor position before calling this function. An offset of -1 is
        used for the text length and custom implementations of this function
        have to return the result as if the length was passed in as offset.
        """
        ...
    def textBeforeOffset(
        self, offset: int, boundaryType: PySide6.QtGui.QAccessible.TextBoundaryType
    ) -> tuple[str, int, int]:
        """
        https://doc.qt.io/qt-6/qaccessibletextinterface.html#textBeforeOffset

        **[virtual] QString QAccessibleTextInterface::textBeforeOffset(int
        offset , QAccessible::TextBoundaryType boundaryType , int * startOffset
        , int * endOffset ) const**

        Returns the text item of type **boundaryType** that is close to offset
        **offset** and sets **startOffset** and **endOffset** values to the
        start and end positions of that item; returns an empty string if there
        is no such an item. Sets **startOffset** and **endOffset** values to -1
        on error.

        This default implementation is provided for small text edits. A word
        processor or text editor should provide their own efficient
        implementations. This function makes no distinction between paragraphs
        and lines.

        **Note:** this function can not take the cursor position into account.
        By convention an **offset** of -2 means that this function should use
        the cursor position as offset. Thus an offset of -2 must be converted to
        the cursor position before calling this function. An offset of -1 is
        used for the text length and custom implementations of this function
        have to return the result as if the length was passed in as offset.
        """
        ...
