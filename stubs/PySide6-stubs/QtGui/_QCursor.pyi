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

class QCursor:
    """
    https://doc.qt.io/qt-6/qcursor.html

    **Detailed Description**

    This class is mainly used to create mouse cursors that are associated with
    particular widgets and to get and set the position of the mouse cursor.

    Qt has a number of standard cursor shapes, but you can also make custom
    cursor shapes based on a **QBitmap** , a mask and a hotspot.

    To associate a cursor with a widget, use **QWidget::setCursor** (). To
    associate a cursor with all widgets (normally for a short period of time),
    use **QGuiApplication::setOverrideCursor** ().

    To set a cursor shape use **QCursor::setShape** () or use the QCursor
    constructor which takes the shape as argument, or you can use one of the
    predefined cursors defined in the **Qt::CursorShape**  enum.

    If you want to create a cursor with your own bitmap, either use the QCursor
    constructor which takes a bitmap and a mask or the constructor which takes a
    pixmap as arguments.

    To set or get the position of the mouse cursor use the static methods
    **QCursor::pos** () and **QCursor::setPos** ().

    **Note:** It is possible to create a QCursor before **QGuiApplication** ,
    but it is not useful except as a place-holder for a real QCursor created
    after **QGuiApplication** . Attempting to use a QCursor that was created
    before **QGuiApplication**  will result in a crash.

    **A Note for X11 Users**

    On X11, Qt supports the **Xcursor**  library, which allows for full color
    icon themes. The table below shows the cursor name used for each
    **Qt::CursorShape**  value. If a cursor cannot be found using the name shown
    below, a standard X11 cursor will be used instead. Note: X11 does not
    provide appropriate cursors for all possible **Qt::CursorShape**  values. It
    is possible that some cursors will be taken from the Xcursor theme, while
    others will use an internal bitmap cursor.

    Shape**Qt::CursorShape**  ValueCursor NameShape**Qt::CursorShape**
    ValueCursor Name
    ![](images/cursor-arrow.png)**Qt::ArrowCursor**
    `left_ptr`![](images/cursor-sizev.png)**Qt::SizeVerCursor** `size_ver`
    ![](images/cursor-uparrow.png)**Qt::UpArrowCursor**
    `up_arrow`![](images/cursor-sizeh.png)**Qt::SizeHorCursor** `size_hor`
    ![](images/cursor-cross.png)**Qt::CrossCursor** `cross`![](images/cursor-
    sizeb.png)**Qt::SizeBDiagCursor** `size_bdiag`
    ![](images/cursor-
    ibeam.png)**Qt::IBeamCursor** `ibeam`![](images/cursor-
    sizef.png)**Qt::SizeFDiagCursor** `size_fdiag`
    ![](images/cursor-
    wait.png)**Qt::WaitCursor** `wait`![](images/cursor-
    sizeall.png)**Qt::SizeAllCursor** `size_all`
    ![](images/cursor-
    busy.png)**Qt::BusyCursor** `left_ptr_watch`![](images/cursor-
    vsplit.png)**Qt::SplitVCursor** `split_v`
    ![](images/cursor-
    forbidden.png)**Qt::ForbiddenCursor** `forbidden`![](images/cursor-
    hsplit.png)**Qt::SplitHCursor** `split_h`
    ![](images/cursor-
    hand.png)**Qt::PointingHandCursor** `pointing_hand`![](images/cursor-
    openhand.png)**Qt::OpenHandCursor** `openhand`
    ![](images/cursor-
    whatsthis.png)**Qt::WhatsThisCursor** `whats_this`![](images/cursor-
    closedhand.png)**Qt::ClosedHandCursor** `closedhand`
    **Qt::DragMoveCursor** `dnd-move` or `move`**Qt::DragCopyCursor** `dnd-copy`
    or `copy`
    **Qt::DragLinkCursor** `dnd-link` or `link`

    **See also** **QWidget**  and **GUI Design Handbook: Cursors** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qcursor.html#QCursor

        **QCursor::QCursor()**

        Constructs a cursor with the default arrow shape.
        """
        ...
    @overload
    def __init__(
        self,
        bitmap: PySide6.QtGui.QBitmap | str,
        mask: PySide6.QtGui.QBitmap | str,
        hotX: int = ...,
        hotY: int = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcursor.html#QCursor-1

        **QCursor::QCursor(Qt::CursorShape shape )**

        Constructs a cursor with the specified **shape**.

        See **Qt::CursorShape**  for a list of shapes.

        **See also** **setShape** ().
        """
        ...
    @overload
    def __init__(
        self,
        cursor: (
            PySide6.QtGui.QCursor | PySide6.QtCore.Qt.CursorShape | PySide6.QtGui.QPixmap
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcursor.html#QCursor-2

        **QCursor::QCursor(const QBitmap & bitmap , const QBitmap & mask , int
        hotX = -1, int hotY = -1)**

        Constructs a custom bitmap cursor.

        **bitmap** and **mask** make up the bitmap. **hotX** and **hotY** define
        the cursor's hot spot.

        If **hotX** is negative, it is set to the `bitmap().width()/2`. If
        **hotY** is negative, it is set to the `bitmap().height()/2`.

        The cursor **bitmap** (B) and **mask** (M) bits are combined like this:

        * B=1 and M=1 gives black.
          * B=0 and M=1 gives white.
          * B=0 and M=0
        gives transparent.
          * B=1 and M=0 gives an XOR'd result under Windows,
        undefined results on all other platforms.

        Use the global Qt color **Qt::color0**  to draw 0-pixels and
        **Qt::color1**  to draw 1-pixels in the bitmaps.

        Valid cursor sizes depend on the display hardware (or the underlying
        window system). We recommend using 32 x 32 cursors, because this size is
        supported on all platforms. Some platforms also support 16 x 16, 48 x
        48, and 64 x 64 cursors.

        **See also** **QBitmap::QBitmap** () and **QBitmap::setMask** ().
        """
        ...
    @overload
    def __init__(
        self,
        pixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage | str,
        hotX: int = ...,
        hotY: int = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcursor.html#QCursor-3

        **QCursor::QCursor(const QPixmap & pixmap , int hotX = -1, int hotY =
        -1)**

        Constructs a custom pixmap cursor.

        **pixmap** is the image. It is usual to give it a mask (set using
        **QPixmap::setMask** ()). **hotX** and **hotY** define the cursor's hot
        spot.

        If **hotX** is negative, it is set to the `pixmap().width()/2`. If
        **hotY** is negative, it is set to the `pixmap().height()/2`.

        Valid cursor sizes depend on the display hardware (or the underlying
        window system). We recommend using 32 x 32 cursors, because this size is
        supported on all platforms. Some platforms also support 16 x 16, 48 x
        48, and 64 x 64 cursors.

        **See also** **QPixmap::QPixmap** () and **QPixmap::setMask** ().
        """
        ...
    @overload
    def __init__(self, shape: PySide6.QtCore.Qt.CursorShape) -> None:
        """
        https://doc.qt.io/qt-6/qcursor.html#QCursor-4

        **QCursor::QCursor(const QCursor & c )**

        Constructs a copy of the cursor **c**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(
        self, outS: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(
        self, inS: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    @overload
    def bitmap(self) -> PySide6.QtGui.QBitmap:
        """
        https://doc.qt.io/qt-6/qcursor.html#bitmap-1

        **QBitmap QCursor::bitmap() const**

        Returns the cursor bitmap, or a null bitmap if it is one of the standard
        cursors.
        """
        ...
    @overload
    def bitmap(
        self, arg__1: PySide6.QtCore.Qt.ReturnByValueConstant
    ) -> PySide6.QtGui.QBitmap:
        """
        https://doc.qt.io/qt-6/qcursor.html#bitmap-1

        **QBitmap QCursor::bitmap() const**

        Returns the cursor bitmap, or a null bitmap if it is one of the standard
        cursors.
        """
        ...
    def hotSpot(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qcursor.html#hotSpot

        **QPoint QCursor::hotSpot() const**

        Returns the cursor hot spot, or (0, 0) if it is one of the standard
        cursors.
        """
        ...
    @overload
    def mask(self) -> PySide6.QtGui.QBitmap:
        """
        https://doc.qt.io/qt-6/qcursor.html#mask-1

        **QBitmap QCursor::mask() const**

        Returns the cursor bitmap mask, or a null bitmap if it is one of the
        standard cursors.
        """
        ...
    @overload
    def mask(
        self, arg__1: PySide6.QtCore.Qt.ReturnByValueConstant
    ) -> PySide6.QtGui.QBitmap:
        """
        https://doc.qt.io/qt-6/qcursor.html#mask-1

        **QBitmap QCursor::mask() const**

        Returns the cursor bitmap mask, or a null bitmap if it is one of the
        standard cursors.
        """
        ...
    def pixmap(self) -> PySide6.QtGui.QPixmap:
        """
        https://doc.qt.io/qt-6/qcursor.html#pixmap

        **QPixmap QCursor::pixmap() const**

        Returns the cursor pixmap. This is only valid if the cursor is a pixmap
        cursor.
        """
        ...
    @overload
    @staticmethod
    def pos() -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qcursor.html#pos

        **[static] QPoint QCursor::pos()**

        Returns the position of the cursor (hot spot) of the primary screen in
        global screen coordinates.

        You can call **QWidget::mapFromGlobal** () to translate it to widget
        coordinates.

        **Note:** The position is queried from the windowing system. If mouse
        events are generated via other means (e.g., via QWindowSystemInterface
        in a unit test), those fake mouse moves will not be reflected in the
        returned value.

        **Note:** On platforms where there is no windowing system or cursors are
        not available, the returned position is based on the mouse move events
        generated via QWindowSystemInterface.

        **See also** **setPos** (), **QWidget::mapFromGlobal** (),
        **QWidget::mapToGlobal** (), and **QGuiApplication::primaryScreen** ().
        """
        ...
    @overload
    @staticmethod
    def pos(screen: PySide6.QtGui.QScreen) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qcursor.html#pos-1

        **[static] QPoint QCursor::pos(const QScreen * screen )**

        Returns the position of the cursor (hot spot) of the **screen** in
        global screen coordinates.

        You can call **QWidget::mapFromGlobal** () to translate it to widget
        coordinates.

        **See also** **setPos** (), **QWidget::mapFromGlobal** (), and
        **QWidget::mapToGlobal** ().
        """
        ...
    @overload
    @staticmethod
    def setPos(p: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/qcursor.html#setPos

        **[static] void QCursor::setPos(int x , int y )**

        Moves the cursor (hot spot) of the primary screen to the global screen
        position ( **x** , **y** ).

        You can call **QWidget::mapToGlobal** () to translate widget coordinates
        to global screen coordinates.

        **See also** **pos** (), **QWidget::mapFromGlobal** (),
        **QWidget::mapToGlobal** (), and **QGuiApplication::primaryScreen** ().
        """
        ...
    @overload
    @staticmethod
    def setPos(screen: PySide6.QtGui.QScreen, p: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/qcursor.html#setPos-1

        **[static] void QCursor::setPos(QScreen * screen , int x , int y )**

        Moves the cursor (hot spot) of the **screen** to the global screen
        position ( **x** , **y** ).

        You can call **QWidget::mapToGlobal** () to translate widget coordinates
        to global screen coordinates.

        **Note:** Calling this function results in changing the cursor position
        through the windowing system. The windowing system will typically
        respond by sending mouse events to the application's window. This means
        that the usage of this function should be avoided in unit tests and
        everywhere where fake mouse events are being injected via
        QWindowSystemInterface because the windowing system's mouse state (with
        regards to buttons for example) may not match the state in the
        application-generated events.

        **Note:** On platforms where there is no windowing system or cursors are
        not available, this function may do nothing.

        **See also** **pos** (), **QWidget::mapFromGlobal** (), and
        **QWidget::mapToGlobal** ().
        """
        ...
    @overload
    @staticmethod
    def setPos(screen: PySide6.QtGui.QScreen, x: int, y: int) -> None:
        """
        https://doc.qt.io/qt-6/qcursor.html#setPos-2

        **[static] void QCursor::setPos(const QPoint & p )**

        This is an overloaded function.

        Moves the cursor (hot spot) to the global screen position at point
        **p**.
        """
        ...
    @overload
    @staticmethod
    def setPos(x: int, y: int) -> None:
        """
        https://doc.qt.io/qt-6/qcursor.html#setPos-3

        **[static] void QCursor::setPos(QScreen * screen , const QPoint & p )**

        This is an overloaded function.

        Moves the cursor (hot spot) to the global screen position of the
        **screen** at point **p**.
        """
        ...
    def setShape(self, newShape: PySide6.QtCore.Qt.CursorShape) -> None:
        """
        https://doc.qt.io/qt-6/qcursor.html#setShape

        **void QCursor::setShape(Qt::CursorShape shape )**

        Sets the cursor to the shape identified by **shape**.

        See **Qt::CursorShape**  for the list of cursor shapes.

        **See also** **shape** ().
        """
        ...
    def shape(self) -> PySide6.QtCore.Qt.CursorShape:
        """
        https://doc.qt.io/qt-6/qcursor.html#shape

        **Qt::CursorShape QCursor::shape() const**

        Returns the cursor shape identifier.

        **See also** **setShape** ().
        """
        ...
    def swap(
        self,
        other: (
            PySide6.QtGui.QCursor | PySide6.QtCore.Qt.CursorShape | PySide6.QtGui.QPixmap
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcursor.html#swap

        **[since 5.7] void QCursor::swap(QCursor & other )**

        Swaps this cursor with the **other** cursor.

        This function was introduced in Qt 5.7.
        """
        ...
