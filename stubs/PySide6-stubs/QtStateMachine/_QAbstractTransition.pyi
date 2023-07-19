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

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtStateMachine

class QAbstractTransition(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qabstracttransition.html

    **Detailed Description**

    The QAbstractTransition class is the abstract base class of transitions
    between states (**QAbstractState**  objects) of a **QStateMachine** .
    QAbstractTransition is part of **Qt State Machine Framework** .

    The **sourceState** () function returns the source of the transition. The
    **targetStates** () function returns the targets of the transition. The
    **machine** () function returns the state machine that the transition is
    part of.

    The **triggered** () signal is emitted when the transition has been
    triggered.

    Transitions can cause animations to be played. Use the **addAnimation** ()
    function to add an animation to the transition.

    **Subclassing**

    The **eventTest** () function is called by the state machine to determine
    whether an event should trigger the transition. In your reimplementation you
    typically check the event type and cast the event object to the proper type,
    and check that one or more properties of the event meet your criteria.

    The **onTransition** () function is called when the transition is triggered;
    reimplement this function to perform custom processing for the transition.
    """

    ExternalTransition: QAbstractTransition.TransitionType = ...
    InternalTransition: QAbstractTransition.TransitionType = ...

    class TransitionType(IntFlag):
        ExternalTransition: QAbstractTransition.TransitionType = ...
        InternalTransition: QAbstractTransition.TransitionType = ...
    def __init__(self, sourceState: PySide6.QtStateMachine.QState | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#QAbstractTransition

        **QAbstractTransition::QAbstractTransition(QState * sourceState =
        nullptr)**

        Constructs a new QAbstractTransition object with the given
        **sourceState**.
        """
        ...
    def addAnimation(self, animation: PySide6.QtCore.QAbstractAnimation) -> None:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#addAnimation

        **void QAbstractTransition::addAnimation(QAbstractAnimation * animation
        )**

        Adds the given **animation** to this transition. The transition does not
        take ownership of the animation.

        **See also** **removeAnimation** () and **animations** ().
        """
        ...
    def animations(self) -> list[PySide6.QtCore.QAbstractAnimation]:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#animations

        **QList<QAbstractAnimation *> QAbstractTransition::animations() const**

        Returns the list of animations associated with this transition, or an
        empty list if it has no animations.

        **See also** **addAnimation** ().
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#event

        **[override virtual protected] bool QAbstractTransition::event(QEvent *
        e )**

        Reimplements: **QObject::event** (QEvent *e).
        """
        ...
    def eventTest(self, event: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#eventTest

        **[pure virtual protected] bool QAbstractTransition::eventTest(QEvent *
        event )**

        This function is called to determine whether the given **event** should
        cause this transition to trigger. Reimplement this function and return
        true if the event should trigger the transition, otherwise return false.
        """
        ...
    def machine(self) -> PySide6.QtStateMachine.QStateMachine:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#machine

        **QStateMachine *QAbstractTransition::machine() const**

        Returns the state machine that this transition is part of, or `nullptr`
        if the transition is not part of a state machine.
        """
        ...
    def onTransition(self, event: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#onTransition

        **[pure virtual protected] void QAbstractTransition::onTransition(QEvent
        * event )**

        This function is called when the transition is triggered. The given
        **event** is what caused the transition to trigger. Reimplement this
        function to perform custom processing when the transition is triggered.
        """
        ...
    def removeAnimation(self, animation: PySide6.QtCore.QAbstractAnimation) -> None:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#removeAnimation

        **void QAbstractTransition::removeAnimation(QAbstractAnimation *
        animation )**

        Removes the given **animation** from this transition.

        **See also** **addAnimation** ().
        """
        ...
    def setTargetState(self, target: PySide6.QtStateMachine.QAbstractState) -> None:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#setTargetState

        **void QAbstractTransition::setTargetState(QAbstractState * target )**

        Sets the **target** state of this transition.

        **Note:** Setter function for property **targetState** .

        **See also** **targetState** ().
        """
        ...
    def setTargetStates(
        self, targets: Sequence[PySide6.QtStateMachine.QAbstractState]
    ) -> None:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#setTargetStates

        **void QAbstractTransition::setTargetStates(const QList<QAbstractState
        *> & targets )**

        Sets the target states of this transition to be the given **targets**.

        **Note:** Setter function for property **targetStates** .

        **See also** **targetStates** ().
        """
        ...
    def setTransitionType(
        self, type: PySide6.QtStateMachine.QAbstractTransition.TransitionType
    ) -> None:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#setTransitionType

        **void QAbstractTransition::setTransitionType(QAbstractTransition::Trans
        itionType type )**

        Sets the type of the transition to **type**.

        **Note:** Setter function for property **transitionType** .

        **See also** **transitionType** ().
        """
        ...
    def sourceState(self) -> PySide6.QtStateMachine.QState:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#sourceState

        **QState *QAbstractTransition::sourceState() const**

        Returns the source state of this transition, or `nullptr` if this
        transition has no source state.

        **Note:** Getter function for property sourceState.
        """
        ...
    def targetState(self) -> PySide6.QtStateMachine.QAbstractState:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#targetState

        **QAbstractState *QAbstractTransition::targetState() const**

        Returns the target state of this transition, or `nullptr` if the
        transition has no target.

        **Note:** Getter function for property targetState.

        **See also** **setTargetState** ().
        """
        ...
    def targetStates(self) -> list[PySide6.QtStateMachine.QAbstractState]:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#targetStates

        **QList<QAbstractState *> QAbstractTransition::targetStates() const**

        Returns the target states of this transition, or an empty list if this
        transition has no target states.

        **Note:** Getter function for property targetStates.

        **See also** **setTargetStates** ().
        """
        ...
    def transitionType(
        self,
    ) -> PySide6.QtStateMachine.QAbstractTransition.TransitionType:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#transitionType

        **QAbstractTransition::TransitionType
        QAbstractTransition::transitionType() const**

        Returns the type of the transition.

        **Note:** Getter function for property transitionType.

        **See also** **setTransitionType** ().
        """
        ...
    @property
    def targetStateChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#targetStateChanged

        **[private signal, since 5.4] void
        QAbstractTransition::targetStateChanged()**

        This signal is emitted when the **targetState**  property is changed.

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.

        **Note:** Notifier signal for property **targetState** .

        This function was introduced in Qt 5.4.

        **See also** **QAbstractTransition::targetState** .
        """
        ...
    @property
    def targetStatesChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#targetStatesChanged

        **[private signal, since 5.4] void
        QAbstractTransition::targetStatesChanged()**

        This signal is emitted when the **targetStates**  property is changed.

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.

        **Note:** Notifier signal for property **targetStates** .

        This function was introduced in Qt 5.4.

        **See also** **QAbstractTransition::targetStates** .
        """
        ...
    @property
    def triggered(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qabstracttransition.html#triggered

        **[private signal] void QAbstractTransition::triggered()**

        This signal is emitted when the transition has been triggered (after
        **onTransition** () has been called).

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.
        """
        ...