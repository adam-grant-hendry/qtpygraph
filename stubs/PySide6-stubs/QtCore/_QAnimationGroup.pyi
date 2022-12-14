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

import PySide6.QtCore

class QAnimationGroup(PySide6.QtCore.QAbstractAnimation):
    """
    https://doc.qt.io/qt-6/qanimationgroup.html

    **Detailed Description**

    An animation group is a container for animations (subclasses of
    **QAbstractAnimation** ). A group is usually responsible for managing the
    **state**  of its animations, i.e., it decides when to start, stop, resume,
    and pause them. Currently, Qt provides two such groups:
    **QParallelAnimationGroup**  and **QSequentialAnimationGroup** . Look up
    their class descriptions for details.

    Since QAnimationGroup inherits from **QAbstractAnimation** , you can combine
    groups, and easily construct complex animation graphs. You can query
    **QAbstractAnimation**  for the group it belongs to (using the **group** ()
    function).

    To start a top-level animation group, you simply use the **start** ()
    function from **QAbstractAnimation** . By a top-level animation group, we
    think of a group that itself is not contained within another group. Starting
    sub groups directly is not supported, and may lead to unexpected behavior.

    QAnimationGroup provides methods for adding and retrieving animations.
    Besides that, you can remove animations by calling **removeAnimation** (),
    and clear the animation group by calling **clear** (). You may keep track of
    changes in the group's animations by listening to **QEvent::ChildAdded**
    and **QEvent::ChildRemoved**  events.

    QAnimationGroup takes ownership of the animations it manages, and ensures
    that they are deleted when the animation group is deleted.

    **See also** **QAbstractAnimation** , **QVariantAnimation** , and **The
    Animation Framework** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qanimationgroup.html#QAnimationGroup

        **QAnimationGroup::QAnimationGroup(QObject * parent = nullptr)**

        Constructs a QAnimationGroup. **parent** is passed to **QObject** 's
        constructor.
        """
        ...
    def addAnimation(self, animation: PySide6.QtCore.QAbstractAnimation) -> None:
        """
        https://doc.qt.io/qt-6/qanimationgroup.html#addAnimation

        **void QAnimationGroup::addAnimation(QAbstractAnimation * animation )**

        Adds **animation** to this group. This will call **insertAnimation**
        with index equals to **animationCount** ().

        **Note:** The group takes ownership of the animation.

        **See also** **removeAnimation** ().
        """
        ...
    def animationAt(self, index: int) -> PySide6.QtCore.QAbstractAnimation:
        """
        https://doc.qt.io/qt-6/qanimationgroup.html#animationAt

        **QAbstractAnimation *QAnimationGroup::animationAt(int index ) const**

        Returns a pointer to the animation at **index** in this group. This
        function is useful when you need access to a particular animation.
        **index** is between 0 and **animationCount** () - 1.

        **See also** **animationCount** () and **indexOfAnimation** ().
        """
        ...
    def animationCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qanimationgroup.html#animationCount

        **int QAnimationGroup::animationCount() const**

        Returns the number of animations managed by this group.

        **See also** **indexOfAnimation** (), **addAnimation** (), and
        **animationAt** ().
        """
        ...
    def clear(self) -> None:
        """
        https://doc.qt.io/qt-6/qanimationgroup.html#clear

        **void QAnimationGroup::clear()**

        Removes and deletes all animations in this animation group, and resets
        the current time to 0.

        **See also** **addAnimation** () and **removeAnimation** ().
        """
        ...
    def event(self, event: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qanimationgroup.html#event

        **[override virtual protected] bool QAnimationGroup::event(QEvent *
        event )**

        Reimplements: **QAbstractAnimation::event** (QEvent *event).
        """
        ...
    def indexOfAnimation(self, animation: PySide6.QtCore.QAbstractAnimation) -> int:
        """
        https://doc.qt.io/qt-6/qanimationgroup.html#indexOfAnimation

        **int QAnimationGroup::indexOfAnimation(QAbstractAnimation * animation )
        const**

        Returns the index of **animation**. The returned index can be passed to
        the other functions that take an index as an argument.

        **See also** **insertAnimation** (), **animationAt** (), and
        **takeAnimation** ().
        """
        ...
    def insertAnimation(
        self, index: int, animation: PySide6.QtCore.QAbstractAnimation
    ) -> None:
        """
        https://doc.qt.io/qt-6/qanimationgroup.html#insertAnimation

        **void QAnimationGroup::insertAnimation(int index , QAbstractAnimation *
        animation )**

        Inserts **animation** into this animation group at **index**. If
        **index** is 0 the animation is inserted at the beginning. If **index**
        is **animationCount** (), the animation is inserted at the end.

        **Note:** The group takes ownership of the animation.

        **See also** **takeAnimation** (), **addAnimation** (),
        **indexOfAnimation** (), and **removeAnimation** ().
        """
        ...
    def removeAnimation(self, animation: PySide6.QtCore.QAbstractAnimation) -> None:
        """
        https://doc.qt.io/qt-6/qanimationgroup.html#removeAnimation

        **void QAnimationGroup::removeAnimation(QAbstractAnimation * animation
        )**

        Removes **animation** from this group. The ownership of **animation** is
        transferred to the caller.

        **See also** **takeAnimation** (), **insertAnimation** (), and
        **addAnimation** ().
        """
        ...
    def takeAnimation(self, index: int) -> PySide6.QtCore.QAbstractAnimation:
        """
        https://doc.qt.io/qt-6/qanimationgroup.html#takeAnimation

        **QAbstractAnimation *QAnimationGroup::takeAnimation(int index )**

        Returns the animation at **index** and removes it from the animation
        group.

        **Note:** The ownership of the animation is transferred to the caller.

        **See also** **removeAnimation** (), **addAnimation** (),
        **insertAnimation** (), and **indexOfAnimation** ().
        """
        ...
