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
from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QScroller(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qscroller.html

    **Detailed Description**

    With kinetic scrolling, the user can push the widget in a given direction
    and it will continue to scroll in this direction until it is stopped either
    by the user or by friction. Aspects of inertia, friction and other physical
    concepts can be changed in order to fine-tune an intuitive user experience.

    The QScroller object is the object that stores the current position and
    scrolling speed and takes care of updates. QScroller can be triggered by a
    flick gesture

    **QWidget**  *w = ...;
            QScroller::grabGesture(w,
    QScroller::LeftMouseButtonGesture);

    or directly like this:

    **QWidget**  *w = ...;
            QScroller *scroller = QScroller::scroller(w);
    scroller->scrollTo(**QPointF** (100, 100));

    The scrolled QObjects receive a **QScrollPrepareEvent**  whenever the
    scroller needs to update its geometry information and a **QScrollEvent**
    whenever the content of the object should actually be scrolled.

    The scroller uses the global **QAbstractAnimation**  timer to generate its
    QScrollEvents. This can be changed with **QScrollerProperties::FrameRate**
    on a per-QScroller basis.

    The **Dir View Example**  shows one way to use a QScroller with a
    **QTreeView** . An example in the `scroller` examples directory also
    demonstrates QScroller.

    Even though this kinetic scroller has a large number of settings available
    via **QScrollerProperties** , we recommend that you leave them all at their
    default, platform optimized values. Before changing them you can experiment
    with the `plot` example in the `scroller` examples directory.

    **See also** **QScrollEvent** , **QScrollPrepareEvent** , and
    **QScrollerProperties** .
    """

    InputPress: QScroller.Input = ...
    InputMove: QScroller.Input = ...
    InputRelease: QScroller.Input = ...
    TouchGesture: QScroller.ScrollerGestureType = ...
    LeftMouseButtonGesture: QScroller.ScrollerGestureType = ...
    RightMouseButtonGesture: QScroller.ScrollerGestureType = ...
    MiddleMouseButtonGesture: QScroller.ScrollerGestureType = ...
    Inactive: QScroller.State = ...
    Pressed: QScroller.State = ...
    Dragging: QScroller.State = ...
    Scrolling: QScroller.State = ...

    class Input(IntFlag):
        InputPress: QScroller.Input = ...
        InputMove: QScroller.Input = ...
        InputRelease: QScroller.Input = ...

    class ScrollerGestureType(IntFlag):
        TouchGesture: QScroller.ScrollerGestureType = ...
        LeftMouseButtonGesture: QScroller.ScrollerGestureType = ...
        RightMouseButtonGesture: QScroller.ScrollerGestureType = ...
        MiddleMouseButtonGesture: QScroller.ScrollerGestureType = ...

    class State(IntFlag):
        Inactive: QScroller.State = ...
        Pressed: QScroller.State = ...
        Dragging: QScroller.State = ...
        Scrolling: QScroller.State = ...
    @staticmethod
    def activeScrollers() -> list[PySide6.QtWidgets.QScroller]:
        """
        https://doc.qt.io/qt-6/qscroller.html#activeScrollers

        **[static] QList<QScroller *> QScroller::activeScrollers()**

        Returns an application wide list of currently active **QScroller**
        objects. Active **QScroller**  objects are in a **state** () that is not
        **QScroller::Inactive** . This function is useful when writing your own
        gesture recognizer.
        """
        ...
    @overload
    def ensureVisible(
        self,
        rect: PySide6.QtCore.QRectF | PySide6.QtCore.QRect,
        xmargin: float,
        ymargin: float,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qscroller.html#ensureVisible

        **[slot] void QScroller::ensureVisible(const QRectF & rect , qreal
        xmargin , qreal ymargin )**

        Starts scrolling so that the rectangle **rect** is visible inside the
        viewport with additional margins specified in pixels by **xmargin** and
        **ymargin** around the rect.

        In cases where it is not possible to fit the rect plus margins inside
        the viewport the contents are scrolled so that as much as possible is
        visible from **rect**.

        The scrolling speed is calculated so that the given position is reached
        after a platform-defined time span.

        This function performs the actual scrolling by calling **scrollTo** ().

        **See also** **scrollTo** ().
        """
        ...
    @overload
    def ensureVisible(
        self,
        rect: PySide6.QtCore.QRectF | PySide6.QtCore.QRect,
        xmargin: float,
        ymargin: float,
        scrollTime: int,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qscroller.html#ensureVisible-1

        **[slot] void QScroller::ensureVisible(const QRectF & rect , qreal
        xmargin , qreal ymargin , int scrollTime )**

        This is an overloaded function.

        This version will reach its destination position in **scrollTime**
        milliseconds.
        """
        ...
    def finalPosition(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qscroller.html#finalPosition

        **QPointF QScroller::finalPosition() const**

        Returns the estimated final position for the current scroll movement.
        Returns the current position if the scroller state is not Scrolling. The
        result is undefined when the scroller state is Inactive.

        The target position is in pixel.

        **See also** **pixelPerMeter** () and **scrollTo** ().
        """
        ...
    @staticmethod
    def grabGesture(
        target: PySide6.QtCore.QObject,
        gestureType: PySide6.QtWidgets.QScroller.ScrollerGestureType = ...,
    ) -> PySide6.QtCore.Qt.GestureType:
        """
        https://doc.qt.io/qt-6/qscroller.html#grabGesture

        **[static] Qt::GestureType QScroller::grabGesture(QObject * target ,
        QScroller::ScrollerGestureType scrollGestureType = TouchGesture)**

        Registers a custom scroll gesture recognizer, grabs it for the
        **target** and returns the resulting gesture type. If
        **scrollGestureType** is set to **TouchGesture**  the gesture triggers
        on touch events. If it is set to one of **LeftMouseButtonGesture** ,
        **RightMouseButtonGesture**  or **MiddleMouseButtonGesture**  it
        triggers on mouse events of the corresponding button.

        Only one scroll gesture can be active on a single object at the same
        time. If you call this function twice on the same object, it will ungrab
        the existing gesture before grabbing the new one.

        **Note:** To avoid unwanted side-effects, mouse events are consumed
        while the gesture is triggered. Since the initial mouse press event is
        not consumed, the gesture sends a fake mouse release event at the global
        position `(INT_MIN, INT_MIN)`. This ensures that internal states of the
        widget that received the original mouse press are consistent.

        **See also** **ungrabGesture** () and **grabbedGesture** ().
        """
        ...
    @staticmethod
    def grabbedGesture(target: PySide6.QtCore.QObject) -> PySide6.QtCore.Qt.GestureType:
        """
        https://doc.qt.io/qt-6/qscroller.html#grabbedGesture

        **[static] Qt::GestureType QScroller::grabbedGesture(QObject * target
        )**

        Returns the gesture type currently grabbed for the **target** or 0 if no
        gesture is grabbed.

        **See also** **grabGesture** () and **ungrabGesture** ().
        """
        ...
    def handleInput(
        self,
        input: PySide6.QtWidgets.QScroller.Input,
        position: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        timestamp: int = ...,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qscroller.html#handleInput

        **bool QScroller::handleInput(QScroller::Input input , const QPointF &
        position , qint64 timestamp = 0)**

        This function is used by gesture recognizers to inform the scroller
        about a new input event. The scroller changes its internal **state** ()
        according to the input event and its attached scroller properties. The
        scroller doesn't distinguish between the kind of input device the event
        came from. Therefore the event needs to be split into the **input**
        type, a **position** and a milli-second **timestamp**. The **position**
        needs to be in the target's coordinate system.

        The return value is `true` if the event should be consumed by the
        calling filter or `false` if the event should be forwarded to the
        control.

        **Note:** Using **grabGesture** () should be sufficient for most use
        cases.
        """
        ...
    @staticmethod
    def hasScroller(target: PySide6.QtCore.QObject) -> bool:
        """
        https://doc.qt.io/qt-6/qscroller.html#hasScroller

        **[static] bool QScroller::hasScroller(QObject * target )**

        Returns `true` if a **QScroller**  object was already created for
        **target** ; `false` otherwise.

        **See also** **scroller** ().
        """
        ...
    def pixelPerMeter(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qscroller.html#pixelPerMeter

        **QPointF QScroller::pixelPerMeter() const**

        Returns the pixel per meter metric for the scrolled widget.

        The value is reported for both the x and y axis separately by using a
        **QPointF** .

        **Note:** Please note that this value should be physically correct. The
        actual DPI settings that Qt returns for the display may be reported
        wrongly on purpose by the underlying windowing system, for example on
        macOS.
        """
        ...
    def resendPrepareEvent(self) -> None:
        """
        https://doc.qt.io/qt-6/qscroller.html#resendPrepareEvent

        **[slot] void QScroller::resendPrepareEvent()**

        This function resends the **QScrollPrepareEvent** . Calling
        resendPrepareEvent triggers a **QScrollPrepareEvent**  from the
        scroller. This allows the receiver to re-set content position and
        content size while scrolling. Calling this function while in the
        Inactive state is useless as the prepare event is sent again before
        scrolling starts.
        """
        ...
    @overload
    def scrollTo(
        self,
        pos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qscroller.html#scrollTo

        **[slot] void QScroller::scrollTo(const QPointF & pos )**

        Starts scrolling the widget so that point **pos** is at the top-left
        position in the viewport.

        The behaviour when scrolling outside the valid scroll area is undefined.
        In this case the scroller might or might not overshoot.

        The scrolling speed will be calculated so that the given position will
        be reached after a platform-defined time span.

        **pos** is given in viewport coordinates.

        **See also** **ensureVisible** ().
        """
        ...
    @overload
    def scrollTo(
        self,
        pos: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        scrollTime: int,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qscroller.html#scrollTo-1

        **[slot] void QScroller::scrollTo(const QPointF & pos , int scrollTime
        )**

        This is an overloaded function.

        This version will reach its destination position in **scrollTime**
        milliseconds.
        """
        ...
    @staticmethod
    def scroller(target: PySide6.QtCore.QObject) -> PySide6.QtWidgets.QScroller:
        """
        https://doc.qt.io/qt-6/qscroller.html#scroller

        **[static] QScroller *QScroller::scroller(QObject * target )**

        Returns the scroller for the given **target**. As long as the object
        exists this function will always return the same **QScroller**
        instance. If no **QScroller**  exists for the **target** , one will
        implicitly be created. At no point more than one **QScroller**  will be
        active on an object.

        **See also** **hasScroller** () and **target** ().
        """
        ...
    def scrollerProperties(self) -> PySide6.QtWidgets.QScrollerProperties:
        """
        https://doc.qt.io/qt-6/qscroller.html#scrollerProperties-prop

        **scrollerProperties : QScrollerProperties**

        This property holds the scroller properties of this scroller. The
        properties are used by the **QScroller**  to determine its scrolling
        behavior.

        **Access functions:**

        QScrollerProperties **scrollerProperties** () const
        void
        **setScrollerProperties** (const QScrollerProperties & **prop** )

        **Notifier signal:**

        void ****scrollerPropertiesChanged** ** (const QScrollerProperties &
        **newProperties** )
        """
        ...
    def setScrollerProperties(self, prop: PySide6.QtWidgets.QScrollerProperties) -> None:
        """
        https://doc.qt.io/qt-6/qscroller.html#scrollerProperties-prop

        **scrollerProperties : QScrollerProperties**

        This property holds the scroller properties of this scroller. The
        properties are used by the **QScroller**  to determine its scrolling
        behavior.

        **Access functions:**

        QScrollerProperties **scrollerProperties** () const
        void
        **setScrollerProperties** (const QScrollerProperties & **prop** )

        **Notifier signal:**

        void ****scrollerPropertiesChanged** ** (const QScrollerProperties &
        **newProperties** )
        """
        ...
    @overload
    def setSnapPositionsX(self, first: float, interval: float) -> None:
        """
        https://doc.qt.io/qt-6/qscroller.html#setSnapPositionsX

        **void QScroller::setSnapPositionsX(const QList<qreal> & positions )**

        Set the snap positions for the horizontal axis to a list of
        **positions**. This overwrites all previously set snap positions and
        also a previously set snapping interval. Snapping can be deactivated by
        setting an empty list of positions.
        """
        ...
    @overload
    def setSnapPositionsX(self, positions: Sequence[float]) -> None:
        """
        https://doc.qt.io/qt-6/qscroller.html#setSnapPositionsX-1

        **void QScroller::setSnapPositionsX(qreal first , qreal interval )**

        Set the snap positions for the horizontal axis to regular spaced
        intervals. The first snap position is at **first**. The next at
        **first** \\+ **interval**. This can be used to implement a list header.
        This overwrites all previously set snap positions and also a previously
        set snapping interval. Snapping can be deactivated by setting an
        interval of 0.0
        """
        ...
    @overload
    def setSnapPositionsY(self, first: float, interval: float) -> None:
        """
        https://doc.qt.io/qt-6/qscroller.html#setSnapPositionsY

        **void QScroller::setSnapPositionsY(const QList<qreal> & positions )**

        Set the snap positions for the vertical axis to a list of **positions**.
        This overwrites all previously set snap positions and also a previously
        set snapping interval. Snapping can be deactivated by setting an empty
        list of positions.
        """
        ...
    @overload
    def setSnapPositionsY(self, positions: Sequence[float]) -> None:
        """
        https://doc.qt.io/qt-6/qscroller.html#setSnapPositionsY-1

        **void QScroller::setSnapPositionsY(qreal first , qreal interval )**

        Set the snap positions for the vertical axis to regular spaced
        intervals. The first snap position is at **first**. The next at
        **first** \\+ **interval**. This overwrites all previously set snap
        positions and also a previously set snapping interval. Snapping can be
        deactivated by setting an interval of 0.0
        """
        ...
    def state(self) -> PySide6.QtWidgets.QScroller.State:
        """
        https://doc.qt.io/qt-6/qscroller.html#state-prop

        **[read-only] state : const State**

        This property holds the state of the scroller

        **Access functions:**

        QScroller::State **state** () const

        **Notifier signal:**

        void ****stateChanged** ** (QScroller::State **newState** )

        **See also** **QScroller::State** .

        **Member Function Documentation**
        """
        ...
    def stop(self) -> None:
        """
        https://doc.qt.io/qt-6/qscroller.html#stop

        **void QScroller::stop()**

        Stops the scroller and resets its state back to Inactive.
        """
        ...
    def target(self) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qscroller.html#target

        **QObject *QScroller::target() const**

        Returns the target object of this scroller.

        **See also** **hasScroller** () and **scroller** ().
        """
        ...
    @staticmethod
    def ungrabGesture(target: PySide6.QtCore.QObject) -> None:
        """
        https://doc.qt.io/qt-6/qscroller.html#ungrabGesture

        **[static] void QScroller::ungrabGesture(QObject * target )**

        Ungrabs the gesture for the **target**. Does nothing if no gesture is
        grabbed.

        **See also** **grabGesture** () and **grabbedGesture** ().
        """
        ...
    def velocity(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qscroller.html#velocity

        **QPointF QScroller::velocity() const**

        Returns the current scrolling velocity in meter per second when the
        state is Scrolling or Dragging. Returns a zero velocity otherwise.

        The velocity is reported for both the x and y axis separately by using a
        **QPointF** .

        **See also** **pixelPerMeter** ().
        """
        ...
    @property
    def scrollerPropertiesChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qscroller.html#scrollerPropertiesChanged

        **[signal] void QScroller::scrollerPropertiesChanged(const
        QScrollerProperties & newProperties )**

        **QScroller**  emits this signal whenever its scroller properties
        change. **newProperties** are the new scroller properties.

        **Note:** Notifier signal for property **scrollerProperties** .

        **See also** **scrollerProperties** .
        """
        ...
    @property
    def stateChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qscroller.html#stateChanged

        **[signal] void QScroller::stateChanged(QScroller::State newState )**

        **QScroller**  emits this signal whenever the state changes.
        **newState** is the new State.

        **Note:** Notifier signal for property **state** .

        **See also** **state** .
        """
        ...
