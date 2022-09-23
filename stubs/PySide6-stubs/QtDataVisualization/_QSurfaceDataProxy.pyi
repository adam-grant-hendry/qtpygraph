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
PySide6.QtDataVisualization, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from collections.abc import Sequence
from typing import overload

import PySide6.QtCore
import PySide6.QtDataVisualization
import PySide6.QtGui

class QSurfaceDataProxy(PySide6.QtDataVisualization.QAbstractDataProxy):
    """
    https://doc.qt.io/qt-6/qsurfacedataproxy.html

    **Detailed Description**

    A surface data proxy handles surface related data in rows. For this it
    provides two auxiliary typedefs: QtDataVisualization::QSurfaceDataArray and
    QtDataVisualization::QSurfaceDataRow. `QSurfaceDataArray` is a **QList**
    that controls the rows. `QSurfaceDataRow` is a **QList**  that contains
    **QSurfaceDataItem**  objects. For more information about how to feed the
    data to the proxy, see the sample code in the **Q3DSurface**  documentation.

    All rows must have the same number of items.

    QSurfaceDataProxy takes ownership of all `QSurfaceDataRow` objects passed to
    it, whether directly or in a `QSurfaceDataArray` container. To use surface
    data row pointers to directly modify data after adding the array to the
    proxy, the appropriate signal must be emitted to update the graph.

    To make a sensible surface, the x-value of each successive item in all rows
    must be either ascending or descending throughout the row. Similarly, the
    z-value of each successive item in all columns must be either ascending or
    descending throughout the column.

    **Note:** Currently only surfaces with straight rows and columns are fully
    supported. Any row with items that do not have the exact same z-value or any
    column with items that do not have the exact same x-value may get clipped
    incorrectly if the whole surface does not completely fit within the visible
    x-axis or z-axis ranges.

    **Note:** Surfaces with less than two rows or columns are not considered
    valid surfaces and will not be rendered.

    **Note:** On some environments, surfaces with a lot of visible vertices may
    not render, because they exceed the per-draw vertex count supported by the
    graphics driver. This is mostly an issue on 32-bit and OpenGL ES2 platforms.

    **See also** **Qt Data Visualization Data Handling** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#QSurfaceDataProxy

        **QSurfaceDataProxy::QSurfaceDataProxy(QObject * parent = nullptr)**

        Constructs QSurfaceDataProxy with the given **parent**.
        """
        ...
    def addRow(
        self, arg__1: Sequence[PySide6.QtDataVisualization.QSurfaceDataItem]
    ) -> int:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#addRow

        **int QSurfaceDataProxy::addRow(QSurfaceDataRow * row )**

        Adds the new row **row** to the end of an array. The new row must have
        the same number of columns as the rows in the initial array.

        Returns the index of the added row.
        """
        ...
    def addRows(
        self, rows: list[list[PySide6.QtDataVisualization.QSurfaceDataItem]]
    ) -> int:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#addRows

        **int QSurfaceDataProxy::addRows(const QSurfaceDataArray & rows )**

        Adds new **rows** to the end of an array. The new rows must have the
        same number of columns as the rows in the initial array.

        Returns the index of the first added row.
        """
        ...
    def array(self) -> list[list[PySide6.QtDataVisualization.QSurfaceDataItem]]:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#array

        **const QSurfaceDataArray *QSurfaceDataProxy::array() const**

        Returns the pointer to the data array.
        """
        ...
    def columnCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#columnCount-prop

        **[read-only] columnCount : const int**

        This property holds the number of columns in the data array.

        **Access functions:**

        int **columnCount** () const

        **Notifier signal:**

        void **columnCountChanged** (int **count** )
        """
        ...
    def insertRow(
        self,
        arg__1: int,
        arg__2: Sequence[PySide6.QtDataVisualization.QSurfaceDataItem],
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#insertRow

        **void QSurfaceDataProxy::insertRow(int rowIndex , QSurfaceDataRow * row
        )**

        Inserts the new row **row** into **rowIndex**. If **rowIndex** is equal
        to the array size, the rows are added to the end of the array. The new
        row must have the same number of columns as the rows in the initial
        array.
        """
        ...
    def insertRows(
        self,
        rowIndex: int,
        rows: list[list[PySide6.QtDataVisualization.QSurfaceDataItem]],
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#insertRows

        **void QSurfaceDataProxy::insertRows(int rowIndex , const
        QSurfaceDataArray & rows )**

        Inserts new **rows** into **rowIndex**. If **rowIndex** is equal to the
        array size, the rows are added to the end of the array. The new **rows**
        must have the same number of columns as the rows in the initial array.
        """
        ...
    @overload
    def itemAt(
        self, position: PySide6.QtCore.QPoint
    ) -> PySide6.QtDataVisualization.QSurfaceDataItem:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#itemAt

        **const QSurfaceDataItem *QSurfaceDataProxy::itemAt(int rowIndex , int
        columnIndex ) const**

        Returns the pointer to the item at the position specified by
        **rowIndex** and **columnIndex**. It is guaranteed to be valid only
        until the next call that modifies data.
        """
        ...
    @overload
    def itemAt(
        self, rowIndex: int, columnIndex: int
    ) -> PySide6.QtDataVisualization.QSurfaceDataItem:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#itemAt-1

        **const QSurfaceDataItem *QSurfaceDataProxy::itemAt(const QPoint &
        position ) const**

        Returns the pointer to the item at the position **position**. The
        x-value of **position** indicates the row and the y-value indicates the
        column. The item is guaranteed to be valid only until the next call that
        modifies data.
        """
        ...
    def removeRows(self, rowIndex: int, removeCount: int) -> None:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#removeRows

        **void QSurfaceDataProxy::removeRows(int rowIndex , int removeCount )**

        Removes the number of rows specified by **removeCount** starting at the
        position **rowIndex**. Attempting to remove rows past the end of the
        array does nothing.
        """
        ...
    def resetArray(
        self, arg__1: list[list[PySide6.QtDataVisualization.QSurfaceDataItem]]
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#resetArray

        **void QSurfaceDataProxy::resetArray(QSurfaceDataArray * newArray )**

        Takes ownership of the array **newArray**. Clears the existing array if
        the new array differs from it. If the arrays are the same, this function
        just triggers the **arrayReset** () signal.

        Passing a null array deletes the old array and creates a new empty
        array. All rows in **newArray** must be of same length.
        """
        ...
    def rowCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowCount-prop

        **[read-only] rowCount : const int**

        This property holds the number of rows in the data array.

        **Access functions:**

        int **rowCount** () const

        **Notifier signal:**

        void **rowCountChanged** (int **count** )
        """
        ...
    def series(self) -> PySide6.QtDataVisualization.QSurface3DSeries:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#series-prop

        **[read-only] series : QSurface3DSeries* const**

        This property holds the series this proxy is attached to.

        **Access functions:**

        QSurface3DSeries * **series** () const

        **Notifier signal:**

        void **seriesChanged** (QSurface3DSeries * **series** )

        **Member Function Documentation**
        """
        ...
    @overload
    def setItem(
        self,
        position: PySide6.QtCore.QPoint,
        item: (PySide6.QtDataVisualization.QSurfaceDataItem | PySide6.QtGui.QVector3D),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#setItem

        **void QSurfaceDataProxy::setItem(int rowIndex , int columnIndex , const
        QSurfaceDataItem & item )**

        Changes a single item at the position specified by **rowIndex** and
        **columnIndex** to the item **item**.
        """
        ...
    @overload
    def setItem(
        self,
        rowIndex: int,
        columnIndex: int,
        item: (PySide6.QtDataVisualization.QSurfaceDataItem | PySide6.QtGui.QVector3D),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#setItem-1

        **void QSurfaceDataProxy::setItem(const QPoint & position , const
        QSurfaceDataItem & item )**

        Changes a single item at the position **position** to the item **item**.
        The x-value of **position** indicates the row and the y-value indicates
        the column.
        """
        ...
    def setRow(
        self,
        arg__1: int,
        arg__2: Sequence[PySide6.QtDataVisualization.QSurfaceDataItem],
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#setRow

        **void QSurfaceDataProxy::setRow(int rowIndex , QSurfaceDataRow * row
        )**

        Changes an existing row by replacing the row at the position
        **rowIndex** with the new row specified by **row**. The new row can be
        the same as the existing row already stored at the **rowIndex**. The new
        row must have the same number of columns as the row it is replacing.
        """
        ...
    def setRows(
        self,
        rowIndex: int,
        rows: list[list[PySide6.QtDataVisualization.QSurfaceDataItem]],
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#setRows

        **void QSurfaceDataProxy::setRows(int rowIndex , const QSurfaceDataArray
        & rows )**

        Changes existing rows by replacing the rows starting at the position
        **rowIndex** with the new rows specifies by **rows**. The rows in the
        **rows** array can be the same as the existing rows already stored at
        the **rowIndex**. The new rows must have the same number of columns as
        the rows they are replacing.
        """
        ...
    @property
    def arrayReset(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#arrayReset

        **[signal] void QSurfaceDataProxy::arrayReset()**

        This signal is emitted when the data array is reset. If the contents of
        the whole array are changed without calling **resetArray** (), this
        signal needs to be emitted to update the graph.
        """
        ...
    @property
    def columnCountChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def itemChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#itemChanged

        **[signal] void QSurfaceDataProxy::itemChanged(int rowIndex , int
        columnIndex )**

        This signal is emitted when the item at the position specified by
        **rowIndex** and **columnIndex** changes. If the item is changed in the
        array without calling **setItem** (), this signal needs to be emitted to
        update the graph.
        """
        ...
    @property
    def rowCountChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def rowsAdded(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowsAdded

        **[signal] void QSurfaceDataProxy::rowsAdded(int startIndex , int count
        )**

        This signal is emitted when the number of rows specified by **count** is
        added starting at the position **startIndex**. If rows are added to the
        array without calling **addRow** () or **addRows** (), this signal needs
        to be emitted to update the graph.
        """
        ...
    @property
    def rowsChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowsChanged

        **[signal] void QSurfaceDataProxy::rowsChanged(int startIndex , int
        count )**

        This signal is emitted when the number of rows specified by **count** is
        changed starting at the position **startIndex**. If rows are changed in
        the array without calling **setRow** () or **setRows** (), this signal
        needs to be emitted to update the graph.
        """
        ...
    @property
    def rowsInserted(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowsInserted

        **[signal] void QSurfaceDataProxy::rowsInserted(int startIndex , int
        count )**

        This signal is emitted when the number of rows specified by **count** is
        inserted at the position **startIndex**.

        If rows are inserted into the array without calling **insertRow** () or
        **insertRows** (), this signal needs to be emitted to update the graph.
        """
        ...
    @property
    def rowsRemoved(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowsRemoved

        **[signal] void QSurfaceDataProxy::rowsRemoved(int startIndex , int
        count )**

        This signal is emitted when the number of rows specified by **count** is
        removed starting at the position **startIndex**.

        The index is the current array size if the rows were removed from the
        end of the array. If rows are removed from the array without calling
        **removeRows** (), this signal needs to be emitted to update the graph.
        """
        ...
    @property
    def seriesChanged(self) -> PySide6.QtCore.SignalInstance: ...
