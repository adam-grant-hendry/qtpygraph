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
from enum import IntFlag
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtGui

class QTextCharFormat(PySide6.QtGui.QTextFormat):
    """
    https://doc.qt.io/qt-6/qtextcharformat.html

    **Detailed Description**

    The character format of text in a document specifies the visual properties
    of the text, as well as information about its role in a hypertext document.

    The font used can be set by supplying a font to the **setFont** () function,
    and each aspect of its appearance can be adjusted to give the desired
    effect. **setFontFamilies** () and **setFontPointSize** () define the font's
    family (e.g. Times) and printed size; **setFontWeight** () and
    **setFontItalic** () provide control over the style of the font.
    **setFontUnderline** (), **setFontOverline** (), **setFontStrikeOut** (),
    and **setFontFixedPitch** () provide additional effects for text.

    The color is set with **setForeground** (). If the text is intended to be
    used as an anchor (for hyperlinks), this can be enabled with **setAnchor**
    (). The **setAnchorHref** () and **setAnchorNames** () functions are used to
    specify the information about the hyperlink's destination and the anchor's
    name.

    **See also** **QTextFormat** , **QTextBlockFormat** , **QTextTableFormat** ,
    and **QTextListFormat** .
    """

    FontPropertiesSpecifiedOnly: QTextCharFormat.FontPropertiesInheritanceBehavior = ...
    FontPropertiesAll: QTextCharFormat.FontPropertiesInheritanceBehavior = ...
    NoUnderline: QTextCharFormat.UnderlineStyle = ...
    SingleUnderline: QTextCharFormat.UnderlineStyle = ...
    DashUnderline: QTextCharFormat.UnderlineStyle = ...
    DotLine: QTextCharFormat.UnderlineStyle = ...
    DashDotLine: QTextCharFormat.UnderlineStyle = ...
    DashDotDotLine: QTextCharFormat.UnderlineStyle = ...
    WaveUnderline: QTextCharFormat.UnderlineStyle = ...
    SpellCheckUnderline: QTextCharFormat.UnderlineStyle = ...
    AlignNormal: QTextCharFormat.VerticalAlignment = ...
    AlignSuperScript: QTextCharFormat.VerticalAlignment = ...
    AlignSubScript: QTextCharFormat.VerticalAlignment = ...
    AlignMiddle: QTextCharFormat.VerticalAlignment = ...
    AlignTop: QTextCharFormat.VerticalAlignment = ...
    AlignBottom: QTextCharFormat.VerticalAlignment = ...
    AlignBaseline: QTextCharFormat.VerticalAlignment = ...

    class FontPropertiesInheritanceBehavior(IntFlag):
        FontPropertiesSpecifiedOnly: QTextCharFormat.FontPropertiesInheritanceBehavior = (
            ...
        )
        FontPropertiesAll: QTextCharFormat.FontPropertiesInheritanceBehavior = ...

    class UnderlineStyle(IntFlag):
        NoUnderline: QTextCharFormat.UnderlineStyle = ...
        SingleUnderline: QTextCharFormat.UnderlineStyle = ...
        DashUnderline: QTextCharFormat.UnderlineStyle = ...
        DotLine: QTextCharFormat.UnderlineStyle = ...
        DashDotLine: QTextCharFormat.UnderlineStyle = ...
        DashDotDotLine: QTextCharFormat.UnderlineStyle = ...
        WaveUnderline: QTextCharFormat.UnderlineStyle = ...
        SpellCheckUnderline: QTextCharFormat.UnderlineStyle = ...

    class VerticalAlignment(IntFlag):
        AlignNormal: QTextCharFormat.VerticalAlignment = ...
        AlignSuperScript: QTextCharFormat.VerticalAlignment = ...
        AlignSubScript: QTextCharFormat.VerticalAlignment = ...
        AlignMiddle: QTextCharFormat.VerticalAlignment = ...
        AlignTop: QTextCharFormat.VerticalAlignment = ...
        AlignBottom: QTextCharFormat.VerticalAlignment = ...
        AlignBaseline: QTextCharFormat.VerticalAlignment = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#QTextCharFormat

        **QTextCharFormat::QTextCharFormat()**

        Constructs a new character format object.
        """
        ...
    @overload
    def __init__(self, QTextCharFormat: PySide6.QtGui.QTextCharFormat) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#QTextCharFormat

        **QTextCharFormat::QTextCharFormat()**

        Constructs a new character format object.
        """
        ...
    @overload
    def __init__(self, fmt: PySide6.QtGui.QTextFormat) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#QTextCharFormat

        **QTextCharFormat::QTextCharFormat()**

        Constructs a new character format object.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def anchorHref(self) -> str:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#anchorHref

        **QString QTextCharFormat::anchorHref() const**

        Returns the text format's hypertext link, or an empty string if none has
        been set.

        **See also** **setAnchorHref** ().
        """
        ...
    def anchorNames(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#anchorNames

        **QStringList QTextCharFormat::anchorNames() const**

        Returns the anchor names associated with this text format, or an empty
        string list if none has been set. If the anchor names are set, text with
        this format can be the destination of a hypertext link.

        **See also** **setAnchorNames** ().
        """
        ...
    def baselineOffset(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#baselineOffset

        **[since 6.0] qreal QTextCharFormat::baselineOffset() const**

        Returns the the baseline offset in %.

        This function was introduced in Qt 6.0.

        **See also** **setBaselineOffset** (), **setSubScriptBaseline** (),
        **subScriptBaseline** (), **setSuperScriptBaseline** (), and
        **superScriptBaseline** ().
        """
        ...
    def font(self) -> PySide6.QtGui.QFont:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#font

        **QFont QTextCharFormat::font() const**

        Returns the font for this character format.

        **See also** **setFont** ().
        """
        ...
    def fontCapitalization(self) -> PySide6.QtGui.QFont.Capitalization:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontCapitalization

        **QFont::Capitalization QTextCharFormat::fontCapitalization() const**

        Returns the current capitalization type of the font.

        **See also** **setFontCapitalization** ().
        """
        ...
    def fontFamilies(self) -> Any:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontFamilies

        **[since 5.13] QVariant QTextCharFormat::fontFamilies() const**

        Returns the text format's font families.

        This function was introduced in Qt 5.13.

        **See also** **setFontFamilies** () and **font** ().
        """
        ...
    def fontFamily(self) -> str: ...
    def fontFixedPitch(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontFixedPitch

        **bool QTextCharFormat::fontFixedPitch() const**

        Returns `true` if the text format's font is fixed pitch; otherwise
        returns `false`.

        **See also** **setFontFixedPitch** () and **font** ().
        """
        ...
    def fontHintingPreference(self) -> PySide6.QtGui.QFont.HintingPreference:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontHintingPreference

        **QFont::HintingPreference QTextCharFormat::fontHintingPreference()
        const**

        Returns the hinting preference set for this text format.

        **See also** **setFontHintingPreference** (), **font** (), and
        **QFont::hintingPreference** ().
        """
        ...
    def fontItalic(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontItalic

        **bool QTextCharFormat::fontItalic() const**

        Returns `true` if the text format's font is italic; otherwise returns
        `false`.

        **See also** **setFontItalic** () and **font** ().
        """
        ...
    def fontKerning(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontKerning

        **bool QTextCharFormat::fontKerning() const**

        Returns `true` if the font kerning is enabled.

        **See also** **setFontKerning** () and **font** ().
        """
        ...
    def fontLetterSpacing(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontLetterSpacing

        **qreal QTextCharFormat::fontLetterSpacing() const**

        Returns the current letter spacing.

        **See also** **setFontLetterSpacing** (), **setFontLetterSpacingType**
        (), and **fontLetterSpacingType** ().
        """
        ...
    def fontLetterSpacingType(self) -> PySide6.QtGui.QFont.SpacingType:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontLetterSpacingType

        **[since 5.0] QFont::SpacingType
        QTextCharFormat::fontLetterSpacingType() const**

        Returns the letter spacing type of this format..

        This function was introduced in Qt 5.0.

        **See also** **setFontLetterSpacingType** (), **setFontLetterSpacing**
        (), and **fontLetterSpacing** ().
        """
        ...
    def fontOverline(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontOverline

        **bool QTextCharFormat::fontOverline() const**

        Returns `true` if the text format's font is overlined; otherwise returns
        `false`.

        **See also** **setFontOverline** () and **font** ().
        """
        ...
    def fontPointSize(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontPointSize

        **qreal QTextCharFormat::fontPointSize() const**

        Returns the font size used to display text in this format.

        **See also** **setFontPointSize** () and **font** ().
        """
        ...
    def fontStretch(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontStretch

        **[since 5.0] int QTextCharFormat::fontStretch() const**

        Returns the current font stretching.

        This function was introduced in Qt 5.0.

        **See also** **setFontStretch** ().
        """
        ...
    def fontStrikeOut(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontStrikeOut

        **bool QTextCharFormat::fontStrikeOut() const**

        Returns `true` if the text format's font is struck out (has a horizontal
        line drawn through it); otherwise returns `false`.

        **See also** **setFontStrikeOut** () and **font** ().
        """
        ...
    def fontStyleHint(self) -> PySide6.QtGui.QFont.StyleHint:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontStyleHint

        **QFont::StyleHint QTextCharFormat::fontStyleHint() const**

        Returns the font style hint.

        **See also** **setFontStyleHint** () and **font** ().
        """
        ...
    def fontStyleName(self) -> Any:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontStyleName

        **[since 5.13] QVariant QTextCharFormat::fontStyleName() const**

        Returns the text format's font style name.

        This function was introduced in Qt 5.13.

        **See also** **setFontStyleName** (), **font** (), and
        **QFont::styleName** ().
        """
        ...
    def fontStyleStrategy(self) -> PySide6.QtGui.QFont.StyleStrategy:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontStyleStrategy

        **QFont::StyleStrategy QTextCharFormat::fontStyleStrategy() const**

        Returns the current font style strategy.

        **See also** **setFontStyleStrategy** () and **font** ().
        """
        ...
    def fontUnderline(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontUnderline

        **bool QTextCharFormat::fontUnderline() const**

        Returns `true` if the text format's font is underlined; otherwise
        returns `false`.

        **See also** **setFontUnderline** () and **font** ().
        """
        ...
    def fontWeight(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontWeight

        **int QTextCharFormat::fontWeight() const**

        Returns the text format's font weight.

        **See also** **setFontWeight** (), **font** (), and **QFont::Weight** .
        """
        ...
    def fontWordSpacing(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#fontWordSpacing

        **qreal QTextCharFormat::fontWordSpacing() const**

        Returns the current word spacing value.

        **See also** **setFontWordSpacing** ().
        """
        ...
    def isAnchor(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#isAnchor

        **bool QTextCharFormat::isAnchor() const**

        Returns `true` if the text is formatted as an anchor; otherwise returns
        `false`.

        **See also** **setAnchor** (), **setAnchorHref** (), and
        **setAnchorNames** ().
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#isValid

        **bool QTextCharFormat::isValid() const**

        Returns `true` if this character format is valid; otherwise returns
        false.
        """
        ...
    def setAnchor(self, anchor: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setAnchor

        **void QTextCharFormat::setAnchor(bool anchor )**

        If **anchor** is true, text with this format represents an anchor, and
        is formatted in the appropriate way; otherwise the text is formatted
        normally. (Anchors are hyperlinks which are often shown underlined and
        in a different color from plain text.)

        The way the text is rendered is independent of whether or not the format
        has a valid anchor defined. Use **setAnchorHref** (), and optionally
        **setAnchorNames** () to create a hypertext link.

        **See also** **isAnchor** ().
        """
        ...
    def setAnchorHref(self, value: str) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setAnchorHref

        **void QTextCharFormat::setAnchorHref(const QString & value )**

        Sets the hypertext link for the text format to the given **value**. This
        is typically a URL like "http://example.com/index.html".

        The anchor will be displayed with the **value** as its display text; if
        you want to display different text call **setAnchorNames** ().

        To format the text as a hypertext link use **setAnchor** ().

        **See also** **anchorHref** ().
        """
        ...
    def setAnchorNames(self, names: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setAnchorNames

        **void QTextCharFormat::setAnchorNames(const QStringList & names )**

        Sets the text format's anchor **names**. For the anchor to work as a
        hyperlink, the destination must be set with **setAnchorHref** () and the
        anchor must be enabled with **setAnchor** ().

        **See also** **anchorNames** ().
        """
        ...
    def setBaselineOffset(self, baseline: float) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setBaselineOffset

        **[since 6.0] void QTextCharFormat::setBaselineOffset(qreal baseline )**

        Sets the base line (in % of height) of text to **baseline**. A positive
        value moves the text up, by the corresponding %; a negative value moves
        it down. The default value is 0.

        This function was introduced in Qt 6.0.

        **See also** **baselineOffset** (), **setSubScriptBaseline** (),
        **subScriptBaseline** (), **setSuperScriptBaseline** (), and
        **superScriptBaseline** ().
        """
        ...
    def setFont(
        self,
        font: PySide6.QtGui.QFont | str | Sequence[str],
        behavior: PySide6.QtGui.QTextCharFormat.FontPropertiesInheritanceBehavior = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFont

        **[since 5.3] void QTextCharFormat::setFont(const QFont & font ,
        QTextCharFormat::FontPropertiesInheritanceBehavior behavior =
        FontPropertiesAll)**

        Sets the text format's **font**.

        If **behavior** is **QTextCharFormat::FontPropertiesAll** , the font
        property that has not been explicitly set is treated like as it were set
        with default value; If **behavior** is
        **QTextCharFormat::FontPropertiesSpecifiedOnly** , the font property
        that has not been explicitly set is ignored and the respective property
        value remains unchanged.

        This function was introduced in Qt 5.3.

        **See also** **font** ().
        """
        ...
    def setFontCapitalization(
        self, capitalization: PySide6.QtGui.QFont.Capitalization
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontCapitalization

        **void QTextCharFormat::setFontCapitalization(QFont::Capitalization
        capitalization )**

        Sets the capitalization of the text that appears in this font to
        **capitalization**.

        A font's capitalization makes the text appear in the selected
        capitalization mode.

        **See also** **fontCapitalization** ().
        """
        ...
    def setFontFamilies(self, families: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontFamilies

        **[since 5.13] void QTextCharFormat::setFontFamilies(const QStringList &
        families )**

        Sets the text format's font **families**.

        This function was introduced in Qt 5.13.

        **See also** **fontFamilies** () and **setFont** ().
        """
        ...
    def setFontFamily(self, family: str) -> None: ...
    def setFontFixedPitch(self, fixedPitch: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontFixedPitch

        **void QTextCharFormat::setFontFixedPitch(bool fixedPitch )**

        If **fixedPitch** is true, sets the text format's font to be fixed
        pitch; otherwise a non-fixed pitch font is used.

        **See also** **fontFixedPitch** () and **setFont** ().
        """
        ...
    def setFontHintingPreference(
        self, hintingPreference: PySide6.QtGui.QFont.HintingPreference
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontHintingPreference

        **void
        QTextCharFormat::setFontHintingPreference(QFont::HintingPreference
        hintingPreference )**

        Sets the hinting preference of the text format's font to be
        **hintingPreference**.

        **See also** **fontHintingPreference** (), **setFont** (), and
        **QFont::setHintingPreference** ().
        """
        ...
    def setFontItalic(self, italic: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontItalic

        **void QTextCharFormat::setFontItalic(bool italic )**

        If **italic** is true, sets the text format's font to be italic;
        otherwise the font will be non-italic.

        **See also** **fontItalic** () and **setFont** ().
        """
        ...
    def setFontKerning(self, enable: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontKerning

        **void QTextCharFormat::setFontKerning(bool enable )**

        Enables kerning for this font if **enable** is true; otherwise disables
        it.

        When kerning is enabled, glyph metrics do not add up anymore, even for
        Latin text. In other words, the assumption that width('a') + width('b')
        is equal to width("ab") is not neccesairly true.

        **See also** **fontKerning** () and **setFont** ().
        """
        ...
    def setFontLetterSpacing(self, spacing: float) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontLetterSpacing

        **void QTextCharFormat::setFontLetterSpacing(qreal spacing )**

        Sets the letter spacing of this format to the given **spacing**. The
        meaning of the value depends on the font letter spacing type.

        For percentage spacing a value of 100 indicates default spacing; a value
        of 200 doubles the amount of space a letter takes.

        **See also** **fontLetterSpacing** (), **setFontLetterSpacingType** (),
        and **fontLetterSpacingType** ().
        """
        ...
    def setFontLetterSpacingType(
        self, letterSpacingType: PySide6.QtGui.QFont.SpacingType
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontLetterSpacingType

        **[since 5.0] void
        QTextCharFormat::setFontLetterSpacingType(QFont::SpacingType
        letterSpacingType )**

        Sets the letter spacing type of this format to **letterSpacingType**.

        This function was introduced in Qt 5.0.

        **See also** **fontLetterSpacingType** (), **setFontLetterSpacing** (),
        and **fontLetterSpacing** ().
        """
        ...
    def setFontOverline(self, overline: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontOverline

        **void QTextCharFormat::setFontOverline(bool overline )**

        If **overline** is true, sets the text format's font to be overlined;
        otherwise the font is displayed non-overlined.

        **See also** **fontOverline** () and **setFont** ().
        """
        ...
    def setFontPointSize(self, size: float) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontPointSize

        **void QTextCharFormat::setFontPointSize(qreal size )**

        Sets the text format's font **size**.

        **See also** **fontPointSize** () and **setFont** ().
        """
        ...
    def setFontStretch(self, factor: int) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontStretch

        **[since 5.0] void QTextCharFormat::setFontStretch(int factor )**

        Sets the stretch factor for the font to **factor**.

        The stretch factor changes the width of all characters in the font by
        factor percent. For example, setting **factor** to 150 results in all
        characters in the font being 1.5 times (ie. 150%) wider. The default
        stretch factor is 100. The minimum stretch factor is 1, and the maximum
        stretch factor is 4000.

        The stretch factor is only applied to outline fonts. The stretch factor
        is ignored for bitmap fonts.

        This function was introduced in Qt 5.0.

        **See also** **fontStretch** ().
        """
        ...
    def setFontStrikeOut(self, strikeOut: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontStrikeOut

        **void QTextCharFormat::setFontStrikeOut(bool strikeOut )**

        If **strikeOut** is true, sets the text format's font with strike-out
        enabled (with a horizontal line through it); otherwise it is displayed
        without strikeout.

        **See also** **fontStrikeOut** () and **setFont** ().
        """
        ...
    def setFontStyleHint(
        self,
        hint: PySide6.QtGui.QFont.StyleHint,
        strategy: PySide6.QtGui.QFont.StyleStrategy = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontStyleHint

        **void QTextCharFormat::setFontStyleHint(QFont::StyleHint hint ,
        QFont::StyleStrategy strategy = QFont::PreferDefault)**

        Sets the font style **hint** and **strategy**.

        Qt does not support style hints on X11 since this information is not
        provided by the window system.

        **See also** **fontStyleHint** (), **setFont** (), and
        **QFont::setStyleHint** ().
        """
        ...
    def setFontStyleName(self, styleName: str) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontStyleName

        **[since 5.13] void QTextCharFormat::setFontStyleName(const QString &
        styleName )**

        Sets the text format's font **styleName**.

        This function was introduced in Qt 5.13.

        **See also** **fontStyleName** (), **setFont** (), and
        **QFont::setStyleName** ().
        """
        ...
    def setFontStyleStrategy(self, strategy: PySide6.QtGui.QFont.StyleStrategy) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontStyleStrategy

        **void QTextCharFormat::setFontStyleStrategy(QFont::StyleStrategy
        strategy )**

        Sets the font style **strategy**.

        **See also** **fontStyleStrategy** (), **setFont** (), and
        **QFont::setStyleStrategy** ().
        """
        ...
    def setFontUnderline(self, underline: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontUnderline

        **void QTextCharFormat::setFontUnderline(bool underline )**

        If **underline** is true, sets the text format's font to be underlined;
        otherwise it is displayed non-underlined.

        **See also** **fontUnderline** () and **setFont** ().
        """
        ...
    def setFontWeight(self, weight: int) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontWeight

        **void QTextCharFormat::setFontWeight(int weight )**

        Sets the text format's font weight to **weight**.

        **See also** **fontWeight** (), **setFont** (), and **QFont::Weight** .
        """
        ...
    def setFontWordSpacing(self, spacing: float) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setFontWordSpacing

        **void QTextCharFormat::setFontWordSpacing(qreal spacing )**

        Sets the word spacing of this format to the given **spacing** , in
        pixels.

        **See also** **fontWordSpacing** ().
        """
        ...
    def setSubScriptBaseline(self, baseline: float) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setSubScriptBaseline

        **[since 6.0] void QTextCharFormat::setSubScriptBaseline(qreal baseline
        )**

        Sets the subscript's base line as a % of font height to **baseline**.
        The default value is 16.67% (1/6 of height)

        This function was introduced in Qt 6.0.

        **See also** **subScriptBaseline** (), **setSuperScriptBaseline** (),
        **superScriptBaseline** (), **setBaselineOffset** (), and
        **baselineOffset** ().
        """
        ...
    def setSuperScriptBaseline(self, baseline: float) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setSuperScriptBaseline

        **[since 6.0] void QTextCharFormat::setSuperScriptBaseline(qreal
        baseline )**

        Sets the superscript's base line as a % of font height to **baseline**.
        The default value is 50% (1/2 of height).

        This function was introduced in Qt 6.0.

        **See also** **superScriptBaseline** (), **setSubScriptBaseline** (),
        **subScriptBaseline** (), **setBaselineOffset** (), and
        **baselineOffset** ().
        """
        ...
    def setTableCellColumnSpan(self, tableCellColumnSpan: int) -> None: ...
    def setTableCellRowSpan(self, tableCellRowSpan: int) -> None: ...
    def setTextOutline(
        self,
        pen: PySide6.QtGui.QPen | PySide6.QtCore.Qt.PenStyle | PySide6.QtGui.QColor,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setTextOutline

        **void QTextCharFormat::setTextOutline(const QPen & pen )**

        Sets the pen used to draw the outlines of characters to the given
        **pen**.

        **See also** **textOutline** ().
        """
        ...
    def setToolTip(self, tip: str) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setToolTip

        **void QTextCharFormat::setToolTip(const QString & text )**

        Sets the tool tip for a fragment of text to the given **text**.

        **See also** **toolTip** ().
        """
        ...
    def setUnderlineColor(
        self,
        color: (
            PySide6.QtGui.QColor
            | PySide6.QtGui.QRgba64
            | Any
            | PySide6.QtCore.Qt.GlobalColor
            | str
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setUnderlineColor

        **void QTextCharFormat::setUnderlineColor(const QColor & color )**

        Sets the color used to draw underlines, overlines and strikeouts on the
        characters with this format to the **color** specified.

        **See also** **underlineColor** ().
        """
        ...
    def setUnderlineStyle(
        self, style: PySide6.QtGui.QTextCharFormat.UnderlineStyle
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setUnderlineStyle

        **void
        QTextCharFormat::setUnderlineStyle(QTextCharFormat::UnderlineStyle style
        )**

        Sets the style of underlining the text to **style**.

        **See also** **underlineStyle** ().
        """
        ...
    def setVerticalAlignment(
        self, alignment: PySide6.QtGui.QTextCharFormat.VerticalAlignment
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#setVerticalAlignment

        **void
        QTextCharFormat::setVerticalAlignment(QTextCharFormat::VerticalAlignment
        alignment )**

        Sets the vertical alignment used for the characters with this format to
        the **alignment** specified.

        **See also** **verticalAlignment** ().
        """
        ...
    def subScriptBaseline(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#subScriptBaseline

        **[since 6.0] qreal QTextCharFormat::subScriptBaseline() const**

        Returns the subscript's base line as a % of font height.

        This function was introduced in Qt 6.0.

        **See also** **setSubScriptBaseline** (), **setSuperScriptBaseline** (),
        **superScriptBaseline** (), **setBaselineOffset** (), and
        **baselineOffset** ().
        """
        ...
    def superScriptBaseline(self) -> float:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#superScriptBaseline

        **[since 6.0] qreal QTextCharFormat::superScriptBaseline() const**

        Returns the superscript's base line as a % of font height.

        This function was introduced in Qt 6.0.

        **See also** **setSuperScriptBaseline** (), **setSubScriptBaseline** (),
        **subScriptBaseline** (), **setBaselineOffset** (), and
        **baselineOffset** ().
        """
        ...
    def tableCellColumnSpan(self) -> int: ...
    def tableCellRowSpan(self) -> int: ...
    def textOutline(self) -> PySide6.QtGui.QPen:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#textOutline

        **QPen QTextCharFormat::textOutline() const**

        Returns the pen used to draw the outlines of characters in this format.

        **See also** **setTextOutline** ().
        """
        ...
    def toolTip(self) -> str:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#toolTip

        **QString QTextCharFormat::toolTip() const**

        Returns the tool tip that is displayed for a fragment of text.

        **See also** **setToolTip** ().
        """
        ...
    def underlineColor(self) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#underlineColor

        **QColor QTextCharFormat::underlineColor() const**

        Returns the color used to draw underlines, overlines and strikeouts on
        the characters with this format.

        **See also** **setUnderlineColor** ().
        """
        ...
    def underlineStyle(self) -> PySide6.QtGui.QTextCharFormat.UnderlineStyle:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#underlineStyle

        **QTextCharFormat::UnderlineStyle QTextCharFormat::underlineStyle()
        const**

        Returns the style of underlining the text.

        **See also** **setUnderlineStyle** ().
        """
        ...
    def verticalAlignment(self) -> PySide6.QtGui.QTextCharFormat.VerticalAlignment:
        """
        https://doc.qt.io/qt-6/qtextcharformat.html#verticalAlignment

        **QTextCharFormat::VerticalAlignment
        QTextCharFormat::verticalAlignment() const**

        Returns the vertical alignment used for characters with this format.

        **See also** **setVerticalAlignment** ().
        """
        ...