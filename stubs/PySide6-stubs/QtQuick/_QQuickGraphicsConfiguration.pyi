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

from collections.abc import Sequence
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtOpenGL
import PySide6.QtQml
import PySide6.QtQuick

class QQuickGraphicsConfiguration:
    """
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html

    **Detailed Description**

    When constructing and showing a **QQuickWindow**  that uses Vulkan to
    render, a Vulkan instance (`VkInstance`), a physical device
    (`VkPhysicalDevice`), a device (`VkDevice`) and associated objects (queues,
    pools) are initialized through the Vulkan API. The same is mostly true when
    using **QQuickRenderControl**  to redirect the rendering into a custom
    render target, such as a texture. While **QVulkanInstance**  construction is
    under the application's control then, the initialization of other graphics
    objects happen the same way in **QQuickRenderControl::initialize** () as
    with an on-screen **QQuickWindow** .

    For the majority of applications no additional configuration is needed
    because Qt Quick provides reasonable defaults for many low-level graphics
    settings, for example which device extensions to enable.

    This will not alway be sufficient, however. In advanced use cases, when
    integrating direct Vulkan or other graphics API content, or when integrating
    with an external 3D or VR engine, such as, OpenXR, the application will want
    to specify its own set of settings when it comes to details, such as which
    device extensions to enable.

    That is what this class enables. It allows specifying, for example, a list
    of device extensions that is then picked up by the scene graph when using
    Vulkan, or graphics APIs where the concept is applicable. Where some
    concepts are not applicable, the related settings are simply ignored.

    Another class of settings are related to the scene graph's renderer. In some
    cases applications may want to control certain behavior,such as using the
    depth buffer when rendering 2D content. In Qt 5 such settings were either
    not controllable at all, or were managed through environment variables. In
    Qt 6, QQuickGraphicsConfiguration provides a new home for these settings,
    while keeping support for the legacy environment variables, where
    applicable.

    **Note:** Setting a QQuickGraphicsConfiguration on a **QQuickWindow**  must
    happen early enough, before the scene graph is initialized for the first
    time for that window. With on-screen windows this means the call must be
    done before invoking show() on the **QQuickWindow**  or **QQuickView** .
    With **QQuickRenderControl**  the configuration must be finalized before
    calling **initialize** ().

    **See also** **QQuickWindow::setGraphicsConfiguration** (), **QQuickWindow**
    , and **QQuickRenderControl** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#QQuickGraphicsCo
        nfiguration

        **QQuickGraphicsConfiguration::QQuickGraphicsConfiguration()**

        Constructs a default QQuickGraphicsConfiguration that does not specify
        any additional settings for the scene graph to take into account.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtQuick.QQuickGraphicsConfiguration) -> None:
        """
        https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#QQuickGraphicsCo
        nfiguration

        **QQuickGraphicsConfiguration::QQuickGraphicsConfiguration()**

        Constructs a default QQuickGraphicsConfiguration that does not specify
        any additional settings for the scene graph to take into account.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def deviceExtensions(self) -> list[PySide6.QtCore.QByteArray]:
        """
        https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#deviceExtensions

        **QByteArrayList QQuickGraphicsConfiguration::deviceExtensions() const**

        Returns the list of the requested additional device extensions.

        **See also** **setDeviceExtensions** ().
        """
        ...
    def isDepthBufferEnabledFor2D(self) -> bool:
        """
        https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#isDepthBufferEna
        bledFor2D

        **bool QQuickGraphicsConfiguration::isDepthBufferEnabledFor2D() const**

        Returns true if depth buffer usage is enabled for 2D content.

        By default the value is true, unless the `QSG_NO_DEPTH_BUFFER`
        environment variable is set.
        """
        ...
    @staticmethod
    def preferredInstanceExtensions() -> list[PySide6.QtCore.QByteArray]:
        """
        https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#preferredInstanc
        eExtensions

        **[static, since 6.1] QByteArrayList
        QQuickGraphicsConfiguration::preferredInstanceExtensions()**

        Returns the list of Vulkan instance extensions Qt Quick prefers to have
        enabled on the VkInstance.

        In most cases Qt Quick is responsible for creating a **QVulkanInstance**
        . This function is not relevant then. On the other hand, when using
        **QQuickRenderControl**  in combination with Vulkan-based rendering, it
        is the application's responsibility to create a **QVulkanInstance**  and
        associate it with the (offscreen) **QQuickWindow** . In this case, it is
        expected that the application queries the list of instance extensions to
        enable, and passes them to **QVulkanInstance::setExtensions** () before
        calling **QVulkanInstance::create** ().

        This function was introduced in Qt 6.1.
        """
        ...
    def setDepthBufferFor2D(self, enable: bool) -> None:
        """
        https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#setDepthBufferFo
        r2D

        **void QQuickGraphicsConfiguration::setDepthBufferFor2D(bool enable )**

        Sets the usage of depth buffer for 2D content to **enable**. When
        disabled, the Qt Quick scene graph never writes into the depth buffer.

        By default the value is true, unless the `QSG_NO_DEPTH_BUFFER`
        environment variable is set.

        The default value of true is the most optimal setting for the vast
        majority of scenes. Disabling depth buffer usage reduces the efficiency
        of the scene graph's batching.

        There are cases however, when allowing the 2D content write to the depth
        buffer is not ideal. Consider a 3D scene as an "overlay" on top the 2D
        scene, rendered via Qt Quick 3D using a **View3D**  with **renderMode**
        set to `Overlay`. In this case, having the depth buffer filled by 2D
        content can cause unexpected results. This is because the way the 2D
        scene graph renderer generates and handles depth values is not
        necessarily compatible with how a 3D scene works. This may end up in
        depth value clashes, collisions, and unexpected depth test failures.
        Therefore, the robust approach here is to call this function with
        **enable** set to false, and disable depth buffer writes for the 2D
        content in the **QQuickWindow** .

        **Note:** This flag is not fully identical to setting the
        `QSG_NO_DEPTH_BUFFER` environment variable. This flag does not control
        the depth-stencil buffers' presence. It is rather relevant for the
        rendering pipeline. To force not having depth/stencil attachments at
        all, set `QSG_NO_DEPTH_BUFFER` and `QSG_NO_STENCIL_BUFFER`. Be aware
        however that such a **QQuickWindow** , and any Item layers in it, may
        then become incompatible with items, such as **View3D**  with certain
        operating modes, because 3D content requires a depth buffer. Calling
        this function is always safe, but can mean that resources, such as depth
        buffers, are created even though they are not actively used.
        """
        ...
    def setDeviceExtensions(
        self, extensions: Sequence[PySide6.QtCore.QByteArray]
    ) -> None:
        """
        https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#setDeviceExtensi
        ons

        **void QQuickGraphicsConfiguration::setDeviceExtensions(const
        QByteArrayList & extensions )**

        Sets the list of additional **extensions** to enable on the graphics
        device (such as, the `VkDevice`).

        When rendering with a graphics API where the concept is not applicable,
        **extensions** will be ignored.

        **Note:** The list specifies additional, extra extensions. Qt Quick
        always enables extensions that are required by the scene graph.

        **See also** **deviceExtensions** ().
        """
        ...