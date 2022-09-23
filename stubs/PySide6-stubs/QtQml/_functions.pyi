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
PySide6.QtQml, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtNetwork
import PySide6.QtQml

def QmlAnonymous(arg__1: object) -> object: ...
def QmlElement(arg__1: object) -> object: ...
def QmlSingleton(arg__1: object) -> object: ...
def qjsEngine(arg__1: PySide6.QtCore.QObject) -> PySide6.QtQml.QJSEngine | None: ...
def qmlClearTypeRegistrations() -> None: ...
def qmlContext(arg__1: PySide6.QtCore.QObject) -> PySide6.QtQml.QQmlContext | None: ...
def qmlEngine(arg__1: PySide6.QtCore.QObject) -> PySide6.QtQml.QQmlEngine | None: ...
def qmlProtectModule(uri: bytes, majVersion: int) -> bool: ...
def qmlRegisterModule(uri: bytes, versionMajor: int, versionMinor: int) -> None: ...
def qmlRegisterSingletonInstance(
    arg__1: type, arg__2: bytes, arg__3: int, arg__4: int, arg__5: bytes, arg__6: object
) -> int: ...
def qmlRegisterSingletonType(
    arg__1: type, arg__2: bytes, arg__3: int, arg__4: int, arg__5: bytes
) -> int: ...
def qmlRegisterSingletonType(
    arg__1: type, arg__2: bytes, arg__3: int, arg__4: int, arg__5: bytes, arg__6: object
) -> int: ...
def qmlRegisterSingletonType(
    arg__1: bytes, arg__2: int, arg__3: int, arg__4: bytes, arg__5: object
) -> int: ...
def qmlRegisterSingletonType(
    url: PySide6.QtCore.QUrl | str,
    uri: bytes,
    versionMajor: int,
    versionMinor: int,
    qmlName: bytes,
) -> int: ...
def qmlRegisterType(
    arg__1: type, arg__2: bytes, arg__3: int, arg__4: int, arg__5: bytes
) -> int: ...
def qmlRegisterType(
    url: PySide6.QtCore.QUrl | str,
    uri: bytes,
    versionMajor: int,
    versionMinor: int,
    qmlName: bytes,
) -> int: ...
def qmlRegisterUncreatableMetaObject(
    staticMetaObject: PySide6.QtCore.QMetaObject,
    uri: bytes,
    versionMajor: int,
    versionMinor: int,
    qmlName: bytes,
    reason: str,
) -> int: ...
def qmlRegisterUncreatableType(
    arg__1: type, arg__2: bytes, arg__3: int, arg__4: int, arg__5: bytes, arg__6: bytes
) -> int: ...
def qmlTypeId(
    uri: bytes, versionMajor: int, versionMinor: int, qmlName: bytes
) -> int: ...
