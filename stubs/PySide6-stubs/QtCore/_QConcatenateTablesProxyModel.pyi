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

from typing import Any, overload

import PySide6.QtCore

class QConcatenateTablesProxyModel(PySide6.QtCore.QAbstractItemModel):
    """
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html

    **Detailed Description**

    QConcatenateTablesProxyModel takes multiple source models and concatenates
    their rows.

    In other words, the proxy will have all rows of the first source model,
    followed by all rows of the second source model, and so on.

    If the source models don't have the same number of columns, the proxy will
    only have as many columns as the source model with the smallest number of
    columns. Additional columns in other source models will simply be ignored.

    Source models can be added and removed at runtime, and the column count is
    adjusted accordingly.

    This proxy does not inherit from **QAbstractProxyModel**  because it uses
    multiple source models, rather than a single one.

    Only flat models (lists and tables) are supported, tree models are not.

    **See also** **QAbstractProxyModel** , **Model/View Programming** ,
    **QIdentityProxyModel** , and **QAbstractItemModel** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#QConcatenateTab
        lesProxyModel

        **QConcatenateTablesProxyModel::QConcatenateTablesProxyModel(QObject *
        parent = nullptr)**

        Constructs a concatenate-rows proxy model with the given **parent**.
        """
        ...
    def addSourceModel(self, sourceModel: PySide6.QtCore.QAbstractItemModel) -> None:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#addSourceModel

        **void QConcatenateTablesProxyModel::addSourceModel(QAbstractItemModel *
        sourceModel )**

        Adds a source model **sourceModel** , below all previously added source
        models.

        The ownership of **sourceModel** is not affected by this.

        The same source model cannot be added more than once.
        """
        ...
    def canDropMimeData(
        self,
        data: PySide6.QtCore.QMimeData,
        action: PySide6.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#canDropMimeData

        **[override virtual] bool
        QConcatenateTablesProxyModel::canDropMimeData(const QMimeData * data ,
        Qt::DropAction action , int row , int column , const QModelIndex &
        parent ) const**

        Reimplements: **QAbstractItemModel::canDropMimeData(const QMimeData
        *data, Qt::DropAction action, int row, int column, const QModelIndex
        &parent) const** .
        """
        ...
    def columnCount(
        self,
        parent: (PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) = ...,
    ) -> int:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#columnCount

        **[override virtual] int QConcatenateTablesProxyModel::columnCount(const
        QModelIndex & parent = QModelIndex()) const**

        Reimplements: **QAbstractItemModel::columnCount(const QModelIndex
        &parent) const** .

        This method returns the column count of the source model with the
        smallest number of columns.
        """
        ...
    def data(
        self,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        role: int = ...,
    ) -> Any:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#data

        **[override virtual] QVariant QConcatenateTablesProxyModel::data(const
        QModelIndex & index , int role = Qt::DisplayRole) const**

        Reimplements: **QAbstractItemModel::data(const QModelIndex &index, int
        role) const** .

        **See also** **setData** ().
        """
        ...
    def dropMimeData(
        self,
        data: PySide6.QtCore.QMimeData,
        action: PySide6.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#dropMimeData

        **[override virtual] bool
        QConcatenateTablesProxyModel::dropMimeData(const QMimeData * data ,
        Qt::DropAction action , int row , int column , const QModelIndex &
        parent )**

        Reimplements: **QAbstractItemModel::dropMimeData** (const QMimeData
        *data, Qt::DropAction action, int row, int column, const QModelIndex
        &parent).

        **QConcatenateTablesProxyModel**  handles dropping onto an item, between
        items, and after the last item. In all cases the call is forwarded to
        the underlying source model. When dropping onto an item, the source
        model for this item is called. When dropping between items, the source
        model immediately below the drop position is called. When dropping after
        the last item, the last source model is called.
        """
        ...
    def flags(
        self,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> PySide6.QtCore.Qt.ItemFlags:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#flags

        **[override virtual] Qt::ItemFlags
        QConcatenateTablesProxyModel::flags(const QModelIndex & index ) const**

        Reimplements: **QAbstractItemModel::flags(const QModelIndex &index)
        const** .

        Returns the flags for the given index. If the **index** is valid, the
        flags come from the source model for this **index**. If the **index** is
        invalid (as used to determine if dropping onto an empty area in the view
        is allowed, for instance), the flags from the first model are returned.
        """
        ...
    def headerData(
        self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int = ...
    ) -> Any:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#headerData

        **[override virtual] QVariant
        QConcatenateTablesProxyModel::headerData(int section , Qt::Orientation
        orientation , int role = Qt::DisplayRole) const**

        Reimplements: **QAbstractItemModel::headerData(int section,
        Qt::Orientation orientation, int role) const** .

        This method returns the horizontal header data for the first source
        model, and the vertical header data for the source model corresponding
        to each row.
        """
        ...
    def index(
        self,
        row: int,
        column: int,
        parent: (PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) = ...,
    ) -> PySide6.QtCore.QModelIndex:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#index

        **[override virtual] QModelIndex QConcatenateTablesProxyModel::index(int
        row , int column , const QModelIndex & parent = QModelIndex()) const**

        Reimplements: **QAbstractItemModel::index(int row, int column, const
        QModelIndex &parent) const** .
        """
        ...
    def itemData(
        self,
        proxyIndex: (PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex),
    ) -> dict[int, Any]:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#itemData

        **[override virtual] QMap<int, QVariant>
        QConcatenateTablesProxyModel::itemData(const QModelIndex & proxyIndex )
        const**

        Reimplements: **QAbstractItemModel::itemData(const QModelIndex &index)
        const** .

        **See also** **setItemData** ().
        """
        ...
    def mapFromSource(
        self,
        sourceIndex: (PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex),
    ) -> PySide6.QtCore.QModelIndex:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#mapFromSource

        **QModelIndex QConcatenateTablesProxyModel::mapFromSource(const
        QModelIndex & sourceIndex ) const**

        Returns the proxy index for a given **sourceIndex** , which can be from
        any of the source models.
        """
        ...
    def mapToSource(
        self,
        proxyIndex: (PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex),
    ) -> PySide6.QtCore.QModelIndex:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#mapToSource

        **QModelIndex QConcatenateTablesProxyModel::mapToSource(const
        QModelIndex & proxyIndex ) const**

        Returns the source index for a given **proxyIndex**.
        """
        ...
    def mimeData(self, indexes: list[int]) -> PySide6.QtCore.QMimeData:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#mimeData

        **[override virtual] QMimeData
        *QConcatenateTablesProxyModel::mimeData(const QModelIndexList & indexes
        ) const**

        Reimplements: **QAbstractItemModel::mimeData(const QModelIndexList
        &indexes) const** .

        The call is forwarded to the source model of the first index in the list
        of **indexes**.

        Important: please note that this proxy only supports dragging a single
        row. It will assert if called with indexes from multiple rows, because
        dragging rows that might come from different source models cannot be
        implemented generically by this proxy model. Each piece of data in the
        **QMimeData**  needs to be merged, which is data-type-specific.
        Reimplement this method in a subclass if you want to support dragging
        multiple rows.
        """
        ...
    def mimeTypes(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#mimeTypes

        **[override virtual] QStringList
        QConcatenateTablesProxyModel::mimeTypes() const**

        Reimplements: **QAbstractItemModel::mimeTypes() const** .

        This method returns the mime types for the first source model.
        """
        ...
    @overload
    def parent(self) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#parent

        **[override virtual] QModelIndex
        QConcatenateTablesProxyModel::parent(const QModelIndex & index ) const**

        Reimplements: **QAbstractItemModel::parent(const QModelIndex &index)
        const** .
        """
        ...
    @overload
    def parent(
        self,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> PySide6.QtCore.QModelIndex:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#parent

        **[override virtual] QModelIndex
        QConcatenateTablesProxyModel::parent(const QModelIndex & index ) const**

        Reimplements: **QAbstractItemModel::parent(const QModelIndex &index)
        const** .
        """
        ...
    def removeSourceModel(self, sourceModel: PySide6.QtCore.QAbstractItemModel) -> None:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#removeSourceMod
        el

        **void
        QConcatenateTablesProxyModel::removeSourceModel(QAbstractItemModel *
        sourceModel )**

        Removes the source model **sourceModel** , which was previously added to
        this proxy.

        The ownership of **sourceModel** is not affected by this.
        """
        ...
    def rowCount(
        self,
        parent: (PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) = ...,
    ) -> int:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#rowCount

        **[override virtual] int QConcatenateTablesProxyModel::rowCount(const
        QModelIndex & parent = QModelIndex()) const**

        Reimplements: **QAbstractItemModel::rowCount(const QModelIndex &parent)
        const** .
        """
        ...
    def setData(
        self,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        value: Any,
        role: int = ...,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#setData

        **[override virtual] bool QConcatenateTablesProxyModel::setData(const
        QModelIndex & index , const QVariant & value , int role =
        Qt::EditRole)**

        Reimplements: **QAbstractItemModel::setData** (const QModelIndex &index,
        const QVariant &value, int role).

        **See also** **data** ().
        """
        ...
    def setItemData(
        self,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        roles: dict[int, Any],
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#setItemData

        **[override virtual] bool
        QConcatenateTablesProxyModel::setItemData(const QModelIndex & proxyIndex
        , const QMap<int, QVariant> & roles )**

        Reimplements: **QAbstractItemModel::setItemData** (const QModelIndex
        &index, const QMap<int, QVariant> &roles).

        **See also** **itemData** ().
        """
        ...
    def sourceModels(self) -> list[PySide6.QtCore.QAbstractItemModel]:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#sourceModels

        **[since 5.15] QList<QAbstractItemModel *>
        QConcatenateTablesProxyModel::sourceModels() const**

        Returns a list of models that were added as source models for this proxy
        model.

        This function was introduced in Qt 5.15.
        """
        ...
    def span(
        self,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#span

        **[override virtual] QSize QConcatenateTablesProxyModel::span(const
        QModelIndex & index ) const**

        Reimplements: **QAbstractItemModel::span(const QModelIndex &index)
        const** .
        """
        ...
