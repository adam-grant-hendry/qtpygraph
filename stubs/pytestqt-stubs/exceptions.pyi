from __future__ import annotations

from collections.abc import Generator

from _typeshed import Incomplete

def capture_exceptions() -> Generator[Incomplete, None, None]: ...

class _QtExceptionCaptureManager:
    old_hook: Incomplete
    exceptions: Incomplete
    def __init__(self) -> None: ...
    def start(self) -> None: ...
    def finish(self) -> None: ...
    def fail_if_exceptions_occurred(self, when) -> None: ...

def format_captured_exceptions(exceptions): ...

class TimeoutError(Exception): ...
