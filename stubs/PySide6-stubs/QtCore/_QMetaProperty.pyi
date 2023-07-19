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
PySide6.QtCore, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import Any, overload

import PySide6.QtCore

class QMetaProperty:
    """
    https://doc.qt.io/qt-6/qmetaproperty.html

    **Detailed Description**

    Property meta-data is obtained from an object's meta-object. See
    **QMetaObject::property** () and **QMetaObject::propertyCount** () for
    details.

    **Property Meta-Data**

    A property has a **name** () and a type(), as well as various attributes
    that specify its behavior: **isReadable** (), **isWritable** (),
    **isDesignable** (), **isScriptable** (), **revision** (), and **isStored**
    ().

    If the property is an enumeration, **isEnumType** () returns `true`; if the
    property is an enumeration that is also a flag (i.e. its values can be
    combined using the OR operator), **isEnumType** () and **isFlagType** ()
    both return true. The enumerator for these types is available from
    **enumerator** ().

    The property's values are set and retrieved with **read** (), **write** (),
    and **reset** (); they can also be changed through **QObject** 's set and
    get functions. See **QObject::setProperty** () and **QObject::property** ()
    for details.

    **Copying and Assignment**

    QMetaProperty objects can be copied by value. However, each copy will refer
    to the same underlying property meta-data.

    **See also** **QMetaObject** , **QMetaEnum** , **QMetaMethod** , and **Qt's
    Property System** .
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QMetaProperty: PySide6.QtCore.QMetaProperty) -> None: ...
    @staticmethod
    def __copy__() -> None: ...
    def enumerator(self) -> PySide6.QtCore.QMetaEnum:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#enumerator

        **QMetaEnum QMetaProperty::enumerator() const**

        Returns the enumerator if this property's type is an enumerator type;
        otherwise the returned value is undefined.

        **See also** **isEnumType** () and **isFlagType** ().
        """
        ...
    def hasNotifySignal(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#hasNotifySignal

        **bool QMetaProperty::hasNotifySignal() const**

        Returns `true` if this property has a corresponding change notify
        signal; otherwise returns `false`.

        **See also** **notifySignal** ().
        """
        ...
    def hasStdCppSet(self) -> bool: ...
    def isAlias(self) -> bool: ...
    def isBindable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isBindable

        **[since 6.0] bool QMetaProperty::isBindable() const**

        Returns `true` if the `Q_PROPERTY()` exposes binding functionality;
        otherwise returns false.

        This implies that you can create bindings that use this property as a
        dependency or install QPropertyObserver objects on this property. Unless
        the property is readonly, you can also set a binding on this property.

        This function was introduced in Qt 6.0.

        **See also** **QProperty** , **isWritable** (), and **bindable** ().
        """
        ...
    def isConstant(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isConstant

        **bool QMetaProperty::isConstant() const**

        Returns `true` if the property is constant; otherwise returns `false`.

        A property is constant if the `Q_PROPERTY()`'s `CONSTANT` attribute is
        set.
        """
        ...
    def isDesignable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isDesignable

        **bool QMetaProperty::isDesignable() const**

        Returns `false` if the `Q_PROPERTY()`'s `DESIGNABLE` attribute is false;
        otherwise returns `true`.

        **See also** **isScriptable** () and **isStored** ().
        """
        ...
    def isEnumType(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isEnumType

        **bool QMetaProperty::isEnumType() const**

        Returns `true` if the property's type is an enumeration value; otherwise
        returns `false`.

        **See also** **enumerator** () and **isFlagType** ().
        """
        ...
    def isFinal(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isFinal

        **bool QMetaProperty::isFinal() const**

        Returns `true` if the property is final; otherwise returns `false`.

        A property is final if the `Q_PROPERTY()`'s `FINAL` attribute is set.
        """
        ...
    def isFlagType(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isFlagType

        **bool QMetaProperty::isFlagType() const**

        Returns `true` if the property's type is an enumeration value that is
        used as a flag; otherwise returns `false`.

        Flags can be combined using the OR operator. A flag type is implicitly
        also an enum type.

        **See also** **isEnumType** (), **enumerator** (), and
        **QMetaEnum::isFlag** ().
        """
        ...
    def isReadable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isReadable

        **bool QMetaProperty::isReadable() const**

        Returns `true` if this property is readable; otherwise returns `false`.

        **See also** **isWritable** (), **read** (), and **isValid** ().
        """
        ...
    def isRequired(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isRequired

        **[since 5.15] bool QMetaProperty::isRequired() const**

        Returns `true` if the property is required; otherwise returns `false`.

        A property is final if the `Q_PROPERTY()`'s `REQUIRED` attribute is set.

        This function was introduced in Qt 5.15.
        """
        ...
    def isResettable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isResettable

        **bool QMetaProperty::isResettable() const**

        Returns `true` if this property can be reset to a default value;
        otherwise returns `false`.

        **See also** **reset** ().
        """
        ...
    def isScriptable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isScriptable

        **bool QMetaProperty::isScriptable() const**

        Returns `false` if the `Q_PROPERTY()`'s `SCRIPTABLE` attribute is false;
        otherwise returns true.

        **See also** **isDesignable** () and **isStored** ().
        """
        ...
    def isStored(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isStored

        **bool QMetaProperty::isStored() const**

        Returns `true` if the property is stored; otherwise returns false.

        The function returns `false` if the `Q_PROPERTY()`'s `STORED` attribute
        is false; otherwise returns true.

        **See also** **isDesignable** () and **isScriptable** ().
        """
        ...
    def isUser(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isUser

        **bool QMetaProperty::isUser() const**

        Returns `false` if the `Q_PROPERTY()`'s `USER` attribute is false.
        Otherwise it returns true, indicating the property is designated as the
        `USER` property, i.e., the one that the user can edit or that is
        significant in some other way.

        **See also** **QMetaObject::userProperty** (), **isDesignable** (), and
        **isScriptable** ().
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isValid

        **bool QMetaProperty::isValid() const**

        Returns `true` if this property is valid (readable); otherwise returns
        `false`.

        **See also** **isReadable** ().
        """
        ...
    def isWritable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#isWritable

        **bool QMetaProperty::isWritable() const**

        Returns `true` if this property is writable; otherwise returns false.

        **See also** **isReadable** () and **write** ().
        """
        ...
    def metaType(self) -> PySide6.QtCore.QMetaType:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#metaType

        **[since 6.0] QMetaType QMetaProperty::metaType() const**

        Returns this property's **QMetaType** .

        This function was introduced in Qt 6.0.

        **See also** **QMetaType** .
        """
        ...
    def name(self) -> bytes:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#name

        **const char *QMetaProperty::name() const**

        Returns this property's name.

        **See also** **type** () and **typeName** ().
        """
        ...
    def notifySignal(self) -> PySide6.QtCore.QMetaMethod:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#notifySignal

        **QMetaMethod QMetaProperty::notifySignal() const**

        Returns the **QMetaMethod**  instance of the property change notifying
        signal if one was specified, otherwise returns an invalid
        **QMetaMethod** .

        **See also** **hasNotifySignal** ().
        """
        ...
    def notifySignalIndex(self) -> int:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#notifySignalIndex

        **int QMetaProperty::notifySignalIndex() const**

        Returns the index of the property change notifying signal if one was
        specified, otherwise returns -1.

        **See also** **hasNotifySignal** ().
        """
        ...
    def propertyIndex(self) -> int:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#propertyIndex

        **int QMetaProperty::propertyIndex() const**

        Returns this property's index.
        """
        ...
    def read(self, obj: PySide6.QtCore.QObject) -> Any:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#read

        **QVariant QMetaProperty::read(const QObject * object ) const**

        Reads the property's value from the given **object**. Returns the value
        if it was able to read it; otherwise returns an invalid variant.

        **See also** **write** (), **reset** (), and **isReadable** ().
        """
        ...
    def readOnGadget(self, gadget: int) -> Any:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#readOnGadget

        **[since 5.5] QVariant QMetaProperty::readOnGadget(const void * gadget )
        const**

        Reads the property's value from the given **gadget**. Returns the value
        if it was able to read it; otherwise returns an invalid variant.

        This function should only be used if this is a property of a
        **Q_GADGET**

        This function was introduced in Qt 5.5.
        """
        ...
    def relativePropertyIndex(self) -> int:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#relativePropertyIndex

        **[since 5.14] int QMetaProperty::relativePropertyIndex() const**

        Returns this property's index relative within the enclosing meta object.

        This function was introduced in Qt 5.14.
        """
        ...
    def reset(self, obj: PySide6.QtCore.QObject) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#reset

        **bool QMetaProperty::reset(QObject * object ) const**

        Resets the property for the given **object** with a reset method.
        Returns `true` if the reset worked; otherwise returns `false`.

        Reset methods are optional; only a few properties support them.

        **See also** **read** () and **write** ().
        """
        ...
    def resetOnGadget(self, gadget: int) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#resetOnGadget

        **[since 5.5] bool QMetaProperty::resetOnGadget(void * gadget ) const**

        Resets the property for the given **gadget** with a reset method.
        Returns `true` if the reset worked; otherwise returns `false`.

        Reset methods are optional; only a few properties support them.

        This function should only be used if this is a property of a
        **Q_GADGET**

        This function was introduced in Qt 5.5.
        """
        ...
    def revision(self) -> int:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#revision

        **[since 5.1] int QMetaProperty::revision() const**

        Returns the property revision if one was specified by REVISION,
        otherwise returns 0.

        This function was introduced in Qt 5.1.
        """
        ...
    def typeId(self) -> int:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#typeId

        **[since 6.0] int QMetaProperty::typeId() const**

        Returns the storage type of the property. This is the same as
        **metaType** ().id().

        This function was introduced in Qt 6.0.

        **See also** **QMetaType** , **typeName** (), and **metaType** ().
        """
        ...
    def typeName(self) -> bytes:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#typeName

        **const char *QMetaProperty::typeName() const**

        Returns the name of this property's type.

        **See also** **type** () and **name** ().
        """
        ...
    def userType(self) -> int:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#userType

        **int QMetaProperty::userType() const**

        Returns this property's user type. The return value is one of the values
        that are registered with **QMetaType** .

        This is equivalent to **metaType** ().id()

        **See also** **type** (), **QMetaType** , **typeName** (), and
        **metaType** ().
        """
        ...
    def write(self, obj: PySide6.QtCore.QObject, value: Any) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#write

        **bool QMetaProperty::write(QObject * object , const QVariant & value )
        const**

        Writes **value** as the property's value to the given **object**.
        Returns true if the write succeeded; otherwise returns `false`.

        If **value** is not of the same type type as the property, a conversion
        is attempted. An empty QVariant() is equivalent to a call to **reset**
        () if this property is resettable, or setting a default-constructed
        object otherwise.

        **See also** **read** (), **reset** (), and **isWritable** ().
        """
        ...
    def writeOnGadget(self, gadget: int, value: Any) -> bool:
        """
        https://doc.qt.io/qt-6/qmetaproperty.html#writeOnGadget

        **[since 5.5] bool QMetaProperty::writeOnGadget(void * gadget , const
        QVariant & value ) const**

        Writes **value** as the property's value to the given **gadget**.
        Returns true if the write succeeded; otherwise returns `false`.

        This function should only be used if this is a property of a
        **Q_GADGET**

        This function was introduced in Qt 5.5.
        """
        ...