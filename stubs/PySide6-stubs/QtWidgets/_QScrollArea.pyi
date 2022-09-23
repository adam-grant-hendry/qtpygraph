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

class QScrollArea(PySide6.QtWidgets.QAbstractScrollArea):
    """
    https://doc.qt.io/qt-6/qscrollarea.html

    **Detailed Description**

    A scroll area is used to display the contents of a child widget within a
    frame. If the widget exceeds the size of the frame, the view can provide
    scroll bars so that the entire area of the child widget can be viewed. The
    child widget must be specified with **setWidget** (). For example:

    **QLabel**  *imageLabel = new **QLabel** ;
        **QImage**
    image("happyguy.png");
        imageLabel->setPixmap(**QPixmap**
    ::fromImage(image));

        scrollArea = new **QScrollArea** ;
    scrollArea->setBackgroundRole(**QPalette** ::Dark);
    scrollArea->setWidget(imageLabel);

    The code above creates a scroll area (shown in the images below) containing
    an image label. When scaling the image, the scroll area can provide the
    necessary scroll bars:

    ![](images/qscrollarea-noscrollbars.png)![](images/qscrollarea-
    onescrollbar.png)![](images/qscrollarea-twoscrollbars.png)

    The scroll bars appearance depends on the currently set **scroll bar
    policies** . You can control the appearance of the scroll bars using the
    inherited functionality from **QAbstractScrollArea** .

    For example, you can set the
    **QAbstractScrollArea::horizontalScrollBarPolicy**  and
    **QAbstractScrollArea::verticalScrollBarPolicy**  properties. Or if you want
    the scroll bars to adjust dynamically when the contents of the scroll area
    changes, you can use the **horizontalScrollBar** () and
    **verticalScrollBar** () functions (which enable you to access the scroll
    bars) and set the scroll bars' values whenever the scroll area's contents
    change, using the **QScrollBar::setValue** () function.

    You can retrieve the child widget using the **widget** () function. The view
    can be made to be resizable with the **setWidgetResizable** () function. The
    alignment of the widget can be specified with **setAlignment** ().

    Two convenience functions **ensureVisible** () and **ensureWidgetVisible**
    () ensure a certain region of the contents is visible inside the viewport,
    by scrolling the contents if necessary.

    **Size Hints and Layouts**

    When using a scroll area to display the contents of a custom widget, it is
    important to ensure that the **size hint**  of the child widget is set to a
    suitable value. If a standard **QWidget**  is used for the child widget, it
    may be necessary to call **QWidget::setMinimumSize** () to ensure that the
    contents of the widget are shown correctly within the scroll area.

    If a scroll area is used to display the contents of a widget that contains
    child widgets arranged in a layout, it is important to realize that the size
    policy of the layout will also determine the size of the widget. This is
    especially useful to know if you intend to dynamically change the contents
    of the layout. In such cases, setting the layout's **size constraint**
    property to one which provides constraints on the minimum and/or maximum
    size of the layout (e.g., **QLayout::SetMinAndMaxSize** ) will cause the
    size of the scroll area to be updated whenever the contents of the layout
    changes.

    For a complete example using the QScrollArea class, see the **Image Viewer**
    example. The example shows how to combine **QLabel**  and QScrollArea to
    display an image.

    **See also** **QAbstractScrollArea** , **QScrollBar** , and **Image Viewer
    Example** .
    """

    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#QScrollArea

        **QScrollArea::QScrollArea(QWidget * parent = nullptr)**

        Constructs an empty scroll area with the given **parent**.

        **See also** **setWidget** ().
        """
        ...
    def alignment(self) -> PySide6.QtCore.Qt.Alignment:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#alignment-prop

        **alignment : Qt::Alignment**

        This property holds the alignment of the scroll area's widget

        A valid alignment is a combination of the following flags:

        * `Qt::AlignLeft`
          * `Qt::AlignHCenter`
          * `Qt::AlignRight`
          *
        `Qt::AlignTop`
          * `Qt::AlignVCenter`
          * `Qt::AlignBottom`

        By default, the widget stays rooted to the top-left corner of the scroll
        area.

        **Access functions:**

        Qt::Alignment **alignment** () const
        void **setAlignment**
        (Qt::Alignment)
        """
        ...
    def ensureVisible(
        self, x: int, y: int, xmargin: int = ..., ymargin: int = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#ensureVisible

        **void QScrollArea::ensureVisible(int x , int y , int xmargin = 50, int
        ymargin = 50)**

        Scrolls the contents of the scroll area so that the point ( **x** ,
        **y** ) is visible inside the region of the viewport with margins
        specified in pixels by **xmargin** and **ymargin**. If the specified
        point cannot be reached, the contents are scrolled to the nearest valid
        position. The default value for both margins is 50 pixels.
        """
        ...
    def ensureWidgetVisible(
        self,
        childWidget: PySide6.QtWidgets.QWidget,
        xmargin: int = ...,
        ymargin: int = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#ensureWidgetVisible

        **void QScrollArea::ensureWidgetVisible(QWidget * childWidget , int
        xmargin = 50, int ymargin = 50)**

        Scrolls the contents of the scroll area so that the **childWidget** of
        **QScrollArea::widget** () is visible inside the viewport with margins
        specified in pixels by **xmargin** and **ymargin**. If the specified
        point cannot be reached, the contents are scrolled to the nearest valid
        position. The default value for both margins is 50 pixels.
        """
        ...
    def event(self, arg__1: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#event

        **[override virtual protected] bool QScrollArea::event(QEvent * e )**

        Reimplements: **QAbstractScrollArea::event** (QEvent *event).
        """
        ...
    def eventFilter(
        self, arg__1: PySide6.QtCore.QObject, arg__2: PySide6.QtCore.QEvent
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#eventFilter

        **[override virtual protected] bool QScrollArea::eventFilter(QObject * o
        , QEvent * e )**

        Reimplements: **QObject::eventFilter** (QObject *watched, QEvent
        *event).
        """
        ...
    def focusNextPrevChild(self, next: bool) -> bool:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#focusNextPrevChild

        **[override virtual] bool QScrollArea::focusNextPrevChild(bool next )**

        Reimplements: **QWidget::focusNextPrevChild** (bool next).
        """
        ...
    def resizeEvent(self, arg__1: PySide6.QtGui.QResizeEvent) -> None:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#resizeEvent

        **[override virtual protected] void
        QScrollArea::resizeEvent(QResizeEvent *)**

        Reimplements: **QAbstractScrollArea::resizeEvent** (QResizeEvent
        *event).
        """
        ...
    def scrollContentsBy(self, dx: int, dy: int) -> None:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#scrollContentsBy

        **[override virtual protected] void QScrollArea::scrollContentsBy(int dx
        , int dy )**

        Reimplements: **QAbstractScrollArea::scrollContentsBy** (int dx, int
        dy).
        """
        ...
    def setAlignment(self, arg__1: PySide6.QtCore.Qt.Alignment) -> None:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#alignment-prop

        **alignment : Qt::Alignment**

        This property holds the alignment of the scroll area's widget

        A valid alignment is a combination of the following flags:

        * `Qt::AlignLeft`
          * `Qt::AlignHCenter`
          * `Qt::AlignRight`
          *
        `Qt::AlignTop`
          * `Qt::AlignVCenter`
          * `Qt::AlignBottom`

        By default, the widget stays rooted to the top-left corner of the scroll
        area.

        **Access functions:**

        Qt::Alignment **alignment** () const
        void **setAlignment**
        (Qt::Alignment)
        """
        ...
    def setWidget(self, widget: PySide6.QtWidgets.QWidget) -> None:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#setWidget

        **void QScrollArea::setWidget(QWidget * widget )**

        Sets the scroll area's **widget**.

        The **widget** becomes a child of the scroll area, and will be destroyed
        when the scroll area is deleted or when a new widget is set.

        The widget's **autoFillBackground**  property will be set to `true`.

        If the scroll area is visible when the **widget** is added, you must
        **show** () it explicitly.

        Note that You must add the layout of **widget** before you call this
        function; if you add it later, the **widget** will not be visible -
        regardless of when you **show** () the scroll area. In this case, you
        can also not **show** () the **widget** later.

        **See also** **widget** ().
        """
        ...
    def setWidgetResizable(self, resizable: bool) -> None:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#widgetResizable-prop

        **widgetResizable : bool**

        This property holds whether the scroll area should resize the view
        widget

        If this property is set to false (the default), the scroll area honors
        the size of its widget. Regardless of this property, you can
        programmatically resize the widget using **widget** ()->**resize** (),
        and the scroll area will automatically adjust itself to the new size.

        If this property is set to true, the scroll area will automatically
        resize the widget in order to avoid scroll bars where they can be
        avoided, or to take advantage of extra space.

        **Access functions:**

        bool **widgetResizable** () const
        void **setWidgetResizable** (bool
        **resizable** )

        **Member Function Documentation**
        """
        ...
    def sizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#sizeHint

        **[override virtual] QSize QScrollArea::sizeHint() const**

        Reimplements: **QAbstractScrollArea::sizeHint() const** .
        """
        ...
    def takeWidget(self) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#takeWidget

        **QWidget *QScrollArea::takeWidget()**

        Removes the scroll area's widget, and passes ownership of the widget to
        the caller.

        **See also** **widget** ().
        """
        ...
    def viewportSizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#viewportSizeHint

        **[override virtual protected] QSize QScrollArea::viewportSizeHint()
        const**

        Reimplements: **QAbstractScrollArea::viewportSizeHint() const** .
        """
        ...
    def widget(self) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#widget

        **QWidget *QScrollArea::widget() const**

        Returns the scroll area's widget, or `nullptr` if there is none.

        **See also** **setWidget** ().
        """
        ...
    def widgetResizable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qscrollarea.html#widgetResizable-prop

        **widgetResizable : bool**

        This property holds whether the scroll area should resize the view
        widget

        If this property is set to false (the default), the scroll area honors
        the size of its widget. Regardless of this property, you can
        programmatically resize the widget using **widget** ()->**resize** (),
        and the scroll area will automatically adjust itself to the new size.

        If this property is set to true, the scroll area will automatically
        resize the widget in order to avoid scroll bars where they can be
        avoided, or to take advantage of extra space.

        **Access functions:**

        bool **widgetResizable** () const
        void **setWidgetResizable** (bool
        **resizable** )

        **Member Function Documentation**
        """
        ...
