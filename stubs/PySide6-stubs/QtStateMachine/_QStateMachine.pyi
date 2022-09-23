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
PySide6.QtStateMachine, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from collections.abc import Sequence
from enum import IntFlag
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtStateMachine

class QStateMachine(PySide6.QtStateMachine.QState):
    """
    https://doc.qt.io/qt-6/qstatemachine.html

    **Detailed Description**

    QStateMachine is based on the concepts and notation of **Statecharts** .
    QStateMachine is part of **Qt State Machine Framework** .

    A state machine manages a set of states (classes that inherit from
    **QAbstractState** ) and transitions (descendants of **QAbstractTransition**
    ) between those states; these states and transitions define a state graph.
    Once a state graph has been built, the state machine can execute it.
    QStateMachine's execution algorithm is based on the **State Chart XML
    (SCXML)**  algorithm. The framework's **overview**  gives several state
    graphs and the code to build them.

    Use the **addState** () function to add a top-level state to the state
    machine. States are removed with the **removeState** () function. Removing
    states while the machine is running is discouraged.

    Before the machine can be started, the **initial state**  must be set. The
    initial state is the state that the machine enters when started. You can
    then **start** () the state machine. The **started** () signal is emitted
    when the initial state is entered.

    The machine is event driven and keeps its own event loop. Events are posted
    to the machine through **postEvent** (). Note that this means that it
    executes asynchronously, and that it will not progress without a running
    event loop. You will normally not have to post events to the machine
    directly as Qt's transitions, e.g., **QEventTransition**  and its
    subclasses, handle this. But for custom transitions triggered by events,
    **postEvent** () is useful.

    The state machine processes events and takes transitions until a top-level
    final state is entered; the state machine then emits the **finished** ()
    signal. You can also **stop** () the state machine explicitly. The
    **stopped** () signal is emitted in this case.

    The following snippet shows a state machine that will finish when a button
    is clicked:

    **QPushButton**  button;

        **QStateMachine**  machine;
        **QState**
    *s1 = new **QState** ();
        s1->assignProperty(&button, "text", "Click
    me");

        **QFinalState**  *s2 = new **QFinalState** ();
    s1->addTransition(&button, &**QPushButton** ::clicked, s2);
    machine.addState(s1);
        machine.addState(s2);
    machine.setInitialState(s1);
        machine.start();

    This code example uses **QState** , which inherits **QAbstractState** . The
    **QState**  class provides a state that you can use to set properties and
    invoke methods on **QObject** s when the state is entered or exited. It also
    contains convenience functions for adding transitions, e.g.,
    **QSignalTransition** s as in this example. See the **QState**  class
    description for further details.

    If an error is encountered, the machine will look for an **error state** ,
    and if one is available, it will enter this state. The types of errors
    possible are described by the **Error**  enum. After the error state is
    entered, the type of the error can be retrieved with **error** (). The
    execution of the state graph will not stop when the error state is entered.
    If no error state applies to the erroneous state, the machine will stop
    executing and an error message will be printed to the console.

    **Note:** Important: setting the **ChildMode**  of a state machine to
    parallel (**ParallelStates** ) results in an invalid state machine. It can
    only be set to (or kept as) **ExclusiveStates** .

    **See also** **QAbstractState** , **QAbstractTransition** , **QState** , and
    **Qt State Machine Overview** .
    """

    NoError: QStateMachine.Error = ...
    NoInitialStateError: QStateMachine.Error = ...
    NoDefaultStateInHistoryStateError: QStateMachine.Error = ...
    NoCommonAncestorForTransitionError: QStateMachine.Error = ...
    StateMachineChildModeSetToParallelError: QStateMachine.Error = ...
    NormalPriority: QStateMachine.EventPriority = ...
    HighPriority: QStateMachine.EventPriority = ...

    class Error(IntFlag):
        NoError: QStateMachine.Error = ...
        NoInitialStateError: QStateMachine.Error = ...
        NoDefaultStateInHistoryStateError: QStateMachine.Error = ...
        NoCommonAncestorForTransitionError: QStateMachine.Error = ...
        StateMachineChildModeSetToParallelError: QStateMachine.Error = ...

    class EventPriority(IntFlag):
        NormalPriority: QStateMachine.EventPriority = ...
        HighPriority: QStateMachine.EventPriority = ...

    class SignalEvent(PySide6.QtCore.QEvent):
        def __init__(
            self,
            sender: PySide6.QtCore.QObject,
            signalIndex: int,
            arguments: Sequence[Any],
        ) -> None: ...
        def arguments(self) -> list[Any]: ...
        def sender(self) -> PySide6.QtCore.QObject: ...
        def signalIndex(self) -> int: ...

    class WrappedEvent(PySide6.QtCore.QEvent):
        def __init__(
            self, object: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent
        ) -> None: ...
        def event(self) -> PySide6.QtCore.QEvent: ...
        def object(self) -> PySide6.QtCore.QObject: ...

    @overload
    def __init__(
        self,
        childMode: PySide6.QtStateMachine.QState.ChildMode,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#QStateMachine

        **QStateMachine::QStateMachine(QObject * parent = nullptr)**

        Constructs a new state machine with the given **parent**.
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#QStateMachine

        **QStateMachine::QStateMachine(QObject * parent = nullptr)**

        Constructs a new state machine with the given **parent**.
        """
        ...
    def addDefaultAnimation(self, animation: PySide6.QtCore.QAbstractAnimation) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#addDefaultAnimation

        **void QStateMachine::addDefaultAnimation(QAbstractAnimation * animation
        )**

        Adds a default **animation** to be considered for any transition.
        """
        ...
    def addState(self, state: PySide6.QtStateMachine.QAbstractState) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#addState

        **void QStateMachine::addState(QAbstractState * state )**

        Adds the given **state** to this state machine. The state becomes a top-
        level state and the state machine takes ownership of the state.

        If the state is already in a different machine, it will first be removed
        from its old machine, and then added to this machine.

        **See also** **removeState** () and **setInitialState** ().
        """
        ...
    def beginMicrostep(self, event: PySide6.QtCore.QEvent) -> None: ...
    def beginSelectTransitions(self, event: PySide6.QtCore.QEvent) -> None: ...
    def cancelDelayedEvent(self, id: int) -> bool:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#cancelDelayedEvent

        **bool QStateMachine::cancelDelayedEvent(int id )**

        Cancels the delayed event identified by the given **id**. The id should
        be a value returned by a call to **postDelayedEvent** (). Returns `true`
        if the event was successfully cancelled, otherwise returns `false`.

        **Note:** This function is **thread-safe** .

        **See also** **postDelayedEvent** ().
        """
        ...
    def clearError(self) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#clearError

        **void QStateMachine::clearError()**

        Clears the error string and error code of the state machine.
        """
        ...
    def configuration(self) -> set[PySide6.QtStateMachine.QAbstractState]:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#configuration

        **QSet<QAbstractState *> QStateMachine::configuration() const**

        Returns the maximal consistent set of states (including parallel and
        final states) that this state machine is currently in. If a state `s` is
        in the configuration, it is always the case that the parent of `s` is
        also in c. Note, however, that the machine itself is not an explicit
        member of the configuration.
        """
        ...
    def defaultAnimations(self) -> list[PySide6.QtCore.QAbstractAnimation]:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#defaultAnimations

        **QList<QAbstractAnimation *> QStateMachine::defaultAnimations() const**

        Returns the list of default animations that will be considered for any
        transition.
        """
        ...
    def endMicrostep(self, event: PySide6.QtCore.QEvent) -> None: ...
    def endSelectTransitions(self, event: PySide6.QtCore.QEvent) -> None: ...
    def error(self) -> PySide6.QtStateMachine.QStateMachine.Error:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#error

        **QStateMachine::Error QStateMachine::error() const**

        Returns the error code of the last error that occurred in the state
        machine.
        """
        ...
    def errorString(self) -> str:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#errorString

        **QString QStateMachine::errorString() const**

        Returns the error string of the last error that occurred in the state
        machine.

        **Note:** Getter function for property errorString.
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#event

        **[override virtual protected] bool QStateMachine::event(QEvent * e )**

        Reimplements: **QState::event** (QEvent *e).
        """
        ...
    def eventFilter(
        self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#eventFilter

        **[override virtual] bool QStateMachine::eventFilter(QObject * watched ,
        QEvent * event )**

        Reimplements: **QObject::eventFilter** (QObject *watched, QEvent
        *event).
        """
        ...
    def globalRestorePolicy(self) -> PySide6.QtStateMachine.QState.RestorePolicy:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#globalRestorePolicy

        **QState::RestorePolicy QStateMachine::globalRestorePolicy() const**

        Returns the restore policy of the state machine.

        **Note:** Getter function for property globalRestorePolicy.

        **See also** **setGlobalRestorePolicy** ().
        """
        ...
    def isAnimated(self) -> bool:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#isAnimated

        **bool QStateMachine::isAnimated() const**

        Returns whether animations are enabled for this state machine.

        **Note:** Getter function for property **animated** .
        """
        ...
    def isRunning(self) -> bool: ...
    def onEntry(self, event: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#onEntry

        **[override virtual protected] void QStateMachine::onEntry(QEvent *
        event )**

        Reimplements: **QState::onEntry** (QEvent *event).

        This function will call **start** () to start the state machine.
        """
        ...
    def onExit(self, event: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#onExit

        **[override virtual protected] void QStateMachine::onExit(QEvent * event
        )**

        Reimplements: **QState::onExit** (QEvent *event).

        This function will call **stop** () to stop the state machine and
        subsequently emit the **stopped** () signal.
        """
        ...
    def postDelayedEvent(self, event: PySide6.QtCore.QEvent, delay: int) -> int:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#postDelayedEvent

        **int QStateMachine::postDelayedEvent(QEvent * event , int delay )**

        Posts the given **event** for processing by this state machine, with the
        given **delay** in milliseconds. Returns an identifier associated with
        the delayed event, or -1 if the event could not be posted.

        This function returns immediately. When the delay has expired, the event
        will be added to the state machine's event queue for processing. The
        state machine takes ownership of the event and deletes it once it has
        been processed.

        You can only post events when the state machine is running.

        **Note:** This function is **thread-safe** .

        **See also** **cancelDelayedEvent** () and **postEvent** ().
        """
        ...
    def postEvent(
        self,
        event: PySide6.QtCore.QEvent,
        priority: PySide6.QtStateMachine.QStateMachine.EventPriority = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#postEvent

        **void QStateMachine::postEvent(QEvent * event ,
        QStateMachine::EventPriority priority = NormalPriority)**

        Posts the given **event** of the given **priority** for processing by
        this state machine.

        This function returns immediately. The event is added to the state
        machine's event queue. Events are processed in the order posted. The
        state machine takes ownership of the event and deletes it once it has
        been processed.

        You can only post events when the state machine is running or when it is
        starting up.

        **Note:** This function is **thread-safe** .

        **See also** **postDelayedEvent** ().
        """
        ...
    def removeDefaultAnimation(
        self, animation: PySide6.QtCore.QAbstractAnimation
    ) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#removeDefaultAnimation

        **void QStateMachine::removeDefaultAnimation(QAbstractAnimation *
        animation )**

        Removes **animation** from the list of default animations.
        """
        ...
    def removeState(self, state: PySide6.QtStateMachine.QAbstractState) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#removeState

        **void QStateMachine::removeState(QAbstractState * state )**

        Removes the given **state** from this state machine. The state machine
        releases ownership of the state.

        **See also** **addState** ().
        """
        ...
    def setAnimated(self, enabled: bool) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#setAnimated

        **void QStateMachine::setAnimated(bool enabled )**

        Sets whether animations are **enabled** for this state machine.

        **Note:** Setter function for property **animated** .

        **See also** **isAnimated** ().
        """
        ...
    def setGlobalRestorePolicy(
        self, restorePolicy: PySide6.QtStateMachine.QState.RestorePolicy
    ) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#setGlobalRestorePolicy

        **void QStateMachine::setGlobalRestorePolicy(QState::RestorePolicy
        restorePolicy )**

        Sets the restore policy of the state machine to **restorePolicy**. The
        default restore policy is **QState::DontRestoreProperties** .

        **Note:** Setter function for property **globalRestorePolicy** .

        **See also** **globalRestorePolicy** ().
        """
        ...
    def setRunning(self, running: bool) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#running-prop

        **[since 5.4] running : bool**

        This property holds the running state of this state machine

        This property was introduced in Qt 5.4.

        **Access functions:**

        bool **isRunning** () const
        void **setRunning** (bool **running** )

        **Notifier signal:**

        void ****runningChanged** ** (bool **running** )

        **See also** **start** (), **stop** (), **started** (), **stopped** (),
        and **runningChanged** ().

        **Member Function Documentation**
        """
        ...
    def start(self) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#start

        **[slot] void QStateMachine::start()**

        Starts this state machine. The machine will reset its configuration and
        transition to the initial state. When a final top-level state
        (**QFinalState** ) is entered, the machine will emit the **finished** ()
        signal.

        **Note:** A state machine will not run without a running event loop,
        such as the main application event loop started with
        **QCoreApplication::exec** () or **QApplication::exec** ().

        **See also** **started** (), **finished** (), **stop** (),
        **initialState** (), and **setRunning** ().
        """
        ...
    def stop(self) -> None:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#stop

        **[slot] void QStateMachine::stop()**

        Stops this state machine. The state machine will stop processing events
        and then emit the **stopped** () signal.

        **See also** **stopped** (), **start** (), and **setRunning** ().
        """
        ...
    @property
    def runningChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#runningChanged

        **[signal, since 5.4] void QStateMachine::runningChanged(bool running
        )**

        This signal is emitted when the running property is changed with
        **running** as argument.

        **Note:** Notifier signal for property **running** .

        This function was introduced in Qt 5.4.

        **See also** **QStateMachine::running** .
        """
        ...
    @property
    def started(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#started

        **[private signal] void QStateMachine::started()**

        This signal is emitted when the state machine has entered its initial
        state (QStateMachine::initialState).

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.

        **See also** **QStateMachine::finished** () and **QStateMachine::start**
        ().
        """
        ...
    @property
    def stopped(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qstatemachine.html#stopped

        **[private signal] void QStateMachine::stopped()**

        This signal is emitted when the state machine has stopped.

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.

        **See also** **QStateMachine::stop** () and **QStateMachine::finished**
        ().
        """
        ...
