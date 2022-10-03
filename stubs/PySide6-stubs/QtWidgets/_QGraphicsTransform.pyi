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

class QGraphicsTransform(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qgraphicstransform.html

    **Detailed Description**

    As an alternative to **QGraphicsItem::transform** , QGraphicsTransform lets
    you create and control advanced transformations that can be configured
    independently using specialized properties.

    **QGraphicsItem**  allows you to assign any number of QGraphicsTransform
    instances to one **QGraphicsItem** . Each QGraphicsTransform is applied in
    order, one at a time, to the **QGraphicsItem**  it's assigned to.

    QGraphicsTransform is particularly useful for animations. Whereas
    **QGraphicsItem::setTransform** () lets you assign any transform directly to
    an item, there is no direct way to interpolate between two different
    transformations (e.g., when transitioning between two states, each for which
    the item has a different arbitrary transform assigned). Using
    QGraphicsTransform you can interpolate the property values of each
    independent transformation. The resulting operation is then combined into a
    single transform which is applied to **QGraphicsItem** .

    Transformations are computed in true 3D space using **QMatrix4x4** . When
    the transformation is applied to a **QGraphicsItem** , it will be projected
    back to a 2D **QTransform** . When multiple QGraphicsTransform objects are
    applied to a **QGraphicsItem** , all of the transformations are computed in
    true 3D space, with the projection back to 2D only occurring after the last
    QGraphicsTransform is applied. The exception to this is
    **QGraphicsRotation** , which projects back to 2D after each rotation to
    preserve the perspective effect around the X and Y axes.

    If you want to create your own configurable transformation, you can create a
    subclass of QGraphicsTransform (or any or the existing subclasses), and
    reimplement the pure virtual **applyTo** () function, which takes a pointer
    to a **QMatrix4x4** . Each operation you would like to apply should be
    exposed as properties (e.g., customTransform->setVerticalShear(2.5)). Inside
    you reimplementation of **applyTo** (), you can modify the provided
    transform respectively.

    QGraphicsTransform can be used together with **QGraphicsItem::setTransform**
    (), **QGraphicsItem::setRotation** (), and **QGraphicsItem::setScale** ().

    **See also** **QGraphicsItem::transform** (), **QGraphicsScale** , and
    **QGraphicsRotation** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicstransform.html#QGraphicsTransform

        **QGraphicsTransform::QGraphicsTransform(QObject * parent = nullptr)**

        Constructs a new QGraphicsTransform with the given **parent**.
        """
        ...
    def applyTo(
        self, matrix: PySide6.QtGui.QMatrix4x4 | PySide6.QtGui.QTransform
    ) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicstransform.html#applyTo

        **[pure virtual] void QGraphicsTransform::applyTo(QMatrix4x4 * matrix )
        const**

        This pure virtual method has to be reimplemented in derived classes.

        It applies this transformation to **matrix**.

        **See also** **QGraphicsItem::transform** () and
        **QMatrix4x4::toTransform** ().
        """
        ...
    def update(self) -> None:
        """
        https://doc.qt.io/qt-6/qgraphicstransform.html#update

        **[protected slot] void QGraphicsTransform::update()**

        Notifies that this transform operation has changed its parameters in
        such a way that **applyTo** () will return a different result than
        before.

        When implementing you own custom graphics transform, you must call this
        function every time you change a parameter, to let **QGraphicsItem**
        know that its transformation needs to be updated.

        **See also** **applyTo** ().
        """
        ...