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

from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QGridLayout(PySide6.QtWidgets.QLayout):
    """
    https://doc.qt.io/qt-6/qgridlayout.html

    **Detailed Description**

    QGridLayout takes the space made available to it (by its parent layout or by
    the **parentWidget** ()), divides it up into rows and columns, and puts each
    widget it manages into the correct cell.

    Columns and rows behave identically; we will discuss columns, but there are
    equivalent functions for rows.

    Each column has a minimum width and a stretch factor. The minimum width is
    the greatest of that set using **setColumnMinimumWidth** () and the minimum
    width of each widget in that column. The stretch factor is set using
    **setColumnStretch** () and determines how much of the available space the
    column will get over and above its necessary minimum.

    Normally, each managed widget or layout is put into a cell of its own using
    **addWidget** (). It is also possible for a widget to occupy multiple cells
    using the row and column spanning overloads of **addItem** () and
    **addWidget** (). If you do this, QGridLayout will guess how to distribute
    the size over the columns/rows (based on the stretch factors).

    To remove a widget from a layout, call **removeWidget** (). Calling
    **QWidget::hide** () on a widget also effectively removes the widget from
    the layout until **QWidget::show** () is called.

    This illustration shows a fragment of a dialog with a five-column, three-row
    grid (the grid is shown overlaid in magenta):

    ![A grid layout](images/qgridlayout.png)

    Columns 0, 2 and 4 in this dialog fragment are made up of a **QLabel** , a
    **QLineEdit** , and a QListBox. Columns 1 and 3 are placeholders made with
    **setColumnMinimumWidth** (). Row 0 consists of three **QLabel**  objects,
    row 1 of three **QLineEdit**  objects and row 2 of three QListBox objects.
    We used placeholder columns (1 and 3) to get the right amount of space
    between the columns.

    Note that the columns and rows are not equally wide or tall. If you want two
    columns to have the same width, you must set their minimum widths and
    stretch factors to be the same yourself. You do this using
    **setColumnMinimumWidth** () and **setColumnStretch** ().

    If the QGridLayout is not the top-level layout (i.e. does not manage all of
    the widget's area and children), you must add it to its parent layout when
    you create it, but before you do anything with it. The normal way to add a
    layout is by calling **addLayout** () on the parent layout.

    Once you have added your layout you can start putting widgets and other
    layouts into the cells of your grid layout using **addWidget** (),
    **addItem** (), and **addLayout** ().

    QGridLayout also includes two margin widths: the **contents margin**  and
    the **spacing** (). The contents margin is the width of the reserved space
    along each of the QGridLayout's four sides. The **spacing** () is the width
    of the automatically allocated spacing between neighboring boxes.

    The default contents margin values are provided by the **style** . The
    default value Qt styles specify is 9 for child widgets and 11 for windows.
    The spacing defaults to the same as the margin width for a top-level layout,
    or to the same as the parent layout.

    **See also** **QBoxLayout** , **QStackedLayout** , **Layout Management** ,
    and **Basic Layouts Example** .
    """

    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#QGridLayout

        **QGridLayout::QGridLayout(QWidget * parent = nullptr)**

        Constructs a new QGridLayout with parent widget, **parent**. The layout
        has one row and one column initially, and will expand when new items are
        inserted.

        The layout is set directly as the top-level layout for **parent**. There
        can be only one top-level layout for a widget. It is returned by
        **QWidget::layout** ().

        If **parent** is `nullptr`, then you must insert this grid layout into
        another layout, or set it as a widget's layout using
        **QWidget::setLayout** ().

        **See also** **QWidget::setLayout** ().
        """
        ...
    @overload
    def addItem(self, arg__1: PySide6.QtWidgets.QLayoutItem) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#addItem

        **void QGridLayout::addItem(QLayoutItem * item , int row , int column ,
        int rowSpan = 1, int columnSpan = 1, Qt::Alignment alignment =
        Qt::Alignment())**

        Adds **item** at position **row** , **column** , spanning **rowSpan**
        rows and **columnSpan** columns, and aligns it according to
        **alignment**. If **rowSpan** and/or **columnSpan** is -1, then the item
        will extend to the bottom and/or right edge, respectively. The layout
        takes ownership of the **item**.

        **Warning:** Do not use this function to add child layouts or child
        widget items. Use **addLayout** () or **addWidget** () instead.
        """
        ...
    @overload
    def addItem(
        self,
        item: PySide6.QtWidgets.QLayoutItem,
        row: int,
        column: int,
        rowSpan: int = ...,
        columnSpan: int = ...,
        alignment: PySide6.QtCore.Qt.Alignment = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#addItem-1

        **[override virtual protected] void QGridLayout::addItem(QLayoutItem *
        item )**

        Reimplements: **QLayout::addItem** (QLayoutItem *item).
        """
        ...
    @overload
    def addLayout(
        self,
        arg__1: PySide6.QtWidgets.QLayout,
        row: int,
        column: int,
        alignment: PySide6.QtCore.Qt.Alignment = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#addLayout

        **void QGridLayout::addLayout(QLayout * layout , int row , int column ,
        Qt::Alignment alignment = Qt::Alignment())**

        Places the **layout** at position ( **row** , **column** ) in the grid.
        The top-left position is (0, 0).

        The alignment is specified by **alignment**. The default alignment is 0,
        which means that the widget fills the entire cell.

        A non-zero alignment indicates that the layout should not grow to fill
        the available space but should be sized according to **sizeHint** ().

        **layout** becomes a child of the grid layout.
        """
        ...
    @overload
    def addLayout(
        self,
        arg__1: PySide6.QtWidgets.QLayout,
        row: int,
        column: int,
        rowSpan: int,
        columnSpan: int,
        alignment: PySide6.QtCore.Qt.Alignment = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#addLayout-1

        **void QGridLayout::addLayout(QLayout * layout , int row , int column ,
        int rowSpan , int columnSpan , Qt::Alignment alignment =
        Qt::Alignment())**

        This is an overloaded function.

        This version adds the layout **layout** to the cell grid, spanning
        multiple rows/columns. The cell will start at **row** , **column**
        spanning **rowSpan** rows and **columnSpan** columns.

        If **rowSpan** and/or **columnSpan** is -1, then the layout will extend
        to the bottom and/or right edge, respectively.
        """
        ...
    @overload
    def addWidget(
        self,
        arg__1: PySide6.QtWidgets.QWidget,
        row: int,
        column: int,
        alignment: PySide6.QtCore.Qt.Alignment = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#addWidget-1

        **void QGridLayout::addWidget(QWidget * widget , int row , int column ,
        Qt::Alignment alignment = Qt::Alignment())**

        Adds the given **widget** to the cell grid at **row** , **column**. The
        top-left position is (0, 0) by default.

        The alignment is specified by **alignment**. The default alignment is 0,
        which means that the widget fills the entire cell.
        """
        ...
    @overload
    def addWidget(
        self,
        arg__1: PySide6.QtWidgets.QWidget,
        row: int,
        column: int,
        rowSpan: int,
        columnSpan: int,
        alignment: PySide6.QtCore.Qt.Alignment = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#addWidget-2

        **void QGridLayout::addWidget(QWidget * widget , int fromRow , int
        fromColumn , int rowSpan , int columnSpan , Qt::Alignment alignment =
        Qt::Alignment())**

        This is an overloaded function.

        This version adds the given **widget** to the cell grid, spanning
        multiple rows/columns. The cell will start at **fromRow** ,
        **fromColumn** spanning **rowSpan** rows and **columnSpan** columns. The
        **widget** will have the given **alignment**.

        If **rowSpan** and/or **columnSpan** is -1, then the widget will extend
        to the bottom and/or right edge, respectively.
        """
        ...
    @overload
    def addWidget(self, w: PySide6.QtWidgets.QWidget) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#addWidget-1

        **void QGridLayout::addWidget(QWidget * widget , int row , int column ,
        Qt::Alignment alignment = Qt::Alignment())**

        Adds the given **widget** to the cell grid at **row** , **column**. The
        top-left position is (0, 0) by default.

        The alignment is specified by **alignment**. The default alignment is 0,
        which means that the widget fills the entire cell.
        """
        ...
    def cellRect(self, row: int, column: int) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#cellRect

        **QRect QGridLayout::cellRect(int row , int column ) const**

        Returns the geometry of the cell with row **row** and column **column**
        in the grid. Returns an invalid rectangle if **row** or **column** is
        outside the grid.

        **Warning:** in the current version of Qt this function does not return
        valid results until **setGeometry** () has been called, i.e. after the
        **parentWidget** () is visible.
        """
        ...
    def columnCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#columnCount

        **int QGridLayout::columnCount() const**

        Returns the number of columns in this grid.
        """
        ...
    def columnMinimumWidth(self, column: int) -> int:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#columnMinimumWidth

        **int QGridLayout::columnMinimumWidth(int column ) const**

        Returns the column spacing for column **column**.

        **See also** **setColumnMinimumWidth** ().
        """
        ...
    def columnStretch(self, column: int) -> int:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#columnStretch

        **int QGridLayout::columnStretch(int column ) const**

        Returns the stretch factor for column **column**.

        **See also** **setColumnStretch** ().
        """
        ...
    def count(self) -> int:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#count

        **[override virtual] int QGridLayout::count() const**

        Reimplements: **QLayout::count() const** .
        """
        ...
    def expandingDirections(self) -> PySide6.QtCore.Qt.Orientations:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#expandingDirections

        **[override virtual] Qt::Orientations QGridLayout::expandingDirections()
        const**

        Reimplements: **QLayout::expandingDirections() const** .
        """
        ...
    def getItemPosition(self, idx: int) -> tuple[int, int, int, int]:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#getItemPosition

        **void QGridLayout::getItemPosition(int index , int * row , int * column
        , int * rowSpan , int * columnSpan ) const**

        Returns the position information of the item with the given **index**.

        The variables passed as **row** and **column** are updated with the
        position of the item in the layout, and the **rowSpan** and
        **columnSpan** variables are updated with the vertical and horizontal
        spans of the item.

        **See also** **itemAtPosition** () and **itemAt** ().
        """
        ...
    def hasHeightForWidth(self) -> bool:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#hasHeightForWidth

        **[override virtual] bool QGridLayout::hasHeightForWidth() const**

        Reimplements: **QLayoutItem::hasHeightForWidth() const** .
        """
        ...
    def heightForWidth(self, arg__1: int) -> int:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#heightForWidth

        **[override virtual] int QGridLayout::heightForWidth(int w ) const**

        Reimplements: **QLayoutItem::heightForWidth(int) const** .
        """
        ...
    def horizontalSpacing(self) -> int:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#horizontalSpacing-prop

        **horizontalSpacing : int**

        This property holds the spacing between widgets that are laid out side
        by side

        If no value is explicitly set, the layout's horizontal spacing is
        inherited from the parent layout, or from the style settings for the
        parent widget.

        **Access functions:**

        int **horizontalSpacing** () const
        void **setHorizontalSpacing** (int
        **spacing** )

        **See also** **verticalSpacing** , **QStyle::pixelMetric** (), and
        **PM_LayoutHorizontalSpacing** .
        """
        ...
    def invalidate(self) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#invalidate

        **[override virtual] void QGridLayout::invalidate()**

        Reimplements: **QLayout::invalidate** ().
        """
        ...
    def itemAt(self, index: int) -> PySide6.QtWidgets.QLayoutItem:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#itemAt

        **[override virtual] QLayoutItem *QGridLayout::itemAt(int index )
        const**

        Reimplements: **QLayout::itemAt(int index) const** .
        """
        ...
    def itemAtPosition(self, row: int, column: int) -> PySide6.QtWidgets.QLayoutItem:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#itemAtPosition

        **QLayoutItem *QGridLayout::itemAtPosition(int row , int column )
        const**

        Returns the layout item that occupies cell ( **row** , **column** ), or
        `nullptr` if the cell is empty.

        **See also** **getItemPosition** () and **indexOf** ().
        """
        ...
    def maximumSize(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#maximumSize

        **[override virtual] QSize QGridLayout::maximumSize() const**

        Reimplements: **QLayout::maximumSize() const** .
        """
        ...
    def minimumHeightForWidth(self, arg__1: int) -> int:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#minimumHeightForWidth

        **[override virtual] int QGridLayout::minimumHeightForWidth(int w )
        const**

        Reimplements: **QLayoutItem::minimumHeightForWidth(int w) const** .
        """
        ...
    def minimumSize(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#minimumSize

        **[override virtual] QSize QGridLayout::minimumSize() const**

        Reimplements: **QLayout::minimumSize() const** .
        """
        ...
    def originCorner(self) -> PySide6.QtCore.Qt.Corner:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#originCorner

        **Qt::Corner QGridLayout::originCorner() const**

        Returns the corner that's used for the grid's origin, i.e. for position
        (0, 0).

        **See also** **setOriginCorner** ().
        """
        ...
    def rowCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#rowCount

        **int QGridLayout::rowCount() const**

        Returns the number of rows in this grid.
        """
        ...
    def rowMinimumHeight(self, row: int) -> int:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#rowMinimumHeight

        **int QGridLayout::rowMinimumHeight(int row ) const**

        Returns the minimum width set for row **row**.

        **See also** **setRowMinimumHeight** ().
        """
        ...
    def rowStretch(self, row: int) -> int:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#rowStretch

        **int QGridLayout::rowStretch(int row ) const**

        Returns the stretch factor for row **row**.

        **See also** **setRowStretch** ().
        """
        ...
    def setColumnMinimumWidth(self, column: int, minSize: int) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#setColumnMinimumWidth

        **void QGridLayout::setColumnMinimumWidth(int column , int minSize )**

        Sets the minimum width of column **column** to **minSize** pixels.

        **See also** **columnMinimumWidth** () and **setRowMinimumHeight** ().
        """
        ...
    def setColumnStretch(self, column: int, stretch: int) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#setColumnStretch

        **void QGridLayout::setColumnStretch(int column , int stretch )**

        Sets the stretch factor of column **column** to **stretch**. The first
        column is number 0.

        The stretch factor is relative to the other columns in this grid.
        Columns with a higher stretch factor take more of the available space.

        The default stretch factor is 0. If the stretch factor is 0 and no other
        column in this table can grow at all, the column may still grow.

        An alternative approach is to add spacing using **addItem** () with a
        **QSpacerItem** .

        **See also** **columnStretch** () and **setRowStretch** ().
        """
        ...
    def setDefaultPositioning(
        self, n: int, orient: PySide6.QtCore.Qt.Orientation
    ) -> None: ...
    def setGeometry(self, arg__1: PySide6.QtCore.QRect) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#setGeometry

        **[override virtual] void QGridLayout::setGeometry(const QRect & rect
        )**

        Reimplements: **QLayout::setGeometry** (const QRect &r).
        """
        ...
    def setHorizontalSpacing(self, spacing: int) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#horizontalSpacing-prop

        **horizontalSpacing : int**

        This property holds the spacing between widgets that are laid out side
        by side

        If no value is explicitly set, the layout's horizontal spacing is
        inherited from the parent layout, or from the style settings for the
        parent widget.

        **Access functions:**

        int **horizontalSpacing** () const
        void **setHorizontalSpacing** (int
        **spacing** )

        **See also** **verticalSpacing** , **QStyle::pixelMetric** (), and
        **PM_LayoutHorizontalSpacing** .
        """
        ...
    def setOriginCorner(self, arg__1: PySide6.QtCore.Qt.Corner) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#setOriginCorner

        **void QGridLayout::setOriginCorner(Qt::Corner corner )**

        Sets the grid's origin corner, i.e. position (0, 0), to **corner**.

        **See also** **originCorner** ().
        """
        ...
    def setRowMinimumHeight(self, row: int, minSize: int) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#setRowMinimumHeight

        **void QGridLayout::setRowMinimumHeight(int row , int minSize )**

        Sets the minimum height of row **row** to **minSize** pixels.

        **See also** **rowMinimumHeight** () and **setColumnMinimumWidth** ().
        """
        ...
    def setRowStretch(self, row: int, stretch: int) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#setRowStretch

        **void QGridLayout::setRowStretch(int row , int stretch )**

        Sets the stretch factor of row **row** to **stretch**. The first row is
        number 0.

        The stretch factor is relative to the other rows in this grid. Rows with
        a higher stretch factor take more of the available space.

        The default stretch factor is 0. If the stretch factor is 0 and no other
        row in this table can grow at all, the row may still grow.

        **See also** **rowStretch** (), **setRowMinimumHeight** (), and
        **setColumnStretch** ().
        """
        ...
    def setSpacing(self, spacing: int) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#setSpacing

        **[override virtual] void QGridLayout::setSpacing(int spacing )**

        Reimplements an access function for property: **QLayout::spacing** .

        This function sets both the vertical and horizontal spacing to
        **spacing**.

        **See also** **spacing** (), **setVerticalSpacing** (), and
        **setHorizontalSpacing** ().
        """
        ...
    def setVerticalSpacing(self, spacing: int) -> None:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#verticalSpacing-prop

        **verticalSpacing : int**

        This property holds the spacing between widgets that are laid out on top
        of each other

        If no value is explicitly set, the layout's vertical spacing is
        inherited from the parent layout, or from the style settings for the
        parent widget.

        **Access functions:**

        int **verticalSpacing** () const
        void **setVerticalSpacing** (int
        **spacing** )

        **See also** **horizontalSpacing** , **QStyle::pixelMetric** (), and
        **PM_LayoutHorizontalSpacing** .

        **Member Function Documentation**
        """
        ...
    def sizeHint(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#sizeHint

        **[override virtual] QSize QGridLayout::sizeHint() const**

        Reimplements: **QLayoutItem::sizeHint() const** .
        """
        ...
    def spacing(self) -> int:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#spacing

        **[override virtual] int QGridLayout::spacing() const**

        Reimplements an access function for property: **QLayout::spacing** .

        If the vertical spacing is equal to the horizontal spacing, this
        function returns that value; otherwise it return -1.

        **See also** **setSpacing** (), **verticalSpacing** (), and
        **horizontalSpacing** ().
        """
        ...
    def takeAt(self, index: int) -> PySide6.QtWidgets.QLayoutItem:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#takeAt

        **[override virtual] QLayoutItem *QGridLayout::takeAt(int index )**

        Reimplements: **QLayout::takeAt** (int index).
        """
        ...
    def verticalSpacing(self) -> int:
        """
        https://doc.qt.io/qt-6/qgridlayout.html#verticalSpacing-prop

        **verticalSpacing : int**

        This property holds the spacing between widgets that are laid out on top
        of each other

        If no value is explicitly set, the layout's vertical spacing is
        inherited from the parent layout, or from the style settings for the
        parent widget.

        **Access functions:**

        int **verticalSpacing** () const
        void **setVerticalSpacing** (int
        **spacing** )

        **See also** **horizontalSpacing** , **QStyle::pixelMetric** (), and
        **PM_LayoutHorizontalSpacing** .

        **Member Function Documentation**
        """
        ...
