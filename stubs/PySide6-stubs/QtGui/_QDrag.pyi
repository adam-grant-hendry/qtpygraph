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

from typing import overload

import PySide6.QtCore
import PySide6.QtGui

class QDrag(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qdrag.html

    **Detailed Description**

    Drag and drop is an intuitive way for users to copy or move data around in
    an application, and is used in many desktop environments as a mechanism for
    copying data between applications. Drag and drop support in Qt is centered
    around the QDrag class that handles most of the details of a drag and drop
    operation.

    The data to be transferred by the drag and drop operation is contained in a
    **QMimeData**  object. This is specified with the **setMimeData** ()
    function in the following way:

    **QDrag**  *drag = new **QDrag** (this);
                **QMimeData**
    *mimeData = new **QMimeData** ;
    mimeData->setText(commentEdit->toPlainText());
    drag->setMimeData(mimeData);

    Note that **setMimeData** () assigns ownership of the **QMimeData**  object
    to the QDrag object. The QDrag must be constructed on the heap with a parent
    **QObject**  to ensure that Qt can clean up after the drag and drop
    operation has been completed.

    A pixmap can be used to represent the data while the drag is in progress,
    and will move with the cursor to the drop target. This pixmap typically
    shows an icon that represents the MIME type of the data being transferred,
    but any pixmap can be set with **setPixmap** (). The cursor's hot spot can
    be given a position relative to the top-left corner of the pixmap with the
    **setHotSpot** () function. The following code positions the pixmap so that
    the cursor's hot spot points to the center of its bottom edge:

    drag->setHotSpot(**QPoint** (drag->pixmap().width()/2,
    drag->pixmap().height()));

    **Note:** On X11, the pixmap may not be able to keep up with the mouse
    movements if the hot spot causes the pixmap to be displayed directly under
    the cursor.

    The source and target widgets can be found with **source** () and **target**
    (). These functions are often used to determine whether drag and drop
    operations started and finished at the same widget, so that special behavior
    can be implemented.

    QDrag only deals with the drag and drop operation itself. It is up to the
    developer to decide when a drag operation begins, and how a QDrag object
    should be constructed and used. For a given widget, it is often necessary to
    reimplement **mousePressEvent** () to determine whether the user has pressed
    a mouse button, and reimplement **mouseMoveEvent** () to check whether a
    QDrag is required.

    **See also** **Drag and Drop** , **QClipboard** , **QMimeData** ,
    **Draggable Icons Example** , **Draggable Text Example** , **Drop Site
    Example** , and **Fridge Magnets Example** .
    """

    def __init__(self, dragSource: PySide6.QtCore.QObject) -> None:
        """
        https://doc.qt.io/qt-6/qdrag.html#QDrag

        **QDrag::QDrag(QObject * dragSource )**

        Constructs a new drag object for the widget specified by **dragSource**.
        """
        ...
    @staticmethod
    def cancel() -> None:
        """
        https://doc.qt.io/qt-6/qdrag.html#cancel

        **[static, since 5.7] void QDrag::cancel()**

        Cancels a drag operation initiated by Qt.

        **Note:** This is currently implemented on Windows and X11.

        This function was introduced in Qt 5.7.

        **See also** **exec** ().
        """
        ...
    def defaultAction(self) -> PySide6.QtCore.Qt.DropAction:
        """
        https://doc.qt.io/qt-6/qdrag.html#defaultAction

        **Qt::DropAction QDrag::defaultAction() const**

        Returns the default proposed drop action for this drag operation.

        **See also** **exec** () and **supportedActions** ().
        """
        ...
    def dragCursor(self, action: PySide6.QtCore.Qt.DropAction) -> PySide6.QtGui.QPixmap:
        """
        https://doc.qt.io/qt-6/qdrag.html#dragCursor

        **[since 5.0] QPixmap QDrag::dragCursor(Qt::DropAction action ) const**

        Returns the drag cursor for the **action**.

        This function was introduced in Qt 5.0.

        **See also** **setDragCursor** ().
        """
        ...
    @overload
    def exec(
        self,
        supportedActions: PySide6.QtCore.Qt.DropActions,
        defaultAction: PySide6.QtCore.Qt.DropAction,
    ) -> PySide6.QtCore.Qt.DropAction:
        """
        https://doc.qt.io/qt-6/qdrag.html#exec

        **Qt::DropAction QDrag::exec(Qt::DropActions supportedActions =
        Qt::MoveAction)**

        Starts the drag and drop operation and returns a value indicating the
        requested drop action when it is completed. The drop actions that the
        user can choose from are specified in **supportedActions**. The default
        proposed action will be selected among the allowed actions in the
        following order: Move, Copy and Link.

        **Note:** On Linux and macOS, the drag and drop operation can take some
        time, but this function does not block the event loop. Other events are
        still delivered to the application while the operation is performed. On
        Windows, the Qt event loop is blocked during the operation.

        **See also** **cancel** ().
        """
        ...
    @overload
    def exec(
        self, supportedActions: PySide6.QtCore.Qt.DropActions = ...
    ) -> PySide6.QtCore.Qt.DropAction:
        """
        https://doc.qt.io/qt-6/qdrag.html#exec-1

        **Qt::DropAction QDrag::exec(Qt::DropActions supportedActions ,
        Qt::DropAction defaultDropAction )**

        Starts the drag and drop operation and returns a value indicating the
        requested drop action when it is completed. The drop actions that the
        user can choose from are specified in **supportedActions**.

        The **defaultDropAction** determines which action will be proposed when
        the user performs a drag without using modifier keys.

        **Note:** On Linux and macOS, the drag and drop operation can take some
        time, but this function does not block the event loop. Other events are
        still delivered to the application while the operation is performed. On
        Windows, the Qt event loop is blocked during the operation. However,
        **QDrag::exec** () on Windows causes processEvents() to be called
        frequently to keep the GUI responsive. If any loops or operations are
        called while a drag operation is active, it will block the drag
        operation.
        """
        ...
    @overload
    def exec_(
        self,
        arg__1: PySide6.QtCore.Qt.DropActions,
        arg__2: PySide6.QtCore.Qt.DropAction,
    ) -> PySide6.QtCore.Qt.DropAction:
        """
        https://doc.qt.io/qt-6/qdrag.html#exec

        **Qt::DropAction QDrag::exec(Qt::DropActions supportedActions =
        Qt::MoveAction)**

        Starts the drag and drop operation and returns a value indicating the
        requested drop action when it is completed. The drop actions that the
        user can choose from are specified in **supportedActions**. The default
        proposed action will be selected among the allowed actions in the
        following order: Move, Copy and Link.

        **Note:** On Linux and macOS, the drag and drop operation can take some
        time, but this function does not block the event loop. Other events are
        still delivered to the application while the operation is performed. On
        Windows, the Qt event loop is blocked during the operation.

        **See also** **cancel** ().
        """
        ...
    @overload
    def exec_(
        self, supportedActions: PySide6.QtCore.Qt.DropActions = ...
    ) -> PySide6.QtCore.Qt.DropAction:
        """
        https://doc.qt.io/qt-6/qdrag.html#exec

        **Qt::DropAction QDrag::exec(Qt::DropActions supportedActions =
        Qt::MoveAction)**

        Starts the drag and drop operation and returns a value indicating the
        requested drop action when it is completed. The drop actions that the
        user can choose from are specified in **supportedActions**. The default
        proposed action will be selected among the allowed actions in the
        following order: Move, Copy and Link.

        **Note:** On Linux and macOS, the drag and drop operation can take some
        time, but this function does not block the event loop. Other events are
        still delivered to the application while the operation is performed. On
        Windows, the Qt event loop is blocked during the operation.

        **See also** **cancel** ().
        """
        ...
    def hotSpot(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qdrag.html#hotSpot

        **QPoint QDrag::hotSpot() const**

        Returns the position of the hot spot relative to the top-left corner of
        the cursor.

        **See also** **setHotSpot** ().
        """
        ...
    def mimeData(self) -> PySide6.QtCore.QMimeData:
        """
        https://doc.qt.io/qt-6/qdrag.html#mimeData

        **QMimeData *QDrag::mimeData() const**

        Returns the MIME data that is encapsulated by the drag object.

        **See also** **setMimeData** ().
        """
        ...
    def pixmap(self) -> PySide6.QtGui.QPixmap:
        """
        https://doc.qt.io/qt-6/qdrag.html#pixmap

        **QPixmap QDrag::pixmap() const**

        Returns the pixmap used to represent the data in a drag and drop
        operation.

        **See also** **setPixmap** ().
        """
        ...
    def setDragCursor(
        self,
        cursor: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage | str,
        action: PySide6.QtCore.Qt.DropAction,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdrag.html#setDragCursor

        **void QDrag::setDragCursor(const QPixmap & cursor , Qt::DropAction
        action )**

        Sets the drag **cursor** for the **action**. This allows you to override
        the default native cursors. To revert to using the native cursor for
        **action** pass in a null **QPixmap**  as **cursor**.

        Note: setting the drag cursor for IgnoreAction may not work on all
        platforms. X11 and macOS has been tested to work. Windows does not
        support it.

        **See also** **dragCursor** ().
        """
        ...
    def setHotSpot(self, hotspot: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/qdrag.html#setHotSpot

        **void QDrag::setHotSpot(const QPoint & hotspot )**

        Sets the position of the hot spot relative to the top-left corner of the
        pixmap used to the point specified by **hotspot**.

        **Note:** on X11, the pixmap may not be able to keep up with the mouse
        movements if the hot spot causes the pixmap to be displayed directly
        under the cursor.

        **See also** **hotSpot** ().
        """
        ...
    def setMimeData(self, data: PySide6.QtCore.QMimeData) -> None:
        """
        https://doc.qt.io/qt-6/qdrag.html#setMimeData

        **void QDrag::setMimeData(QMimeData * data )**

        Sets the data to be sent to the given MIME **data**. Ownership of the
        data is transferred to the **QDrag**  object.

        **See also** **mimeData** ().
        """
        ...
    def setPixmap(
        self, arg__1: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage | str
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdrag.html#setPixmap

        **void QDrag::setPixmap(const QPixmap & pixmap )**

        Sets **pixmap** as the pixmap used to represent the data in a drag and
        drop operation. You can only set a pixmap before the drag is started.

        **See also** **pixmap** ().
        """
        ...
    def source(self) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qdrag.html#source

        **QObject *QDrag::source() const**

        Returns the source of the drag object. This is the widget where the drag
        and drop operation originated.
        """
        ...
    def supportedActions(self) -> PySide6.QtCore.Qt.DropActions:
        """
        https://doc.qt.io/qt-6/qdrag.html#supportedActions

        **Qt::DropActions QDrag::supportedActions() const**

        Returns the set of possible drop actions for this drag operation.

        **See also** **exec** () and **defaultAction** ().
        """
        ...
    def target(self) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qdrag.html#target

        **QObject *QDrag::target() const**

        Returns the target of the drag and drop operation. This is the widget
        where the drag object was dropped.
        """
        ...
    @property
    def actionChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdrag.html#actionChanged

        **[signal] void QDrag::actionChanged(Qt::DropAction action )**

        This signal is emitted when the **action** associated with the drag
        changes.

        **See also** **targetChanged** ().
        """
        ...
    @property
    def targetChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdrag.html#targetChanged

        **[signal] void QDrag::targetChanged(QObject * newTarget )**

        This signal is emitted when the target of the drag and drop operation
        changes, with **newTarget** the new target.

        **See also** **target** () and **actionChanged** ().
        """
        ...
