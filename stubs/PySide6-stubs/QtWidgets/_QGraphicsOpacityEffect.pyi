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

class QGraphicsOpacityEffect(PySide6.QtWidgets.QGraphicsEffect):
    """
    https://doc.qt.io/qt-6/qgraphicsopacityeffect.html

    **Detailed Description**

    An opacity effect renders the source with an opacity. This effect is useful
    for making the source semi-transparent, similar to a fade-in/fade-out
    sequence. The opacity can be modified using the **setOpacity** () function.

    By default, the opacity is 0.7.

    ![](images/graphicseffect-opacity.png)

    **See also** **QGraphicsDropShadowEffect** , **QGraphicsBlurEffect** , and
    **QGraphicsColorizeEffect** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#QGraphicsOpacityEffec
        t

        **QGraphicsOpacityEffect::QGraphicsOpacityEffect(QObject * parent =
        nullptr)**

        Constructs a new QGraphicsOpacityEffect instance. The **parent**
        parameter is passed to **QGraphicsEffect** 's constructor.
        """
        ...
    def draw(self, painter: PySide6.QtGui.QPainter) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#draw

        **[override virtual protected] void
        QGraphicsOpacityEffect::draw(QPainter * painter )**

        Reimplements: **QGraphicsEffect::draw** (QPainter *painter).
        """
        ...
    def opacity(self) -> float:
        """
        https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#opacity-prop

        **opacity : qreal**

        This property holds the opacity of the effect.

        The value should be in the range of 0.0 to 1.0, where 0.0 is fully
        transparent and 1.0 is fully opaque.

        By default, the opacity is 0.7.

        **Access functions:**

        qreal **opacity** () const
        void **setOpacity** (qreal **opacity** )

        **Notifier signal:**

        void ****opacityChanged** ** (qreal **opacity** )

        **See also** **setOpacityMask** ().
        """
        ...
    def opacityMask(self) -> PySide6.QtGui.QBrush:
        """
        https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#opacityMask-prop

        **opacityMask : QBrush**

        This property holds the opacity mask of the effect.

        An opacity mask allows you apply opacity to portions of an element.

        For example:

        ...
            **QLinearGradient**  alphaGradient(rect.topLeft(),
        rect.bottomLeft());
            alphaGradient.setColorAt(0.0, Qt::transparent);
        alphaGradient.setColorAt(0.5, Qt::black);
        alphaGradient.setColorAt(1.0, Qt::transparent);
        **QGraphicsOpacityEffect**  *effect = new **QGraphicsOpacityEffect** ;
        effect->setOpacityMask(alphaGradient);
            ...

        There is no opacity mask by default.

        **Access functions:**

        QBrush **opacityMask** () const
        void **setOpacityMask** (const QBrush
        & **mask** )

        **Notifier signal:**

        void ****opacityMaskChanged** ** (const QBrush & **mask** )

        **See also** **setOpacity** ().

        **Member Function Documentation**
        """
        ...
    def setOpacity(self, opacity: float) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#opacity-prop

        **opacity : qreal**

        This property holds the opacity of the effect.

        The value should be in the range of 0.0 to 1.0, where 0.0 is fully
        transparent and 1.0 is fully opaque.

        By default, the opacity is 0.7.

        **Access functions:**

        qreal **opacity** () const
        void **setOpacity** (qreal **opacity** )

        **Notifier signal:**

        void ****opacityChanged** ** (qreal **opacity** )

        **See also** **setOpacityMask** ().
        """
        ...
    def setOpacityMask(
        self,
        mask: (
            PySide6.QtGui.QBrush
            | PySide6.QtCore.Qt.BrushStyle
            | PySide6.QtCore.Qt.GlobalColor
            | PySide6.QtGui.QColor
            | PySide6.QtGui.QGradient
            | PySide6.QtGui.QImage
            | PySide6.QtGui.QPixmap
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#opacityMask-prop

        **opacityMask : QBrush**

        This property holds the opacity mask of the effect.

        An opacity mask allows you apply opacity to portions of an element.

        For example:

        ...
            **QLinearGradient**  alphaGradient(rect.topLeft(),
        rect.bottomLeft());
            alphaGradient.setColorAt(0.0, Qt::transparent);
        alphaGradient.setColorAt(0.5, Qt::black);
        alphaGradient.setColorAt(1.0, Qt::transparent);
        **QGraphicsOpacityEffect**  *effect = new **QGraphicsOpacityEffect** ;
        effect->setOpacityMask(alphaGradient);
            ...

        There is no opacity mask by default.

        **Access functions:**

        QBrush **opacityMask** () const
        void **setOpacityMask** (const QBrush
        & **mask** )

        **Notifier signal:**

        void ****opacityMaskChanged** ** (const QBrush & **mask** )

        **See also** **setOpacity** ().

        **Member Function Documentation**
        """
        ...
    @property
    def opacityChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#opacityChanged

        **[signal] void QGraphicsOpacityEffect::opacityChanged(qreal opacity )**

        This signal is emitted whenever the effect's opacity changes. The
        **opacity** parameter holds the effect's new opacity.

        **Note:** Notifier signal for property **opacity** .
        """
        ...
    @property
    def opacityMaskChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#opacityMaskChanged

        **[signal] void QGraphicsOpacityEffect::opacityMaskChanged(const QBrush
        & mask )**

        This signal is emitted whenever the effect's opacity mask changes. The
        **mask** parameter holds the effect's new opacity mask.

        **Note:** Notifier signal for property **opacityMask** .
        """
        ...