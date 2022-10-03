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

from collections.abc import Sequence
from enum import IntFlag
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtNetwork
import PySide6.QtQml

class QJSManagedValue:
    """
    https://doc.qt.io/qt-6/qjsmanagedvalue.html

    **Detailed Description**

    The QJSManagedValue class allows interaction with JavaScript values in most
    ways you can interact with them from JavaScript itself. You can get and set
    properties and prototypes, and you can access arrays. Additionally, you can
    transform the value into the Qt counterparts of JavaScript objects. For
    example, a Url object may be transformed into a **QUrl** .

    A QJSManagedValue is always bound to a particular **QJSEngine** . You cannot
    use it independently. This means that you cannot have a QJSManagedValue from
    one engine be a property or a proptotype of a QJSManagedValue from a
    different engine.

    In contrast to **QJSValue** , almost all values held by QJSManagedValue live
    on the JavaScript heap. There is no inline or unmanaged storage. Therefore,
    you can get the prototype of a primitive value, and you can get the `length`
    property of a string.

    Only default-constructed or moved-from QJSManagedValues do not hold a value
    on the JavaScript heap. They represent `undefined`, which doesn't have any
    properties or prototypes.

    Also in contrast to **QJSValue** , QJSManagedValue does not catch any
    JavaScript exceptions. If an operation on a QJSManagedValue causes an error,
    it will generally return an `undefined` value and **QJSEngine::hasError** ()
    will return `true` afterwards. You can then catch the exception using
    **QJSEngine::catchError** (), or pass it up the stack, at your own
    discretion.

    **Note:** As the reference to the value on the JavaScript heap has to be
    freed on destruction, you cannot move a QJSManagedValue to a different
    thread. The destruction would take place in the new thread, which would
    create a race condition with the garbage collector on the original thread.
    This also means that you cannot hold a QJSManagedValue beyond the lifespan
    of its engine.

    The recommended way of working with a QJSManagedValue is creating it on the
    stack, possibly by moving a **QJSValue**  and adding an engine, then
    performing the necessary operations on it, and finally moving it back into a
    **QJSValue**  for storage. Moving between QJSManagedValue and **QJSValue**
    is fast.
    """

    Undefined: QJSManagedValue.Type = ...
    Boolean: QJSManagedValue.Type = ...
    Number: QJSManagedValue.Type = ...
    String: QJSManagedValue.Type = ...
    Object: QJSManagedValue.Type = ...
    Symbol: QJSManagedValue.Type = ...
    Function: QJSManagedValue.Type = ...

    class Type(IntFlag):
        Undefined: QJSManagedValue.Type = ...
        Boolean: QJSManagedValue.Type = ...
        Number: QJSManagedValue.Type = ...
        String: QJSManagedValue.Type = ...
        Object: QJSManagedValue.Type = ...
        Symbol: QJSManagedValue.Type = ...
        Function: QJSManagedValue.Type = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#QJSManagedValue-1

        **QJSManagedValue::QJSManagedValue()**

        Creates a QJSManagedValue that represents the JavaScript `undefined`
        value. This is the only value not stored on the JavaScript heap. Calling
        **engine** () on a default-constructed QJSManagedValue will return
        nullptr.
        """
        ...
    @overload
    def __init__(self, string: str, engine: PySide6.QtQml.QJSEngine) -> None:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#QJSManagedValue-2

        **QJSManagedValue::QJSManagedValue(QJSValue value , QJSEngine * engine
        )**

        Creates a QJSManagedValue from **value** , using the heap of **engine**.
        If **value** is itself managed and the engine it belongs to is not
        **engine** , the result is an `undefined` value, and a warning is
        generated.
        """
        ...
    @overload
    def __init__(
        self,
        value: PySide6.QtQml.QJSPrimitiveValue | str | float | int,
        engine: PySide6.QtQml.QJSEngine,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#QJSManagedValue-3

        **QJSManagedValue::QJSManagedValue(const QJSPrimitiveValue & value ,
        QJSEngine * engine )**

        Creates a QJSManagedValue from **value** using the heap of **engine**.
        """
        ...
    @overload
    def __init__(
        self,
        value: (
            PySide6.QtQml.QJSValue
            | PySide6.QtQml.QJSValue.SpecialValue
            | str
            | bytes
            | float
            | int
        ),
        engine: PySide6.QtQml.QJSEngine,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#QJSManagedValue-4

        **QJSManagedValue::QJSManagedValue(const QVariant & variant , QJSEngine
        * engine )**

        Creates a QJSManagedValue from **variant** using the heap of **engine**.
        """
        ...
    @overload
    def __init__(self, variant: Any, engine: PySide6.QtQml.QJSEngine) -> None:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#QJSManagedValue-5

        **QJSManagedValue::QJSManagedValue(const QString & string , QJSEngine *
        engine )**

        Creates a QJSManagedValue from **string** using the heap of **engine**.
        """
        ...
    def call(
        self, arguments: Sequence[PySide6.QtQml.QJSValue] = ...
    ) -> PySide6.QtQml.QJSValue:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#call

        **QJSValue QJSManagedValue::call(const QJSValueList & arguments = {})
        const**

        If this **QJSManagedValue**  represents a JavaScript FunctionObject,
        calls it with the given **arguments** , and returns the result.
        Otherwise returns a JavaScript `undefined` value.

        The **arguments** have to be either primitive values or belong to the
        same **QJSEngine**  as this **QJSManagedValue** . Otherwise the call is
        not carried out and a JavaScript `undefined` value is returned.
        """
        ...
    def callAsConstructor(
        self, arguments: Sequence[PySide6.QtQml.QJSValue] = ...
    ) -> PySide6.QtQml.QJSValue:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#callAsConstructor

        **QJSValue QJSManagedValue::callAsConstructor(const QJSValueList &
        arguments = {}) const**

        If this **QJSManagedValue**  represents a JavaScript FunctionObject,
        calls it as constructor with the given **arguments** , and returns the
        result. Otherwise returns a JavaScript `undefined` value.

        The **arguments** have to be either primitive values or belong to the
        same **QJSEngine**  as this **QJSManagedValue** . Otherwise the call is
        not carried out and a JavaScript `undefined` value is returned.
        """
        ...
    def callWithInstance(
        self,
        instance: (
            PySide6.QtQml.QJSValue
            | PySide6.QtQml.QJSValue.SpecialValue
            | str
            | bytes
            | float
            | int
        ),
        arguments: Sequence[PySide6.QtQml.QJSValue] = ...,
    ) -> PySide6.QtQml.QJSValue:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#callWithInstance

        **QJSValue QJSManagedValue::callWithInstance(const QJSValue & instance ,
        const QJSValueList & arguments = {}) const**

        If this **QJSManagedValue**  represents a JavaScript FunctionObject,
        calls it on **instance** with the given **arguments** , and returns the
        result. Otherwise returns a JavaScript `undefined` value.

        The **arguments** and the **instance** have to be either primitive
        values or belong to the same **QJSEngine**  as this **QJSManagedValue**
        . Otherwise the call is not carried out and a JavaScript `undefined`
        value is returned.
        """
        ...
    @overload
    def deleteProperty(self, arrayIndex: int) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#deleteProperty

        **bool QJSManagedValue::deleteProperty(const QString & name )**

        Deletes the property **name** from this **QJSManagedValue** . Returns
        `true` if the deletion succeeded, or `false` otherwise.
        """
        ...
    @overload
    def deleteProperty(self, name: str) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#deleteProperty-1

        **bool QJSManagedValue::deleteProperty(quint32 arrayIndex )**

        Deletes the value stored at **arrayIndex** from this **QJSManagedValue**
        . Returns `true` if the deletion succeeded, or `false` otherwise.
        """
        ...
    def engine(self) -> PySide6.QtQml.QJSEngine:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#engine

        **QJSEngine *QJSManagedValue::engine() const**

        Returns the **QJSEngine**  this **QJSManagedValue**  belongs to. Mind
        that the engine is always valid, unless the **QJSManagedValue**  is
        default-constructed or moved from. In the latter case a nullptr is
        returned.
        """
        ...
    def equals(self, other: PySide6.QtQml.QJSManagedValue) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#equals

        **bool QJSManagedValue::equals(const QJSManagedValue & other ) const**

        Invokes the JavaScript '==' operator on this **QJSManagedValue**  and
        **other** , and returns the result.

        **See also** **strictlyEquals** .
        """
        ...
    @overload
    def hasOwnProperty(self, arrayIndex: int) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#hasOwnProperty

        **bool QJSManagedValue::hasOwnProperty(const QString & name ) const**

        Returns `true` if this **QJSManagedValue**  has a property **name** ,
        otherwise returns `false`. The properties of the prototype chain are not
        considered.
        """
        ...
    @overload
    def hasOwnProperty(self, name: str) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#hasOwnProperty-1

        **bool QJSManagedValue::hasOwnProperty(quint32 arrayIndex ) const**

        Returns `true` if this **QJSManagedValue**  has an array index
        **arrayIndex** , otherwise returns `false`. The properties of the
        prototype chain are not considered.
        """
        ...
    @overload
    def hasProperty(self, arrayIndex: int) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#hasProperty

        **bool QJSManagedValue::hasProperty(const QString & name ) const**

        Returns `true` if this **QJSManagedValue**  has a property **name** ,
        otherwise returns `false`. The properties of the prototype chain are
        considered.
        """
        ...
    @overload
    def hasProperty(self, name: str) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#hasProperty-1

        **bool QJSManagedValue::hasProperty(quint32 arrayIndex ) const**

        Returns `true` if this **QJSManagedValue**  has an array index
        **arrayIndex** , otherwise returns `false`. The properties of the
        prototype chain are considered.
        """
        ...
    def isArray(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isArray

        **bool QJSManagedValue::isArray() const**

        Returns `true` if this value represents a JavaScript Array object, or
        `false` otherwise.
        """
        ...
    def isBoolean(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isBoolean

        **bool QJSManagedValue::isBoolean() const**

        Returns `true` if the type of this **QJSManagedValue**  is `boolean`, or
        `false` otherwise.
        """
        ...
    def isDate(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isDate

        **bool QJSManagedValue::isDate() const**

        Returns `true` if this value represents a JavaScript Date object, or
        `false` otherwise.
        """
        ...
    def isError(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isError

        **bool QJSManagedValue::isError() const**

        Returns `true` if this value represents a JavaScript Error object, or
        `false` otherwise.
        """
        ...
    def isFunction(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isFunction

        **bool QJSManagedValue::isFunction() const**

        Returns `true` if the type of this **QJSManagedValue**  is `function`,
        `false` otherwise.
        """
        ...
    def isInteger(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isInteger

        **bool QJSManagedValue::isInteger() const**

        Returns `true` if this **QJSManagedValue**  holds an integer value, or
        `false` otherwise. The storage format of a number does not affect the
        result of any operations performed on it, but if an integer is stored,
        many operations are faster.
        """
        ...
    def isJsMetaType(self) -> bool: ...
    def isNull(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isNull

        **bool QJSManagedValue::isNull() const**

        Returns `true` if this **QJSManagedValue**  holds the JavaScript `null`
        value, or `false` otherwise.
        """
        ...
    def isNumber(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isNumber

        **bool QJSManagedValue::isNumber() const**

        Returns `true` if the type of this **QJSManagedValue**  is `number`, or
        `false` otherwise.
        """
        ...
    def isObject(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isObject

        **bool QJSManagedValue::isObject() const**

        Returns `true` if the type of this **QJSManagedValue**  is `object`, or
        `false` otherwise.
        """
        ...
    def isQMetaObject(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isQMetaObject

        **bool QJSManagedValue::isQMetaObject() const**

        Returns `true` if this value represents a **QMetaObject**  pointer
        managed on the JavaScript heap, or `false` otherwise.
        """
        ...
    def isQObject(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isQObject

        **bool QJSManagedValue::isQObject() const**

        Returns `true` if this value represents a **QObject**  pointer managed
        on the JavaScript heap, or `false` otherwise.
        """
        ...
    def isRegularExpression(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isRegularExpression

        **bool QJSManagedValue::isRegularExpression() const**

        Returns `true` if this value represents a JavaScript regular expression
        object, or `false` otherwise.
        """
        ...
    def isString(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isString

        **bool QJSManagedValue::isString() const**

        Returns `true` if the type of this **QJSManagedValue**  is `string`, or
        `false` otherwise.
        """
        ...
    def isSymbol(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isSymbol

        **bool QJSManagedValue::isSymbol() const**

        Returns `true` if the type of this **QJSManagedValue**  is `symbol`, or
        `false` otherwise.
        """
        ...
    def isUndefined(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isUndefined

        **bool QJSManagedValue::isUndefined() const**

        Returns `true` if the type of this **QJSManagedValue**  is `undefined`,
        or `false` otherwise.
        """
        ...
    def isUrl(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isUrl

        **bool QJSManagedValue::isUrl() const**

        Returns `true` if this value represents a JavaScript Url object, or
        `false` otherwise.
        """
        ...
    def isVariant(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#isVariant

        **bool QJSManagedValue::isVariant() const**

        Returns `true` if this value represents a **QVariant**  managed on the
        JavaScript heap, or `false` otherwise.
        """
        ...
    def jsMetaInstantiate(
        self, values: Sequence[PySide6.QtQml.QJSValue] = ...
    ) -> PySide6.QtQml.QJSManagedValue: ...
    def jsMetaMembers(self) -> list[str]: ...
    def jsMetaType(self) -> PySide6.QtQml.QJSManagedValue: ...
    @overload
    def property(self, arrayIndex: int) -> PySide6.QtQml.QJSValue:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#property

        **QJSValue QJSManagedValue::property(const QString & name ) const**

        Returns the property **name** of this **QJSManagedValue** . The
        prototype chain is searched if the property is not found on the actual
        object.

        **See also** **setProperty** ().
        """
        ...
    @overload
    def property(self, name: str) -> PySide6.QtQml.QJSValue:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#property-1

        **QJSValue QJSManagedValue::property(quint32 arrayIndex ) const**

        Returns the property stored at **arrayIndex** of this
        **QJSManagedValue** . The prototype chain is searched if the property is
        not found on the actual object.
        """
        ...
    def prototype(self) -> PySide6.QtQml.QJSManagedValue:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#prototype

        **QJSManagedValue QJSManagedValue::prototype() const**

        Returns the prototype for this **QJSManagedValue** . This works on any
        value. You can, for example retrieve the JavaScript `boolean` prototype
        from a `boolean` value.

        **See also** **setPrototype** ().
        """
        ...
    @overload
    def setProperty(
        self,
        arrayIndex: int,
        value: (
            PySide6.QtQml.QJSValue
            | PySide6.QtQml.QJSValue.SpecialValue
            | str
            | bytes
            | float
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#setProperty

        **void QJSManagedValue::setProperty(const QString & name , const
        QJSValue & value )**

        Sets the property **name** to **value** on this **QJSManagedValue** .
        This can only be done on JavaScript values of type `object`. Furhermore,
        **value** has to be either a primitive or belong to the same engine as
        this value.

        **See also** **property** ().
        """
        ...
    @overload
    def setProperty(
        self,
        name: str,
        value: (
            PySide6.QtQml.QJSValue
            | PySide6.QtQml.QJSValue.SpecialValue
            | str
            | bytes
            | float
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#setProperty-1

        **void QJSManagedValue::setProperty(quint32 arrayIndex , const QJSValue
        & value )**

        Stores the **value** at **arrayIndex** in this **QJSManagedValue** .
        This can only be done on JavaScript values of type `object`, and it's
        not recommended if the value is not an array. Furhermore, **value** has
        to be either a primitive or belong to the same engine as this value.
        """
        ...
    def setPrototype(self, prototype: PySide6.QtQml.QJSManagedValue) -> None:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#setPrototype

        **void QJSManagedValue::setPrototype(const QJSManagedValue & prototype
        )**

        Sets the prototype of this **QJSManagedValue**  to **prototype**. A
        precondition is that **prototype** belongs to the same **QJSEngine**  as
        this **QJSManagedValue**  and is an object (including null).
        Furthermore, this **QJSManagedValue**  has to be an object (excluding
        null), too, and you cannot create prototype cycles.

        **See also** **prototype** ().
        """
        ...
    def strictlyEquals(self, other: PySide6.QtQml.QJSManagedValue) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#strictlyEquals

        **bool QJSManagedValue::strictlyEquals(const QJSManagedValue & other )
        const**

        Invokes the JavaScript '===' operator on this **QJSManagedValue**  and
        **other** , and returns the result.

        **See also** **equals** .
        """
        ...
    def toBoolean(self) -> bool:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#toBoolean

        **bool QJSManagedValue::toBoolean() const**

        Converts the manged value to a boolean. If the managed value holds a
        boolean, that one is returned. Otherwise a boolean coercion by
        JavaScript rules is performed.
        """
        ...
    def toDateTime(self) -> PySide6.QtCore.QDateTime:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#toDateTime

        **QDateTime QJSManagedValue::toDateTime() const**

        If this **QJSManagedValue**  holds a JavaScript Date object, returns an
        equivalent **QDateTime** . Otherwise returns an invalid one.
        """
        ...
    def toInteger(self) -> int:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#toInteger

        **int QJSManagedValue::toInteger() const**

        Converts the manged value to an integer. This first converts the value
        to a number by the rules of **toNumber** (), and then clamps it into the
        integer range by the rules given for coercing the arguments to
        JavaScript bit shift operators into 32bit integers.

        Internally, the value may already be stored as an integer, in which case
        a fast path is taken.

        **Note:** Conversion of a managed value to a number can throw an
        exception. In particular, symbols cannot be coerced into numbers, or a
        custom valueOf() method may throw. In this case the result is 0 and the
        engine carries an error after the conversion.

        **Note:** The JavaScript rules for coercing numbers into 32bit integers
        are unintuitive.
        """
        ...
    def toJSValue(self) -> PySide6.QtQml.QJSValue:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#toJSValue

        **QJSValue QJSManagedValue::toJSValue() const**

        Copies this **QJSManagedValue**  into a new **QJSValue** . This is less
        efficient than move-constructing a **QJSValue**  from a
        **QJSManagedValue** , but retains the **QJSManagedValue** .
        """
        ...
    def toNumber(self) -> float:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#toNumber

        **double QJSManagedValue::toNumber() const**

        Converts the manged value to a number. If the managed value holds a
        number, that one is returned. Otherwise a number coercion by JavaScript
        rules is performed.

        **Note:** Conversion of a managed value to a number can throw an
        exception. In particular, symbols cannot be coerced into numbers, or a
        custom valueOf() method may throw. In this case the result is 0 and the
        engine carries an error after the conversion.
        """
        ...
    def toPrimitive(self) -> PySide6.QtQml.QJSPrimitiveValue:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#toPrimitive

        **QJSPrimitiveValue QJSManagedValue::toPrimitive() const**

        Converts the manged value to a **QJSPrimitiveValue** . If the managed
        value holds a type supported by **QJSPrimitiveValue** , the value is
        copied. Otherwise the value is converted to a string, and the string is
        stored in **QJSPrimitiveValue** .

        **Note:** Conversion of a managed value to a string can throw an
        exception. In particular, symbols cannot be coerced into strings, or a
        custom **toString** () method may throw. In this case the result is the
        undefined value and the engine carries an error after the conversion.
        """
        ...
    def toQMetaObject(self) -> PySide6.QtCore.QMetaObject:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#toQMetaObject

        **const QMetaObject *QJSManagedValue::toQMetaObject() const**

        If this **QJSManagedValue**  holds a **QMetaObject**  pointer, returns
        it. Otherwise returns nullptr.
        """
        ...
    def toQObject(self) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#toQObject

        **QObject *QJSManagedValue::toQObject() const**

        If this **QJSManagedValue**  holds a **QObject**  pointer, returns it.
        Otherwise returns nullptr.
        """
        ...
    def toRegularExpression(self) -> PySide6.QtCore.QRegularExpression:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#toRegularExpression

        **QRegularExpression QJSManagedValue::toRegularExpression() const**

        If this **QJSManagedValue**  holds a JavaScript regular expression
        object, returns an equivalent **QRegularExpression** . Otherwise returns
        an invalid one.
        """
        ...
    def toString(self) -> str:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#toString

        **QString QJSManagedValue::toString() const**

        Converts the manged value to a string. If the managed value holds a
        string, that one is returned. Otherwise a string coercion by JavaScript
        rules is performed.

        **Note:** Conversion of a managed value to a string can throw an
        exception. In particular, symbols cannot be coerced into strings, or a
        custom toString() method may throw. In this case the result is an empty
        string and the engine carries an error after the conversion.
        """
        ...
    def toUrl(self) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#toUrl

        **QUrl QJSManagedValue::toUrl() const**

        If this **QJSManagedValue**  holds a JavaScript Url object, returns an
        equivalent **QUrl** . Otherwise returns an invalid one.
        """
        ...
    def toVariant(self) -> Any:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#toVariant

        **QVariant QJSManagedValue::toVariant() const**

        Copies this **QJSManagedValue**  into a new **QVariant** . This also
        creates a useful **QVariant**  if **QJSManagedValue::isVariant** ()
        returns false. **QVariant**  can hold all types supported by
        **QJSManagedValue** .
        """
        ...
    def type(self) -> PySide6.QtQml.QJSManagedValue.Type:
        """
        https://doc.qt.io/qt-6/qjsmanagedvalue.html#type

        **QJSManagedValue::Type QJSManagedValue::type() const**

        Returns the JavaScript type of this **QJSManagedValue** .
        """
        ...