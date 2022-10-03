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

import PySide6.QtCore
import PySide6.QtGui

class QAccessibleInterface:
    """
    https://doc.qt.io/qt-6/qaccessibleinterface.html

    **Detailed Description**

    This class is part of **Accessibility for QWidget Applications** .

    Accessibility tools (also called AT Clients), such as screen readers or
    braille displays, require high-level information about accessible objects in
    an application. Accessible objects provide specialized input and output
    methods, making it possible for users to use accessibility tools with
    enabled applications (AT Servers).

    Every element that the user needs to interact with or react to is an
    accessible object, and should provide this information. These are mainly
    visual objects, such as widgets and widget elements, but can also be
    content, such as sounds.

    The AT client uses three basic concepts to acquire information about any
    accessible object in an application:

    * **Properties** The client can read information about accessible objects.
    In some cases the client can also modify these properties; such as text in a
    line edit.
      * **Actions** The client can invoke actions like pressing a
    button or .
      * **Relationships and Navigation** The client can traverse
    from one accessible object to another, using the relationships between
    objects.

    The QAccessibleInterface defines the API for these three concepts.

    **Relationships and Navigation**

    The functions **childCount** () and **indexOfChild** () return the number of
    children of an accessible object and the index a child object has in its
    parent. The **childAt** () function returns a child QAccessibleInterface
    that is found at a position. The child does not have to be a direct child.
    This allows bypassing intermediate layers when the parent already knows the
    top-most child. **childAt** () is used for hit testing (finding the object
    under the mouse).

    The **relations** () function provides information about the relations an
    object has to other objects, and **parent** () and **child** () allows
    traversing from one object to another object.

    **Properties**

    The central property of an accessible objects is what **role** () it has.
    Different objects can have the same role, e.g. both the "Add line" element
    in a scroll bar and the `OK` button in a dialog have the same role,
    "button". The role implies what kind of interaction the user can perform
    with the user interface element.

    An object's **state** () property is a combination of different state flags
    and can describe both how the object's state differs from a "normal" state,
    e.g. it might be unavailable, and also how it behaves, e.g. it might be
    selectable.

    The **text** () property provides textual information about the object. An
    object usually has a name, but can provide extended information such as a
    description, help text, or information about any keyboard accelerators it
    provides. Some objects allow changing the **text** () property through the
    **setText** () function, but this information is in most cases read-only.

    The **rect** () property provides information about the geometry of an
    accessible object. This information is usually only available for visual
    objects.

    **Interfaces**

    To enable the user to interact with an accessible object the object must
    implement **QAccessibleActionInterface**  in addition to
    QAccessibleInterface. Objects that support selections can define actions to
    change the selection.

    There are several other interfaces that should be implemented as required.
    **QAccessibleTextInterface**  should be used for bigger texts edits such as
    document views. This interface should not be implemented for labels/single
    line edits.

    For sliders, scrollbars and other numerical value selectors
    **QAccessibleValueInterface**  should be implemented.

    Lists, tables and trees should implement **QAccessibleTableInterface** .

    **See also** **QAccessible** , **QAccessibleActionInterface** ,
    **QAccessibleTextInterface** , **QAccessibleValueInterface** , and
    **QAccessibleTableInterface** .
    """

    def __init__(self) -> None: ...
    def actionInterface(self) -> PySide6.QtGui.QAccessibleActionInterface:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#actionInterface

        **QAccessibleActionInterface *QAccessibleInterface::actionInterface()**
        """
        ...
    def backgroundColor(self) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#backgroundColor

        **[virtual] QColor QAccessibleInterface::backgroundColor() const**

        Returns the accessible's background color if applicable or an invalid
        **QColor** .

        **See also** **foregroundColor** ().
        """
        ...
    def child(self, index: int) -> PySide6.QtGui.QAccessibleInterface:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#child

        **[pure virtual] QAccessibleInterface *QAccessibleInterface::child(int
        index ) const**

        Returns the accessible child with index **index**. 0-based index. The
        number of children of an object can be checked with **childCount** .

        Returns `nullptr` when asking for an invalid child (e.g. when the child
        became invalid in the meantime).

        **See also** **childCount** () and **parent** ().
        """
        ...
    def childAt(self, x: int, y: int) -> PySide6.QtGui.QAccessibleInterface:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#childAt

        **[pure virtual] QAccessibleInterface *QAccessibleInterface::childAt(int
        x , int y ) const**

        Returns the **QAccessibleInterface**  of a child that contains the
        screen coordinates ( **x** , **y** ). If there are no children at this
        position this function returns `nullptr`. The returned accessible must
        be a child, but not necessarily a direct child.

        This function is only reliable for visible objects (invisible object
        might not be laid out correctly).

        All visual objects provide this information.

        A default implementation is provided for objects inheriting
        **QAccessibleObject** . This will iterate over all children. If the
        widget manages its children (e.g. a table) it will be more efficient to
        write a specialized implementation.

        **See also** **rect** ().
        """
        ...
    def childCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#childCount

        **[pure virtual] int QAccessibleInterface::childCount() const**

        Returns the number of children that belong to this object. A child can
        provide accessibility information on its own (e.g. a child widget), or
        be a sub-element of this accessible object.

        All objects provide this information.

        **See also** **indexOfChild** ().
        """
        ...
    def editableTextInterface(self) -> PySide6.QtGui.QAccessibleEditableTextInterface: ...
    def focusChild(self) -> PySide6.QtGui.QAccessibleInterface:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#focusChild

        **[virtual] QAccessibleInterface *QAccessibleInterface::focusChild()
        const**

        Returns the object that has the keyboard focus.

        The object returned can be any descendant, including itself.
        """
        ...
    def foregroundColor(self) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#foregroundColor

        **[virtual] QColor QAccessibleInterface::foregroundColor() const**

        Returns the accessible's foreground color if applicable or an invalid
        **QColor** .

        **See also** **backgroundColor** ().
        """
        ...
    def indexOfChild(self, arg__1: PySide6.QtGui.QAccessibleInterface) -> int:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#indexOfChild

        **[pure virtual] int QAccessibleInterface::indexOfChild(const
        QAccessibleInterface * child ) const**

        Returns the 0-based index of the object **child** in this object's
        children list, or -1 if **child** is not a child of this object.

        All objects provide this information about their children.

        **See also** **childCount** ().
        """
        ...
    def interface_cast(self, arg__1: PySide6.QtGui.QAccessible.InterfaceType) -> int:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#interface_cast

        **[virtual] void
        *QAccessibleInterface::interface_cast(QAccessible::InterfaceType type
        )**

        Returns a specialized accessibility interface **type** from the generic
        **QAccessibleInterface** .

        This function must be reimplemented when providing more information
        about a widget or object through the specialized interfaces. For example
        a line edit should implement the **QAccessibleTextInterface** .

        **See also** **QAccessible::InterfaceType** ,
        **QAccessibleTextInterface** , **QAccessibleValueInterface** ,
        **QAccessibleActionInterface** , **QAccessibleTableInterface** , and
        **QAccessibleTableCellInterface** .
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#isValid

        **[pure virtual] bool QAccessibleInterface::isValid() const**

        Returns `true` if all the data necessary to use this interface
        implementation is valid (e.g. all pointers are non-null); otherwise
        returns `false`.

        **See also** **object** ().
        """
        ...
    def object(self) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#object

        **[pure virtual] QObject *QAccessibleInterface::object() const**

        Returns a pointer to the **QObject**  this interface implementation
        provides information for.

        **See also** **isValid** ().
        """
        ...
    def parent(self) -> PySide6.QtGui.QAccessibleInterface:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#parent

        **[pure virtual] QAccessibleInterface *QAccessibleInterface::parent()
        const**

        Returns the **QAccessibleInterface**  of the parent in the accessible
        object hierarchy.

        Returns `nullptr` if no parent exists (e.g. for the top level
        application object).

        **See also** **child** ().
        """
        ...
    def rect(self) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#rect

        **[pure virtual] QRect QAccessibleInterface::rect() const**

        Returns the geometry of the object. The geometry is in screen
        coordinates.

        This function is only reliable for visible objects (invisible objects
        might not be laid out correctly).

        All visual objects provide this information.

        **See also** **childAt** ().
        """
        ...
    def relations(
        self, match: PySide6.QtGui.QAccessible.Relation = ...
    ) -> list[
        tuple[PySide6.QtGui.QAccessibleInterface, PySide6.QtGui.QAccessible.Relation]
    ]:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#relations

        **[virtual] QList<QPair<QAccessibleInterface *, QAccessible::Relation> >
        QAccessibleInterface::relations(QAccessible::Relation match =
        QAccessible::AllRelations) const**

        Returns the meaningful relations to other widgets. Usually this will not
        return parent/child relations, unless they are handled in a specific way
        such as in tree views. It will typically return the labelled-by and
        label relations.

        It is possible to filter the relations by using the optional parameter
        **match**. It should never return itself.

        **See also** **parent** () and **child** ().
        """
        ...
    def role(self) -> PySide6.QtGui.QAccessible.Role:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#role

        **[pure virtual] QAccessible::Role QAccessibleInterface::role() const**

        Returns the role of the object. The role of an object is usually static.

        All accessible objects have a role.

        **See also** **text** () and **state** ().
        """
        ...
    def setText(self, t: PySide6.QtGui.QAccessible.Text, text: str) -> None:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#setText

        **[pure virtual] void QAccessibleInterface::setText(QAccessible::Text t
        , const QString & text )**

        Sets the text property **t** of the object to **text**.

        Note that the text properties of most objects are read-only so calling
        this function might have no effect.

        **See also** **text** ().
        """
        ...
    def state(self) -> PySide6.QtGui.QAccessible.State:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#state

        **[pure virtual] QAccessible::State QAccessibleInterface::state()
        const**

        Returns the current state of the object. The returned value is a
        combination of the flags in the QAccessible::StateFlag enumeration.

        All accessible objects have a state.

        **See also** **text** () and **role** ().
        """
        ...
    def tableCellInterface(self) -> PySide6.QtGui.QAccessibleTableCellInterface:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#tableCellInterface

        **QAccessibleTableCellInterface
        *QAccessibleInterface::tableCellInterface()**
        """
        ...
    def text(self, t: PySide6.QtGui.QAccessible.Text) -> str:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#text

        **[pure virtual] QString QAccessibleInterface::text(QAccessible::Text t
        ) const**

        Returns the value of the text property **t** of the object.

        The **QAccessible::Name**  is a string used by clients to identify,
        find, or announce an accessible object for the user. All objects must
        have a name that is unique within their container. The name can be used
        differently by clients, so the name should both give a short description
        of the object and be unique.

        An accessible object's **QAccessible::Description**  provides textual
        information about an object's visual appearance. The description is
        primarily used to provide greater context for vision-impaired users, but
        is also used for context searching or other applications. Not all
        objects have a description. An "OK" button would not need a description,
        but a tool button that shows a picture of a smiley would.

        The **QAccessible::Value**  of an accessible object represents visual
        information contained by the object, e.g. the text in a line edit.
        Usually, the value can be modified by the user. Not all objects have a
        value, e.g. static text labels don't, and some objects have a state that
        already is the value, e.g. toggle buttons.

        The **QAccessible::Help**  text provides information about the function
        and usage of an accessible object. Not all objects provide this
        information.

        The **QAccessible::Accelerator**  is a keyboard shortcut that activates
        the object's default action. A keyboard shortcut is the underlined
        character in the text of a menu, menu item or widget, and is either the
        character itself, or a combination of this character and a modifier key
        like Alt, Ctrl or Shift. Command controls like tool buttons also have
        shortcut keys and usually display them in their tooltip.

        All objects provide a string for **QAccessible::Name** .

        **See also** **setText** (), **role** (), and **state** ().
        """
        ...
    def textInterface(self) -> PySide6.QtGui.QAccessibleTextInterface:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#textInterface

        **QAccessibleTextInterface *QAccessibleInterface::textInterface()**
        """
        ...
    def valueInterface(self) -> PySide6.QtGui.QAccessibleValueInterface:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#valueInterface

        **QAccessibleValueInterface *QAccessibleInterface::valueInterface()**
        """
        ...
    def virtual_hook(self, id: int, data: int) -> None: ...
    def window(self) -> PySide6.QtGui.QWindow:
        """
        https://doc.qt.io/qt-6/qaccessibleinterface.html#window

        **[virtual] QWindow *QAccessibleInterface::window() const**

        Returns the window associated with the underlying object. For instance,
        **QAccessibleWidget**  reimplements this and returns the windowHandle()
        of the **QWidget** .

        It is used on some platforms to be able to notify the AT client about
        state changes. The backend will traverse up all ancestors until it finds
        a window. (This means that at least one interface among the ancestors
        should return a valid **QWindow**  pointer).

        The default implementation returns `nullptr`.
        """
        ...