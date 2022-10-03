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

from collections.abc import Sequence
from typing import overload

import PySide6.QtCore
import PySide6.QtGui

class QFontMetrics:
    """
    https://doc.qt.io/qt-6/qfontmetrics.html

    **Detailed Description**

    QFontMetrics functions calculate the size of characters and strings for a
    given font. There are three ways you can create a QFontMetrics object:

    1. Calling the QFontMetrics constructor with a **QFont**  creates a font
    metrics object for a screen-compatible font, i.e. the font cannot be a
    printer font. If the font is changed later, the font metrics object is
    **not** updated.

    (Note: If you use a printer font the values returned may
    be inaccurate. Printer fonts are not always accessible so the nearest screen
    font is used if a printer font is supplied.)

      2. **QWidget::fontMetrics**
    () returns the font metrics for a widget's font. This is equivalent to
    QFontMetrics(widget->font()). If the widget's font is changed later, the
    font metrics object is **not** updated.
      3. **QPainter::fontMetrics** ()
    returns the font metrics for a painter's current font. If the painter's font
    is changed later, the font metrics object is **not** updated.

    Once created, the object provides functions to access the individual metrics
    of the font, its characters, and for strings rendered in the font.

    There are several functions that operate on the font: **ascent** (),
    **descent** (), **height** (), **leading** () and **lineSpacing** () return
    the basic size properties of the font. The **underlinePos** (),
    **overlinePos** (), **strikeOutPos** () and **lineWidth** () functions,
    return the properties of the line that underlines, overlines or strikes out
    the characters. These functions are all fast.

    There are also some functions that operate on the set of glyphs in the font:
    **minLeftBearing** (), **minRightBearing** () and **maxWidth** (). These are
    by necessity slow, and we recommend avoiding them if possible.

    For each character, you can get its **horizontalAdvance** (),
    **leftBearing** (), and **rightBearing** (), and find out whether it is in
    the font using **inFont** (). You can also treat the character as a string,
    and use the string functions on it.

    The string functions include **horizontalAdvance** (), to return the width
    of a string in pixels (or points, for a printer), **boundingRect** (), to
    return a rectangle large enough to contain the rendered string, and **size**
    (), to return the size of that rectangle.

    Example:

    **QFont**  font("times", 24);
        **QFontMetrics**  fm(font);
        int
    pixelsWide = fm.horizontalAdvance("What's the width of this text?");
        int
    pixelsHigh = fm.height();

    **See also** **QFont** , **QFontInfo** , **QFontDatabase** , and **Character
    Map Example** .
    """

    @overload
    def __init__(self, arg__1: PySide6.QtGui.QFontMetrics) -> None:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#QFontMetrics

        **QFontMetrics::QFontMetrics(const QFont & font )**

        Constructs a font metrics object for **font**.

        The font metrics will be compatible with the paintdevice used to create
        **font**.

        The font metrics object holds the information for the font that is
        passed in the constructor at the time it is created, and is not updated
        if the font's attributes are changed later.

        Use QFontMetrics(const **QFont**  &, **QPaintDevice**  *) to get the
        font metrics that are compatible with a certain paint device.
        """
        ...
    @overload
    def __init__(self, arg__1: PySide6.QtGui.QFont | str | Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#QFontMetrics-1

        **[since 5.13] QFontMetrics::QFontMetrics(const QFont & font , const
        QPaintDevice * paintdevice )**

        Constructs a font metrics object for **font** and **paintdevice**.

        The font metrics will be compatible with the paintdevice passed. If the
        **paintdevice** is `nullptr`, the metrics will be screen-compatible, ie.
        the metrics you get if you use the font for drawing text on a
        **widgets**  or **pixmaps** , not on a **QPicture**  or **QPrinter** .

        The font metrics object holds the information for the font that is
        passed in the constructor at the time it is created, and is not updated
        if the font's attributes are changed later.

        This function was introduced in Qt 5.13.
        """
        ...
    @overload
    def __init__(
        self,
        font: PySide6.QtGui.QFont | str | Sequence[str],
        pd: PySide6.QtGui.QPaintDevice,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#QFontMetrics-2

        **QFontMetrics::QFontMetrics(const QFontMetrics & fm )**

        Constructs a copy of **fm**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def ascent(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#ascent

        **int QFontMetrics::ascent() const**

        Returns the ascent of the font.

        The ascent of a font is the distance from the baseline to the highest
        position characters extend to. In practice, some font designers break
        this rule, e.g. when they put more than one accent on top of a
        character, or to accommodate a certain character, so it is possible
        (though rare) that this value will be too small.

        **See also** **descent** ().
        """
        ...
    def averageCharWidth(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#averageCharWidth

        **int QFontMetrics::averageCharWidth() const**

        Returns the average width of glyphs in the font.
        """
        ...
    @overload
    def boundingRect(
        self,
        r: PySide6.QtCore.QRect,
        flags: int,
        text: str,
        tabstops: int,
        tabarray: object = ...,
    ) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#boundingRect

        **QRect QFontMetrics::boundingRect(QChar ch ) const**

        Returns the rectangle that is covered by ink if character **ch** were to
        be drawn at the origin of the coordinate system.

        Note that the bounding rectangle may extend to the left of (0, 0) (e.g.,
        for italicized fonts), and that the text output may cover **all** pixels
        in the bounding rectangle. For a space character the rectangle will
        usually be empty.

        Note that the rectangle usually extends both above and below the base
        line.

        **Warning:** The width of the returned rectangle is not the advance
        width of the character. Use boundingRect(const **QString**  &) or
        **horizontalAdvance** () instead.

        **See also** **horizontalAdvance** ().
        """
        ...
    @overload
    def boundingRect(self, text: str) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#boundingRect-1

        **QRect QFontMetrics::boundingRect(const QString & text ) const**

        Returns the bounding rectangle of the characters in the string specified
        by **text**. The bounding rectangle always covers at least the set of
        pixels the text would cover if drawn at (0, 0).

        Note that the bounding rectangle may extend to the left of (0, 0), e.g.
        for italicized fonts, and that the width of the returned rectangle might
        be different than what the **horizontalAdvance** () method returns.

        If you want to know the advance width of the string (to lay out a set of
        strings next to each other), use **horizontalAdvance** () instead.

        Newline characters are processed as normal characters, **not** as
        linebreaks.

        The height of the bounding rectangle is at least as large as the value
        returned by **height** ().

        **See also** **horizontalAdvance** (), **height** (),
        **QPainter::boundingRect** (), and **tightBoundingRect** ().
        """
        ...
    @overload
    def boundingRect(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        flags: int,
        text: str,
        tabstops: int,
        tabarray: object = ...,
    ) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#boundingRect-2

        **QRect QFontMetrics::boundingRect(const QRect & rect , int flags ,
        const QString & text , int tabStops = 0, int * tabArray = nullptr)
        const**

        This is an overloaded function.

        Returns the bounding rectangle of the characters in the string specified
        by **text** , which is the set of pixels the text would cover if drawn
        at (0, 0). The drawing, and hence the bounding rectangle, is constrained
        to the rectangle **rect**.

        The **flags** argument is the bitwise OR of the following flags:

        * **Qt::AlignLeft**  aligns to the left border, except for Arabic and
        Hebrew where it aligns to the right.
          * **Qt::AlignRight**  aligns to
        the right border, except for Arabic and Hebrew where it aligns to the
        left.
          * **Qt::AlignJustify**  produces justified text.
          *
        **Qt::AlignHCenter**  aligns horizontally centered.
          * **Qt::AlignTop**
        aligns to the top border.
          * **Qt::AlignBottom**  aligns to the bottom
        border.
          * **Qt::AlignVCenter**  aligns vertically centered
          *
        **Qt::AlignCenter**  (== `Qt::AlignHCenter | Qt::AlignVCenter`)
          *
        **Qt::TextSingleLine**  ignores newline characters in the text.
          *
        **Qt::TextExpandTabs**  expands tabs (see below)
          *
        **Qt::TextShowMnemonic**  interprets "&x" as **x** ; i.e., underlined.
        * **Qt::TextWordWrap**  breaks the text to fit the rectangle.

        **Qt::Horizontal**  alignment defaults to **Qt::AlignLeft**  and
        vertical alignment defaults to **Qt::AlignTop** .

        If several of the horizontal or several of the vertical alignment flags
        are set, the resulting alignment is undefined.

        If **Qt::TextExpandTabs**  is set in **flags** , then: if **tabArray**
        is non-null, it specifies a 0-terminated sequence of pixel-positions for
        tabs; otherwise if **tabStops** is non-zero, it is used as the tab
        spacing (in pixels).

        Note that the bounding rectangle may extend to the left of (0, 0), e.g.
        for italicized fonts, and that the text output may cover **all** pixels
        in the bounding rectangle.

        Newline characters are processed as linebreaks.

        Despite the different actual character heights, the heights of the
        bounding rectangles of "Yes" and "yes" are the same.

        The bounding rectangle returned by this function is somewhat larger than
        that calculated by the simpler boundingRect() function. This function
        uses the **maximum left**  and **right**  font bearings as is necessary
        for multi-line text to align correctly. Also, fontHeight() and
        **lineSpacing** () are used to calculate the height, rather than
        individual character heights.

        **See also** **horizontalAdvance** (), **QPainter::boundingRect** (),
        and **Qt::Alignment** .
        """
        ...
    def boundingRectChar(self, arg__1: int) -> PySide6.QtCore.QRect: ...
    def capHeight(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#capHeight

        **[since 5.8] int QFontMetrics::capHeight() const**

        Returns the cap height of the font.

        The cap height of a font is the height of a capital letter above the
        baseline. It specifically is the height of capital letters that are flat
        - such as H or I - as opposed to round letters such as O, or pointed
        letters like A, both of which may display overshoot.

        This function was introduced in Qt 5.8.

        **See also** **ascent** ().
        """
        ...
    def descent(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#descent

        **int QFontMetrics::descent() const**

        Returns the descent of the font.

        The descent is the distance from the base line to the lowest point
        characters extend to. In practice, some font designers break this rule,
        e.g. to accommodate a certain character, so it is possible (though rare)
        that this value will be too small.

        **See also** **ascent** ().
        """
        ...
    def elidedText(
        self,
        text: str,
        mode: PySide6.QtCore.Qt.TextElideMode,
        width: int,
        flags: int = ...,
    ) -> str:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#elidedText

        **QString QFontMetrics::elidedText(const QString & text ,
        Qt::TextElideMode mode , int width , int flags = 0) const**

        If the string **text** is wider than **width** , returns an elided
        version of the string (i.e., a string with "..." in it). Otherwise,
        returns the original string.

        The **mode** parameter specifies whether the text is elided on the left
        (e.g., "...tech"), in the middle (e.g., "Tr...ch"), or on the right
        (e.g., "Trol...").

        The **width** is specified in pixels, not characters.

        The **flags** argument is optional and currently only supports
        **Qt::TextShowMnemonic**  as value.

        The elide mark follows the **layoutdirection** . For example, it will be
        on the right side of the text for right-to-left layouts if the **mode**
        is `Qt::ElideLeft`, and on the left side of the text if the **mode** is
        `Qt::ElideRight`.
        """
        ...
    def fontDpi(self) -> float:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#fontDpi

        **[since 5.14] qreal QFontMetrics::fontDpi() const**

        Returns the font DPI.

        This function was introduced in Qt 5.14.
        """
        ...
    def height(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#height

        **int QFontMetrics::height() const**

        Returns the height of the font.

        This is always equal to **ascent** ()+**descent** ().

        **See also** **leading** () and **lineSpacing** ().
        """
        ...
    def horizontalAdvance(self, arg__1: str, len: int = ...) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#horizontalAdvance

        **[since 5.11] int QFontMetrics::horizontalAdvance(const QString & text
        , int len = -1) const**

        Returns the horizontal advance in pixels of the first **len** characters
        of **text**. If **len** is negative (the default), the entire string is
        used.

        This is the distance appropriate for drawing a subsequent character
        after **text**.

        This function was introduced in Qt 5.11.

        **See also** **boundingRect** ().
        """
        ...
    def horizontalAdvanceChar(self, arg__1: int) -> int: ...
    def inFont(self, arg__1: str) -> bool:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#inFont

        **bool QFontMetrics::inFont(QChar ch ) const**

        Returns `true` if character **ch** is a valid character in the font;
        otherwise returns `false`.
        """
        ...
    def inFontUcs4(self, ucs4: int) -> bool:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#inFontUcs4

        **bool QFontMetrics::inFontUcs4(uint ucs4 ) const**

        Returns `true` if the character **ucs4** encoded in UCS-4/UTF-32 is a
        valid character in the font; otherwise returns `false`.
        """
        ...
    def leading(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#leading

        **int QFontMetrics::leading() const**

        Returns the leading of the font.

        This is the natural inter-line spacing.

        **See also** **height** () and **lineSpacing** ().
        """
        ...
    def leftBearing(self, arg__1: str) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#leftBearing

        **int QFontMetrics::leftBearing(QChar ch ) const**

        Returns the left bearing of character **ch** in the font.

        The left bearing is the right-ward distance of the left-most pixel of
        the character from the logical origin of the character. This value is
        negative if the pixels of the character extend to the left of the
        logical origin.

        See **horizontalAdvance** () for a graphical description of this metric.

        **See also** **rightBearing** (), **minLeftBearing** (), and
        **horizontalAdvance** ().
        """
        ...
    def lineSpacing(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#lineSpacing

        **int QFontMetrics::lineSpacing() const**

        Returns the distance from one base line to the next.

        This value is always equal to **leading** ()+**height** ().

        **See also** **height** () and **leading** ().
        """
        ...
    def lineWidth(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#lineWidth

        **int QFontMetrics::lineWidth() const**

        Returns the width of the underline and strikeout lines, adjusted for the
        point size of the font.

        **See also** **underlinePos** (), **overlinePos** (), and
        **strikeOutPos** ().
        """
        ...
    def maxWidth(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#maxWidth

        **int QFontMetrics::maxWidth() const**

        Returns the width of the widest character in the font.
        """
        ...
    def minLeftBearing(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#minLeftBearing

        **int QFontMetrics::minLeftBearing() const**

        Returns the minimum left bearing of the font.

        This is the smallest **leftBearing** (char) of all characters in the
        font.

        Note that this function can be very slow if the font is large.

        **See also** **minRightBearing** () and **leftBearing** ().
        """
        ...
    def minRightBearing(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#minRightBearing

        **int QFontMetrics::minRightBearing() const**

        Returns the minimum right bearing of the font.

        This is the smallest **rightBearing** (char) of all characters in the
        font.

        Note that this function can be very slow if the font is large.

        **See also** **minLeftBearing** () and **rightBearing** ().
        """
        ...
    def overlinePos(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#overlinePos

        **int QFontMetrics::overlinePos() const**

        Returns the distance from the base line to where an overline should be
        drawn.

        **See also** **underlinePos** (), **strikeOutPos** (), and **lineWidth**
        ().
        """
        ...
    def rightBearing(self, arg__1: str) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#rightBearing

        **int QFontMetrics::rightBearing(QChar ch ) const**

        Returns the right bearing of character **ch** in the font.

        The right bearing is the left-ward distance of the right-most pixel of
        the character from the logical origin of a subsequent character. This
        value is negative if the pixels of the character extend to the right of
        the **horizontalAdvance** () of the character.

        See **horizontalAdvance** () for a graphical description of this metric.

        **See also** **leftBearing** (), **minRightBearing** (), and
        **horizontalAdvance** ().
        """
        ...
    def size(
        self, flags: int, str: str, tabstops: int, tabarray: object = ...
    ) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#size

        **QSize QFontMetrics::size(int flags , const QString & text , int
        tabStops = 0, int * tabArray = nullptr) const**

        Returns the size in pixels of **text**.

        The **flags** argument is the bitwise OR of the following flags:

        * **Qt::TextSingleLine**  ignores newline characters.
          *
        **Qt::TextExpandTabs**  expands tabs (see below)
          *
        **Qt::TextShowMnemonic**  interprets "&x" as **x** ; i.e., underlined.
        * **Qt::TextWordWrap**  breaks the text to fit the rectangle.

        If **Qt::TextExpandTabs**  is set in **flags** , then: if **tabArray**
        is non-null, it specifies a 0-terminated sequence of pixel-positions for
        tabs; otherwise if **tabStops** is non-zero, it is used as the tab
        spacing (in pixels).

        Newline characters are processed as linebreaks.

        Despite the different actual character heights, the heights of the
        bounding rectangles of "Yes" and "yes" are the same.

        **See also** **boundingRect** ().
        """
        ...
    def strikeOutPos(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#strikeOutPos

        **int QFontMetrics::strikeOutPos() const**

        Returns the distance from the base line to where the strikeout line
        should be drawn.

        **See also** **underlinePos** (), **overlinePos** (), and **lineWidth**
        ().
        """
        ...
    def swap(self, other: PySide6.QtGui.QFontMetrics) -> None:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#swap

        **[since 5.0] void QFontMetrics::swap(QFontMetrics & other )**

        Swaps this font metrics instance with **other**. This function is very
        fast and never fails.

        This function was introduced in Qt 5.0.
        """
        ...
    def tightBoundingRect(self, text: str) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#tightBoundingRect

        **QRect QFontMetrics::tightBoundingRect(const QString & text ) const**

        Returns a tight bounding rectangle around the characters in the string
        specified by **text**. The bounding rectangle always covers at least the
        set of pixels the text would cover if drawn at (0, 0).

        Note that the bounding rectangle may extend to the left of (0, 0), e.g.
        for italicized fonts, and that the width of the returned rectangle might
        be different than what the **horizontalAdvance** () method returns.

        If you want to know the advance width of the string (to lay out a set of
        strings next to each other), use **horizontalAdvance** () instead.

        Newline characters are processed as normal characters, **not** as
        linebreaks.

        **Warning:** Calling this method is very slow on Windows.

        **See also** **horizontalAdvance** (), **height** (), and
        **boundingRect** ().
        """
        ...
    def underlinePos(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#underlinePos

        **int QFontMetrics::underlinePos() const**

        Returns the distance from the base line to where an underscore should be
        drawn.

        **See also** **overlinePos** (), **strikeOutPos** (), and **lineWidth**
        ().
        """
        ...
    def xHeight(self) -> int:
        """
        https://doc.qt.io/qt-6/qfontmetrics.html#xHeight

        **int QFontMetrics::xHeight() const**

        Returns the 'x' height of the font. This is often but not always the
        same as the height of the character 'x'.
        """
        ...