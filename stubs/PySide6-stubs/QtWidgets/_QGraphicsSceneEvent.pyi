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

class QGraphicsSceneEvent(PySide6.QtCore.QEvent):
    """
    https://doc.qt.io/qt-6/qgraphicssceneevent.html

    **Detailed Description**

    When a **QGraphicsView**  receives Qt mouse, keyboard, and drag and drop
    events (**QMouseEvent** , **QKeyEvent** , QDragEvent, etc.), it translates
    them into instances of QGraphicsSceneEvent subclasses and forwards them to
    the **QGraphicsScene**  it displays. The scene then forwards the events to
    the relevant items.

    For example, when a **QGraphicsView**  receives a **QMouseEvent**  of type
    MousePress as a response to a user click, the view sends a
    **QGraphicsSceneMouseEvent**  of type GraphicsSceneMousePress to the
    underlying **QGraphicsScene**  through its **mousePressEvent** () function.
    The default **QGraphicsScene::mousePressEvent** () implementation determines
    which item was clicked and forwards the event to
    **QGraphicsItem::mousePressEvent** ().

    Subclasses such as **QGraphicsSceneMouseEvent**  and
    **QGraphicsSceneContextMenuEvent**  provide the coordinates from the
    original **QEvent**  in screen, scene, and item coordinates (see
    **screenPos** (), **scenePos** (), and **pos** ()). The item coordinates are
    set by the **QGraphicsScene**  before it forwards the event to the event to
    a **QGraphicsItem** . The mouse events also add the possibility to retrieve
    the coordinates from the last event received by the view (see
    **lastScreenPos** (), **lastScenePos** (), and **lastPos** ()).

    **See also** **QEvent** .
    """

    def __init__(self, type: PySide6.QtCore.QEvent.Type) -> None: ...
    def setTimestamp(self, ts: int) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicssceneevent.html#timestamp

        **[since 6.2] quint64 QGraphicsSceneEvent::timestamp() const**

        Returns the timestamp of the original event, or 0 if the original event
        does not report a time stamp.

        This function was introduced in Qt 6.2.
        """
        ...
    def timestamp(self) -> int:
        """
        https://doc.qt.io/qt-6/qgraphicssceneevent.html#timestamp

        **[since 6.2] quint64 QGraphicsSceneEvent::timestamp() const**

        Returns the timestamp of the original event, or 0 if the original event
        does not report a time stamp.

        This function was introduced in Qt 6.2.
        """
        ...
    def widget(self) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qgraphicssceneevent.html#widget

        **QWidget *QGraphicsSceneEvent::widget() const**

        Returns the widget where the event originated, or `nullptr` if the event
        originates from another application.
        """
        ...
