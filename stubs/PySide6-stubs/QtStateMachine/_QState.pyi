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

from enum import IntFlag
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtStateMachine

class QState(PySide6.QtStateMachine.QAbstractState):
    """
    https://doc.qt.io/qt-6/qstate.html

    **Detailed Description**

    QState objects can have child states, and can have transitions to other
    states. QState is part of **Qt State Machine Framework** .

    The **addTransition** () function adds a transition. The
    **removeTransition** () function removes a transition. The **transitions**
    () function returns the state's outgoing transitions.

    The **assignProperty** () function is used for defining property assignments
    that should be performed when a state is entered.

    Top-level states must be passed a **QStateMachine**  object as their parent
    state, or added to a state machine using **QStateMachine::addState** ().

    **States with Child States**

    The **childMode**  property determines how child states are treated. For
    non-parallel state groups, the **setInitialState** () function must be
    called to set the initial state. The child states are mutually exclusive
    states, and the state machine needs to know which child state to enter when
    the parent state is the target of a transition.

    The state emits the **QState::finished** () signal when a final child state
    (**QFinalState** ) is entered.

    The **setErrorState** () sets the state's error state. The error state is
    the state that the state machine will transition to if an error is detected
    when attempting to enter the state (e.g. because no initial state has been
    set).
    """

    ExclusiveStates: QState.ChildMode = ...
    ParallelStates: QState.ChildMode = ...
    DontRestoreProperties: QState.RestorePolicy = ...
    RestoreProperties: QState.RestorePolicy = ...

    class ChildMode(IntFlag):
        ExclusiveStates: QState.ChildMode = ...
        ParallelStates: QState.ChildMode = ...

    class RestorePolicy(IntFlag):
        DontRestoreProperties: QState.RestorePolicy = ...
        RestoreProperties: QState.RestorePolicy = ...
    @overload
    def __init__(
        self,
        childMode: PySide6.QtStateMachine.QState.ChildMode,
        parent: PySide6.QtStateMachine.QState | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qstate.html#QState

        **QState::QState(QState * parent = nullptr)**

        Constructs a new state with the given **parent** state.
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtStateMachine.QState | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qstate.html#QState-1

        **QState::QState(QState::ChildMode childMode , QState * parent =
        nullptr)**

        Constructs a new state with the given **childMode** and the given
        **parent** state.
        """
        ...
    @overload
    def addTransition(
        self, arg__1: object, arg__2: PySide6.QtStateMachine.QAbstractState
    ) -> PySide6.QtStateMachine.QSignalTransition:
        """
        https://doc.qt.io/qt-6/qstate.html#addTransition

        **void QState::addTransition(QAbstractTransition * transition )**

        Adds the given **transition**. The transition has this state as the
        source. This state takes ownership of the transition.
        """
        ...
    @overload
    def addTransition(
        self,
        sender: PySide6.QtCore.QObject,
        signal: bytes,
        target: PySide6.QtStateMachine.QAbstractState,
    ) -> PySide6.QtStateMachine.QSignalTransition:
        """
        https://doc.qt.io/qt-6/qstate.html#addTransition-1

        **QSignalTransition *QState::addTransition(const QObject * sender ,
        const char * signal , QAbstractState * target )**

        Adds a transition associated with the given **signal** of the given
        **sender** object, and returns the new **QSignalTransition**  object.
        The transition has this state as the source, and the given **target** as
        the target state.
        """
        ...
    @overload
    def addTransition(
        self, target: PySide6.QtStateMachine.QAbstractState
    ) -> PySide6.QtStateMachine.QAbstractTransition:
        """
        https://doc.qt.io/qt-6/qstate.html#addTransition-2

        **[since 5.5] template <typename PointerToMemberFunction>
        QSignalTransition *QState::addTransition(const QObject * sender ,
        PointerToMemberFunction signal , QAbstractState * target )**

        This is an overloaded function.

        Adds a transition associated with the given **signal** of the given
        **sender** object, and returns the new **QSignalTransition**  object.
        The transition has this state as the source, and the given **target** as
        the target state.

        This function was introduced in Qt 5.5.
        """
        ...
    @overload
    def addTransition(
        self, transition: PySide6.QtStateMachine.QAbstractTransition
    ) -> None:
        """
        https://doc.qt.io/qt-6/qstate.html#addTransition-3

        **QAbstractTransition *QState::addTransition(QAbstractState * target )**

        Adds an unconditional transition from this state to the given **target**
        state, and returns then new transition object.
        """
        ...
    def assignProperty(
        self, object: PySide6.QtCore.QObject, name: bytes, value: Any
    ) -> None:
        """
        https://doc.qt.io/qt-6/qstate.html#assignProperty

        **void QState::assignProperty(QObject * object , const char * name ,
        const QVariant & value )**

        Instructs this state to set the property with the given **name** of the
        given **object** to the given **value** when the state is entered.

        **See also** **propertiesAssigned** ().
        """
        ...
    def childMode(self) -> PySide6.QtStateMachine.QState.ChildMode:
        """
        https://doc.qt.io/qt-6/qstate.html#childMode

        **QState::ChildMode QState::childMode() const**

        Returns the child mode of this state.

        **Note:** Getter function for property childMode.

        **See also** **setChildMode** ().
        """
        ...
    def errorState(self) -> PySide6.QtStateMachine.QAbstractState:
        """
        https://doc.qt.io/qt-6/qstate.html#errorState

        **QAbstractState *QState::errorState() const**

        Returns this state's error state.

        **Note:** Getter function for property errorState.

        **See also** **setErrorState** () and **QStateMachine::error** ().
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qstate.html#event

        **[override virtual protected] bool QState::event(QEvent * e )**

        Reimplements: **QAbstractState::event** (QEvent *e).
        """
        ...
    def initialState(self) -> PySide6.QtStateMachine.QAbstractState:
        """
        https://doc.qt.io/qt-6/qstate.html#initialState

        **QAbstractState *QState::initialState() const**

        Returns this state's initial state, or `nullptr` if the state has no
        initial state.

        **Note:** Getter function for property initialState.

        **See also** **setInitialState** ().
        """
        ...
    def onEntry(self, event: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qstate.html#onEntry

        **[override virtual protected] void QState::onEntry(QEvent * event )**

        Reimplements: **QAbstractState::onEntry** (QEvent *event).
        """
        ...
    def onExit(self, event: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qstate.html#onExit

        **[override virtual protected] void QState::onExit(QEvent * event )**

        Reimplements: **QAbstractState::onExit** (QEvent *event).
        """
        ...
    def removeTransition(
        self, transition: PySide6.QtStateMachine.QAbstractTransition
    ) -> None:
        """
        https://doc.qt.io/qt-6/qstate.html#removeTransition

        **void QState::removeTransition(QAbstractTransition * transition )**

        Removes the given **transition** from this state. The state releases
        ownership of the transition.

        **See also** **addTransition** ().
        """
        ...
    def setChildMode(self, mode: PySide6.QtStateMachine.QState.ChildMode) -> None:
        """
        https://doc.qt.io/qt-6/qstate.html#setChildMode

        **void QState::setChildMode(QState::ChildMode mode )**

        Sets the child **mode** of this state.

        **Note:** Setter function for property **childMode** .

        **See also** **childMode** ().
        """
        ...
    def setErrorState(self, state: PySide6.QtStateMachine.QAbstractState) -> None:
        """
        https://doc.qt.io/qt-6/qstate.html#setErrorState

        **void QState::setErrorState(QAbstractState * state )**

        Sets this state's error state to be the given **state**. If the error
        state is not set, or if it is set to `nullptr`, the state will inherit
        its parent's error state recursively. If no error state is set for the
        state itself or any of its ancestors, an error will cause the machine to
        stop executing and an error will be printed to the console.

        **Note:** Setter function for property **errorState** .

        **See also** **errorState** ().
        """
        ...
    def setInitialState(self, state: PySide6.QtStateMachine.QAbstractState) -> None:
        """
        https://doc.qt.io/qt-6/qstate.html#setInitialState

        **void QState::setInitialState(QAbstractState * state )**

        Sets this state's initial state to be the given **state**. **state** has
        to be a child of this state.

        **Note:** Setter function for property **initialState** .

        **See also** **initialState** ().
        """
        ...
    def transitions(self) -> list[PySide6.QtStateMachine.QAbstractTransition]:
        """
        https://doc.qt.io/qt-6/qstate.html#transitions

        **QList<QAbstractTransition *> QState::transitions() const**

        Returns this state's outgoing transitions (i.e. transitions where this
        state is the **source state** ), or an empty list if this state has no
        outgoing transitions.

        **See also** **addTransition** ().
        """
        ...
    @property
    def childModeChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qstate.html#childModeChanged

        **[private signal, since 5.4] void QState::childModeChanged()**

        This signal is emitted when the **childMode**  property is changed.

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.

        **Note:** Notifier signal for property **childMode** .

        This function was introduced in Qt 5.4.

        **See also** **QState::childMode** .
        """
        ...
    @property
    def errorStateChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qstate.html#errorStateChanged

        **[private signal, since 5.4] void QState::errorStateChanged()**

        This signal is emitted when the **errorState**  property is changed.

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.

        **Note:** Notifier signal for property **errorState** .

        This function was introduced in Qt 5.4.

        **See also** **QState::errorState** .
        """
        ...
    @property
    def finished(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qstate.html#finished

        **[private signal] void QState::finished()**

        This signal is emitted when a final child state of this state is
        entered.

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.

        **See also** **QFinalState** .
        """
        ...
    @property
    def initialStateChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qstate.html#initialStateChanged

        **[private signal, since 5.4] void QState::initialStateChanged()**

        This signal is emitted when the **initialState**  property is changed.

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.

        **Note:** Notifier signal for property **initialState** .

        This function was introduced in Qt 5.4.

        **See also** **QState::initialState** .
        """
        ...
    @property
    def propertiesAssigned(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qstate.html#propertiesAssigned

        **[private signal] void QState::propertiesAssigned()**

        This signal is emitted when all properties have been assigned their
        final value. If the state assigns a value to one or more properties for
        which an animation exists (either set on the transition or as a default
        animation on the state machine), then the signal will not be emitted
        until all such animations have finished playing.

        If there are no relevant animations, or no property assignments defined
        for the state, then the signal will be emitted immediately before the
        state is entered.

        **See also**  **QState::assignProperty** () and
        **QAbstractTransition::addAnimation** ()

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.
        """
        ...
