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

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QAbstractItemDelegate(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qabstractitemdelegate.html

    **Detailed Description**

    A QAbstractItemDelegate provides the interface and common functionality for
    delegates in the model/view architecture. Delegates display individual items
    in views, and handle the editing of model data.

    The QAbstractItemDelegate class is one of the **Model/View Classes**  and is
    part of Qt's **model/view framework** .

    To render an item in a custom way, you must implement **paint** () and
    **sizeHint** (). The **QStyledItemDelegate**  class provides default
    implementations for these functions; if you do not need custom rendering,
    subclass that class instead.

    We give an example of drawing a progress bar in items; in our case for a
    package management program.

    ![](images/widgetdelegate.png)

    We create the `WidgetDelegate` class, which inherits from
    **QStyledItemDelegate** . We do the drawing in the **paint** () function:

    void WidgetDelegate::paint(**QPainter**  *painter, const
    **QStyleOptionViewItem**  &option,
                                   const
    **QModelIndex**  &index) const
        {
            if (index.column() == 1) {
    int progress = index.data().toInt();
    **QStyleOptionProgressBar**  progressBarOption;
    progressBarOption.rect = option.rect;
                progressBarOption.minimum
    = 0;
                progressBarOption.maximum = 100;
    progressBarOption.progress = progress;
                progressBarOption.text =
    **QString** ::number(progress) + "%";
    progressBarOption.textVisible = true;

                **QApplication**
    ::style()->drawControl(**QStyle** ::CE_ProgressBar,
    &progressBarOption, painter);
            } else
    **QStyledItemDelegate** ::paint(painter, option, index);

    Notice that we use a **QStyleOptionProgressBar**  and initialize its
    members. We can then use the current **QStyle**  to draw it.

    To provide custom editing, there are two approaches that can be used. The
    first approach is to create an editor widget and display it directly on top
    of the item. To do this you must reimplement **createEditor** () to provide
    an editor widget, **setEditorData** () to populate the editor with the data
    from the model, and **setModelData** () so that the delegate can update the
    model with data from the editor.

    The second approach is to handle user events directly by reimplementing
    **editorEvent** ().

    **See also** **Model/View Programming** , **QStyledItemDelegate** ,
    **Pixelator Example** , **QStyledItemDelegate** , and **QStyle** .
    """

    NoHint: QAbstractItemDelegate.EndEditHint = ...
    EditNextItem: QAbstractItemDelegate.EndEditHint = ...
    EditPreviousItem: QAbstractItemDelegate.EndEditHint = ...
    SubmitModelCache: QAbstractItemDelegate.EndEditHint = ...
    RevertModelCache: QAbstractItemDelegate.EndEditHint = ...

    class EndEditHint(IntFlag):
        NoHint: QAbstractItemDelegate.EndEditHint = ...
        EditNextItem: QAbstractItemDelegate.EndEditHint = ...
        EditPreviousItem: QAbstractItemDelegate.EndEditHint = ...
        SubmitModelCache: QAbstractItemDelegate.EndEditHint = ...
        RevertModelCache: QAbstractItemDelegate.EndEditHint = ...
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#QAbstractItemDelegate

        **QAbstractItemDelegate::QAbstractItemDelegate(QObject * parent =
        nullptr)**

        Creates a new abstract item delegate with the given **parent**.
        """
        ...
    def createEditor(
        self,
        parent: PySide6.QtWidgets.QWidget,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#createEditor

        **[virtual] QWidget *QAbstractItemDelegate::createEditor(QWidget *
        parent , const QStyleOptionViewItem & option , const QModelIndex & index
        ) const**

        Returns the editor to be used for editing the data item with the given
        **index**. Note that the index contains information about the model
        being used. The editor's parent widget is specified by **parent** , and
        the item options by **option**.

        The base implementation returns `nullptr`. If you want custom editing
        you will need to reimplement this function.

        The returned editor widget should have **Qt::StrongFocus** ; otherwise,
        **QMouseEvent** s received by the widget will propagate to the view. The
        view's background will shine through unless the editor paints its own
        background (e.g., with **setAutoFillBackground** ()).

        **See also** **destroyEditor** (), **setModelData** (), and
        **setEditorData** ().
        """
        ...
    def destroyEditor(
        self,
        editor: PySide6.QtWidgets.QWidget,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#destroyEditor

        **[virtual, since 5.0] void QAbstractItemDelegate::destroyEditor(QWidget
        * editor , const QModelIndex & index ) const**

        Called when the **editor** is no longer needed for editing the data item
        with the given **index** and should be destroyed. The default behavior
        is a call to deleteLater on the editor. It is possible e.g. to avoid
        this delete by reimplementing this function.

        This function was introduced in Qt 5.0.

        **See also** **createEditor** ().
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
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#editorEvent

        **[virtual] bool QAbstractItemDelegate::editorEvent(QEvent * event ,
        QAbstractItemModel * model , const QStyleOptionViewItem & option , const
        QModelIndex & index )**

        When editing of an item starts, this function is called with the
        **event** that triggered the editing, the **model** , the **index** of
        the item, and the **option** used for rendering the item.

        Mouse events are sent to editorEvent() even if they don't start editing
        of the item. This can, for instance, be useful if you wish to open a
        context menu when the right mouse button is pressed on an item.

        The base implementation returns `false` (indicating that it has not
        handled the event).
        """
        ...
    def helpEvent(
        self,
        event: PySide6.QtGui.QHelpEvent,
        view: PySide6.QtWidgets.QAbstractItemView,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#helpEvent

        **[virtual] bool QAbstractItemDelegate::helpEvent(QHelpEvent * event ,
        QAbstractItemView * view , const QStyleOptionViewItem & option , const
        QModelIndex & index )**

        Whenever a help event occurs, this function is called with the **event**
        **view** **option** and the **index** that corresponds to the item where
        the event occurs.

        Returns `true` if the delegate can handle the event; otherwise returns
        `false`. A return value of true indicates that the data obtained using
        the index had the required role.

        For **QEvent::ToolTip**  and **QEvent::WhatsThis**  events that were
        handled successfully, the relevant popup may be shown depending on the
        user's system configuration.

        **See also** **QHelpEvent** .
        """
        ...
    def paint(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#paint

        **[pure virtual] void QAbstractItemDelegate::paint(QPainter * painter ,
        const QStyleOptionViewItem & option , const QModelIndex & index )
        const**

        This pure abstract function must be reimplemented if you want to provide
        custom rendering. Use the **painter** and style **option** to render the
        item specified by the item **index**.

        If you reimplement this you must also reimplement **sizeHint** ().
        """
        ...
    def paintingRoles(self) -> list[int]: ...
    def setEditorData(
        self,
        editor: PySide6.QtWidgets.QWidget,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#setEditorData

        **[virtual] void QAbstractItemDelegate::setEditorData(QWidget * editor ,
        const QModelIndex & index ) const**

        Sets the contents of the given **editor** to the data for the item at
        the given **index**. Note that the index contains information about the
        model being used.

        The base implementation does nothing. If you want custom editing you
        will need to reimplement this function.

        **See also** **setModelData** ().
        """
        ...
    def setModelData(
        self,
        editor: PySide6.QtWidgets.QWidget,
        model: PySide6.QtCore.QAbstractItemModel,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#setModelData

        **[virtual] void QAbstractItemDelegate::setModelData(QWidget * editor ,
        QAbstractItemModel * model , const QModelIndex & index ) const**

        Sets the data for the item at the given **index** in the **model** to
        the contents of the given **editor**.

        The base implementation does nothing. If you want custom editing you
        will need to reimplement this function.

        **See also** **setEditorData** ().
        """
        ...
    def sizeHint(
        self,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#sizeHint

        **[pure virtual] QSize QAbstractItemDelegate::sizeHint(const
        QStyleOptionViewItem & option , const QModelIndex & index ) const**

        This pure abstract function must be reimplemented if you want to provide
        custom rendering. The options are specified by **option** and the model
        item by **index**.

        If you reimplement this you must also reimplement **paint** ().
        """
        ...
    def updateEditorGeometry(
        self,
        editor: PySide6.QtWidgets.QWidget,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#updateEditorGeometry

        **[virtual] void QAbstractItemDelegate::updateEditorGeometry(QWidget *
        editor , const QStyleOptionViewItem & option , const QModelIndex & index
        ) const**

        Updates the geometry of the **editor** for the item with the given
        **index** , according to the rectangle specified in the **option**. If
        the item has an internal layout, the editor will be laid out
        accordingly. Note that the index contains information about the model
        being used.

        The base implementation does nothing. If you want custom editing you
        must reimplement this function.
        """
        ...
    @property
    def closeEditor(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#closeEditor

        **[signal] void QAbstractItemDelegate::closeEditor(QWidget * editor ,
        QAbstractItemDelegate::EndEditHint hint = NoHint)**

        This signal is emitted when the user has finished editing an item using
        the specified **editor**.

        The **hint** provides a way for the delegate to influence how the model
        and view behave after editing is completed. It indicates to these
        components what action should be performed next to provide a comfortable
        editing experience for the user. For example, if `EditNextItem` is
        specified, the view should use a delegate to open an editor on the next
        item in the model.

        **See also** **EndEditHint** .
        """
        ...
    @property
    def commitData(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#commitData

        **[signal] void QAbstractItemDelegate::commitData(QWidget * editor )**

        This signal must be emitted when the **editor** widget has completed
        editing the data, and wants to write it back into the model.
        """
        ...
    @property
    def sizeHintChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qabstractitemdelegate.html#sizeHintChanged

        **[signal] void QAbstractItemDelegate::sizeHintChanged(const QModelIndex
        & index )**

        This signal must be emitted when the **sizeHint** () of **index**
        changed.

        Views automatically connect to this signal and relayout items as
        necessary.
        """
        ...
