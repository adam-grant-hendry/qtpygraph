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

from typing import Any

import PySide6.QtCore
import PySide6.QtScxml

class QScxmlDataModel(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qscxmldatamodel.html

    **Detailed Description**

    SCXML data models are described in **SCXML Specification - 5 Data Model and
    Data Manipulation** . For more information about supported data models, see
    **SCXML Compliance** .

    One data model can only belong to one state machine.

    **See also** **QScxmlStateMachine** , **QScxmlCppDataModel** , and
    **QScxmlNullDataModel** .
    """

    class ForeachLoopBody:
        def __init__(self) -> None: ...
        def run(self) -> bool: ...

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#QScxmlDataModel

        **QScxmlDataModel::QScxmlDataModel(QObject * parent = nullptr)**

        Creates a new data model, with the parent object **parent**.
        """
        ...
    @staticmethod
    def createScxmlDataModel(pluginKey: str) -> PySide6.QtScxml.QScxmlDataModel:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#createScxmlDataModel

        **[static] QScxmlDataModel *QScxmlDataModel::createScxmlDataModel(const
        QString & pluginKey )**

        Creates a data model from a plugin specified by a **pluginKey**.
        """
        ...
    def evaluateAssignment(self, id: int) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#evaluateAssignment

        **[pure virtual] void
        QScxmlDataModel::evaluateAssignment(QScxmlExecutableContent::EvaluatorId
        id , bool * ok )**

        Evaluates the assignment pointed to by **id** and sets **ok** to `false`
        if there was an error or to `true` if there was not.
        """
        ...
    def evaluateForeach(
        self, id: int, body: PySide6.QtScxml.QScxmlDataModel.ForeachLoopBody
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#evaluateForeach

        **[pure virtual] void
        QScxmlDataModel::evaluateForeach(QScxmlExecutableContent::EvaluatorId id
        , bool * ok , QScxmlDataModel::ForeachLoopBody * body )**

        Evaluates the foreach loop pointed to by **id** and sets **ok** to
        `false` if there was an error or to `true` if there was not. The
        **body** is executed on each iteration.
        """
        ...
    def evaluateInitialization(self, id: int) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#evaluateInitialization

        **[pure virtual] void QScxmlDataModel::evaluateInitialization(QScxmlExec
        utableContent::EvaluatorId id , bool * ok )**

        Evaluates the initialization pointed to by **id** and sets **ok** to
        `false` if there was an error or to `true` if there was not.
        """
        ...
    def evaluateToBool(self, id: int) -> tuple[bool, bool]:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#evaluateToBool

        **[pure virtual] bool
        QScxmlDataModel::evaluateToBool(QScxmlExecutableContent::EvaluatorId id
        , bool * ok )**

        Evaluates the executable content pointed to by **id** and sets **ok** to
        `false` if there was an error or to `true` if there was not. Returns the
        result of the evaluation as a boolean value.
        """
        ...
    def evaluateToString(self, id: int) -> tuple[str, bool]:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#evaluateToString

        **[pure virtual] QString
        QScxmlDataModel::evaluateToString(QScxmlExecutableContent::EvaluatorId
        id , bool * ok )**

        Evaluates the executable content pointed to by **id** and sets **ok** to
        `false` if there was an error or to `true` if there was not. Returns the
        result of the evaluation as a **QString** .
        """
        ...
    def evaluateToVariant(self, id: int) -> tuple[Any, bool]:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#evaluateToVariant

        **[pure virtual] QVariant
        QScxmlDataModel::evaluateToVariant(QScxmlExecutableContent::EvaluatorId
        id , bool * ok )**

        Evaluates the executable content pointed to by **id** and sets **ok** to
        `false` if there was an error or to `true` if there was not. Returns the
        result of the evaluation as a **QVariant** .
        """
        ...
    def evaluateToVoid(self, id: int) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#evaluateToVoid

        **[pure virtual] void
        QScxmlDataModel::evaluateToVoid(QScxmlExecutableContent::EvaluatorId id
        , bool * ok )**

        Evaluates the executable content pointed to by **id** and sets **ok** to
        `false` if there was an error or to `true` if there was not. The
        execution is expected to return no result.
        """
        ...
    def hasScxmlProperty(self, name: str) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#hasScxmlProperty

        **[pure virtual] bool QScxmlDataModel::hasScxmlProperty(const QString &
        name ) const**

        Returns `true` if a property with the given **name** exists, `false`
        otherwise.
        """
        ...
    def scxmlProperty(self, name: str) -> Any:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#scxmlProperty

        **[pure virtual] QVariant QScxmlDataModel::scxmlProperty(const QString &
        name ) const**

        Returns the value of the property **name**.

        **See also** **setScxmlProperty** ().
        """
        ...
    def setScxmlEvent(self, event: PySide6.QtScxml.QScxmlEvent) -> None:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#setScxmlEvent

        **[pure virtual] void QScxmlDataModel::setScxmlEvent(const QScxmlEvent &
        event )**

        Sets the **event** to use in the subsequent executable content
        execution.
        """
        ...
    def setScxmlProperty(self, name: str, value: Any, context: str) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#setScxmlProperty

        **[pure virtual] bool QScxmlDataModel::setScxmlProperty(const QString &
        name , const QVariant & value , const QString & context )**

        Sets a the value **value** for the property **name**.

        The **context** is a string that is used in error messages to indicate
        the location in the SCXML file where the error occurred.

        Returns `true` if successful or `false` if an error occurred.

        **See also** **scxmlProperty** ().
        """
        ...
    def setStateMachine(self, stateMachine: PySide6.QtScxml.QScxmlStateMachine) -> None:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#setStateMachine

        **void QScxmlDataModel::setStateMachine(QScxmlStateMachine *
        stateMachine )**

        Sets the state machine this model belongs to to **stateMachine**. There
        is a 1:1 relation between state machines and models. After setting the
        state machine once you cannot change it anymore. Any further attempts to
        set the state machine using this method will be ignored.

        **Note:** Setter function for property **stateMachine** .

        **See also** **stateMachine** ().
        """
        ...
    def setup(self, initialDataValues: dict[str, Any]) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#setup

        **[pure virtual invokable] bool QScxmlDataModel::setup(const QVariantMap
        & initialDataValues )**

        Initializes the data model with the initial values specified by
        **initialDataValues**.

        Returns `false` if parse errors occur or if any of the initialization
        steps fail. Returns `true` otherwise.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def stateMachine(self) -> PySide6.QtScxml.QScxmlStateMachine:
        """
        https://doc.qt.io/qt-6/qscxmldatamodel.html#stateMachine

        **QScxmlStateMachine *QScxmlDataModel::stateMachine() const**

        Returns the state machine associated with the data model.

        **Note:** Getter function for property stateMachine.

        **See also** **setStateMachine** ().
        """
        ...
    @property
    def stateMachineChanged(self) -> PySide6.QtCore.SignalInstance: ...