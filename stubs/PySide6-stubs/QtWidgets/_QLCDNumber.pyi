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
PySide6.QtWidgets, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QLCDNumber(PySide6.QtWidgets.QFrame):
    """
    https://doc.qt.io/qt-6/qlcdnumber.html

    **Detailed Description**

    ![](images/windows-lcdnumber.png)

    It can display a number in just about any size. It can display decimal,
    hexadecimal, octal or binary numbers. It is easy to connect to data sources
    using the **display** () slot, which is overloaded to take any of five
    argument types.

    There are also slots to change the base with **setMode** () and the decimal
    point with **setSmallDecimalPoint** ().

    QLCDNumber emits the **overflow** () signal when it is asked to display
    something beyond its range. The range is set by **setDigitCount** (), but
    **setSmallDecimalPoint** () also influences it. If the display is set to
    hexadecimal, octal or binary, the integer equivalent of the value is
    displayed.

    These digits and other symbols can be shown: 0/O, 1, 2, 3, 4, 5/S, 6, 7, 8,
    9/g, minus, decimal point, A, B, C, D, E, F, h, H, L, o, P, r, u, U, Y,
    colon, degree sign (which is specified as single quote in the string) and
    space. QLCDNumber substitutes spaces for illegal characters.

    It is not possible to retrieve the contents of a QLCDNumber object, although
    you can retrieve the numeric value with **value** (). If you really need the
    text, we recommend that you connect the signals that feed the **display** ()
    slot to another slot as well and store the value there.

    Incidentally, QLCDNumber is the very oldest part of Qt, tracing its roots
    back to a BASIC program on the **Sinclair Spectrum** .

    **See also** **QLabel** , **QFrame** , **Digital Clock Example** , and
    **Tetrix Example** .
    """

    Hex: QLCDNumber.Mode = ...
    Dec: QLCDNumber.Mode = ...
    Oct: QLCDNumber.Mode = ...
    Bin: QLCDNumber.Mode = ...
    Outline: QLCDNumber.SegmentStyle = ...
    Filled: QLCDNumber.SegmentStyle = ...
    Flat: QLCDNumber.SegmentStyle = ...

    class Mode(IntFlag):
        Hex: QLCDNumber.Mode = ...
        Dec: QLCDNumber.Mode = ...
        Oct: QLCDNumber.Mode = ...
        Bin: QLCDNumber.Mode = ...

    class SegmentStyle(IntFlag):
        Outline: QLCDNumber.SegmentStyle = ...
        Filled: QLCDNumber.SegmentStyle = ...
        Flat: QLCDNumber.SegmentStyle = ...
    @overload
    def __init__(
        self, numDigits: int, parent: PySide6.QtWidgets.QWidget | None = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#QLCDNumber

        **QLCDNumber::QLCDNumber(QWidget * parent = nullptr)**

        Constructs an LCD number, sets the number of digits to 5, the base to
        decimal, the decimal point mode to 'small' and the frame style to a
        raised box. The **segmentStyle** () is set to `Outline`.

        The **parent** argument is passed to the **QFrame**  constructor.

        **See also** **setDigitCount** () and **setSmallDecimalPoint** ().
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#QLCDNumber-1

        **QLCDNumber::QLCDNumber(uint numDigits , QWidget * parent = nullptr)**

        Constructs an LCD number, sets the number of digits to **numDigits** ,
        the base to decimal, the decimal point mode to 'small' and the frame
        style to a raised box. The **segmentStyle** () is set to `Filled`.

        The **parent** argument is passed to the **QFrame**  constructor.

        **See also** **setDigitCount** () and **setSmallDecimalPoint** ().
        """
        ...
    @overload
    def checkOverflow(self, num: float) -> bool:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#checkOverflow

        **bool QLCDNumber::checkOverflow(double num ) const**

        Returns `true` if **num** is too big to be displayed in its entirety;
        otherwise returns `false`.

        **See also** **display** (), **digitCount** (), and
        **smallDecimalPoint** ().
        """
        ...
    @overload
    def checkOverflow(self, num: int) -> bool:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#checkOverflow-1

        **bool QLCDNumber::checkOverflow(int num ) const**

        This is an overloaded function.

        Returns `true` if **num** is too big to be displayed in its entirety;
        otherwise returns `false`.

        **See also** **display** (), **digitCount** (), and
        **smallDecimalPoint** ().
        """
        ...
    def digitCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#digitCount

        **int QLCDNumber::digitCount() const**

        Returns the current number of digits.

        **Note:** Getter function for property digitCount.

        **See also** **setDigitCount** ().
        """
        ...
    @overload
    def display(self, num: float) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#display

        **[slot] void QLCDNumber::display(const QString & s )**

        Displays the number represented by the string **s**.

        This version of the function disregards **mode** () and
        **smallDecimalPoint** ().

        These digits and other symbols can be shown: 0/O, 1, 2, 3, 4, 5/S, 6, 7,
        8, 9/g, minus, decimal point, A, B, C, D, E, F, h, H, L, o, P, r, u, U,
        Y, colon, degree sign (which is specified as single quote in the string)
        and space. **QLCDNumber**  substitutes spaces for illegal characters.

        **Note:** Setter function for property **intValue** . Setter function
        for property **value** .
        """
        ...
    @overload
    def display(self, num: int) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#display-1

        **[slot] void QLCDNumber::display(int num )**

        This is an overloaded function.

        Displays the number **num**.

        **Note:** Setter function for property **intValue** . Setter function
        for property **value** .
        """
        ...
    @overload
    def display(self, str: str) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#display-2

        **[slot] void QLCDNumber::display(double num )**

        This is an overloaded function.

        Displays the number **num**.

        **Note:** Setter function for property **intValue** . Setter function
        for property **value** .
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#event

        **[override virtual protected] bool QLCDNumber::event(QEvent * e )**

        Reimplements: **QFrame::event** (QEvent *e).
        """
        ...
    def intValue(self) -> int:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#intValue-prop

        **intValue : int**

        This property holds the displayed value rounded to the nearest integer

        This property corresponds to the nearest integer to the current value
        displayed by the LCDNumber. This is the value used for hexadecimal,
        octal and binary modes.

        If the displayed value is not a number, the property has a value of 0.

        By default, this property contains a value of 0.

        **Access functions:**

        int **intValue** () const
        void ****display** ** (const QString & **s**
        )
        void ****display** ** (int **num** )
        void ****display** ** (double
        **num** )
        """
        ...
    def mode(self) -> PySide6.QtWidgets.QLCDNumber.Mode:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#mode-prop

        **mode : Mode**

        This property holds the current display mode (number base)

        Corresponds to the current display mode, which is one of `Bin`, `Oct`,
        `Dec` (the default) and `Hex`. `Dec` mode can display floating point
        values, the other modes display the integer equivalent.

        **Access functions:**

        QLCDNumber::Mode **mode** () const
        void **setMode** (QLCDNumber::Mode)

        **See also** **smallDecimalPoint** (), **setHexMode** (), **setDecMode**
        (), **setOctMode** (), and **setBinMode** ().
        """
        ...
    def paintEvent(self, arg__1: PySide6.QtGui.QPaintEvent) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#paintEvent

        **[override virtual protected] void QLCDNumber::paintEvent(QPaintEvent
        *)**

        Reimplements: **QFrame::paintEvent** (QPaintEvent *).
        """
        ...
    def segmentStyle(self) -> PySide6.QtWidgets.QLCDNumber.SegmentStyle:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#segmentStyle-prop

        **segmentStyle : SegmentStyle**

        This property holds the style of the LCDNumber

        StyleResult
        `Outline`Produces raised segments filled with the
        background color
        `Filled` (this is the default).Produces raised
        segments filled with the foreground color.
        `Flat`Produces flat
        segments filled with the foreground color.

        `Outline` and `Filled` will additionally use **QPalette::light** () and
        **QPalette::dark** () for shadow effects.

        **Access functions:**

        QLCDNumber::SegmentStyle **segmentStyle** () const
        void
        **setSegmentStyle** (QLCDNumber::SegmentStyle)
        """
        ...
    def setBinMode(self) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#setBinMode

        **[slot] void QLCDNumber::setBinMode()**

        Calls **setMode** (Bin). Provided for convenience (e.g. for connecting
        buttons to it).

        **See also** **setMode** (), **setHexMode** (), **setDecMode** (),
        **setOctMode** (), and **mode** ().
        """
        ...
    def setDecMode(self) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#setDecMode

        **[slot] void QLCDNumber::setDecMode()**

        Calls **setMode** (Dec). Provided for convenience (e.g. for connecting
        buttons to it).

        **See also** **setMode** (), **setHexMode** (), **setOctMode** (),
        **setBinMode** (), and **mode** ().
        """
        ...
    def setDigitCount(self, nDigits: int) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#setDigitCount

        **void QLCDNumber::setDigitCount(int numDigits )**

        Sets the current number of digits to **numDigits**. Must be in the range
        0..99.

        **Note:** Setter function for property **digitCount** .

        **See also** **digitCount** ().
        """
        ...
    def setHexMode(self) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#setHexMode

        **[slot] void QLCDNumber::setHexMode()**

        Calls **setMode** (Hex). Provided for convenience (e.g. for connecting
        buttons to it).

        **See also** **setMode** (), **setDecMode** (), **setOctMode** (),
        **setBinMode** (), and **mode** ().
        """
        ...
    def setMode(self, arg__1: PySide6.QtWidgets.QLCDNumber.Mode) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#mode-prop

        **mode : Mode**

        This property holds the current display mode (number base)

        Corresponds to the current display mode, which is one of `Bin`, `Oct`,
        `Dec` (the default) and `Hex`. `Dec` mode can display floating point
        values, the other modes display the integer equivalent.

        **Access functions:**

        QLCDNumber::Mode **mode** () const
        void **setMode** (QLCDNumber::Mode)

        **See also** **smallDecimalPoint** (), **setHexMode** (), **setDecMode**
        (), **setOctMode** (), and **setBinMode** ().
        """
        ...
    def setOctMode(self) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#setOctMode

        **[slot] void QLCDNumber::setOctMode()**

        Calls **setMode** (Oct). Provided for convenience (e.g. for connecting
        buttons to it).

        **See also** **setMode** (), **setHexMode** (), **setDecMode** (),
        **setBinMode** (), and **mode** ().
        """
        ...
    def setSegmentStyle(self, arg__1: PySide6.QtWidgets.QLCDNumber.SegmentStyle) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#segmentStyle-prop

        **segmentStyle : SegmentStyle**

        This property holds the style of the LCDNumber

        StyleResult
        `Outline`Produces raised segments filled with the
        background color
        `Filled` (this is the default).Produces raised
        segments filled with the foreground color.
        `Flat`Produces flat
        segments filled with the foreground color.

        `Outline` and `Filled` will additionally use **QPalette::light** () and
        **QPalette::dark** () for shadow effects.

        **Access functions:**

        QLCDNumber::SegmentStyle **segmentStyle** () const
        void
        **setSegmentStyle** (QLCDNumber::SegmentStyle)
        """
        ...
    def setSmallDecimalPoint(self, arg__1: bool) -> None:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#smallDecimalPoint-prop

        **smallDecimalPoint : bool**

        This property holds the style of the decimal point

        If true the decimal point is drawn between two digit positions.
        Otherwise it occupies a digit position of its own, i.e. is drawn in a
        digit position. The default is false.

        The inter-digit space is made slightly wider when the decimal point is
        drawn between the digits.

        **Access functions:**

        bool **smallDecimalPoint** () const
        void **setSmallDecimalPoint**
        (bool)

        **See also** **mode** .
        """
        ...
    def sizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#sizeHint

        **[override virtual] QSize QLCDNumber::sizeHint() const**

        Reimplements: **QFrame::sizeHint() const** .
        """
        ...
    def smallDecimalPoint(self) -> bool:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#smallDecimalPoint-prop

        **smallDecimalPoint : bool**

        This property holds the style of the decimal point

        If true the decimal point is drawn between two digit positions.
        Otherwise it occupies a digit position of its own, i.e. is drawn in a
        digit position. The default is false.

        The inter-digit space is made slightly wider when the decimal point is
        drawn between the digits.

        **Access functions:**

        bool **smallDecimalPoint** () const
        void **setSmallDecimalPoint**
        (bool)

        **See also** **mode** .
        """
        ...
    def value(self) -> float:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#value-prop

        **value : double**

        This property holds the displayed value

        This property corresponds to the current value displayed by the
        LCDNumber.

        If the displayed value is not a number, the property has a value of 0.

        By default, this property contains a value of 0.

        **Access functions:**

        double **value** () const
        void ****display** ** (const QString & **s**
        )
        void ****display** ** (int **num** )
        void ****display** ** (double
        **num** )

        **Member Function Documentation**
        """
        ...
    @property
    def overflow(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlcdnumber.html#overflow

        **[signal] void QLCDNumber::overflow()**

        This signal is emitted whenever the **QLCDNumber**  is asked to display
        a too-large number or a too-long string.

        It is never emitted by **setDigitCount** ().
        """
        ...