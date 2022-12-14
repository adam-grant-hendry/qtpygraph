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

import PySide6.QtCore
import PySide6.QtScxml

class QScxmlInvokableService(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qscxmlinvokableservice.html

    **Detailed Description**

    The services are called from state machines via the mechanism described in
    **SCXML Specification - 6.4 <invoke>** . This class represents an actual
    instance of an invoked service.
    """

    def __init__(
        self,
        parentStateMachine: PySide6.QtScxml.QScxmlStateMachine,
        parent: PySide6.QtScxml.QScxmlInvokableServiceFactory,
    ) -> None: ...
    def id(self) -> str:
        """
        https://doc.qt.io/qt-6/qscxmlinvokableservice.html#id-prop

        **[read-only] id : const QString**

        This property holds the ID of the invokable service.

        The ID is specified by the `id` attribute of the `<invoke>` element.

        **Access functions:**

        virtual QString **id** () const = 0
        """
        ...
    def name(self) -> str:
        """
        https://doc.qt.io/qt-6/qscxmlinvokableservice.html#name-prop

        **[read-only] name : const QString**

        This property holds the name of the service being invoked.

        **Access functions:**

        virtual QString **name** () const = 0
        """
        ...
    def parentStateMachine(self) -> PySide6.QtScxml.QScxmlStateMachine:
        """
        https://doc.qt.io/qt-6/qscxmlinvokableservice.html#parentStateMachine-
        prop

        **[read-only] parentStateMachine : QScxmlStateMachine* const**

        This property holds the SCXML state machine that invoked the service.

        **Access functions:**

        QScxmlStateMachine * **parentStateMachine** () const

        **Member Function Documentation**
        """
        ...
    def postEvent(self, event: PySide6.QtScxml.QScxmlEvent) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlinvokableservice.html#postEvent

        **[pure virtual] void QScxmlInvokableService::postEvent(QScxmlEvent *
        event )**

        Sends an **event** to the service.
        """
        ...
    def start(self) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlinvokableservice.html#start

        **[pure virtual] bool QScxmlInvokableService::start()**

        Starts the invokable service. Returns `true` on success, or `false` if
        the invocation fails.
        """
        ...
