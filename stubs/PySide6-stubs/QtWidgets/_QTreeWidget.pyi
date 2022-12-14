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

class QTreeWidget(PySide6.QtWidgets.QTreeView):
    """
    https://doc.qt.io/qt-6/qtreewidget.html

    **Detailed Description**

    ![](images/windows-treeview.png)

    The QTreeWidget class is a convenience class that provides a standard tree
    widget with a classic item-based interface similar to that used by the
    **QListView**  class in Qt 3. This class is based on Qt's Model/View
    architecture and uses a default model to hold items, each of which is a
    **QTreeWidgetItem** .

    Developers who do not need the flexibility of the Model/View framework can
    use this class to create simple hierarchical lists very easily. A more
    flexible approach involves combining a **QTreeView**  with a standard item
    model. This allows the storage of data to be separated from its
    representation.

    In its simplest form, a tree widget can be constructed in the following way:

    **QTreeWidget**  *treeWidget = new **QTreeWidget** ();
    treeWidget->setColumnCount(1);
        **QList** <**QTreeWidgetItem**  *> items;
    for (int i = 0; i < 10; ++i)
            items.append(new **QTreeWidgetItem**
    (static_cast<**QTreeWidget**  *>(nullptr), **QStringList** (**QString**
    ("item: %1").arg(i))));
        treeWidget->insertTopLevelItems(0, items);

    Before items can be added to the tree widget, the number of columns must be
    set with **setColumnCount** (). This allows each item to have one or more
    labels or other decorations. The number of columns in use can be found with
    the **columnCount** () function.

    The tree can have a header that contains a section for each column in the
    widget. It is easiest to set up the labels for each section by supplying a
    list of strings with **setHeaderLabels** (), but a custom header can be
    constructed with a **QTreeWidgetItem**  and inserted into the tree with the
    **setHeaderItem** () function.

    The items in the tree can be sorted by column according to a predefined sort
    order. If sorting is enabled, the user can sort the items by clicking on a
    column header. Sorting can be enabled or disabled by calling
    **setSortingEnabled** (). The **isSortingEnabled** () function indicates
    whether sorting is enabled.

    **See also** **QTreeWidgetItem** , **QTreeWidgetItemIterator** ,
    **QTreeView** , **Model/View Programming** , and **Settings Editor Example**
    .
    """

    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#QTreeWidget

        **QTreeWidget::QTreeWidget(QWidget * parent = nullptr)**

        Constructs a tree widget with the given **parent**.
        """
        ...
    def addTopLevelItem(self, item: PySide6.QtWidgets.QTreeWidgetItem) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#addTopLevelItem

        **void QTreeWidget::addTopLevelItem(QTreeWidgetItem * item )**

        Appends the **item** as a top-level item in the widget.

        **See also** **insertTopLevelItem** ().
        """
        ...
    def addTopLevelItems(
        self, items: Sequence[PySide6.QtWidgets.QTreeWidgetItem]
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#addTopLevelItems

        **void QTreeWidget::addTopLevelItems(const QList<QTreeWidgetItem *> &
        items )**

        Appends the list of **items** as a top-level items in the widget.

        **See also** **insertTopLevelItems** ().
        """
        ...
    def clear(self) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#clear

        **[slot] void QTreeWidget::clear()**

        Clears the tree widget by removing all of its items and selections.

        **Note:** Since each item is removed from the tree widget before being
        deleted, the return value of **QTreeWidgetItem::treeWidget** () will be
        invalid when called from an item's destructor.

        **See also** **takeTopLevelItem** (), **topLevelItemCount** (), and
        **columnCount** ().
        """
        ...
    def closePersistentEditor(
        self, item: PySide6.QtWidgets.QTreeWidgetItem, column: int = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#closePersistentEditor

        **void QTreeWidget::closePersistentEditor(QTreeWidgetItem * item , int
        column = 0)**

        Closes the persistent editor for the **item** in the given **column**.

        This function has no effect if no persistent editor is open for this
        combination of item and column.

        **See also** **openPersistentEditor** () and **isPersistentEditorOpen**
        ().
        """
        ...
    def collapseItem(self, item: PySide6.QtWidgets.QTreeWidgetItem) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#collapseItem

        **[slot] void QTreeWidget::collapseItem(const QTreeWidgetItem * item )**

        Closes the **item**. This causes the tree containing the item's children
        to be collapsed.

        **See also** **expandItem** (), **currentItem** (), **itemAt** (), and
        **topLevelItem** ().
        """
        ...
    def columnCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#columnCount-prop

        **columnCount : int**

        This property holds the number of columns displayed in the tree widget

        By default, this property has a value of 1.

        **Access functions:**

        int **columnCount** () const
        void **setColumnCount** (int **columns**
        )
        """
        ...
    def currentColumn(self) -> int:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#currentColumn

        **int QTreeWidget::currentColumn() const**

        Returns the current column in the tree widget.

        **See also** **setCurrentItem** () and **columnCount** ().
        """
        ...
    def currentItem(self) -> PySide6.QtWidgets.QTreeWidgetItem:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#currentItem

        **QTreeWidgetItem *QTreeWidget::currentItem() const**

        Returns the current item in the tree widget.

        **See also** **setCurrentItem** () and **currentItemChanged** ().
        """
        ...
    def dropEvent(self, event: PySide6.QtGui.QDropEvent) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#dropEvent

        **[override virtual protected] void QTreeWidget::dropEvent(QDropEvent *
        event )**

        Reimplements: **QAbstractItemView::dropEvent** (QDropEvent *event).
        """
        ...
    def dropMimeData(
        self,
        parent: PySide6.QtWidgets.QTreeWidgetItem,
        index: int,
        data: PySide6.QtCore.QMimeData,
        action: PySide6.QtCore.Qt.DropAction,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#dropMimeData

        **[virtual protected] bool QTreeWidget::dropMimeData(QTreeWidgetItem *
        parent , int index , const QMimeData * data , Qt::DropAction action )**

        Handles the **data** supplied by a drag and drop operation that ended
        with the given **action** in the **index** in the given **parent** item.

        The default implementation returns `true` if the drop was successfully
        handled by decoding the mime data and inserting it into the model;
        otherwise it returns `false`.

        **See also** **supportedDropActions** ().
        """
        ...
    def editItem(
        self, item: PySide6.QtWidgets.QTreeWidgetItem, column: int = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#editItem

        **void QTreeWidget::editItem(QTreeWidgetItem * item , int column = 0)**

        Starts editing the **item** in the given **column** if it is editable.
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#event

        **[override virtual protected] bool QTreeWidget::event(QEvent * e )**

        Reimplements: **QAbstractItemView::event** (QEvent *event).
        """
        ...
    def expandItem(self, item: PySide6.QtWidgets.QTreeWidgetItem) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#expandItem

        **[slot] void QTreeWidget::expandItem(const QTreeWidgetItem * item )**

        Expands the **item**. This causes the tree containing the item's
        children to be expanded.

        **See also** **collapseItem** (), **currentItem** (), **itemAt** (),
        **topLevelItem** (), and **itemExpanded** ().
        """
        ...
    def findItems(
        self, text: str, flags: PySide6.QtCore.Qt.MatchFlags, column: int = ...
    ) -> list[PySide6.QtWidgets.QTreeWidgetItem]:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#findItems

        **QList<QTreeWidgetItem *> QTreeWidget::findItems(const QString & text ,
        Qt::MatchFlags flags , int column = 0) const**

        Returns a list of items that match the given **text** , using the given
        **flags** , in the given **column**.
        """
        ...
    def headerItem(self) -> PySide6.QtWidgets.QTreeWidgetItem:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#headerItem

        **QTreeWidgetItem *QTreeWidget::headerItem() const**

        Returns the item used for the tree widget's header.

        **See also** **setHeaderItem** ().
        """
        ...
    def indexFromItem(
        self, item: PySide6.QtWidgets.QTreeWidgetItem, column: int = ...
    ) -> PySide6.QtCore.QModelIndex:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#indexFromItem

        **QModelIndex QTreeWidget::indexFromItem(const QTreeWidgetItem * item ,
        int column = 0) const**

        Returns the **QModelIndex**  associated with the given **item** in the
        given **column**.

        **Note:** In Qt versions prior to 5.7, this function took a non-`const`
        **item**.

        **See also** **itemFromIndex** () and **topLevelItem** ().
        """
        ...
    def indexOfTopLevelItem(self, item: PySide6.QtWidgets.QTreeWidgetItem) -> int:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#indexOfTopLevelItem

        **int QTreeWidget::indexOfTopLevelItem(QTreeWidgetItem * item ) const**

        Returns the index of the given top-level **item** , or -1 if the item
        cannot be found.

        **See also** **sortItems** () and **topLevelItemCount** ().
        """
        ...
    def insertTopLevelItem(
        self, index: int, item: PySide6.QtWidgets.QTreeWidgetItem
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#insertTopLevelItem

        **void QTreeWidget::insertTopLevelItem(int index , QTreeWidgetItem *
        item )**

        Inserts the **item** at **index** in the top level in the view.

        If the item has already been inserted somewhere else it won't be
        inserted.

        **See also** **addTopLevelItem** () and **columnCount** ().
        """
        ...
    def insertTopLevelItems(
        self, index: int, items: Sequence[PySide6.QtWidgets.QTreeWidgetItem]
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#insertTopLevelItems

        **void QTreeWidget::insertTopLevelItems(int index , const
        QList<QTreeWidgetItem *> & items )**

        Inserts the list of **items** at **index** in the top level in the view.

        Items that have already been inserted somewhere else won't be inserted.

        **See also** **addTopLevelItems** ().
        """
        ...
    def invisibleRootItem(self) -> PySide6.QtWidgets.QTreeWidgetItem:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#invisibleRootItem

        **QTreeWidgetItem *QTreeWidget::invisibleRootItem() const**

        Returns the tree widget's invisible root item.

        The invisible root item provides access to the tree widget's top-level
        items through the **QTreeWidgetItem**  API, making it possible to write
        functions that can treat top-level items and their children in a uniform
        way; for example, recursive functions.
        """
        ...
    def isPersistentEditorOpen(
        self, item: PySide6.QtWidgets.QTreeWidgetItem, column: int = ...
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#isPersistentEditorOpen

        **[since 5.10] bool QTreeWidget::isPersistentEditorOpen(QTreeWidgetItem
        * item , int column = 0) const**

        Returns whether a persistent editor is open for item **item** in column
        **column**.

        This function was introduced in Qt 5.10.

        **See also** **openPersistentEditor** () and **closePersistentEditor**
        ().
        """
        ...
    def itemAbove(
        self, item: PySide6.QtWidgets.QTreeWidgetItem
    ) -> PySide6.QtWidgets.QTreeWidgetItem:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemAbove

        **QTreeWidgetItem *QTreeWidget::itemAbove(const QTreeWidgetItem * item )
        const**

        Returns the item above the given **item**.
        """
        ...
    @overload
    def itemAt(self, p: PySide6.QtCore.QPoint) -> PySide6.QtWidgets.QTreeWidgetItem:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemAt

        **QTreeWidgetItem *QTreeWidget::itemAt(const QPoint & p ) const**

        Returns a pointer to the item at the coordinates **p**. The coordinates
        are relative to the tree widget's **viewport** ().

        **See also** **visualItemRect** ().
        """
        ...
    @overload
    def itemAt(self, x: int, y: int) -> PySide6.QtWidgets.QTreeWidgetItem:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemAt-1

        **QTreeWidgetItem *QTreeWidget::itemAt(int x , int y ) const**

        This is an overloaded function.

        Returns a pointer to the item at the coordinates ( **x** , **y** ). The
        coordinates are relative to the tree widget's **viewport** ().
        """
        ...
    def itemBelow(
        self, item: PySide6.QtWidgets.QTreeWidgetItem
    ) -> PySide6.QtWidgets.QTreeWidgetItem:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemBelow

        **QTreeWidgetItem *QTreeWidget::itemBelow(const QTreeWidgetItem * item )
        const**

        Returns the item visually below the given **item**.
        """
        ...
    def itemFromIndex(
        self,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> PySide6.QtWidgets.QTreeWidgetItem:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemFromIndex

        **QTreeWidgetItem *QTreeWidget::itemFromIndex(const QModelIndex & index
        ) const**

        Returns a pointer to the **QTreeWidgetItem**  associated with the given
        **index**.

        **See also** **indexFromItem** ().
        """
        ...
    def itemWidget(
        self, item: PySide6.QtWidgets.QTreeWidgetItem, column: int
    ) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemWidget

        **QWidget *QTreeWidget::itemWidget(QTreeWidgetItem * item , int column )
        const**

        Returns the widget displayed in the cell specified by **item** and the
        given **column**.

        **See also** **setItemWidget** ().
        """
        ...
    def mimeData(
        self, items: Sequence[PySide6.QtWidgets.QTreeWidgetItem]
    ) -> PySide6.QtCore.QMimeData:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#mimeData

        **[virtual protected] QMimeData *QTreeWidget::mimeData(const
        QList<QTreeWidgetItem *> & items ) const**

        Returns an object that contains a serialized description of the
        specified **items**. The format used to describe the items is obtained
        from the **mimeTypes** () function.

        If the list of items is empty, `nullptr` is returned rather than a
        serialized empty list.
        """
        ...
    def mimeTypes(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#mimeTypes

        **[virtual protected] QStringList QTreeWidget::mimeTypes() const**

        Returns a list of MIME types that can be used to describe a list of
        treewidget items.

        **See also** **mimeData** ().
        """
        ...
    def openPersistentEditor(
        self, item: PySide6.QtWidgets.QTreeWidgetItem, column: int = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#openPersistentEditor

        **void QTreeWidget::openPersistentEditor(QTreeWidgetItem * item , int
        column = 0)**

        Opens a persistent editor for the **item** in the given **column**.

        **See also** **closePersistentEditor** () and **isPersistentEditorOpen**
        ().
        """
        ...
    def removeItemWidget(
        self, item: PySide6.QtWidgets.QTreeWidgetItem, column: int
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#removeItemWidget

        **void QTreeWidget::removeItemWidget(QTreeWidgetItem * item , int column
        )**

        Removes the widget set in the given **item** in the given **column**.
        """
        ...
    def scrollToItem(
        self,
        item: PySide6.QtWidgets.QTreeWidgetItem,
        hint: PySide6.QtWidgets.QAbstractItemView.ScrollHint = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#scrollToItem

        **[slot] void QTreeWidget::scrollToItem(const QTreeWidgetItem * item ,
        QAbstractItemView::ScrollHint hint = EnsureVisible)**

        Ensures that the **item** is visible, scrolling the view if necessary
        using the specified **hint**.

        **See also** **currentItem** (), **itemAt** (), and **topLevelItem** ().
        """
        ...
    def selectedItems(self) -> list[PySide6.QtWidgets.QTreeWidgetItem]:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#selectedItems

        **QList<QTreeWidgetItem *> QTreeWidget::selectedItems() const**

        Returns a list of all selected non-hidden items.

        **See also** **itemSelectionChanged** ().
        """
        ...
    def setColumnCount(self, columns: int) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#columnCount-prop

        **columnCount : int**

        This property holds the number of columns displayed in the tree widget

        By default, this property has a value of 1.

        **Access functions:**

        int **columnCount** () const
        void **setColumnCount** (int **columns**
        )
        """
        ...
    @overload
    def setCurrentItem(self, item: PySide6.QtWidgets.QTreeWidgetItem) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#setCurrentItem

        **void QTreeWidget::setCurrentItem(QTreeWidgetItem * item )**

        Sets the current **item** in the tree widget.

        Unless the selection mode is **NoSelection** , the item is also
        selected.

        **See also** **currentItem** () and **currentItemChanged** ().
        """
        ...
    @overload
    def setCurrentItem(
        self, item: PySide6.QtWidgets.QTreeWidgetItem, column: int
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#setCurrentItem-1

        **void QTreeWidget::setCurrentItem(QTreeWidgetItem * item , int column
        )**

        Sets the current **item** in the tree widget and the current column to
        **column**.

        **See also** **currentItem** ().
        """
        ...
    @overload
    def setCurrentItem(
        self,
        item: PySide6.QtWidgets.QTreeWidgetItem,
        column: int,
        command: PySide6.QtCore.QItemSelectionModel.SelectionFlags,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#setCurrentItem-2

        **void QTreeWidget::setCurrentItem(QTreeWidgetItem * item , int column ,
        QItemSelectionModel::SelectionFlags command )**

        Sets the current **item** in the tree widget and the current column to
        **column** , using the given **command**.

        **See also** **currentItem** ().
        """
        ...
    def setHeaderItem(self, item: PySide6.QtWidgets.QTreeWidgetItem) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#setHeaderItem

        **void QTreeWidget::setHeaderItem(QTreeWidgetItem * item )**

        Sets the header **item** for the tree widget. The label for each column
        in the header is supplied by the corresponding label in the item.

        The tree widget takes ownership of the item.

        **See also** **headerItem** () and **setHeaderLabels** ().
        """
        ...
    def setHeaderLabel(self, label: str) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#setHeaderLabel

        **void QTreeWidget::setHeaderLabel(const QString & label )**

        Same as **setHeaderLabels** (**QStringList** ( **label** )).
        """
        ...
    def setHeaderLabels(self, labels: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#setHeaderLabels

        **void QTreeWidget::setHeaderLabels(const QStringList & labels )**

        Adds a column in the header for each item in the **labels** list, and
        sets the label for each column.

        Note that setHeaderLabels() won't remove existing columns.

        **See also** **setHeaderItem** () and **setHeaderLabel** ().
        """
        ...
    def setItemWidget(
        self,
        item: PySide6.QtWidgets.QTreeWidgetItem,
        column: int,
        widget: PySide6.QtWidgets.QWidget,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#setItemWidget

        **void QTreeWidget::setItemWidget(QTreeWidgetItem * item , int column ,
        QWidget * widget )**

        Sets the given **widget** to be displayed in the cell specified by the
        given **item** and **column**.

        The given **widget** 's **autoFillBackground**  property must be set to
        true, otherwise the widget's background will be transparent, showing
        both the model data and the tree widget item.

        This function should only be used to display static content in the place
        of a tree widget item. If you want to display custom dynamic content or
        implement a custom editor widget, use **QTreeView**  and subclass
        **QStyledItemDelegate**  instead.

        This function cannot be called before the item hierarchy has been set
        up, i.e., the **QTreeWidgetItem**  that will hold **widget** must have
        been added to the view before **widget** is set.

        **Note:** The tree takes ownership of the widget.

        **See also** **itemWidget** () and **Delegate Classes** .
        """
        ...
    def setModel(self, model: PySide6.QtCore.QAbstractItemModel) -> None: ...
    def setSelectionModel(
        self, selectionModel: PySide6.QtCore.QItemSelectionModel
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#setSelectionModel

        **[override virtual] void
        QTreeWidget::setSelectionModel(QItemSelectionModel * selectionModel )**

        Reimplements: **QTreeView::setSelectionModel** (QItemSelectionModel
        *selectionModel).
        """
        ...
    def sortColumn(self) -> int:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#sortColumn

        **int QTreeWidget::sortColumn() const**

        Returns the column used to sort the contents of the widget.

        **See also** **sortItems** ().
        """
        ...
    def sortItems(self, column: int, order: PySide6.QtCore.Qt.SortOrder) -> None:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#sortItems

        **void QTreeWidget::sortItems(int column , Qt::SortOrder order )**

        Sorts the items in the widget in the specified **order** by the values
        in the given **column**.

        **See also** **sortColumn** ().
        """
        ...
    def supportedDropActions(self) -> PySide6.QtCore.Qt.DropActions:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#supportedDropActions

        **[virtual protected] Qt::DropActions
        QTreeWidget::supportedDropActions() const**

        Returns the drop actions supported by this view.

        **See also** **Qt::DropActions** .
        """
        ...
    def takeTopLevelItem(self, index: int) -> PySide6.QtWidgets.QTreeWidgetItem:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#takeTopLevelItem

        **QTreeWidgetItem *QTreeWidget::takeTopLevelItem(int index )**

        Removes the top-level item at the given **index** in the tree and
        returns it, otherwise returns `nullptr`;

        **See also** **insertTopLevelItem** (), **topLevelItem** (), and
        **topLevelItemCount** ().
        """
        ...
    def topLevelItem(self, index: int) -> PySide6.QtWidgets.QTreeWidgetItem:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#topLevelItem

        **QTreeWidgetItem *QTreeWidget::topLevelItem(int index ) const**

        Returns the top level item at the given **index** , or `nullptr` if the
        item does not exist.

        **See also** **topLevelItemCount** () and **insertTopLevelItem** ().
        """
        ...
    def topLevelItemCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#topLevelItemCount-prop

        **[read-only] topLevelItemCount : const int**

        This property holds the number of top-level items

        By default, this property has a value of 0.

        **Access functions:**

        int **topLevelItemCount** () const

        **See also** **columnCount** () and **currentItem** ().

        **Member Function Documentation**
        """
        ...
    def visualItemRect(
        self, item: PySide6.QtWidgets.QTreeWidgetItem
    ) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#visualItemRect

        **QRect QTreeWidget::visualItemRect(const QTreeWidgetItem * item )
        const**

        Returns the rectangle on the viewport occupied by the item at **item**.

        **See also** **itemAt** ().
        """
        ...
    @property
    def currentItemChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#currentItemChanged

        **[signal] void QTreeWidget::currentItemChanged(QTreeWidgetItem *
        current , QTreeWidgetItem * previous )**

        This signal is emitted when the current item changes. The current item
        is specified by **current** , and this replaces the **previous** current
        item.

        **See also** **setCurrentItem** ().
        """
        ...
    @property
    def itemActivated(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemActivated

        **[signal] void QTreeWidget::itemActivated(QTreeWidgetItem * item , int
        column )**

        This signal is emitted when the user activates an item by single- or
        double-clicking (depending on the platform, i.e. on the
        **QStyle::SH_ItemView_ActivateItemOnSingleClick**  style hint) or
        pressing a special key (e.g., **Enter** ).

        The specified **item** is the item that was clicked, or `nullptr` if no
        item was clicked. The **column** is the item's column that was clicked,
        or -1 if no item was clicked.
        """
        ...
    @property
    def itemChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemChanged

        **[signal] void QTreeWidget::itemChanged(QTreeWidgetItem * item , int
        column )**

        This signal is emitted when the contents of the **column** in the
        specified **item** changes.
        """
        ...
    @property
    def itemClicked(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemClicked

        **[signal] void QTreeWidget::itemClicked(QTreeWidgetItem * item , int
        column )**

        This signal is emitted when the user clicks inside the widget.

        The specified **item** is the item that was clicked. The **column** is
        the item's column that was clicked. If no item was clicked, no signal
        will be emitted.
        """
        ...
    @property
    def itemCollapsed(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemCollapsed

        **[signal] void QTreeWidget::itemCollapsed(QTreeWidgetItem * item )**

        This signal is emitted when the specified **item** is collapsed so that
        none of its children are displayed.

        **Note:** This signal will not be emitted if an item changes its state
        when **collapseAll** () is invoked.

        **See also** **QTreeWidgetItem::isExpanded** (), **itemExpanded** (),
        and **collapseItem** ().
        """
        ...
    @property
    def itemDoubleClicked(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemDoubleClicked

        **[signal] void QTreeWidget::itemDoubleClicked(QTreeWidgetItem * item ,
        int column )**

        This signal is emitted when the user double clicks inside the widget.

        The specified **item** is the item that was clicked, or `nullptr` if no
        item was clicked. The **column** is the item's column that was clicked.
        If no item was double clicked, no signal will be emitted.
        """
        ...
    @property
    def itemEntered(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemEntered

        **[signal] void QTreeWidget::itemEntered(QTreeWidgetItem * item , int
        column )**

        This signal is emitted when the mouse cursor enters an **item** over the
        specified **column**. **QTreeWidget**  mouse tracking needs to be
        enabled for this feature to work.
        """
        ...
    @property
    def itemExpanded(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemExpanded

        **[signal] void QTreeWidget::itemExpanded(QTreeWidgetItem * item )**

        This signal is emitted when the specified **item** is expanded so that
        all of its children are displayed.

        **Note:** This signal will not be emitted if an item changes its state
        when **expandAll** () is invoked.

        **See also** **QTreeWidgetItem::isExpanded** (), **itemCollapsed** (),
        and **expandItem** ().
        """
        ...
    @property
    def itemPressed(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemPressed

        **[signal] void QTreeWidget::itemPressed(QTreeWidgetItem * item , int
        column )**

        This signal is emitted when the user presses a mouse button inside the
        widget.

        The specified **item** is the item that was clicked, or `nullptr` if no
        item was clicked. The **column** is the item's column that was clicked,
        or -1 if no item was clicked.
        """
        ...
    @property
    def itemSelectionChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtreewidget.html#itemSelectionChanged

        **[signal] void QTreeWidget::itemSelectionChanged()**

        This signal is emitted when the selection changes in the tree widget.
        The current selection can be found with **selectedItems** ().
        """
        ...
