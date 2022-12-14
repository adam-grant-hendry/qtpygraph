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

from collections.abc import Sequence
from typing import overload

import PySide6.QtCore

class QItemSelection:
    """
    https://doc.qt.io/qt-6/qitemselection.html

    **Detailed Description**

    A QItemSelection describes the items in a model that have been selected by
    the user. A QItemSelection is basically a list of selection ranges, see
    **QItemSelectionRange** . It provides functions for creating and
    manipulating selections, and selecting a range of items from a model.

    The QItemSelection class is one of the **Model/View Classes**  and is part
    of Qt's **model/view framework** .

    An item selection can be constructed and initialized to contain a range of
    items from an existing model. The following example constructs a selection
    that contains a range of items from the given `model`, beginning at the
    `topLeft`, and ending at the `bottomRight`.

    **QItemSelection**  *selection = new **QItemSelection** (topLeft,
    bottomRight);

    An empty item selection can be constructed, and later populated as required.
    So, if the model is going to be unavailable when we construct the item
    selection, we can rewrite the above code in the following way:

    **QItemSelection**  *selection = new **QItemSelection** ();
        ...
    selection->select(topLeft, bottomRight);

    QItemSelection saves memory, and avoids unnecessary work, by working with
    selection ranges rather than recording the model item index for each item in
    the selection. Generally, an instance of this class will contain a list of
    non-overlapping selection ranges.

    Use **merge** () to merge one item selection into another without making
    overlapping ranges. Use **split** () to split one selection range into
    smaller ranges based on a another selection range.

    **See also** **Model/View Programming**  and **QItemSelectionModel** .
    """

    @overload
    def __init__(self) -> PySide6.QtCore.QItemSelection:
        """
        https://doc.qt.io/qt-6/qitemselection.html#QItemSelection

        **QItemSelection::QItemSelection(const QModelIndex & topLeft , const
        QModelIndex & bottomRight )**

        Constructs an item selection that extends from the top-left model item,
        specified by the **topLeft** index, to the bottom-right item, specified
        by **bottomRight**.
        """
        ...
    @overload
    def __init__(self, QItemSelection: PySide6.QtCore.QItemSelection) -> None:
        """
        https://doc.qt.io/qt-6/qitemselection.html#QItemSelection-1

        **[default] QItemSelection::QItemSelection()**

        Constructs an empty selection.
        """
        ...
    @overload
    def __init__(
        self,
        topLeft: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        bottomRight: (PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemselection.html#QItemSelection

        **QItemSelection::QItemSelection(const QModelIndex & topLeft , const
        QModelIndex & bottomRight )**

        Constructs an item selection that extends from the top-left model item,
        specified by the **topLeft** index, to the bottom-right item, specified
        by **bottomRight**.
        """
        ...
    def __add__(
        self, arg__1: PySide6.QtCore.QItemSelection
    ) -> PySide6.QtCore.QItemSelection: ...
    @staticmethod
    def __copy__() -> None: ...
    def __iadd__(
        self, l: Sequence[PySide6.QtCore.QItemSelectionRange]
    ) -> list[PySide6.QtCore.QItemSelectionRange]: ...
    def __lshift__(
        self, l: Sequence[PySide6.QtCore.QItemSelectionRange]
    ) -> list[PySide6.QtCore.QItemSelectionRange]: ...
    @overload
    def append(self, arg__1: PySide6.QtCore.QItemSelectionRange) -> None: ...
    @overload
    def append(self, l: Sequence[PySide6.QtCore.QItemSelectionRange]) -> None: ...
    def at(self, i: int) -> PySide6.QtCore.QItemSelectionRange: ...
    def back(self) -> PySide6.QtCore.QItemSelectionRange: ...
    def capacity(self) -> int: ...
    def clear(self) -> None: ...
    def constData(self) -> PySide6.QtCore.QItemSelectionRange: ...
    def constFirst(self) -> PySide6.QtCore.QItemSelectionRange: ...
    def constLast(self) -> PySide6.QtCore.QItemSelectionRange: ...
    def contains(
        self,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qitemselection.html#contains

        **bool QItemSelection::contains(const QModelIndex & index ) const**

        Returns `true` if the selection contains the given **index** ; otherwise
        returns `false`.
        """
        ...
    def count(self) -> int: ...
    def data(self) -> PySide6.QtCore.QItemSelectionRange: ...
    def empty(self) -> bool: ...
    @overload
    def first(self) -> PySide6.QtCore.QItemSelectionRange: ...
    @overload
    def first(self, n: int) -> list[PySide6.QtCore.QItemSelectionRange]: ...
    @staticmethod
    def fromList(
        list: Sequence[PySide6.QtCore.QItemSelectionRange],
    ) -> list[PySide6.QtCore.QItemSelectionRange]: ...
    @staticmethod
    def fromVector(
        vector: Sequence[PySide6.QtCore.QItemSelectionRange],
    ) -> list[PySide6.QtCore.QItemSelectionRange]: ...
    def front(self) -> PySide6.QtCore.QItemSelectionRange: ...
    def indexes(self) -> list[int]:
        """
        https://doc.qt.io/qt-6/qitemselection.html#indexes

        **QModelIndexList QItemSelection::indexes() const**

        Returns a list of model indexes that correspond to the selected items.
        """
        ...
    def insert(self, arg__1: int, arg__2: PySide6.QtCore.QItemSelectionRange) -> None: ...
    def isEmpty(self) -> bool: ...
    def isSharedWith(
        self, other: Sequence[PySide6.QtCore.QItemSelectionRange]
    ) -> bool: ...
    @overload
    def last(self) -> PySide6.QtCore.QItemSelectionRange: ...
    @overload
    def last(self, n: int) -> list[PySide6.QtCore.QItemSelectionRange]: ...
    def length(self) -> int: ...
    def merge(
        self,
        other: PySide6.QtCore.QItemSelection,
        command: PySide6.QtCore.QItemSelectionModel.SelectionFlags,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemselection.html#merge

        **void QItemSelection::merge(const QItemSelection & other ,
        QItemSelectionModel::SelectionFlags command )**

        Merges the **other** selection with this **QItemSelection**  using the
        **command** given. This method guarantees that no ranges are
        overlapping.

        Note that only **QItemSelectionModel::Select** ,
        **QItemSelectionModel::Deselect** , and **QItemSelectionModel::Toggle**
        are supported.

        **See also** **split** ().
        """
        ...
    def mid(
        self, pos: int, len: int = ...
    ) -> list[PySide6.QtCore.QItemSelectionRange]: ...
    def move(self, from_: int, to: int) -> None: ...
    def pop_back(self) -> None: ...
    def pop_front(self) -> None: ...
    def prepend(self, arg__1: PySide6.QtCore.QItemSelectionRange) -> None: ...
    def push_back(self, arg__1: PySide6.QtCore.QItemSelectionRange) -> None: ...
    def push_front(self, arg__1: PySide6.QtCore.QItemSelectionRange) -> None: ...
    def remove(self, i: int, n: int = ...) -> None: ...
    def removeAll(self, arg__1: PySide6.QtCore.QItemSelectionRange) -> None: ...
    def removeAt(self, i: int) -> None: ...
    def removeFirst(self) -> None: ...
    def removeLast(self) -> None: ...
    def removeOne(self, arg__1: PySide6.QtCore.QItemSelectionRange) -> None: ...
    def reserve(self, size: int) -> None: ...
    def resize(self, size: int) -> None: ...
    def select(
        self,
        topLeft: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        bottomRight: (PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemselection.html#select

        **void QItemSelection::select(const QModelIndex & topLeft , const
        QModelIndex & bottomRight )**

        Adds the items in the range that extends from the top-left model item,
        specified by the **topLeft** index, to the bottom-right item, specified
        by **bottomRight** to the list.

        **Note:** **topLeft** and **bottomRight** must have the same parent.
        """
        ...
    def shrink_to_fit(self) -> None: ...
    def size(self) -> int: ...
    @overload
    def sliced(self, pos: int) -> list[PySide6.QtCore.QItemSelectionRange]: ...
    @overload
    def sliced(self, pos: int, n: int) -> list[PySide6.QtCore.QItemSelectionRange]: ...
    @staticmethod
    def split(
        range: PySide6.QtCore.QItemSelectionRange,
        other: PySide6.QtCore.QItemSelectionRange,
        result: PySide6.QtCore.QItemSelection,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemselection.html#split

        **[static] void QItemSelection::split(const QItemSelectionRange & range
        , const QItemSelectionRange & other , QItemSelection * result )**

        Splits the selection **range** using the selection **other** range.
        Removes all items in **other** from **range** and puts the result in
        **result**. This can be compared with the semantics of the **subtract**
        operation of a set.

        **See also** **merge** ().
        """
        ...
    def squeeze(self) -> None: ...
    def swap(self, other: Sequence[PySide6.QtCore.QItemSelectionRange]) -> None: ...
    def swapItemsAt(self, i: int, j: int) -> None: ...
    def takeAt(self, i: int) -> PySide6.QtCore.QItemSelectionRange: ...
    def toList(self) -> list[PySide6.QtCore.QItemSelectionRange]: ...
    def toVector(self) -> list[PySide6.QtCore.QItemSelectionRange]: ...
    def value(self, i: int) -> PySide6.QtCore.QItemSelectionRange: ...
