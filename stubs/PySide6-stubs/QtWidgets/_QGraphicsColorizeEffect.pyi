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

from typing import Any

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QGraphicsColorizeEffect(PySide6.QtWidgets.QGraphicsEffect):
    """
    https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html

    **Detailed Description**

    A colorize effect renders the source with a tint of its **color** (). The
    color can be modified using the **setColor** () function.

    By default, the color is light blue (**QColor** (0, 0, 192)).

    ![](images/graphicseffect-colorize.png)

    **See also** **QGraphicsDropShadowEffect** , **QGraphicsBlurEffect** , and
    **QGraphicsOpacityEffect** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#QGraphicsColorizeEff
        ect

        **QGraphicsColorizeEffect::QGraphicsColorizeEffect(QObject * parent =
        nullptr)**

        Constructs a new QGraphicsColorizeEffect instance. The **parent**
        parameter is passed to **QGraphicsEffect** 's constructor.
        """
        ...
    def color(self) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#color-prop

        **color : QColor**

        This property holds the color of the effect.

        By default, the color is light blue (**QColor** (0, 0, 192)).

        **Access functions:**

        QColor **color** () const
        void **setColor** (const QColor & **c** )

        **Notifier signal:**

        void ****colorChanged** ** (const QColor & **color** )
        """
        ...
    def draw(self, painter: PySide6.QtGui.QPainter) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#draw

        **[override virtual protected] void
        QGraphicsColorizeEffect::draw(QPainter * painter )**

        Reimplements: **QGraphicsEffect::draw** (QPainter *painter).
        """
        ...
    def setColor(
        self,
        c: (
            PySide6.QtGui.QColor
            | PySide6.QtGui.QRgba64
            | Any
            | PySide6.QtCore.Qt.GlobalColor
            | str
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#color-prop

        **color : QColor**

        This property holds the color of the effect.

        By default, the color is light blue (**QColor** (0, 0, 192)).

        **Access functions:**

        QColor **color** () const
        void **setColor** (const QColor & **c** )

        **Notifier signal:**

        void ****colorChanged** ** (const QColor & **color** )
        """
        ...
    def setStrength(self, strength: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#strength-prop

        **strength : qreal**

        This property holds the strength of the effect.

        By default, the strength is 1.0. A strength 0.0 equals to no effect,
        while 1.0 means full colorization.

        **Access functions:**

        qreal **strength** () const
        void **setStrength** (qreal **strength** )

        **Notifier signal:**

        void ****strengthChanged** ** (qreal **strength** )

        **Member Function Documentation**
        """
        ...
    def strength(self) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#strength-prop

        **strength : qreal**

        This property holds the strength of the effect.

        By default, the strength is 1.0. A strength 0.0 equals to no effect,
        while 1.0 means full colorization.

        **Access functions:**

        qreal **strength** () const
        void **setStrength** (qreal **strength** )

        **Notifier signal:**

        void ****strengthChanged** ** (qreal **strength** )

        **Member Function Documentation**
        """
        ...
    @property
    def colorChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#colorChanged

        **[signal] void QGraphicsColorizeEffect::colorChanged(const QColor &
        color )**

        This signal is emitted whenever the effect's color changes. The
        **color** parameter holds the effect's new color.

        **Note:** Notifier signal for property **color** .
        """
        ...
    @property
    def strengthChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#strengthChanged

        **[signal] void QGraphicsColorizeEffect::strengthChanged(qreal strength
        )**

        This signal is emitted whenever **setStrength** () changes the colorize
        strength property. **strength** contains the new strength value of the
        colorize effect.

        **Note:** Notifier signal for property **strength** .
        """
        ...
