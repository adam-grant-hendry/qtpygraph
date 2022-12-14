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

from collections.abc import Sequence

import PySide6.QtCore
import PySide6.QtScxml

class QScxmlInvokableServiceFactory(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qscxmlinvokableservicefactory.html

    **Detailed Description**

    Each service instance represents an `<invoke>` element in the SCXML
    document. Each time the service is actually invoked, a new instance of
    **QScxmlInvokableService**  is created.
    """

    def __init__(
        self,
        invokeInfo: PySide6.QtScxml.QScxmlExecutableContent.InvokeInfo,
        names: Sequence[int],
        parameters: Sequence[PySide6.QtScxml.QScxmlExecutableContent.ParameterInfo],
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None: ...
    def invoke(
        self, parentStateMachine: PySide6.QtScxml.QScxmlStateMachine
    ) -> PySide6.QtScxml.QScxmlInvokableService:
        """
        https://doc.qt.io/qt-6/qscxmlinvokableservicefactory.html#invoke

        **[pure virtual] QScxmlInvokableService
        *QScxmlInvokableServiceFactory::invoke(QScxmlStateMachine *
        parentStateMachine )**

        Invokes the service with the parameters given in the constructor,
        passing **parentStateMachine** as the parent. Returns the new invokable
        service.
        """
        ...
    def invokeInfo(self) -> PySide6.QtScxml.QScxmlExecutableContent.InvokeInfo:
        """
        https://doc.qt.io/qt-6/qscxmlinvokableservicefactory.html#invokeInfo-
        prop

        **[read-only] invokeInfo : const QScxmlExecutableContent::InvokeInfo**

        This property holds the **QScxmlExecutableContent::InvokeInfo**  passed
        to the constructor.

        **Access functions:**

        const QScxmlExecutableContent::InvokeInfo & **invokeInfo** () const
        """
        ...
    def names(self) -> list[int]:
        """
        https://doc.qt.io/qt-6/qscxmlinvokableservicefactory.html#names-prop

        **[read-only] names : const QList<QScxmlExecutableContent::StringId>**

        This property holds the names passed to the constructor.

        **Access functions:**

        const QList<QScxmlExecutableContent::StringId> & **names** () const
        """
        ...
    def parameters(self) -> list[PySide6.QtScxml.QScxmlExecutableContent.ParameterInfo]:
        """
        https://doc.qt.io/qt-6/qscxmlinvokableservicefactory.html#parameters-
        prop

        **[read-only] parameters : const
        QList<QScxmlExecutableContent::ParameterInfo>**

        This property holds the parameters passed to the constructor.

        **Access functions:**

        const QList<QScxmlExecutableContent::ParameterInfo> & **parameters** ()
        const

        **Member Function Documentation**
        """
        ...
