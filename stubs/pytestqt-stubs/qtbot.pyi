from __future__ import annotations

from collections.abc import Callable, Generator
from types import TracebackType
from typing import Any, Optional, TypeVar

from _pytest.fixtures import SubRequest
from pytestqt.exceptions import TimeoutError as TimeoutError
from pytestqt.qt_compat import qt_api as qt_api
from pytestqt.wait_signal import CallbackBlocker as CallbackBlocker
from pytestqt.wait_signal import CallbackCalledTwiceError as CallbackCalledTwiceError
from pytestqt.wait_signal import MultiSignalBlocker as MultiSignalBlocker
from pytestqt.wait_signal import SignalBlocker as SignalBlocker
from pytestqt.wait_signal import SignalEmittedError as SignalEmittedError
from pytestqt.wait_signal import SignalEmittedSpy as SignalEmittedSpy

AssertReturn = Optional[bool | AssertionError]

class QtBot:
    def __init__(
        self,
        request: SubRequest,
    ) -> None: ...
    def addWidget(
        self,
        widget: qt_api.QtWidgets.QWidget,
        *,
        before_close_func: Callable[..., Any] | None = ...,
    ) -> None: ...
    def waitActive(
        self,
        widget: qt_api.QtWidgets.QWidget,
        *,
        timeout: int = ...,
    ) -> _WaitWidgetContextManager: ...
    def waitExposed(
        self,
        widget: qt_api.QtWidgets.QWidget,
        *,
        timeout: int = ...,
    ) -> _WaitWidgetContextManager: ...
    def waitForWindowShown(
        self,
        widget: qt_api.QtWidgets.QWidget,
    ) -> bool: ...
    def stop(self) -> None: ...
    def waitSignal(
        self,
        signal: qt_api.QtCore.SignalInstance,
        *,
        timeout: int = ...,
        raising: bool | None = ...,
        check_params_cb: Callable[..., bool] = ...,
    ) -> SignalBlocker: ...
    def waitSignals(
        self,
        signals: list[qt_api.QtCore.SignalInstance],
        *,
        timeout: int = ...,
        raising: bool | None = ...,
        check_params_cbs: Callable[..., bool] = ...,
        order: str = ...,
    ) -> MultiSignalBlocker: ...
    def wait(
        self,
        ms: int,
    ) -> None: ...
    def assertNotEmitted(
        self,
        signal: qt_api.QtCore.SignalInstance,
        *,
        wait: int = ...,
    ) -> Generator[None, None, None]: ...
    def waitUntil(
        self,
        callback: Callable[
            ...,
            AssertReturn,
        ],
        *,
        timeout: int = ...,
    ) -> None: ...
    def waitCallback(
        self,
        *,
        timeout: int = ...,
        raising: bool | None = ...,
    ) -> CallbackBlocker: ...
    def captureExceptions(
        self,
    ) -> Generator[
        list[
            tuple[
                type[BaseException] | None,
                BaseException | None,
                TracebackType | None,
            ]
        ],
        None,
        None,
    ]: ...
    @staticmethod
    def keyClick(
        __widget_window: qt_api.QtWidgets.QWidget | qt_api.QtGui.QWindow,
        __key: qt_api.QtCore.Qt.Key | str,  # c char
        modifier: qt_api.QtCore.Qt.KeyboardModifiers = ...,
        delay: int = ...,  # c int
    ) -> None: ...
    @staticmethod
    def keyClicks(
        __widget: qt_api.QtWidgets.QWidget,
        __sequence: qt_api.QtCore.Qt.QString,
        modifier: qt_api.QtCore.Qt.KeyboardModifiers = ...,
        delay: int = ...,
    ) -> None: ...
    @staticmethod
    def keyEvent(
        __action: qt_api.QtTests.QTest.KeyAction,
        __widget_window: qt_api.QtWidgets.QWidget | qt_api.QtGui.QWindow,
        __key_ascii: qt_api.QtGui.Key | str,  # c char
        modifier: qt_api.QtCore.Qt.KeyboardModifiers = ...,
        delay: int = ...,  # c int
    ) -> None: ...
    @staticmethod
    def keyPress(
        __widget_window: qt_api.QtWidgets.QWidget | qt_api.QtGui.QWindow,
        __key: qt_api.QtCore.Qt.Key | str,  # c char
        modifier: qt_api.QtCore.Qt.KeyboardModifiers = ...,
        delay: int = ...,  # c int
    ) -> None: ...
    @staticmethod
    def keyRelease(
        __widget_window: qt_api.QtWidgets.QWidget | qt_api.QtGui.QWindow,
        __key: qt_api.QtCore.Qt.Key | str,  # c char
        modifier: qt_api.QtCore.Qt.KeyboardModifiers = ...,
        delay: int = ...,  # c int
    ) -> None: ...
    @staticmethod
    def keySequence(
        widget: qt_api.QtWidgets.QWidget,
        key_sequence: qt_api.QtGui.QKeySequence,
    ) -> None: ...
    @staticmethod
    def keyToAscii(key: qt_api.QtGui.Key | str) -> str: ...
    @staticmethod
    def mouseClick(
        __widget_window: qt_api.QtWidgets.QWidget | qt_api.QtGui.QWindow,
        __button: qt_api.QtCore.Qt.MouseButton,
        modifier: qt_api.QtCore.Qt.KeyboardModifiers = ...,
        pos: qt_api.QtCore.QPoint = ...,
        delay: int = ...,  # c int
    ) -> None: ...
    @staticmethod
    def mouseDClick(
        __widget_window: qt_api.QtWidgets.QWidget | qt_api.QtGui.QWindow,
        __button: qt_api.QtCore.Qt.MouseButton,
        modifier: qt_api.QtCore.Qt.KeyboardModifiers = ...,
        pos: qt_api.QtCore.QPoint = ...,
        delay: int = ...,  # c int
    ) -> None: ...
    @staticmethod
    def mouseMove(
        __widget_window: qt_api.QtWidgets.QWidget | qt_api.QtGui.QWindow,
        pos: qt_api.QtCore.QPoint = ...,
        delay: int = ...,
    ) -> None: ...
    @staticmethod
    def mousePress(
        __widget_window: qt_api.QtWidgets.QWidget | qt_api.QtGui.QWindow,
        __button: qt_api.QtCore.Qt.MouseButton,
        modifier: qt_api.QtCore.Qt.KeyboardModifiers = ...,
        pos: qt_api.QtCore.QPoint = ...,
        delay: int = ...,  # c int
    ) -> None: ...
    @staticmethod
    def mouseRelease(
        __widget_window: qt_api.QtWidgets.QWidget | qt_api.QtGui.QWindow,
        __button: qt_api.QtCore.Qt.MouseButton,
        modifier: qt_api.QtCore.Qt.KeyboardModifiers = ...,
        pos: qt_api.QtCore.QPoint = ...,
        delay: int = ...,  # c int
    ) -> None: ...
    def add_widget(
        self,
        widget: qt_api.QtWidgets.QWidget,
        *,
        before_close_func: Callable[..., Any] | None = ...,
    ) -> None: ...
    def wait_active(
        self,
        widget: qt_api.QtWidgets.QWidget,
        *,
        timeout: int = ...,
    ) -> _WaitWidgetContextManager: ...
    def wait_exposed(
        self,
        widget: qt_api.QtWidgets.QWidget,
        *,
        timeout: int = ...,
    ) -> _WaitWidgetContextManager: ...
    def wait_for_window_shown(
        self,
        widget: qt_api.QtWidgets.QWidget,
    ) -> bool: ...
    def wait_signal(
        self,
        signal: qt_api.QtCore.SignalInstance,
        *,
        timeout: int = ...,
        raising: bool | None = ...,
        check_params_cb: Callable[..., bool] = ...,
    ) -> SignalBlocker: ...
    def wait_signals(
        self,
        signals: list[qt_api.QtCore.SignalInstance],
        *,
        timeout: int = ...,
        raising: bool | None = ...,
        check_params_cbs: Callable[..., bool] = ...,
        order: str = ...,
    ) -> MultiSignalBlocker: ...
    def assert_not_emitted(
        self,
        signal: qt_api.QtCore.SignalInstance,
        *,
        wait: int = ...,
    ) -> Generator[None, None, None]: ...
    def wait_until(
        self,
        callback: Callable[
            ...,
            AssertReturn,
        ],
        *,
        timeout: int = ...,
    ) -> None: ...
    def wait_callback(
        self,
        *,
        timeout: int = ...,
        raising: bool | None = ...,
    ) -> CallbackBlocker: ...

Self = TypeVar('Self', bound='_WaitWidgetContextManager')

class _WaitWidgetContextManager:
    def __init__(
        self,
        method_name: str,
        adjective_name: str,
        widget: qt_api.QtWidgets.QWidget,
        timeout: int,
    ) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
