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

from collections.abc import Callable, Sequence
from typing import overload

import PySide6.QtCore
import PySide6.QtGui

class QShortcut(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qshortcut.html

    **Detailed Description**

    The QShortcut class provides a way of connecting keyboard shortcuts to Qt's
    **signals and slots**  mechanism, so that objects can be informed when a
    shortcut is executed. The shortcut can be set up to contain all the key
    presses necessary to describe a keyboard shortcut, including the states of
    modifier keys such as **Shift** , **Ctrl** , and **Alt**.

    In widget applications, certain widgets can use '&' in front of a character.
    This will automatically create a mnemonic (a shortcut) for that character,
    e.g. "E&xit" will create the shortcut **Alt+X** (use '&&' to display an
    actual ampersand). The widget might consume and perform an action on a given
    shortcut. On X11 the ampersand will not be shown and the character will be
    underlined. On Windows, shortcuts are normally not displayed until the user
    presses the **Alt** key, but this is a setting the user can change. On Mac,
    shortcuts are disabled by default. Call **qt_set_sequence_auto_mnemonic** ()
    to enable them. However, because mnemonic shortcuts do not fit in with
    Aqua's guidelines, Qt will not show the shortcut character underlined.

    For applications that use menus, it may be more convenient to use the
    convenience functions provided in the **QMenu**  class to assign keyboard
    shortcuts to menu items as they are created. Alternatively, shortcuts may be
    associated with other types of actions in the **QAction**  class.

    The simplest way to create a shortcut for a particular widget is to
    construct the shortcut with a key sequence. For example:

    shortcut = new **QShortcut** (**QKeySequence** (tr("Ctrl+O", "File|Open")),
    parent);

    When the user types the **key sequence**  for a given shortcut, the
    shortcut's **activated** () signal is emitted. (In the case of ambiguity,
    the **activatedAmbiguously** () signal is emitted.) A shortcut is "listened
    for" by Qt's event loop when the shortcut's parent widget is receiving
    events.

    A shortcut's key sequence can be set with **setKey** () and retrieved with
    **key** (). A shortcut can be enabled or disabled with **setEnabled** (),
    and can have "What's This?" help text set with **setWhatsThis** ().

    **See also** **QShortcutEvent** , **QKeySequence** , and **QAction** .
    """

    @overload
    def __init__(
        self,
        arg__1: PySide6.QtGui.QKeySequence.StandardKey,
        arg__2: PySide6.QtCore.QObject,
        arg__3: Callable,
        arg__4: PySide6.QtCore.Qt.ShortcutContext = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qshortcut.html#QShortcut

        **QShortcut::QShortcut(QObject * parent )**

        Constructs a QShortcut object for the **parent** , which should be a
        **QWindow**  or a **QWidget** .

        Since no shortcut key sequence is specified, the shortcut will not emit
        any signals.

        **See also** **setKey** ().
        """
        ...
    @overload
    def __init__(
        self,
        arg__1: (
            PySide6.QtGui.QKeySequence
            | PySide6.QtCore.QKeyCombination
            | PySide6.QtGui.QKeySequence.StandardKey
            | str
            | int
        ),
        arg__2: PySide6.QtCore.QObject,
        arg__3: Callable,
        arg__4: PySide6.QtCore.Qt.ShortcutContext = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qshortcut.html#QShortcut-1

        **QShortcut::QShortcut(const QKeySequence & key , QObject * parent ,
        const char * member = nullptr, const char * ambiguousMember = nullptr,
        Qt::ShortcutContext context = Qt::WindowShortcut)**

        Constructs a QShortcut object for the **parent** , which should be a
        **QWindow**  or a **QWidget** .

        The shortcut operates on its parent, listening for **QShortcutEvent** s
        that match the **key** sequence. Depending on the ambiguity of the
        event, the shortcut will call the **member** function, or the
        **ambiguousMember** function, if the key press was in the shortcut's
        **context**.
        """
        ...
    @overload
    def __init__(
        self,
        key: PySide6.QtGui.QKeySequence.StandardKey,
        parent: PySide6.QtCore.QObject,
        member: bytes | None = ...,
        ambiguousMember: bytes | None = ...,
        context: PySide6.QtCore.Qt.ShortcutContext = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qshortcut.html#QShortcut-2

        **[since 6.0] QShortcut::QShortcut(QKeySequence::StandardKey standardKey
        , QObject * parent , const char * member = nullptr, const char *
        ambiguousMember = nullptr, Qt::ShortcutContext context =
        Qt::WindowShortcut)**

        Constructs a QShortcut object for the **parent** , which should be a
        **QWindow**  or a **QWidget** .

        The shortcut operates on its parent, listening for **QShortcutEvent** s
        that match the **standardKey**. Depending on the ambiguity of the event,
        the shortcut will call the **member** function, or the
        **ambiguousMember** function, if the key press was in the shortcut's
        **context**.

        This function was introduced in Qt 6.0.
        """
        ...
    @overload
    def __init__(
        self,
        key: (
            PySide6.QtGui.QKeySequence
            | PySide6.QtCore.QKeyCombination
            | PySide6.QtGui.QKeySequence.StandardKey
            | str
            | int
        ),
        parent: PySide6.QtCore.QObject,
        member: bytes | None = ...,
        ambiguousMember: bytes | None = ...,
        context: PySide6.QtCore.Qt.ShortcutContext = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qshortcut.html#QShortcut-3

        **[since 5.15] template <typename Functor> QShortcut::QShortcut(const
        QKeySequence & key , QObject * parent , Functor functor ,
        Qt::ShortcutContext shortcutContext = Qt::WindowShortcut)**

        This is an overloaded function.

        This is a QShortcut convenience constructor which connects the
        shortcut's **activated** () signal to the **functor**.

        This function was introduced in Qt 5.15.
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject) -> None:
        """
        https://doc.qt.io/qt-6/qshortcut.html#QShortcut-4

        **[since 5.15] template <typename Functor> QShortcut::QShortcut(const
        QKeySequence & key , QObject * parent , const QObject * context ,
        Functor functor , Qt::ShortcutContext shortcutContext =
        Qt::WindowShortcut)**

        This is an overloaded function.

        This is a QShortcut convenience constructor which connects the
        shortcut's **activated** () signal to the **functor**.

        The **functor** can be a pointer to a member function of the **context**
        object.

        If the **context** object is destroyed, the **functor** will not be
        called.

        This function was introduced in Qt 5.15.
        """
        ...
    def autoRepeat(self) -> bool:
        """
        https://doc.qt.io/qt-6/qshortcut.html#autoRepeat-prop

        **autoRepeat : bool**

        This property holds whether the shortcut can auto repeat

        If true, the shortcut will auto repeat when the keyboard shortcut
        combination is held down, provided that keyboard auto repeat is enabled
        on the system. The default value is true.

        **Access functions:**

        bool **autoRepeat** () const
        void **setAutoRepeat** (bool **on** )
        """
        ...
    def context(self) -> PySide6.QtCore.Qt.ShortcutContext:
        """
        https://doc.qt.io/qt-6/qshortcut.html#context-prop

        **context : Qt::ShortcutContext**

        This property holds the context in which the shortcut is valid

        A shortcut's context decides in which circumstances a shortcut is
        allowed to be triggered. The normal context is **Qt::WindowShortcut** ,
        which allows the shortcut to trigger if the parent (the widget
        containing the shortcut) is a subwidget of the active top-level window.

        By default, this property is set to **Qt::WindowShortcut** .

        **Access functions:**

        Qt::ShortcutContext **context** () const
        void **setContext**
        (Qt::ShortcutContext **context** )
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    def id(self) -> int:
        """
        https://doc.qt.io/qt-6/qshortcut.html#id

        **int QShortcut::id() const**

        Returns the primary key binding's ID.

        **See also** **QShortcutEvent::shortcutId** ().
        """
        ...
    def isEnabled(self) -> bool: ...
    def key(self) -> PySide6.QtGui.QKeySequence:
        """
        https://doc.qt.io/qt-6/qshortcut.html#key-prop

        **key : QKeySequence**

        This property holds the shortcut's primary key sequence

        This is a key sequence with an optional combination of Shift, Ctrl, and
        Alt. The key sequence may be supplied in a number of ways:

        setKey(0);                  // no signal emitted
        setKey(**QKeySequence** ());     // no signal emitted
            setKey(0x3b1);
        // Greek letter alpha
            setKey(Qt::Key_D);              // 'd', e.g.
        to delete
            setKey('q');                // 'q', e.g. to quit
        setKey(Qt::CTRL | Qt::Key_P);       // Ctrl+P, e.g. to print document
        setKey("Ctrl+P");           // Ctrl+P, e.g. to print document

        By default, this property contains an empty key sequence.

        **Access functions:**

        QKeySequence **key** () const
        void **setKey** (const QKeySequence &
        **key** )

        **Member Function Documentation**
        """
        ...
    def keys(self) -> list[PySide6.QtGui.QKeySequence]:
        """
        https://doc.qt.io/qt-6/qshortcut.html#keys

        **[since 6.0] QList<QKeySequence> QShortcut::keys() const**

        Returns the list of key sequences which trigger this shortcut.

        This function was introduced in Qt 6.0.

        **See also** **key**  and **setKeys** ().
        """
        ...
    def setAutoRepeat(self, on: bool) -> None:
        """
        https://doc.qt.io/qt-6/qshortcut.html#autoRepeat-prop

        **autoRepeat : bool**

        This property holds whether the shortcut can auto repeat

        If true, the shortcut will auto repeat when the keyboard shortcut
        combination is held down, provided that keyboard auto repeat is enabled
        on the system. The default value is true.

        **Access functions:**

        bool **autoRepeat** () const
        void **setAutoRepeat** (bool **on** )
        """
        ...
    def setContext(self, context: PySide6.QtCore.Qt.ShortcutContext) -> None:
        """
        https://doc.qt.io/qt-6/qshortcut.html#context-prop

        **context : Qt::ShortcutContext**

        This property holds the context in which the shortcut is valid

        A shortcut's context decides in which circumstances a shortcut is
        allowed to be triggered. The normal context is **Qt::WindowShortcut** ,
        which allows the shortcut to trigger if the parent (the widget
        containing the shortcut) is a subwidget of the active top-level window.

        By default, this property is set to **Qt::WindowShortcut** .

        **Access functions:**

        Qt::ShortcutContext **context** () const
        void **setContext**
        (Qt::ShortcutContext **context** )
        """
        ...
    def setEnabled(self, enable: bool) -> None:
        """
        https://doc.qt.io/qt-6/qshortcut.html#enabled-prop

        **enabled : bool**

        This property holds whether the shortcut is enabled

        An enabled shortcut emits the **activated** () or
        **activatedAmbiguously** () signal when a **QShortcutEvent**  occurs
        that matches the shortcut's **key** () sequence.

        If the application is in `WhatsThis` mode the shortcut will not emit the
        signals, but will show the "What's This?" text instead.

        By default, this property is `true`.

        **Access functions:**

        bool **isEnabled** () const
        void **setEnabled** (bool **enable** )

        **See also** **whatsThis** .
        """
        ...
    def setKey(
        self,
        key: (
            PySide6.QtGui.QKeySequence
            | PySide6.QtCore.QKeyCombination
            | PySide6.QtGui.QKeySequence.StandardKey
            | str
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qshortcut.html#key-prop

        **key : QKeySequence**

        This property holds the shortcut's primary key sequence

        This is a key sequence with an optional combination of Shift, Ctrl, and
        Alt. The key sequence may be supplied in a number of ways:

        setKey(0);                  // no signal emitted
        setKey(**QKeySequence** ());     // no signal emitted
            setKey(0x3b1);
        // Greek letter alpha
            setKey(Qt::Key_D);              // 'd', e.g.
        to delete
            setKey('q');                // 'q', e.g. to quit
        setKey(Qt::CTRL | Qt::Key_P);       // Ctrl+P, e.g. to print document
        setKey("Ctrl+P");           // Ctrl+P, e.g. to print document

        By default, this property contains an empty key sequence.

        **Access functions:**

        QKeySequence **key** () const
        void **setKey** (const QKeySequence &
        **key** )

        **Member Function Documentation**
        """
        ...
    @overload
    def setKeys(self, key: PySide6.QtGui.QKeySequence.StandardKey) -> None:
        """
        https://doc.qt.io/qt-6/qshortcut.html#setKeys

        **[since 6.0] void QShortcut::setKeys(QKeySequence::StandardKey key )**

        Sets the triggers to those matching the standard key **key**.

        This function was introduced in Qt 6.0.

        **See also** **key**  and **keys** ().
        """
        ...
    @overload
    def setKeys(self, keys: Sequence[PySide6.QtGui.QKeySequence]) -> None:
        """
        https://doc.qt.io/qt-6/qshortcut.html#setKeys-1

        **[since 6.0] void QShortcut::setKeys(const QList<QKeySequence> & keys
        )**

        Sets **keys** as the list of key sequences that trigger the shortcut.

        This function was introduced in Qt 6.0.

        **See also** **key**  and **keys** ().
        """
        ...
    def setWhatsThis(self, text: str) -> None:
        """
        https://doc.qt.io/qt-6/qshortcut.html#setWhatsThis

        **void QShortcut::setWhatsThis(const QString & text )**

        Sets the shortcut's "What's This?" help **text**.

        The text will be shown when a widget application is in "What's This?"
        mode and the user types the shortcut **key** () sequence.

        To set "What's This?" help on a menu item (with or without a shortcut
        key), set the help on the item's action.

        By default, the help text is an empty string.

        This function has no effect in applications that don't use widgets.

        **See also** **whatsThis** (), **QWhatsThis::inWhatsThisMode** (), and
        **QAction::setWhatsThis** ().
        """
        ...
    def whatsThis(self) -> str:
        """
        https://doc.qt.io/qt-6/qshortcut.html#whatsThis

        **QString QShortcut::whatsThis() const**

        Returns the shortcut's "What's This?" help text.

        **See also** **setWhatsThis** ().
        """
        ...
    @property
    def activated(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qshortcut.html#activated

        **[signal] void QShortcut::activated()**

        This signal is emitted when the user types the shortcut's key sequence.

        **See also** **activatedAmbiguously** ().
        """
        ...
    @property
    def activatedAmbiguously(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qshortcut.html#activatedAmbiguously

        **[signal] void QShortcut::activatedAmbiguously()**

        When a key sequence is being typed at the keyboard, it is said to be
        ambiguous as long as it matches the start of more than one shortcut.

        When a shortcut's key sequence is completed, activatedAmbiguously() is
        emitted if the key sequence is still ambiguous (i.e., it is the start of
        one or more other shortcuts). The **activated** () signal is not emitted
        in this case.

        **See also** **activated** ().
        """
        ...