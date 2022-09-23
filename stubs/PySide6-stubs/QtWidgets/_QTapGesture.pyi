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

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QTapGesture(PySide6.QtWidgets.QGesture):
    """
    https://doc.qt.io/qt-6/qtapgesture.html

    **Detailed Description**

    For an overview of gesture handling in Qt and information on using gestures
    in your applications, see the **Gestures in Widgets and Graphics View**
    document.

    **See also** **QPanGesture**  and **QPinchGesture** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None: ...
    def position(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qtapgesture.html#position-prop

        **position : QPointF**

        This property holds the position of the tap

        **Access functions:**

        QPointF **position** () const
        void **setPosition** (const QPointF &
        **pos** )

        **Member Function Documentation**
        """
        ...
    def setPosition(
        self,
        pos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtapgesture.html#position-prop

        **position : QPointF**

        This property holds the position of the tap

        **Access functions:**

        QPointF **position** () const
        void **setPosition** (const QPointF &
        **pos** )

        **Member Function Documentation**
        """
        ...
