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
from typing import Any, overload

import PySide6.QtCore

class QJsonArray:
    """
    https://doc.qt.io/qt-6/qjsonarray.html

    **Detailed Description**

    A JSON array is a list of values. The list can be manipulated by inserting
    and removing **QJsonValue** 's from the array.

    A QJsonArray can be converted to and from a QVariantList. You can query the
    number of entries with **size** (), **insert** (), and **removeAt** ()
    entries from it and iterate over its content using the standard C++ iterator
    pattern.

    QJsonArray is an implicitly shared class and shares the data with the
    document it has been created from as long as it is not being modified.

    You can convert the array to and from text based JSON through
    **QJsonDocument** .

    **See also** **JSON Support in Qt**  and **JSON Save Game Example** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#QJsonArray

        **QJsonArray::QJsonArray()**

        Creates an empty array.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtCore.QJsonArray) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#QJsonArray-1

        **[since 5.4] QJsonArray::QJsonArray(std::initializer_list<QJsonValue>
        args )**

        Creates an array initialized from **args** initialization list.

        QJsonArray can be constructed in a way similar to JSON notation, for
        example:

        **QJsonArray**  array = { 1, 2.2, **QString** () };

        This function was introduced in Qt 5.4.
        """
        ...
    def __add__(
        self,
        v: (
            PySide6.QtCore.QJsonValue
            | PySide6.QtCore.QJsonValue.Type
            | PySide6.QtCore.QJsonArray
            | dict[str, PySide6.QtCore.QJsonValue]
            | str
            | bytes
            | float
            | int
        ),
    ) -> PySide6.QtCore.QJsonArray: ...
    @staticmethod
    def __copy__() -> None: ...
    def __iadd__(
        self,
        v: (
            PySide6.QtCore.QJsonValue
            | PySide6.QtCore.QJsonValue.Type
            | PySide6.QtCore.QJsonArray
            | dict[str, PySide6.QtCore.QJsonValue]
            | str
            | bytes
            | float
            | int
        ),
    ) -> PySide6.QtCore.QJsonArray: ...
    def __lshift__(
        self,
        v: (
            PySide6.QtCore.QJsonValue
            | PySide6.QtCore.QJsonValue.Type
            | PySide6.QtCore.QJsonArray
            | dict[str, PySide6.QtCore.QJsonValue]
            | str
            | bytes
            | float
            | int
        ),
    ) -> PySide6.QtCore.QJsonArray: ...
    def append(
        self,
        value: (
            PySide6.QtCore.QJsonValue
            | PySide6.QtCore.QJsonValue.Type
            | PySide6.QtCore.QJsonArray
            | dict[str, PySide6.QtCore.QJsonValue]
            | str
            | bytes
            | float
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#append

        **void QJsonArray::append(const QJsonValue & value )**

        Inserts **value** at the end of the array.

        **See also** **prepend** () and **insert** ().
        """
        ...
    def at(self, i: int) -> PySide6.QtCore.QJsonValue:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#at

        **QJsonValue QJsonArray::at(qsizetype i ) const**

        Returns a **QJsonValue**  representing the value for index **i**.

        The returned **QJsonValue**  is `Undefined`, if **i** is out of bounds.
        """
        ...
    def contains(
        self,
        element: (
            PySide6.QtCore.QJsonValue
            | PySide6.QtCore.QJsonValue.Type
            | PySide6.QtCore.QJsonArray
            | dict[str, PySide6.QtCore.QJsonValue]
            | str
            | bytes
            | float
            | int
        ),
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#contains

        **bool QJsonArray::contains(const QJsonValue & value ) const**

        Returns `true` if the array contains an occurrence of **value** ,
        otherwise `false`.

        **See also** **count** ().
        """
        ...
    def count(self) -> int:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#count

        **qsizetype QJsonArray::count() const**

        Same as **size** ().

        **See also** **size** ().
        """
        ...
    def empty(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#empty

        **bool QJsonArray::empty() const**

        This function is provided for STL compatibility. It is equivalent to
        **isEmpty** () and returns `true` if the array is empty.
        """
        ...
    def first(self) -> PySide6.QtCore.QJsonValue:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#first

        **QJsonValue QJsonArray::first() const**

        Returns the first value stored in the array.

        Same as `at(0)`.

        **See also** **at** ().
        """
        ...
    @staticmethod
    def fromStringList(list: Sequence[str]) -> PySide6.QtCore.QJsonArray:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#fromStringList

        **[static] QJsonArray QJsonArray::fromStringList(const QStringList &
        list )**

        Converts the string list **list** to a **QJsonArray** .

        The values in **list** will be converted to JSON values.

        **See also** **toVariantList** () and **QJsonValue::fromVariant** ().
        """
        ...
    @staticmethod
    def fromVariantList(list: Sequence[Any]) -> PySide6.QtCore.QJsonArray:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#fromVariantList

        **[static] QJsonArray QJsonArray::fromVariantList(const QVariantList &
        list )**

        Converts the variant list **list** to a **QJsonArray** .

        The **QVariant**  values in **list** will be converted to JSON values.

        **Note:** Conversion from **QVariant**  is not completely lossless.
        Please see the documentation in **QJsonValue::fromVariant** () for more
        information.

        **See also** **toVariantList** () and **QJsonValue::fromVariant** ().
        """
        ...
    def insert(
        self,
        i: int,
        value: (
            PySide6.QtCore.QJsonValue
            | PySide6.QtCore.QJsonValue.Type
            | PySide6.QtCore.QJsonArray
            | dict[str, PySide6.QtCore.QJsonValue]
            | str
            | bytes
            | float
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#insert

        **void QJsonArray::insert(qsizetype i , const QJsonValue & value )**

        Inserts **value** at index position **i** in the array. If **i** is `0`,
        the value is prepended to the array. If **i** is **size** (), the value
        is appended to the array.

        **See also** **append** (), **prepend** (), **replace** (), and
        **removeAt** ().
        """
        ...
    def isEmpty(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#isEmpty

        **bool QJsonArray::isEmpty() const**

        Returns `true` if the object is empty. This is the same as **size** ()
        == 0.

        **See also** **size** ().
        """
        ...
    def last(self) -> PySide6.QtCore.QJsonValue:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#last

        **QJsonValue QJsonArray::last() const**

        Returns the last value stored in the array.

        Same as `at(size() - 1)`.

        **See also** **at** ().
        """
        ...
    def pop_back(self) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#pop_back

        **void QJsonArray::pop_back()**

        This function is provided for STL compatibility. It is equivalent to
        **removeLast** (). The array must not be empty. If the array can be
        empty, call **isEmpty** () before calling this function.
        """
        ...
    def pop_front(self) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#pop_front

        **void QJsonArray::pop_front()**

        This function is provided for STL compatibility. It is equivalent to
        **removeFirst** (). The array must not be empty. If the array can be
        empty, call **isEmpty** () before calling this function.
        """
        ...
    def prepend(
        self,
        value: (
            PySide6.QtCore.QJsonValue
            | PySide6.QtCore.QJsonValue.Type
            | PySide6.QtCore.QJsonArray
            | dict[str, PySide6.QtCore.QJsonValue]
            | str
            | bytes
            | float
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#prepend

        **void QJsonArray::prepend(const QJsonValue & value )**

        Inserts **value** at the beginning of the array.

        This is the same as `insert(0, value)` and will prepend **value** to the
        array.

        **See also** **append** () and **insert** ().
        """
        ...
    def push_back(
        self,
        t: (
            PySide6.QtCore.QJsonValue
            | PySide6.QtCore.QJsonValue.Type
            | PySide6.QtCore.QJsonArray
            | dict[str, PySide6.QtCore.QJsonValue]
            | str
            | bytes
            | float
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#push_back

        **void QJsonArray::push_back(const QJsonValue & value )**

        This function is provided for STL compatibility. It is equivalent to
        **append** (value) and will append **value** to the array.
        """
        ...
    def push_front(
        self,
        t: (
            PySide6.QtCore.QJsonValue
            | PySide6.QtCore.QJsonValue.Type
            | PySide6.QtCore.QJsonArray
            | dict[str, PySide6.QtCore.QJsonValue]
            | str
            | bytes
            | float
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#push_front

        **void QJsonArray::push_front(const QJsonValue & value )**

        This function is provided for STL compatibility. It is equivalent to
        **prepend** (value) and will prepend **value** to the array.
        """
        ...
    def removeAt(self, i: int) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#removeAt

        **void QJsonArray::removeAt(qsizetype i )**

        Removes the value at index position **i**. **i** must be a valid index
        position in the array (i.e., `0 <= i < size()`).

        **See also** **insert** () and **replace** ().
        """
        ...
    def removeFirst(self) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#removeFirst

        **void QJsonArray::removeFirst()**

        Removes the first item in the array. Calling this function is equivalent
        to calling `removeAt(0)`. The array must not be empty. If the array can
        be empty, call **isEmpty** () before calling this function.

        **See also** **removeAt** () and **removeLast** ().
        """
        ...
    def removeLast(self) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#removeLast

        **void QJsonArray::removeLast()**

        Removes the last item in the array. Calling this function is equivalent
        to calling `removeAt(size() - 1)`. The array must not be empty. If the
        array can be empty, call **isEmpty** () before calling this function.

        **See also** **removeAt** () and **removeFirst** ().
        """
        ...
    def replace(
        self,
        i: int,
        value: (
            PySide6.QtCore.QJsonValue
            | PySide6.QtCore.QJsonValue.Type
            | PySide6.QtCore.QJsonArray
            | dict[str, PySide6.QtCore.QJsonValue]
            | str
            | bytes
            | float
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#replace

        **void QJsonArray::replace(qsizetype i , const QJsonValue & value )**

        Replaces the item at index position **i** with **value**. **i** must be
        a valid index position in the array (i.e., `0 <= i < size()`).

        **See also** **operator[]** () and **removeAt** ().
        """
        ...
    def size(self) -> int:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#size

        **qsizetype QJsonArray::size() const**

        Returns the number of values stored in the array.
        """
        ...
    def swap(self, other: PySide6.QtCore.QJsonArray) -> None:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#swap

        **[since 5.10] void QJsonArray::swap(QJsonArray & other )**

        Swaps the array **other** with this. This operation is very fast and
        never fails.

        This function was introduced in Qt 5.10.
        """
        ...
    def takeAt(self, i: int) -> PySide6.QtCore.QJsonValue:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#takeAt

        **QJsonValue QJsonArray::takeAt(qsizetype i )**

        Removes the item at index position **i** and returns it. **i** must be a
        valid index position in the array (i.e., `0 <= i < size()`).

        If you don't use the return value, **removeAt** () is more efficient.

        **See also** **removeAt** ().
        """
        ...
    def toVariantList(self) -> list[Any]:
        """
        https://doc.qt.io/qt-6/qjsonarray.html#toVariantList

        **QVariantList QJsonArray::toVariantList() const**

        Converts this object to a QVariantList.

        Returns the created map.
        """
        ...
