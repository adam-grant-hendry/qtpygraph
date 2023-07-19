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

from collections.abc import Sequence
from typing import Any

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QItemDelegate(PySide6.QtWidgets.QAbstractItemDelegate):
    """
    https://doc.qt.io/qt-6/qitemdelegate.html

    **Detailed Description**

    QItemDelegate can be used to provide custom display features and editor
    widgets for item views based on **QAbstractItemView**  subclasses. Using a
    delegate for this purpose allows the display and editing mechanisms to be
    customized and developed independently from the model and view.

    The QItemDelegate class is one of the **Model/View Classes**  and is part of
    Qt's **model/view framework** . Note that **QStyledItemDelegate**  has taken
    over the job of drawing Qt's item views. We recommend the use of
    **QStyledItemDelegate**  when creating new delegates.

    When displaying items from a custom model in a standard view, it is often
    sufficient to simply ensure that the model returns appropriate data for each
    of the **roles**  that determine the appearance of items in views. The
    default delegate used by Qt's standard views uses this role information to
    display items in most of the common forms expected by users. However, it is
    sometimes necessary to have even more control over the appearance of items
    than the default delegate can provide.

    This class provides default implementations of the functions for painting
    item data in a view and editing data from item models. Default
    implementations of the **paint** () and **sizeHint** () virtual functions,
    defined in **QAbstractItemDelegate** , are provided to ensure that the
    delegate implements the correct basic behavior expected by views. You can
    reimplement these functions in subclasses to customize the appearance of
    items.

    When editing data in an item view, QItemDelegate provides an editor widget,
    which is a widget that is placed on top of the view while editing takes
    place. Editors are created with a **QItemEditorFactory** ; a default static
    instance provided by **QItemEditorFactory**  is installed on all item
    delegates. You can set a custom factory using **setItemEditorFactory** () or
    set a new default factory with **QItemEditorFactory::setDefaultFactory** ().
    It is the data stored in the item model with the **Qt::EditRole**  that is
    edited.

    Only the standard editing functions for widget-based delegates are
    reimplemented here:

    * **createEditor** () returns the widget used to change data from the model
    and can be reimplemented to customize editing behavior.
      *
    **setEditorData** () provides the widget with data to manipulate.
      *
    **updateEditorGeometry** () ensures that the editor is displayed correctly
    with respect to the item view.
      * **setModelData** () returns updated data
    to the model.

    The **closeEditor** () signal indicates that the user has completed editing
    the data, and that the editor widget can be destroyed.

    **Standard Roles and Data Types**

    The default delegate used by the standard views supplied with Qt associates
    each standard role (defined by **Qt::ItemDataRole** ) with certain data
    types. Models that return data in these types can influence the appearance
    of the delegate as described in the following table.

    RoleAccepted Types
    **Qt::BackgroundRole** **QBrush**  (
    **Qt::CheckStateRole** **Qt::CheckState**
    **Qt::DecorationRole** **QIcon**
    , **QPixmap**  and **QColor**
    **Qt::DisplayRole** **QString**  and types
    with a string representation
    **Qt::EditRole** See **QItemEditorFactory**
    for details
    **Qt::FontRole** **QFont**
    **Qt::SizeHintRole** **QSize**
    **Qt::TextAlignmentRole** **Qt::Alignment**
    **Qt::ForegroundRole**
    **QBrush**  (

    If the default delegate does not allow the level of customization that you
    need, either for display purposes or for editing data, it is possible to
    subclass QItemDelegate to implement the desired behavior.

    **Subclassing**

    When subclassing QItemDelegate to create a delegate that displays items
    using a custom renderer, it is important to ensure that the delegate can
    render items suitably for all the required states; e.g. selected, disabled,
    checked. The documentation for the **paint** () function contains some hints
    to show how this can be achieved.

    You can provide custom editors by using a **QItemEditorFactory** . The
    **Color Editor Factory Example**  shows how a custom editor can be made
    available to delegates with the default item editor factory. This way, there
    is no need to subclass QItemDelegate. An alternative is to reimplement
    **createEditor** (), **setEditorData** (), **setModelData** (), and
    **updateEditorGeometry** (). This process is described in the **Spin Box
    Delegate Example** .

    **QStyledItemDelegate vs. QItemDelegate**

    Since Qt 4.4, there are two delegate classes: QItemDelegate and
    **QStyledItemDelegate** . However, the default delegate is
    **QStyledItemDelegate** . These two classes are independent alternatives to
    painting and providing editors for items in views. The difference between
    them is that **QStyledItemDelegate**  uses the current style to paint its
    items. We therefore recommend using **QStyledItemDelegate**  as the base
    class when implementing custom delegates or when working with Qt style
    sheets. The code required for either class should be equal unless the custom
    delegate needs to use the style for drawing.

    **See also** **Delegate Classes** , **QStyledItemDelegate** ,
    **QAbstractItemDelegate** , **Spin Box Delegate Example** , **Settings
    Editor Example** , and **Icons Example** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#QItemDelegate

        **QItemDelegate::QItemDelegate(QObject * parent = nullptr)**

        Constructs an item delegate with the given **parent**.
        """
        ...
    def createEditor(
        self,
        parent: PySide6.QtWidgets.QWidget,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#createEditor

        **[override virtual] QWidget *QItemDelegate::createEditor(QWidget *
        parent , const QStyleOptionViewItem & option , const QModelIndex & index
        ) const**

        Reimplements: **QAbstractItemDelegate::createEditor(QWidget *parent,
        const QStyleOptionViewItem &option, const QModelIndex &index) const** .

        Returns the widget used to edit the item specified by **index** for
        editing. The **parent** widget and style **option** are used to control
        how the editor widget appears.

        **See also** **QAbstractItemDelegate::createEditor** ().
        """
        ...
    def decoration(
        self, option: PySide6.QtWidgets.QStyleOptionViewItem, variant: Any
    ) -> PySide6.QtGui.QPixmap: ...
    def doCheck(
        self,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        bounding: PySide6.QtCore.QRect,
        variant: Any,
    ) -> PySide6.QtCore.QRect: ...
    def drawBackground(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#drawBackground

        **[protected] void QItemDelegate::drawBackground(QPainter * painter ,
        const QStyleOptionViewItem & option , const QModelIndex & index )
        const**

        Renders the item background for the given **index** , using the given
        **painter** and style **option**.
        """
        ...
    def drawCheck(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        rect: PySide6.QtCore.QRect,
        state: PySide6.QtCore.Qt.CheckState,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#drawCheck

        **[virtual protected] void QItemDelegate::drawCheck(QPainter * painter ,
        const QStyleOptionViewItem & option , const QRect & rect ,
        Qt::CheckState state ) const**

        Renders a check indicator within the rectangle specified by **rect** ,
        using the given **painter** and style **option** , using the given
        **state**.
        """
        ...
    def drawDecoration(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        rect: PySide6.QtCore.QRect,
        pixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage | str,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#drawDecoration

        **[virtual protected] void QItemDelegate::drawDecoration(QPainter *
        painter , const QStyleOptionViewItem & option , const QRect & rect ,
        const QPixmap & pixmap ) const**

        Renders the decoration **pixmap** within the rectangle specified by
        **rect** using the given **painter** and style **option**.
        """
        ...
    def drawDisplay(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        rect: PySide6.QtCore.QRect,
        text: str,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#drawDisplay

        **[virtual protected] void QItemDelegate::drawDisplay(QPainter * painter
        , const QStyleOptionViewItem & option , const QRect & rect , const
        QString & text ) const**

        Renders the item view **text** within the rectangle specified by
        **rect** using the given **painter** and style **option**.
        """
        ...
    def drawFocus(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        rect: PySide6.QtCore.QRect,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#drawFocus

        **[virtual protected] void QItemDelegate::drawFocus(QPainter * painter ,
        const QStyleOptionViewItem & option , const QRect & rect ) const**

        Renders the region within the rectangle specified by **rect** ,
        indicating that it has the focus, using the given **painter** and style
        **option**.
        """
        ...
    def editorEvent(
        self,
        event: PySide6.QtCore.QEvent,
        model: PySide6.QtCore.QAbstractItemModel,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#editorEvent

        **[override virtual protected] bool QItemDelegate::editorEvent(QEvent *
        event , QAbstractItemModel * model , const QStyleOptionViewItem & option
        , const QModelIndex & index )**

        Reimplements: **QAbstractItemDelegate::editorEvent** (QEvent *event,
        QAbstractItemModel *model, const QStyleOptionViewItem &option, const
        QModelIndex &index).
        """
        ...
    def eventFilter(
        self, object: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#eventFilter

        **[override virtual protected] bool QItemDelegate::eventFilter(QObject *
        editor , QEvent * event )**

        Reimplements: **QObject::eventFilter** (QObject *watched, QEvent
        *event).

        Returns `true` if the given **editor** is a valid **QWidget**  and the
        given **event** is handled; otherwise returns `false`. The following key
        press events are handled by default:

        * **Tab**
          * **Backtab**
          * **Enter**
          * **Return**
          * **Esc**

        In the case of **Tab** , **Backtab** , **Enter** and **Return** key
        press events, the **editor** 's data is committed to the model and the
        editor is closed. If the **event** is a **Tab** key press the view will
        open an editor on the next item in the view. Likewise, if the **event**
        is a **Backtab** key press the view will open an editor on the
        **previous** item in the view.

        If the event is a **Esc** key press event, the **editor** is closed
        **without** committing its data.

        **See also** **commitData** () and **closeEditor** ().
        """
        ...
    def hasClipping(self) -> bool: ...
    def itemEditorFactory(self) -> PySide6.QtWidgets.QItemEditorFactory:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#itemEditorFactory

        **QItemEditorFactory *QItemDelegate::itemEditorFactory() const**

        Returns the editor factory used by the item delegate. If no editor
        factory is set, the function will return null.

        **See also** **setItemEditorFactory** ().
        """
        ...
    def paint(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#paint

        **[override virtual] void QItemDelegate::paint(QPainter * painter ,
        const QStyleOptionViewItem & option , const QModelIndex & index )
        const**

        Reimplements: **QAbstractItemDelegate::paint(QPainter *painter, const
        QStyleOptionViewItem &option, const QModelIndex &index) const** .

        Renders the delegate using the given **painter** and style **option**
        for the item specified by **index**.

        When reimplementing this function in a subclass, you should update the
        area held by the option's **rect**  variable, using the option's
        **state**  variable to determine the state of the item to be displayed,
        and adjust the way it is painted accordingly.

        For example, a selected item may need to be displayed differently to
        unselected items, as shown in the following code:

        if (option.state & **QStyle** ::State_Selected)
        painter->fillRect(option.rect, option.palette.highlight());
        const int size = qMin(option.rect.width(), option.rect.height());
        const int brightness = index.model()->data(index,
        Qt::DisplayRole).toInt();
                const double radius = (size / 2.0) -
        (brightness / 255.0 * size / 2.0);
                if (qFuzzyIsNull(radius))
        return;

                painter->save();
        painter->setRenderHint(**QPainter** ::Antialiasing, true);
        painter->setPen(Qt::NoPen);
                if (option.state & **QStyle**
        ::State_Selected)
        painter->setBrush(option.palette.highlightedText());
                else
        ...

        After painting, you should ensure that the painter is returned to its
        the state it was supplied in when this function was called. For example,
        it may be useful to call **QPainter::save** () before painting and
        **QPainter::restore** () afterwards.

        **See also** **QStyle::State** .
        """
        ...
    def rect(
        self,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        role: int,
    ) -> PySide6.QtCore.QRect: ...
    @staticmethod
    def selectedPixmap(
        pixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage | str,
        palette: (
            PySide6.QtGui.QPalette | PySide6.QtCore.Qt.GlobalColor | PySide6.QtGui.QColor
        ),
        enabled: bool,
    ) -> PySide6.QtGui.QPixmap: ...
    def setClipping(self, clip: bool) -> None:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#clipping-prop

        **clipping : bool**

        if the delegate should clip the paint events

        This property will set the paint clip to the size of the item. The
        default value is on. It is useful for cases such as when images are
        larger than the size of the item.

        **Access functions:**

        bool **hasClipping** () const
        void **setClipping** (bool **clip** )

        **Member Function Documentation**
        """
        ...
    def setEditorData(
        self,
        editor: PySide6.QtWidgets.QWidget,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#setEditorData

        **[override virtual] void QItemDelegate::setEditorData(QWidget * editor
        , const QModelIndex & index ) const**

        Reimplements: **QAbstractItemDelegate::setEditorData(QWidget *editor,
        const QModelIndex &index) const** .

        Sets the data to be displayed and edited by the **editor** from the data
        model item specified by the model **index**.

        The default implementation stores the data in the **editor** widget's
        **user property** .

        **See also** **QMetaProperty::isUser** ().
        """
        ...
    def setItemEditorFactory(self, factory: PySide6.QtWidgets.QItemEditorFactory) -> None:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#setItemEditorFactory

        **void QItemDelegate::setItemEditorFactory(QItemEditorFactory * factory
        )**

        Sets the editor factory to be used by the item delegate to be the
        **factory** specified. If no editor factory is set, the item delegate
        will use the default editor factory.

        **See also** **itemEditorFactory** ().
        """
        ...
    def setModelData(
        self,
        editor: PySide6.QtWidgets.QWidget,
        model: PySide6.QtCore.QAbstractItemModel,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#setModelData

        **[override virtual] void QItemDelegate::setModelData(QWidget * editor ,
        QAbstractItemModel * model , const QModelIndex & index ) const**

        Reimplements: **QAbstractItemDelegate::setModelData(QWidget *editor,
        QAbstractItemModel *model, const QModelIndex &index) const** .

        Gets data from the **editor** widget and stores it in the specified
        **model** at the item **index**.

        The default implementation gets the value to be stored in the data model
        from the **editor** widget's **user property** .

        **See also** **QMetaProperty::isUser** ().
        """
        ...
    def setOptions(
        self,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
    ) -> PySide6.QtWidgets.QStyleOptionViewItem: ...
    def sizeHint(
        self,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#sizeHint

        **[override virtual] QSize QItemDelegate::sizeHint(const
        QStyleOptionViewItem & option , const QModelIndex & index ) const**

        Reimplements: **QAbstractItemDelegate::sizeHint(const
        QStyleOptionViewItem &option, const QModelIndex &index) const** .

        Returns the size needed by the delegate to display the item specified by
        **index** , taking into account the style information provided by
        **option**.

        When reimplementing this function, note that in case of text items,
        **QItemDelegate**  adds a margin (i.e. 2 *
        **QStyle::PM_FocusFrameHMargin** ) to the length of the text.
        """
        ...
    def textRectangle(
        self,
        painter: PySide6.QtGui.QPainter,
        rect: PySide6.QtCore.QRect,
        font: PySide6.QtGui.QFont | str | Sequence[str],
        text: str,
    ) -> PySide6.QtCore.QRect: ...
    def updateEditorGeometry(
        self,
        editor: PySide6.QtWidgets.QWidget,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qitemdelegate.html#updateEditorGeometry

        **[override virtual] void QItemDelegate::updateEditorGeometry(QWidget *
        editor , const QStyleOptionViewItem & option , const QModelIndex & index
        ) const**

        Reimplements: **QAbstractItemDelegate::updateEditorGeometry(QWidget
        *editor, const QStyleOptionViewItem &option, const QModelIndex &index)
        const** .

        Updates the **editor** for the item specified by **index** according to
        the style **option** given.
        """
        ...