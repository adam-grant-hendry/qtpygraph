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

class QGraphicsLayout(PySide6.QtWidgets.QGraphicsLayoutItem):
    """
    https://doc.qt.io/qt-6/qgraphicslayout.html

    **Detailed Description**

    QGraphicsLayout is an abstract class that defines a virtual API for
    arranging **QGraphicsWidget**  children and other **QGraphicsLayoutItem**
    objects for a **QGraphicsWidget** . **QGraphicsWidget**  assigns
    responsibility to a QGraphicsLayout through **QGraphicsWidget::setLayout**
    (). As the widget is resized, the layout will automatically arrange the
    widget's children. QGraphicsLayout inherits **QGraphicsLayoutItem** , so, it
    can be managed by any layout, including its own subclasses.

    **Writing a Custom Layout**

    You can use QGraphicsLayout as a base to write your own custom layout (e.g.,
    a flowlayout), but it is more common to use one of its subclasses instead -
    **QGraphicsLinearLayout**  or **QGraphicsGridLayout** . When creating a
    custom layout, the following functions must be reimplemented as a bare
    minimum:

    FunctionDescription
    **QGraphicsLayoutItem::setGeometry** ()Notifies you
    when the geometry of the layout is set. You can store the geometry in your
    own layout class in a reimplementation of this function.
    **QGraphicsLayoutItem::sizeHint** ()Returns the layout's size hints.
    **QGraphicsLayout::count** ()Returns the number of items in your layout.
    **QGraphicsLayout::itemAt** ()Returns a pointer to an item in your layout.
    **QGraphicsLayout::removeAt** ()Removes an item from your layout without
    destroying it.

    For more details on how to implement each function, refer to the individual
    function documentation.

    Each layout defines its own API for arranging widgets and layout items. For
    example, with a grid layout, you require a row and a column index with
    optional row and column spans, alignment, spacing, and more. A linear
    layout, however, requires a single row or column index to position its
    items. For a grid layout, the order of insertion does not affect the layout
    in any way, but for a linear layout, the order is essential. When writing
    your own layout subclass, you are free to choose the API that best suits
    your layout.

    QGraphicsLayout provides the **addChildLayoutItem** () convenience function
    to add layout items to a custom layout. The function will automatically
    reparent graphics items, if required.

    **Activating the Layout**

    When the layout's geometry changes, QGraphicsLayout immediately rearranges
    all of its managed items by calling **setGeometry** () on each item. This
    rearrangement is called **activating** the layout.

    QGraphicsLayout updates its own geometry to match the **contentsRect** () of
    the **QGraphicsLayoutItem**  it is managing. Thus, it will automatically
    rearrange all its items when the widget is resized. QGraphicsLayout caches
    the sizes of all its managed items to avoid calling **setGeometry** () too
    often.

    **Note:** A QGraphicsLayout will have the same geometry as the
    **contentsRect** () of the widget (not the layout) it is assigned to.

    **Activating the Layout Implicitly**

    The layout can be activated implicitly using one of two ways: by calling
    **activate** () or by calling **invalidate** (). Calling **activate** ()
    activates the layout immediately. In contrast, calling **invalidate** () is
    delayed, as it posts a **LayoutRequest**  event to the managed widget. Due
    to event compression, the **activate** () will only be called once after
    control has returned to the event loop. This is referred to as
    **invalidating** the layout. Invalidating the layout also invalidates any
    cached information. Also, the **invalidate** () function is a virtual
    function. So, you can invalidate your own cache in a subclass of
    QGraphicsLayout by reimplementing this function.

    **Event Handling**

    QGraphicsLayout listens to events for the widget it manages through the
    virtual **widgetEvent** () event handler. When the layout is assigned to a
    widget, all events delivered to the widget are first processed by
    **widgetEvent** (). This allows the layout to be aware of any relevant state
    changes on the widget such as visibility changes or layout direction
    changes.

    **Margin Handling**

    The margins of a QGraphicsLayout can be modified by reimplementing
    **setContentsMargins** () and **getContentsMargins** ().
    """

    def __init__(
        self, parent: PySide6.QtWidgets.QGraphicsLayoutItem | None = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslayout.html#QGraphicsLayout

        **QGraphicsLayout::QGraphicsLayout(QGraphicsLayoutItem * parent =
        nullptr)**

        Constructs a QGraphicsLayout object.

        **parent** is passed to **QGraphicsLayoutItem** 's constructor and the
        **QGraphicsLayoutItem** 's isLayout argument is set to **true**.

        If **parent** is a **QGraphicsWidget**  the layout will be installed on
        that widget. (Note that installing a layout will delete the old one
        installed.)
        """
        ...
    def activate(self) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslayout.html#activate

        **void QGraphicsLayout::activate()**

        Activates the layout, causing all items in the layout to be immediately
        rearranged. This function is based on calling **count** () and
        **itemAt** (), and then calling **setGeometry** () on all items
        sequentially. When activated, the layout will adjust its geometry to its
        parent's **contentsRect** (). The parent will then invalidate any layout
        of its own.

        If called in sequence or recursively, e.g., by one of the arranged items
        in response to being resized, this function will do nothing.

        Note that the layout is free to use geometry caching to optimize this
        process. To forcefully invalidate any such cache, you can call
        **invalidate** () before calling activate().

        **See also** **invalidate** ().
        """
        ...
    def addChildLayoutItem(
        self, layoutItem: PySide6.QtWidgets.QGraphicsLayoutItem
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslayout.html#addChildLayoutItem

        **[protected] void
        QGraphicsLayout::addChildLayoutItem(QGraphicsLayoutItem * layoutItem )**

        This function is a convenience function provided for custom layouts, and
        will go through all items in the layout and reparent their graphics
        items to the closest **QGraphicsWidget**  ancestor of the layout.

        If **layoutItem** is already in a different layout, it will be removed
        from that layout.

        If custom layouts want special behaviour they can ignore to use this
        function, and implement their own behaviour.

        **See also** **graphicsItem** ().
        """
        ...
    def count(self) -> int:
        """
        https://doc.qt.io/qt-6/qgraphicslayout.html#count

        **[pure virtual] int QGraphicsLayout::count() const**

        This pure virtual function must be reimplemented in a subclass of
        **QGraphicsLayout**  to return the number of items in the layout.

        The subclass is free to decide how to store the items.

        **See also** **itemAt** () and **removeAt** ().
        """
        ...
    def getContentsMargins(self) -> tuple[float, float, float, float]:
        """
        https://doc.qt.io/qt-6/qgraphicslayout.html#getContentsMargins

        **[override virtual] void QGraphicsLayout::getContentsMargins(qreal *
        left , qreal * top , qreal * right , qreal * bottom ) const**

        Reimplements: **QGraphicsLayoutItem::getContentsMargins(qreal *left,
        qreal *top, qreal *right, qreal *bottom) const** .
        """
        ...
    @staticmethod
    def instantInvalidatePropagation() -> bool: ...
    def invalidate(self) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslayout.html#invalidate

        **[virtual] void QGraphicsLayout::invalidate()**

        Clears any cached geometry and size hint information in the layout, and
        posts a **LayoutRequest**  event to the managed parent
        **QGraphicsLayoutItem** .

        **See also** **activate** () and **setGeometry** ().
        """
        ...
    def isActivated(self) -> bool:
        """
        https://doc.qt.io/qt-6/qgraphicslayout.html#isActivated

        **bool QGraphicsLayout::isActivated() const**

        Returns `true` if the layout is currently being activated; otherwise,
        returns `false`. If the layout is being activated, this means that it is
        currently in the process of rearranging its items (i.e., the
        **activate** () function has been called, and has not yet returned).

        **See also** **activate** () and **invalidate** ().
        """
        ...
    def itemAt(self, i: int) -> PySide6.QtWidgets.QGraphicsLayoutItem:
        """
        https://doc.qt.io/qt-6/qgraphicslayout.html#itemAt

        **[pure virtual] QGraphicsLayoutItem *QGraphicsLayout::itemAt(int i )
        const**

        This pure virtual function must be reimplemented in a subclass of
        **QGraphicsLayout**  to return a pointer to the item at index **i**. The
        reimplementation can assume that **i** is valid (i.e., it respects the
        value of **count** ()). Together with **count** (), it is provided as a
        means of iterating over all items in a layout.

        The subclass is free to decide how to store the items, and the visual
        arrangement does not have to be reflected through this function.

        **See also** **count** () and **removeAt** ().
        """
        ...
    def removeAt(self, index: int) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslayout.html#removeAt

        **[pure virtual] void QGraphicsLayout::removeAt(int index )**

        This pure virtual function must be reimplemented in a subclass of
        **QGraphicsLayout**  to remove the item at **index**. The
        reimplementation can assume that **index** is valid (i.e., it respects
        the value of **count** ()).

        The implementation must ensure that the **parentLayoutItem** () of the
        removed item does not point to this layout, since the item is considered
        to be removed from the layout hierarchy.

        If the layout is to be reused between applications, we recommend that
        the layout deletes the item, but the graphics view framework does not
        depend on this.

        The subclass is free to decide how to store the items.

        **See also** **itemAt** () and **count** ().
        """
        ...
    def setContentsMargins(
        self, left: float, top: float, right: float, bottom: float
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslayout.html#setContentsMargins

        **void QGraphicsLayout::setContentsMargins(qreal left , qreal top ,
        qreal right , qreal bottom )**

        Sets the contents margins to **left** , **top** , **right** and
        **bottom**. The default contents margins for toplevel layouts are style
        dependent (by querying the pixelMetric for
        **QStyle::PM_LayoutLeftMargin** , **QStyle::PM_LayoutTopMargin** ,
        **QStyle::PM_LayoutRightMargin**  and **QStyle::PM_LayoutBottomMargin**
        ).

        For sublayouts the default margins are 0.

        Changing the contents margins automatically invalidates the layout.

        **See also** **invalidate** ().
        """
        ...
    @staticmethod
    def setInstantInvalidatePropagation(enable: bool) -> None: ...
    def updateGeometry(self) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslayout.html#updateGeometry

        **[override virtual] void QGraphicsLayout::updateGeometry()**

        Reimplements: **QGraphicsLayoutItem::updateGeometry** ().
        """
        ...
    def widgetEvent(self, e: PySide6.QtCore.QEvent) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicslayout.html#widgetEvent

        **[virtual] void QGraphicsLayout::widgetEvent(QEvent * e )**

        This virtual event handler receives all events for the managed widget.
        **QGraphicsLayout**  uses this event handler to listen for layout
        related events such as geometry changes, layout changes or layout
        direction changes.

        **e** is a pointer to the event.

        You can reimplement this event handler to track similar events for your
        own custom layout.

        **See also** **QGraphicsWidget::event** () and
        **QGraphicsItem::sceneEvent** ().
        """
        ...
