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

from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtSql
import PySide6.QtWidgets

class QSqlError:
    """
    https://doc.qt.io/qt-6/qsqlerror.html

    **Detailed Description**

    A QSqlError object can provide database-specific error data, including the
    **driverText** () and **databaseText** () messages (or both concatenated
    together as **text** ()), and the **nativeErrorCode** () and **type** ().

    **See also** **QSqlDatabase::lastError** () and **QSqlQuery::lastError** ().
    """

    NoError: QSqlError.ErrorType = ...
    ConnectionError: QSqlError.ErrorType = ...
    StatementError: QSqlError.ErrorType = ...
    TransactionError: QSqlError.ErrorType = ...
    UnknownError: QSqlError.ErrorType = ...

    class ErrorType(IntFlag):
        NoError: QSqlError.ErrorType = ...
        ConnectionError: QSqlError.ErrorType = ...
        StatementError: QSqlError.ErrorType = ...
        TransactionError: QSqlError.ErrorType = ...
        UnknownError: QSqlError.ErrorType = ...
    @overload
    def __init__(
        self,
        driverText: str = ...,
        databaseText: str = ...,
        type: PySide6.QtSql.QSqlError.ErrorType = ...,
        errorCode: str = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsqlerror.html#QSqlError

        **QSqlError::QSqlError(const QString & driverText = QString(), const
        QString & databaseText = QString(), QSqlError::ErrorType type = NoError,
        const QString & code = QString())**

        Constructs an error containing the driver error text **driverText** ,
        the database-specific error text **databaseText** , the type **type**
        and the error code **code**.

        **Note:** DB2: It is possible for DB2 to report more than one error
        code. When this happens, `;` is used as separator between the error
        codes.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtSql.QSqlError) -> None:
        """
        https://doc.qt.io/qt-6/qsqlerror.html#QSqlError-1

        **QSqlError::QSqlError(const QSqlError & other )**

        Creates a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def databaseText(self) -> str:
        """
        https://doc.qt.io/qt-6/qsqlerror.html#databaseText

        **QString QSqlError::databaseText() const**

        Returns the text of the error as reported by the database. This may
        contain database-specific descriptions; it may be empty.

        **See also** **driverText** () and **text** ().
        """
        ...
    def driverText(self) -> str:
        """
        https://doc.qt.io/qt-6/qsqlerror.html#driverText

        **QString QSqlError::driverText() const**

        Returns the text of the error as reported by the driver. This may
        contain database-specific descriptions. It may also be empty.

        **See also** **databaseText** () and **text** ().
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsqlerror.html#isValid

        **bool QSqlError::isValid() const**

        Returns `true` if an error is set, otherwise false.

        Example:

        **QSqlQueryModel**  model;
            model.setQuery("select * from myTable");
        if (model.lastError().isValid())
                **qDebug** () <<
        model.lastError();

        **See also** **type** ().
        """
        ...
    def nativeErrorCode(self) -> str:
        """
        https://doc.qt.io/qt-6/qsqlerror.html#nativeErrorCode

        **QString QSqlError::nativeErrorCode() const**

        Returns the database-specific error code, or an empty string if it
        cannot be determined.
        """
        ...
    def swap(self, other: PySide6.QtSql.QSqlError) -> None:
        """
        https://doc.qt.io/qt-6/qsqlerror.html#swap

        **[since 5.10] void QSqlError::swap(QSqlError & other )**

        Swaps error **other** with this error. This operation is very fast and
        never fails.

        This function was introduced in Qt 5.10.
        """
        ...
    def text(self) -> str:
        """
        https://doc.qt.io/qt-6/qsqlerror.html#text

        **QString QSqlError::text() const**

        This is a convenience function that returns **databaseText** () and
        **driverText** () concatenated into a single string.

        **See also** **driverText** () and **databaseText** ().
        """
        ...
    def type(self) -> PySide6.QtSql.QSqlError.ErrorType:
        """
        https://doc.qt.io/qt-6/qsqlerror.html#type

        **QSqlError::ErrorType QSqlError::type() const**

        Returns the error type, or -1 if the type cannot be determined.
        """
        ...
