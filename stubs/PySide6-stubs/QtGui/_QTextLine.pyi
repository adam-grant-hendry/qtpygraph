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

class QTextLine:
    """
    https://doc.qt.io/qt-6/qtextline.html

    **Detailed Description**

    A text line is usually created by **QTextLayout::createLine** ().

    After being created, the line can be filled using the **setLineWidth** () or
    **setNumColumns** () functions. A line has a number of attributes including
    the rectangle it occupies, **rect** (), its coordinates, **x** () and **y**
    (), its **textLength** (), **width** () and **naturalTextWidth** (), and its
    **ascent** () and **descent** () relative to the text. The position of the
    cursor in terms of the line is available from **cursorToX** () and its
    inverse from **xToCursor** (). A line can be moved with **setPosition** ().
    """

    CursorBetweenCharacters: QTextLine.CursorPosition = ...
    CursorOnCharacter: QTextLine.CursorPosition = ...
    Leading: QTextLine.Edge = ...
    Trailing: QTextLine.Edge = ...

    class CursorPosition(IntFlag):
        CursorBetweenCharacters: QTextLine.CursorPosition = ...
        CursorOnCharacter: QTextLine.CursorPosition = ...

    class Edge(IntFlag):
        Leading: QTextLine.Edge = ...
        Trailing: QTextLine.Edge = ...
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qtextline.html#QTextLine

        **QTextLine::QTextLine()**

        Creates an invalid line.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def ascent(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextline.html#ascent

        **qreal QTextLine::ascent() const**

        Returns the line's ascent.

        **See also** **descent** () and **height** ().
        """
        ...
    def cursorToX(
        self, cursorPos: int, edge: PySide6.QtGui.QTextLine.Edge = ...
    ) -> object:
        """
        https://doc.qt.io/qt-6/qtextline.html#cursorToX

        **qreal QTextLine::cursorToX(int * cursorPos , QTextLine::Edge edge =
        Leading) const**

        Converts the cursor position **cursorPos** to the corresponding x
        position inside the line, taking account of the **edge**.

        If **cursorPos** is not a valid cursor position, the nearest valid
        cursor position will be used instead, and **cursorPos** will be modified
        to point to this valid cursor position.

        **See also** **xToCursor** ().
        """
        ...
    def descent(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextline.html#descent

        **qreal QTextLine::descent() const**

        Returns the line's descent.

        **See also** **ascent** () and **height** ().
        """
        ...
    def draw(
        self,
        painter: PySide6.QtGui.QPainter,
        position: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextline.html#draw

        **void QTextLine::draw(QPainter * painter , const QPointF & position )
        const**

        Draws a line on the given **painter** at the specified **position**.
        """
        ...
    def glyphRuns(
        self, from_: int = ..., length: int = ...
    ) -> list[PySide6.QtGui.QGlyphRun]:
        """
        https://doc.qt.io/qt-6/qtextline.html#glyphRuns

        **[since 5.0] QList<QGlyphRun> QTextLine::glyphRuns(int from = -1, int
        length = -1) const**

        Returns the glyph indexes and positions for all glyphs in this
        **QTextLine**  for characters in the range defined by **from** and
        **length**. The **from** index is relative to the beginning of the text
        in the containing **QTextLayout** , and the range must be within the
        range of **QTextLine**  as given by functions **textStart** () and
        **textLength** ().

        If **from** is negative, it will default to **textStart** (), and if
        **length** is negative it will default to the return value of
        **textLength** ().

        This function was introduced in Qt 5.0.

        **See also** **QTextLayout::glyphRuns** ().
        """
        ...
    def height(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextline.html#height

        **qreal QTextLine::height() const**

        Returns the line's height. This is equal to **ascent** () + **descent**
        () if leading is not included. If leading is included, this equals to
        **ascent** () + **descent** () + **leading** ().

        **See also** **ascent** (), **descent** (), **leading** (), and
        **setLeadingIncluded** ().
        """
        ...
    def horizontalAdvance(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextline.html#horizontalAdvance

        **qreal QTextLine::horizontalAdvance() const**

        Returns the horizontal advance of the text. The advance of the text is
        the distance from its position to the next position at which text would
        naturally be drawn.

        By adding the advance to the position of the text line and using this as
        the position of a second text line, you will be able to position the two
        lines side-by-side without gaps in-between.
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextline.html#isValid

        **bool QTextLine::isValid() const**

        Returns `true` if this text line is valid; otherwise returns `false`.
        """
        ...
    def leading(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextline.html#leading

        **qreal QTextLine::leading() const**

        Returns the line's leading.

        **See also** **ascent** (), **descent** (), and **height** ().
        """
        ...
    def leadingIncluded(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextline.html#leadingIncluded

        **bool QTextLine::leadingIncluded() const**

        Returns `true` if positive leading is included into the line's height;
        otherwise returns `false`.

        By default, leading is not included.

        **See also** **setLeadingIncluded** ().
        """
        ...
    def lineNumber(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextline.html#lineNumber

        **int QTextLine::lineNumber() const**

        Returns the position of the line in the text engine.
        """
        ...
    def naturalTextRect(self) -> PySide6.QtCore.QRectF:
        """
        https://doc.qt.io/qt-6/qtextline.html#naturalTextRect

        **QRectF QTextLine::naturalTextRect() const**

        Returns the rectangle covered by the line.
        """
        ...
    def naturalTextWidth(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextline.html#naturalTextWidth

        **qreal QTextLine::naturalTextWidth() const**

        Returns the width of the line that is occupied by text. This is always
        <= to **width** (), and is the minimum width that could be used by
        layout() without changing the line break position.
        """
        ...
    def position(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qtextline.html#position

        **QPointF QTextLine::position() const**

        Returns the line's position relative to the text layout's position.

        **See also** **setPosition** ().
        """
        ...
    def rect(self) -> PySide6.QtCore.QRectF:
        """
        https://doc.qt.io/qt-6/qtextline.html#rect

        **QRectF QTextLine::rect() const**

        Returns the line's bounding rectangle.

        **See also** **x** (), **y** (), **textLength** (), and **width** ().
        """
        ...
    def setLeadingIncluded(self, included: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtextline.html#setLeadingIncluded

        **void QTextLine::setLeadingIncluded(bool included )**

        Includes positive leading into the line's height if **included** is
        true; otherwise does not include leading.

        By default, leading is not included.

        Note that negative leading is ignored, it must be handled in the code
        using the text lines by letting the lines overlap.

        **See also** **leadingIncluded** ().
        """
        ...
    def setLineWidth(self, width: float) -> None:
        """
        https://doc.qt.io/qt-6/qtextline.html#setLineWidth

        **void QTextLine::setLineWidth(qreal width )**

        Lays out the line with the given **width**. The line is filled from its
        starting position with as many characters as will fit into the line. In
        case the text cannot be split at the end of the line, it will be filled
        with additional characters to the next whitespace or end of the text.
        """
        ...
    @overload
    def setNumColumns(self, columns: int) -> None:
        """
        https://doc.qt.io/qt-6/qtextline.html#setNumColumns

        **void QTextLine::setNumColumns(int numColumns )**

        Lays out the line. The line is filled from its starting position with as
        many characters as are specified by **numColumns**. In case the text
        cannot be split until **numColumns** characters, the line will be filled
        with as many characters to the next whitespace or end of the text.
        """
        ...
    @overload
    def setNumColumns(self, columns: int, alignmentWidth: float) -> None:
        """
        https://doc.qt.io/qt-6/qtextline.html#setNumColumns-1

        **void QTextLine::setNumColumns(int numColumns , qreal alignmentWidth
        )**

        Lays out the line. The line is filled from its starting position with as
        many characters as are specified by **numColumns**. In case the text
        cannot be split until **numColumns** characters, the line will be filled
        with as many characters to the next whitespace or end of the text. The
        provided **alignmentWidth** is used as reference width for alignment.
        """
        ...
    def setPosition(
        self,
        pos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextline.html#setPosition

        **void QTextLine::setPosition(const QPointF & pos )**

        Moves the line to position **pos**.

        **See also** **position** ().
        """
        ...
    def textLength(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextline.html#textLength

        **int QTextLine::textLength() const**

        Returns the length of the text in the line.

        **See also** **naturalTextWidth** ().
        """
        ...
    def textStart(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextline.html#textStart

        **int QTextLine::textStart() const**

        Returns the start of the line from the beginning of the string passed to
        the **QTextLayout** .
        """
        ...
    def width(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextline.html#width

        **qreal QTextLine::width() const**

        Returns the line's width as specified by the layout() function.

        **See also** **naturalTextWidth** (), **x** (), **y** (), **textLength**
        (), and **rect** ().
        """
        ...
    def x(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextline.html#x

        **qreal QTextLine::x() const**

        Returns the line's x position.

        **See also** **rect** (), **y** (), **textLength** (), and **width** ().
        """
        ...
    def xToCursor(
        self, x: float, edge: PySide6.QtGui.QTextLine.CursorPosition = ...
    ) -> int:
        """
        https://doc.qt.io/qt-6/qtextline.html#xToCursor

        **int QTextLine::xToCursor(qreal x , QTextLine::CursorPosition cpos =
        CursorBetweenCharacters) const**

        Converts the x-coordinate **x** , to the nearest matching cursor
        position, depending on the cursor position type, **cpos**. Note that
        result cursor position includes possible preedit area text.

        **See also** **cursorToX** ().
        """
        ...
    def y(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextline.html#y

        **qreal QTextLine::y() const**

        Returns the line's y position.

        **See also** **x** (), **rect** (), **textLength** (), and **width** ().
        """
        ...
