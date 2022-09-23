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
PySide6.QtCharts, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCharts
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QHPieModelMapper(PySide6.QtCharts.QPieModelMapper):
    """
    https://doc.qt.io/qt-6/qhpiemodelmapper.html

    **Detailed Description**

    Model mappers enable using a data model derived from the
    **QAbstractItemModel**  class as a data source for a chart. A horizontal
    model mapper is used to create a connection between a data model and
    **QPieSeries** , so that each column in the data model defines a pie slice
    and each row maps to the label or the value of the pie slice.

    Both model and pie series properties can be used to manipulate the data. The
    model mapper keeps the pie series and the data model in sync.
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#QHPieModelMapper

        **QHPieModelMapper::QHPieModelMapper(QObject * parent = nullptr)**

        Constructs a mapper object that is a child of **parent**.
        """
        ...
    def columnCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#columnCount-prop

        **columnCount : int**

        This property holds the number of columns of the model that are mapped
        as the data for the pie series.

        The minimum and default value is -1 (number limited to the number of
        columns in the model).

        **Access functions:**

        int **columnCount** () const
        void **setColumnCount** (int
        **columnCount** )

        **Notifier signal:**

        void ****columnCountChanged** ** ()
        """
        ...
    def firstColumn(self) -> int:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#firstColumn-prop

        **firstColumn : int**

        This property holds the column of the model that contains the first
        slice value.

        The minimum and default value is 0.

        **Access functions:**

        int **firstColumn** () const
        void **setFirstColumn** (int
        **firstColumn** )

        **Notifier signal:**

        void ****firstColumnChanged** ** ()
        """
        ...
    def labelsRow(self) -> int:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#labelsRow

        **int QHPieModelMapper::labelsRow() const**

        Returns the row of the model that is kept in sync with the labels of the
        pie's slices.

        **Note:** Getter function for property labelsRow.

        **See also** **setLabelsRow** ().
        """
        ...
    def model(self) -> PySide6.QtCore.QAbstractItemModel:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#model-prop

        **model : QAbstractItemModel***

        This property holds the model that is used by the mapper.

        **Access functions:**

        QAbstractItemModel * **model** () const
        void **setModel**
        (QAbstractItemModel * **model** )

        **Notifier signal:**

        void ****modelReplaced** ** ()
        """
        ...
    def series(self) -> PySide6.QtCharts.QPieSeries:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#series-prop

        **series : QPieSeries***

        This property holds the pie series that is used by the mapper.

        All the data in the series is discarded when it is set to the mapper.
        When a new series is specified, the old series is disconnected (but it
        preserves its data).

        **Access functions:**

        QPieSeries * **series** () const
        void **setSeries** (QPieSeries *
        **series** )

        **Notifier signal:**

        void ****seriesReplaced** ** ()
        """
        ...
    def setColumnCount(self, columnCount: int) -> None:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#columnCount-prop

        **columnCount : int**

        This property holds the number of columns of the model that are mapped
        as the data for the pie series.

        The minimum and default value is -1 (number limited to the number of
        columns in the model).

        **Access functions:**

        int **columnCount** () const
        void **setColumnCount** (int
        **columnCount** )

        **Notifier signal:**

        void ****columnCountChanged** ** ()
        """
        ...
    def setFirstColumn(self, firstColumn: int) -> None:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#firstColumn-prop

        **firstColumn : int**

        This property holds the column of the model that contains the first
        slice value.

        The minimum and default value is 0.

        **Access functions:**

        int **firstColumn** () const
        void **setFirstColumn** (int
        **firstColumn** )

        **Notifier signal:**

        void ****firstColumnChanged** ** ()
        """
        ...
    def setLabelsRow(self, labelsRow: int) -> None:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#setLabelsRow

        **void QHPieModelMapper::setLabelsRow(int labelsRow )**

        Sets the model row that is kept in sync with the pie slices' labels to
        **labelsRow**.

        **Note:** Setter function for property **labelsRow** .

        **See also** **labelsRow** ().
        """
        ...
    def setModel(self, model: PySide6.QtCore.QAbstractItemModel) -> None:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#model-prop

        **model : QAbstractItemModel***

        This property holds the model that is used by the mapper.

        **Access functions:**

        QAbstractItemModel * **model** () const
        void **setModel**
        (QAbstractItemModel * **model** )

        **Notifier signal:**

        void ****modelReplaced** ** ()
        """
        ...
    def setSeries(self, series: PySide6.QtCharts.QPieSeries) -> None:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#series-prop

        **series : QPieSeries***

        This property holds the pie series that is used by the mapper.

        All the data in the series is discarded when it is set to the mapper.
        When a new series is specified, the old series is disconnected (but it
        preserves its data).

        **Access functions:**

        QPieSeries * **series** () const
        void **setSeries** (QPieSeries *
        **series** )

        **Notifier signal:**

        void ****seriesReplaced** ** ()
        """
        ...
    def setValuesRow(self, valuesRow: int) -> None:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#setValuesRow

        **void QHPieModelMapper::setValuesRow(int valuesRow )**

        Sets the model row that is kept in sync with the pie slices' values to
        **valuesRow**.

        **Note:** Setter function for property **valuesRow** .

        **See also** **valuesRow** ().
        """
        ...
    def valuesRow(self) -> int:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#valuesRow

        **int QHPieModelMapper::valuesRow() const**

        Returns the row of the model that is kept in sync with the values of the
        pie's slices.

        **Note:** Getter function for property valuesRow.

        **See also** **setValuesRow** ().
        """
        ...
    @property
    def columnCountChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#columnCountChanged

        **[signal] void QHPieModelMapper::columnCountChanged()**

        This signal is emitted when the number of columns changes.

        **Note:** Notifier signal for property **columnCount** .
        """
        ...
    @property
    def firstColumnChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#firstColumnChanged

        **[signal] void QHPieModelMapper::firstColumnChanged()**

        This signal is emitted when the first column changes.

        **Note:** Notifier signal for property **firstColumn** .
        """
        ...
    @property
    def labelsRowChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#labelsRowChanged

        **[signal] void QHPieModelMapper::labelsRowChanged()**

        This signal is emitted when the labels row changes.

        **Note:** Notifier signal for property **labelsRow** .
        """
        ...
    @property
    def modelReplaced(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#modelReplaced

        **[signal] void QHPieModelMapper::modelReplaced()**

        This signal is emitted when the model that the mapper is connected to
        changes.

        **Note:** Notifier signal for property **model** .
        """
        ...
    @property
    def seriesReplaced(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#seriesReplaced

        **[signal] void QHPieModelMapper::seriesReplaced()**

        This signal is emitted when the series that the mapper is connected to
        changes.

        **Note:** Notifier signal for property **series** .
        """
        ...
    @property
    def valuesRowChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qhpiemodelmapper.html#valuesRowChanged

        **[signal] void QHPieModelMapper::valuesRowChanged()**

        This signal is emitted when the values row changes.

        **Note:** Notifier signal for property **valuesRow** .
        """
        ...
