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

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QMdiSubWindow(PySide6.QtWidgets.QWidget):
    """
    https://doc.qt.io/qt-6/qmdisubwindow.html

    **Detailed Description**

    QMdiSubWindow represents a top-level window in a **QMdiArea** , and consists
    of a title bar with window decorations, an internal widget, and (depending
    on the current style) a window frame and a size grip. QMdiSubWindow has its
    own layout, which consists of the title bar and a center area for the
    internal widget.

    ![](images/qmdisubwindowlayout.png)

    The most common way to construct a QMdiSubWindow is to call
    **QMdiArea::addSubWindow** () with the internal widget as the argument. You
    can also create a subwindow yourself, and set an internal widget by calling
    **setWidget** ().

    You use the same API when programming with subwindows as with regular top-
    level windows (e.g., you can call functions such as **show** (), **hide**
    (), **showMaximized** (), and **setWindowTitle** ()).

    **Subwindow Handling**

    QMdiSubWindow also supports behavior specific to subwindows in an MDI area.

    By default, each QMdiSubWindow is visible inside the MDI area viewport when
    moved around, but it is also possible to specify transparent window movement
    and resizing behavior, where only the outline of a subwindow is updated
    during these operations. The **setOption** () function is used to enable
    this behavior.

    The **isShaded** () function detects whether the subwindow is currently
    shaded (i.e., the window is collapsed so that only the title bar is
    visible). To enter shaded mode, call **showShaded** (). QMdiSubWindow emits
    the **windowStateChanged** () signal whenever the window state has changed
    (e.g., when the window becomes minimized, or is restored). It also emits
    **aboutToActivate** () before it is activated.

    In keyboard-interactive mode, the windows are moved and resized with the
    keyboard. You can enter this mode through the system menu of the window. The
    **keyboardSingleStep**  and **keyboardPageStep**  properties control the
    distance the widget is moved or resized for each keypress event. When shift
    is pressed down page step is used; otherwise single step is used.

    You can also change the active window with the keyboard. By pressing the
    control and tab keys at the same time, the next (using the current
    **WindowOrder** ) subwindow will be activated. By pressing control, shift,
    and tab, you will activate the previous window. This is equivalent to
    calling **activateNextSubWindow** () and **activatePreviousSubWindow** ().
    Note that these shortcuts overrides global shortcuts, but not the
    **QMdiArea** s shortcuts.

    **See also** **QMdiArea** .
    """

    AllowOutsideAreaHorizontally: QMdiSubWindow.SubWindowOption = ...
    AllowOutsideAreaVertically: QMdiSubWindow.SubWindowOption = ...
    RubberBandResize: QMdiSubWindow.SubWindowOption = ...
    RubberBandMove: QMdiSubWindow.SubWindowOption = ...

    class SubWindowOption(IntFlag):
        AllowOutsideAreaHorizontally: QMdiSubWindow.SubWindowOption = ...
        AllowOutsideAreaVertically: QMdiSubWindow.SubWindowOption = ...
        RubberBandResize: QMdiSubWindow.SubWindowOption = ...
        RubberBandMove: QMdiSubWindow.SubWindowOption = ...

    class SubWindowOptions: ...

    def __init__(
        self,
        parent: PySide6.QtWidgets.QWidget | None = ...,
        flags: PySide6.QtCore.Qt.WindowFlags = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#QMdiSubWindow

        **QMdiSubWindow::QMdiSubWindow(QWidget * parent = nullptr,
        Qt::WindowFlags flags = Qt::WindowFlags())**

        Constructs a new QMdiSubWindow widget. The **parent** and **flags**
        arguments are passed to **QWidget** 's constructor.

        Instead of using addSubWindow(), it is also simply possible to use
        **setParent** () when you add the subwindow to a **QMdiArea** .

        Note that only **QMdiSubWindow** s can be set as children of
        **QMdiArea** ; you cannot, for instance, write:

        //bad code
            **QMdiArea**  mdiArea;
            **QTextEdit**
        editor(&mdiArea); // invalid child widget

        **See also** **QMdiArea::addSubWindow** ().
        """
        ...
    def changeEvent(self, changeEvent: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#changeEvent

        **[override virtual protected] void QMdiSubWindow::changeEvent(QEvent *
        changeEvent )**

        Reimplements: **QWidget::changeEvent** (QEvent *event).
        """
        ...
    def childEvent(self, childEvent: PySide6.QtCore.QChildEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#childEvent

        **[override virtual protected] void
        QMdiSubWindow::childEvent(QChildEvent * childEvent )**

        Reimplements: **QObject::childEvent** (QChildEvent *event).
        """
        ...
    def closeEvent(self, closeEvent: PySide6.QtGui.QCloseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#closeEvent

        **[override virtual protected] void
        QMdiSubWindow::closeEvent(QCloseEvent * closeEvent )**

        Reimplements: **QWidget::closeEvent** (QCloseEvent *event).
        """
        ...
    def contextMenuEvent(self, contextMenuEvent: PySide6.QtGui.QContextMenuEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#contextMenuEvent

        **[override virtual protected] void
        QMdiSubWindow::contextMenuEvent(QContextMenuEvent * contextMenuEvent )**

        Reimplements: **QWidget::contextMenuEvent** (QContextMenuEvent *event).
        """
        ...
    def event(self, event: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#event

        **[override virtual protected] bool QMdiSubWindow::event(QEvent * event
        )**

        Reimplements: **QWidget::event** (QEvent *event).
        """
        ...
    def eventFilter(
        self, object: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#eventFilter

        **[override virtual protected] bool QMdiSubWindow::eventFilter(QObject *
        object , QEvent * event )**

        Reimplements: **QObject::eventFilter** (QObject *watched, QEvent
        *event).
        """
        ...
    def focusInEvent(self, focusInEvent: PySide6.QtGui.QFocusEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#focusInEvent

        **[override virtual protected] void
        QMdiSubWindow::focusInEvent(QFocusEvent * focusInEvent )**

        Reimplements: **QWidget::focusInEvent** (QFocusEvent *event).
        """
        ...
    def focusOutEvent(self, focusOutEvent: PySide6.QtGui.QFocusEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#focusOutEvent

        **[override virtual protected] void
        QMdiSubWindow::focusOutEvent(QFocusEvent * focusOutEvent )**

        Reimplements: **QWidget::focusOutEvent** (QFocusEvent *event).
        """
        ...
    def hideEvent(self, hideEvent: PySide6.QtGui.QHideEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#hideEvent

        **[override virtual protected] void QMdiSubWindow::hideEvent(QHideEvent
        * hideEvent )**

        Reimplements: **QWidget::hideEvent** (QHideEvent *event).
        """
        ...
    def isShaded(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#isShaded

        **bool QMdiSubWindow::isShaded() const**

        Returns `true` if this window is shaded; otherwise returns `false`.

        A window is shaded if it is collapsed so that only the title bar is
        visible.
        """
        ...
    def keyPressEvent(self, keyEvent: PySide6.QtGui.QKeyEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#keyPressEvent

        **[override virtual protected] void
        QMdiSubWindow::keyPressEvent(QKeyEvent * keyEvent )**

        Reimplements: **QWidget::keyPressEvent** (QKeyEvent *event).
        """
        ...
    def keyboardPageStep(self) -> int:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#keyboardPageStep-prop

        **keyboardPageStep : int**

        sets how far a widget should move or resize when using the keyboard page
        keys.

        When in keyboard-interactive mode, you can use the arrow and page keys
        to either move or resize the window. This property controls the page
        keys. The common way to enter keyboard interactive mode is to enter the
        subwindow menu, and select either "resize" or "move".

        The default keyboard page step value is 20 pixels.

        **Access functions:**

        int **keyboardPageStep** () const
        void **setKeyboardPageStep** (int
        **step** )

        **See also** **keyboardSingleStep** .
        """
        ...
    def keyboardSingleStep(self) -> int:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#keyboardSingleStep-prop

        **keyboardSingleStep : int**

        sets how far a widget should move or resize when using the keyboard
        arrow keys.

        When in keyboard-interactive mode, you can use the arrow and page keys
        to either move or resize the window. This property controls the arrow
        keys. The common way to enter keyboard interactive mode is to enter the
        subwindow menu, and select either "resize" or "move".

        The default keyboard single step value is 5 pixels.

        **Access functions:**

        int **keyboardSingleStep** () const
        void **setKeyboardSingleStep**
        (int **step** )

        **See also** **keyboardPageStep** .

        **Member Function Documentation**
        """
        ...
    def leaveEvent(self, leaveEvent: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#leaveEvent

        **[override virtual protected] void QMdiSubWindow::leaveEvent(QEvent *
        leaveEvent )**

        Reimplements: **QWidget::leaveEvent** (QEvent *event).
        """
        ...
    def maximizedButtonsWidget(self) -> PySide6.QtWidgets.QWidget: ...
    def maximizedSystemMenuIconWidget(self) -> PySide6.QtWidgets.QWidget: ...
    def mdiArea(self) -> PySide6.QtWidgets.QMdiArea:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#mdiArea

        **QMdiArea *QMdiSubWindow::mdiArea() const**

        Returns the area containing this sub-window, or `nullptr` if there is
        none.

        **See also** **QMdiArea::addSubWindow** ().
        """
        ...
    def minimumSizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#minimumSizeHint

        **[override virtual] QSize QMdiSubWindow::minimumSizeHint() const**

        Reimplements an access function for property:
        **QWidget::minimumSizeHint** .
        """
        ...
    def mouseDoubleClickEvent(self, mouseEvent: PySide6.QtGui.QMouseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#mouseDoubleClickEvent

        **[override virtual protected] void
        QMdiSubWindow::mouseDoubleClickEvent(QMouseEvent * mouseEvent )**

        Reimplements: **QWidget::mouseDoubleClickEvent** (QMouseEvent *event).
        """
        ...
    def mouseMoveEvent(self, mouseEvent: PySide6.QtGui.QMouseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#mouseMoveEvent

        **[override virtual protected] void
        QMdiSubWindow::mouseMoveEvent(QMouseEvent * mouseEvent )**

        Reimplements: **QWidget::mouseMoveEvent** (QMouseEvent *event).
        """
        ...
    def mousePressEvent(self, mouseEvent: PySide6.QtGui.QMouseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#mousePressEvent

        **[override virtual protected] void
        QMdiSubWindow::mousePressEvent(QMouseEvent * mouseEvent )**

        Reimplements: **QWidget::mousePressEvent** (QMouseEvent *event).
        """
        ...
    def mouseReleaseEvent(self, mouseEvent: PySide6.QtGui.QMouseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#mouseReleaseEvent

        **[override virtual protected] void
        QMdiSubWindow::mouseReleaseEvent(QMouseEvent * mouseEvent )**

        Reimplements: **QWidget::mouseReleaseEvent** (QMouseEvent *event).
        """
        ...
    def moveEvent(self, moveEvent: PySide6.QtGui.QMoveEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#moveEvent

        **[override virtual protected] void QMdiSubWindow::moveEvent(QMoveEvent
        * moveEvent )**

        Reimplements: **QWidget::moveEvent** (QMoveEvent *event).
        """
        ...
    def paintEvent(self, paintEvent: PySide6.QtGui.QPaintEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#paintEvent

        **[override virtual protected] void
        QMdiSubWindow::paintEvent(QPaintEvent * paintEvent )**

        Reimplements: **QWidget::paintEvent** (QPaintEvent *event).
        """
        ...
    def resizeEvent(self, resizeEvent: PySide6.QtGui.QResizeEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#resizeEvent

        **[override virtual protected] void
        QMdiSubWindow::resizeEvent(QResizeEvent * resizeEvent )**

        Reimplements: **QWidget::resizeEvent** (QResizeEvent *event).

        **Warning:** When maximizing or restoring a subwindow, the resulting
        call to this function may have an invalid **QResizeEvent::oldSize** ().
        """
        ...
    def setKeyboardPageStep(self, step: int) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#keyboardPageStep-prop

        **keyboardPageStep : int**

        sets how far a widget should move or resize when using the keyboard page
        keys.

        When in keyboard-interactive mode, you can use the arrow and page keys
        to either move or resize the window. This property controls the page
        keys. The common way to enter keyboard interactive mode is to enter the
        subwindow menu, and select either "resize" or "move".

        The default keyboard page step value is 20 pixels.

        **Access functions:**

        int **keyboardPageStep** () const
        void **setKeyboardPageStep** (int
        **step** )

        **See also** **keyboardSingleStep** .
        """
        ...
    def setKeyboardSingleStep(self, step: int) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#keyboardSingleStep-prop

        **keyboardSingleStep : int**

        sets how far a widget should move or resize when using the keyboard
        arrow keys.

        When in keyboard-interactive mode, you can use the arrow and page keys
        to either move or resize the window. This property controls the arrow
        keys. The common way to enter keyboard interactive mode is to enter the
        subwindow menu, and select either "resize" or "move".

        The default keyboard single step value is 5 pixels.

        **Access functions:**

        int **keyboardSingleStep** () const
        void **setKeyboardSingleStep**
        (int **step** )

        **See also** **keyboardPageStep** .

        **Member Function Documentation**
        """
        ...
    def setOption(
        self, option: PySide6.QtWidgets.QMdiSubWindow.SubWindowOption, on: bool = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#setOption

        **void QMdiSubWindow::setOption(QMdiSubWindow::SubWindowOption option ,
        bool on = true)**

        If **on** is true, **option** is enabled on the subwindow; otherwise it
        is disabled. See **SubWindowOption**  for the effect of each option.

        **See also** **SubWindowOption**  and **testOption** ().
        """
        ...
    def setSystemMenu(self, systemMenu: PySide6.QtWidgets.QMenu) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#setSystemMenu

        **void QMdiSubWindow::setSystemMenu(QMenu * systemMenu )**

        Sets **systemMenu** as the current system menu for this subwindow.

        By default, each **QMdiSubWindow**  has a standard system menu.

        QActions for the system menu created by **QMdiSubWindow**  will
        automatically be updated depending on the current window state; e.g.,
        the minimize action will be disabled after the window is minimized.

        QActions added by the user are not updated by **QMdiSubWindow** .

        **QMdiSubWindow**  takes ownership of **systemMenu** ; you do not have
        to delete it. Any existing menus will be deleted.

        **See also** **systemMenu** () and **showSystemMenu** ().
        """
        ...
    def setWidget(self, widget: PySide6.QtWidgets.QWidget) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#setWidget

        **void QMdiSubWindow::setWidget(QWidget * widget )**

        Sets **widget** as the internal widget of this subwindow. The internal
        widget is displayed in the center of the subwindow beneath the title
        bar.

        **QMdiSubWindow**  takes temporary ownership of **widget** ; you do not
        have to delete it. Any existing internal widget will be removed and
        reparented to the root window.

        **See also** **widget** ().
        """
        ...
    def showEvent(self, showEvent: PySide6.QtGui.QShowEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#showEvent

        **[override virtual protected] void QMdiSubWindow::showEvent(QShowEvent
        * showEvent )**

        Reimplements: **QWidget::showEvent** (QShowEvent *event).
        """
        ...
    def showShaded(self) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#showShaded

        **[slot] void QMdiSubWindow::showShaded()**

        Calling this function makes the subwindow enter the shaded mode. When
        the subwindow is shaded, only the title bar is visible.

        Although shading is not supported by all styles, this function will
        still show the subwindow as shaded, regardless of whether support for
        shading is available. However, when used with styles without shading
        support, the user will be unable to return from shaded mode through the
        user interface (e.g., through a shade button in the title bar).

        **See also** **isShaded** ().
        """
        ...
    def showSystemMenu(self) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#showSystemMenu

        **[slot] void QMdiSubWindow::showSystemMenu()**

        Shows the system menu below the system menu icon in the title bar.

        **See also** **setSystemMenu** () and **systemMenu** ().
        """
        ...
    def sizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#sizeHint

        **[override virtual] QSize QMdiSubWindow::sizeHint() const**

        Reimplements an access function for property: **QWidget::sizeHint** .
        """
        ...
    def systemMenu(self) -> PySide6.QtWidgets.QMenu:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#systemMenu

        **QMenu *QMdiSubWindow::systemMenu() const**

        Returns a pointer to the current system menu, or zero if no system menu
        is set. **QMdiSubWindow**  provides a default system menu, but you can
        also set the menu with **setSystemMenu** ().

        **See also** **setSystemMenu** () and **showSystemMenu** ().
        """
        ...
    def testOption(self, arg__1: PySide6.QtWidgets.QMdiSubWindow.SubWindowOption) -> bool:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#testOption

        **bool QMdiSubWindow::testOption(QMdiSubWindow::SubWindowOption option )
        const**

        Returns `true` if **option** is enabled; otherwise returns `false`.

        **See also** **SubWindowOption**  and **setOption** ().
        """
        ...
    def timerEvent(self, timerEvent: PySide6.QtCore.QTimerEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#timerEvent

        **[override virtual protected] void
        QMdiSubWindow::timerEvent(QTimerEvent * timerEvent )**

        Reimplements: **QObject::timerEvent** (QTimerEvent *event).
        """
        ...
    def widget(self) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#widget

        **QWidget *QMdiSubWindow::widget() const**

        Returns the current internal widget.

        **See also** **setWidget** ().
        """
        ...
    @property
    def aboutToActivate(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#aboutToActivate

        **[signal] void QMdiSubWindow::aboutToActivate()**

        **QMdiSubWindow**  emits this signal immediately before it is activated.
        After the subwindow has been activated, the **QMdiArea**  that manages
        the subwindow will also emit the **subWindowActivated** () signal.

        **See also** **QMdiArea::subWindowActivated** ().
        """
        ...
    @property
    def windowStateChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qmdisubwindow.html#windowStateChanged

        **[signal] void QMdiSubWindow::windowStateChanged(Qt::WindowStates
        oldState , Qt::WindowStates newState )**

        **QMdiSubWindow**  emits this signal after the window state changes.
        **oldState** is the window state before it changed, and **newState** is
        the new, current state.
        """
        ...
