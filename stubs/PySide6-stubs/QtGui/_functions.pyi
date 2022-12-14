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
PySide6.QtGui, except for defaults which are replaced by "...".
"""
from __future__ import annotations

import PySide6.QtCore
import PySide6.QtGui

def qAlpha(rgb: int) -> int: ...
def qBlue(rgb: int) -> int: ...
def qGray(r: int, g: int, b: int) -> int: ...
def qGray(rgb: int) -> int: ...
def qGreen(rgb: int) -> int: ...
def qIsGray(rgb: int) -> bool: ...
def qPixelFormatAlpha(
    channelSize: int, typeInt: PySide6.QtGui.QPixelFormat.TypeInterpretation = ...
) -> PySide6.QtGui.QPixelFormat: ...
def qPixelFormatCmyk(
    channelSize: int,
    alfa: int = ...,
    usage: PySide6.QtGui.QPixelFormat.AlphaUsage = ...,
    position: PySide6.QtGui.QPixelFormat.AlphaPosition = ...,
    typeInt: PySide6.QtGui.QPixelFormat.TypeInterpretation = ...,
) -> PySide6.QtGui.QPixelFormat: ...
def qPixelFormatGrayscale(
    channelSize: int, typeInt: PySide6.QtGui.QPixelFormat.TypeInterpretation = ...
) -> PySide6.QtGui.QPixelFormat: ...
def qPixelFormatHsl(
    channelSize: int,
    alfa: int = ...,
    usage: PySide6.QtGui.QPixelFormat.AlphaUsage = ...,
    position: PySide6.QtGui.QPixelFormat.AlphaPosition = ...,
    typeInt: PySide6.QtGui.QPixelFormat.TypeInterpretation = ...,
) -> PySide6.QtGui.QPixelFormat: ...
def qPixelFormatHsv(
    channelSize: int,
    alfa: int = ...,
    usage: PySide6.QtGui.QPixelFormat.AlphaUsage = ...,
    position: PySide6.QtGui.QPixelFormat.AlphaPosition = ...,
    typeInt: PySide6.QtGui.QPixelFormat.TypeInterpretation = ...,
) -> PySide6.QtGui.QPixelFormat: ...
def qPixelFormatRgba(
    red: int,
    green: int,
    blue: int,
    alfa: int,
    usage: PySide6.QtGui.QPixelFormat.AlphaUsage,
    position: PySide6.QtGui.QPixelFormat.AlphaPosition,
    pmul: PySide6.QtGui.QPixelFormat.AlphaPremultiplied = ...,
    typeInt: PySide6.QtGui.QPixelFormat.TypeInterpretation = ...,
) -> PySide6.QtGui.QPixelFormat: ...
def qPixelFormatYuv(
    layout: PySide6.QtGui.QPixelFormat.YUVLayout,
    alfa: int = ...,
    usage: PySide6.QtGui.QPixelFormat.AlphaUsage = ...,
    position: PySide6.QtGui.QPixelFormat.AlphaPosition = ...,
    p_mul: PySide6.QtGui.QPixelFormat.AlphaPremultiplied = ...,
    typeInt: PySide6.QtGui.QPixelFormat.TypeInterpretation = ...,
    b_order: PySide6.QtGui.QPixelFormat.ByteOrder = ...,
) -> PySide6.QtGui.QPixelFormat: ...
def qRed(rgb: int) -> int: ...
def qRgb(r: int, g: int, b: int) -> int: ...
def qRgba(r: int, g: int, b: int, a: int) -> int: ...
