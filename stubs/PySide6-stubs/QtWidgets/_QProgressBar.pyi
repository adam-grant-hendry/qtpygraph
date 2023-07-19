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

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QProgressBar(PySide6.QtWidgets.QWidget):
    """
    https://doc.qt.io/qt-6/qprogressbar.html

    **Detailed Description**

    ![](images/windows-progressbar.png)

    A progress bar is used to give the user an indication of the progress of an
    operation and to reassure them that the application is still running.

    The progress bar uses the concept of **steps**. You set it up by specifying
    the minimum and maximum possible step values, and it will display the
    percentage of steps that have been completed when you later give it the
    current step value. The percentage is calculated by dividing the progress
    (**value** () - **minimum** ()) divided by **maximum** () - **minimum** ().

    You can specify the minimum and maximum number of steps with **setMinimum**
    () and **setMaximum** . The current number of steps is set with **setValue**
    (). The progress bar can be rewound to the beginning with **reset** ().

    If minimum and maximum both are set to 0, the bar shows a busy indicator
    instead of a percentage of steps. This is useful, for example, when using
    QNetworkAccessManager to download items when they are unable to determine
    the size of the item being downloaded.

    **See also** **QProgressDialog**  and **GUI Design Handbook: Progress
    Indicator** .
    """

    TopToBottom: QProgressBar.Direction = ...
    BottomToTop: QProgressBar.Direction = ...

    class Direction(IntFlag):
        TopToBottom: QProgressBar.Direction = ...
        BottomToTop: QProgressBar.Direction = ...
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#QProgressBar

        **QProgressBar::QProgressBar(QWidget * parent = nullptr)**

        Constructs a progress bar with the given **parent**.

        By default, the minimum step value is set to 0, and the maximum to 100.

        **See also** **setRange** ().
        """
        ...
    def alignment(self) -> PySide6.QtCore.Qt.Alignment:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#alignment-prop

        **alignment : Qt::Alignment**

        This property holds the alignment of the progress bar

        **Access functions:**

        Qt::Alignment **alignment** () const
        void **setAlignment**
        (Qt::Alignment **alignment** )
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#event

        **[override virtual protected] bool QProgressBar::event(QEvent * e )**

        Reimplements: **QWidget::event** (QEvent *event).
        """
        ...
    def format(self) -> str:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#format-prop

        **format : QString**

        This property holds the string used to generate the current text

        %p - is replaced by the percentage completed. %v - is replaced by the
        current value. %m - is replaced by the total number of steps.

        The default value is "%p%".

        **Access functions:**

        QString **format** () const
        void **setFormat** (const QString &
        **format** )
        void **resetFormat** ()

        **See also** **text** ().
        """
        ...
    def initStyleOption(self, option: PySide6.QtWidgets.QStyleOptionProgressBar) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#initStyleOption

        **[virtual protected] void
        QProgressBar::initStyleOption(QStyleOptionProgressBar * option ) const**

        Initialize **option** with the values from this **QProgressBar** . This
        method is useful for subclasses when they need a
        **QStyleOptionProgressBar** , but don't want to fill in all the
        information themselves.

        **See also** **QStyleOption::initFrom** ().
        """
        ...
    def invertedAppearance(self) -> bool:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#invertedAppearance-prop

        **invertedAppearance : bool**

        This property holds whether or not a progress bar shows its progress
        inverted

        If this property is `true`, the progress bar grows in the other
        direction (e.g. from right to left). By default, the progress bar is not
        inverted.

        **Access functions:**

        bool **invertedAppearance** () const
        void **setInvertedAppearance**
        (bool **invert** )

        **See also** **orientation**  and **layoutDirection** .
        """
        ...
    def isTextVisible(self) -> bool: ...
    def maximum(self) -> int:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#maximum-prop

        **maximum : int**

        This property holds the progress bar's maximum value

        When setting this property, the **minimum**  is adjusted if necessary to
        ensure that the range remains valid. If the current value falls outside
        the new range, the progress bar is reset with **reset** ().

        **Access functions:**

        int **maximum** () const
        void **setMaximum** (int **maximum** )
        """
        ...
    def minimum(self) -> int:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#minimum-prop

        **minimum : int**

        This property holds the progress bar's minimum value

        When setting this property, the **maximum**  is adjusted if necessary to
        ensure that the range remains valid. If the current value falls outside
        the new range, the progress bar is reset with **reset** ().

        **Access functions:**

        int **minimum** () const
        void **setMinimum** (int **minimum** )
        """
        ...
    def minimumSizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#minimumSizeHint

        **[override virtual] QSize QProgressBar::minimumSizeHint() const**

        Reimplements an access function for property:
        **QWidget::minimumSizeHint** .
        """
        ...
    def orientation(self) -> PySide6.QtCore.Qt.Orientation:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#orientation-prop

        **orientation : Qt::Orientation**

        This property holds the orientation of the progress bar

        The orientation must be **Qt::Horizontal**  (the default) or
        **Qt::Vertical** .

        **Access functions:**

        Qt::Orientation **orientation** () const
        void **setOrientation**
        (Qt::Orientation)

        **See also** **invertedAppearance**  and **textDirection** .
        """
        ...
    def paintEvent(self, arg__1: PySide6.QtGui.QPaintEvent) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#paintEvent

        **[override virtual protected] void QProgressBar::paintEvent(QPaintEvent
        *)**

        Reimplements: **QWidget::paintEvent** (QPaintEvent *event).
        """
        ...
    def reset(self) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#reset

        **[slot] void QProgressBar::reset()**

        Reset the progress bar. The progress bar "rewinds" and shows no
        progress.
        """
        ...
    def resetFormat(self) -> None: ...
    def setAlignment(self, alignment: PySide6.QtCore.Qt.Alignment) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#alignment-prop

        **alignment : Qt::Alignment**

        This property holds the alignment of the progress bar

        **Access functions:**

        Qt::Alignment **alignment** () const
        void **setAlignment**
        (Qt::Alignment **alignment** )
        """
        ...
    def setFormat(self, format: str) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#format-prop

        **format : QString**

        This property holds the string used to generate the current text

        %p - is replaced by the percentage completed. %v - is replaced by the
        current value. %m - is replaced by the total number of steps.

        The default value is "%p%".

        **Access functions:**

        QString **format** () const
        void **setFormat** (const QString &
        **format** )
        void **resetFormat** ()

        **See also** **text** ().
        """
        ...
    def setInvertedAppearance(self, invert: bool) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#invertedAppearance-prop

        **invertedAppearance : bool**

        This property holds whether or not a progress bar shows its progress
        inverted

        If this property is `true`, the progress bar grows in the other
        direction (e.g. from right to left). By default, the progress bar is not
        inverted.

        **Access functions:**

        bool **invertedAppearance** () const
        void **setInvertedAppearance**
        (bool **invert** )

        **See also** **orientation**  and **layoutDirection** .
        """
        ...
    def setMaximum(self, maximum: int) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#maximum-prop

        **maximum : int**

        This property holds the progress bar's maximum value

        When setting this property, the **minimum**  is adjusted if necessary to
        ensure that the range remains valid. If the current value falls outside
        the new range, the progress bar is reset with **reset** ().

        **Access functions:**

        int **maximum** () const
        void **setMaximum** (int **maximum** )
        """
        ...
    def setMinimum(self, minimum: int) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#minimum-prop

        **minimum : int**

        This property holds the progress bar's minimum value

        When setting this property, the **maximum**  is adjusted if necessary to
        ensure that the range remains valid. If the current value falls outside
        the new range, the progress bar is reset with **reset** ().

        **Access functions:**

        int **minimum** () const
        void **setMinimum** (int **minimum** )
        """
        ...
    def setOrientation(self, arg__1: PySide6.QtCore.Qt.Orientation) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#orientation-prop

        **orientation : Qt::Orientation**

        This property holds the orientation of the progress bar

        The orientation must be **Qt::Horizontal**  (the default) or
        **Qt::Vertical** .

        **Access functions:**

        Qt::Orientation **orientation** () const
        void **setOrientation**
        (Qt::Orientation)

        **See also** **invertedAppearance**  and **textDirection** .
        """
        ...
    def setRange(self, minimum: int, maximum: int) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#setRange

        **[slot] void QProgressBar::setRange(int minimum , int maximum )**

        Sets the progress bar's minimum and maximum values to **minimum** and
        **maximum** respectively.

        If **maximum** is smaller than **minimum** , **minimum** becomes the
        only legal value.

        If the current value falls outside the new range, the progress bar is
        reset with **reset** ().

        The **QProgressBar**  can be set to undetermined state by using
        setRange(0, 0).

        **See also** **minimum**  and **maximum** .
        """
        ...
    def setTextDirection(
        self, textDirection: PySide6.QtWidgets.QProgressBar.Direction
    ) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#textDirection-prop

        **textDirection : Direction**

        This property holds the reading direction of the **text**  for vertical
        progress bars

        This property has no impact on horizontal progress bars. By default, the
        reading direction is **QProgressBar::TopToBottom** .

        **Access functions:**

        QProgressBar::Direction **textDirection** () const
        void
        **setTextDirection** (QProgressBar::Direction **textDirection** )

        **See also** **orientation**  and **textVisible** .
        """
        ...
    def setTextVisible(self, visible: bool) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#textVisible-prop

        **textVisible : bool**

        This property holds whether the current completed percentage should be
        displayed

        This property may be ignored by the style (e.g., QMacStyle never draws
        the text).

        **Access functions:**

        bool **isTextVisible** () const
        void **setTextVisible** (bool
        **visible** )

        **See also** **textDirection** .
        """
        ...
    def setValue(self, value: int) -> None:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#value-prop

        **value : int**

        This property holds the progress bar's current value

        Attempting to change the current value to one outside the minimum-
        maximum range has no effect on the current value.

        **Access functions:**

        int **value** () const
        void **setValue** (int **value** )

        **Notifier signal:**

        void ****valueChanged** ** (int **value** )

        **Member Function Documentation**
        """
        ...
    def sizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#sizeHint

        **[override virtual] QSize QProgressBar::sizeHint() const**

        Reimplements an access function for property: **QWidget::sizeHint** .
        """
        ...
    def text(self) -> str:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#text-prop

        **[read-only] text : const QString**

        This property holds the descriptive text shown with the progress bar

        The text returned is the same as the text displayed in the center (or in
        some styles, to the left) of the progress bar.

        The progress shown in the text may be smaller than the minimum value,
        indicating that the progress bar is in the "reset" state before any
        progress is set.

        In the default implementation, the text either contains a percentage
        value that indicates the progress so far, or it is blank because the
        progress bar is in the reset state.

        **Access functions:**

        virtual QString **text** () const
        """
        ...
    def textDirection(self) -> PySide6.QtWidgets.QProgressBar.Direction:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#textDirection-prop

        **textDirection : Direction**

        This property holds the reading direction of the **text**  for vertical
        progress bars

        This property has no impact on horizontal progress bars. By default, the
        reading direction is **QProgressBar::TopToBottom** .

        **Access functions:**

        QProgressBar::Direction **textDirection** () const
        void
        **setTextDirection** (QProgressBar::Direction **textDirection** )

        **See also** **orientation**  and **textVisible** .
        """
        ...
    def value(self) -> int:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#value-prop

        **value : int**

        This property holds the progress bar's current value

        Attempting to change the current value to one outside the minimum-
        maximum range has no effect on the current value.

        **Access functions:**

        int **value** () const
        void **setValue** (int **value** )

        **Notifier signal:**

        void ****valueChanged** ** (int **value** )

        **Member Function Documentation**
        """
        ...
    @property
    def valueChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qprogressbar.html#valueChanged

        **[signal] void QProgressBar::valueChanged(int value )**

        This signal is emitted when the value shown in the progress bar changes.
        **value** is the new value shown by the progress bar.

        **Note:** Notifier signal for property **value** .
        """
        ...