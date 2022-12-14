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
PySide6.QtPrintSupport, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtPrintSupport
import PySide6.QtWidgets

class QPageSetupDialog(PySide6.QtWidgets.QDialog):
    """
    https://doc.qt.io/qt-6/qpagesetupdialog.html

    **Detailed Description**

    On Windows and macOS the page setup dialog is implemented using the native
    page setup dialogs.

    Note that on Windows and macOS custom paper sizes won't be reflected in the
    native page setup dialogs. Additionally, custom page margins set on a
    **QPrinter**  won't show in the native macOS page setup dialog.

    **See also** **QPrinter**  and **QPrintDialog** .
    """

    @overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qpagesetupdialog.html#QPageSetupDialog

        **QPageSetupDialog::QPageSetupDialog(QPrinter * printer , QWidget *
        parent = nullptr)**

        Constructs a page setup dialog that configures **printer** with
        **parent** as the parent widget.
        """
        ...
    @overload
    def __init__(
        self,
        printer: PySide6.QtPrintSupport.QPrinter,
        parent: PySide6.QtWidgets.QWidget | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpagesetupdialog.html#QPageSetupDialog-1

        **QPageSetupDialog::QPageSetupDialog(QWidget * parent = nullptr)**

        Constructs a page setup dialog that configures a default-constructed
        **QPrinter**  with **parent** as the parent widget.

        **See also** **printer** ().
        """
        ...
    def done(self, result: int) -> None:
        """
        https://doc.qt.io/qt-6/qpagesetupdialog.html#done

        **[override virtual] void QPageSetupDialog::done(int result )**

        Reimplements: **QDialog::done** (int r).
        """
        ...
    def exec(self) -> int:
        """
        https://doc.qt.io/qt-6/qpagesetupdialog.html#exec

        **[override virtual] int QPageSetupDialog::exec()**

        Reimplements: **QDialog::exec** ().

        This virtual function is called to pop up the dialog. It must be
        reimplemented in subclasses.
        """
        ...
    def exec_(self) -> int:
        """
        https://doc.qt.io/qt-6/qpagesetupdialog.html#exec

        **[override virtual] int QPageSetupDialog::exec()**

        Reimplements: **QDialog::exec** ().

        This virtual function is called to pop up the dialog. It must be
        reimplemented in subclasses.
        """
        ...
    @overload
    def open(self) -> None:
        """
        https://doc.qt.io/qt-6/qpagesetupdialog.html#open

        **void QPageSetupDialog::open(QObject * receiver , const char * member
        )**

        This is an overloaded function.

        Opens the dialog and connects its **accepted** () signal to the slot
        specified by **receiver** and **member**.

        The signal will be disconnected from the slot when the dialog is closed.
        """
        ...
    @overload
    def open(self, receiver: PySide6.QtCore.QObject, member: bytes) -> None:
        """
        https://doc.qt.io/qt-6/qpagesetupdialog.html#open

        **void QPageSetupDialog::open(QObject * receiver , const char * member
        )**

        This is an overloaded function.

        Opens the dialog and connects its **accepted** () signal to the slot
        specified by **receiver** and **member**.

        The signal will be disconnected from the slot when the dialog is closed.
        """
        ...
    def printer(self) -> PySide6.QtPrintSupport.QPrinter:
        """
        https://doc.qt.io/qt-6/qpagesetupdialog.html#printer

        **QPrinter *QPageSetupDialog::printer()**

        Returns the printer that was passed to the **QPageSetupDialog**
        constructor.
        """
        ...
    def setVisible(self, visible: bool) -> None:
        """
        https://doc.qt.io/qt-6/qpagesetupdialog.html#setVisible

        **[override virtual] void QPageSetupDialog::setVisible(bool visible )**

        Reimplements: **QDialog::setVisible** (bool visible).
        """
        ...
