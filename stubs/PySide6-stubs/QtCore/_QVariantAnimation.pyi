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

from collections.abc import Sequence
from typing import Any

import PySide6.QtCore

class QVariantAnimation(PySide6.QtCore.QAbstractAnimation):
    """
    https://doc.qt.io/qt-6/qvariantanimation.html

    **Detailed Description**

    This class is part of **The Animation Framework** . It serves as a base
    class for property and item animations, with functions for shared
    functionality.

    The class performs interpolation over **QVariant** s, but leaves using the
    interpolated values to its subclasses. Currently, Qt provides
    **QPropertyAnimation** , which animates Qt **properties** . See the
    **QPropertyAnimation**  class description if you wish to animate such
    properties.

    You can then set start and end values for the property by calling
    **setStartValue** () and **setEndValue** (), and finally call **start** ()
    to start the animation. QVariantAnimation will interpolate the property of
    the target object and emit **valueChanged** (). To react to a change in the
    current value you have to reimplement the **updateCurrentValue** () virtual
    function or connect to said signal.

    It is also possible to set values at specified steps situated between the
    start and end value. The interpolation will then touch these points at the
    specified steps. Note that the start and end values are defined as the key
    values at 0.0 and 1.0.

    There are two ways to affect how QVariantAnimation interpolates the values.
    You can set an easing curve by calling **setEasingCurve** (), and configure
    the duration by calling **setDuration** (). You can change how the
    **QVariant** s are interpolated by creating a subclass of QVariantAnimation,
    and reimplementing the virtual **interpolated** () function.

    Subclassing QVariantAnimation can be an alternative if you have **QVariant**
    s that you do not wish to declare as Qt properties. Note, however, that you
    in most cases will be better off declaring your **QVariant**  as a property.

    Not all **QVariant**  types are supported. Below is a list of currently
    supported **QVariant**  types:

    * **Int**
      * **UInt**
      * **Double**
      * **Float**
      * **QLine**
      *
    **QLineF**
      * **QPoint**
      * **QPointF**
      * **QSize**
      * **QSizeF**
    * **QRect**
      * **QRectF**
      * **QColor**

    If you need to interpolate other variant types, including custom types, you
    have to implement interpolation for these yourself. To do this, you can
    register an interpolator function for a given type. This function takes 3
    parameters: the start value, the end value, and the current progress.

    Example:

    **QVariant**  myColorInterpolator(const **QColor**  &start, const **QColor**
    &end, **qreal**  progress)
            {
                ...
                return
    **QColor** (...);
            }
            ...
    **qRegisterAnimationInterpolator** <**QColor** >(myColorInterpolator);

    Another option is to reimplement **interpolated** (), which returns
    interpolation values for the value being interpolated.

    **See also** **QPropertyAnimation** , **QAbstractAnimation** , and **The
    Animation Framework** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#QVariantAnimation

        **QVariantAnimation::QVariantAnimation(QObject * parent = nullptr)**

        Construct a QVariantAnimation object. **parent** is passed to
        **QAbstractAnimation** 's constructor.
        """
        ...
    def currentValue(self) -> Any:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#currentValue-prop

        **[read-only] currentValue : const QVariant**

        This property holds the current value of the animation.

        This property describes the current value; an interpolated value between
        the **start value**  and the **end value** , using the current time for
        progress. The value itself is obtained from **interpolated** (), which
        is called repeatedly as the animation is running.

        **QVariantAnimation**  calls the virtual **updateCurrentValue** ()
        function when the current value changes. This is particularly useful for
        subclasses that need to track updates. For example,
        **QPropertyAnimation**  uses this function to animate Qt **properties**
        .

        **Access functions:**

        QVariant **currentValue** () const

        **Notifier signal:**

        void ****valueChanged** ** (const QVariant & **value** )

        **See also** **startValue**  and **endValue** .
        """
        ...
    def duration(self) -> int:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#duration-prop

        **[bindable] duration : int**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the duration of the animation

        This property describes the duration in milliseconds of the animation.
        The default duration is 250 milliseconds.

        **See also** **QAbstractAnimation::duration** ().
        """
        ...
    def easingCurve(self) -> PySide6.QtCore.QEasingCurve:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#easingCurve-prop

        **[bindable] easingCurve : QEasingCurve**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the easing curve of the animation

        This property defines the easing curve of the animation. By default, a
        linear easing curve is used, resulting in linear interpolation. Other
        curves are provided, for instance, **QEasingCurve::InCirc** , which
        provides a circular entry curve. Another example is
        **QEasingCurve::InOutElastic** , which provides an elastic effect on the
        values of the interpolated variant.

        **QVariantAnimation**  will use the **QEasingCurve::valueForProgress**
        () to transform the "normalized progress" (currentTime / totalDuration)
        of the animation into the effective progress actually used by the
        animation. It is this effective progress that will be the progress when
        **interpolated** () is called. Also, the steps in the **keyValues**  are
        referring to this effective progress.

        The easing curve is used with the interpolator, the **interpolated** ()
        virtual function, and the animation's duration to control how the
        current value changes as the animation progresses.
        """
        ...
    def endValue(self) -> Any:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#endValue-prop

        **endValue : QVariant**

        This property holds the end value of the animation

        This property describes the end value of the animation.

        **Access functions:**

        QVariant **endValue** () const
        void **setEndValue** (const QVariant &
        **value** )

        **See also** **startValue** .
        """
        ...
    def event(self, event: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#event

        **[override virtual protected] bool QVariantAnimation::event(QEvent *
        event )**

        Reimplements: **QAbstractAnimation::event** (QEvent *event).
        """
        ...
    def interpolated(self, from_: Any, to: Any, progress: float) -> Any:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#interpolated

        **[virtual protected] QVariant QVariantAnimation::interpolated(const
        QVariant & from , const QVariant & to , qreal progress ) const**

        This virtual function returns the linear interpolation between variants
        **from** and **to** , at **progress** , usually a value between 0 and 1.
        You can reimplement this function in a subclass of **QVariantAnimation**
        to provide your own interpolation algorithm.

        Note that in order for the interpolation to work with a **QEasingCurve**
        that return a value smaller than 0 or larger than 1 (such as
        **QEasingCurve::InBack** ) you should make sure that it can extrapolate.
        If the semantic of the datatype does not allow extrapolation this
        function should handle that gracefully.

        You should call the **QVariantAnimation**  implementation of this
        function if you want your class to handle the types already supported by
        Qt (see class **QVariantAnimation**  description for a list of supported
        types).

        **See also** **QEasingCurve** .
        """
        ...
    def keyValueAt(self, step: float) -> Any:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#keyValueAt

        **QVariant QVariantAnimation::keyValueAt(qreal step ) const**

        Returns the key frame value for the given **step**. The given **step**
        must be in the range 0 to 1. If there is no **KeyValue**  for **step** ,
        it returns an invalid **QVariant** .

        **See also** **keyValues** () and **setKeyValueAt** ().
        """
        ...
    def keyValues(self) -> list[tuple[float, Any]]:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#keyValues

        **QVariantAnimation::KeyValues QVariantAnimation::keyValues() const**

        Returns the key frames of this animation.

        **See also** **keyValueAt** () and **setKeyValues** ().
        """
        ...
    def setDuration(self, msecs: int) -> None:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#duration-prop

        **[bindable] duration : int**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the duration of the animation

        This property describes the duration in milliseconds of the animation.
        The default duration is 250 milliseconds.

        **See also** **QAbstractAnimation::duration** ().
        """
        ...
    def setEasingCurve(
        self,
        easing: PySide6.QtCore.QEasingCurve | PySide6.QtCore.QEasingCurve.Type,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#easingCurve-prop

        **[bindable] easingCurve : QEasingCurve**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the easing curve of the animation

        This property defines the easing curve of the animation. By default, a
        linear easing curve is used, resulting in linear interpolation. Other
        curves are provided, for instance, **QEasingCurve::InCirc** , which
        provides a circular entry curve. Another example is
        **QEasingCurve::InOutElastic** , which provides an elastic effect on the
        values of the interpolated variant.

        **QVariantAnimation**  will use the **QEasingCurve::valueForProgress**
        () to transform the "normalized progress" (currentTime / totalDuration)
        of the animation into the effective progress actually used by the
        animation. It is this effective progress that will be the progress when
        **interpolated** () is called. Also, the steps in the **keyValues**  are
        referring to this effective progress.

        The easing curve is used with the interpolator, the **interpolated** ()
        virtual function, and the animation's duration to control how the
        current value changes as the animation progresses.
        """
        ...
    def setEndValue(self, value: Any) -> None:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#endValue-prop

        **endValue : QVariant**

        This property holds the end value of the animation

        This property describes the end value of the animation.

        **Access functions:**

        QVariant **endValue** () const
        void **setEndValue** (const QVariant &
        **value** )

        **See also** **startValue** .
        """
        ...
    def setKeyValueAt(self, step: float, value: Any) -> None:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#setKeyValueAt

        **void QVariantAnimation::setKeyValueAt(qreal step , const QVariant &
        value )**

        Creates a key frame at the given **step** with the given **value**. The
        given **step** must be in the range 0 to 1.

        **See also** **setKeyValues** () and **keyValueAt** ().
        """
        ...
    def setKeyValues(self, values: Sequence[tuple[float, Any]]) -> None:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#setKeyValues

        **void QVariantAnimation::setKeyValues(const
        QVariantAnimation::KeyValues & keyValues )**

        Replaces the current set of key frames with the given **keyValues**. the
        step of the key frames must be in the range 0 to 1.

        **See also** **keyValues** () and **keyValueAt** ().
        """
        ...
    def setStartValue(self, value: Any) -> None:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#startValue-prop

        **startValue : QVariant**

        This property holds the optional start value of the animation

        This property describes the optional start value of the animation. If
        omitted, or if a null **QVariant**  is assigned as the start value, the
        animation will use the current position of the end when the animation is
        started.

        **Access functions:**

        QVariant **startValue** () const
        void **setStartValue** (const
        QVariant & **value** )

        **See also** **endValue** .

        **Member Function Documentation**
        """
        ...
    def startValue(self) -> Any:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#startValue-prop

        **startValue : QVariant**

        This property holds the optional start value of the animation

        This property describes the optional start value of the animation. If
        omitted, or if a null **QVariant**  is assigned as the start value, the
        animation will use the current position of the end when the animation is
        started.

        **Access functions:**

        QVariant **startValue** () const
        void **setStartValue** (const
        QVariant & **value** )

        **See also** **endValue** .

        **Member Function Documentation**
        """
        ...
    def updateCurrentTime(self, arg__1: int) -> None:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#updateCurrentTime

        **[override virtual protected] void
        QVariantAnimation::updateCurrentTime(int)**

        Reimplements: **QAbstractAnimation::updateCurrentTime** (int
        currentTime).
        """
        ...
    def updateCurrentValue(self, value: Any) -> None:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#updateCurrentValue

        **[virtual protected] void QVariantAnimation::updateCurrentValue(const
        QVariant & value )**

        This virtual function is called every time the animation's current value
        changes. The **value** argument is the new current value.

        The base class implementation does nothing.

        **See also** **currentValue** .
        """
        ...
    def updateState(
        self,
        newState: PySide6.QtCore.QAbstractAnimation.State,
        oldState: PySide6.QtCore.QAbstractAnimation.State,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#updateState

        **[override virtual protected] void
        QVariantAnimation::updateState(QAbstractAnimation::State newState ,
        QAbstractAnimation::State oldState )**

        Reimplements: **QAbstractAnimation::updateState**
        (QAbstractAnimation::State newState, QAbstractAnimation::State
        oldState).
        """
        ...
    @property
    def valueChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qvariantanimation.html#valueChanged

        **[signal] void QVariantAnimation::valueChanged(const QVariant & value
        )**

        **QVariantAnimation**  emits this signal whenever the current **value**
        changes.

        **Note:** Notifier signal for property **currentValue** .

        **See also** **currentValue** , **startValue** , and **endValue** .
        """
        ...