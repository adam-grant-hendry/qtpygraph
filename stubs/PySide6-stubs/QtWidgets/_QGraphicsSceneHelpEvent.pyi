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

class QGraphicsSceneHelpEvent(PySide6.QtWidgets.QGraphicsSceneEvent):
    """
    https://doc.qt.io/qt-6/qgraphicsscenehelpevent.html

    **Detailed Description**

    When a **QGraphicsView**  receives a **QEvent**  of type **QEvent::ToolTip**
    , it creates a QGraphicsSceneHelpEvent, which is forwarded to the scene. You
    can set a tooltip on a **QGraphicsItem**  with **setToolTip** (); by default
    **QGraphicsScene**  displays the tooltip of the **QGraphicsItem**  with the
    highest z-value (i.e, the top-most item) under the mouse position.

    **QGraphicsView**  does not forward events when **"What's This"**  and
    **status tip**  help is requested. If you need this, you can reimplement
    **QGraphicsView::viewportEvent** () and forward **QStatusTipEvent**  events
    and **QEvents**  of type **QEvent::WhatsThis**  to the scene.

    **See also** **QEvent** .
    """

    def __init__(self, type: PySide6.QtCore.QEvent.Type | None = ...) -> None: ...
    def scenePos(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehelpevent.html#scenePos

        **QPointF QGraphicsSceneHelpEvent::scenePos() const**

        Returns the position of the mouse cursor in scene coordinates at the
        moment the help event was sent.

        **See also** **screenPos** ().
        """
        ...
    def screenPos(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehelpevent.html#screenPos

        **QPoint QGraphicsSceneHelpEvent::screenPos() const**

        Returns the position of the mouse cursor in screen coordinates at the
        moment the help event was sent.

        **See also** **scenePos** ().
        """
        ...
    def setScenePos(
        self,
        pos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehelpevent.html#scenePos

        **QPointF QGraphicsSceneHelpEvent::scenePos() const**

        Returns the position of the mouse cursor in scene coordinates at the
        moment the help event was sent.

        **See also** **screenPos** ().
        """
        ...
    def setScreenPos(self, pos: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsscenehelpevent.html#screenPos

        **QPoint QGraphicsSceneHelpEvent::screenPos() const**

        Returns the position of the mouse cursor in screen coordinates at the
        moment the help event was sent.

        **See also** **scenePos** ().
        """
        ...
