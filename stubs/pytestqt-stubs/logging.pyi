from __future__ import annotations

from collections.abc import Generator
from typing import NamedTuple

from _typeshed import Incomplete
from py._code.code import TerminalRepr

class QtLoggingPlugin:
    LOG_FAIL_OPTIONS: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def pytest_runtest_setup(self, item) -> None: ...
    def pytest_runtest_makereport(
        self, item, call
    ) -> Generator[None, Incomplete, None]: ...

class _QtMessageCapture:
    def __init__(self, ignore_regexes) -> None: ...
    def disabled(self) -> Generator[None, None, None]: ...

    class _Context(NamedTuple):
        file: Incomplete
        function: Incomplete
        line: Incomplete
        category: Incomplete
    @property
    def records(self): ...

class Record:
    def __init__(self, msg_type, message, ignored, context) -> None: ...
    message: Incomplete
    type: Incomplete
    type_name: Incomplete
    log_type_name: Incomplete
    when: Incomplete
    ignored: Incomplete
    context: Incomplete
    def matches_level(self, level): ...

class _QtLogLevelErrorRepr(TerminalRepr):
    fileloc: Incomplete
    sections: Incomplete
    def __init__(self, item, level, is_modeltest_error) -> None: ...
    def addsection(self, name, content, sep: str = ...) -> None: ...
    def toterminal(self, out) -> None: ...
