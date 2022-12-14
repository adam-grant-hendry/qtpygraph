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

from collections.abc import Sequence
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QSplitter(PySide6.QtWidgets.QFrame):
    """
    https://doc.qt.io/qt-6/qsplitter.html

    **Detailed Description**

    A splitter lets the user control the size of child widgets by dragging the
    boundary between them. Any number of widgets may be controlled by a single
    splitter. The typical use of a QSplitter is to create several widgets and
    add them using **insertWidget** () or **addWidget** ().

    The following example will show a **QListView** , **QTreeView** , and
    **QTextEdit**  side by side, with two splitter handles:

    **QSplitter**  *splitter = new **QSplitter** (parent);
            **QListView**
    *listview = new **QListView** ;
            **QTreeView**  *treeview = new
    **QTreeView** ;
            **QTextEdit**  *textedit = new **QTextEdit** ;
    splitter->addWidget(listview);
            splitter->addWidget(treeview);
    splitter->addWidget(textedit);

    If a widget is already inside a QSplitter when **insertWidget** () or
    **addWidget** () is called, it will move to the new position. This can be
    used to reorder widgets in the splitter later. You can use **indexOf** (),
    **widget** (), and **count** () to get access to the widgets inside the
    splitter.

    A default QSplitter lays out its children horizontally (side by side); you
    can use **setOrientation** (**Qt::Vertical** ) to lay its children out
    vertically.

    By default, all widgets can be as large or as small as the user wishes,
    between the **minimumSizeHint** () (or **minimumSize** ()) and
    **maximumSize** () of the widgets.

    QSplitter resizes its children dynamically by default. If you would rather
    have QSplitter resize the children only at the end of a resize operation,
    call **setOpaqueResize** (false).

    The initial distribution of size between the widgets is determined by
    multiplying the initial size with the stretch factor. You can also use
    **setSizes** () to set the sizes of all the widgets. The function **sizes**
    () returns the sizes set by the user. Alternatively, you can save and
    restore the sizes of the widgets from a **QByteArray**  using **saveState**
    () and **restoreState** () respectively.

    When you **hide** () a child, its space will be distributed among the other
    children. It will be reinstated when you **show** () it again.

    **Note:** Adding a **QLayout**  to a QSplitter is not supported (either
    through **setLayout** () or making the QSplitter a parent of the **QLayout**
    ); use **addWidget** () instead (see example above).

    **See also** **QSplitterHandle** , **QHBoxLayout** , **QVBoxLayout** , and
    **QTabWidget** .
    """

    @overload
    def __init__(
        self,
        arg__1: PySide6.QtCore.Qt.Orientation,
        parent: PySide6.QtWidgets.QWidget | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#QSplitter

        **QSplitter::QSplitter(QWidget * parent = nullptr)**

        Constructs a horizontal splitter with the **parent** argument passed on
        to the **QFrame**  constructor.

        **See also** **setOrientation** ().
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#QSplitter-1

        **QSplitter::QSplitter(Qt::Orientation orientation , QWidget * parent =
        nullptr)**

        Constructs a splitter with the given **orientation** and **parent**.

        **See also** **setOrientation** ().
        """
        ...
    def addWidget(self, widget: PySide6.QtWidgets.QWidget) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#addWidget

        **void QSplitter::addWidget(QWidget * widget )**

        Adds the given **widget** to the splitter's layout after all the other
        items.

        If **widget** is already in the splitter, it will be moved to the new
        position.

        **Note:** The splitter takes ownership of the widget.

        **See also** **insertWidget** (), **widget** (), and **indexOf** ().
        """
        ...
    def changeEvent(self, arg__1: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#changeEvent

        **[override virtual protected] void QSplitter::changeEvent(QEvent * ev
        )**

        Reimplements: **QFrame::changeEvent** (QEvent *ev).
        """
        ...
    def childEvent(self, arg__1: PySide6.QtCore.QChildEvent) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#childEvent

        **[override virtual protected] void QSplitter::childEvent(QChildEvent *
        c )**

        Reimplements: **QObject::childEvent** (QChildEvent *event).

        Tells the splitter that the child widget described by **c** has been
        inserted or removed.

        This method is also used to handle the situation where a widget is
        created with the splitter as a parent but not explicitly added with
        **insertWidget** () or **addWidget** (). This is for compatibility and
        not the recommended way of putting widgets into a splitter in new code.
        Please use **insertWidget** () or **addWidget** () in new code.

        **See also** **addWidget** () and **insertWidget** ().
        """
        ...
    def childrenCollapsible(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsplitter.html#childrenCollapsible-prop

        **childrenCollapsible : bool**

        This property holds whether child widgets can be resized down to size 0
        by the user

        By default, children are collapsible. It is possible to enable and
        disable the collapsing of individual children using **setCollapsible**
        ().

        **Access functions:**

        bool **childrenCollapsible** () const
        void **setChildrenCollapsible**
        (bool)

        **See also** **setCollapsible** ().
        """
        ...
    def closestLegalPosition(self, arg__1: int, arg__2: int) -> int:
        """
        https://doc.qt.io/qt-6/qsplitter.html#closestLegalPosition

        **[protected] int QSplitter::closestLegalPosition(int pos , int index
        )**

        Returns the closest legal position to **pos** of the widget at
        **index**.

        For right-to-left languages such as Arabic and Hebrew, the layout of
        horizontal splitters is reversed. Positions are then measured from the
        right edge of the widget.

        **See also** **getRange** ().
        """
        ...
    def count(self) -> int:
        """
        https://doc.qt.io/qt-6/qsplitter.html#count

        **int QSplitter::count() const**

        Returns the number of widgets contained in the splitter's layout.

        **See also** **widget** () and **handle** ().
        """
        ...
    def createHandle(self) -> PySide6.QtWidgets.QSplitterHandle:
        """
        https://doc.qt.io/qt-6/qsplitter.html#createHandle

        **[virtual protected] QSplitterHandle *QSplitter::createHandle()**

        Returns a new splitter handle as a child widget of this splitter. This
        function can be reimplemented in subclasses to provide support for
        custom handles.

        **See also** **handle** () and **indexOf** ().
        """
        ...
    def event(self, arg__1: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qsplitter.html#event

        **[override virtual protected] bool QSplitter::event(QEvent * e )**

        Reimplements: **QFrame::event** (QEvent *e).
        """
        ...
    def getRange(self, index: int) -> tuple[int, int]:
        """
        https://doc.qt.io/qt-6/qsplitter.html#getRange

        **void QSplitter::getRange(int index , int * min , int * max ) const**

        Returns the valid range of the splitter at **index** in * **min** and *
        **max** if **min** and **max** are not 0.
        """
        ...
    def handle(self, index: int) -> PySide6.QtWidgets.QSplitterHandle:
        """
        https://doc.qt.io/qt-6/qsplitter.html#handle

        **QSplitterHandle *QSplitter::handle(int index ) const**

        Returns the handle to the left of (or above) the item in the splitter's
        layout at the given **index** , or `nullptr` if there is no such item.
        The handle at index 0 is always hidden.

        For right-to-left languages such as Arabic and Hebrew, the layout of
        horizontal splitters is reversed. The handle will be to the right of the
        widget at **index**.

        **See also** **count** (), **widget** (), **indexOf** (),
        **createHandle** (), and **setHandleWidth** ().
        """
        ...
    def handleWidth(self) -> int:
        """
        https://doc.qt.io/qt-6/qsplitter.html#handleWidth-prop

        **handleWidth : int**

        This property holds the width of the splitter handles

        By default, this property contains a value that depends on the user's
        platform and style preferences.

        If you set handleWidth to 1 or 0, the actual grab area will grow to
        overlap a few pixels of its respective widgets.

        **Access functions:**

        int **handleWidth** () const
        void **setHandleWidth** (int)
        """
        ...
    def indexOf(self, w: PySide6.QtWidgets.QWidget) -> int:
        """
        https://doc.qt.io/qt-6/qsplitter.html#indexOf

        **int QSplitter::indexOf(QWidget * widget ) const**

        Returns the index in the splitter's layout of the specified **widget** ,
        or -1 if **widget** is not found. This also works for handles.

        Handles are numbered from 0. There are as many handles as there are
        child widgets, but the handle at position 0 is always hidden.

        **See also** **count** () and **widget** ().
        """
        ...
    def insertWidget(self, index: int, widget: PySide6.QtWidgets.QWidget) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#insertWidget

        **void QSplitter::insertWidget(int index , QWidget * widget )**

        Inserts the **widget** specified into the splitter's layout at the given
        **index**.

        If **widget** is already in the splitter, it will be moved to the new
        position.

        If **index** is an invalid index, then the widget will be inserted at
        the end.

        **Note:** The splitter takes ownership of the widget.

        **See also** **addWidget** (), **indexOf** (), and **widget** ().
        """
        ...
    def isCollapsible(self, index: int) -> bool:
        """
        https://doc.qt.io/qt-6/qsplitter.html#isCollapsible

        **bool QSplitter::isCollapsible(int index ) const**

        Returns `true` if the widget at **index** is collapsible, otherwise
        returns `false`.
        """
        ...
    def minimumSizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qsplitter.html#minimumSizeHint

        **[override virtual] QSize QSplitter::minimumSizeHint() const**

        Reimplements an access function for property:
        **QWidget::minimumSizeHint** .
        """
        ...
    def moveSplitter(self, pos: int, index: int) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#moveSplitter

        **[protected] void QSplitter::moveSplitter(int pos , int index )**

        Moves the left or top edge of the splitter handle at **index** as close
        as possible to position **pos** , which is the distance from the left or
        top edge of the widget.

        For right-to-left languages such as Arabic and Hebrew, the layout of
        horizontal splitters is reversed. **pos** is then the distance from the
        right edge of the widget.

        **See also** **splitterMoved** (), **closestLegalPosition** (), and
        **getRange** ().
        """
        ...
    def opaqueResize(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsplitter.html#opaqueResize-prop

        **opaqueResize : bool**

        Returns `true` if widgets are resized dynamically (opaquely) while
        interactively moving the splitter. Otherwise returns `false`.

        The default resize behavior is style dependent (determined by the
        SH_Splitter_OpaqueResize style hint). However, you can override it by
        calling setOpaqueResize()

        **Access functions:**

        bool **opaqueResize** () const
        void **setOpaqueResize** (bool
        **opaque** = true)

        **See also** **QStyle::StyleHint** .
        """
        ...
    def orientation(self) -> PySide6.QtCore.Qt.Orientation:
        """
        https://doc.qt.io/qt-6/qsplitter.html#orientation-prop

        **orientation : Qt::Orientation**

        This property holds the orientation of the splitter

        By default, the orientation is horizontal (i.e., the widgets are laid
        out side by side). The possible orientations are **Qt::Horizontal**  and
        **Qt::Vertical** .

        **Access functions:**

        Qt::Orientation **orientation** () const
        void **setOrientation**
        (Qt::Orientation)

        **See also** **QSplitterHandle::orientation** ().

        **Member Function Documentation**
        """
        ...
    def refresh(self) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#refresh

        **void QSplitter::refresh()**

        Updates the splitter's state. You should not need to call this function.
        """
        ...
    def replaceWidget(
        self, index: int, widget: PySide6.QtWidgets.QWidget
    ) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qsplitter.html#replaceWidget

        **[since 5.9] QWidget *QSplitter::replaceWidget(int index , QWidget *
        widget )**

        Replaces the widget in the splitter's layout at the given **index** by
        **widget**.

        Returns the widget that has just been replaced if **index** is valid and
        **widget** is not already a child of the splitter. Otherwise, it returns
        null and no replacement or addition is made.

        The geometry of the newly inserted widget will be the same as the widget
        it replaces. Its visible and collapsed states are also inherited.

        **Note:** The splitter takes ownership of **widget** and sets the parent
        of the replaced widget to null.

        **Note:** Because **widget** gets **reparented**  into the splitter, its
        **geometry**  may not be set right away, but only after **widget** will
        receive the appropriate events.

        This function was introduced in Qt 5.9.

        **See also** **insertWidget** () and **indexOf** ().
        """
        ...
    def resizeEvent(self, arg__1: PySide6.QtGui.QResizeEvent) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#resizeEvent

        **[override virtual protected] void QSplitter::resizeEvent(QResizeEvent
        *)**

        Reimplements: **QWidget::resizeEvent** (QResizeEvent *event).
        """
        ...
    def restoreState(self, state: PySide6.QtCore.QByteArray | bytes) -> bool:
        """
        https://doc.qt.io/qt-6/qsplitter.html#restoreState

        **bool QSplitter::restoreState(const QByteArray & state )**

        Restores the splitter's layout to the **state** specified. Returns
        `true` if the state is restored; otherwise returns `false`.

        Typically this is used in conjunction with **QSettings**  to restore the
        size from a past session. Here is an example:

        Restore the splitter's state:

        **QSettings**  settings;
        splitter->restoreState(settings.value("splitterSizes").toByteArray());

        A failure to restore the splitter's layout may result from either
        invalid or out-of-date data in the supplied byte array.

        **See also** **saveState** ().
        """
        ...
    def saveState(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qsplitter.html#saveState

        **QByteArray QSplitter::saveState() const**

        Saves the state of the splitter's layout.

        Typically this is used in conjunction with **QSettings**  to remember
        the size for a future session. A version number is stored as part of the
        data. Here is an example:

        **QSettings**  settings;
                settings.setValue("splitterSizes",
        splitter->saveState());

        **See also** **restoreState** ().
        """
        ...
    def setChildrenCollapsible(self, arg__1: bool) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#childrenCollapsible-prop

        **childrenCollapsible : bool**

        This property holds whether child widgets can be resized down to size 0
        by the user

        By default, children are collapsible. It is possible to enable and
        disable the collapsing of individual children using **setCollapsible**
        ().

        **Access functions:**

        bool **childrenCollapsible** () const
        void **setChildrenCollapsible**
        (bool)

        **See also** **setCollapsible** ().
        """
        ...
    def setCollapsible(self, index: int, arg__2: bool) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#setCollapsible

        **void QSplitter::setCollapsible(int index , bool collapse )**

        Sets whether the child widget at **index** is collapsible to
        **collapse**.

        By default, children are collapsible, meaning that the user can resize
        them down to size 0, even if they have a non-zero **minimumSize** () or
        **minimumSizeHint** (). This behavior can be changed on a per-widget
        basis by calling this function, or globally for all the widgets in the
        splitter by setting the **childrenCollapsible**  property.

        **See also** **isCollapsible** () and **childrenCollapsible** .
        """
        ...
    def setHandleWidth(self, arg__1: int) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#handleWidth-prop

        **handleWidth : int**

        This property holds the width of the splitter handles

        By default, this property contains a value that depends on the user's
        platform and style preferences.

        If you set handleWidth to 1 or 0, the actual grab area will grow to
        overlap a few pixels of its respective widgets.

        **Access functions:**

        int **handleWidth** () const
        void **setHandleWidth** (int)
        """
        ...
    def setOpaqueResize(self, opaque: bool = ...) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#opaqueResize-prop

        **opaqueResize : bool**

        Returns `true` if widgets are resized dynamically (opaquely) while
        interactively moving the splitter. Otherwise returns `false`.

        The default resize behavior is style dependent (determined by the
        SH_Splitter_OpaqueResize style hint). However, you can override it by
        calling setOpaqueResize()

        **Access functions:**

        bool **opaqueResize** () const
        void **setOpaqueResize** (bool
        **opaque** = true)

        **See also** **QStyle::StyleHint** .
        """
        ...
    def setOrientation(self, arg__1: PySide6.QtCore.Qt.Orientation) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#orientation-prop

        **orientation : Qt::Orientation**

        This property holds the orientation of the splitter

        By default, the orientation is horizontal (i.e., the widgets are laid
        out side by side). The possible orientations are **Qt::Horizontal**  and
        **Qt::Vertical** .

        **Access functions:**

        Qt::Orientation **orientation** () const
        void **setOrientation**
        (Qt::Orientation)

        **See also** **QSplitterHandle::orientation** ().

        **Member Function Documentation**
        """
        ...
    def setRubberBand(self, position: int) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#setRubberBand

        **[protected] void QSplitter::setRubberBand(int pos )**

        Displays a rubber band at position **pos**. If **pos** is negative, the
        rubber band is removed.
        """
        ...
    def setSizes(self, list: Sequence[int]) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#setSizes

        **void QSplitter::setSizes(const QList<int> & list )**

        Sets the child widgets' respective sizes to the values given in the
        **list**.

        If the splitter is horizontal, the values set the width of each widget
        in pixels, from left to right. If the splitter is vertical, the height
        of each widget is set, from top to bottom.

        Extra values in the **list** are ignored. If **list** contains too few
        values, the result is undefined, but the program will still be well-
        behaved.

        The overall size of the splitter widget is not affected. Instead, any
        additional/missing space is distributed amongst the widgets according to
        the relative weight of the sizes.

        If you specify a size of 0, the widget will be invisible. The size
        policies of the widgets are preserved. That is, a value smaller than the
        minimal size hint of the respective widget will be replaced by the value
        of the hint.

        **See also** **sizes** ().
        """
        ...
    def setStretchFactor(self, index: int, stretch: int) -> None:
        """
        https://doc.qt.io/qt-6/qsplitter.html#setStretchFactor

        **void QSplitter::setStretchFactor(int index , int stretch )**

        Updates the size policy of the widget at position **index** to have a
        stretch factor of **stretch**.

        **stretch** is not the effective stretch factor; the effective stretch
        factor is calculated by taking the initial size of the widget and
        multiplying it with **stretch**.

        This function is provided for convenience. It is equivalent to

        **QWidget**  *widget = splitter->widget(index);
            **QSizePolicy**
        policy = widget->sizePolicy();
            policy.setHorizontalStretch(stretch);
        policy.setVerticalStretch(stretch);
            widget->setSizePolicy(policy);

        **See also** **setSizes** () and **widget** ().
        """
        ...
    def sizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qsplitter.html#sizeHint

        **[override virtual] QSize QSplitter::sizeHint() const**

        Reimplements: **QFrame::sizeHint() const** .
        """
        ...
    def sizes(self) -> list[int]:
        """
        https://doc.qt.io/qt-6/qsplitter.html#sizes

        **QList<int> QSplitter::sizes() const**

        Returns a list of the size parameters of all the widgets in this
        splitter.

        If the splitter's orientation is horizontal, the list contains the
        widgets width in pixels, from left to right; if the orientation is
        vertical, the list contains the widgets' heights in pixels, from top to
        bottom.

        Giving the values to another splitter's **setSizes** () function will
        produce a splitter with the same layout as this one.

        Note that invisible widgets have a size of 0.

        **See also** **setSizes** ().
        """
        ...
    def widget(self, index: int) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qsplitter.html#widget

        **QWidget *QSplitter::widget(int index ) const**

        Returns the widget at the given **index** in the splitter's layout, or
        `nullptr` if there is no such widget.

        **See also** **count** (), **handle** (), **indexOf** (), and
        **insertWidget** ().
        """
        ...
    @property
    def splitterMoved(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qsplitter.html#splitterMoved

        **[signal] void QSplitter::splitterMoved(int pos , int index )**

        This signal is emitted when the splitter handle at a particular
        **index** has been moved to position **pos**.

        For right-to-left languages such as Arabic and Hebrew, the layout of
        horizontal splitters is reversed. **pos** is then the distance from the
        right edge of the widget.

        **See also** **moveSplitter** ().
        """
        ...
