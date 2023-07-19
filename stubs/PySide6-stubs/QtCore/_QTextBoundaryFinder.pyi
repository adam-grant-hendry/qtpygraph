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

from enum import IntFlag
from typing import overload

import PySide6.QtCore

class QTextBoundaryFinder:
    """
    https://doc.qt.io/qt-6/qtextboundaryfinder.html

    **Detailed Description**

    QTextBoundaryFinder allows to find Unicode text boundaries in a string,
    accordingly to the Unicode text boundary specification (see **Unicode
    Standard Annex #14**  and **Unicode Standard Annex #29** ).

    QTextBoundaryFinder can operate on a **QString**  in four possible modes
    depending on the value of **BoundaryType**.

    Units of Unicode characters that make up what the user thinks of as a
    character or basic unit of the language are here called Grapheme clusters.
    The two unicode characters 'A' + diaeresis do for example form one grapheme
    cluster as the user thinks of them as one character, yet it is in this case
    represented by two unicode code points (see
    <https://www.unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries>).

    Word boundaries are there to locate the start and end of what a language
    considers to be a word (see
    <https://www.unicode.org/reports/tr29/#Word_Boundaries>).

    Line break boundaries give possible places where a line break might happen
    and sentence boundaries will show the beginning and end of whole sentences
    (see <https://www.unicode.org/reports/tr29/#Sentence_Boundaries> and
    <https://www.unicode.org/reports/tr14/>).

    The first position in a string is always a valid boundary and refers to the
    position before the first character. The last position at the length of the
    string is also valid and refers to the position after the last character.
    """

    NotAtBoundary: QTextBoundaryFinder.BoundaryReason = ...
    BreakOpportunity: QTextBoundaryFinder.BoundaryReason = ...
    StartOfItem: QTextBoundaryFinder.BoundaryReason = ...
    EndOfItem: QTextBoundaryFinder.BoundaryReason = ...
    MandatoryBreak: QTextBoundaryFinder.BoundaryReason = ...
    SoftHyphen: QTextBoundaryFinder.BoundaryReason = ...
    Grapheme: QTextBoundaryFinder.BoundaryType = ...
    Word: QTextBoundaryFinder.BoundaryType = ...
    Sentence: QTextBoundaryFinder.BoundaryType = ...
    Line: QTextBoundaryFinder.BoundaryType = ...

    class BoundaryReason(IntFlag):
        NotAtBoundary: QTextBoundaryFinder.BoundaryReason = ...
        BreakOpportunity: QTextBoundaryFinder.BoundaryReason = ...
        StartOfItem: QTextBoundaryFinder.BoundaryReason = ...
        EndOfItem: QTextBoundaryFinder.BoundaryReason = ...
        MandatoryBreak: QTextBoundaryFinder.BoundaryReason = ...
        SoftHyphen: QTextBoundaryFinder.BoundaryReason = ...

    class BoundaryReasons: ...

    class BoundaryType(IntFlag):
        Grapheme: QTextBoundaryFinder.BoundaryType = ...
        Word: QTextBoundaryFinder.BoundaryType = ...
        Sentence: QTextBoundaryFinder.BoundaryType = ...
        Line: QTextBoundaryFinder.BoundaryType = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#QTextBoundaryFinder

        **QTextBoundaryFinder::QTextBoundaryFinder()**

        Constructs an invalid QTextBoundaryFinder object.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtCore.QTextBoundaryFinder) -> None:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#QTextBoundaryFinder-1

        **QTextBoundaryFinder::QTextBoundaryFinder(const QTextBoundaryFinder &
        other )**

        Copies the QTextBoundaryFinder object, **other**.
        """
        ...
    @overload
    def __init__(
        self,
        type: PySide6.QtCore.QTextBoundaryFinder.BoundaryType,
        str: str,
        buffer: bytes | None = ...,
        bufferSize: int = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#QTextBoundaryFinder-2

        **QTextBoundaryFinder::QTextBoundaryFinder(QTextBoundaryFinder::Boundary
        Type type , const QString & string )**

        Creates a QTextBoundaryFinder object of **type** operating on
        **string**.
        """
        ...
    @overload
    def __init__(
        self, type: PySide6.QtCore.QTextBoundaryFinder.BoundaryType, string: str
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#QTextBoundaryFinder-3

        **QTextBoundaryFinder::QTextBoundaryFinder(QTextBoundaryFinder::Boundary
        Type type , const QChar * chars , qsizetype length , unsigned char *
        buffer = nullptr, qsizetype bufferSize = 0)**

        This is an overloaded function.

        The same as QTextBoundaryFinder(type, **QStringView** (chars, length),
        buffer, bufferSize).
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def boundaryReasons(self) -> PySide6.QtCore.QTextBoundaryFinder.BoundaryReasons:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#boundaryReasons

        **QTextBoundaryFinder::BoundaryReasons
        QTextBoundaryFinder::boundaryReasons() const**

        Returns the reasons for the boundary finder to have chosen the current
        position as a boundary.
        """
        ...
    def isAtBoundary(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#isAtBoundary

        **bool QTextBoundaryFinder::isAtBoundary() const**

        Returns `true` if the object's **position** () is currently at a valid
        text boundary.
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#isValid

        **bool QTextBoundaryFinder::isValid() const**

        Returns `true` if the text boundary finder is valid; otherwise returns
        `false`. A default **QTextBoundaryFinder**  is invalid.
        """
        ...
    def position(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#position

        **qsizetype QTextBoundaryFinder::position() const**

        Returns the current position of the **QTextBoundaryFinder** .

        The range is from 0 (the beginning of the string) to the length of the
        string inclusive.

        **See also** **setPosition** ().
        """
        ...
    def setPosition(self, position: int) -> None:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#setPosition

        **void QTextBoundaryFinder::setPosition(qsizetype position )**

        Sets the current position of the **QTextBoundaryFinder**  to
        **position**.

        If **position** is out of bounds, it will be bound to only valid
        positions. In this case, valid positions are from 0 to the length of the
        string inclusive.

        **See also** **position** ().
        """
        ...
    def string(self) -> str:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#string

        **QString QTextBoundaryFinder::string() const**

        Returns the string the **QTextBoundaryFinder**  object operates on.
        """
        ...
    def toEnd(self) -> None:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#toEnd

        **void QTextBoundaryFinder::toEnd()**

        Moves the finder to the end of the string. This is equivalent to
        **setPosition** (string.length()).

        **See also** **setPosition** () and **position** ().
        """
        ...
    def toNextBoundary(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#toNextBoundary

        **qsizetype QTextBoundaryFinder::toNextBoundary()**

        Moves the **QTextBoundaryFinder**  to the next boundary position and
        returns that position.

        Returns -1 if there is no next boundary.
        """
        ...
    def toPreviousBoundary(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#toPreviousBoundary

        **qsizetype QTextBoundaryFinder::toPreviousBoundary()**

        Moves the **QTextBoundaryFinder**  to the previous boundary position and
        returns that position.

        Returns -1 if there is no previous boundary.
        """
        ...
    def toStart(self) -> None:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#toStart

        **void QTextBoundaryFinder::toStart()**

        Moves the finder to the start of the string. This is equivalent to
        **setPosition** (0).

        **See also** **setPosition** () and **position** ().
        """
        ...
    def type(self) -> PySide6.QtCore.QTextBoundaryFinder.BoundaryType:
        """
        https://doc.qt.io/qt-6/qtextboundaryfinder.html#type

        **QTextBoundaryFinder::BoundaryType QTextBoundaryFinder::type() const**

        Returns the type of the **QTextBoundaryFinder** .
        """
        ...