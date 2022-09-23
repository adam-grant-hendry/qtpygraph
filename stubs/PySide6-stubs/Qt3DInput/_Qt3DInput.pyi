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
PySide6.Qt3DInput, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from collections.abc import Sequence
from enum import IntFlag

import PySide6.Qt3DCore
import PySide6.Qt3DInput
import PySide6.QtCore
import PySide6.QtGui

class Qt3DInput:
    """
    https://doc.qt.io/qt-6/qt3dinput.html

    **Detailed Description**
    """

    class QAbstractActionInput(PySide6.Qt3DCore.Qt3DCore.QNode): ...

    class QAbstractAxisInput(PySide6.Qt3DCore.Qt3DCore.QNode):
        def setSourceDevice(
            self, sourceDevice: PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice
        ) -> None: ...
        def sourceDevice(self) -> PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice: ...

    class QAbstractPhysicalDevice(PySide6.Qt3DCore.Qt3DCore.QNode):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def addAxisSetting(
            self, axisSetting: PySide6.Qt3DInput.Qt3DInput.QAxisSetting
        ) -> None: ...
        def axisCount(self) -> int: ...
        def axisIdentifier(self, name: str) -> int: ...
        def axisNames(self) -> list[str]: ...
        def axisSettings(self) -> list[PySide6.Qt3DInput.Qt3DInput.QAxisSetting]: ...
        def buttonCount(self) -> int: ...
        def buttonIdentifier(self, name: str) -> int: ...
        def buttonNames(self) -> list[str]: ...
        def removeAxisSetting(
            self, axisSetting: PySide6.Qt3DInput.Qt3DInput.QAxisSetting
        ) -> None: ...

    class QAction(PySide6.Qt3DCore.Qt3DCore.QNode):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def addInput(
            self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput
        ) -> None: ...
        def inputs(self) -> list[PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput]: ...
        def isActive(self) -> bool: ...
        def removeInput(
            self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput
        ) -> None: ...

    class QActionInput(PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def buttons(self) -> list[int]: ...
        def setButtons(self, buttons: Sequence[int]) -> None: ...
        def setSourceDevice(
            self, sourceDevice: PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice
        ) -> None: ...
        def sourceDevice(self) -> PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice: ...

    class QAnalogAxisInput(PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def axis(self) -> int: ...
        def setAxis(self, axis: int) -> None: ...

    class QAxis(PySide6.Qt3DCore.Qt3DCore.QNode):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def addInput(
            self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput
        ) -> None: ...
        def inputs(self) -> list[PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput]: ...
        def removeInput(
            self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput
        ) -> None: ...
        def value(self) -> float: ...

    class QAxisAccumulator(PySide6.Qt3DCore.Qt3DCore.QComponent):
        Velocity: Qt3DInput.QAxisAccumulator.SourceAxisType = ...
        Acceleration: Qt3DInput.QAxisAccumulator.SourceAxisType = ...

        class SourceAxisType(IntFlag):
            Velocity: Qt3DInput.QAxisAccumulator.SourceAxisType = ...
            Acceleration: Qt3DInput.QAxisAccumulator.SourceAxisType = ...
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def scale(self) -> float: ...
        def setScale(self, scale: float) -> None: ...
        def setSourceAxis(
            self, sourceAxis: PySide6.Qt3DInput.Qt3DInput.QAxis
        ) -> None: ...
        def setSourceAxisType(
            self,
            sourceAxisType: PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType,
        ) -> None: ...
        def sourceAxis(self) -> PySide6.Qt3DInput.Qt3DInput.QAxis: ...
        def sourceAxisType(
            self,
        ) -> PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType: ...
        def value(self) -> float: ...
        def velocity(self) -> float: ...

    class QAxisSetting(PySide6.Qt3DCore.Qt3DCore.QNode):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def axes(self) -> list[int]: ...
        def deadZoneRadius(self) -> float: ...
        def isSmoothEnabled(self) -> bool: ...
        def setAxes(self, axes: Sequence[int]) -> None: ...
        def setDeadZoneRadius(self, deadZoneRadius: float) -> None: ...
        def setSmoothEnabled(self, enabled: bool) -> None: ...

    class QButtonAxisInput(PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def acceleration(self) -> float: ...
        def buttons(self) -> list[int]: ...
        def deceleration(self) -> float: ...
        def scale(self) -> float: ...
        def setAcceleration(self, acceleration: float) -> None: ...
        def setButtons(self, buttons: Sequence[int]) -> None: ...
        def setDeceleration(self, deceleration: float) -> None: ...
        def setScale(self, scale: float) -> None: ...

    class QInputAspect(PySide6.Qt3DCore.Qt3DCore.QAbstractAspect):
        def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None: ...
        def availablePhysicalDevices(self) -> list[str]: ...
        def createPhysicalDevice(
            self, name: str
        ) -> PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice: ...

    class QInputChord(PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def addChord(
            self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput
        ) -> None: ...
        def chords(self) -> list[PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput]: ...
        def removeChord(
            self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput
        ) -> None: ...
        def setTimeout(self, timeout: int) -> None: ...
        def timeout(self) -> int: ...

    class QInputSequence(PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def addSequence(
            self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput
        ) -> None: ...
        def buttonInterval(self) -> int: ...
        def removeSequence(
            self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput
        ) -> None: ...
        def sequences(self) -> list[PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput]: ...
        def setButtonInterval(self, buttonInterval: int) -> None: ...
        def setTimeout(self, timeout: int) -> None: ...
        def timeout(self) -> int: ...

    class QInputSettings(PySide6.Qt3DCore.Qt3DCore.QComponent):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def eventSource(self) -> PySide6.QtCore.QObject: ...
        def setEventSource(self, eventSource: PySide6.QtCore.QObject) -> None: ...

    class QKeyEvent(PySide6.QtCore.QObject):
        def __init__(
            self,
            type: PySide6.QtCore.QEvent.Type,
            key: int,
            modifiers: PySide6.QtCore.Qt.KeyboardModifiers,
            text: str = ...,
            autorep: bool = ...,
            count: int = ...,
        ) -> None: ...
        def count(self) -> int: ...
        def isAccepted(self) -> bool: ...
        def isAutoRepeat(self) -> bool: ...
        def key(self) -> int: ...
        def matches(self, key_: PySide6.QtGui.QKeySequence.StandardKey) -> bool: ...
        def modifiers(self) -> int: ...
        def nativeScanCode(self) -> int: ...
        def setAccepted(self, accepted: bool) -> None: ...
        def text(self) -> str: ...
        def type(self) -> PySide6.QtCore.QEvent.Type: ...

    class QKeyboardDevice(PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def activeInput(self) -> PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler: ...
        def axisCount(self) -> int: ...
        def axisIdentifier(self, name: str) -> int: ...
        def axisNames(self) -> list[str]: ...
        def buttonCount(self) -> int: ...
        def buttonIdentifier(self, name: str) -> int: ...
        def buttonNames(self) -> list[str]: ...

    class QKeyboardHandler(PySide6.Qt3DCore.Qt3DCore.QComponent):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def focus(self) -> bool: ...
        def setFocus(self, focus: bool) -> None: ...
        def setSourceDevice(
            self, keyboardDevice: PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice
        ) -> None: ...
        def sourceDevice(self) -> PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice: ...

    class QLogicalDevice(PySide6.Qt3DCore.Qt3DCore.QComponent):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def actions(self) -> list[PySide6.Qt3DInput.Qt3DInput.QAction]: ...
        def addAction(self, action: PySide6.Qt3DInput.Qt3DInput.QAction) -> None: ...
        def addAxis(self, axis: PySide6.Qt3DInput.Qt3DInput.QAxis) -> None: ...
        def axes(self) -> list[PySide6.Qt3DInput.Qt3DInput.QAxis]: ...
        def removeAction(self, action: PySide6.Qt3DInput.Qt3DInput.QAction) -> None: ...
        def removeAxis(self, axis: PySide6.Qt3DInput.Qt3DInput.QAxis) -> None: ...

    class QMouseDevice(PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice):
        X: Qt3DInput.QMouseDevice.Axis = ...
        Y: Qt3DInput.QMouseDevice.Axis = ...
        WheelX: Qt3DInput.QMouseDevice.Axis = ...
        WheelY: Qt3DInput.QMouseDevice.Axis = ...

        class Axis(IntFlag):
            X: Qt3DInput.QMouseDevice.Axis = ...
            Y: Qt3DInput.QMouseDevice.Axis = ...
            WheelX: Qt3DInput.QMouseDevice.Axis = ...
            WheelY: Qt3DInput.QMouseDevice.Axis = ...
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def axisCount(self) -> int: ...
        def axisIdentifier(self, name: str) -> int: ...
        def axisNames(self) -> list[str]: ...
        def buttonCount(self) -> int: ...
        def buttonIdentifier(self, name: str) -> int: ...
        def buttonNames(self) -> list[str]: ...
        def sensitivity(self) -> float: ...
        def setSensitivity(self, value: float) -> None: ...
        def setUpdateAxesContinuously(self, updateAxesContinuously: bool) -> None: ...
        def updateAxesContinuously(self) -> bool: ...

    class QMouseEvent(PySide6.QtCore.QObject):
        NoButton: Qt3DInput.QMouseEvent.Buttons = ...
        LeftButton: Qt3DInput.QMouseEvent.Buttons = ...
        RightButton: Qt3DInput.QMouseEvent.Buttons = ...
        MiddleButton: Qt3DInput.QMouseEvent.Buttons = ...
        BackButton: Qt3DInput.QMouseEvent.Buttons = ...
        NoModifier: Qt3DInput.QMouseEvent.Modifiers = ...
        ShiftModifier: Qt3DInput.QMouseEvent.Modifiers = ...
        ControlModifier: Qt3DInput.QMouseEvent.Modifiers = ...
        AltModifier: Qt3DInput.QMouseEvent.Modifiers = ...
        MetaModifier: Qt3DInput.QMouseEvent.Modifiers = ...
        KeypadModifier: Qt3DInput.QMouseEvent.Modifiers = ...

        class Buttons(IntFlag):
            NoButton: Qt3DInput.QMouseEvent.Buttons = ...
            LeftButton: Qt3DInput.QMouseEvent.Buttons = ...
            RightButton: Qt3DInput.QMouseEvent.Buttons = ...
            MiddleButton: Qt3DInput.QMouseEvent.Buttons = ...
            BackButton: Qt3DInput.QMouseEvent.Buttons = ...

        class Modifiers(IntFlag):
            NoModifier: Qt3DInput.QMouseEvent.Modifiers = ...
            ShiftModifier: Qt3DInput.QMouseEvent.Modifiers = ...
            ControlModifier: Qt3DInput.QMouseEvent.Modifiers = ...
            AltModifier: Qt3DInput.QMouseEvent.Modifiers = ...
            MetaModifier: Qt3DInput.QMouseEvent.Modifiers = ...
            KeypadModifier: Qt3DInput.QMouseEvent.Modifiers = ...
        def button(self) -> PySide6.Qt3DInput.Qt3DInput.QMouseEvent.Buttons: ...
        def buttons(self) -> int: ...
        def isAccepted(self) -> bool: ...
        def modifiers(self) -> PySide6.Qt3DInput.Qt3DInput.QMouseEvent.Modifiers: ...
        def setAccepted(self, accepted: bool) -> None: ...
        def type(self) -> PySide6.QtCore.QEvent.Type: ...
        def wasHeld(self) -> bool: ...
        def x(self) -> int: ...
        def y(self) -> int: ...

    class QMouseHandler(PySide6.Qt3DCore.Qt3DCore.QComponent):
        def __init__(
            self, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...
        ) -> None: ...
        def containsMouse(self) -> bool: ...
        def setContainsMouse(self, contains: bool) -> None: ...
        def setSourceDevice(
            self, mouseDevice: PySide6.Qt3DInput.Qt3DInput.QMouseDevice
        ) -> None: ...
        def sourceDevice(self) -> PySide6.Qt3DInput.Qt3DInput.QMouseDevice: ...

    class QWheelEvent(PySide6.QtCore.QObject):
        NoButton: Qt3DInput.QWheelEvent.Buttons = ...
        LeftButton: Qt3DInput.QWheelEvent.Buttons = ...
        RightButton: Qt3DInput.QWheelEvent.Buttons = ...
        MiddleButton: Qt3DInput.QWheelEvent.Buttons = ...
        BackButton: Qt3DInput.QWheelEvent.Buttons = ...
        NoModifier: Qt3DInput.QWheelEvent.Modifiers = ...
        ShiftModifier: Qt3DInput.QWheelEvent.Modifiers = ...
        ControlModifier: Qt3DInput.QWheelEvent.Modifiers = ...
        AltModifier: Qt3DInput.QWheelEvent.Modifiers = ...
        MetaModifier: Qt3DInput.QWheelEvent.Modifiers = ...
        KeypadModifier: Qt3DInput.QWheelEvent.Modifiers = ...

        class Buttons(IntFlag):
            NoButton: Qt3DInput.QWheelEvent.Buttons = ...
            LeftButton: Qt3DInput.QWheelEvent.Buttons = ...
            RightButton: Qt3DInput.QWheelEvent.Buttons = ...
            MiddleButton: Qt3DInput.QWheelEvent.Buttons = ...
            BackButton: Qt3DInput.QWheelEvent.Buttons = ...

        class Modifiers(IntFlag):
            NoModifier: Qt3DInput.QWheelEvent.Modifiers = ...
            ShiftModifier: Qt3DInput.QWheelEvent.Modifiers = ...
            ControlModifier: Qt3DInput.QWheelEvent.Modifiers = ...
            AltModifier: Qt3DInput.QWheelEvent.Modifiers = ...
            MetaModifier: Qt3DInput.QWheelEvent.Modifiers = ...
            KeypadModifier: Qt3DInput.QWheelEvent.Modifiers = ...
        def angleDelta(self) -> PySide6.QtCore.QPoint: ...
        def buttons(self) -> int: ...
        def isAccepted(self) -> bool: ...
        def modifiers(self) -> PySide6.Qt3DInput.Qt3DInput.QWheelEvent.Modifiers: ...
        def setAccepted(self, accepted: bool) -> None: ...
        def type(self) -> PySide6.QtCore.QEvent.Type: ...
        def x(self) -> int: ...
        def y(self) -> int: ...
