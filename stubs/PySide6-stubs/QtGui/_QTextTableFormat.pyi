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

from collections.abc import Sequence
from typing import overload

import PySide6.QtCore
import PySide6.QtGui

class QTextTableFormat(PySide6.QtGui.QTextFrameFormat):
    """
    https://doc.qt.io/qt-6/qtexttableformat.html

    **Detailed Description**

    A table is a group of cells ordered into rows and columns. Each table
    contains at least one row and one column. Each cell contains a block. Tables
    in rich text documents are formatted using the properties defined in this
    class.

    Tables are horizontally justified within their parent frame according to the
    table's alignment. This can be read with the **alignment** () function and
    set with **setAlignment** ().

    Cells within the table are separated by cell spacing. The number of pixels
    between cells is set with **setCellSpacing** () and read with
    **cellSpacing** (). The contents of each cell is surrounded by cell padding.
    The number of pixels between each cell edge and its contents is set with
    **setCellPadding** () and read with **cellPadding** ().

    ![](images/qtexttableformat-cell.png)

    The table's background color can be read with the **background** ()
    function, and can be specified with **setBackground** (). The background
    color of each cell can be set independently, and will control the color of
    the cell within the padded area.

    The table format also provides a way to constrain the widths of the columns
    in the table. Columns can be assigned a fixed width, a variable width, or a
    percentage of the available width (see **QTextLength** ). The **columns** ()
    function returns the number of columns with constraints, and the
    **columnWidthConstraints** () function returns the constraints defined for
    the table. These quantities can also be set by calling
    **setColumnWidthConstraints** () with a list containing new constraints. If
    no constraints are required, **clearColumnWidthConstraints** () can be used
    to remove them.

    **See also** **QTextTable** , **QTextTableCell** , and **QTextLength** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#QTextTableFormat

        **QTextTableFormat::QTextTableFormat()**

        Constructs a new table format object.
        """
        ...
    @overload
    def __init__(self, QTextTableFormat: PySide6.QtGui.QTextTableFormat) -> None:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#QTextTableFormat

        **QTextTableFormat::QTextTableFormat()**

        Constructs a new table format object.
        """
        ...
    @overload
    def __init__(self, fmt: PySide6.QtGui.QTextFormat) -> None:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#QTextTableFormat

        **QTextTableFormat::QTextTableFormat()**

        Constructs a new table format object.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def alignment(self) -> PySide6.QtCore.Qt.Alignment:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#alignment

        **Qt::Alignment QTextTableFormat::alignment() const**

        Returns the table's alignment.

        **See also** **setAlignment** ().
        """
        ...
    def borderCollapse(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#borderCollapse

        **[since 5.14] bool QTextTableFormat::borderCollapse() const**

        Returns true if borderCollapse is enabled.

        This function was introduced in Qt 5.14.

        **See also** **setBorderCollapse** ().
        """
        ...
    def cellPadding(self) -> float:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#cellPadding

        **qreal QTextTableFormat::cellPadding() const**

        Returns the table's cell padding. This describes the distance between
        the border of a cell and its contents.

        **See also** **setCellPadding** ().
        """
        ...
    def cellSpacing(self) -> float:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#cellSpacing

        **qreal QTextTableFormat::cellSpacing() const**

        Returns the table's cell spacing. This describes the distance between
        adjacent cells.

        **See also** **setCellSpacing** ().
        """
        ...
    def clearColumnWidthConstraints(self) -> None:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#clearColumnWidthConstraints

        **void QTextTableFormat::clearColumnWidthConstraints()**

        Clears the column width constraints for the table.

        **See also** **columnWidthConstraints** () and
        **setColumnWidthConstraints** ().
        """
        ...
    def columnWidthConstraints(self) -> list[PySide6.QtGui.QTextLength]:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#columnWidthConstraints

        **QList<QTextLength> QTextTableFormat::columnWidthConstraints() const**

        Returns a list of constraints used by this table format to control the
        appearance of columns in a table.

        **See also** **setColumnWidthConstraints** ().
        """
        ...
    def columns(self) -> int:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#columns

        **int QTextTableFormat::columns() const**

        Returns the number of columns specified by the table format.
        """
        ...
    def headerRowCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#headerRowCount

        **int QTextTableFormat::headerRowCount() const**

        Returns the number of rows in the table that define the header.

        **See also** **setHeaderRowCount** ().
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#isValid

        **bool QTextTableFormat::isValid() const**

        Returns `true` if this table format is valid; otherwise returns `false`.
        """
        ...
    def setAlignment(self, alignment: PySide6.QtCore.Qt.Alignment) -> None:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#setAlignment

        **void QTextTableFormat::setAlignment(Qt::Alignment alignment )**

        Sets the table's **alignment**.

        **See also** **alignment** ().
        """
        ...
    def setBorderCollapse(self, borderCollapse: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#setBorderCollapse

        **[since 5.14] void QTextTableFormat::setBorderCollapse(bool
        borderCollapse )**

        Enabling **borderCollapse** will have the following implications:

        * The borders and grid of the table will be rendered following the CSS
        table `border-collapse`: `collapse` rules
          * Setting the `border`
        property to a minimum value of `1` will render a one pixel solid inner
        table grid using the **borderBrush**  property and an outer border as
        specified
          * The various border style properties of
        **QTextTableCellFormat**  can be used to customize the grid and have
        precedence over the border and grid of the table
          * The **cellSpacing**
        property will be ignored
          * For print pagination:
            * Columns
        continued on a page will not have their top cell border rendered
            *
        Repeated header rows will always have their bottom cell border rendered

        With **borderCollapse**  disabled, cell borders can still be styled
        using **QTextTableCellFormat**  but styling will be applied only within
        the cell's frame, which is probably not very useful in practice.

        This function was introduced in Qt 5.14.

        **See also** **borderCollapse** (), **setBorder** (), **setBorderBrush**
        (), **setBorderStyle** (), and **QTextTableCellFormat** .
        """
        ...
    def setCellPadding(self, padding: float) -> None:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#setCellPadding

        **void QTextTableFormat::setCellPadding(qreal padding )**

        Sets the cell **padding** for the table. This determines the distance
        between the border of a cell and its contents.

        **See also** **cellPadding** ().
        """
        ...
    def setCellSpacing(self, spacing: float) -> None:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#setCellSpacing

        **void QTextTableFormat::setCellSpacing(qreal spacing )**

        Sets the cell **spacing** for the table. This determines the distance
        between adjacent cells.

        This property will be ignored if **borderCollapse**  is enabled.

        **See also** **cellSpacing** ().
        """
        ...
    def setColumnWidthConstraints(
        self, constraints: Sequence[PySide6.QtGui.QTextLength]
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#setColumnWidthConstraints

        **void QTextTableFormat::setColumnWidthConstraints(const
        QList<QTextLength> & constraints )**

        Sets the column width **constraints** for the table.

        **See also** **columnWidthConstraints** () and
        **clearColumnWidthConstraints** ().
        """
        ...
    def setColumns(self, columns: int) -> None:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#columns

        **int QTextTableFormat::columns() const**

        Returns the number of columns specified by the table format.
        """
        ...
    def setHeaderRowCount(self, count: int) -> None:
        """
        https://doc.qt.io/qt-6/qtexttableformat.html#setHeaderRowCount

        **void QTextTableFormat::setHeaderRowCount(int count )**

        Declares the first **count** rows of the table as table header. The
        table header rows get repeated when a table is broken across a page
        boundary.

        **See also** **headerRowCount** ().
        """
        ...
