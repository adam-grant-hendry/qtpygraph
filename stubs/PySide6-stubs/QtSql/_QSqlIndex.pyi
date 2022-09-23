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
PySide6.QtSql, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore
import PySide6.QtSql
import PySide6.QtWidgets

class QSqlIndex(PySide6.QtSql.QSqlRecord):
    """
    https://doc.qt.io/qt-6/qsqlindex.html

    **Detailed Description**

    An **index** refers to a single table or view in a database. Information
    about the fields that comprise the index can be used to generate SQL
    statements.
    """

    @overload
    def __init__(self, cursorName: str = ..., name: str = ...) -> None:
        """
        https://doc.qt.io/qt-6/qsqlindex.html#QSqlIndex

        **QSqlIndex::QSqlIndex(const QString & cursorname = QString(), const
        QString & name = QString())**

        Constructs an empty index using the cursor name **cursorname** and index
        name **name**.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtSql.QSqlIndex) -> None:
        """
        https://doc.qt.io/qt-6/qsqlindex.html#QSqlIndex-1

        **QSqlIndex::QSqlIndex(const QSqlIndex & other )**

        Constructs a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    @overload
    def append(self, field: PySide6.QtSql.QSqlField) -> None:
        """
        https://doc.qt.io/qt-6/qsqlindex.html#append

        **void QSqlIndex::append(const QSqlField & field )**

        Appends the field **field** to the list of indexed fields. The field is
        appended with an ascending sort order.
        """
        ...
    @overload
    def append(self, field: PySide6.QtSql.QSqlField, desc: bool) -> None:
        """
        https://doc.qt.io/qt-6/qsqlindex.html#append-1

        **void QSqlIndex::append(const QSqlField & field , bool desc )**

        This is an overloaded function.

        Appends the field **field** to the list of indexed fields. The field is
        appended with an ascending sort order, unless **desc** is true.
        """
        ...
    def cursorName(self) -> str:
        """
        https://doc.qt.io/qt-6/qsqlindex.html#cursorName

        **QString QSqlIndex::cursorName() const**

        Returns the name of the cursor which the index is associated with.

        **See also** **setCursorName** ().
        """
        ...
    def isDescending(self, i: int) -> bool:
        """
        https://doc.qt.io/qt-6/qsqlindex.html#isDescending

        **bool QSqlIndex::isDescending(int i ) const**

        Returns `true` if field **i** in the index is sorted in descending
        order; otherwise returns `false`.
        """
        ...
    def name(self) -> str:
        """
        https://doc.qt.io/qt-6/qsqlindex.html#name

        **QString QSqlIndex::name() const**

        Returns the name of the index.

        **See also** **setName** ().
        """
        ...
    def setCursorName(self, cursorName: str) -> None:
        """
        https://doc.qt.io/qt-6/qsqlindex.html#setCursorName

        **void QSqlIndex::setCursorName(const QString & cursorName )**

        Sets the name of the cursor that the index is associated with to
        **cursorName**.

        **See also** **cursorName** ().
        """
        ...
    def setDescending(self, i: int, desc: bool) -> None:
        """
        https://doc.qt.io/qt-6/qsqlindex.html#setDescending

        **void QSqlIndex::setDescending(int i , bool desc )**

        If **desc** is true, field **i** is sorted in descending order.
        Otherwise, field **i** is sorted in ascending order (the default). If
        the field does not exist, nothing happens.

        **See also** **isDescending** ().
        """
        ...
    def setName(self, name: str) -> None:
        """
        https://doc.qt.io/qt-6/qsqlindex.html#setName

        **void QSqlIndex::setName(const QString & name )**

        Sets the name of the index to **name**.

        **See also** **name** ().
        """
        ...
