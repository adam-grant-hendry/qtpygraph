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

class QItemEditorFactory:
    """
    https://doc.qt.io/qt-6/qitemeditorfactory.html

    **Detailed Description**

    When editing data in an item view, editors are created and displayed by a
    delegate. **QStyledItemDelegate** , which is the delegate by default
    installed on Qt's item views, uses a QItemEditorFactory to create editors
    for it. A default unique instance provided by QItemEditorFactory is used by
    all item delegates. If you set a new default factory with
    **setDefaultFactory** (), the new factory will be used by existing and new
    delegates.

    A factory keeps a collection of **QItemEditorCreatorBase**  instances, which
    are specialized editors that produce editors for one particular **QVariant**
    data type (All Qt models store their data in **QVariant** s).

    **Standard Editing Widgets**

    The standard factory implementation provides editors for a variety of data
    types. These are created whenever a delegate needs to provide an editor for
    data supplied by a model. The following table shows the relationship between
    types and the standard editors provided.

    TypeEditor Widget
    bool**QComboBox**
    double**QDoubleSpinBox**
    int**QSpinBox**
    unsigned int
    **QDate** **QDateEdit**
    **QDateTime**
    **QDateTimeEdit**
    **QPixmap** **QLabel**
    **QString** **QLineEdit**
    **QTime** **QTimeEdit**

    Additional editors can be registered with the **registerEditor** ()
    function.

    **See also** **QStyledItemDelegate** , **Model/View Programming** , and
    **Color Editor Factory Example** .
    """

    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qitemeditorfactory.html#QItemEditorFactory

        **QItemEditorFactory::QItemEditorFactory()**

        Constructs a new item editor factory.
        """
        ...
    def createEditor(
        self, userType: int, parent: PySide6.QtWidgets.QWidget
    ) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qitemeditorfactory.html#createEditor

        **[virtual] QWidget *QItemEditorFactory::createEditor(int userType ,
        QWidget * parent ) const**

        Creates an editor widget with the given **parent** for the specified
        **userType** of data, and returns it as a **QWidget** .

        **See also** **registerEditor** ().
        """
        ...
    @staticmethod
    def defaultFactory() -> PySide6.QtWidgets.QItemEditorFactory:
        """
        https://doc.qt.io/qt-6/qitemeditorfactory.html#defaultFactory

        **[static] const QItemEditorFactory
        *QItemEditorFactory::defaultFactory()**

        Returns the default item editor factory.

        **See also** **setDefaultFactory** ().
        """
        ...
    def registerEditor(
        self, userType: int, creator: PySide6.QtWidgets.QItemEditorCreatorBase
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemeditorfactory.html#registerEditor

        **void QItemEditorFactory::registerEditor(int userType ,
        QItemEditorCreatorBase * creator )**

        Registers an item editor creator specified by **creator** for the given
        **userType** of data.

        **Note:** The factory takes ownership of the item editor creator and
        will destroy it if a new creator for the same type is registered later.

        **See also** **createEditor** ().
        """
        ...
    @staticmethod
    def setDefaultFactory(factory: PySide6.QtWidgets.QItemEditorFactory) -> None:
        """
        https://doc.qt.io/qt-6/qitemeditorfactory.html#setDefaultFactory

        **[static] void QItemEditorFactory::setDefaultFactory(QItemEditorFactory
        * factory )**

        Sets the default item editor factory to the given **factory**. Both new
        and existing delegates will use the new factory.

        **See also** **defaultFactory** ().
        """
        ...
    def valuePropertyName(self, userType: int) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qitemeditorfactory.html#valuePropertyName

        **[virtual] QByteArray QItemEditorFactory::valuePropertyName(int
        userType ) const**

        Returns the property name used to access data for the given **userType**
        of data.
        """
        ...
