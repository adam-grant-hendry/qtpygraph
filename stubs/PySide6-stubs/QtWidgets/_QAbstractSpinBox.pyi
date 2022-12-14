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
from typing import Any

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QAbstractSpinBox(PySide6.QtWidgets.QWidget):
    """
    https://doc.qt.io/qt-6/qabstractspinbox.html

    **Detailed Description**

    The class is designed as a common super class for widgets like **QSpinBox**
    , **QDoubleSpinBox**  and **QDateTimeEdit**

    Here are the main properties of the class:

    1. **text** : The text that is displayed in the QAbstractSpinBox.
      2.
    **alignment** : The alignment of the text in the QAbstractSpinBox.
      3.
    **wrapping** : Whether the QAbstractSpinBox wraps from the minimum value to
    the maximum value and vice versa.

    QAbstractSpinBox provides a virtual **stepBy** () function that is called
    whenever the user triggers a step. This function takes an integer value to
    signify how many steps were taken. E.g. Pressing **Qt::Key_Down**  will
    trigger a call to **stepBy** (-1).

    When the user triggers a step whilst holding the **Qt::ControlModifier** ,
    QAbstractSpinBox steps by 10 instead of making a single step. This step
    modifier affects wheel events, key events and interaction with the spinbox
    buttons. Note that on macOS, Control corresponds to the Command key.

    Since Qt 5.12, **QStyle::SH_SpinBox_StepModifier**  can be used to select
    which **Qt::KeyboardModifier**  increases the step rate. **Qt::NoModifier**
    disables this feature.

    QAbstractSpinBox also provide a virtual function **stepEnabled** () to
    determine whether stepping up/down is allowed at any point. This function
    returns a bitset of **StepEnabled** .

    **See also** **QAbstractSlider** , **QSpinBox** , **QDoubleSpinBox** ,
    **QDateTimeEdit** , and **Spin Boxes Example** .
    """

    UpDownArrows: QAbstractSpinBox.ButtonSymbols = ...
    PlusMinus: QAbstractSpinBox.ButtonSymbols = ...
    NoButtons: QAbstractSpinBox.ButtonSymbols = ...
    CorrectToPreviousValue: QAbstractSpinBox.CorrectionMode = ...
    CorrectToNearestValue: QAbstractSpinBox.CorrectionMode = ...
    StepNone: QAbstractSpinBox.StepEnabledFlag = ...
    StepUpEnabled: QAbstractSpinBox.StepEnabledFlag = ...
    StepDownEnabled: QAbstractSpinBox.StepEnabledFlag = ...
    DefaultStepType: QAbstractSpinBox.StepType = ...
    AdaptiveDecimalStepType: QAbstractSpinBox.StepType = ...

    class ButtonSymbols(IntFlag):
        UpDownArrows: QAbstractSpinBox.ButtonSymbols = ...
        PlusMinus: QAbstractSpinBox.ButtonSymbols = ...
        NoButtons: QAbstractSpinBox.ButtonSymbols = ...

    class CorrectionMode(IntFlag):
        CorrectToPreviousValue: QAbstractSpinBox.CorrectionMode = ...
        CorrectToNearestValue: QAbstractSpinBox.CorrectionMode = ...

    class StepEnabled: ...

    class StepEnabledFlag(IntFlag):
        StepNone: QAbstractSpinBox.StepEnabledFlag = ...
        StepUpEnabled: QAbstractSpinBox.StepEnabledFlag = ...
        StepDownEnabled: QAbstractSpinBox.StepEnabledFlag = ...

    class StepType(IntFlag):
        DefaultStepType: QAbstractSpinBox.StepType = ...
        AdaptiveDecimalStepType: QAbstractSpinBox.StepType = ...
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#QAbstractSpinBox

        **QAbstractSpinBox::QAbstractSpinBox(QWidget * parent = nullptr)**

        Constructs an abstract spinbox with the given **parent** with default
        **wrapping** , and **alignment**  properties.
        """
        ...
    def alignment(self) -> PySide6.QtCore.Qt.Alignment:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#alignment-prop

        **alignment : Qt::Alignment**

        This property holds the alignment of the spin box

        Possible Values are **Qt::AlignLeft** , **Qt::AlignRight** , and
        **Qt::AlignHCenter** .

        By default, the alignment is **Qt::AlignLeft**

        Attempting to set the alignment to an illegal flag combination does
        nothing.

        **Access functions:**

        Qt::Alignment **alignment** () const
        void **setAlignment**
        (Qt::Alignment **flag** )

        **See also** **Qt::Alignment** .
        """
        ...
    def buttonSymbols(self) -> PySide6.QtWidgets.QAbstractSpinBox.ButtonSymbols:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#buttonSymbols-prop

        **buttonSymbols : ButtonSymbols**

        This property holds the current button symbol mode

        The possible values can be either `UpDownArrows` or `PlusMinus`. The
        default is `UpDownArrows`.

        Note that some styles might render **PlusMinus**  and **UpDownArrows**
        identically.

        **Access functions:**

        QAbstractSpinBox::ButtonSymbols **buttonSymbols** () const
        void
        **setButtonSymbols** (QAbstractSpinBox::ButtonSymbols **bs** )

        **See also** **ButtonSymbols** .
        """
        ...
    def changeEvent(self, event: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#changeEvent

        **[override virtual protected] void QAbstractSpinBox::changeEvent(QEvent
        * event )**

        Reimplements: **QWidget::changeEvent** (QEvent *event).
        """
        ...
    def clear(self) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#clear

        **[virtual slot] void QAbstractSpinBox::clear()**

        Clears the lineedit of all text but prefix and suffix.
        """
        ...
    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#closeEvent

        **[override virtual protected] void
        QAbstractSpinBox::closeEvent(QCloseEvent * event )**

        Reimplements: **QWidget::closeEvent** (QCloseEvent *event).
        """
        ...
    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#contextMenuEvent

        **[override virtual protected] void
        QAbstractSpinBox::contextMenuEvent(QContextMenuEvent * event )**

        Reimplements: **QWidget::contextMenuEvent** (QContextMenuEvent *event).
        """
        ...
    def correctionMode(self) -> PySide6.QtWidgets.QAbstractSpinBox.CorrectionMode:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#correctionMode-prop

        **correctionMode : CorrectionMode**

        This property holds the mode to correct an **Intermediate**  value if
        editing finishes

        The default mode is **QAbstractSpinBox::CorrectToPreviousValue** .

        **Access functions:**

        QAbstractSpinBox::CorrectionMode **correctionMode** () const
        void
        **setCorrectionMode** (QAbstractSpinBox::CorrectionMode **cm** )

        **See also** **acceptableInput** , **validate** (), and **fixup** ().
        """
        ...
    def event(self, event: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#event

        **[override virtual] bool QAbstractSpinBox::event(QEvent * event )**

        Reimplements: **QWidget::event** (QEvent *event).
        """
        ...
    def fixup(self, input: str) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#fixup

        **[virtual] void QAbstractSpinBox::fixup(QString & input ) const**

        This virtual function is called by the **QAbstractSpinBox**  if the
        **input** is not validated to **QValidator::Acceptable**  when Return is
        pressed or **interpretText** () is called. It will try to change the
        text so it is valid. Reimplemented in the various subclasses.
        """
        ...
    def focusInEvent(self, event: PySide6.QtGui.QFocusEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#focusInEvent

        **[override virtual protected] void
        QAbstractSpinBox::focusInEvent(QFocusEvent * event )**

        Reimplements: **QWidget::focusInEvent** (QFocusEvent *event).
        """
        ...
    def focusOutEvent(self, event: PySide6.QtGui.QFocusEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#focusOutEvent

        **[override virtual protected] void
        QAbstractSpinBox::focusOutEvent(QFocusEvent * event )**

        Reimplements: **QWidget::focusOutEvent** (QFocusEvent *event).
        """
        ...
    def hasAcceptableInput(self) -> bool: ...
    def hasFrame(self) -> bool: ...
    def hideEvent(self, event: PySide6.QtGui.QHideEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#hideEvent

        **[override virtual protected] void
        QAbstractSpinBox::hideEvent(QHideEvent * event )**

        Reimplements: **QWidget::hideEvent** (QHideEvent *event).
        """
        ...
    def initStyleOption(self, option: PySide6.QtWidgets.QStyleOptionSpinBox) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#initStyleOption

        **[virtual protected] void
        QAbstractSpinBox::initStyleOption(QStyleOptionSpinBox * option ) const**

        Initialize **option** with the values from this **QSpinBox** . This
        method is useful for subclasses when they need a **QStyleOptionSpinBox**
        , but don't want to fill in all the information themselves.

        **See also** **QStyleOption::initFrom** ().
        """
        ...
    def inputMethodQuery(self, arg__1: PySide6.QtCore.Qt.InputMethodQuery) -> Any:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#inputMethodQuery

        **[override virtual] QVariant
        QAbstractSpinBox::inputMethodQuery(Qt::InputMethodQuery query ) const**

        Reimplements: **QWidget::inputMethodQuery(Qt::InputMethodQuery query)
        const** .
        """
        ...
    def interpretText(self) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#interpretText

        **void QAbstractSpinBox::interpretText()**

        This function interprets the text of the spin box. If the value has
        changed since last interpretation it will emit signals.
        """
        ...
    def isAccelerated(self) -> bool: ...
    def isGroupSeparatorShown(self) -> bool: ...
    def isReadOnly(self) -> bool: ...
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#keyPressEvent

        **[override virtual protected] void
        QAbstractSpinBox::keyPressEvent(QKeyEvent * event )**

        Reimplements: **QWidget::keyPressEvent** (QKeyEvent *event).

        This function handles keyboard input.

        The following keys are handled specifically:

        Enter/ReturnThis will reinterpret the text and emit a signal even if the
        value has not changed since last time a signal was emitted.
        UpThis
        will invoke **stepBy** (1)
        DownThis will invoke **stepBy** (-1)
        Page
        upThis will invoke **stepBy** (10)
        Page downThis will invoke
        **stepBy** (-10)

        **See also** **stepBy** ().
        """
        ...
    def keyReleaseEvent(self, event: PySide6.QtGui.QKeyEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#keyReleaseEvent

        **[override virtual protected] void
        QAbstractSpinBox::keyReleaseEvent(QKeyEvent * event )**

        Reimplements: **QWidget::keyReleaseEvent** (QKeyEvent *event).
        """
        ...
    def keyboardTracking(self) -> bool:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#keyboardTracking-prop

        **keyboardTracking : bool**

        This property holds whether keyboard tracking is enabled for the
        spinbox.

        If keyboard tracking is enabled (the default), the spinbox emits the
        valueChanged() and textChanged() signals while the new value is being
        entered from the keyboard.

        E.g. when the user enters the value 600 by typing 6, 0, and 0, the
        spinbox emits 3 signals with the values 6, 60, and 600 respectively.

        If keyboard tracking is disabled, the spinbox doesn't emit the
        valueChanged() and textChanged() signals while typing. It emits the
        signals later, when the return key is pressed, when keyboard focus is
        lost, or when other spinbox functionality is used, e.g. pressing an
        arrow key.

        **Access functions:**

        bool **keyboardTracking** () const
        void **setKeyboardTracking** (bool
        **kt** )
        """
        ...
    def lineEdit(self) -> PySide6.QtWidgets.QLineEdit:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#lineEdit

        **[protected] QLineEdit *QAbstractSpinBox::lineEdit() const**

        This function returns a pointer to the line edit of the spin box.

        **See also** **setLineEdit** ().
        """
        ...
    def minimumSizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#minimumSizeHint

        **[override virtual] QSize QAbstractSpinBox::minimumSizeHint() const**

        Reimplements an access function for property:
        **QWidget::minimumSizeHint** .
        """
        ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#mouseMoveEvent

        **[override virtual protected] void
        QAbstractSpinBox::mouseMoveEvent(QMouseEvent * event )**

        Reimplements: **QWidget::mouseMoveEvent** (QMouseEvent *event).
        """
        ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#mousePressEvent

        **[override virtual protected] void
        QAbstractSpinBox::mousePressEvent(QMouseEvent * event )**

        Reimplements: **QWidget::mousePressEvent** (QMouseEvent *event).
        """
        ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#mouseReleaseEvent

        **[override virtual protected] void
        QAbstractSpinBox::mouseReleaseEvent(QMouseEvent * event )**

        Reimplements: **QWidget::mouseReleaseEvent** (QMouseEvent *event).
        """
        ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#paintEvent

        **[override virtual protected] void
        QAbstractSpinBox::paintEvent(QPaintEvent * event )**

        Reimplements: **QWidget::paintEvent** (QPaintEvent *event).
        """
        ...
    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#resizeEvent

        **[override virtual protected] void
        QAbstractSpinBox::resizeEvent(QResizeEvent * event )**

        Reimplements: **QWidget::resizeEvent** (QResizeEvent *event).
        """
        ...
    def selectAll(self) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#selectAll

        **[slot] void QAbstractSpinBox::selectAll()**

        Selects all the text in the spinbox except the prefix and suffix.
        """
        ...
    def setAccelerated(self, on: bool) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#accelerated-prop

        **accelerated : bool**

        This property holds whether the spin box will accelerate the frequency
        of the steps when pressing the step Up/Down buttons.

        If enabled the spin box will increase/decrease the value faster the
        longer you hold the button down.

        **Access functions:**

        bool **isAccelerated** () const
        void **setAccelerated** (bool **on** )
        """
        ...
    def setAlignment(self, flag: PySide6.QtCore.Qt.Alignment) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#alignment-prop

        **alignment : Qt::Alignment**

        This property holds the alignment of the spin box

        Possible Values are **Qt::AlignLeft** , **Qt::AlignRight** , and
        **Qt::AlignHCenter** .

        By default, the alignment is **Qt::AlignLeft**

        Attempting to set the alignment to an illegal flag combination does
        nothing.

        **Access functions:**

        Qt::Alignment **alignment** () const
        void **setAlignment**
        (Qt::Alignment **flag** )

        **See also** **Qt::Alignment** .
        """
        ...
    def setButtonSymbols(
        self, bs: PySide6.QtWidgets.QAbstractSpinBox.ButtonSymbols
    ) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#buttonSymbols-prop

        **buttonSymbols : ButtonSymbols**

        This property holds the current button symbol mode

        The possible values can be either `UpDownArrows` or `PlusMinus`. The
        default is `UpDownArrows`.

        Note that some styles might render **PlusMinus**  and **UpDownArrows**
        identically.

        **Access functions:**

        QAbstractSpinBox::ButtonSymbols **buttonSymbols** () const
        void
        **setButtonSymbols** (QAbstractSpinBox::ButtonSymbols **bs** )

        **See also** **ButtonSymbols** .
        """
        ...
    def setCorrectionMode(
        self, cm: PySide6.QtWidgets.QAbstractSpinBox.CorrectionMode
    ) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#correctionMode-prop

        **correctionMode : CorrectionMode**

        This property holds the mode to correct an **Intermediate**  value if
        editing finishes

        The default mode is **QAbstractSpinBox::CorrectToPreviousValue** .

        **Access functions:**

        QAbstractSpinBox::CorrectionMode **correctionMode** () const
        void
        **setCorrectionMode** (QAbstractSpinBox::CorrectionMode **cm** )

        **See also** **acceptableInput** , **validate** (), and **fixup** ().
        """
        ...
    def setFrame(self, arg__1: bool) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#frame-prop

        **frame : bool**

        This property holds whether the spin box draws itself with a frame

        If enabled (the default) the spin box draws itself inside a frame,
        otherwise the spin box draws itself without any frame.

        **Access functions:**

        bool **hasFrame** () const
        void **setFrame** (bool)
        """
        ...
    def setGroupSeparatorShown(self, shown: bool) -> None: ...
    def setKeyboardTracking(self, kt: bool) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#keyboardTracking-prop

        **keyboardTracking : bool**

        This property holds whether keyboard tracking is enabled for the
        spinbox.

        If keyboard tracking is enabled (the default), the spinbox emits the
        valueChanged() and textChanged() signals while the new value is being
        entered from the keyboard.

        E.g. when the user enters the value 600 by typing 6, 0, and 0, the
        spinbox emits 3 signals with the values 6, 60, and 600 respectively.

        If keyboard tracking is disabled, the spinbox doesn't emit the
        valueChanged() and textChanged() signals while typing. It emits the
        signals later, when the return key is pressed, when keyboard focus is
        lost, or when other spinbox functionality is used, e.g. pressing an
        arrow key.

        **Access functions:**

        bool **keyboardTracking** () const
        void **setKeyboardTracking** (bool
        **kt** )
        """
        ...
    def setLineEdit(self, edit: PySide6.QtWidgets.QLineEdit) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#setLineEdit

        **[protected] void QAbstractSpinBox::setLineEdit(QLineEdit * lineEdit
        )**

        Sets the line edit of the spinbox to be **lineEdit** instead of the
        current line edit widget. **lineEdit** cannot be `nullptr`.

        **QAbstractSpinBox**  takes ownership of the new **lineEdit**

        If **QLineEdit::validator** () for the **lineEdit** returns `nullptr`,
        the internal validator of the spinbox will be set on the line edit.

        **See also** **lineEdit** ().
        """
        ...
    def setReadOnly(self, r: bool) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#readOnly-prop

        **readOnly : bool**

        This property holds whether the spin box is read only.

        In read-only mode, the user can still copy the text to the clipboard, or
        drag and drop the text; but cannot edit it.

        The **QLineEdit**  in the **QAbstractSpinBox**  does not show a cursor
        in read-only mode.

        **Access functions:**

        bool **isReadOnly** () const
        void **setReadOnly** (bool **r** )

        **See also** **QLineEdit::readOnly** .
        """
        ...
    def setSpecialValueText(self, txt: str) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#specialValueText-prop

        **specialValueText : QString**

        This property holds the special-value text

        If set, the spin box will display this text instead of a numeric value
        whenever the current value is equal to minimum(). Typical use is to
        indicate that this choice has a special (default) meaning.

        For example, if your spin box allows the user to choose a scale factor
        (or zoom level) for displaying an image, and your application is able to
        automatically choose one that will enable the image to fit completely
        within the display window, you can set up the spin box like this:

        **QSpinBox**  *zoomSpinBox = new **QSpinBox** ;
        zoomSpinBox->setRange(0, 1000);
                zoomSpinBox->setSingleStep(10);
        zoomSpinBox->setSuffix("%");
        zoomSpinBox->setSpecialValueText(tr("Automatic"));
        zoomSpinBox->setValue(100);

        The user will then be able to choose a scale from 1% to 1000% or select
        "Auto" to leave it up to the application to choose. Your code must then
        interpret the spin box value of 0 as a request from the user to scale
        the image to fit inside the window.

        All values are displayed with the prefix and suffix (if set), **except**
        for the special value, which only shows the special value text. This
        special text is passed in the **QSpinBox::textChanged** () signal that
        passes a **QString** .

        To turn off the special-value text display, call this function with an
        empty string. The default is no special-value text, i.e. the numeric
        value is shown as usual.

        If no special-value text is set, specialValueText() returns an empty
        string.

        **Access functions:**

        QString **specialValueText** () const
        void **setSpecialValueText**
        (const QString & **txt** )
        """
        ...
    def setWrapping(self, w: bool) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#wrapping-prop

        **wrapping : bool**

        This property holds whether the spin box is circular.

        If wrapping is true stepping up from maximum() value will take you to
        the minimum() value and vice versa. Wrapping only make sense if you have
        minimum() and maximum() values set.

        **QSpinBox**  *spinBox = new **QSpinBox** (this);
        spinBox->setRange(0, 100);
            spinBox->setWrapping(true);
        spinBox->setValue(100);
            spinBox->stepBy(1);
            // value is 0

        **Access functions:**

        bool **wrapping** () const
        void **setWrapping** (bool **w** )

        **See also** **QSpinBox::minimum** () and **QSpinBox::maximum** ().

        **Member Function Documentation**
        """
        ...
    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#showEvent

        **[override virtual protected] void
        QAbstractSpinBox::showEvent(QShowEvent * event )**

        Reimplements: **QWidget::showEvent** (QShowEvent *event).
        """
        ...
    def sizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#sizeHint

        **[override virtual] QSize QAbstractSpinBox::sizeHint() const**

        Reimplements an access function for property: **QWidget::sizeHint** .
        """
        ...
    def specialValueText(self) -> str:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#specialValueText-prop

        **specialValueText : QString**

        This property holds the special-value text

        If set, the spin box will display this text instead of a numeric value
        whenever the current value is equal to minimum(). Typical use is to
        indicate that this choice has a special (default) meaning.

        For example, if your spin box allows the user to choose a scale factor
        (or zoom level) for displaying an image, and your application is able to
        automatically choose one that will enable the image to fit completely
        within the display window, you can set up the spin box like this:

        **QSpinBox**  *zoomSpinBox = new **QSpinBox** ;
        zoomSpinBox->setRange(0, 1000);
                zoomSpinBox->setSingleStep(10);
        zoomSpinBox->setSuffix("%");
        zoomSpinBox->setSpecialValueText(tr("Automatic"));
        zoomSpinBox->setValue(100);

        The user will then be able to choose a scale from 1% to 1000% or select
        "Auto" to leave it up to the application to choose. Your code must then
        interpret the spin box value of 0 as a request from the user to scale
        the image to fit inside the window.

        All values are displayed with the prefix and suffix (if set), **except**
        for the special value, which only shows the special value text. This
        special text is passed in the **QSpinBox::textChanged** () signal that
        passes a **QString** .

        To turn off the special-value text display, call this function with an
        empty string. The default is no special-value text, i.e. the numeric
        value is shown as usual.

        If no special-value text is set, specialValueText() returns an empty
        string.

        **Access functions:**

        QString **specialValueText** () const
        void **setSpecialValueText**
        (const QString & **txt** )
        """
        ...
    def stepBy(self, steps: int) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#stepBy

        **[virtual] void QAbstractSpinBox::stepBy(int steps )**

        Virtual function that is called whenever the user triggers a step. The
        **steps** parameter indicates how many steps were taken. For example,
        pressing `Qt::Key_Down` will trigger a call to `stepBy(-1)`, whereas
        pressing `Qt::Key_PageUp` will trigger a call to `stepBy(10)`.

        If you subclass `QAbstractSpinBox` you must reimplement this function.
        Note that this function is called even if the resulting value will be
        outside the bounds of minimum and maximum. It's this function's job to
        handle these situations.

        **See also** **stepUp** (), **stepDown** (), and **keyPressEvent** ().
        """
        ...
    def stepDown(self) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#stepDown

        **[slot] void QAbstractSpinBox::stepDown()**

        Steps down by one linestep Calling this slot is analogous to calling
        **stepBy** (-1);

        **See also** **stepBy** () and **stepUp** ().
        """
        ...
    def stepEnabled(self) -> PySide6.QtWidgets.QAbstractSpinBox.StepEnabled:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#stepEnabled

        **[virtual protected] QAbstractSpinBox::StepEnabled
        QAbstractSpinBox::stepEnabled() const**

        Virtual function that determines whether stepping up and down is legal
        at any given time.

        The up arrow will be painted as disabled unless (stepEnabled() &
        **StepUpEnabled** ) != 0.

        The default implementation will return (**StepUpEnabled** |
        **StepDownEnabled** ) if wrapping is turned on. Else it will return
        **StepDownEnabled**  if value is > minimum() or'ed with
        **StepUpEnabled**  if value < maximum().

        If you subclass **QAbstractSpinBox**  you will need to reimplement this
        function.

        **See also** **QSpinBox::minimum** (), **QSpinBox::maximum** (), and
        **wrapping** ().
        """
        ...
    def stepUp(self) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#stepUp

        **[slot] void QAbstractSpinBox::stepUp()**

        Steps up by one linestep Calling this slot is analogous to calling
        **stepBy** (1);

        **See also** **stepBy** () and **stepDown** ().
        """
        ...
    def text(self) -> str:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#text-prop

        **[read-only] text : const QString**

        This property holds the spin box's text, including any prefix and suffix

        There is no default text.

        **Access functions:**

        QString **text** () const
        """
        ...
    def timerEvent(self, event: PySide6.QtCore.QTimerEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#timerEvent

        **[override virtual protected] void
        QAbstractSpinBox::timerEvent(QTimerEvent * event )**

        Reimplements: **QObject::timerEvent** (QTimerEvent *event).
        """
        ...
    def validate(self, input: str, pos: int) -> object:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#validate

        **[virtual] QValidator::State QAbstractSpinBox::validate(QString & input
        , int & pos ) const**

        This virtual function is called by the **QAbstractSpinBox**  to
        determine whether **input** is valid. The **pos** parameter indicates
        the position in the string. Reimplemented in the various subclasses.
        """
        ...
    def wheelEvent(self, event: PySide6.QtGui.QWheelEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#wheelEvent

        **[override virtual protected] void
        QAbstractSpinBox::wheelEvent(QWheelEvent * event )**

        Reimplements: **QWidget::wheelEvent** (QWheelEvent *event).
        """
        ...
    def wrapping(self) -> bool:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#wrapping-prop

        **wrapping : bool**

        This property holds whether the spin box is circular.

        If wrapping is true stepping up from maximum() value will take you to
        the minimum() value and vice versa. Wrapping only make sense if you have
        minimum() and maximum() values set.

        **QSpinBox**  *spinBox = new **QSpinBox** (this);
        spinBox->setRange(0, 100);
            spinBox->setWrapping(true);
        spinBox->setValue(100);
            spinBox->stepBy(1);
            // value is 0

        **Access functions:**

        bool **wrapping** () const
        void **setWrapping** (bool **w** )

        **See also** **QSpinBox::minimum** () and **QSpinBox::maximum** ().

        **Member Function Documentation**
        """
        ...
    @property
    def editingFinished(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qabstractspinbox.html#editingFinished

        **[signal] void QAbstractSpinBox::editingFinished()**

        This signal is emitted editing is finished. This happens when the
        spinbox loses focus and when enter is pressed.
        """
        ...
