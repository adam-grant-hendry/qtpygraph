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

from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QToolBox(PySide6.QtWidgets.QFrame):
    """
    https://doc.qt.io/qt-6/qtoolbox.html

    **Detailed Description**

    A toolbox is a widget that displays a column of tabs one above the other,
    with the current item displayed below the current tab. Every tab has an
    index position within the column of tabs. A tab's item is a **QWidget** .

    Each item has an **itemText** (), an optional **itemIcon** (), an optional
    **itemToolTip** (), and a **widget** (). The item's attributes can be
    changed with **setItemText** (), **setItemIcon** (), and **setItemToolTip**
    (). Each item can be enabled or disabled individually with
    **setItemEnabled** ().

    Items are added using **addItem** (), or inserted at particular positions
    using **insertItem** (). The total number of items is given by **count** ().
    Items can be deleted with delete, or removed from the toolbox with
    **removeItem** (). Combining **removeItem** () and **insertItem** () allows
    you to move items to different positions.

    The index of the current item widget is returned by **currentIndex** (), and
    set with **setCurrentIndex** (). The index of a particular item can be found
    using **indexOf** (), and the item at a given index is returned by item().

    The **currentChanged** () signal is emitted when the current item is
    changed.

    **See also** **QTabWidget** .
    """

    def __init__(
        self,
        parent: PySide6.QtWidgets.QWidget | None = ...,
        f: PySide6.QtCore.Qt.WindowFlags = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#QToolBox

        **QToolBox::QToolBox(QWidget * parent = nullptr, Qt::WindowFlags f =
        Qt::WindowFlags())**

        Constructs a new toolbox with the given **parent** and the flags, **f**.
        """
        ...
    @overload
    def addItem(
        self,
        widget: PySide6.QtWidgets.QWidget,
        icon: PySide6.QtGui.QIcon | PySide6.QtGui.QPixmap,
        text: str,
    ) -> int:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#addItem

        **int QToolBox::addItem(QWidget * widget , const QIcon & iconSet , const
        QString & text )**

        Adds the **widget** in a new tab at bottom of the toolbox. The new tab's
        text is set to **text** , and the **iconSet** is displayed to the left
        of the **text**. Returns the new tab's index.
        """
        ...
    @overload
    def addItem(self, widget: PySide6.QtWidgets.QWidget, text: str) -> int:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#addItem-1

        **int QToolBox::addItem(QWidget * w , const QString & text )**

        This is an overloaded function.

        Adds the widget **w** in a new tab at bottom of the toolbox. The new
        tab's text is set to **text**. Returns the new tab's index.
        """
        ...
    def changeEvent(self, arg__1: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#changeEvent

        **[override virtual protected] void QToolBox::changeEvent(QEvent * ev
        )**

        Reimplements: **QFrame::changeEvent** (QEvent *ev).
        """
        ...
    def count(self) -> int:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#count-prop

        **[read-only] count : const int**

        This property holds the number of items contained in the toolbox.

        By default, this property has a value of 0.

        **Access functions:**

        int **count** () const
        """
        ...
    def currentIndex(self) -> int:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#currentIndex-prop

        **currentIndex : int**

        This property holds the index of the current item

        By default, for an empty toolbox, this property has a value of -1.

        **Access functions:**

        int **currentIndex** () const
        void **setCurrentIndex** (int **index**
        )

        **Notifier signal:**

        void ****currentChanged** ** (int **index** )

        **See also** **indexOf** () and **widget** ().

        **Member Function Documentation**
        """
        ...
    def currentWidget(self) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#currentWidget

        **QWidget *QToolBox::currentWidget() const**

        Returns a pointer to the current widget, or `nullptr` if there is no
        such item.

        **See also** **currentIndex** () and **setCurrentWidget** ().
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#event

        **[override virtual protected] bool QToolBox::event(QEvent * e )**

        Reimplements: **QFrame::event** (QEvent *e).
        """
        ...
    def indexOf(self, widget: PySide6.QtWidgets.QWidget) -> int:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#indexOf

        **int QToolBox::indexOf(const QWidget * widget ) const**

        Returns the index of **widget** , or -1 if the item does not exist.
        """
        ...
    @overload
    def insertItem(
        self,
        index: int,
        widget: PySide6.QtWidgets.QWidget,
        icon: PySide6.QtGui.QIcon | PySide6.QtGui.QPixmap,
        text: str,
    ) -> int:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#insertItem

        **int QToolBox::insertItem(int index , QWidget * widget , const QIcon &
        icon , const QString & text )**

        Inserts the **widget** at position **index** , or at the bottom of the
        toolbox if **index** is out of range. The new item's text is set to
        **text** , and the **icon** is displayed to the left of the **text**.
        Returns the new item's index.
        """
        ...
    @overload
    def insertItem(self, index: int, widget: PySide6.QtWidgets.QWidget, text: str) -> int:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#insertItem-1

        **int QToolBox::insertItem(int index , QWidget * widget , const QString
        & text )**

        This is an overloaded function.

        Inserts the **widget** at position **index** , or at the bottom of the
        toolbox if **index** is out of range. The new item's text is set to
        **text**. Returns the new item's index.
        """
        ...
    def isItemEnabled(self, index: int) -> bool:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#isItemEnabled

        **bool QToolBox::isItemEnabled(int index ) const**

        Returns `true` if the item at position **index** is enabled; otherwise
        returns `false`.
        """
        ...
    def itemIcon(self, index: int) -> PySide6.QtGui.QIcon:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#itemIcon

        **QIcon QToolBox::itemIcon(int index ) const**

        Returns the icon of the item at position **index** , or a null icon if
        **index** is out of range.

        **See also** **setItemIcon** ().
        """
        ...
    def itemInserted(self, index: int) -> None:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#itemInserted

        **[virtual protected] void QToolBox::itemInserted(int index )**

        This virtual handler is called after a new item was added or inserted at
        position **index**.

        **See also** **itemRemoved** ().
        """
        ...
    def itemRemoved(self, index: int) -> None:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#itemRemoved

        **[virtual protected] void QToolBox::itemRemoved(int index )**

        This virtual handler is called after an item was removed from position
        **index**.

        **See also** **itemInserted** ().
        """
        ...
    def itemText(self, index: int) -> str:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#itemText

        **QString QToolBox::itemText(int index ) const**

        Returns the text of the item at position **index** , or an empty string
        if **index** is out of range.

        **See also** **setItemText** ().
        """
        ...
    def itemToolTip(self, index: int) -> str:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#itemToolTip

        **QString QToolBox::itemToolTip(int index ) const**

        Returns the tooltip of the item at position **index** , or an empty
        string if **index** is out of range.

        **See also** **setItemToolTip** ().
        """
        ...
    def removeItem(self, index: int) -> None:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#removeItem

        **void QToolBox::removeItem(int index )**

        Removes the item at position **index** from the toolbox. Note that the
        widget is **not** deleted.
        """
        ...
    def setCurrentIndex(self, index: int) -> None:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#currentIndex-prop

        **currentIndex : int**

        This property holds the index of the current item

        By default, for an empty toolbox, this property has a value of -1.

        **Access functions:**

        int **currentIndex** () const
        void **setCurrentIndex** (int **index**
        )

        **Notifier signal:**

        void ****currentChanged** ** (int **index** )

        **See also** **indexOf** () and **widget** ().

        **Member Function Documentation**
        """
        ...
    def setCurrentWidget(self, widget: PySide6.QtWidgets.QWidget) -> None:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#setCurrentWidget

        **[slot] void QToolBox::setCurrentWidget(QWidget * widget )**

        Makes **widget** the current widget. The **widget** must be an item in
        this tool box.

        **See also** **addItem** (), **setCurrentIndex** (), and
        **currentWidget** ().
        """
        ...
    def setItemEnabled(self, index: int, enabled: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#setItemEnabled

        **void QToolBox::setItemEnabled(int index , bool enabled )**

        If **enabled** is true then the item at position **index** is enabled;
        otherwise the item at position **index** is disabled.

        **See also** **isItemEnabled** ().
        """
        ...
    def setItemIcon(
        self, index: int, icon: PySide6.QtGui.QIcon | PySide6.QtGui.QPixmap
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#setItemIcon

        **void QToolBox::setItemIcon(int index , const QIcon & icon )**

        Sets the icon of the item at position **index** to **icon**.

        **See also** **itemIcon** ().
        """
        ...
    def setItemText(self, index: int, text: str) -> None:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#setItemText

        **void QToolBox::setItemText(int index , const QString & text )**

        Sets the text of the item at position **index** to **text**.

        If the provided text contains an ampersand character ('&'), a mnemonic
        is automatically created for it. The character that follows the '&' will
        be used as the shortcut key. Any previous mnemonic will be overwritten,
        or cleared if no mnemonic is defined by the text. See the **QShortcut**
        documentation for details (to display an actual ampersand, use '&&').

        **See also** **itemText** ().
        """
        ...
    def setItemToolTip(self, index: int, toolTip: str) -> None:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#setItemToolTip

        **void QToolBox::setItemToolTip(int index , const QString & toolTip )**

        Sets the tooltip of the item at position **index** to **toolTip**.

        **See also** **itemToolTip** ().
        """
        ...
    def showEvent(self, e: PySide6.QtGui.QShowEvent) -> None:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#showEvent

        **[override virtual protected] void QToolBox::showEvent(QShowEvent * e
        )**

        Reimplements: **QWidget::showEvent** (QShowEvent *event).
        """
        ...
    def widget(self, index: int) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#widget

        **QWidget *QToolBox::widget(int index ) const**

        Returns the widget at position **index** , or `nullptr` if there is no
        such item.
        """
        ...
    @property
    def currentChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtoolbox.html#currentChanged

        **[signal] void QToolBox::currentChanged(int index )**

        This signal is emitted when the current item is changed. The new current
        item's index is passed in **index** , or -1 if there is no current item.

        **Note:** Notifier signal for property **currentIndex** .
        """
        ...
