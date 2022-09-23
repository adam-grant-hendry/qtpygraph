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
PySide6.QtQuick, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtOpenGL
import PySide6.QtQml
import PySide6.QtQuick

class QSGClipNode(PySide6.QtQuick.QSGBasicGeometryNode):
    """
    https://doc.qt.io/qt-6/qsgclipnode.html

    **Detailed Description**

    Clipping applies to the node's subtree and can be nested. Multiple clip
    nodes will be accumulated by intersecting all their geometries. The
    accumulation happens as part of the rendering.

    Clip nodes must have a geometry before they can be added to the scene graph.

    Clipping is usually implemented by using the stencil buffer.

    **Note:** All classes with QSG prefix should be used solely on the scene
    graph's rendering thread. See **Scene Graph and Rendering**  for more
    information.
    """

    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qsgclipnode.html#QSGClipNode

        **QSGClipNode::QSGClipNode()**

        Creates a new QSGClipNode without a geometry.

        The clip node must have a geometry before it can be added to the scene
        graph.
        """
        ...
    def clipRect(self) -> PySide6.QtCore.QRectF:
        """
        https://doc.qt.io/qt-6/qsgclipnode.html#clipRect

        **QRectF QSGClipNode::clipRect() const**

        Returns the clip rect of this node.

        **See also** **setClipRect** ().
        """
        ...
    def isRectangular(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsgclipnode.html#isRectangular

        **bool QSGClipNode::isRectangular() const**

        Returns if this clip node has a rectangular clip.

        **See also** **setIsRectangular** ().
        """
        ...
    def setClipRect(self, arg__1: PySide6.QtCore.QRectF | PySide6.QtCore.QRect) -> None:
        """
        https://doc.qt.io/qt-6/qsgclipnode.html#setClipRect

        **void QSGClipNode::setClipRect(const QRectF & rect )**

        Sets the clip rect of this clip node to **rect**.

        When a rectangular clip is set in combination with **setIsRectangular**
        the renderer may in some cases use a more optimal clip method.

        **See also** **clipRect** ().
        """
        ...
    def setIsRectangular(self, rectHint: bool) -> None:
        """
        https://doc.qt.io/qt-6/qsgclipnode.html#setIsRectangular

        **void QSGClipNode::setIsRectangular(bool rectHint )**

        Sets whether this clip node has a rectangular clip to **rectHint**.

        This is an optimization hint which means that the renderer can use
        scissoring instead of stencil, which is significantly faster.

        When this hint is set and it is applicable, the clip region will be
        generated from **clipRect** () rather than **geometry** ().

        By default this property is `false`.

        **See also** **isRectangular** ().
        """
        ...
