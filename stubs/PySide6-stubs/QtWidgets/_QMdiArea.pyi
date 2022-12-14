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

class QMdiArea(PySide6.QtWidgets.QAbstractScrollArea):
    """
    https://doc.qt.io/qt-6/qmdiarea.html

    **Detailed Description**

    QMdiArea functions, essentially, like a window manager for MDI windows. For
    instance, it draws the windows it manages on itself and arranges them in a
    cascading or tile pattern. QMdiArea is commonly used as the center widget in
    a **QMainWindow**  to create MDI applications, but can also be placed in any
    layout. The following code adds an area to a main window:

    **QMainWindow**  *mainWindow = new **QMainWindow** ;
    mainWindow->setCentralWidget(mdiArea);

    Unlike the window managers for top-level windows, all window flags
    (**Qt::WindowFlags** ) are supported by QMdiArea as long as the flags are
    supported by the current widget style. If a specific flag is not supported
    by the style (e.g., the **WindowShadeButtonHint** ), you can still shade the
    window with showShaded().

    Subwindows in QMdiArea are instances of **QMdiSubWindow** . They are added
    to an MDI area with **addSubWindow** (). It is common to pass a **QWidget**
    , which is set as the internal widget, to this function, but it is also
    possible to pass a **QMdiSubWindow**  directly. The class inherits
    **QWidget** , and you can use the same API as with a normal top-level window
    when programming. **QMdiSubWindow**  also has behavior that is specific to
    MDI windows. See the **QMdiSubWindow**  class description for more details.

    A subwindow becomes active when it gets the keyboard focus, or when
    **setFocus** () is called. The user activates a window by moving focus in
    the usual ways. The MDI area emits the **subWindowActivated** () signal when
    the active window changes, and the **activeSubWindow** () function returns
    the active subwindow.

    The convenience function **subWindowList** () returns a list of all
    subwindows. This information could be used in a popup menu containing a list
    of windows, for example.

    The subwindows are sorted by the current **WindowOrder** . This is used for
    the **subWindowList** () and for **activateNextSubWindow** () and
    **activatePreviousSubWindow** (). Also, it is used when cascading or tiling
    the windows with **cascadeSubWindows** () and **tileSubWindows** ().

    QMdiArea provides two built-in layout strategies for subwindows:
    **cascadeSubWindows** () and **tileSubWindows** (). Both are slots and are
    easily connected to menu entries.

    ![](images/mdi-cascade.png)![](images/mdi-tile.png)

    **Note:** The default scroll bar property for QMdiArea is
    **Qt::ScrollBarAlwaysOff** .

    **See also** **QMdiSubWindow** .
    """

    DontMaximizeSubWindowOnActivation: QMdiArea.AreaOption = ...
    SubWindowView: QMdiArea.ViewMode = ...
    TabbedView: QMdiArea.ViewMode = ...
    CreationOrder: QMdiArea.WindowOrder = ...
    StackingOrder: QMdiArea.WindowOrder = ...
    ActivationHistoryOrder: QMdiArea.WindowOrder = ...

    class AreaOption(IntFlag):
        DontMaximizeSubWindowOnActivation: QMdiArea.AreaOption = ...

    class AreaOptions: ...

    class ViewMode(IntFlag):
        SubWindowView: QMdiArea.ViewMode = ...
        TabbedView: QMdiArea.ViewMode = ...

    class WindowOrder(IntFlag):
        CreationOrder: QMdiArea.WindowOrder = ...
        StackingOrder: QMdiArea.WindowOrder = ...
        ActivationHistoryOrder: QMdiArea.WindowOrder = ...
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#QMdiArea

        **QMdiArea::QMdiArea(QWidget * parent = nullptr)**

        Constructs an empty mdi area. **parent** is passed to **QWidget** 's
        constructor.
        """
        ...
    def activateNextSubWindow(self) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#activateNextSubWindow

        **[slot] void QMdiArea::activateNextSubWindow()**

        Gives the keyboard focus to another window in the list of child windows.
        The window activated will be the next one determined by the current
        **activation order** .

        **See also** **activatePreviousSubWindow** () and
        **QMdiArea::WindowOrder** .
        """
        ...
    def activatePreviousSubWindow(self) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#activatePreviousSubWindow

        **[slot] void QMdiArea::activatePreviousSubWindow()**

        Gives the keyboard focus to another window in the list of child windows.
        The window activated will be the previous one determined by the current
        **activation order** .

        **See also** **activateNextSubWindow** () and **QMdiArea::WindowOrder**
        .
        """
        ...
    def activationOrder(self) -> PySide6.QtWidgets.QMdiArea.WindowOrder:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#activationOrder-prop

        **activationOrder : WindowOrder**

        This property holds the ordering criteria for subwindow lists

        This property specifies the ordering criteria for the list of subwindows
        returned by **subWindowList** (). By default, it is the window creation
        order.

        **Access functions:**

        QMdiArea::WindowOrder **activationOrder** () const
        void
        **setActivationOrder** (QMdiArea::WindowOrder **order** )

        **See also** **subWindowList** ().
        """
        ...
    def activeSubWindow(self) -> PySide6.QtWidgets.QMdiSubWindow:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#activeSubWindow

        **QMdiSubWindow *QMdiArea::activeSubWindow() const**

        Returns a pointer to the current active subwindow. If no window is
        currently active, `nullptr` is returned.

        Subwindows are treated as top-level windows with respect to window
        state, i.e., if a widget outside the MDI area is the active window, no
        subwindow will be active. Note that if a widget in the window in which
        the MDI area lives gains focus, the window will be activated.

        **See also** **setActiveSubWindow** () and **Qt::WindowState** .
        """
        ...
    def addSubWindow(
        self,
        widget: PySide6.QtWidgets.QWidget,
        flags: PySide6.QtCore.Qt.WindowFlags = ...,
    ) -> PySide6.QtWidgets.QMdiSubWindow:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#addSubWindow

        **QMdiSubWindow *QMdiArea::addSubWindow(QWidget * widget ,
        Qt::WindowFlags windowFlags = Qt::WindowFlags())**

        Adds **widget** as a new subwindow to the MDI area. If **windowFlags**
        are non-zero, they will override the flags set on the widget.

        The **widget** can be either a **QMdiSubWindow**  or another **QWidget**
        (in which case the MDI area will create a subwindow and set the
        **widget** as the internal widget).

        **Note:** Once the subwindow has been added, its parent will be the
        **viewport widget** of the **QMdiArea** .

        **QMdiArea**  mdiArea;
                **QMdiSubWindow**  *subWindow1 = new
        **QMdiSubWindow** ;
                subWindow1->setWidget(internalWidget1);
        subWindow1->setAttribute(Qt::WA_DeleteOnClose);
        mdiArea.addSubWindow(subWindow1);

                **QMdiSubWindow**
        *subWindow2 =
                    mdiArea.addSubWindow(internalWidget2);

        When you create your own subwindow, you must set the
        **Qt::WA_DeleteOnClose**  widget attribute if you want the window to be
        deleted when closed in the MDI area. If not, the window will be hidden
        and the MDI area will not activate the next subwindow.

        Returns the **QMdiSubWindow**  that is added to the MDI area.

        **See also** **removeSubWindow** ().
        """
        ...
    def background(self) -> PySide6.QtGui.QBrush:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#background-prop

        **background : QBrush**

        This property holds the background brush for the workspace

        This property sets the background brush for the workspace area itself.
        By default, it is a gray color, but can be any brush (e.g., colors,
        gradients or pixmaps).

        **Access functions:**

        QBrush **background** () const
        void **setBackground** (const QBrush &
        **background** )
        """
        ...
    def cascadeSubWindows(self) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#cascadeSubWindows

        **[slot] void QMdiArea::cascadeSubWindows()**

        Arranges all the child windows in a cascade pattern.

        **See also** **tileSubWindows** ().
        """
        ...
    def childEvent(self, childEvent: PySide6.QtCore.QChildEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#childEvent

        **[override virtual protected] void QMdiArea::childEvent(QChildEvent *
        childEvent )**

        Reimplements: **QObject::childEvent** (QChildEvent *event).
        """
        ...
    def closeActiveSubWindow(self) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#closeActiveSubWindow

        **[slot] void QMdiArea::closeActiveSubWindow()**

        Closes the active subwindow.

        **See also** **closeAllSubWindows** ().
        """
        ...
    def closeAllSubWindows(self) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#closeAllSubWindows

        **[slot] void QMdiArea::closeAllSubWindows()**

        Closes all subwindows by sending a **QCloseEvent**  to each window. You
        may receive **subWindowActivated** () signals from subwindows before
        they are closed (if the MDI area activates the subwindow when another is
        closing).

        Subwindows that ignore the close event will remain open.

        **See also** **closeActiveSubWindow** ().
        """
        ...
    def currentSubWindow(self) -> PySide6.QtWidgets.QMdiSubWindow:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#currentSubWindow

        **QMdiSubWindow *QMdiArea::currentSubWindow() const**

        Returns a pointer to the current subwindow, or `nullptr` if there is no
        current subwindow.

        This function will return the same as **activeSubWindow** () if the
        **QApplication**  containing **QMdiArea**  is active.

        **See also** **activeSubWindow** () and **QApplication::activeWindow**
        ().
        """
        ...
    def documentMode(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#documentMode-prop

        **documentMode : bool**

        This property holds whether the tab bar is set to document mode in
        tabbed view mode.

        Document mode is disabled by default.

        **Access functions:**

        bool **documentMode** () const
        void **setDocumentMode** (bool
        **enabled** )

        **See also** **QTabBar::documentMode**  and **setViewMode** ().
        """
        ...
    def event(self, event: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#event

        **[override virtual protected] bool QMdiArea::event(QEvent * event )**

        Reimplements: **QAbstractScrollArea::event** (QEvent *event).
        """
        ...
    def eventFilter(
        self, object: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#eventFilter

        **[override virtual protected] bool QMdiArea::eventFilter(QObject *
        object , QEvent * event )**

        Reimplements: **QObject::eventFilter** (QObject *watched, QEvent
        *event).
        """
        ...
    def minimumSizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#minimumSizeHint

        **[override virtual] QSize QMdiArea::minimumSizeHint() const**

        Reimplements: **QAbstractScrollArea::minimumSizeHint() const** .
        """
        ...
    def paintEvent(self, paintEvent: PySide6.QtGui.QPaintEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#paintEvent

        **[override virtual protected] void QMdiArea::paintEvent(QPaintEvent *
        paintEvent )**

        Reimplements: **QAbstractScrollArea::paintEvent** (QPaintEvent *event).
        """
        ...
    def removeSubWindow(self, widget: PySide6.QtWidgets.QWidget) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#removeSubWindow

        **void QMdiArea::removeSubWindow(QWidget * widget )**

        Removes **widget** from the MDI area. The **widget** must be either a
        **QMdiSubWindow**  or a widget that is the internal widget of a
        subwindow. Note **widget** is never actually deleted by **QMdiArea** .
        If a **QMdiSubWindow**  is passed in, its parent is set to `nullptr` and
        it is removed; but if an internal widget is passed in, the child widget
        is set to `nullptr` and the **QMdiSubWindow**  is **not** removed.

        **See also** **addSubWindow** ().
        """
        ...
    def resizeEvent(self, resizeEvent: PySide6.QtGui.QResizeEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#resizeEvent

        **[override virtual protected] void QMdiArea::resizeEvent(QResizeEvent *
        resizeEvent )**

        Reimplements: **QAbstractScrollArea::resizeEvent** (QResizeEvent
        *event).
        """
        ...
    def scrollContentsBy(self, dx: int, dy: int) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#scrollContentsBy

        **[override virtual protected] void QMdiArea::scrollContentsBy(int dx ,
        int dy )**

        Reimplements: **QAbstractScrollArea::scrollContentsBy** (int dx, int
        dy).
        """
        ...
    def setActivationOrder(self, order: PySide6.QtWidgets.QMdiArea.WindowOrder) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#activationOrder-prop

        **activationOrder : WindowOrder**

        This property holds the ordering criteria for subwindow lists

        This property specifies the ordering criteria for the list of subwindows
        returned by **subWindowList** (). By default, it is the window creation
        order.

        **Access functions:**

        QMdiArea::WindowOrder **activationOrder** () const
        void
        **setActivationOrder** (QMdiArea::WindowOrder **order** )

        **See also** **subWindowList** ().
        """
        ...
    def setActiveSubWindow(self, window: PySide6.QtWidgets.QMdiSubWindow) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#setActiveSubWindow

        **[slot] void QMdiArea::setActiveSubWindow(QMdiSubWindow * window )**

        Activates the subwindow **window**. If **window** is `nullptr`, any
        current active window is deactivated.

        **See also** **activeSubWindow** ().
        """
        ...
    def setBackground(
        self,
        background: (
            PySide6.QtGui.QBrush
            | PySide6.QtCore.Qt.BrushStyle
            | PySide6.QtCore.Qt.GlobalColor
            | PySide6.QtGui.QColor
            | PySide6.QtGui.QGradient
            | PySide6.QtGui.QImage
            | PySide6.QtGui.QPixmap
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#background-prop

        **background : QBrush**

        This property holds the background brush for the workspace

        This property sets the background brush for the workspace area itself.
        By default, it is a gray color, but can be any brush (e.g., colors,
        gradients or pixmaps).

        **Access functions:**

        QBrush **background** () const
        void **setBackground** (const QBrush &
        **background** )
        """
        ...
    def setDocumentMode(self, enabled: bool) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#documentMode-prop

        **documentMode : bool**

        This property holds whether the tab bar is set to document mode in
        tabbed view mode.

        Document mode is disabled by default.

        **Access functions:**

        bool **documentMode** () const
        void **setDocumentMode** (bool
        **enabled** )

        **See also** **QTabBar::documentMode**  and **setViewMode** ().
        """
        ...
    def setOption(
        self, option: PySide6.QtWidgets.QMdiArea.AreaOption, on: bool = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#setOption

        **void QMdiArea::setOption(QMdiArea::AreaOption option , bool on =
        true)**

        If **on** is true, **option** is enabled on the MDI area; otherwise it
        is disabled. See **AreaOption**  for the effect of each option.

        **See also** **AreaOption**  and **testOption** ().
        """
        ...
    def setTabPosition(self, position: PySide6.QtWidgets.QTabWidget.TabPosition) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#tabPosition-prop

        **tabPosition : QTabWidget::TabPosition**

        This property holds the position of the tabs in tabbed view mode.

        Possible values for this property are described by the
        **QTabWidget::TabPosition**  enum.

        **Access functions:**

        QTabWidget::TabPosition **tabPosition** () const
        void
        **setTabPosition** (QTabWidget::TabPosition **position** )

        **See also** **QTabWidget::TabPosition**  and **setViewMode** ().
        """
        ...
    def setTabShape(self, shape: PySide6.QtWidgets.QTabWidget.TabShape) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#tabShape-prop

        **tabShape : QTabWidget::TabShape**

        This property holds the shape of the tabs in tabbed view mode.

        Possible values for this property are **QTabWidget::Rounded**  (default)
        or **QTabWidget::Triangular** .

        **Access functions:**

        QTabWidget::TabShape **tabShape** () const
        void **setTabShape**
        (QTabWidget::TabShape **shape** )

        **See also** **QTabWidget::TabShape**  and **setViewMode** ().
        """
        ...
    def setTabsClosable(self, closable: bool) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#tabsClosable-prop

        **tabsClosable : bool**

        This property holds whether the tab bar should place close buttons on
        each tab in tabbed view mode.

        Tabs are not closable by default.

        **Access functions:**

        bool **tabsClosable** () const
        void **setTabsClosable** (bool
        **closable** )

        **See also** **QTabBar::tabsClosable**  and **setViewMode** ().
        """
        ...
    def setTabsMovable(self, movable: bool) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#tabsMovable-prop

        **tabsMovable : bool**

        This property holds whether the user can move the tabs within the tabbar
        area in tabbed view mode.

        Tabs are not movable by default.

        **Access functions:**

        bool **tabsMovable** () const
        void **setTabsMovable** (bool
        **movable** )

        **See also** **QTabBar::movable**  and **setViewMode** ().
        """
        ...
    def setViewMode(self, mode: PySide6.QtWidgets.QMdiArea.ViewMode) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#viewMode-prop

        **viewMode : ViewMode**

        This property holds the way sub-windows are displayed in the
        **QMdiArea** .

        By default, the **SubWindowView**  is used to display sub-windows.

        **Access functions:**

        QMdiArea::ViewMode **viewMode** () const
        void **setViewMode**
        (QMdiArea::ViewMode **mode** )

        **See also** **ViewMode** , **setTabShape** (), and **setTabPosition**
        ().

        **Member Function Documentation**
        """
        ...
    def setupViewport(self, viewport: PySide6.QtWidgets.QWidget) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#setupViewport

        **[override virtual protected slot] void QMdiArea::setupViewport(QWidget
        * viewport )**

        Reimplements: **QAbstractScrollArea::setupViewport** (QWidget
        *viewport).

        This slot is called by **QAbstractScrollArea**  after **setViewport** ()
        has been called. Reimplement this function in a subclass of **QMdiArea**
        to initialize the new **viewport** before it is used.

        **See also** **setViewport** ().
        """
        ...
    def showEvent(self, showEvent: PySide6.QtGui.QShowEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#showEvent

        **[override virtual protected] void QMdiArea::showEvent(QShowEvent *
        showEvent )**

        Reimplements: **QWidget::showEvent** (QShowEvent *event).
        """
        ...
    def sizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#sizeHint

        **[override virtual] QSize QMdiArea::sizeHint() const**

        Reimplements: **QAbstractScrollArea::sizeHint() const** .
        """
        ...
    def subWindowList(
        self, order: PySide6.QtWidgets.QMdiArea.WindowOrder = ...
    ) -> list[PySide6.QtWidgets.QMdiSubWindow]:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#subWindowList

        **QList<QMdiSubWindow *> QMdiArea::subWindowList(QMdiArea::WindowOrder
        order = CreationOrder) const**

        Returns a list of all subwindows in the MDI area. If **order** is
        **CreationOrder**  (the default), the windows are sorted in the order in
        which they were inserted into the workspace. If **order** is
        **StackingOrder** , the windows are listed in their stacking order, with
        the topmost window as the last item in the list. If **order** is
        **ActivationHistoryOrder** , the windows are listed according to their
        recent activation history.

        **See also** **WindowOrder** .
        """
        ...
    def tabPosition(self) -> PySide6.QtWidgets.QTabWidget.TabPosition:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#tabPosition-prop

        **tabPosition : QTabWidget::TabPosition**

        This property holds the position of the tabs in tabbed view mode.

        Possible values for this property are described by the
        **QTabWidget::TabPosition**  enum.

        **Access functions:**

        QTabWidget::TabPosition **tabPosition** () const
        void
        **setTabPosition** (QTabWidget::TabPosition **position** )

        **See also** **QTabWidget::TabPosition**  and **setViewMode** ().
        """
        ...
    def tabShape(self) -> PySide6.QtWidgets.QTabWidget.TabShape:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#tabShape-prop

        **tabShape : QTabWidget::TabShape**

        This property holds the shape of the tabs in tabbed view mode.

        Possible values for this property are **QTabWidget::Rounded**  (default)
        or **QTabWidget::Triangular** .

        **Access functions:**

        QTabWidget::TabShape **tabShape** () const
        void **setTabShape**
        (QTabWidget::TabShape **shape** )

        **See also** **QTabWidget::TabShape**  and **setViewMode** ().
        """
        ...
    def tabsClosable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#tabsClosable-prop

        **tabsClosable : bool**

        This property holds whether the tab bar should place close buttons on
        each tab in tabbed view mode.

        Tabs are not closable by default.

        **Access functions:**

        bool **tabsClosable** () const
        void **setTabsClosable** (bool
        **closable** )

        **See also** **QTabBar::tabsClosable**  and **setViewMode** ().
        """
        ...
    def tabsMovable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#tabsMovable-prop

        **tabsMovable : bool**

        This property holds whether the user can move the tabs within the tabbar
        area in tabbed view mode.

        Tabs are not movable by default.

        **Access functions:**

        bool **tabsMovable** () const
        void **setTabsMovable** (bool
        **movable** )

        **See also** **QTabBar::movable**  and **setViewMode** ().
        """
        ...
    def testOption(self, opton: PySide6.QtWidgets.QMdiArea.AreaOption) -> bool:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#testOption

        **bool QMdiArea::testOption(QMdiArea::AreaOption option ) const**

        Returns `true` if **option** is enabled; otherwise returns `false`.

        **See also** **AreaOption**  and **setOption** ().
        """
        ...
    def tileSubWindows(self) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#tileSubWindows

        **[slot] void QMdiArea::tileSubWindows()**

        Arranges all child windows in a tile pattern.

        **See also** **cascadeSubWindows** ().
        """
        ...
    def timerEvent(self, timerEvent: PySide6.QtCore.QTimerEvent) -> None:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#timerEvent

        **[override virtual protected] void QMdiArea::timerEvent(QTimerEvent *
        timerEvent )**

        Reimplements: **QObject::timerEvent** (QTimerEvent *event).
        """
        ...
    def viewMode(self) -> PySide6.QtWidgets.QMdiArea.ViewMode:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#viewMode-prop

        **viewMode : ViewMode**

        This property holds the way sub-windows are displayed in the
        **QMdiArea** .

        By default, the **SubWindowView**  is used to display sub-windows.

        **Access functions:**

        QMdiArea::ViewMode **viewMode** () const
        void **setViewMode**
        (QMdiArea::ViewMode **mode** )

        **See also** **ViewMode** , **setTabShape** (), and **setTabPosition**
        ().

        **Member Function Documentation**
        """
        ...
    def viewportEvent(self, event: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#viewportEvent

        **[override virtual protected] bool QMdiArea::viewportEvent(QEvent *
        event )**

        Reimplements: **QAbstractScrollArea::viewportEvent** (QEvent *event).
        """
        ...
    @property
    def subWindowActivated(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qmdiarea.html#subWindowActivated

        **[signal] void QMdiArea::subWindowActivated(QMdiSubWindow * window )**

        **QMdiArea**  emits this signal after **window** has been activated.
        When **window** is `nullptr`, **QMdiArea**  has just deactivated its
        last active window, and there are no active windows on the workspace.

        **See also** **QMdiArea::activeSubWindow** ().
        """
        ...
