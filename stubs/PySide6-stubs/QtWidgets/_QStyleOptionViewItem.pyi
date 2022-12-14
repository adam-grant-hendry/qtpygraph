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

class QStyleOptionViewItem(PySide6.QtWidgets.QStyleOption):
    """
    https://doc.qt.io/qt-6/qstyleoptionviewitem.html

    **Detailed Description**

    QStyleOptionViewItem contains all the information that **QStyle**  functions
    need to draw the items for Qt's model/view classes.

    For performance reasons, there are few member functions and the access to
    the member variables is direct (i.e., using the `.` or `->` operator). This
    makes the structures straightforward to use and emphasizes that these are
    simply parameters used by the style functions.

    For an example demonstrating how style options can be used, see the
    **Styles**  example.

    **See also** **QStyleOption**  and **Model/View Programming** .
    """

    Left: QStyleOptionViewItem.Position = ...
    Right: QStyleOptionViewItem.Position = ...
    Top: QStyleOptionViewItem.Position = ...
    Bottom: QStyleOptionViewItem.Position = ...
    Type: QStyleOptionViewItem.StyleOptionType = ...
    Version: QStyleOptionViewItem.StyleOptionVersion = ...
    None_: QStyleOptionViewItem.ViewItemFeature = ...
    WrapText: QStyleOptionViewItem.ViewItemFeature = ...
    Alternate: QStyleOptionViewItem.ViewItemFeature = ...
    HasCheckIndicator: QStyleOptionViewItem.ViewItemFeature = ...
    HasDisplay: QStyleOptionViewItem.ViewItemFeature = ...
    HasDecoration: QStyleOptionViewItem.ViewItemFeature = ...
    Invalid: QStyleOptionViewItem.ViewItemPosition = ...
    Beginning: QStyleOptionViewItem.ViewItemPosition = ...
    Middle: QStyleOptionViewItem.ViewItemPosition = ...
    End: QStyleOptionViewItem.ViewItemPosition = ...
    OnlyOne: QStyleOptionViewItem.ViewItemPosition = ...

    class Position(IntFlag):
        Left: QStyleOptionViewItem.Position = ...
        Right: QStyleOptionViewItem.Position = ...
        Top: QStyleOptionViewItem.Position = ...
        Bottom: QStyleOptionViewItem.Position = ...

    class StyleOptionType(IntFlag):
        Type: QStyleOptionViewItem.StyleOptionType = ...

    class StyleOptionVersion(IntFlag):
        Version: QStyleOptionViewItem.StyleOptionVersion = ...

    class ViewItemFeature(IntFlag):
        None_: QStyleOptionViewItem.ViewItemFeature = ...
        WrapText: QStyleOptionViewItem.ViewItemFeature = ...
        Alternate: QStyleOptionViewItem.ViewItemFeature = ...
        HasCheckIndicator: QStyleOptionViewItem.ViewItemFeature = ...
        HasDisplay: QStyleOptionViewItem.ViewItemFeature = ...
        HasDecoration: QStyleOptionViewItem.ViewItemFeature = ...

    class ViewItemFeatures: ...

    class ViewItemPosition(IntFlag):
        Invalid: QStyleOptionViewItem.ViewItemPosition = ...
        Beginning: QStyleOptionViewItem.ViewItemPosition = ...
        Middle: QStyleOptionViewItem.ViewItemPosition = ...
        End: QStyleOptionViewItem.ViewItemPosition = ...
        OnlyOne: QStyleOptionViewItem.ViewItemPosition = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qstyleoptionviewitem.html#QStyleOptionViewItem

        **QStyleOptionViewItem::QStyleOptionViewItem()**

        Constructs a QStyleOptionViewItem, initializing the members variables to
        their default values.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtWidgets.QStyleOptionViewItem) -> None:
        """
        https://doc.qt.io/qt-6/qstyleoptionviewitem.html#QStyleOptionViewItem-1

        **QStyleOptionViewItem::QStyleOptionViewItem(const QStyleOptionViewItem
        & other )**

        Constructs a copy of the **other** style option.
        """
        ...
    @overload
    def __init__(self, version: int) -> None:
        """
        https://doc.qt.io/qt-6/qstyleoptionviewitem.html#QStyleOptionViewItem

        **QStyleOptionViewItem::QStyleOptionViewItem()**

        Constructs a QStyleOptionViewItem, initializing the members variables to
        their default values.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
