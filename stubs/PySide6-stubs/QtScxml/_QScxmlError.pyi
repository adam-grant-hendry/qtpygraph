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
PySide6.QtScxml, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore
import PySide6.QtScxml

class QScxmlError:
    """
    https://doc.qt.io/qt-6/qscxmlerror.html

    **Detailed Description**

    **See also** **QScxmlStateMachine**  and **QScxmlCompiler** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlerror.html#QScxmlError

        **QScxmlError::QScxmlError()**

        Creates a new invalid SCXML error.
        """
        ...
    @overload
    def __init__(self, arg__1: PySide6.QtScxml.QScxmlError) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlerror.html#QScxmlError-1

        **QScxmlError::QScxmlError(const QString & fileName , int line , int
        column , const QString & description )**

        Creates a new valid SCXML error that contains the error message,
        **description** , as well as the **fileName** , **line** , and
        **column** where the error occurred.
        """
        ...
    @overload
    def __init__(self, fileName: str, line: int, column: int, description: str) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlerror.html#QScxmlError-2

        **QScxmlError::QScxmlError(const QScxmlError & other )**

        Constructs a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def column(self) -> int:
        """
        https://doc.qt.io/qt-6/qscxmlerror.html#column

        **int QScxmlError::column() const**

        Returns the column in which the error occurred.

        **Note:** Getter function for property column.
        """
        ...
    def description(self) -> str:
        """
        https://doc.qt.io/qt-6/qscxmlerror.html#description

        **QString QScxmlError::description() const**

        Returns the error message.

        **Note:** Getter function for property **description** .
        """
        ...
    def fileName(self) -> str:
        """
        https://doc.qt.io/qt-6/qscxmlerror.html#fileName

        **QString QScxmlError::fileName() const**

        Returns the name of the file in which the error occurred.

        **Note:** Getter function for property fileName.
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlerror.html#isValid

        **bool QScxmlError::isValid() const**

        Returns `true` if the error is valid, `false` otherwise. An invalid
        error can only be created by calling the default constructor or by
        assigning an invalid error.

        **Note:** Getter function for property **valid** .
        """
        ...
    def line(self) -> int:
        """
        https://doc.qt.io/qt-6/qscxmlerror.html#line

        **int QScxmlError::line() const**

        Returns the line on which the error occurred.

        **Note:** Getter function for property line.
        """
        ...
    def toString(self) -> str:
        """
        https://doc.qt.io/qt-6/qscxmlerror.html#toString

        **QString QScxmlError::toString() const**

        This convenience method converts an error to a string. Returns the error
        message formatted as: **"filename:line:column: error: description"**
        """
        ...