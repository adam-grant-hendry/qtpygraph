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
PySide6.QtQml, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtNetwork
import PySide6.QtQml

class QQmlProperty:
    """
    https://doc.qt.io/qt-6/qqmlproperty.html

    **Detailed Description**

    As QML uses Qt's meta-type system all of the existing **QMetaObject**
    classes can be used to introspect and interact with objects created by QML.
    However, some of the new features provided by QML - such as type safety and
    attached properties - are most easily used through the QQmlProperty class
    that simplifies some of their natural complexity.

    Unlike **QMetaProperty**  which represents a property on a class type,
    QQmlProperty encapsulates a property on a specific object instance. To read
    a property's value, programmers create a QQmlProperty instance and call the
    **read** () method. Likewise to write a property value the **write** ()
    method is used.

    For example, for the following QML code:

    // MyItem.qml
        import QtQuick 2.0

        **Text**  { text: "A bit of
    text" }

    The **Text**  object's properties could be accessed using QQmlProperty, like
    this:

    #include <QQmlProperty>
        #include <QGraphicsObject>

        ...
    **QQuickView**  view(**QUrl** ::fromLocalFile("MyItem.qml"));
    **QQmlProperty**  property(view.rootObject(), "font.pixelSize");
    **qWarning** () << "Current pixel size:" << property.read().toInt();
    property.write(24);
        **qWarning** () << "Pixel size should now be 24:" <<
    property.read().toInt();
    """

    InvalidCategory: QQmlProperty.PropertyTypeCategory = ...
    List: QQmlProperty.PropertyTypeCategory = ...
    Object: QQmlProperty.PropertyTypeCategory = ...
    Normal: QQmlProperty.PropertyTypeCategory = ...
    Invalid: QQmlProperty.Type = ...
    Property: QQmlProperty.Type = ...
    SignalProperty: QQmlProperty.Type = ...

    class PropertyTypeCategory(IntFlag):
        InvalidCategory: QQmlProperty.PropertyTypeCategory = ...
        List: QQmlProperty.PropertyTypeCategory = ...
        Object: QQmlProperty.PropertyTypeCategory = ...
        Normal: QQmlProperty.PropertyTypeCategory = ...

    class Type(IntFlag):
        Invalid: QQmlProperty.Type = ...
        Property: QQmlProperty.Type = ...
        SignalProperty: QQmlProperty.Type = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty

        **QQmlProperty::QQmlProperty()**

        Create an invalid QQmlProperty.
        """
        ...
    @overload
    def __init__(self, arg__1: PySide6.QtCore.QObject) -> None:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty-1

        **QQmlProperty::QQmlProperty(QObject * obj )**

        Creates a QQmlProperty for the default property of **obj**. If there is
        no default property, an invalid QQmlProperty will be created.
        """
        ...
    @overload
    def __init__(
        self, arg__1: PySide6.QtCore.QObject, arg__2: PySide6.QtQml.QQmlContext
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty-2

        **QQmlProperty::QQmlProperty(QObject * obj , QQmlContext * ctxt )**

        Creates a QQmlProperty for the default property of **obj** using the
        **context**  **ctxt**. If there is no default property, an invalid
        QQmlProperty will be created.
        """
        ...
    @overload
    def __init__(
        self, arg__1: PySide6.QtCore.QObject, arg__2: PySide6.QtQml.QQmlEngine
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty-3

        **QQmlProperty::QQmlProperty(QObject * obj , QQmlEngine * engine )**

        Creates a QQmlProperty for the default property of **obj** using the
        environment for instantiating QML components that is provided by
        **engine**. If there is no default property, an invalid QQmlProperty
        will be created.
        """
        ...
    @overload
    def __init__(self, arg__1: PySide6.QtCore.QObject, arg__2: str) -> None:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty-4

        **QQmlProperty::QQmlProperty(QObject * obj , const QString & name )**

        Creates a QQmlProperty for the property **name** of **obj**.
        """
        ...
    @overload
    def __init__(
        self,
        arg__1: PySide6.QtCore.QObject,
        arg__2: str,
        arg__3: PySide6.QtQml.QQmlContext,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty-5

        **QQmlProperty::QQmlProperty(QObject * obj , const QString & name ,
        QQmlContext * ctxt )**

        Creates a QQmlProperty for the property **name** of **obj** using the
        **context**  **ctxt**.

        Creating a QQmlProperty without a context will render some properties -
        like attached properties - inaccessible.
        """
        ...
    @overload
    def __init__(
        self,
        arg__1: PySide6.QtCore.QObject,
        arg__2: str,
        arg__3: PySide6.QtQml.QQmlEngine,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty-6

        **QQmlProperty::QQmlProperty(QObject * obj , const QString & name ,
        QQmlEngine * engine )**

        Creates a QQmlProperty for the property **name** of **obj** using the
        environment for instantiating QML components that is provided by
        **engine**.
        """
        ...
    @overload
    def __init__(
        self, arg__1: PySide6.QtQml.QQmlProperty | PySide6.QtCore.QObject
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty-7

        **QQmlProperty::QQmlProperty(const QQmlProperty & other )**

        Create a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    @overload
    def connectNotifySignal(self, dest: PySide6.QtCore.QObject, method: int) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#connectNotifySignal

        **bool QQmlProperty::connectNotifySignal(QObject * dest , const char *
        slot ) const**

        Connects the property's change notifier signal to the specified **slot**
        of the **dest** object and returns true. Returns false if this
        metaproperty does not represent a regular Qt property or if it has no
        change notifier signal, or if the **dest** object does not have the
        specified **slot**.

        **Note:** **slot** should be passed using the SLOT() macro so it is
        correctly identified.
        """
        ...
    @overload
    def connectNotifySignal(self, dest: PySide6.QtCore.QObject, slot: bytes) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#connectNotifySignal-1

        **bool QQmlProperty::connectNotifySignal(QObject * dest , int method )
        const**

        Connects the property's change notifier signal to the specified
        **method** of the **dest** object and returns true. Returns false if
        this metaproperty does not represent a regular Qt property or if it has
        no change notifier signal, or if the **dest** object does not have the
        specified **method**.
        """
        ...
    def hasNotifySignal(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#hasNotifySignal

        **bool QQmlProperty::hasNotifySignal() const**

        Returns true if the property has a change notifier signal, otherwise
        false.
        """
        ...
    def index(self) -> int:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#index

        **int QQmlProperty::index() const**

        Return the Qt metaobject index of the property.
        """
        ...
    def isBindable(self) -> bool: ...
    def isDesignable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#isDesignable

        **bool QQmlProperty::isDesignable() const**

        Returns true if the property is designable, otherwise false.
        """
        ...
    def isProperty(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#isProperty

        **bool QQmlProperty::isProperty() const**

        Returns true if this **QQmlProperty**  represents a regular Qt property.
        """
        ...
    def isResettable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#isResettable

        **bool QQmlProperty::isResettable() const**

        Returns true if the property is resettable, otherwise false.
        """
        ...
    def isSignalProperty(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#isSignalProperty

        **bool QQmlProperty::isSignalProperty() const**

        Returns true if this **QQmlProperty**  represents a QML signal property.
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#isValid

        **bool QQmlProperty::isValid() const**

        Returns true if the **QQmlProperty**  refers to a valid property,
        otherwise false.
        """
        ...
    def isWritable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#isWritable

        **bool QQmlProperty::isWritable() const**

        Returns true if the property is writable, otherwise false.
        """
        ...
    def method(self) -> PySide6.QtCore.QMetaMethod:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#method

        **QMetaMethod QQmlProperty::method() const**

        Return the **QMetaMethod**  for this property if it is a
        **SignalProperty** , otherwise returns an invalid **QMetaMethod** .
        """
        ...
    def name(self) -> str:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#name

        **QString QQmlProperty::name() const**

        Return the name of this QML property.

        **Note:** Getter function for property name.
        """
        ...
    def needsNotifySignal(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#needsNotifySignal

        **bool QQmlProperty::needsNotifySignal() const**

        Returns true if the property needs a change notifier signal for bindings
        to remain upto date, false otherwise.

        Some properties, such as attached properties or those whose value never
        changes, do not require a change notifier.
        """
        ...
    def object(self) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#object

        **QObject *QQmlProperty::object() const**

        Returns the **QQmlProperty** 's **QObject** .

        **Note:** Getter function for property object.
        """
        ...
    def property(self) -> PySide6.QtCore.QMetaProperty:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#property

        **QMetaProperty QQmlProperty::property() const**

        Returns the **Qt property**  associated with this QML property.
        """
        ...
    def propertyMetaType(self) -> PySide6.QtCore.QMetaType:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#propertyMetaType

        **QMetaType QQmlProperty::propertyMetaType() const**

        Returns the metatype of the property.

        **See also** **propertyType** .
        """
        ...
    def propertyType(self) -> int:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#propertyType

        **int QQmlProperty::propertyType() const**

        Returns the metatype id of the property, or **QMetaType::UnknownType**
        if the property has no metatype.

        **See also** **propertyMetaType** .
        """
        ...
    def propertyTypeCategory(self) -> PySide6.QtQml.QQmlProperty.PropertyTypeCategory:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#propertyTypeCategory

        **QQmlProperty::PropertyTypeCategory
        QQmlProperty::propertyTypeCategory() const**

        Returns the property category.
        """
        ...
    def propertyTypeName(self) -> bytes:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#propertyTypeName

        **const char *QQmlProperty::propertyTypeName() const**

        Returns the type name of the property, or 0 if the property has no type
        name.
        """
        ...
    @overload
    @staticmethod
    def read(arg__1: PySide6.QtCore.QObject, arg__2: str) -> Any:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#read

        **QVariant QQmlProperty::read() const**

        Returns the property value.
        """
        ...
    @overload
    @staticmethod
    def read(
        arg__1: PySide6.QtCore.QObject, arg__2: str, arg__3: PySide6.QtQml.QQmlContext
    ) -> Any:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#read-1

        **[static] QVariant QQmlProperty::read(const QObject * object , const
        QString & name )**

        Return the **name** property value of **object**. This method is
        equivalent to:

        **QQmlProperty**  p(object, name);
            p.read();
        """
        ...
    @overload
    @staticmethod
    def read(
        arg__1: PySide6.QtCore.QObject, arg__2: str, arg__3: PySide6.QtQml.QQmlEngine
    ) -> Any:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#read-2

        **[static] QVariant QQmlProperty::read(const QObject * object , const
        QString & name , QQmlContext * ctxt )**

        Return the **name** property value of **object** using the **context**
        **ctxt**. This method is equivalent to:

        **QQmlProperty**  p(object, name, context);
            p.read();
        """
        ...
    @overload
    def read(self) -> Any:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#read-3

        **[static] QVariant QQmlProperty::read(const QObject * object , const
        QString & name , QQmlEngine * engine )**

        Return the **name** property value of **object** using the environment
        for instantiating QML components that is provided by **engine**. . This
        method is equivalent to:

        **QQmlProperty**  p(object, name, engine);
            p.read();
        """
        ...
    def reset(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#reset

        **bool QQmlProperty::reset() const**

        Resets the property and returns true if the property is resettable. If
        the property is not resettable, nothing happens and false is returned.
        """
        ...
    def type(self) -> PySide6.QtQml.QQmlProperty.Type:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#type

        **QQmlProperty::Type QQmlProperty::type() const**

        Returns the type of the property.
        """
        ...
    @overload
    @staticmethod
    def write(arg__1: PySide6.QtCore.QObject, arg__2: str, arg__3: Any) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#write

        **bool QQmlProperty::write(const QVariant & value ) const**

        Sets the property value to **value**. Returns `true` on success, or
        `false` if the property can't be set because the **value** is the wrong
        type, for example.
        """
        ...
    @overload
    @staticmethod
    def write(
        arg__1: PySide6.QtCore.QObject,
        arg__2: str,
        arg__3: Any,
        arg__4: PySide6.QtQml.QQmlContext,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#write-1

        **[static] bool QQmlProperty::write(QObject * object , const QString &
        name , const QVariant & value )**

        Writes **value** to the **name** property of **object**. This method is
        equivalent to:

        **QQmlProperty**  p(object, name);
            p.write(value);

        Returns `true` on success, `false` otherwise.
        """
        ...
    @overload
    @staticmethod
    def write(
        arg__1: PySide6.QtCore.QObject,
        arg__2: str,
        arg__3: Any,
        arg__4: PySide6.QtQml.QQmlEngine,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#write-2

        **[static] bool QQmlProperty::write(QObject * object , const QString &
        name , const QVariant & value , QQmlContext * ctxt )**

        Writes **value** to the **name** property of **object** using the
        **context**  **ctxt**. This method is equivalent to:

        **QQmlProperty**  p(object, name, ctxt);
            p.write(value);

        Returns `true` on success, `false` otherwise.
        """
        ...
    @overload
    def write(self, arg__1: Any) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlproperty.html#write-3

        **[static] bool QQmlProperty::write(QObject * object , const QString &
        name , const QVariant & value , QQmlEngine * engine )**

        Writes **value** to the **name** property of **object** using the
        environment for instantiating QML components that is provided by
        **engine**. This method is equivalent to:

        **QQmlProperty**  p(object, name, engine);
            p.write(value);

        Returns `true` on success, `false` otherwise.
        """
        ...
