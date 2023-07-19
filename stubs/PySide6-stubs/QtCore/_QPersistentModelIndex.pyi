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

class QPersistentModelIndex:
    """
    https://doc.qt.io/qt-6/qpersistentmodelindex.html

    **Detailed Description**

    A QPersistentModelIndex is a model index that can be stored by an
    application, and later used to access information in a model. Unlike the
    **QModelIndex**  class, it is safe to store a QPersistentModelIndex since
    the model will ensure that references to items will continue to be valid as
    long as they can be accessed by the model.

    It is good practice to check that persistent model indexes are valid before
    using them.

    **Note:** You cannot store a **QStandardItemModel** 's QPersistentModelIndex
    in one of the model's items.

    **See also** **Model/View Programming** , **QModelIndex** , and
    **QAbstractItemModel** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qpersistentmodelindex.html#QPersistentModelIndex-
        1

        **QPersistentModelIndex::QPersistentModelIndex(const QModelIndex & index
        )**

        Creates a new QPersistentModelIndex that is a copy of the model
        **index**.
        """
        ...
    @overload
    def __init__(
        self,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpersistentmodelindex.html#QPersistentModelIndex-
        2

        **QPersistentModelIndex::QPersistentModelIndex(const
        QPersistentModelIndex & other )**

        Creates a new QPersistentModelIndex that is a copy of the **other**
        persistent model index.
        """
        ...
    @overload
    def __init__(
        self,
        other: PySide6.QtCore.QPersistentModelIndex | PySide6.QtCore.QModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpersistentmodelindex.html#QPersistentModelIndex-
        3

        **[since 5.2]
        QPersistentModelIndex::QPersistentModelIndex(QPersistentModelIndex &&
        other )**

        Move-constructs a QPersistentModelIndex instance, making it point at the
        same object that **other** was pointing to.

        This function was introduced in Qt 5.2.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def column(self) -> int:
        """
        https://doc.qt.io/qt-6/qpersistentmodelindex.html#column

        **int QPersistentModelIndex::column() const**

        Returns the column this persistent model index refers to.
        """
        ...
    def constInternalPointer(self) -> int: ...
    def data(self, role: int = ...) -> Any:
        """
        https://doc.qt.io/qt-6/qpersistentmodelindex.html#data

        **QVariant QPersistentModelIndex::data(int role = Qt::DisplayRole)
        const**

        Returns the data for the given **role** for the item referred to by the
        index.

        **See also** **Qt::ItemDataRole**  and **QAbstractItemModel::setData**
        ().
        """
        ...
    def flags(self) -> PySide6.QtCore.Qt.ItemFlags:
        """
        https://doc.qt.io/qt-6/qpersistentmodelindex.html#flags

        **Qt::ItemFlags QPersistentModelIndex::flags() const**

        Returns the flags for the item referred to by the index.
        """
        ...
    def internalId(self) -> int: ...
    def internalPointer(self) -> int: ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qpersistentmodelindex.html#isValid

        **bool QPersistentModelIndex::isValid() const**

        Returns `true` if this persistent model index is valid; otherwise
        returns `false`.

        A valid index belongs to a model, and has non-negative row and column
        numbers.

        **See also** **model** (), **row** (), and **column** ().
        """
        ...
    def model(self) -> PySide6.QtCore.QAbstractItemModel:
        """
        https://doc.qt.io/qt-6/qpersistentmodelindex.html#model

        **const QAbstractItemModel *QPersistentModelIndex::model() const**

        Returns the model that the index belongs to.
        """
        ...
    def parent(self) -> PySide6.QtCore.QModelIndex:
        """
        https://doc.qt.io/qt-6/qpersistentmodelindex.html#parent

        **QModelIndex QPersistentModelIndex::parent() const**

        Returns the parent **QModelIndex**  for this persistent index, or an
        invalid **QModelIndex**  if it has no parent.

        **See also** **sibling** () and **model** ().
        """
        ...
    def row(self) -> int:
        """
        https://doc.qt.io/qt-6/qpersistentmodelindex.html#row

        **int QPersistentModelIndex::row() const**

        Returns the row this persistent model index refers to.
        """
        ...
    def sibling(self, row: int, column: int) -> PySide6.QtCore.QModelIndex:
        """
        https://doc.qt.io/qt-6/qpersistentmodelindex.html#sibling

        **QModelIndex QPersistentModelIndex::sibling(int row , int column )
        const**

        Returns the sibling at **row** and **column** or an invalid
        **QModelIndex**  if there is no sibling at this position.

        **See also** **parent** ().
        """
        ...
    def swap(
        self,
        other: PySide6.QtCore.QPersistentModelIndex | PySide6.QtCore.QModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpersistentmodelindex.html#swap

        **[since 5.0] void QPersistentModelIndex::swap(QPersistentModelIndex &
        other )**

        Swaps this persistent modelindex with **other**. This function is very
        fast and never fails.

        This function was introduced in Qt 5.0.
        """
        ...