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

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtStateMachine

class QAbstractState(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qabstractstate.html

    **Detailed Description**

    The QAbstractState class is the abstract base class of states that are part
    of a **QStateMachine** . It defines the interface that all state objects
    have in common. QAbstractState is part of **Qt State Machine Framework** .

    The **entered** () signal is emitted when the state has been entered. The
    **exited** () signal is emitted when the state has been exited.

    The **parentState** () function returns the state's parent state. The
    **machine** () function returns the state machine that the state is part of.

    **Subclassing**

    The **onEntry** () function is called when the state is entered; reimplement
    this function to perform custom processing when the state is entered.

    The **onExit** () function is called when the state is exited; reimplement
    this function to perform custom processing when the state is exited.
    """

    def __init__(self, parent: PySide6.QtStateMachine.QState | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qabstractstate.html#QAbstractState

        **[protected] QAbstractState::QAbstractState(QState * parent =
        nullptr)**

        Constructs a new state with the given **parent** state.
        """
        ...
    def active(self) -> bool:
        """
        https://doc.qt.io/qt-6/qabstractstate.html#active

        **bool QAbstractState::active() const**

        Returns whether this state is active.

        **Note:** Getter function for property active.

        **See also** **activeChanged** (bool), **entered** (), and **exited**
        ().
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qabstractstate.html#event

        **[override virtual protected] bool QAbstractState::event(QEvent * e )**

        Reimplements: **QObject::event** (QEvent *e).
        """
        ...
    def machine(self) -> PySide6.QtStateMachine.QStateMachine:
        """
        https://doc.qt.io/qt-6/qabstractstate.html#machine

        **QStateMachine *QAbstractState::machine() const**

        Returns the state machine that this state is part of, or `nullptr` if
        the state is not part of a state machine.
        """
        ...
    def onEntry(self, event: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractstate.html#onEntry

        **[pure virtual protected] void QAbstractState::onEntry(QEvent * event
        )**

        This function is called when the state is entered. The given **event**
        is what caused the state to be entered. Reimplement this function to
        perform custom processing when the state is entered.
        """
        ...
    def onExit(self, event: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qabstractstate.html#onExit

        **[pure virtual protected] void QAbstractState::onExit(QEvent * event
        )**

        This function is called when the state is exited. The given **event** is
        what caused the state to be exited. Reimplement this function to perform
        custom processing when the state is exited.
        """
        ...
    def parentState(self) -> PySide6.QtStateMachine.QState:
        """
        https://doc.qt.io/qt-6/qabstractstate.html#parentState

        **QState *QAbstractState::parentState() const**

        Returns this state's parent state, or `nullptr` if the state has no
        parent state.
        """
        ...
    @property
    def activeChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qabstractstate.html#activeChanged

        **[signal, since 5.4] void QAbstractState::activeChanged(bool active )**

        This signal is emitted when the active property is changed with
        **active** as argument.

        **Note:** Notifier signal for property **active** .

        This function was introduced in Qt 5.4.

        **See also** **QAbstractState::active** , **entered** (), and **exited**
        ().
        """
        ...
    @property
    def entered(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qabstractstate.html#entered

        **[private signal] void QAbstractState::entered()**

        This signal is emitted when the state has been entered (after
        **onEntry** () has been called).

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.
        """
        ...
    @property
    def exited(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qabstractstate.html#exited

        **[private signal] void QAbstractState::exited()**

        This signal is emitted when the state has been exited (after **onExit**
        () has been called).

        **Note:** This is a private signal. It can be used in signal connections
        but cannot be emitted by the user.
        """
        ...
