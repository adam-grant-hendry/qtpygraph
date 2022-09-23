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

class QSizePolicy:
    """
    https://doc.qt.io/qt-6/qsizepolicy.html

    **Detailed Description**

    The size policy of a widget is an expression of its willingness to be
    resized in various ways, and affects how the widget is treated by the
    **layout engine** . Each widget returns a QSizePolicy that describes the
    horizontal and vertical resizing policy it prefers when being laid out. You
    can change this for a specific widget by changing its
    **QWidget::sizePolicy**  property.

    QSizePolicy contains two independent **QSizePolicy::Policy**  values and two
    stretch factors; one describes the widgets's horizontal size policy, and the
    other describes its vertical size policy. It also contains a flag to
    indicate whether the height and width of its preferred size are related.

    The horizontal and vertical policies can be set in the constructor, and
    altered using the **setHorizontalPolicy** () and **setVerticalPolicy** ()
    functions. The stretch factors can be set using the **setHorizontalStretch**
    () and **setVerticalStretch** () functions. The flag indicating whether the
    widget's **sizeHint** () is width-dependent (such as a menu bar or a word-
    wrapping label) can be set using the **setHeightForWidth** () function.

    The current size policies and stretch factors be retrieved using the
    **horizontalPolicy** (), **verticalPolicy** (), **horizontalStretch** () and
    **verticalStretch** () functions. Alternatively, use the **transpose** ()
    function to swap the horizontal and vertical policies and stretches. The
    **hasHeightForWidth** () function returns the current status of the flag
    indicating the size hint dependencies.

    Use the **expandingDirections** () function to determine whether the
    associated widget can make use of more space than its **sizeHint** ()
    function indicates, as well as find out in which directions it can expand.

    Finally, the QSizePolicy class provides operators comparing this size policy
    to a given policy, as well as a **QVariant**  operator storing this
    QSizePolicy as a **QVariant**  object.

    **See also** **QSize** , **QWidget::sizeHint** (), **QWidget::sizePolicy** ,
    and **QLayoutItem::sizeHint** ().
    """

    DefaultType: QSizePolicy.ControlType = ...
    ButtonBox: QSizePolicy.ControlType = ...
    CheckBox: QSizePolicy.ControlType = ...
    ComboBox: QSizePolicy.ControlType = ...
    Frame: QSizePolicy.ControlType = ...
    GroupBox: QSizePolicy.ControlType = ...
    Label: QSizePolicy.ControlType = ...
    Line: QSizePolicy.ControlType = ...
    LineEdit: QSizePolicy.ControlType = ...
    PushButton: QSizePolicy.ControlType = ...
    RadioButton: QSizePolicy.ControlType = ...
    Slider: QSizePolicy.ControlType = ...
    SpinBox: QSizePolicy.ControlType = ...
    TabWidget: QSizePolicy.ControlType = ...
    ToolButton: QSizePolicy.ControlType = ...
    Fixed: QSizePolicy.Policy = ...
    Minimum: QSizePolicy.Policy = ...
    MinimumExpanding: QSizePolicy.Policy = ...
    Maximum: QSizePolicy.Policy = ...
    Preferred: QSizePolicy.Policy = ...
    Expanding: QSizePolicy.Policy = ...
    Ignored: QSizePolicy.Policy = ...
    GrowFlag: QSizePolicy.PolicyFlag = ...
    ExpandFlag: QSizePolicy.PolicyFlag = ...
    ShrinkFlag: QSizePolicy.PolicyFlag = ...
    IgnoreFlag: QSizePolicy.PolicyFlag = ...

    class ControlType(IntFlag):
        DefaultType: QSizePolicy.ControlType = ...
        ButtonBox: QSizePolicy.ControlType = ...
        CheckBox: QSizePolicy.ControlType = ...
        ComboBox: QSizePolicy.ControlType = ...
        Frame: QSizePolicy.ControlType = ...
        GroupBox: QSizePolicy.ControlType = ...
        Label: QSizePolicy.ControlType = ...
        Line: QSizePolicy.ControlType = ...
        LineEdit: QSizePolicy.ControlType = ...
        PushButton: QSizePolicy.ControlType = ...
        RadioButton: QSizePolicy.ControlType = ...
        Slider: QSizePolicy.ControlType = ...
        SpinBox: QSizePolicy.ControlType = ...
        TabWidget: QSizePolicy.ControlType = ...
        ToolButton: QSizePolicy.ControlType = ...

    class ControlTypes: ...

    class Policy(IntFlag):
        Fixed: QSizePolicy.Policy = ...
        Minimum: QSizePolicy.Policy = ...
        MinimumExpanding: QSizePolicy.Policy = ...
        Maximum: QSizePolicy.Policy = ...
        Preferred: QSizePolicy.Policy = ...
        Expanding: QSizePolicy.Policy = ...
        Ignored: QSizePolicy.Policy = ...

    class PolicyFlag(IntFlag):
        GrowFlag: QSizePolicy.PolicyFlag = ...
        ExpandFlag: QSizePolicy.PolicyFlag = ...
        ShrinkFlag: QSizePolicy.PolicyFlag = ...
        IgnoreFlag: QSizePolicy.PolicyFlag = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#QSizePolicy

        **QSizePolicy::QSizePolicy()**

        Constructs a QSizePolicy object with **Fixed**  as its horizontal and
        vertical policies.

        The policies can be altered using the **setHorizontalPolicy** () and
        **setVerticalPolicy** () functions. Use the **setHeightForWidth** ()
        function if the preferred height of the widget is dependent on the width
        of the widget (for example, a **QLabel**  with line wrapping).

        **See also** **setHorizontalStretch** () and **setVerticalStretch** ().
        """
        ...
    @overload
    def __init__(
        self,
        horizontal: PySide6.QtWidgets.QSizePolicy.Policy,
        vertical: PySide6.QtWidgets.QSizePolicy.Policy,
        type: PySide6.QtWidgets.QSizePolicy.ControlType = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#QSizePolicy-1

        **QSizePolicy::QSizePolicy(QSizePolicy::Policy horizontal ,
        QSizePolicy::Policy vertical , QSizePolicy::ControlType type =
        DefaultType)**

        Constructs a QSizePolicy object with the given **horizontal** and
        **vertical** policies, and the specified control **type**.

        Use **setHeightForWidth** () if the preferred height of the widget is
        dependent on the width of the widget (for example, a **QLabel**  with
        line wrapping).

        **See also** **setHorizontalStretch** (), **setVerticalStretch** (), and
        **controlType** ().
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(
        self, arg__1: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(
        self, arg__1: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    def controlType(self) -> PySide6.QtWidgets.QSizePolicy.ControlType:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#controlType

        **QSizePolicy::ControlType QSizePolicy::controlType() const**

        Returns the control type associated with the widget for which this size
        policy applies.

        **See also** **setControlType** ().
        """
        ...
    def expandingDirections(self) -> PySide6.QtCore.Qt.Orientations:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#expandingDirections

        **Qt::Orientations QSizePolicy::expandingDirections() const**

        Returns whether a widget can make use of more space than the
        **QWidget::sizeHint** () function indicates.

        A value of **Qt::Horizontal**  or **Qt::Vertical**  means that the
        widget can grow horizontally or vertically (i.e., the horizontal or
        vertical policy is **Expanding**  or **MinimumExpanding** ), whereas
        **Qt::Horizontal**  | **Qt::Vertical**  means that it can grow in both
        dimensions.

        **See also** **horizontalPolicy** () and **verticalPolicy** ().
        """
        ...
    def hasHeightForWidth(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#hasHeightForWidth

        **bool QSizePolicy::hasHeightForWidth() const**

        Returns `true` if the widget's preferred height depends on its width;
        otherwise returns `false`.

        **See also** **setHeightForWidth** ().
        """
        ...
    def hasWidthForHeight(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#hasWidthForHeight

        **bool QSizePolicy::hasWidthForHeight() const**

        Returns `true` if the widget's width depends on its height; otherwise
        returns `false`.

        **See also** **setWidthForHeight** ().
        """
        ...
    def horizontalPolicy(self) -> PySide6.QtWidgets.QSizePolicy.Policy:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#horizontalPolicy

        **QSizePolicy::Policy QSizePolicy::horizontalPolicy() const**

        Returns the horizontal component of the size policy.

        **See also** **setHorizontalPolicy** (), **verticalPolicy** (), and
        **horizontalStretch** ().
        """
        ...
    def horizontalStretch(self) -> int:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#horizontalStretch

        **int QSizePolicy::horizontalStretch() const**

        Returns the horizontal stretch factor of the size policy.

        **See also** **setHorizontalStretch** (), **verticalStretch** (), and
        **horizontalPolicy** ().
        """
        ...
    def retainSizeWhenHidden(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#retainSizeWhenHidden

        **[since 5.2] bool QSizePolicy::retainSizeWhenHidden() const**

        Returns whether the layout should retain the widget's size when it is
        hidden. This is `false` by default.

        This function was introduced in Qt 5.2.

        **See also** **setRetainSizeWhenHidden** ().
        """
        ...
    def setControlType(self, type: PySide6.QtWidgets.QSizePolicy.ControlType) -> None:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#setControlType

        **void QSizePolicy::setControlType(QSizePolicy::ControlType type )**

        Sets the control type associated with the widget for which this size
        policy applies to **type**.

        The control type specifies the type of the widget for which this size
        policy applies. It is used by some styles, notably QMacStyle, to insert
        proper spacing between widgets. For example, the macOS Aqua guidelines
        specify that push buttons should be separated by 12 pixels, whereas
        vertically stacked radio buttons only require 6 pixels.

        **See also** **controlType** () and **QStyle::layoutSpacing** ().
        """
        ...
    def setHeightForWidth(self, b: bool) -> None:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#setHeightForWidth

        **void QSizePolicy::setHeightForWidth(bool dependent )**

        Sets the flag determining whether the widget's preferred height depends
        on its width, to **dependent**.

        **See also** **hasHeightForWidth** () and **setWidthForHeight** ().
        """
        ...
    def setHorizontalPolicy(self, d: PySide6.QtWidgets.QSizePolicy.Policy) -> None:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#setHorizontalPolicy

        **void QSizePolicy::setHorizontalPolicy(QSizePolicy::Policy policy )**

        Sets the horizontal component to the given **policy**.

        **See also** **horizontalPolicy** (), **setVerticalPolicy** (), and
        **setHorizontalStretch** ().
        """
        ...
    def setHorizontalStretch(self, stretchFactor: int) -> None:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#setHorizontalStretch

        **void QSizePolicy::setHorizontalStretch(int stretchFactor )**

        Sets the horizontal stretch factor of the size policy to the given
        **stretchFactor**. **stretchFactor** must be in the range [0,255].

        When two widgets are adjacent to each other in a horizontal layout,
        setting the horizontal stretch factor of the widget on the left to 2 and
        the factor of widget on the right to 1 will ensure that the widget on
        the left will always be twice the size of the one on the right.

        **See also** **horizontalStretch** (), **setVerticalStretch** (), and
        **setHorizontalPolicy** ().
        """
        ...
    def setRetainSizeWhenHidden(self, retainSize: bool) -> None:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#setRetainSizeWhenHidden

        **[since 5.2] void QSizePolicy::setRetainSizeWhenHidden(bool retainSize
        )**

        Sets whether a layout should retain the widget's size when it is hidden.
        If **retainSize** is `true`, the layout will not be changed by hiding
        the widget.

        This function was introduced in Qt 5.2.

        **See also** **retainSizeWhenHidden** ().
        """
        ...
    def setVerticalPolicy(self, d: PySide6.QtWidgets.QSizePolicy.Policy) -> None:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#setVerticalPolicy

        **void QSizePolicy::setVerticalPolicy(QSizePolicy::Policy policy )**

        Sets the vertical component to the given **policy**.

        **See also** **verticalPolicy** (), **setHorizontalPolicy** (), and
        **setVerticalStretch** ().
        """
        ...
    def setVerticalStretch(self, stretchFactor: int) -> None:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#setVerticalStretch

        **void QSizePolicy::setVerticalStretch(int stretchFactor )**

        Sets the vertical stretch factor of the size policy to the given
        **stretchFactor**. **stretchFactor** must be in the range [0,255].

        When two widgets are adjacent to each other in a vertical layout,
        setting the vertical stretch factor of the widget on the top to 2 and
        the factor of widget on the bottom to 1 will ensure that the widget on
        the top will always be twice the size of the one on the bottom.

        **See also** **verticalStretch** (), **setHorizontalStretch** (), and
        **setVerticalPolicy** ().
        """
        ...
    def setWidthForHeight(self, b: bool) -> None:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#setWidthForHeight

        **void QSizePolicy::setWidthForHeight(bool dependent )**

        Sets the flag determining whether the widget's width depends on its
        height, to **dependent**.

        This is only supported for **QGraphicsLayout** 's subclasses. It is not
        possible to have a layout with both height-for-width and width-for-
        height constraints at the same time.

        **See also** **hasWidthForHeight** () and **setHeightForWidth** ().
        """
        ...
    def transpose(self) -> None:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#transpose

        **void QSizePolicy::transpose()**

        Swaps the horizontal and vertical policies and stretches.

        **See also** **transposed** ().
        """
        ...
    def transposed(self) -> PySide6.QtWidgets.QSizePolicy:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#transposed

        **[since 5.9] QSizePolicy QSizePolicy::transposed() const**

        Returns a size policy object with the horizontal and vertical policies
        and stretches swapped.

        This function was introduced in Qt 5.9.

        **See also** **transpose** ().
        """
        ...
    def verticalPolicy(self) -> PySide6.QtWidgets.QSizePolicy.Policy:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#verticalPolicy

        **QSizePolicy::Policy QSizePolicy::verticalPolicy() const**

        Returns the vertical component of the size policy.

        **See also** **setVerticalPolicy** (), **horizontalPolicy** (), and
        **verticalStretch** ().
        """
        ...
    def verticalStretch(self) -> int:
        """
        https://doc.qt.io/qt-6/qsizepolicy.html#verticalStretch

        **int QSizePolicy::verticalStretch() const**

        Returns the vertical stretch factor of the size policy.

        **See also** **setVerticalStretch** (), **horizontalStretch** (), and
        **verticalPolicy** ().
        """
        ...
