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

class QGraphicsGridLayout(PySide6.QtWidgets.QGraphicsLayout):
    """
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html

    **Detailed Description**

    The most common way to use QGraphicsGridLayout is to construct an object on
    the heap with no parent, add widgets and layouts by calling **addItem** (),
    and finally assign the layout to a widget by calling
    **QGraphicsWidget::setLayout** (). QGraphicsGridLayout automatically
    computes the dimensions of the grid as you add items.

    **QGraphicsScene**  scene;
        **QGraphicsWidget**  *textEdit =
    scene.addWidget(new **QTextEdit** );
        **QGraphicsWidget**  *pushButton =
    scene.addWidget(new **QPushButton** );

        **QGraphicsGridLayout**
    *layout = new **QGraphicsGridLayout** ;
        layout->addItem(textEdit, 0, 0);
    layout->addItem(pushButton, 0, 1);

        **QGraphicsWidget**  *form = new
    **QGraphicsWidget** ;
        form->setLayout(layout);
        scene.addItem(form);

    The layout takes ownership of the items. In some cases when the layout item
    also inherits from **QGraphicsItem**  (such as **QGraphicsWidget** ) there
    will be a ambiguity in ownership because the layout item belongs to two
    ownership hierarchies. See the documentation of
    **QGraphicsLayoutItem::setOwnedByLayout** () how to handle this. You can
    access each item in the layout by calling **count** () and **itemAt** ().
    Calling **removeAt** () will remove an item from the layout, without
    destroying it.

    **Size Hints and Size Policies in QGraphicsGridLayout**

    QGraphicsGridLayout respects each item's size hints and size policies, and
    when a cell in the grid has more space than the items can fill, each item is
    arranged according to the layout's alignment for that item. You can set an
    alignment for each item by calling **setAlignment** (), and check the
    alignment for any item by calling **alignment** (). You can also set the
    alignment for an entire row or column by calling **setRowAlignment** () and
    **setColumnAlignment** () respectively. By default, items are aligned to the
    top left.

    **See also** **QGraphicsLinearLayout**  and **QGraphicsWidget** .
    """

    def __init__(
        self, parent: PySide6.QtWidgets.QGraphicsLayoutItem | None = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#QGraphicsGridLayout

        **QGraphicsGridLayout::QGraphicsGridLayout(QGraphicsLayoutItem * parent
        = nullptr)**

        Constructs a QGraphicsGridLayout instance. **parent** is passed to
        **QGraphicsLayout** 's constructor.
        """
        ...
    @overload
    def addItem(
        self,
        item: PySide6.QtWidgets.QGraphicsLayoutItem,
        row: int,
        column: int,
        alignment: PySide6.QtCore.Qt.Alignment = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#addItem

        **void QGraphicsGridLayout::addItem(QGraphicsLayoutItem * item , int row
        , int column , int rowSpan , int columnSpan , Qt::Alignment alignment =
        Qt::Alignment())**

        Adds **item** to the grid on **row** and **column**. You can specify a
        **rowSpan** and **columnSpan** and an optional **alignment**.
        """
        ...
    @overload
    def addItem(
        self,
        item: PySide6.QtWidgets.QGraphicsLayoutItem,
        row: int,
        column: int,
        rowSpan: int,
        columnSpan: int,
        alignment: PySide6.QtCore.Qt.Alignment = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#addItem-1

        **void QGraphicsGridLayout::addItem(QGraphicsLayoutItem * item , int row
        , int column , Qt::Alignment alignment = Qt::Alignment())**

        Adds **item** to the grid on **row** and **column**. You can specify an
        optional **alignment** for **item**.
        """
        ...
    def alignment(
        self, item: PySide6.QtWidgets.QGraphicsLayoutItem
    ) -> PySide6.QtCore.Qt.Alignment:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#alignment

        **Qt::Alignment QGraphicsGridLayout::alignment(QGraphicsLayoutItem *
        item ) const**

        Returns the alignment for **item**.

        **See also** **setAlignment** ().
        """
        ...
    def columnAlignment(self, column: int) -> PySide6.QtCore.Qt.Alignment:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnAlignment

        **Qt::Alignment QGraphicsGridLayout::columnAlignment(int column )
        const**

        Returns the alignment for **column**.

        **See also** **setColumnAlignment** ().
        """
        ...
    def columnCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnCount

        **int QGraphicsGridLayout::columnCount() const**

        Returns the number of columns in the grid layout. This is always one
        more than the index of the last column that is occupied by a layout item
        (empty columns are counted except for those at the end).
        """
        ...
    def columnMaximumWidth(self, column: int) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnMaximumWidth

        **qreal QGraphicsGridLayout::columnMaximumWidth(int column ) const**

        Returns the maximum width for **column**.

        **See also** **setColumnMaximumWidth** ().
        """
        ...
    def columnMinimumWidth(self, column: int) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnMinimumWidth

        **qreal QGraphicsGridLayout::columnMinimumWidth(int column ) const**

        Returns the minimum width for **column**.

        **See also** **setColumnMinimumWidth** ().
        """
        ...
    def columnPreferredWidth(self, column: int) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnPreferredWidth

        **qreal QGraphicsGridLayout::columnPreferredWidth(int column ) const**

        Returns the preferred width for **column**.

        **See also** **setColumnPreferredWidth** ().
        """
        ...
    def columnSpacing(self, column: int) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnSpacing

        **qreal QGraphicsGridLayout::columnSpacing(int column ) const**

        Returns the column spacing for **column**.

        **See also** **setColumnSpacing** ().
        """
        ...
    def columnStretchFactor(self, column: int) -> int:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnStretchFactor

        **int QGraphicsGridLayout::columnStretchFactor(int column ) const**

        Returns the stretch factor for **column**.

        **See also** **setColumnStretchFactor** ().
        """
        ...
    def count(self) -> int:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#count

        **[override virtual] int QGraphicsGridLayout::count() const**

        Reimplements: **QGraphicsLayout::count() const** .

        Returns the number of layout items in this grid layout.
        """
        ...
    def horizontalSpacing(self) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#horizontalSpacing

        **qreal QGraphicsGridLayout::horizontalSpacing() const**

        Returns the default horizontal spacing for the grid layout.

        **See also** **setHorizontalSpacing** ().
        """
        ...
    def invalidate(self) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#invalidate

        **[override virtual] void QGraphicsGridLayout::invalidate()**

        Reimplements: **QGraphicsLayout::invalidate** ().
        """
        ...
    @overload
    def itemAt(self, index: int) -> PySide6.QtWidgets.QGraphicsLayoutItem:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#itemAt

        **QGraphicsLayoutItem *QGraphicsGridLayout::itemAt(int row , int column
        ) const**

        Returns a pointer to the layout item at ( **row** , **column** ).
        """
        ...
    @overload
    def itemAt(self, row: int, column: int) -> PySide6.QtWidgets.QGraphicsLayoutItem:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#itemAt-1

        **[override virtual] QGraphicsLayoutItem
        *QGraphicsGridLayout::itemAt(int index ) const**

        Reimplements: **QGraphicsLayout::itemAt(int i) const** .

        Returns the layout item at **index** , or `nullptr` if there is no
        layout item at this index.
        """
        ...
    def removeAt(self, index: int) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#removeAt

        **[override virtual] void QGraphicsGridLayout::removeAt(int index )**

        Reimplements: **QGraphicsLayout::removeAt** (int index).

        Removes the layout item at **index** without destroying it. Ownership of
        the item is transferred to the caller.

        **See also** **addItem** ().
        """
        ...
    def removeItem(self, item: PySide6.QtWidgets.QGraphicsLayoutItem) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#removeItem

        **void QGraphicsGridLayout::removeItem(QGraphicsLayoutItem * item )**

        Removes the layout item **item** without destroying it. Ownership of the
        item is transferred to the caller.

        **See also** **addItem** ().
        """
        ...
    def rowAlignment(self, row: int) -> PySide6.QtCore.Qt.Alignment:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowAlignment

        **Qt::Alignment QGraphicsGridLayout::rowAlignment(int row ) const**

        Returns the alignment of **row**.

        **See also** **setRowAlignment** ().
        """
        ...
    def rowCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowCount

        **int QGraphicsGridLayout::rowCount() const**

        Returns the number of rows in the grid layout. This is always one more
        than the index of the last row that is occupied by a layout item (empty
        rows are counted except for those at the end).
        """
        ...
    def rowMaximumHeight(self, row: int) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowMaximumHeight

        **qreal QGraphicsGridLayout::rowMaximumHeight(int row ) const**

        Returns the maximum height for row, **row**.

        **See also** **setRowMaximumHeight** ().
        """
        ...
    def rowMinimumHeight(self, row: int) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowMinimumHeight

        **qreal QGraphicsGridLayout::rowMinimumHeight(int row ) const**

        Returns the minimum height for row, **row**.

        **See also** **setRowMinimumHeight** ().
        """
        ...
    def rowPreferredHeight(self, row: int) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowPreferredHeight

        **qreal QGraphicsGridLayout::rowPreferredHeight(int row ) const**

        Returns the preferred height for row, **row**.

        **See also** **setRowPreferredHeight** ().
        """
        ...
    def rowSpacing(self, row: int) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowSpacing

        **qreal QGraphicsGridLayout::rowSpacing(int row ) const**

        Returns the row spacing for **row**.

        **See also** **setRowSpacing** ().
        """
        ...
    def rowStretchFactor(self, row: int) -> int:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowStretchFactor

        **int QGraphicsGridLayout::rowStretchFactor(int row ) const**

        Returns the stretch factor for **row**.

        **See also** **setRowStretchFactor** ().
        """
        ...
    def setAlignment(
        self,
        item: PySide6.QtWidgets.QGraphicsLayoutItem,
        alignment: PySide6.QtCore.Qt.Alignment,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setAlignment

        **void QGraphicsGridLayout::setAlignment(QGraphicsLayoutItem * item ,
        Qt::Alignment alignment )**

        Sets the alignment for **item** to **alignment**.

        **See also** **alignment** ().
        """
        ...
    def setColumnAlignment(
        self, column: int, alignment: PySide6.QtCore.Qt.Alignment
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnAlignment

        **void QGraphicsGridLayout::setColumnAlignment(int column ,
        Qt::Alignment alignment )**

        Sets the alignment for **column** to **alignment**.

        **See also** **columnAlignment** ().
        """
        ...
    def setColumnFixedWidth(self, column: int, width: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnFixedWidth

        **void QGraphicsGridLayout::setColumnFixedWidth(int column , qreal width
        )**

        Sets the fixed width of **column** to **width**.
        """
        ...
    def setColumnMaximumWidth(self, column: int, width: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnMaximumWidth

        **void QGraphicsGridLayout::setColumnMaximumWidth(int column , qreal
        width )**

        Sets the maximum width of **column** to **width**.

        **See also** **columnMaximumWidth** ().
        """
        ...
    def setColumnMinimumWidth(self, column: int, width: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnMinimumWidth

        **void QGraphicsGridLayout::setColumnMinimumWidth(int column , qreal
        width )**

        Sets the minimum width for **column** to **width**.

        **See also** **columnMinimumWidth** ().
        """
        ...
    def setColumnPreferredWidth(self, column: int, width: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnPreferredWidth

        **void QGraphicsGridLayout::setColumnPreferredWidth(int column , qreal
        width )**

        Sets the preferred width for **column** to **width**.

        **See also** **columnPreferredWidth** ().
        """
        ...
    def setColumnSpacing(self, column: int, spacing: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnSpacing

        **void QGraphicsGridLayout::setColumnSpacing(int column , qreal spacing
        )**

        Sets the spacing for **column** to **spacing**.

        **See also** **columnSpacing** ().
        """
        ...
    def setColumnStretchFactor(self, column: int, stretch: int) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnStretchFactor

        **void QGraphicsGridLayout::setColumnStretchFactor(int column , int
        stretch )**

        Sets the stretch factor for **column** to **stretch**.

        **See also** **columnStretchFactor** ().
        """
        ...
    def setGeometry(self, rect: PySide6.QtCore.QRectF | PySide6.QtCore.QRect) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setGeometry

        **[override virtual] void QGraphicsGridLayout::setGeometry(const QRectF
        & rect )**

        Reimplements: **QGraphicsLayoutItem::setGeometry** (const QRectF &rect).

        Sets the bounding geometry of the grid layout to **rect**.
        """
        ...
    def setHorizontalSpacing(self, spacing: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setHorizontalSpacing

        **void QGraphicsGridLayout::setHorizontalSpacing(qreal spacing )**

        Sets the default horizontal spacing for the grid layout to **spacing**.

        **See also** **horizontalSpacing** ().
        """
        ...
    def setRowAlignment(self, row: int, alignment: PySide6.QtCore.Qt.Alignment) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowAlignment

        **void QGraphicsGridLayout::setRowAlignment(int row , Qt::Alignment
        alignment )**

        Sets the alignment of **row** to **alignment**.

        **See also** **rowAlignment** ().
        """
        ...
    def setRowFixedHeight(self, row: int, height: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowFixedHeight

        **void QGraphicsGridLayout::setRowFixedHeight(int row , qreal height )**

        Sets the fixed height for row, **row** , to **height**.
        """
        ...
    def setRowMaximumHeight(self, row: int, height: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowMaximumHeight

        **void QGraphicsGridLayout::setRowMaximumHeight(int row , qreal height
        )**

        Sets the maximum height for row, **row** , to **height**.

        **See also** **rowMaximumHeight** ().
        """
        ...
    def setRowMinimumHeight(self, row: int, height: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowMinimumHeight

        **void QGraphicsGridLayout::setRowMinimumHeight(int row , qreal height
        )**

        Sets the minimum height for row, **row** , to **height**.

        **See also** **rowMinimumHeight** ().
        """
        ...
    def setRowPreferredHeight(self, row: int, height: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowPreferredHeight

        **void QGraphicsGridLayout::setRowPreferredHeight(int row , qreal height
        )**

        Sets the preferred height for row, **row** , to **height**.

        **See also** **rowPreferredHeight** ().
        """
        ...
    def setRowSpacing(self, row: int, spacing: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowSpacing

        **void QGraphicsGridLayout::setRowSpacing(int row , qreal spacing )**

        Sets the spacing for **row** to **spacing**.

        **See also** **rowSpacing** ().
        """
        ...
    def setRowStretchFactor(self, row: int, stretch: int) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowStretchFactor

        **void QGraphicsGridLayout::setRowStretchFactor(int row , int stretch
        )**

        Sets the stretch factor for **row** to **stretch**.

        **See also** **rowStretchFactor** ().
        """
        ...
    def setSpacing(self, spacing: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setSpacing

        **void QGraphicsGridLayout::setSpacing(qreal spacing )**

        Sets the grid layout's default spacing, both vertical and horizontal, to
        **spacing**.

        **See also** **rowSpacing** () and **columnSpacing** ().
        """
        ...
    def setVerticalSpacing(self, spacing: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setVerticalSpacing

        **void QGraphicsGridLayout::setVerticalSpacing(qreal spacing )**

        Sets the default vertical spacing for the grid layout to **spacing**.

        **See also** **verticalSpacing** ().
        """
        ...
    def sizeHint(
        self,
        which: PySide6.QtCore.Qt.SizeHint,
        constraint: PySide6.QtCore.QSizeF | PySide6.QtCore.QSize = ...,
    ) -> PySide6.QtCore.QSizeF:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#sizeHint

        **[override virtual] QSizeF QGraphicsGridLayout::sizeHint(Qt::SizeHint
        which , const QSizeF & constraint = QSizeF()) const**

        Reimplements: **QGraphicsLayoutItem::sizeHint(Qt::SizeHint which, const
        QSizeF &constraint) const** .
        """
        ...
    def verticalSpacing(self) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsgridlayout.html#verticalSpacing

        **qreal QGraphicsGridLayout::verticalSpacing() const**

        Returns the default vertical spacing for the grid layout.

        **See also** **setVerticalSpacing** ().
        """
        ...
