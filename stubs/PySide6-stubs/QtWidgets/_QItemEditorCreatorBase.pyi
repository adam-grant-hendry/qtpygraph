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

class QItemEditorCreatorBase:
    """
    https://doc.qt.io/qt-6/qitemeditorcreatorbase.html

    **Detailed Description**

    QItemEditorCreatorBase objects are specialized widget factories that provide
    editor widgets for one particular **QVariant**  data type. They are used by
    **QItemEditorFactory**  to create editors for **QStyledItemDelegate** s.
    Creator bases must be registered with **QItemEditorFactory::registerEditor**
    ().

    An editor should provide a user property for the data it edits.
    QItemDelagates can then access the property using Qt's **meta-object
    system**  to set and retrieve the editing data. A property is set as the
    user property with the USER keyword:

    Q_PROPERTY(**QColor**  color READ color WRITE setColor USER true)

    If the editor does not provide a user property, it must return the name of
    the property from **valuePropertyName** (); delegates will then use the name
    to access the property. If a user property exists, item delegates will not
    call **valuePropertyName** ().

    **QStandardItemEditorCreator**  is a convenience template class that can be
    used to register widgets without the need to subclass
    QItemEditorCreatorBase.

    **See also** **QStandardItemEditorCreator** , **QItemEditorFactory** ,
    **Model/View Programming** , and **Color Editor Factory Example** .
    """

    def __init__(self) -> None: ...
    def createWidget(
        self, parent: PySide6.QtWidgets.QWidget
    ) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qitemeditorcreatorbase.html#createWidget

        **[pure virtual] QWidget *QItemEditorCreatorBase::createWidget(QWidget *
        parent ) const**

        Returns an editor widget with the given **parent**.

        When implementing this function in subclasses of this class, you must
        construct and return new editor widgets with the parent widget
        specified.
        """
        ...
    def valuePropertyName(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qitemeditorcreatorbase.html#valuePropertyName

        **[pure virtual] QByteArray QItemEditorCreatorBase::valuePropertyName()
        const**

        Returns the name of the property used to get and set values in the
        creator's editor widgets.

        When implementing this function in subclasses, you must ensure that the
        editor widget's property specified by this function can accept the type
        the creator is registered for. For example, a creator which constructs
        **QCheckBox**  widgets to edit boolean values would return the
        **checkable**  property name from this function, and must be registered
        in the item editor factory for the **QMetaType::Bool**  type.

        Note: Since Qt 4.2 the item delegates query the user property of
        widgets, and only call this function if the widget has no user property.
        You can override this behavior by reimplementing
        **QAbstractItemDelegate::setModelData** () and
        **QAbstractItemDelegate::setEditorData** ().

        **See also** **QMetaObject::userProperty** () and
        **QItemEditorFactory::registerEditor** ().
        """
        ...
