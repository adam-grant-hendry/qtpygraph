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

class QStyleOptionToolBox(PySide6.QtWidgets.QStyleOption):
    """
    https://doc.qt.io/qt-6/qstyleoptiontoolbox.html

    **Detailed Description**

    QStyleOptionToolBox contains all the information that **QStyle**  functions
    need to draw **QToolBox** .

    For performance reasons, there are few member functions and the access to
    the member variables is direct (i.e., using the `.` or `->` operator). This
    makes the structures straightforward to use and emphasizes that these are
    simply parameters used by the style functions.

    For an example demonstrating how style options can be used, see the
    **Styles**  example.

    **See also** **QStyleOption**  and **QToolBox** .
    """

    NotAdjacent: QStyleOptionToolBox.SelectedPosition = ...
    NextIsSelected: QStyleOptionToolBox.SelectedPosition = ...
    PreviousIsSelected: QStyleOptionToolBox.SelectedPosition = ...
    Type: QStyleOptionToolBox.StyleOptionType = ...
    Version: QStyleOptionToolBox.StyleOptionVersion = ...
    Beginning: QStyleOptionToolBox.TabPosition = ...
    Middle: QStyleOptionToolBox.TabPosition = ...
    End: QStyleOptionToolBox.TabPosition = ...
    OnlyOneTab: QStyleOptionToolBox.TabPosition = ...

    class SelectedPosition(IntFlag):
        NotAdjacent: QStyleOptionToolBox.SelectedPosition = ...
        NextIsSelected: QStyleOptionToolBox.SelectedPosition = ...
        PreviousIsSelected: QStyleOptionToolBox.SelectedPosition = ...

    class StyleOptionType(IntFlag):
        Type: QStyleOptionToolBox.StyleOptionType = ...

    class StyleOptionVersion(IntFlag):
        Version: QStyleOptionToolBox.StyleOptionVersion = ...

    class TabPosition(IntFlag):
        Beginning: QStyleOptionToolBox.TabPosition = ...
        Middle: QStyleOptionToolBox.TabPosition = ...
        End: QStyleOptionToolBox.TabPosition = ...
        OnlyOneTab: QStyleOptionToolBox.TabPosition = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qstyleoptiontoolbox.html#QStyleOptionToolBox

        **QStyleOptionToolBox::QStyleOptionToolBox()**

        Creates a QStyleOptionToolBox, initializing the members variables to
        their default values.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtWidgets.QStyleOptionToolBox) -> None:
        """
        https://doc.qt.io/qt-6/qstyleoptiontoolbox.html#QStyleOptionToolBox-1

        **QStyleOptionToolBox::QStyleOptionToolBox(const QStyleOptionToolBox &
        other )**

        Constructs a copy of the **other** style option.
        """
        ...
    @overload
    def __init__(self, version: int) -> None:
        """
        https://doc.qt.io/qt-6/qstyleoptiontoolbox.html#QStyleOptionToolBox

        **QStyleOptionToolBox::QStyleOptionToolBox()**

        Creates a QStyleOptionToolBox, initializing the members variables to
        their default values.
        """
        ...
