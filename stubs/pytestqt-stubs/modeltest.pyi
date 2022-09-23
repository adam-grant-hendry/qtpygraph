from __future__ import annotations

from typing import NamedTuple

from _typeshed import Incomplete

class _Changing(NamedTuple):
    parent: Incomplete
    old_size: Incomplete
    last: Incomplete
    next: Incomplete

HAS_QT_TESTER: Incomplete

class ModelTester:
    def __init__(self, config) -> None: ...
    def check(self, model, force_py: bool = ...) -> None: ...
