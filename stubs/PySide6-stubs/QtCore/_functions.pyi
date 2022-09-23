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
PySide6.QtCore, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore

def QEnum(arg__1: object) -> object: ...
def QFlag(arg__1: object) -> object: ...
def QT_TRANSLATE_NOOP(arg__1: object, arg__2: object) -> object: ...
def QT_TRANSLATE_NOOP3(arg__1: object, arg__2: object, arg__3: object) -> object: ...
def QT_TRANSLATE_NOOP_UTF8(arg__1: object) -> object: ...
def QT_TR_NOOP(arg__1: object) -> object: ...
def QT_TR_NOOP_UTF8(arg__1: object) -> object: ...
def SIGNAL(arg__1: bytes) -> str: ...
def SLOT(arg__1: bytes) -> str: ...
def __init_feature__() -> None: ...
def __moduleShutdown() -> None: ...
def qAbs(arg__1: float) -> float: ...
def qAddPostRoutine(arg__1: object) -> None: ...
def qCompress(
    data: PySide6.QtCore.QByteArray | bytes, compressionLevel: int = ...
) -> PySide6.QtCore.QByteArray: ...
def qCompress(
    data: bytes, nbytes: int, compressionLevel: int = ...
) -> PySide6.QtCore.QByteArray: ...
def qCritical(arg__1: bytes) -> None: ...
def qDebug(arg__1: bytes) -> None: ...
def qFastCos(x: float) -> float: ...
def qFastSin(x: float) -> float: ...
def qFatal(arg__1: bytes) -> None: ...
def qFormatLogMessage(
    type: PySide6.QtCore.QtMsgType, context: PySide6.QtCore.QMessageLogContext, buf: str
) -> str: ...
def qFuzzyCompare(p1: float, p2: float) -> bool: ...
def qFuzzyIsNull(d: float) -> bool: ...
def qInstallMessageHandler(arg__1: object) -> object: ...
def qIsFinite(d: float) -> bool: ...
def qIsInf(d: float) -> bool: ...
def qIsNaN(d: float) -> bool: ...
def qIsNull(d: float) -> bool: ...
def qRegisterResourceData(
    arg__1: int, arg__2: bytes, arg__3: bytes, arg__4: bytes
) -> bool: ...
def qSetMessagePattern(messagePattern: str) -> None: ...
def qUncompress(data: PySide6.QtCore.QByteArray | bytes) -> PySide6.QtCore.QByteArray: ...
def qUncompress(data: bytes, nbytes: int) -> PySide6.QtCore.QByteArray: ...
def qUnregisterResourceData(
    arg__1: int, arg__2: bytes, arg__3: bytes, arg__4: bytes
) -> bool: ...
def qVersion() -> bytes: ...
def qWarning(arg__1: bytes) -> None: ...
def qtTrId(id: bytes, n: int = ...) -> str: ...
