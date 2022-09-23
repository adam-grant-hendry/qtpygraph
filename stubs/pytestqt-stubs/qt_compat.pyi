from __future__ import annotations

from typing import NamedTuple

from _typeshed import Incomplete

class VersionTuple(NamedTuple):
    qt_api: Incomplete
    qt_api_version: Incomplete
    runtime: Incomplete
    compiled: Incomplete

class _QtApi:
    def __init__(self) -> None: ...
    pytest_qt_api: Incomplete
    is_pyside: Incomplete
    is_pyqt: Incomplete
    QtCore: Incomplete
    QtGui: Incomplete
    QtTest: Incomplete
    QtWidgets: Incomplete
    qInfo: Incomplete
    qDebug: Incomplete
    qWarning: Incomplete
    qCritical: Incomplete
    qFatal: Incomplete
    Signal: Incomplete
    Slot: Incomplete
    Property: Incomplete
    def set_qt_api(self, api): ...
    def exec(self, obj, *args, **kwargs): ...
    def get_versions(self): ...

qt_api: Incomplete
