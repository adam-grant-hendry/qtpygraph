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
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QListWidget(PySide6.QtWidgets.QListView):
    """
    https://doc.qt.io/qt-6/qlistwidget.html

    **Detailed Description**

    ![](images/windows-listview.png)

    QListWidget is a convenience class that provides a list view similar to the
    one supplied by **QListView** , but with a classic item-based interface for
    adding and removing items. QListWidget uses an internal model to manage each
    **QListWidgetItem**  in the list.

    For a more flexible list view widget, use the **QListView**  class with a
    standard model.

    List widgets are constructed in the same way as other widgets:

    QListWidget *listWidget = new QListWidget(this);

    The **selectionMode** () of a list widget determines how many of the items
    in the list can be selected at the same time, and whether complex selections
    of items can be created. This can be set with the **setSelectionMode** ()
    function.

    There are two ways to add items to the list: they can be constructed with
    the list widget as their parent widget, or they can be constructed with no
    parent widget and added to the list later. If a list widget already exists
    when the items are constructed, the first method is easier to use:

    new **QListWidgetItem** (tr("Oak"), listWidget);
            new
    **QListWidgetItem** (tr("Fir"), listWidget);
            new **QListWidgetItem**
    (tr("Pine"), listWidget);

    If you need to insert a new item into the list at a particular position,
    then it should be constructed without a parent widget. The **insertItem** ()
    function should then be used to place it within the list. The list widget
    will take ownership of the item.

    **QListWidgetItem**  *newItem = new **QListWidgetItem** ;
    newItem->setText(itemText);
            listWidget->insertItem(row, newItem);

    For multiple items, **insertItems** () can be used instead. The number of
    items in the list is found with the **count** () function. To remove items
    from the list, use **takeItem** ().

    The current item in the list can be found with **currentItem** (), and
    changed with **setCurrentItem** (). The user can also change the current
    item by navigating with the keyboard or clicking on a different item. When
    the current item changes, the **currentItemChanged** () signal is emitted
    with the new current item and the item that was previously current.

    **See also** **QListWidgetItem** , **QListView** , **QTreeView** ,
    **Model/View Programming** , and **Tab Dialog Example** .
    """

    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#QListWidget

        **QListWidget::QListWidget(QWidget * parent = nullptr)**

        Constructs an empty QListWidget with the given **parent**.
        """
        ...
    @overload
    def addItem(self, item: PySide6.QtWidgets.QListWidgetItem) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#addItem

        **void QListWidget::addItem(const QString & label )**

        Inserts an item with the text **label** at the end of the list widget.
        """
        ...
    @overload
    def addItem(self, label: str) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#addItem-1

        **void QListWidget::addItem(QListWidgetItem * item )**

        Inserts the **item** at the end of the list widget.

        **Warning:** A **QListWidgetItem**  can only be added to a
        **QListWidget**  once. Adding the same **QListWidgetItem**  multiple
        times to a **QListWidget**  will result in undefined behavior.

        **See also** **insertItem** ().
        """
        ...
    def addItems(self, labels: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#addItems

        **void QListWidget::addItems(const QStringList & labels )**

        Inserts items with the text **labels** at the end of the list widget.

        **See also** **insertItems** ().
        """
        ...
    def clear(self) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#clear

        **[slot] void QListWidget::clear()**

        Removes all items and selections in the view.

        **Warning:** All items will be permanently deleted.
        """
        ...
    def closePersistentEditor(self, item: PySide6.QtWidgets.QListWidgetItem) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#closePersistentEditor

        **void QListWidget::closePersistentEditor(QListWidgetItem * item )**

        Closes the persistent editor for the given **item**.

        **See also** **openPersistentEditor** () and **isPersistentEditorOpen**
        ().
        """
        ...
    def count(self) -> int:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#count-prop

        **[read-only] count : const int**

        This property holds the number of items in the list including any hidden
        items.

        **Access functions:**

        int **count** () const
        """
        ...
    def currentItem(self) -> PySide6.QtWidgets.QListWidgetItem:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#currentItem

        **QListWidgetItem *QListWidget::currentItem() const**

        Returns the current item.

        **See also** **setCurrentItem** ().
        """
        ...
    def currentRow(self) -> int:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#currentRow-prop

        **currentRow : int**

        This property holds the row of the current item.

        Depending on the current selection mode, the row may also be selected.

        **Access functions:**

        int **currentRow** () const
        void **setCurrentRow** (int **row** )
        void ****setCurrentRow** ** (int **row** ,
        QItemSelectionModel::SelectionFlags **command** )

        **Notifier signal:**

        void ****currentRowChanged** ** (int **currentRow** )
        """
        ...
    def dropEvent(self, event: PySide6.QtGui.QDropEvent) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#dropEvent

        **[override virtual protected] void QListWidget::dropEvent(QDropEvent *
        event )**

        Reimplements: **QListView::dropEvent** (QDropEvent *event).
        """
        ...
    def dropMimeData(
        self,
        index: int,
        data: PySide6.QtCore.QMimeData,
        action: PySide6.QtCore.Qt.DropAction,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#dropMimeData

        **[virtual protected] bool QListWidget::dropMimeData(int index , const
        QMimeData * data , Qt::DropAction action )**

        Handles **data** supplied by an external drag and drop operation that
        ended with the given **action** in the given **index**. Returns `true`
        if **data** and **action** can be handled by the model; otherwise
        returns `false`.

        **See also** **supportedDropActions** ().
        """
        ...
    def editItem(self, item: PySide6.QtWidgets.QListWidgetItem) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#editItem

        **void QListWidget::editItem(QListWidgetItem * item )**

        Starts editing the **item** if it is editable.
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#event

        **[override virtual protected] bool QListWidget::event(QEvent * e )**

        Reimplements: **QListView::event** (QEvent *e).
        """
        ...
    def findItems(
        self, text: str, flags: PySide6.QtCore.Qt.MatchFlags
    ) -> list[PySide6.QtWidgets.QListWidgetItem]:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#findItems

        **QList<QListWidgetItem *> QListWidget::findItems(const QString & text ,
        Qt::MatchFlags flags ) const**

        Finds items with the text that matches the string **text** using the
        given **flags**.
        """
        ...
    def indexFromItem(
        self, item: PySide6.QtWidgets.QListWidgetItem
    ) -> PySide6.QtCore.QModelIndex:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#indexFromItem

        **QModelIndex QListWidget::indexFromItem(const QListWidgetItem * item )
        const**

        Returns the **QModelIndex**  associated with the given **item**.

        **Note:** In Qt versions prior to 5.10, this function took a non-`const`
        **item**.
        """
        ...
    @overload
    def insertItem(self, row: int, item: PySide6.QtWidgets.QListWidgetItem) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#insertItem

        **void QListWidget::insertItem(int row , QListWidgetItem * item )**

        Inserts the **item** at the position in the list given by **row**.

        **See also** **addItem** ().
        """
        ...
    @overload
    def insertItem(self, row: int, label: str) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#insertItem-1

        **void QListWidget::insertItem(int row , const QString & label )**

        Inserts an item with the text **label** in the list widget at the
        position given by **row**.

        **See also** **addItem** ().
        """
        ...
    def insertItems(self, row: int, labels: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#insertItems

        **void QListWidget::insertItems(int row , const QStringList & labels )**

        Inserts items from the list of **labels** into the list, starting at the
        given **row**.

        **See also** **insertItem** () and **addItem** ().
        """
        ...
    def isPersistentEditorOpen(self, item: PySide6.QtWidgets.QListWidgetItem) -> bool:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#isPersistentEditorOpen

        **[since 5.10] bool QListWidget::isPersistentEditorOpen(QListWidgetItem
        * item ) const**

        Returns whether a persistent editor is open for item **item**.

        This function was introduced in Qt 5.10.

        **See also** **openPersistentEditor** () and **closePersistentEditor**
        ().
        """
        ...
    def isSortingEnabled(self) -> bool: ...
    def item(self, row: int) -> PySide6.QtWidgets.QListWidgetItem:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#item

        **QListWidgetItem *QListWidget::item(int row ) const**

        Returns the item that occupies the given **row** in the list if one has
        been set; otherwise returns `nullptr`.

        **See also** **row** ().
        """
        ...
    @overload
    def itemAt(self, p: PySide6.QtCore.QPoint) -> PySide6.QtWidgets.QListWidgetItem:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#itemAt

        **QListWidgetItem *QListWidget::itemAt(const QPoint & p ) const**

        Returns a pointer to the item at the coordinates **p**. The coordinates
        are relative to the list widget's **viewport** ().
        """
        ...
    @overload
    def itemAt(self, x: int, y: int) -> PySide6.QtWidgets.QListWidgetItem:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#itemAt-1

        **QListWidgetItem *QListWidget::itemAt(int x , int y ) const**

        This is an overloaded function.

        Returns a pointer to the item at the coordinates ( **x** , **y** ). The
        coordinates are relative to the list widget's **viewport** ().
        """
        ...
    def itemFromIndex(
        self,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> PySide6.QtWidgets.QListWidgetItem:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#itemFromIndex

        **QListWidgetItem *QListWidget::itemFromIndex(const QModelIndex & index
        ) const**

        Returns a pointer to the **QListWidgetItem**  associated with the given
        **index**.
        """
        ...
    def itemWidget(
        self, item: PySide6.QtWidgets.QListWidgetItem
    ) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#itemWidget

        **QWidget *QListWidget::itemWidget(QListWidgetItem * item ) const**

        Returns the widget displayed in the given **item**.

        **See also** **setItemWidget** () and **removeItemWidget** ().
        """
        ...
    def items(
        self, data: PySide6.QtCore.QMimeData
    ) -> list[PySide6.QtWidgets.QListWidgetItem]:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#items

        **QList<QListWidgetItem *> QListWidget::items(const QMimeData * data )
        const**

        Returns a list of pointers to the items contained in the **data**
        object. If the object was not created by a **QListWidget**  in the same
        process, the list is empty.
        """
        ...
    def mimeData(
        self, items: Sequence[PySide6.QtWidgets.QListWidgetItem]
    ) -> PySide6.QtCore.QMimeData:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#mimeData

        **[virtual protected] QMimeData *QListWidget::mimeData(const
        QList<QListWidgetItem *> & items ) const**

        Returns an object that contains a serialized description of the
        specified **items**. The format used to describe the items is obtained
        from the **mimeTypes** () function.

        If the list of items is empty, `nullptr` is returned instead of a
        serialized empty list.
        """
        ...
    def mimeTypes(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#mimeTypes

        **[virtual protected] QStringList QListWidget::mimeTypes() const**

        Returns a list of MIME types that can be used to describe a list of
        listwidget items.

        **See also** **mimeData** ().
        """
        ...
    def openPersistentEditor(self, item: PySide6.QtWidgets.QListWidgetItem) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#openPersistentEditor

        **void QListWidget::openPersistentEditor(QListWidgetItem * item )**

        Opens an editor for the given **item**. The editor remains open after
        editing.

        **See also** **closePersistentEditor** () and **isPersistentEditorOpen**
        ().
        """
        ...
    def removeItemWidget(self, item: PySide6.QtWidgets.QListWidgetItem) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#removeItemWidget

        **void QListWidget::removeItemWidget(QListWidgetItem * item )**

        Removes the widget set on the given **item**.

        To remove an item (row) from the list entirely, either delete the item
        or use **takeItem** ().

        **See also** **itemWidget** () and **setItemWidget** ().
        """
        ...
    def row(self, item: PySide6.QtWidgets.QListWidgetItem) -> int:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#row

        **int QListWidget::row(const QListWidgetItem * item ) const**

        Returns the row containing the given **item**.

        **See also** **item** ().
        """
        ...
    def scrollToItem(
        self,
        item: PySide6.QtWidgets.QListWidgetItem,
        hint: PySide6.QtWidgets.QAbstractItemView.ScrollHint = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#scrollToItem

        **[slot] void QListWidget::scrollToItem(const QListWidgetItem * item ,
        QAbstractItemView::ScrollHint hint = EnsureVisible)**

        Scrolls the view if necessary to ensure that the **item** is visible.

        **hint** specifies where the **item** should be located after the
        operation.
        """
        ...
    def selectedItems(self) -> list[PySide6.QtWidgets.QListWidgetItem]:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#selectedItems

        **QList<QListWidgetItem *> QListWidget::selectedItems() const**

        Returns a list of all selected items in the list widget.
        """
        ...
    @overload
    def setCurrentItem(self, item: PySide6.QtWidgets.QListWidgetItem) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#setCurrentItem

        **void QListWidget::setCurrentItem(QListWidgetItem * item )**

        Sets the current item to **item**.

        Unless the selection mode is **NoSelection** , the item is also
        selected.

        **See also** **currentItem** ().
        """
        ...
    @overload
    def setCurrentItem(
        self,
        item: PySide6.QtWidgets.QListWidgetItem,
        command: PySide6.QtCore.QItemSelectionModel.SelectionFlags,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#setCurrentItem-1

        **void QListWidget::setCurrentItem(QListWidgetItem * item ,
        QItemSelectionModel::SelectionFlags command )**

        Set the current item to **item** , using the given **command**.
        """
        ...
    @overload
    def setCurrentRow(self, row: int) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#setCurrentRow-1

        **void QListWidget::setCurrentRow(int row ,
        QItemSelectionModel::SelectionFlags command )**

        Sets the current row to be the given **row** , using the given
        **command** ,

        **Note:** Setter function for property **currentRow** .
        """
        ...
    @overload
    def setCurrentRow(
        self, row: int, command: PySide6.QtCore.QItemSelectionModel.SelectionFlags
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#setCurrentRow-1

        **void QListWidget::setCurrentRow(int row ,
        QItemSelectionModel::SelectionFlags command )**

        Sets the current row to be the given **row** , using the given
        **command** ,

        **Note:** Setter function for property **currentRow** .
        """
        ...
    def setItemWidget(
        self, item: PySide6.QtWidgets.QListWidgetItem, widget: PySide6.QtWidgets.QWidget
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#setItemWidget

        **void QListWidget::setItemWidget(QListWidgetItem * item , QWidget *
        widget )**

        Sets the **widget** to be displayed in the given **item**.

        This function should only be used to display static content in the place
        of a list widget item. If you want to display custom dynamic content or
        implement a custom editor widget, use **QListView**  and subclass
        **QStyledItemDelegate**  instead.

        **See also** **itemWidget** (), **removeItemWidget** (), and **Delegate
        Classes** .
        """
        ...
    def setModel(self, model: PySide6.QtCore.QAbstractItemModel) -> None: ...
    def setSelectionModel(
        self, selectionModel: PySide6.QtCore.QItemSelectionModel
    ) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#setSelectionModel

        **[override virtual] void
        QListWidget::setSelectionModel(QItemSelectionModel * selectionModel )**

        Reimplements: **QAbstractItemView::setSelectionModel**
        (QItemSelectionModel *selectionModel).
        """
        ...
    def setSortingEnabled(self, enable: bool) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#sortingEnabled-prop

        **sortingEnabled : bool**

        This property holds whether sorting is enabled

        If this property is `true`, sorting is enabled for the list; if the
        property is false, sorting is not enabled.

        The default value is false.

        **Access functions:**

        bool **isSortingEnabled** () const
        void **setSortingEnabled** (bool
        **enable** )

        **Member Function Documentation**
        """
        ...
    def sortItems(self, order: PySide6.QtCore.Qt.SortOrder = ...) -> None:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#sortItems

        **void QListWidget::sortItems(Qt::SortOrder order =
        Qt::AscendingOrder)**

        Sorts all the items in the list widget according to the specified
        **order**.
        """
        ...
    def supportedDropActions(self) -> PySide6.QtCore.Qt.DropActions:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#supportedDropActions

        **[virtual protected] Qt::DropActions
        QListWidget::supportedDropActions() const**

        Returns the drop actions supported by this view.

        **See also** **Qt::DropActions** .
        """
        ...
    def takeItem(self, row: int) -> PySide6.QtWidgets.QListWidgetItem:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#takeItem

        **QListWidgetItem *QListWidget::takeItem(int row )**

        Removes and returns the item from the given **row** in the list widget;
        otherwise returns `nullptr`.

        Items removed from a list widget will not be managed by Qt, and will
        need to be deleted manually.

        **See also** **insertItem** () and **addItem** ().
        """
        ...
    def visualItemRect(
        self, item: PySide6.QtWidgets.QListWidgetItem
    ) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#visualItemRect

        **QRect QListWidget::visualItemRect(const QListWidgetItem * item )
        const**

        Returns the rectangle on the viewport occupied by the item at **item**.
        """
        ...
    @property
    def currentItemChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#currentItemChanged

        **[signal] void QListWidget::currentItemChanged(QListWidgetItem *
        current , QListWidgetItem * previous )**

        This signal is emitted whenever the current item changes.

        **previous** is the item that previously had the focus; **current** is
        the new current item.
        """
        ...
    @property
    def currentRowChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#currentRowChanged

        **[signal] void QListWidget::currentRowChanged(int currentRow )**

        This signal is emitted whenever the current item changes.

        **currentRow** is the row of the current item. If there is no current
        item, the **currentRow** is -1.

        **Note:** Notifier signal for property **currentRow** .
        """
        ...
    @property
    def currentTextChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#currentTextChanged

        **[signal] void QListWidget::currentTextChanged(const QString &
        currentText )**

        This signal is emitted whenever the current item changes.

        **currentText** is the text data in the current item. If there is no
        current item, the **currentText** is invalid.
        """
        ...
    @property
    def itemActivated(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#itemActivated

        **[signal] void QListWidget::itemActivated(QListWidgetItem * item )**

        This signal is emitted when the **item** is activated. The **item** is
        activated when the user clicks or double clicks on it, depending on the
        system configuration. It is also activated when the user presses the
        activation key (on Windows and X11 this is the **Return** key, on Mac OS
        X it is **Command+O** ).
        """
        ...
    @property
    def itemChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#itemChanged

        **[signal] void QListWidget::itemChanged(QListWidgetItem * item )**

        This signal is emitted whenever the data of **item** has changed.
        """
        ...
    @property
    def itemClicked(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#itemClicked

        **[signal] void QListWidget::itemClicked(QListWidgetItem * item )**

        This signal is emitted with the specified **item** when a mouse button
        is clicked on an item in the widget.

        **See also** **itemPressed** () and **itemDoubleClicked** ().
        """
        ...
    @property
    def itemDoubleClicked(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#itemDoubleClicked

        **[signal] void QListWidget::itemDoubleClicked(QListWidgetItem * item
        )**

        This signal is emitted with the specified **item** when a mouse button
        is double clicked on an item in the widget.

        **See also** **itemClicked** () and **itemPressed** ().
        """
        ...
    @property
    def itemEntered(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#itemEntered

        **[signal] void QListWidget::itemEntered(QListWidgetItem * item )**

        This signal is emitted when the mouse cursor enters an item. The
        **item** is the item entered. This signal is only emitted when
        mouseTracking is turned on, or when a mouse button is pressed while
        moving into an item.

        **See also** **QWidget::setMouseTracking** ().
        """
        ...
    @property
    def itemPressed(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#itemPressed

        **[signal] void QListWidget::itemPressed(QListWidgetItem * item )**

        This signal is emitted with the specified **item** when a mouse button
        is pressed on an item in the widget.

        **See also** **itemClicked** () and **itemDoubleClicked** ().
        """
        ...
    @property
    def itemSelectionChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qlistwidget.html#itemSelectionChanged

        **[signal] void QListWidget::itemSelectionChanged()**

        This signal is emitted whenever the selection changes.

        **See also** **selectedItems** (), **QListWidgetItem::isSelected** (),
        and **currentItemChanged** ().
        """
        ...