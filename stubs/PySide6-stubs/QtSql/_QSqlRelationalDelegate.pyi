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
PySide6.QtSql, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtSql
import PySide6.QtWidgets

class QSqlRelationalDelegate(PySide6.QtWidgets.QStyledItemDelegate):
    """
    https://doc.qt.io/qt-6/qsqlrelationaldelegate.html

    **Detailed Description**

    Unlike the default delegate, QSqlRelationalDelegate provides a combobox for
    fields that are foreign keys into other tables. To use the class, simply
    call **QAbstractItemView::setItemDelegate** () on the view with an instance
    of QSqlRelationalDelegate:

    std::unique_ptr<**QTableView** > view{new **QTableView** };
    view->setModel(model);
            view->setItemDelegate(new
    **QSqlRelationalDelegate** (view.get()));

    The **Relational Table Model**  example (shown below) illustrates how to use
    QSqlRelationalDelegate in conjunction with **QSqlRelationalTableModel**  to
    provide tables with foreign key support.

    ![](images/relationaltable.png)

    **See also** **QSqlRelationalTableModel**  and **Model/View Programming** .
    """

    def __init__(self, aParent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qsqlrelationaldelegate.html#QSqlRelationalDelegat
        e

        **QSqlRelationalDelegate::QSqlRelationalDelegate(QObject * parent =
        nullptr)**

        Constructs a QSqlRelationalDelegate object with the given **parent**.
        """
        ...
    def createEditor(
        self,
        aParent: PySide6.QtWidgets.QWidget,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qsqlrelationaldelegate.html#createEditor

        **[override virtual] QWidget
        *QSqlRelationalDelegate::createEditor(QWidget * parent , const
        QStyleOptionViewItem & option , const QModelIndex & index ) const**

        Reimplements: **QStyledItemDelegate::createEditor(QWidget *parent, const
        QStyleOptionViewItem &option, const QModelIndex &index) const** .
        """
        ...
    def setEditorData(
        self,
        editor: PySide6.QtWidgets.QWidget,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None: ...
    def setModelData(
        self,
        editor: PySide6.QtWidgets.QWidget,
        model: PySide6.QtCore.QAbstractItemModel,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsqlrelationaldelegate.html#setModelData

        **[override virtual] void QSqlRelationalDelegate::setModelData(QWidget *
        editor , QAbstractItemModel * model , const QModelIndex & index )
        const**

        Reimplements: **QStyledItemDelegate::setModelData(QWidget *editor,
        QAbstractItemModel *model, const QModelIndex &index) const** .
        """
        ...
