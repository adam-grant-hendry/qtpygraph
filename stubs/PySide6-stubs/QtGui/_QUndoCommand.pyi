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

from typing import overload

import PySide6.QtCore
import PySide6.QtGui

class QUndoCommand:
    """
    https://doc.qt.io/qt-6/qundocommand.html

    **Detailed Description**

    For an overview of Qt's Undo Framework, see the **overview document** .

    A QUndoCommand represents a single editing action on a document; for
    example, inserting or deleting a block of text in a text editor.
    QUndoCommand can apply a change to the document with **redo** () and undo
    the change with **undo** (). The implementations for these functions must be
    provided in a derived class.

    class AppendText : public **QUndoCommand**
        {
        public:
    AppendText(**QString**  *doc, const **QString**  &text)
                :
    m_document(doc), m_text(text) { setText("append text"); }
            void
    undo() override
                { m_document->chop(m_text.length()); }
    void redo() override
                { m_document->append(m_text); }
    private:
            **QString**  *m_document;
            **QString**  m_text;
    };

    A QUndoCommand has an associated **text** (). This is a short string
    describing what the command does. It is used to update the text properties
    of the stack's undo and redo actions; see **QUndoStack::createUndoAction**
    () and **QUndoStack::createRedoAction** ().

    QUndoCommand objects are owned by the stack they were pushed on.
    **QUndoStack**  deletes a command if it has been undone and a new command is
    pushed. For example:

    MyCommand *command1 = new MyCommand();
        stack->push(command1);
    MyCommand *command2 = new MyCommand();
        stack->push(command2);
    stack->undo();

        MyCommand *command3 = new MyCommand();
    stack->push(command3); // command2 gets deleted

    In effect, when a command is pushed, it becomes the top-most command on the
    stack.

    To support command compression, QUndoCommand has an **id** () and the
    virtual function **mergeWith** (). These functions are used by
    **QUndoStack::push** ().

    To support command macros, a QUndoCommand object can have any number of
    child commands. Undoing or redoing the parent command will cause the child
    commands to be undone or redone. A command can be assigned to a parent
    explicitly in the constructor. In this case, the command will be owned by
    the parent.

    The parent in this case is usually an empty command, in that it doesn't
    provide its own implementation of **undo** () and **redo** (). Instead, it
    uses the base implementations of these functions, which simply call **undo**
    () or **redo** () on all its children. The parent should, however, have a
    meaningful **text** ().

    **QUndoCommand**  *insertRed = new **QUndoCommand** (); // an empty command
    insertRed->setText("insert red text");

        new InsertText(document,
    idx, text, insertRed); // becomes child of insertRed
        new
    SetColor(document, idx, text.length(), Qt::red, insertRed);
    stack.push(insertRed);

    Another way to create macros is to use the convenience functions
    **QUndoStack::beginMacro** () and **QUndoStack::endMacro** ().

    **See also** **QUndoStack** .
    """

    @overload
    def __init__(self, parent: PySide6.QtGui.QUndoCommand | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qundocommand.html#QUndoCommand

        **QUndoCommand::QUndoCommand(QUndoCommand * parent = nullptr)**

        Constructs a QUndoCommand object with parent **parent**.

        If **parent** is not `nullptr`, this command is appended to parent's
        child list. The parent command then owns this command and will delete it
        in its destructor.

        **See also** **~QUndoCommand** ().
        """
        ...
    @overload
    def __init__(
        self, text: str, parent: PySide6.QtGui.QUndoCommand | None = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qundocommand.html#QUndoCommand-1

        **QUndoCommand::QUndoCommand(const QString & text , QUndoCommand *
        parent = nullptr)**

        Constructs a QUndoCommand object with the given **parent** and **text**.

        If **parent** is not `nullptr`, this command is appended to parent's
        child list. The parent command then owns this command and will delete it
        in its destructor.

        **See also** **~QUndoCommand** ().
        """
        ...
    def actionText(self) -> str:
        """
        https://doc.qt.io/qt-6/qundocommand.html#actionText

        **QString QUndoCommand::actionText() const**

        Returns a short text string describing what this command does; for
        example, "insert text".

        The text is used when the text properties of the stack's undo and redo
        actions are updated.

        **See also** **text** (), **setText** (),
        **QUndoStack::createUndoAction** (), and
        **QUndoStack::createRedoAction** ().
        """
        ...
    def child(self, index: int) -> PySide6.QtGui.QUndoCommand:
        """
        https://doc.qt.io/qt-6/qundocommand.html#child

        **const QUndoCommand *QUndoCommand::child(int index ) const**

        Returns the child command at **index**.

        **See also** **childCount** () and **QUndoStack::command** ().
        """
        ...
    def childCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qundocommand.html#childCount

        **int QUndoCommand::childCount() const**

        Returns the number of child commands in this command.

        **See also** **child** ().
        """
        ...
    def id(self) -> int:
        """
        https://doc.qt.io/qt-6/qundocommand.html#id

        **[virtual] int QUndoCommand::id() const**

        Returns the ID of this command.

        A command ID is used in command compression. It must be an integer
        unique to this command's class, or -1 if the command doesn't support
        compression.

        If the command supports compression this function must be overridden in
        the derived class to return the correct ID. The base implementation
        returns -1.

        **QUndoStack::push** () will only try to merge two commands if they have
        the same ID, and the ID is not -1.

        **See also** **mergeWith** () and **QUndoStack::push** ().
        """
        ...
    def isObsolete(self) -> bool:
        """
        https://doc.qt.io/qt-6/qundocommand.html#isObsolete

        **[since 5.9] bool QUndoCommand::isObsolete() const**

        Returns whether the command is obsolete.

        The boolean is used for the automatic removal of commands that are not
        necessary in the stack anymore. The isObsolete function is checked in
        the functions **QUndoStack::push** (), **QUndoStack::undo** (),
        **QUndoStack::redo** (), and **QUndoStack::setIndex** ().

        This function was introduced in Qt 5.9.

        **See also** **setObsolete** (), **mergeWith** (), **QUndoStack::push**
        (), **QUndoStack::undo** (), and **QUndoStack::redo** ().
        """
        ...
    def mergeWith(self, other: PySide6.QtGui.QUndoCommand) -> bool:
        """
        https://doc.qt.io/qt-6/qundocommand.html#mergeWith

        **[virtual] bool QUndoCommand::mergeWith(const QUndoCommand * command
        )**

        Attempts to merge this command with **command**. Returns `true` on
        success; otherwise returns `false`.

        If this function returns `true`, calling this command's **redo** () must
        have the same effect as redoing both this command and **command**.
        Similarly, calling this command's **undo** () must have the same effect
        as undoing **command** and this command.

        **QUndoStack**  will only try to merge two commands if they have the
        same id, and the id is not -1.

        The default implementation returns `false`.

        bool AppendText::mergeWith(const **QUndoCommand**  *other)
            {
        if (other->id() != id()) // make sure other is also an AppendText
        command
                    return false;
                m_text += static_cast<const
        AppendText\\*>(other)->m_text;
                return true;
            }

        **See also** **id** () and **QUndoStack::push** ().
        """
        ...
    def redo(self) -> None:
        """
        https://doc.qt.io/qt-6/qundocommand.html#redo

        **[virtual] void QUndoCommand::redo()**

        Applies a change to the document. This function must be implemented in
        the derived class. Calling **QUndoStack::push** (), **QUndoStack::undo**
        () or **QUndoStack::redo** () from this function leads to undefined
        beahavior.

        The default implementation calls redo() on all child commands.

        **See also** **undo** ().
        """
        ...
    def setObsolete(self, obsolete: bool) -> None:
        """
        https://doc.qt.io/qt-6/qundocommand.html#setObsolete

        **[since 5.9] void QUndoCommand::setObsolete(bool obsolete )**

        Sets whether the command is obsolete to **obsolete**.

        This function was introduced in Qt 5.9.

        **See also** **isObsolete** (), **mergeWith** (), **QUndoStack::push**
        (), **QUndoStack::undo** (), and **QUndoStack::redo** ().
        """
        ...
    def setText(self, text: str) -> None:
        """
        https://doc.qt.io/qt-6/qundocommand.html#setText

        **void QUndoCommand::setText(const QString & text )**

        Sets the command's text to be the **text** specified.

        The specified text should be a short user-readable string describing
        what this command does.

        If you need to have two different strings for **text** () and
        **actionText** (), separate them with "\\n" and pass into this function.
        Even if you do not use this feature for English strings during
        development, you can still let translators use two different strings in
        order to match specific languages' needs. The described feature and the
        function **actionText** () are available since Qt 4.8.

        **See also** **text** (), **actionText** (),
        **QUndoStack::createUndoAction** (), and
        **QUndoStack::createRedoAction** ().
        """
        ...
    def text(self) -> str:
        """
        https://doc.qt.io/qt-6/qundocommand.html#text

        **QString QUndoCommand::text() const**

        Returns a short text string describing what this command does; for
        example, "insert text".

        The text is used for names of items in **QUndoView** .

        **See also** **actionText** (), **setText** (),
        **QUndoStack::createUndoAction** (), and
        **QUndoStack::createRedoAction** ().
        """
        ...
    def undo(self) -> None:
        """
        https://doc.qt.io/qt-6/qundocommand.html#undo

        **[virtual] void QUndoCommand::undo()**

        Reverts a change to the document. After undo() is called, the state of
        the document should be the same as before **redo** () was called. This
        function must be implemented in the derived class. Calling
        **QUndoStack::push** (), **QUndoStack::undo** () or **QUndoStack::redo**
        () from this function leads to undefined beahavior.

        The default implementation calls undo() on all child commands in reverse
        order.

        **See also** **redo** ().
        """
        ...
