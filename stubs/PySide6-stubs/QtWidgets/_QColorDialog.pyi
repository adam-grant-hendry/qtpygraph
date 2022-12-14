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
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QColorDialog(PySide6.QtWidgets.QDialog):
    """
    https://doc.qt.io/qt-6/qcolordialog.html

    **Detailed Description**

    The color dialog's function is to allow users to choose colors. For example,
    you might use this in a drawing program to allow the user to set the brush
    color.

    The static functions provide modal color dialogs.

    The static **getColor** () function shows the dialog, and allows the user to
    specify a color. This function can also be used to let users choose a color
    with a level of transparency: pass the **ShowAlphaChannel**  option as an
    additional argument.

    The user can store **customCount** () different custom colors. The custom
    colors are shared by all color dialogs, and remembered during the execution
    of the program. Use **setCustomColor** () to set the custom colors, and use
    **customColor** () to get them.

    When pressing the "Pick Screen Color" button, the cursor changes to a
    haircross and the colors on the screen are scanned. The user can pick up one
    by clicking the mouse or the Enter button. Pressing Escape restores the last
    color selected before entering this mode.

    The **Standard Dialogs**  example shows how to use QColorDialog as well as
    other built-in Qt dialogs.

    ![A color dialog in the Fusion widget style.](images/fusion-colordialog.png)

    **See also** **QColor** , **QFileDialog** , **QFontDialog** , and **Standard
    Dialogs Example** .
    """

    ShowAlphaChannel: QColorDialog.ColorDialogOption = ...
    NoButtons: QColorDialog.ColorDialogOption = ...
    DontUseNativeDialog: QColorDialog.ColorDialogOption = ...

    class ColorDialogOption(IntFlag):
        ShowAlphaChannel: QColorDialog.ColorDialogOption = ...
        NoButtons: QColorDialog.ColorDialogOption = ...
        DontUseNativeDialog: QColorDialog.ColorDialogOption = ...

    class ColorDialogOptions: ...

    @overload
    def __init__(
        self,
        initial: (
            PySide6.QtGui.QColor
            | PySide6.QtGui.QRgba64
            | Any
            | PySide6.QtCore.Qt.GlobalColor
            | str
            | int
        ),
        parent: PySide6.QtWidgets.QWidget | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#QColorDialog

        **QColorDialog::QColorDialog(QWidget * parent = nullptr)**

        Constructs a color dialog with the given **parent**.
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#QColorDialog-1

        **QColorDialog::QColorDialog(const QColor & initial , QWidget * parent =
        nullptr)**

        Constructs a color dialog with the given **parent** and specified
        **initial** color.
        """
        ...
    def changeEvent(self, event: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#changeEvent

        **[override virtual protected] void QColorDialog::changeEvent(QEvent * e
        )**

        Reimplements: **QWidget::changeEvent** (QEvent *event).
        """
        ...
    def currentColor(self) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#currentColor-prop

        **currentColor : QColor**

        This property holds the currently selected color in the dialog

        **Access functions:**

        QColor **currentColor** () const
        void **setCurrentColor** (const
        QColor & **color** )

        **Notifier signal:**

        void ****currentColorChanged** ** (const QColor & **color** )
        """
        ...
    @staticmethod
    def customColor(index: int) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#customColor

        **[static] QColor QColorDialog::customColor(int index )**

        Returns the custom color at the given **index** as a **QColor**  value.

        **See also** **setCustomColor** ().
        """
        ...
    @staticmethod
    def customCount() -> int:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#customCount

        **[static] int QColorDialog::customCount()**

        Returns the number of custom colors supported by **QColorDialog** . All
        color dialogs share the same custom colors.
        """
        ...
    def done(self, result: int) -> None:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#done

        **[override virtual protected] void QColorDialog::done(int result )**

        Reimplements: **QDialog::done** (int r).

        Closes the dialog and sets its result code to **result**. If this dialog
        is shown with **exec** (), done() causes the local event loop to finish,
        and **exec** () to return **result**.

        **See also** **QDialog::done** ().
        """
        ...
    @staticmethod
    def getColor(
        initial: (
            PySide6.QtGui.QColor
            | PySide6.QtGui.QRgba64
            | Any
            | PySide6.QtCore.Qt.GlobalColor
            | str
            | int
        ) = ...,
        parent: PySide6.QtWidgets.QWidget | None = ...,
        title: str = ...,
        options: PySide6.QtWidgets.QColorDialog.ColorDialogOptions = ...,
    ) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#getColor

        **[static] QColor QColorDialog::getColor(const QColor & initial =
        Qt::white, QWidget * parent = nullptr, const QString & title =
        QString(), QColorDialog::ColorDialogOptions options =
        ColorDialogOptions())**

        Pops up a modal color dialog with the given window **title** (or "Select
        Color" if none is specified), lets the user choose a color, and returns
        that color. The color is initially set to **initial**. The dialog is a
        child of **parent**. It returns an invalid (see **QColor::isValid** ())
        color if the user cancels the dialog.

        The **options** argument allows you to customize the dialog.
        """
        ...
    @overload
    def open(self) -> None:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#open

        **void QColorDialog::open(QObject * receiver , const char * member )**

        Opens the dialog and connects its **colorSelected** () signal to the
        slot specified by **receiver** and **member**.

        The signal will be disconnected from the slot when the dialog is closed.
        """
        ...
    @overload
    def open(self, receiver: PySide6.QtCore.QObject, member: bytes) -> None:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#open

        **void QColorDialog::open(QObject * receiver , const char * member )**

        Opens the dialog and connects its **colorSelected** () signal to the
        slot specified by **receiver** and **member**.

        The signal will be disconnected from the slot when the dialog is closed.
        """
        ...
    def options(self) -> PySide6.QtWidgets.QColorDialog.ColorDialogOptions:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#options-prop

        **options : ColorDialogOptions**

        This property holds the various options that affect the look and feel of
        the dialog

        By default, all options are disabled.

        Options should be set before showing the dialog. Setting them while the
        dialog is visible is not guaranteed to have an immediate effect on the
        dialog (depending on the option and on the platform).

        **Access functions:**

        QColorDialog::ColorDialogOptions **options** () const
        void
        **setOptions** (QColorDialog::ColorDialogOptions **options** )

        **See also** **setOption** () and **testOption** ().

        **Member Function Documentation**
        """
        ...
    def selectedColor(self) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#selectedColor

        **QColor QColorDialog::selectedColor() const**

        Returns the color that the user selected by clicking the **OK** or
        equivalent button.

        **Note:** This color is not always the same as the color held by the
        **currentColor**  property since the user can choose different colors
        before finally selecting the one to use.
        """
        ...
    def setCurrentColor(
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
        https://doc.qt.io/qt-6/qcolordialog.html#currentColor-prop

        **currentColor : QColor**

        This property holds the currently selected color in the dialog

        **Access functions:**

        QColor **currentColor** () const
        void **setCurrentColor** (const
        QColor & **color** )

        **Notifier signal:**

        void ****currentColorChanged** ** (const QColor & **color** )
        """
        ...
    @staticmethod
    def setCustomColor(
        index: int,
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
        https://doc.qt.io/qt-6/qcolordialog.html#setCustomColor

        **[static] void QColorDialog::setCustomColor(int index , QColor color
        )**

        Sets the custom color at **index** to the **QColor**  **color** value.

        **Note:** This function does not apply to the Native Color Dialog on the
        macOS platform. If you still require this function, use the
        **QColorDialog::DontUseNativeDialog**  option.

        **See also** **customColor** ().
        """
        ...
    def setOption(
        self, option: PySide6.QtWidgets.QColorDialog.ColorDialogOption, on: bool = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#setOption

        **void QColorDialog::setOption(QColorDialog::ColorDialogOption option ,
        bool on = true)**

        Sets the given **option** to be enabled if **on** is true; otherwise,
        clears the given **option**.

        **See also** **options**  and **testOption** ().
        """
        ...
    def setOptions(
        self, options: PySide6.QtWidgets.QColorDialog.ColorDialogOptions
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#options-prop

        **options : ColorDialogOptions**

        This property holds the various options that affect the look and feel of
        the dialog

        By default, all options are disabled.

        Options should be set before showing the dialog. Setting them while the
        dialog is visible is not guaranteed to have an immediate effect on the
        dialog (depending on the option and on the platform).

        **Access functions:**

        QColorDialog::ColorDialogOptions **options** () const
        void
        **setOptions** (QColorDialog::ColorDialogOptions **options** )

        **See also** **setOption** () and **testOption** ().

        **Member Function Documentation**
        """
        ...
    @staticmethod
    def setStandardColor(
        index: int,
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
        https://doc.qt.io/qt-6/qcolordialog.html#setStandardColor

        **[static] void QColorDialog::setStandardColor(int index , QColor color
        )**

        Sets the standard color at **index** to the **QColor**  **color** value.

        **Note:** This function does not apply to the Native Color Dialog on the
        macOS platform. If you still require this function, use the
        **QColorDialog::DontUseNativeDialog**  option.

        **See also** **standardColor** ().
        """
        ...
    def setVisible(self, visible: bool) -> None:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#setVisible

        **[override virtual] void QColorDialog::setVisible(bool visible )**

        Reimplements: **QDialog::setVisible** (bool visible).

        Changes the visibility of the dialog. If **visible** is true, the dialog
        is shown; otherwise, it is hidden.
        """
        ...
    @staticmethod
    def standardColor(index: int) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#standardColor

        **[static, since 5.0] QColor QColorDialog::standardColor(int index )**

        Returns the standard color at the given **index** as a **QColor**
        value.

        This function was introduced in Qt 5.0.

        **See also** **setStandardColor** ().
        """
        ...
    def testOption(
        self, option: PySide6.QtWidgets.QColorDialog.ColorDialogOption
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#testOption

        **bool QColorDialog::testOption(QColorDialog::ColorDialogOption option )
        const**

        Returns `true` if the given **option** is enabled; otherwise, returns
        false.

        **See also** **options**  and **setOption** ().
        """
        ...
    @property
    def colorSelected(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#colorSelected

        **[signal] void QColorDialog::colorSelected(const QColor & color )**

        This signal is emitted just after the user has clicked **OK** to select
        a color to use. The chosen color is specified by **color**.

        **See also** **color**  and **currentColorChanged** ().
        """
        ...
    @property
    def currentColorChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qcolordialog.html#currentColorChanged

        **[signal] void QColorDialog::currentColorChanged(const QColor & color
        )**

        This signal is emitted whenever the current color changes in the dialog.
        The current color is specified by **color**.

        **Note:** Notifier signal for property **currentColor** .

        **See also** **color**  and **colorSelected** ().
        """
        ...
