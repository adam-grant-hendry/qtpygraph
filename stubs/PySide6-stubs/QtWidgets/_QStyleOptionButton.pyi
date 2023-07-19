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

class QStyleOptionButton(PySide6.QtWidgets.QStyleOption):
    """
    https://doc.qt.io/qt-6/qstyleoptionbutton.html

    **Detailed Description**

    QStyleOptionButton contains all the information that **QStyle**  functions
    need to draw graphical elements like **QPushButton** , **QCheckBox** , and
    **QRadioButton** .

    For performance reasons, there are few member functions and the access to
    the member variables is direct (i.e., using the `.` or `->` operator). This
    makes the structures straightforward to use and emphasizes that these are
    simply parameters used by the style functions.

    For an example demonstrating how style options can be used, see the
    **Styles**  example.

    **See also** **QStyleOption**  and **QStyleOptionToolButton** .
    """

    None_: QStyleOptionButton.ButtonFeature = ...
    Flat: QStyleOptionButton.ButtonFeature = ...
    HasMenu: QStyleOptionButton.ButtonFeature = ...
    DefaultButton: QStyleOptionButton.ButtonFeature = ...
    AutoDefaultButton: QStyleOptionButton.ButtonFeature = ...
    CommandLinkButton: QStyleOptionButton.ButtonFeature = ...
    Type: QStyleOptionButton.StyleOptionType = ...
    Version: QStyleOptionButton.StyleOptionVersion = ...

    class ButtonFeature(IntFlag):
        None_: QStyleOptionButton.ButtonFeature = ...
        Flat: QStyleOptionButton.ButtonFeature = ...
        HasMenu: QStyleOptionButton.ButtonFeature = ...
        DefaultButton: QStyleOptionButton.ButtonFeature = ...
        AutoDefaultButton: QStyleOptionButton.ButtonFeature = ...
        CommandLinkButton: QStyleOptionButton.ButtonFeature = ...

    class ButtonFeatures: ...

    class StyleOptionType(IntFlag):
        Type: QStyleOptionButton.StyleOptionType = ...

    class StyleOptionVersion(IntFlag):
        Version: QStyleOptionButton.StyleOptionVersion = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qstyleoptionbutton.html#QStyleOptionButton

        **QStyleOptionButton::QStyleOptionButton()**

        Constructs a QStyleOptionButton, initializing the members variables to
        their default values.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtWidgets.QStyleOptionButton) -> None:
        """
        https://doc.qt.io/qt-6/qstyleoptionbutton.html#QStyleOptionButton-1

        **QStyleOptionButton::QStyleOptionButton(const QStyleOptionButton &
        other )**

        Constructs a copy of the **other** style option.
        """
        ...
    @overload
    def __init__(self, version: int) -> None:
        """
        https://doc.qt.io/qt-6/qstyleoptionbutton.html#QStyleOptionButton

        **QStyleOptionButton::QStyleOptionButton()**

        Constructs a QStyleOptionButton, initializing the members variables to
        their default values.
        """
        ...