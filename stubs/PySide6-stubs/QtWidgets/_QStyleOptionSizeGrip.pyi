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
PySide6.QtWidgets, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QStyleOptionSizeGrip(PySide6.QtWidgets.QStyleOptionComplex):
    """
    https://doc.qt.io/qt-6/qstyleoptionsizegrip.html

    **Detailed Description**

    **QStyleOptionButton**  contains all the information that **QStyle**
    functions need to draw **QSizeGrip** .

    For performance reasons, there are few member functions and the access to
    the member variables is direct (i.e., using the `.` or `->` operator). This
    makes the structures straightforward to use and emphasizes that these are
    simply parameters used by the style functions.

    For an example demonstrating how style options can be used, see the
    **Styles**  example.

    **See also** **QStyleOption** , **QStyleOptionComplex** , and **QSizeGrip**
    .
    """

    Type: QStyleOptionSizeGrip.StyleOptionType = ...
    Version: QStyleOptionSizeGrip.StyleOptionVersion = ...

    class StyleOptionType(IntFlag):
        Type: QStyleOptionSizeGrip.StyleOptionType = ...

    class StyleOptionVersion(IntFlag):
        Version: QStyleOptionSizeGrip.StyleOptionVersion = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qstyleoptionsizegrip.html#QStyleOptionSizeGrip

        **QStyleOptionSizeGrip::QStyleOptionSizeGrip()**

        Constructs a QStyleOptionSizeGrip.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtWidgets.QStyleOptionSizeGrip) -> None:
        """
        https://doc.qt.io/qt-6/qstyleoptionsizegrip.html#QStyleOptionSizeGrip-1

        **QStyleOptionSizeGrip::QStyleOptionSizeGrip(const QStyleOptionSizeGrip
        & other )**

        Constructs a copy of the **other** style option.
        """
        ...
    @overload
    def __init__(self, version: int) -> None:
        """
        https://doc.qt.io/qt-6/qstyleoptionsizegrip.html#QStyleOptionSizeGrip

        **QStyleOptionSizeGrip::QStyleOptionSizeGrip()**

        Constructs a QStyleOptionSizeGrip.
        """
        ...
