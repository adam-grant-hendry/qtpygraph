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

from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QDialogButtonBox(PySide6.QtWidgets.QWidget):
    """
    https://doc.qt.io/qt-6/qdialogbuttonbox.html

    **Detailed Description**

    Dialogs and message boxes typically present buttons in a layout that
    conforms to the interface guidelines for that platform. Invariably,
    different platforms have different layouts for their dialogs.
    QDialogButtonBox allows a developer to add buttons to it and will
    automatically use the appropriate layout for the user's desktop environment.

    Most buttons for a dialog follow certain roles. Such roles include:

    * Accepting or rejecting the dialog.
      * Asking for help.
      * Performing
    actions on the dialog itself (such as resetting fields or applying changes).

    There can also be alternate ways of dismissing the dialog which may cause
    destructive results.

    Most dialogs have buttons that can almost be considered standard (e.g.
    **OK** and **Cancel** buttons). It is sometimes convenient to create these
    buttons in a standard way.

    There are a couple ways of using QDialogButtonBox. One ways is to create the
    buttons (or button texts) yourself and add them to the button box,
    specifying their role.

    findButton = new **QPushButton** (tr("&Find"));
    findButton->setDefault(true);

            moreButton = new **QPushButton**
    (tr("&More"));
            moreButton->setCheckable(true);
    moreButton->setAutoDefault(false);

    Alternatively, QDialogButtonBox provides several standard buttons (e.g. OK,
    Cancel, Save) that you can use. They exist as flags so you can OR them
    together in the constructor.

    buttonBox = new **QDialogButtonBox** (**QDialogButtonBox** ::Ok
    | **QDialogButtonBox** ::Cancel);

            connect(buttonBox,
    &**QDialogButtonBox** ::accepted, this, &**QDialog** ::accept);
    connect(buttonBox, &**QDialogButtonBox** ::rejected, this, &**QDialog**
    ::reject);

    You can mix and match normal buttons and standard buttons.

    Currently the buttons are laid out in the following way if the button box is
    horizontal:

    ![GnomeLayout Horizontal](images/buttonbox-gnomelayout-horizontal.png)Button
    box laid out in horizontal **GnomeLayout**
    ![KdeLayout
    Horizontal](images/buttonbox-kdelayout-horizontal.png)Button box laid out in
    horizontal **KdeLayout**
    ![MacLayout Horizontal](images/buttonbox-
    maclayout-horizontal.png)Button box laid out in horizontal **MacLayout**
    ![WinLayout Horizontal](images/buttonbox-winlayout-horizontal.png)Button box
    laid out in horizontal **WinLayout**

    The buttons are laid out the following way if the button box is vertical:

    **GnomeLayout** **KdeLayout** **MacLayout** **WinLayout**
    ![GnomeLayout
    Vertical](images/buttonbox-gnomelayout-vertical.png)![KdeLayout
    Vertical](images/buttonbox-kdelayout-vertical.png)![MacLayout
    Vertical](images/buttonbox-maclayout-vertical.png)![WinLayout
    Vertical](images/buttonbox-winlayout-vertical.png)

    Additionally, button boxes that contain only buttons with **ActionRole**  or
    **HelpRole**  can be considered modeless and have an alternate look on
    macOS:

    modeless horizontal **MacLayout** ![Screenshot of modeless horizontal
    MacLayout](images/buttonbox-mac-modeless-horizontal.png)
    modeless vertical
    **MacLayout** ![Screenshot of modeless vertical MacLayout](images/buttonbox-
    mac-modeless-vertical.png)

    When a button is clicked in the button box, the **clicked** () signal is
    emitted for the actual button is that is pressed. For convenience, if the
    button has an **AcceptRole** , **RejectRole** , or **HelpRole** , the
    **accepted** (), **rejected** (), or **helpRequested** () signals are
    emitted respectively.

    If you want a specific button to be default you need to call
    **QPushButton::setDefault** () on it yourself. However, if there is no
    default button set and to preserve which button is the default button across
    platforms when using the **QPushButton::autoDefault**  property, the first
    push button with the accept role is made the default button when the
    QDialogButtonBox is shown,

    **See also** **QMessageBox** , **QPushButton** , and **QDialog** .
    """

    WinLayout: QDialogButtonBox.ButtonLayout = ...
    MacLayout: QDialogButtonBox.ButtonLayout = ...
    KdeLayout: QDialogButtonBox.ButtonLayout = ...
    GnomeLayout: QDialogButtonBox.ButtonLayout = ...
    AndroidLayout: QDialogButtonBox.ButtonLayout = ...
    InvalidRole: QDialogButtonBox.ButtonRole = ...
    AcceptRole: QDialogButtonBox.ButtonRole = ...
    RejectRole: QDialogButtonBox.ButtonRole = ...
    DestructiveRole: QDialogButtonBox.ButtonRole = ...
    ActionRole: QDialogButtonBox.ButtonRole = ...
    HelpRole: QDialogButtonBox.ButtonRole = ...
    YesRole: QDialogButtonBox.ButtonRole = ...
    NoRole: QDialogButtonBox.ButtonRole = ...
    ResetRole: QDialogButtonBox.ButtonRole = ...
    ApplyRole: QDialogButtonBox.ButtonRole = ...
    NRoles: QDialogButtonBox.ButtonRole = ...
    NoButton: QDialogButtonBox.StandardButton = ...
    FirstButton: QDialogButtonBox.StandardButton = ...
    Ok: QDialogButtonBox.StandardButton = ...
    Save: QDialogButtonBox.StandardButton = ...
    SaveAll: QDialogButtonBox.StandardButton = ...
    Open: QDialogButtonBox.StandardButton = ...
    Yes: QDialogButtonBox.StandardButton = ...
    YesToAll: QDialogButtonBox.StandardButton = ...
    No: QDialogButtonBox.StandardButton = ...
    NoToAll: QDialogButtonBox.StandardButton = ...
    Abort: QDialogButtonBox.StandardButton = ...
    Retry: QDialogButtonBox.StandardButton = ...
    Ignore: QDialogButtonBox.StandardButton = ...
    Close: QDialogButtonBox.StandardButton = ...
    Cancel: QDialogButtonBox.StandardButton = ...
    Discard: QDialogButtonBox.StandardButton = ...
    Help: QDialogButtonBox.StandardButton = ...
    Apply: QDialogButtonBox.StandardButton = ...
    Reset: QDialogButtonBox.StandardButton = ...
    LastButton: QDialogButtonBox.StandardButton = ...
    RestoreDefaults: QDialogButtonBox.StandardButton = ...

    class ButtonLayout(IntFlag):
        WinLayout: QDialogButtonBox.ButtonLayout = ...
        MacLayout: QDialogButtonBox.ButtonLayout = ...
        KdeLayout: QDialogButtonBox.ButtonLayout = ...
        GnomeLayout: QDialogButtonBox.ButtonLayout = ...
        AndroidLayout: QDialogButtonBox.ButtonLayout = ...

    class ButtonRole(IntFlag):
        InvalidRole: QDialogButtonBox.ButtonRole = ...
        AcceptRole: QDialogButtonBox.ButtonRole = ...
        RejectRole: QDialogButtonBox.ButtonRole = ...
        DestructiveRole: QDialogButtonBox.ButtonRole = ...
        ActionRole: QDialogButtonBox.ButtonRole = ...
        HelpRole: QDialogButtonBox.ButtonRole = ...
        YesRole: QDialogButtonBox.ButtonRole = ...
        NoRole: QDialogButtonBox.ButtonRole = ...
        ResetRole: QDialogButtonBox.ButtonRole = ...
        ApplyRole: QDialogButtonBox.ButtonRole = ...
        NRoles: QDialogButtonBox.ButtonRole = ...

    class StandardButton(IntFlag):
        NoButton: QDialogButtonBox.StandardButton = ...
        FirstButton: QDialogButtonBox.StandardButton = ...
        Ok: QDialogButtonBox.StandardButton = ...
        Save: QDialogButtonBox.StandardButton = ...
        SaveAll: QDialogButtonBox.StandardButton = ...
        Open: QDialogButtonBox.StandardButton = ...
        Yes: QDialogButtonBox.StandardButton = ...
        YesToAll: QDialogButtonBox.StandardButton = ...
        No: QDialogButtonBox.StandardButton = ...
        NoToAll: QDialogButtonBox.StandardButton = ...
        Abort: QDialogButtonBox.StandardButton = ...
        Retry: QDialogButtonBox.StandardButton = ...
        Ignore: QDialogButtonBox.StandardButton = ...
        Close: QDialogButtonBox.StandardButton = ...
        Cancel: QDialogButtonBox.StandardButton = ...
        Discard: QDialogButtonBox.StandardButton = ...
        Help: QDialogButtonBox.StandardButton = ...
        Apply: QDialogButtonBox.StandardButton = ...
        Reset: QDialogButtonBox.StandardButton = ...
        LastButton: QDialogButtonBox.StandardButton = ...
        RestoreDefaults: QDialogButtonBox.StandardButton = ...

    class StandardButtons: ...

    @overload
    def __init__(
        self,
        buttons: PySide6.QtWidgets.QDialogButtonBox.StandardButtons,
        orientation: PySide6.QtCore.Qt.Orientation,
        parent: PySide6.QtWidgets.QWidget | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#QDialogButtonBox

        **QDialogButtonBox::QDialogButtonBox(QWidget * parent = nullptr)**

        Constructs an empty, horizontal button box with the given **parent**.

        **See also** **orientation**  and **addButton** ().
        """
        ...
    @overload
    def __init__(
        self,
        buttons: PySide6.QtWidgets.QDialogButtonBox.StandardButtons,
        parent: PySide6.QtWidgets.QWidget | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#QDialogButtonBox-1

        **QDialogButtonBox::QDialogButtonBox(Qt::Orientation orientation ,
        QWidget * parent = nullptr)**

        Constructs an empty button box with the given **orientation** and
        **parent**.

        **See also** **orientation**  and **addButton** ().
        """
        ...
    @overload
    def __init__(
        self,
        orientation: PySide6.QtCore.Qt.Orientation,
        parent: PySide6.QtWidgets.QWidget | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#QDialogButtonBox-2

        **[since 5.2]
        QDialogButtonBox::QDialogButtonBox(QDialogButtonBox::StandardButtons
        buttons , QWidget * parent = nullptr)**

        Constructs a horizontal button box with the given **parent** ,
        containing the standard buttons specified by **buttons**.

        This function was introduced in Qt 5.2.

        **See also** **orientation**  and **addButton** ().
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#QDialogButtonBox-3

        **QDialogButtonBox::QDialogButtonBox(QDialogButtonBox::StandardButtons
        buttons , Qt::Orientation orientation , QWidget * parent = nullptr)**

        Constructs a button box with the given **orientation** and **parent** ,
        containing the standard buttons specified by **buttons**.

        **See also** **orientation**  and **addButton** ().
        """
        ...
    @overload
    def addButton(
        self,
        button: PySide6.QtWidgets.QAbstractButton,
        role: PySide6.QtWidgets.QDialogButtonBox.ButtonRole,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#addButton

        **void QDialogButtonBox::addButton(QAbstractButton * button ,
        QDialogButtonBox::ButtonRole role )**

        Adds the given **button** to the button box with the specified **role**.
        If the role is invalid, the button is not added.

        If the button has already been added, it is removed and added again with
        the new role.

        **Note:** The button box takes ownership of the button.

        **See also** **removeButton** () and **clear** ().
        """
        ...
    @overload
    def addButton(
        self, button: PySide6.QtWidgets.QDialogButtonBox.StandardButton
    ) -> PySide6.QtWidgets.QPushButton:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#addButton-1

        **QPushButton *QDialogButtonBox::addButton(const QString & text ,
        QDialogButtonBox::ButtonRole role )**

        Creates a push button with the given **text** , adds it to the button
        box for the specified **role** , and returns the corresponding push
        button. If **role** is invalid, no button is created, and zero is
        returned.

        **See also** **removeButton** () and **clear** ().
        """
        ...
    @overload
    def addButton(
        self, text: str, role: PySide6.QtWidgets.QDialogButtonBox.ButtonRole
    ) -> PySide6.QtWidgets.QPushButton:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#addButton-2

        **QPushButton
        *QDialogButtonBox::addButton(QDialogButtonBox::StandardButton button )**

        Adds a standard **button** to the button box if it is valid to do so,
        and returns a push button. If **button** is invalid, it is not added to
        the button box, and zero is returned.

        **See also** **removeButton** () and **clear** ().
        """
        ...
    def button(
        self, which: PySide6.QtWidgets.QDialogButtonBox.StandardButton
    ) -> PySide6.QtWidgets.QPushButton:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#button

        **QPushButton *QDialogButtonBox::button(QDialogButtonBox::StandardButton
        which ) const**

        Returns the **QPushButton**  corresponding to the standard button
        **which** , or `nullptr` if the standard button doesn't exist in this
        button box.

        **See also** **standardButton** (), **standardButtons** (), and
        **buttons** ().
        """
        ...
    def buttonRole(
        self, button: PySide6.QtWidgets.QAbstractButton
    ) -> PySide6.QtWidgets.QDialogButtonBox.ButtonRole:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#buttonRole

        **QDialogButtonBox::ButtonRole
        QDialogButtonBox::buttonRole(QAbstractButton * button ) const**

        Returns the button role for the specified **button**. This function
        returns **InvalidRole**  if **button** is `nullptr` or has not been
        added to the button box.

        **See also** **buttons** () and **addButton** ().
        """
        ...
    def buttons(self) -> list[PySide6.QtWidgets.QAbstractButton]:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#buttons

        **QList<QAbstractButton *> QDialogButtonBox::buttons() const**

        Returns a list of all the buttons that have been added to the button
        box.

        **See also** **buttonRole** (), **addButton** (), and **removeButton**
        ().
        """
        ...
    def centerButtons(self) -> bool:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#centerButtons-prop

        **centerButtons : bool**

        This property holds whether the buttons in the button box are centered

        By default, this property is `false`. This behavior is appropriate for
        most types of dialogs. A notable exception is message boxes on most
        platforms (e.g. Windows), where the button box is centered horizontally.

        **Access functions:**

        bool **centerButtons** () const
        void **setCenterButtons** (bool
        **center** )

        **See also** **QMessageBox** .
        """
        ...
    def changeEvent(self, event: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#changeEvent

        **[override virtual protected] void QDialogButtonBox::changeEvent(QEvent
        * event )**

        Reimplements: **QWidget::changeEvent** (QEvent *event).
        """
        ...
    def clear(self) -> None:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#clear

        **void QDialogButtonBox::clear()**

        Clears the button box, deleting all buttons within it.

        **See also** **removeButton** () and **addButton** ().
        """
        ...
    def event(self, event: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#event

        **[override virtual protected] bool QDialogButtonBox::event(QEvent *
        event )**

        Reimplements: **QWidget::event** (QEvent *event).
        """
        ...
    def orientation(self) -> PySide6.QtCore.Qt.Orientation:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#orientation-prop

        **orientation : Qt::Orientation**

        This property holds the orientation of the button box

        By default, the orientation is horizontal (i.e. the buttons are laid out
        side by side). The possible orientations are **Qt::Horizontal**  and
        **Qt::Vertical** .

        **Access functions:**

        Qt::Orientation **orientation** () const
        void **setOrientation**
        (Qt::Orientation **orientation** )
        """
        ...
    def removeButton(self, button: PySide6.QtWidgets.QAbstractButton) -> None:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#removeButton

        **void QDialogButtonBox::removeButton(QAbstractButton * button )**

        Removes **button** from the button box without deleting it and sets its
        parent to zero.

        **See also** **clear** (), **buttons** (), and **addButton** ().
        """
        ...
    def setCenterButtons(self, center: bool) -> None:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#centerButtons-prop

        **centerButtons : bool**

        This property holds whether the buttons in the button box are centered

        By default, this property is `false`. This behavior is appropriate for
        most types of dialogs. A notable exception is message boxes on most
        platforms (e.g. Windows), where the button box is centered horizontally.

        **Access functions:**

        bool **centerButtons** () const
        void **setCenterButtons** (bool
        **center** )

        **See also** **QMessageBox** .
        """
        ...
    def setOrientation(self, orientation: PySide6.QtCore.Qt.Orientation) -> None:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#orientation-prop

        **orientation : Qt::Orientation**

        This property holds the orientation of the button box

        By default, the orientation is horizontal (i.e. the buttons are laid out
        side by side). The possible orientations are **Qt::Horizontal**  and
        **Qt::Vertical** .

        **Access functions:**

        Qt::Orientation **orientation** () const
        void **setOrientation**
        (Qt::Orientation **orientation** )
        """
        ...
    def setStandardButtons(
        self, buttons: PySide6.QtWidgets.QDialogButtonBox.StandardButtons
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#standardButtons-prop

        **standardButtons : StandardButtons**

        collection of standard buttons in the button box

        This property controls which standard buttons are used by the button
        box.

        **Access functions:**

        QDialogButtonBox::StandardButtons **standardButtons** () const
        void
        **setStandardButtons** (QDialogButtonBox::StandardButtons **buttons** )

        **See also** **addButton** ().

        **Member Function Documentation**
        """
        ...
    def standardButton(
        self, button: PySide6.QtWidgets.QAbstractButton
    ) -> PySide6.QtWidgets.QDialogButtonBox.StandardButton:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#standardButton

        **QDialogButtonBox::StandardButton
        QDialogButtonBox::standardButton(QAbstractButton * button ) const**

        Returns the standard button enum value corresponding to the given
        **button** , or **NoButton**  if the given **button** isn't a standard
        button.

        **See also** **button** (), **buttons** (), and **standardButtons** ().
        """
        ...
    def standardButtons(self) -> PySide6.QtWidgets.QDialogButtonBox.StandardButtons:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#standardButtons-prop

        **standardButtons : StandardButtons**

        collection of standard buttons in the button box

        This property controls which standard buttons are used by the button
        box.

        **Access functions:**

        QDialogButtonBox::StandardButtons **standardButtons** () const
        void
        **setStandardButtons** (QDialogButtonBox::StandardButtons **buttons** )

        **See also** **addButton** ().

        **Member Function Documentation**
        """
        ...
    @property
    def accepted(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#accepted

        **[signal] void QDialogButtonBox::accepted()**

        This signal is emitted when a button inside the button box is clicked,
        as long as it was defined with the **AcceptRole**  or **YesRole** .

        **See also** **rejected** (), **clicked** (), and **helpRequested** ().
        """
        ...
    @property
    def clicked(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#clicked

        **[signal] void QDialogButtonBox::clicked(QAbstractButton * button )**

        This signal is emitted when a button inside the button box is clicked.
        The specific button that was pressed is specified by **button**.

        **See also** **accepted** (), **rejected** (), and **helpRequested** ().
        """
        ...
    @property
    def helpRequested(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#helpRequested

        **[signal] void QDialogButtonBox::helpRequested()**

        This signal is emitted when a button inside the button box is clicked,
        as long as it was defined with the **HelpRole** .

        **See also** **accepted** (), **rejected** (), and **clicked** ().
        """
        ...
    @property
    def rejected(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdialogbuttonbox.html#rejected

        **[signal] void QDialogButtonBox::rejected()**

        This signal is emitted when a button inside the button box is clicked,
        as long as it was defined with the **RejectRole**  or **NoRole** .

        **See also** **accepted** (), **helpRequested** (), and **clicked** ().
        """
        ...
