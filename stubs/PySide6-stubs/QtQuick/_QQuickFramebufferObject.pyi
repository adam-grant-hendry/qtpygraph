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

class QQuickFramebufferObject(PySide6.QtQuick.QQuickItem):
    """
    https://doc.qt.io/qt-6/qquickframebufferobject.html

    **Detailed Description**

    **Warning:** This class is only functional when Qt Quick is rendering via
    OpenGL. It is not compatible with other graphics APIs, such as Vulkan or
    Metal. It should be treated as a legacy class that is only present in order
    to enable Qt 5 applications to function without source compatibility breaks
    as long as they tie themselves to OpenGL.

    On most platforms, the rendering will occur on a **dedicated thread** . For
    this reason, the QQuickFramebufferObject class enforces a strict separation
    between the item implementation and the FBO rendering. All item logic, such
    as properties and UI-related helper functions needed by QML should be
    located in a QQuickFramebufferObject class subclass. Everything that relates
    to rendering must be located in the **QQuickFramebufferObject::Renderer**
    class.

    To avoid race conditions and read/write issues from two threads it is
    important that the renderer and the item never read or write shared
    variables. Communication between the item and the renderer should primarily
    happen via the **QQuickFramebufferObject::Renderer::synchronize** ()
    function. This function will be called on the render thread while the GUI
    thread is blocked.

    Using queued connections or events for communication between item and
    renderer is also possible.

    Both the Renderer and the FBO are memory managed internally.

    To render into the FBO, the user should subclass the Renderer class and
    reimplement its **Renderer::render** () function. The Renderer subclass is
    returned from **createRenderer** ().

    The size of the FBO will by default adapt to the size of the item. If a
    fixed size is preferred, set **textureFollowsItemSize**  to `false` and
    return a texture of your choosing from
    **QQuickFramebufferObject::Renderer::createFramebufferObject** ().

    Starting Qt 5.4, the QQuickFramebufferObject class is a **texture provider**
    and can be used directly in **ShaderEffects**  and other classes that
    consume texture providers.

    **See also** **Scene Graph - Rendering FBOs**  and **Scene Graph and
    Rendering** .
    """

    class Renderer:
        def __init__(self) -> None: ...
        def createFramebufferObject(
            self, size: PySide6.QtCore.QSize
        ) -> PySide6.QtOpenGL.QOpenGLFramebufferObject: ...
        def framebufferObject(self) -> PySide6.QtOpenGL.QOpenGLFramebufferObject: ...
        def invalidateFramebufferObject(self) -> None: ...
        def render(self) -> None: ...
        def synchronize(
            self, arg__1: PySide6.QtQuick.QQuickFramebufferObject
        ) -> None: ...
        def update(self) -> None: ...

    def __init__(self, parent: PySide6.QtQuick.QQuickItem | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qquickframebufferobject.html#QQuickFramebufferObj
        ect

        **QQuickFramebufferObject::QQuickFramebufferObject(QQuickItem * parent =
        nullptr)**

        Constructs a new QQuickFramebufferObject with parent **parent**.
        """
        ...
    def createRenderer(self) -> PySide6.QtQuick.QQuickFramebufferObject.Renderer:
        """
        https://doc.qt.io/qt-6/qquickframebufferobject.html#createRenderer

        **[pure virtual] QQuickFramebufferObject::Renderer
        *QQuickFramebufferObject::createRenderer() const**

        Reimplement this function to create a renderer used to render into the
        FBO.

        This function will be called on the rendering thread while the GUI
        thread is blocked.
        """
        ...
    def geometryChange(
        self,
        newGeometry: PySide6.QtCore.QRectF | PySide6.QtCore.QRect,
        oldGeometry: PySide6.QtCore.QRectF | PySide6.QtCore.QRect,
    ) -> None: ...
    def isTextureProvider(self) -> bool:
        """
        https://doc.qt.io/qt-6/qquickframebufferobject.html#isTextureProvider

        **[override virtual] bool QQuickFramebufferObject::isTextureProvider()
        const**

        Reimplements: **QQuickItem::isTextureProvider() const** .
        """
        ...
    def mirrorVertically(self) -> bool:
        """
        https://doc.qt.io/qt-6/qquickframebufferobject.html#mirrorVertically-
        prop

        **[since 5.6] mirrorVertically : bool**

        This property controls if the size of the FBO's contents should be
        mirrored vertically when drawing. This allows easy integration of third-
        party rendering code that does not follow the standard expectations.

        The default value is `false`.

        This property was introduced in Qt 5.6.

        **Access functions:**

        bool **mirrorVertically** () const
        void **setMirrorVertically** (bool
        **enable** )

        **Notifier signal:**

        void **mirrorVerticallyChanged** (bool)
        """
        ...
    def releaseResources(self) -> None:
        """
        https://doc.qt.io/qt-6/qquickframebufferobject.html#releaseResources

        **[override virtual] void QQuickFramebufferObject::releaseResources()**

        Reimplements: **QQuickItem::releaseResources** ().
        """
        ...
    def setMirrorVertically(self, enable: bool) -> None:
        """
        https://doc.qt.io/qt-6/qquickframebufferobject.html#mirrorVertically-
        prop

        **[since 5.6] mirrorVertically : bool**

        This property controls if the size of the FBO's contents should be
        mirrored vertically when drawing. This allows easy integration of third-
        party rendering code that does not follow the standard expectations.

        The default value is `false`.

        This property was introduced in Qt 5.6.

        **Access functions:**

        bool **mirrorVertically** () const
        void **setMirrorVertically** (bool
        **enable** )

        **Notifier signal:**

        void **mirrorVerticallyChanged** (bool)
        """
        ...
    def setTextureFollowsItemSize(self, follows: bool) -> None:
        """
        https://doc.qt.io/qt-6/qquickframebufferobject.html#textureFollowsItemSi
        ze-prop

        **textureFollowsItemSize : bool**

        This property controls if the size of the FBO's texture should follow
        the dimensions of the **QQuickFramebufferObject**  item. When this
        property is false, the FBO will be created once the first time it is
        displayed. If it is set to true, the FBO will be recreated every time
        the dimensions of the item change.

        The default value is `true`.

        **Access functions:**

        bool **textureFollowsItemSize** () const
        void
        **setTextureFollowsItemSize** (bool **follows** )

        **Notifier signal:**

        void **textureFollowsItemSizeChanged** (bool)

        **Member Function Documentation**
        """
        ...
    def textureFollowsItemSize(self) -> bool:
        """
        https://doc.qt.io/qt-6/qquickframebufferobject.html#textureFollowsItemSi
        ze-prop

        **textureFollowsItemSize : bool**

        This property controls if the size of the FBO's texture should follow
        the dimensions of the **QQuickFramebufferObject**  item. When this
        property is false, the FBO will be created once the first time it is
        displayed. If it is set to true, the FBO will be recreated every time
        the dimensions of the item change.

        The default value is `true`.

        **Access functions:**

        bool **textureFollowsItemSize** () const
        void
        **setTextureFollowsItemSize** (bool **follows** )

        **Notifier signal:**

        void **textureFollowsItemSizeChanged** (bool)

        **Member Function Documentation**
        """
        ...
    def textureProvider(self) -> PySide6.QtQuick.QSGTextureProvider:
        """
        https://doc.qt.io/qt-6/qquickframebufferobject.html#textureProvider

        **[override virtual] QSGTextureProvider
        *QQuickFramebufferObject::textureProvider() const**

        Reimplements: **QQuickItem::textureProvider() const** .
        """
        ...
    def updatePaintNode(
        self,
        arg__1: PySide6.QtQuick.QSGNode,
        arg__2: PySide6.QtQuick.QQuickItem.UpdatePaintNodeData,
    ) -> PySide6.QtQuick.QSGNode: ...
    @property
    def mirrorVerticallyChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def textureFollowsItemSizeChanged(self) -> PySide6.QtCore.SignalInstance: ...