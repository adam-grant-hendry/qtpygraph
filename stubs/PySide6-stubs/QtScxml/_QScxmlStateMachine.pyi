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

from typing import Any, overload

import PySide6.QtCore
import PySide6.QtScxml

class QScxmlStateMachine(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qscxmlstatemachine.html

    **Detailed Description**

    QScxmlStateMachine is an implementation of the **State Chart XML (SCXML)** .

    All states that are defined in the SCXML file are accessible as properties
    of QScxmlStateMachine. These properties are boolean values and indicate
    whether the state is active or inactive.

    **Note:** The QScxmlStateMachine needs a **QEventLoop**  to work correctly.
    The event loop is used to implement the `delay` attribute for events and to
    schedule the processing of a state machine when events are received from
    nested (or parent) state machines.
    """

    def __init__(
        self,
        metaObject: PySide6.QtCore.QMetaObject,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None: ...
    def activeStateNames(self, compress: bool = ...) -> list[str]:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#activeStateNames

        **[invokable] QStringList QScxmlStateMachine::activeStateNames(bool
        compress = true) const**

        Retrieves a list of state names of all active states.

        When a state is active, all its parent states are active by definition.
        When **compress** is `true` (the default), the parent states will be
        filtered out and only the **leaf states** will be returned. When it is
        `false`, the full list of active states will be returned.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def cancelDelayedEvent(self, sendId: str) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#cancelDelayedEvent

        **[invokable] void QScxmlStateMachine::cancelDelayedEvent(const QString
        & sendId )**

        Cancels a delayed event with the specified **sendId**.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def connectToEvent(
        self,
        scxmlEventSpec: str,
        receiver: PySide6.QtCore.QObject,
        method: bytes,
        type: PySide6.QtCore.Qt.ConnectionType = ...,
    ) -> PySide6.QtCore.QMetaObject.Connection:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#connectToEvent

        **QMetaObject::Connection QScxmlStateMachine::connectToEvent(const
        QString & scxmlEventSpec , const QObject * receiver , const char *
        method , Qt::ConnectionType type = Qt::AutoConnection)**

        Creates a connection of the specified **type** from the event specified
        by **scxmlEventSpec** to the **method** in the **receiver** object. The
        receiver's **method** may take a **QScxmlEvent**  as a parameter. For
        example:

        void mySlot(const **QScxmlEvent**  &event);

        In contrast to event specifications in SCXML documents, spaces are not
        allowed in the **scxmlEventSpec** here. In order to connect to multiple
        events with different prefixes, connectToEvent() has to be called
        multiple times.

        Returns a handle to the connection, which can be used later to
        disconnect.
        """
        ...
    def connectToState(
        self,
        scxmlStateName: str,
        receiver: PySide6.QtCore.QObject,
        method: bytes,
        type: PySide6.QtCore.Qt.ConnectionType = ...,
    ) -> PySide6.QtCore.QMetaObject.Connection:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#connectToState

        **QMetaObject::Connection QScxmlStateMachine::connectToState(const
        QString & scxmlStateName , const QObject * receiver , const char *
        method , Qt::ConnectionType type = Qt::AutoConnection)**

        Creates a connection of the given **type** from the state identified by
        **scxmlStateName** to the **method** in the **receiver** object. The
        receiver's **method** may take a boolean argument that indicates whether
        the state connected became active or inactive. For example:

        void mySlot(bool active);

        Returns a handle to the connection, which can be used later to
        disconnect.
        """
        ...
    def dataModel(self) -> PySide6.QtScxml.QScxmlDataModel:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#dataModel

        **QScxmlDataModel *QScxmlStateMachine::dataModel() const**

        Returns the data model used by the state machine.

        **Note:** Getter function for property dataModel.

        **See also** **setDataModel** ().
        """
        ...
    @staticmethod
    def fromData(
        data: PySide6.QtCore.QIODevice, fileName: str = ...
    ) -> PySide6.QtScxml.QScxmlStateMachine:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#fromData

        **[static] QScxmlStateMachine *QScxmlStateMachine::fromData(QIODevice *
        data , const QString & fileName = QString())**

        Creates a state machine by reading from the **QIODevice**  specified by
        **data**.

        This method will always return a state machine. If errors occur while
        reading the SCXML file, **fileName** , the state machine cannot be
        started. The errors can be retrieved by calling the **parseErrors** ()
        method.

        **See also** **parseErrors** ().
        """
        ...
    @staticmethod
    def fromFile(fileName: str) -> PySide6.QtScxml.QScxmlStateMachine:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#fromFile

        **[static] QScxmlStateMachine *QScxmlStateMachine::fromFile(const
        QString & fileName )**

        Creates a state machine from the SCXML file specified by **fileName**.

        This method will always return a state machine. If errors occur while
        reading the SCXML file, the state machine cannot be started. The errors
        can be retrieved by calling the **parseErrors** () method.

        **See also** **parseErrors** ().
        """
        ...
    def init(self) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#init

        **[slot] bool QScxmlStateMachine::init()**

        Initializes the state machine.

        State machine initialization consists of calling
        **QScxmlDataModel::setup** (), setting the initial values for `<data>`
        elements, and executing any `<script>` tags of the `<scxml>` tag. The
        initial data values are taken from the `initialValues` property.

        Returns `false` if parse errors occur or if any of the initialization
        steps fail. Returns `true` otherwise.
        """
        ...
    def initialValues(self) -> dict[str, Any]:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#initialValues-prop

        **[bindable] initialValues : QVariantMap**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the initial values to be used for setting up the
        data model.

        **See also** **QScxmlStateMachine::init** () and **QScxmlDataModel** .
        """
        ...
    def invokedServices(self) -> list[PySide6.QtScxml.QScxmlInvokableService]:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#invokedServices-prop

        **[bindable read-only] invokedServices :
        QList<QScxmlInvokableService*>**

        **Note:** This property supports **QProperty**  bindings.

        This property holds a list of SCXML services that were invoked from the
        main state machine (possibly recursively).
        """
        ...
    @overload
    def isActive(self, scxmlStateName: str) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#isActive

        **[invokable] bool QScxmlStateMachine::isActive(const QString &
        scxmlStateName ) const**

        Returns `true` if the state specified by **scxmlStateName** is active,
        `false` otherwise.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    @overload
    def isActive(self, stateIndex: int) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#isActive-1

        **[protected] bool QScxmlStateMachine::isActive(int stateIndex ) const**

        Returns `true` if the state with the ID **stateIndex** is active.

        This method is part of the interface to the compiled representation of
        SCXML state machines. It should only be used internally and by state
        machines compiled from SCXML documents.
        """
        ...
    def isDispatchableTarget(self, target: str) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#isDispatchableTarget

        **[invokable] bool QScxmlStateMachine::isDispatchableTarget(const
        QString & target ) const**

        Returns `true` if a message to **target** can be dispatched by this
        state machine.

        Valid targets are:

        * `#_parent` for the parent state machine if the current state machine
        is started by `<invoke>`
          * `#_internal` for the current state machine
        * `#_scxml_sessionid`, where `sessionid` is the session ID of the
        current state machine
          * `#_servicename`, where `servicename` is the ID
        or name of a service started with `<invoke>` by this state machine

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def isInitialized(self) -> bool: ...
    def isInvoked(self) -> bool: ...
    def isRunning(self) -> bool:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#isRunning

        **bool QScxmlStateMachine::isRunning() const**

        Returns `true` if the state machine is running, `false` otherwise.

        **Note:** Getter function for property **running** .

        **See also** **setRunning** () and **runningChanged** ().
        """
        ...
    def loader(self) -> PySide6.QtScxml.QScxmlCompiler.Loader:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#loader-prop

        **[bindable] loader : QScxmlCompiler::Loader***

        **Note:** This property supports **QProperty**  bindings.

        This property holds the loader that is currently used to resolve and
        load URIs for the state machine.
        """
        ...
    def name(self) -> str:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#name-prop

        **[read-only] name : const QString**

        This property holds the name of the state machine as set by the **name**
        attribute of the `<scxml>` tag.

        **Access functions:**

        QString **name** () const
        """
        ...
    def parseErrors(self) -> list[PySide6.QtScxml.QScxmlError]:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#parseErrors-prop

        **[read-only] parseErrors : const QList<QScxmlError>**

        This property holds the list of parse errors that occurred while
        creating a state machine from an SCXML file.

        **Access functions:**

        QList<QScxmlError> **parseErrors** () const
        """
        ...
    def sessionId(self) -> str:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#sessionId-prop

        **[read-only] sessionId : const QString**

        This property holds the session ID of the current state machine.

        The session ID is used for message routing between parent and child
        state machines. If a state machine is started by an `<invoke>` element,
        any event it sends will have the `invokeid` field set to the session ID.
        The state machine will use the origin of an event (which is set by the
        **target** or **targetexpr** attribute in a `<send>` element) to
        dispatch messages to the correct child state machine.

        **Access functions:**

        QString **sessionId** () const

        **See also** **QScxmlEvent::invokeId** ().
        """
        ...
    def setDataModel(self, model: PySide6.QtScxml.QScxmlDataModel) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#setDataModel

        **void QScxmlStateMachine::setDataModel(QScxmlDataModel * model )**

        Sets the data model for this state machine to **model**. There is a 1:1
        relation between state machines and models. After setting the model once
        you cannot change it anymore. Any further attempts to set the model
        using this method will be ignored.

        **Note:** Setter function for property **dataModel** .

        **See also** **dataModel** ().
        """
        ...
    def setInitialValues(self, initialValues: dict[str, Any]) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#initialValues-prop

        **[bindable] initialValues : QVariantMap**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the initial values to be used for setting up the
        data model.

        **See also** **QScxmlStateMachine::init** () and **QScxmlDataModel** .
        """
        ...
    def setLoader(self, loader: PySide6.QtScxml.QScxmlCompiler.Loader) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#loader-prop

        **[bindable] loader : QScxmlCompiler::Loader***

        **Note:** This property supports **QProperty**  bindings.

        This property holds the loader that is currently used to resolve and
        load URIs for the state machine.
        """
        ...
    def setRunning(self, running: bool) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#setRunning

        **void QScxmlStateMachine::setRunning(bool running )**

        Starts the state machine if **running** is `true`, or stops it
        otherwise.

        **Note:** Setter function for property **running** .

        **See also** **start** (), **stop** (), **isRunning** (), and
        **runningChanged** ().
        """
        ...
    def setTableData(self, tableData: PySide6.QtScxml.QScxmlTableData) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#tableData-prop

        **[bindable] tableData : QScxmlTableData***

        **Note:** This property supports **QProperty**  bindings.

        This property holds the table data that is used when generating C++ from
        an SCXML file.

        The class implementing the state machine will use this property to
        assign the generated table data. The state machine does not assume
        ownership of the table data.

        **Member Function Documentation**
        """
        ...
    def start(self) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#start

        **[slot] void QScxmlStateMachine::start()**

        Starts this state machine. The machine will reset its configuration and
        transition to the initial state. When a final top-level state is
        entered, the machine will emit the **finished** () signal.

        **Note:** A state machine will not run without a running event loop,
        such as the main application event loop started with
        **QCoreApplication::exec** () or **QApplication::exec** ().

        **See also** **runningChanged** (), **setRunning** (), **stop** (), and
        **finished** ().
        """
        ...
    def stateNames(self, compress: bool = ...) -> list[str]:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#stateNames

        **[invokable] QStringList QScxmlStateMachine::stateNames(bool compress =
        true) const**

        Retrieves a list of state names of all states.

        When **compress** is `true` (the default), the states that contain child
        states will be filtered out and only the **leaf states** will be
        returned. When it is `false`, the full list of all states will be
        returned.

        The returned list does not contain the states of possible nested state
        machines.

        **Note:** The order of the state names in the list is the order in which
        the states occurred in the SCXML document.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def stop(self) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#stop

        **[slot] void QScxmlStateMachine::stop()**

        Stops this state machine. The machine will not execute any further state
        transitions. Its `running` property is set to `false`.

        **See also** **runningChanged** (), **start** (), and **setRunning** ().
        """
        ...
    @overload
    def submitEvent(self, event: PySide6.QtScxml.QScxmlEvent) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#submitEvent

        **[invokable] void QScxmlStateMachine::submitEvent(QScxmlEvent * event
        )**

        Submits the SCXML event **event** to the internal or external event
        queue depending on the priority of the event.

        When a delay is set, the event will be queued for delivery after the
        timeout has passed. The state machine takes ownership of **event** and
        deletes it after processing.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    @overload
    def submitEvent(self, eventName: str) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#submitEvent-1

        **[invokable] void QScxmlStateMachine::submitEvent(const QString &
        eventName )**

        A utility method to create and submit an external event with the
        specified **eventName** as the name.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    @overload
    def submitEvent(self, eventName: str, data: Any) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#submitEvent-2

        **[invokable] void QScxmlStateMachine::submitEvent(const QString &
        eventName , const QVariant & data )**

        A utility method to create and submit an external event with the
        specified **eventName** as the name and **data** as the payload data.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def tableData(self) -> PySide6.QtScxml.QScxmlTableData:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#tableData-prop

        **[bindable] tableData : QScxmlTableData***

        **Note:** This property supports **QProperty**  bindings.

        This property holds the table data that is used when generating C++ from
        an SCXML file.

        The class implementing the state machine will use this property to
        assign the generated table data. The state machine does not assume
        ownership of the table data.

        **Member Function Documentation**
        """
        ...
    @property
    def dataModelChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def finished(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#finished

        **[signal] void QScxmlStateMachine::finished()**

        This signal is emitted when the state machine reaches a top-level final
        state.

        **See also** **running** .
        """
        ...
    @property
    def initialValuesChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def initializedChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def invokedServicesChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def loaderChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def log(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#log

        **[signal] void QScxmlStateMachine::log(const QString & label , const
        QString & msg )**

        This signal is emitted if a `<log>` tag is used in the SCXML. **label**
        is the value of the **label** attribute of the `<log>` tag. **msg** is
        the value of the evaluated **expr** attribute of the `<log>` tag. If
        there is no **expr** attribute, a null string will be returned.
        """
        ...
    @property
    def reachedStableState(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#reachedStableState

        **[signal] void QScxmlStateMachine::reachedStableState()**

        This signal is emitted when the event queue is empty at the end of a
        macro step or when a final state is reached.
        """
        ...
    @property
    def runningChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qscxmlstatemachine.html#runningChanged

        **[signal] void QScxmlStateMachine::runningChanged(bool running )**

        This signal is emitted when the `running` property is changed with
        **running** as argument.

        **Note:** Notifier signal for property **running** .
        """
        ...
    @property
    def tableDataChanged(self) -> PySide6.QtCore.SignalInstance: ...
