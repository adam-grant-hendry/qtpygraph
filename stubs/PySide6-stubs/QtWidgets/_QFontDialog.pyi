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

from collections.abc import Sequence
from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QFontDialog(PySide6.QtWidgets.QDialog):
    """
    https://doc.qt.io/qt-6/qfontdialog.html

    **Detailed Description**

    A font dialog is created through one of the static **getFont** () functions.

    Examples:

    bool ok;
        **QFont**  font = **QFontDialog** ::getFont(
    &ok, **QFont** ("Helvetica [Cronyx]", 10), this);
        if (ok) {
            //
    the user clicked OK and font is set to the font the user selected
        } else
    {
            // the user canceled the dialog; font is set to the initial
    // value, in this case Helvetica [Cronyx], 10
        }

    The dialog can also be used to set a widget's font directly:

    myWidget.setFont(**QFontDialog** ::getFont(0, myWidget.font()));

    If the user clicks OK the font they chose will be used for myWidget, and if
    they click Cancel the original font is used.

    ![A font dialog in the Fusion widget style.](images/fusion-fontdialog.png)

    **See also** **QFont** , **QFontInfo** , **QFontMetrics** , **QColorDialog**
    , **QFileDialog** , and **Standard Dialogs Example** .
    """

    NoButtons: QFontDialog.FontDialogOption = ...
    DontUseNativeDialog: QFontDialog.FontDialogOption = ...
    ScalableFonts: QFontDialog.FontDialogOption = ...
    NonScalableFonts: QFontDialog.FontDialogOption = ...
    MonospacedFonts: QFontDialog.FontDialogOption = ...
    ProportionalFonts: QFontDialog.FontDialogOption = ...

    class FontDialogOption(IntFlag):
        NoButtons: QFontDialog.FontDialogOption = ...
        DontUseNativeDialog: QFontDialog.FontDialogOption = ...
        ScalableFonts: QFontDialog.FontDialogOption = ...
        NonScalableFonts: QFontDialog.FontDialogOption = ...
        MonospacedFonts: QFontDialog.FontDialogOption = ...
        ProportionalFonts: QFontDialog.FontDialogOption = ...

    class FontDialogOptions: ...

    @overload
    def __init__(
        self,
        initial: PySide6.QtGui.QFont | str | Sequence[str],
        parent: PySide6.QtWidgets.QWidget | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#QFontDialog

        **QFontDialog::QFontDialog(QWidget * parent = nullptr)**

        Constructs a standard font dialog.

        Use **setCurrentFont** () to set the initial font attributes.

        The **parent** parameter is passed to the **QDialog**  constructor.

        **See also** **getFont** ().
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#QFontDialog-1

        **QFontDialog::QFontDialog(const QFont & initial , QWidget * parent =
        nullptr)**

        Constructs a standard font dialog with the given **parent** and
        specified **initial** font.
        """
        ...
    def changeEvent(self, event: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#changeEvent

        **[override virtual protected] void QFontDialog::changeEvent(QEvent * e
        )**

        Reimplements: **QWidget::changeEvent** (QEvent *event).
        """
        ...
    def currentFont(self) -> PySide6.QtGui.QFont:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#currentFont

        **QFont QFontDialog::currentFont() const**

        Returns the current font.

        **Note:** Getter function for property currentFont.

        **See also** **setCurrentFont** () and **selectedFont** ().
        """
        ...
    def done(self, result: int) -> None:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#done

        **[override virtual protected] void QFontDialog::done(int result )**

        Reimplements: **QDialog::done** (int r).

        Closes the dialog and sets its result code to **result**. If this dialog
        is shown with **exec** (), done() causes the local event loop to finish,
        and **exec** () to return **result**.

        **See also** **QDialog::done** ().
        """
        ...
    def eventFilter(
        self, object: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent
    ) -> bool: ...
    @overload
    @staticmethod
    def getFont(
        initial: PySide6.QtGui.QFont | str | Sequence[str],
        parent: PySide6.QtWidgets.QWidget | None = ...,
        title: str = ...,
        options: PySide6.QtWidgets.QFontDialog.FontDialogOptions = ...,
    ) -> tuple[bool, tuple]:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#getFont

        **[static] QFont QFontDialog::getFont(bool * ok , const QFont & initial
        , QWidget * parent = nullptr, const QString & title = QString(),
        QFontDialog::FontDialogOptions options = FontDialogOptions())**

        Executes a modal font dialog and returns a font.

        If the user clicks **OK** , the selected font is returned. If the user
        clicks **Cancel** , the **initial** font is returned.

        The dialog is constructed with the given **parent** and the options
        specified in **options**. **title** is shown as the window title of the
        dialog and **initial** is the initially selected font. If the **ok**
        parameter is not-null, the value it refers to is set to true if the user
        clicks **OK** , and set to false if the user clicks **Cancel**.

        Examples:

        bool ok;
            **QFont**  font = **QFontDialog** ::getFont(&ok, **QFont**
        ("Times", 12), this);
            if (ok) {
                // font is set to the font
        the user selected
            } else {
                // the user canceled the dialog;
        font is set to the initial
                // value, in this case Times, 12.
        }

        The dialog can also be used to set a widget's font directly:

        myWidget.setFont(**QFontDialog** ::getFont(0, myWidget.font()));

        In this example, if the user clicks OK the font they chose will be used,
        and if they click Cancel the original font is used.

        **Warning:** Do not delete **parent** during the execution of the
        dialog. If you want to do this, you should create the dialog yourself
        using one of the **QFontDialog**  constructors.
        """
        ...
    @overload
    @staticmethod
    def getFont(
        parent: PySide6.QtWidgets.QWidget | None = ...,
    ) -> tuple[bool, tuple]:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#getFont-1

        **[static] QFont QFontDialog::getFont(bool * ok , QWidget * parent =
        nullptr)**

        This is an overloaded function.

        Executes a modal font dialog and returns a font.

        If the user clicks **OK** , the selected font is returned. If the user
        clicks **Cancel** , the Qt default font is returned.

        The dialog is constructed with the given **parent**. If the **ok**
        parameter is not-null, the value it refers to is set to true if the user
        clicks **OK** , and false if the user clicks **Cancel**.

        Example:

        bool ok;
            **QFont**  font = **QFontDialog** ::getFont(&ok, this);
        if (ok) {
                // font is set to the font the user selected
            }
        else {
                // the user canceled the dialog; font is set to the
        default
                // application font, QApplication::font()
            }

        **Warning:** Do not delete **parent** during the execution of the
        dialog. If you want to do this, you should create the dialog yourself
        using one of the **QFontDialog**  constructors.
        """
        ...
    @overload
    def open(self) -> None:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#open

        **void QFontDialog::open(QObject * receiver , const char * member )**

        Opens the dialog and connects its **fontSelected** () signal to the slot
        specified by **receiver** and **member**.

        The signal will be disconnected from the slot when the dialog is closed.
        """
        ...
    @overload
    def open(self, receiver: PySide6.QtCore.QObject, member: bytes) -> None:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#open

        **void QFontDialog::open(QObject * receiver , const char * member )**

        Opens the dialog and connects its **fontSelected** () signal to the slot
        specified by **receiver** and **member**.

        The signal will be disconnected from the slot when the dialog is closed.
        """
        ...
    def options(self) -> PySide6.QtWidgets.QFontDialog.FontDialogOptions:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#options-prop

        **options : FontDialogOptions**

        This property holds the various options that affect the look and feel of
        the dialog

        By default, all options are disabled.

        Options should be set before showing the dialog. Setting them while the
        dialog is visible is not guaranteed to have an immediate effect on the
        dialog (depending on the option and on the platform).

        **Access functions:**

        QFontDialog::FontDialogOptions **options** () const
        void
        **setOptions** (QFontDialog::FontDialogOptions **options** )

        **See also** **setOption** () and **testOption** ().

        **Member Function Documentation**
        """
        ...
    def selectedFont(self) -> PySide6.QtGui.QFont:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#selectedFont

        **QFont QFontDialog::selectedFont() const**

        Returns the font that the user selected by clicking the **OK** or
        equivalent button.

        **Note:** This font is not always the same as the font held by the
        **currentFont**  property since the user can choose different fonts
        before finally selecting the one to use.
        """
        ...
    def setCurrentFont(self, font: PySide6.QtGui.QFont | str | Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#setCurrentFont

        **void QFontDialog::setCurrentFont(const QFont & font )**

        Sets the font highlighted in the **QFontDialog**  to the given **font**.

        **Note:** Setter function for property **currentFont** .

        **See also** **currentFont** () and **selectedFont** ().
        """
        ...
    def setOption(
        self, option: PySide6.QtWidgets.QFontDialog.FontDialogOption, on: bool = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#setOption

        **void QFontDialog::setOption(QFontDialog::FontDialogOption option ,
        bool on = true)**

        Sets the given **option** to be enabled if **on** is true; otherwise,
        clears the given **option**.

        **See also** **options**  and **testOption** ().
        """
        ...
    def setOptions(
        self, options: PySide6.QtWidgets.QFontDialog.FontDialogOptions
    ) -> None:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#options-prop

        **options : FontDialogOptions**

        This property holds the various options that affect the look and feel of
        the dialog

        By default, all options are disabled.

        Options should be set before showing the dialog. Setting them while the
        dialog is visible is not guaranteed to have an immediate effect on the
        dialog (depending on the option and on the platform).

        **Access functions:**

        QFontDialog::FontDialogOptions **options** () const
        void
        **setOptions** (QFontDialog::FontDialogOptions **options** )

        **See also** **setOption** () and **testOption** ().

        **Member Function Documentation**
        """
        ...
    def setVisible(self, visible: bool) -> None:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#setVisible

        **[override virtual] void QFontDialog::setVisible(bool visible )**

        Reimplements: **QDialog::setVisible** (bool visible).
        """
        ...
    def testOption(self, option: PySide6.QtWidgets.QFontDialog.FontDialogOption) -> bool:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#testOption

        **bool QFontDialog::testOption(QFontDialog::FontDialogOption option )
        const**

        Returns `true` if the given **option** is enabled; otherwise, returns
        false.

        **See also** **options**  and **setOption** ().
        """
        ...
    @property
    def currentFontChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#currentFontChanged

        **[signal] void QFontDialog::currentFontChanged(const QFont & font )**

        This signal is emitted when the current font is changed. The new font is
        specified in **font**.

        The signal is emitted while a user is selecting a font. Ultimately, the
        chosen font may differ from the font currently selected.

        **Note:** Notifier signal for property **currentFont** .

        **See also** **currentFont** , **fontSelected** (), and **selectedFont**
        ().
        """
        ...
    @property
    def fontSelected(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qfontdialog.html#fontSelected

        **[signal] void QFontDialog::fontSelected(const QFont & font )**

        This signal is emitted when a font has been selected. The selected font
        is specified in **font**.

        The signal is only emitted when a user has chosen the final font to be
        used. It is not emitted while the user is changing the current font in
        the font dialog.

        **See also** **selectedFont** (), **currentFontChanged** (), and
        **currentFont** .
        """
        ...