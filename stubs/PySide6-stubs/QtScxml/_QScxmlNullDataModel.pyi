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

class QScxmlNullDataModel(PySide6.QtScxml.QScxmlDataModel):
    """
    https://doc.qt.io/qt-6/qscxmlnulldatamodel.html

    **Detailed Description**

    This class implements the null data model as described in the **SCXML
    Specification - B.1 The Null Data Model** . Using the value `"null"` for the
    **datamodel** attribute of the `<scxml>` element means that there is no
    underlying data model, but some executable content, like `In(...)` or
    `<log>` can still be used.

    **See also** **QScxmlStateMachine**  and **QScxmlDataModel** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#QScxmlNullDataModel

        **QScxmlNullDataModel::QScxmlNullDataModel(QObject * parent = nullptr)**

        Creates a new Qt SCXML null data model, with the parent object
        **parent**.
        """
        ...
    def evaluateAssignment(self, id: int) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#evaluateAssignment

        **[override virtual] void QScxmlNullDataModel::evaluateAssignment(QScxml
        ExecutableContent::EvaluatorId id , bool * ok )**

        Reimplements: **QScxmlDataModel::evaluateAssignment**
        (QScxmlExecutableContent::EvaluatorId id, bool *ok).

        Throws an error and sets **ok** to `false`, because the null data model
        cannot evaluate assignments.
        """
        ...
    def evaluateForeach(
        self, id: int, body: PySide6.QtScxml.QScxmlDataModel.ForeachLoopBody
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#evaluateForeach

        **[override virtual] void QScxmlNullDataModel::evaluateForeach(QScxmlExe
        cutableContent::EvaluatorId id , bool * ok ,
        QScxmlDataModel::ForeachLoopBody * body )**

        Reimplements: **QScxmlDataModel::evaluateForeach**
        (QScxmlExecutableContent::EvaluatorId id, bool *ok,
        QScxmlDataModel::ForeachLoopBody *body).

        Throws an error and sets **ok** to `false`, because the null data model
        cannot evaluate `<foreach>` blocks.
        """
        ...
    def evaluateInitialization(self, id: int) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#evaluateInitialization

        **[override virtual] void QScxmlNullDataModel::evaluateInitialization(QS
        cxmlExecutableContent::EvaluatorId id , bool * ok )**

        Reimplements: **QScxmlDataModel::evaluateInitialization**
        (QScxmlExecutableContent::EvaluatorId id, bool *ok).

        Throws an error and sets **ok** to `false`, because the null data model
        cannot initialize data.
        """
        ...
    def evaluateToBool(self, id: int) -> tuple[bool, bool]:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#evaluateToBool

        **[override virtual] bool
        QScxmlNullDataModel::evaluateToBool(QScxmlExecutableContent::EvaluatorId
        id , bool * ok )**

        Reimplements: **QScxmlDataModel::evaluateToBool**
        (QScxmlExecutableContent::EvaluatorId id, bool *ok).

        Evaluates the executable content pointed to by **id** and records in
        **ok** whether there was an error. Returns the result of the evaluation
        as a boolean value. The null data model can evaluate the instruction
        `In(...)`, so this might result in an actual value, rather than an
        error.
        """
        ...
    def evaluateToString(self, id: int) -> tuple[str, bool]:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#evaluateToString

        **[override virtual] QString QScxmlNullDataModel::evaluateToString(QScxm
        lExecutableContent::EvaluatorId id , bool * ok )**

        Reimplements: **QScxmlDataModel::evaluateToString**
        (QScxmlExecutableContent::EvaluatorId id, bool *ok).

        Evaluates the executable content pointed to by **id** and records in
        **ok** whether there was an error. Returns the result of the evaluation
        as a string. The null data model can evaluate the `<log>` element, so
        this might result in an actual value, rather than an error
        """
        ...
    def evaluateToVariant(self, id: int) -> tuple[Any, bool]:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#evaluateToVariant

        **[override virtual] QVariant QScxmlNullDataModel::evaluateToVariant(QSc
        xmlExecutableContent::EvaluatorId id , bool * ok )**

        Reimplements: **QScxmlDataModel::evaluateToVariant**
        (QScxmlExecutableContent::EvaluatorId id, bool *ok).

        Evaluates the executable content pointed to by **id** and records in
        **ok** whether there was an error. As this is the null data model, any
        evaluation will in fact result in an error, with **ok** set to `false`.
        Returns an empty **QVariant** .
        """
        ...
    def evaluateToVoid(self, id: int) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#evaluateToVoid

        **[override virtual] void
        QScxmlNullDataModel::evaluateToVoid(QScxmlExecutableContent::EvaluatorId
        id , bool * ok )**

        Reimplements: **QScxmlDataModel::evaluateToVoid**
        (QScxmlExecutableContent::EvaluatorId id, bool *ok).

        Evaluates the executable content pointed to by **id** and records in
        **ok** whether there was an error. As this is the null data model, any
        evaluation will in fact result in an error, with **ok** set to `false`.
        """
        ...
    def hasScxmlProperty(self, name: str) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#hasScxmlProperty

        **[override virtual] bool QScxmlNullDataModel::hasScxmlProperty(const
        QString & name ) const**

        Reimplements: **QScxmlDataModel::hasScxmlProperty(const QString &name)
        const** .

        Returns `false`, because the null data model does not support
        properties.
        """
        ...
    def scxmlProperty(self, name: str) -> Any:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#scxmlProperty

        **[override virtual] QVariant QScxmlNullDataModel::scxmlProperty(const
        QString & name ) const**

        Reimplements: **QScxmlDataModel::scxmlProperty(const QString &name)
        const** .

        Returns an invalid variant, because the null data model does not support
        properties.

        **See also** **setScxmlProperty** ().
        """
        ...
    def setScxmlEvent(self, event: PySide6.QtScxml.QScxmlEvent) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#setScxmlEvent

        **[override virtual] void QScxmlNullDataModel::setScxmlEvent(const
        QScxmlEvent & event )**

        Reimplements: **QScxmlDataModel::setScxmlEvent** (const QScxmlEvent
        &event).

        Does not actually set the **event** , because the null data model does
        not handle events.
        """
        ...
    def setScxmlProperty(self, name: str, value: Any, context: str) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#setScxmlProperty

        **[override virtual] bool QScxmlNullDataModel::setScxmlProperty(const
        QString & name , const QVariant & value , const QString & context )**

        Reimplements: **QScxmlDataModel::setScxmlProperty** (const QString
        &name, const QVariant &value, const QString &context).

        Returns `false`, because the null data model does not support
        properties.

        **See also** **scxmlProperty** ().
        """
        ...
    def setup(self, initialDataValues: dict[str, Any]) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlnulldatamodel.html#setup

        **[override virtual invokable] bool QScxmlNullDataModel::setup(const
        QVariantMap & initialDataValues )**

        Reimplements: **QScxmlDataModel::setup** (const QVariantMap
        &initialDataValues).
        """
        ...
