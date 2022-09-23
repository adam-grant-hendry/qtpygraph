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

class QScxmlCppDataModel(PySide6.QtScxml.QScxmlDataModel):
    """
    https://doc.qt.io/qt-6/qscxmlcppdatamodel.html

    **Detailed Description**

    The C++ data model for SCXML lets you write C++ code for **expr** attributes
    and `<script>` elements. The **data part** of the data model is backed by a
    subclass of QScxmlCppDataModel, for which the Qt SCXML compiler (`qscxmlc`)
    will generate the dispatch methods. It cannot be used when loading an SCXML
    file at runtime.

    Usage is through the **datamodel** attribute of the `<scxml>` element:

    <scxml datamodel="cplusplus:TheDataModel:thedatamodel.h"  ....>

    The format of the **datamodel** attribute is: `cplusplus:<class-
    name>:<classdef-header>`. So, for the example above, there should be a file
    **thedatamodel.h** containing a subclass of QScxmlCppDataModel, containing
    at least the following:

    #include "qscxmlcppdatamodel.h"

        class TheDataModel: public
    QScxmlCppDataModel
        {
            \\Q_OBJECT
            Q_SCXML_DATAMODEL
        };

    The Q_SCXML_DATAMODEL has to appear in the private section of the class
    definition, for example right after the opening bracket, or after a
    **Q_OBJECT**  macro. This macro expands to the declaration of some virtual
    methods whose implementation is generated by the Qt SCXML compiler.

    The Qt SCXML compiler will generate the various `evaluateTo` methods, and
    convert expressions and scripts into lambdas inside those methods. For
    example:

    <scxml datamodel="cplusplus:TheDataModel:thedatamodel.h"
    xmlns="http://www.w3.org/2005/07/scxml" version="1.0"
    name="MediaPlayerStateMachine">
            <state id="stopped">
    <transition event="tap" cond="isValidMedia()" target="playing"/>
    </state>

            <state id="playing">
                <onentry>
    <script>
                        media = eventData().value(**QStringLiteral**
    (&quot;media&quot;)).toString();
                    </script>
    <send event="playbackStarted">
                        <param name="media"
    expr="media"/>
                    </send>
                </onentry>
    </state>
        </scxml>

    This will result in:

    bool TheDataModel::evaluateToBool(QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
            // ....
                return [this]()->bool{ return
    isValidMedia(); }();
            // ....
        }

        **QVariant**
    TheDataModel::evaluateToVariant(QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
            // ....
                return [this]()->**QVariant** {
    return media; }();
            // ....
        }

        void
    TheDataModel::evaluateToVoid(QScxmlExecutableContent::EvaluatorId id, bool
    *ok) {
            // ....
                [this]()->void{ media =
    eventData().value(**QStringLiteral** ("media")).toString(); }();
            //
    ....
        }

    So, you are not limited to call functions. In a `<script>` element you can
    put zero or more C++ statements, and in **cond** or **expr** attributes you
    can use any C++ expression that can be converted to the respective bool or
    **QVariant** . And, as the `this` pointer is also captured, you can call or
    access the data model (the **media** attribute in the example above). For
    the full example, see **Qt SCXML: Media Player QML Example (C++ Data
    Model)** .

    **See also** **QScxmlStateMachine**  and **QScxmlDataModel** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#QScxmlCppDataModel

        **QScxmlCppDataModel::QScxmlCppDataModel(QObject * parent = nullptr)**

        Creates a new C++ data model with the parent object **parent**.
        """
        ...
    def evaluateAssignment(self, id: int) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#evaluateAssignment

        **[override virtual] void QScxmlCppDataModel::evaluateAssignment(QScxmlE
        xecutableContent::EvaluatorId id , bool * ok )**

        Reimplements: **QScxmlDataModel::evaluateAssignment**
        (QScxmlExecutableContent::EvaluatorId id, bool *ok).

        This method does not perform any action, ignores **id** , and sets
        **ok** to `false`. Override it in your specific data model in order to
        implement `<assign>`.
        """
        ...
    def evaluateForeach(
        self, id: int, body: PySide6.QtScxml.QScxmlDataModel.ForeachLoopBody
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#evaluateForeach

        **[override virtual] void
        QScxmlCppDataModel::evaluateForeach(QScxmlExecutableContent::EvaluatorId
        id , bool * ok , QScxmlDataModel::ForeachLoopBody * body )**

        Reimplements: **QScxmlDataModel::evaluateForeach**
        (QScxmlExecutableContent::EvaluatorId id, bool *ok,
        QScxmlDataModel::ForeachLoopBody *body).

        This method does not perform any action, ignores **id** and **body** ,
        and sets **ok** to `false`. Override it in your specific data model in
        order to implement `<foreach>`.
        """
        ...
    def evaluateInitialization(self, id: int) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#evaluateInitialization

        **[override virtual] void QScxmlCppDataModel::evaluateInitialization(QSc
        xmlExecutableContent::EvaluatorId id , bool * ok )**

        Reimplements: **QScxmlDataModel::evaluateInitialization**
        (QScxmlExecutableContent::EvaluatorId id, bool *ok).

        This method does not perform any action, ignores **id** , and sets
        **ok** to `false`. Override it in your specific data model in order to
        implement `<data>`.
        """
        ...
    def hasScxmlProperty(self, name: str) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#hasScxmlProperty

        **[override virtual] bool QScxmlCppDataModel::hasScxmlProperty(const
        QString & name ) const**

        Reimplements: **QScxmlDataModel::hasScxmlProperty(const QString &name)
        const** .

        This method always returns `false` and ignores **name**. Override it to
        implement the lookup of data model properties via the `location`
        attribute of various elements.
        """
        ...
    def inState(self, stateName: str) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#inState

        **bool QScxmlCppDataModel::inState(const QString & stateName ) const**

        Returns `true` if the state machine is in the state specified by
        **stateName** , `false` otherwise.
        """
        ...
    def scxmlEvent(self) -> PySide6.QtScxml.QScxmlEvent:
        """
        https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#scxmlEvent

        **const QScxmlEvent &QScxmlCppDataModel::scxmlEvent() const**

        Holds the current event that is being processed by the state machine.

        See also **SCXML Specification - 5.10 System Variables**  for the
        description of the `_event` variable.

        Returns the event currently being processed.

        **See also** **setScxmlEvent** ().
        """
        ...
    def scxmlProperty(self, name: str) -> Any:
        """
        https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#scxmlProperty

        **[override virtual] QVariant QScxmlCppDataModel::scxmlProperty(const
        QString & name ) const**

        Reimplements: **QScxmlDataModel::scxmlProperty(const QString &name)
        const** .

        This method always returns an empty **QVariant**  and ignores **name**.
        Override it to implement the lookup of data model properties via the
        `location` attribute of various elements.

        **See also** **setScxmlProperty** ().
        """
        ...
    def setScxmlEvent(self, scxmlEvent: PySide6.QtScxml.QScxmlEvent) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#setScxmlEvent

        **[override virtual] void QScxmlCppDataModel::setScxmlEvent(const
        QScxmlEvent & event )**

        Reimplements: **QScxmlDataModel::setScxmlEvent** (const QScxmlEvent
        &event).

        Sets the **event** that will be processed next.

        **See also** **QScxmlCppDataModel::scxmlEvent** .
        """
        ...
    def setScxmlProperty(self, name: str, value: Any, context: str) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#setScxmlProperty

        **[override virtual] bool QScxmlCppDataModel::setScxmlProperty(const
        QString & name , const QVariant & value , const QString & context )**

        Reimplements: **QScxmlDataModel::setScxmlProperty** (const QString
        &name, const QVariant &value, const QString &context).

        This method always returns `false` and ignores **name** , **value** ,
        and **context**. Override it to implement the lookup of data model
        properties via the `location` attribute of various elements.

        **See also** **scxmlProperty** ().
        """
        ...
    def setup(self, initialDataValues: dict[str, Any]) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlcppdatamodel.html#setup

        **[override virtual invokable] bool QScxmlCppDataModel::setup(const
        QVariantMap & initialDataValues )**

        Reimplements: **QScxmlDataModel::setup** (const QVariantMap
        &initialDataValues).

        Called during state machine initialization to set up a state machine
        using the initial values for data model variables specified by their
        keys, **initialDataValues**. These are the values specified by `<param>`
        tags in an `<invoke>` element.

        Returns `true` on success.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        **See also** **QScxmlStateMachine::init** .
        """
        ...
