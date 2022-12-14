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
PySide6.QtGui, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtGui

class QOffscreenSurface(PySide6.QtCore.QObject, PySide6.QtGui.QSurface):
    """
    https://doc.qt.io/qt-6/qoffscreensurface.html

    **Detailed Description**

    QOffscreenSurface is intended to be used with **QOpenGLContext**  to allow
    rendering with OpenGL in an arbitrary thread without the need to create a
    **QWindow** .

    Even though the surface is typically renderable, the surface's pixels are
    not accessible. QOffscreenSurface should only be used to create OpenGL
    resources such as textures or framebuffer objects.

    An application will typically use QOffscreenSurface to perform some time-
    consuming tasks in a separate thread in order to avoid stalling the main
    rendering thread. Resources created in the QOffscreenSurface's context can
    be shared with the main OpenGL context. Some common use cases are
    asynchronous texture uploads or rendering into a
    **QOpenGLFramebufferObject** .

    How the offscreen surface is implemented depends on the underlying platform,
    but it will typically use a pixel buffer (pbuffer). If the platform doesn't
    implement or support offscreen surfaces, QOffscreenSurface will use an
    invisible **QWindow**  internally.

    **Note:** Due to the fact that QOffscreenSurface is backed by a **QWindow**
    on some platforms, cross-platform applications must ensure that **create**
    () is only called on the main (GUI) thread. The QOffscreenSurface is then
    safe to be used with **makeCurrent** () on other threads, but the
    initialization and destruction must always happen on the main (GUI) thread.

    **Note:** In order to create an offscreen surface that is guaranteed to be
    compatible with a given context and window, make sure to set the format to
    the context's or the window's actual format, that is, the **QSurfaceFormat**
    returned from **QOpenGLContext::format** () or **QWindow::format** ()
    **after the context or window has been created**. Passing the format
    returned from **QWindow::requestedFormat** () to **setFormat** () may result
    in an incompatible offscreen surface since the underlying windowing system
    interface may offer a different set of configurations for window and pbuffer
    surfaces.

    **Note:** Some platforms may utilize a surfaceless context extension (for
    example EGL_KHR_surfaceless_context) when available. In this case there will
    be no underlying native surface. For the use cases of QOffscreenSurface
    (rendering to FBOs, texture upload) this is not a problem.
    """

    def __init__(
        self,
        screen: PySide6.QtGui.QScreen | None = ...,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qoffscreensurface.html#QOffscreenSurface

        **[since 5.10] QOffscreenSurface::QOffscreenSurface(QScreen *
        targetScreen = nullptr, QObject * parent = nullptr)**

        Creates an offscreen surface for the **targetScreen** with the given
        **parent**.

        The underlying platform surface is not created until **create** () is
        called.

        This function was introduced in Qt 5.10.

        **See also** **setScreen** () and **create** ().
        """
        ...
    def create(self) -> None:
        """
        https://doc.qt.io/qt-6/qoffscreensurface.html#create

        **void QOffscreenSurface::create()**

        Allocates the platform resources associated with the offscreen surface.

        It is at this point that the surface format set using **setFormat** ()
        gets resolved into an actual native surface.

        Call **destroy** () to free the platform resources if necessary.

        **Note:** Some platforms require this function to be called on the main
        (GUI) thread.

        **See also** **destroy** ().
        """
        ...
    def destroy(self) -> None:
        """
        https://doc.qt.io/qt-6/qoffscreensurface.html#destroy

        **void QOffscreenSurface::destroy()**

        Releases the native platform resources associated with this offscreen
        surface.

        **See also** **create** ().
        """
        ...
    def format(self) -> PySide6.QtGui.QSurfaceFormat:
        """
        https://doc.qt.io/qt-6/qoffscreensurface.html#format

        **[override virtual] QSurfaceFormat QOffscreenSurface::format() const**

        Reimplements: **QSurface::format() const** .

        Returns the actual format of this offscreen surface.

        After the offscreen surface has been created, this function will return
        the actual surface format of the surface. It might differ from the
        requested format if the requested format could not be fulfilled by the
        platform.

        **See also** **setFormat** (), **create** (), and **requestedFormat**
        ().
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qoffscreensurface.html#isValid

        **bool QOffscreenSurface::isValid() const**

        Returns `true` if this offscreen surface is valid; otherwise returns
        `false`.

        The offscreen surface is valid if the platform resources have been
        successfully allocated.

        **See also** **create** ().
        """
        ...
    def requestedFormat(self) -> PySide6.QtGui.QSurfaceFormat:
        """
        https://doc.qt.io/qt-6/qoffscreensurface.html#requestedFormat

        **QSurfaceFormat QOffscreenSurface::requestedFormat() const**

        Returns the requested surfaceformat of this offscreen surface.

        If the requested format was not supported by the platform
        implementation, the requestedFormat will differ from the actual
        offscreen surface format.

        This is the value set with **setFormat** ().

        **See also** **setFormat** () and **format** ().
        """
        ...
    def resolveInterface(self, name: bytes, revision: int) -> int: ...
    def screen(self) -> PySide6.QtGui.QScreen:
        """
        https://doc.qt.io/qt-6/qoffscreensurface.html#screen

        **QScreen *QOffscreenSurface::screen() const**

        Returns the screen to which the offscreen surface is connected.

        **See also** **setScreen** ().
        """
        ...
    def setFormat(
        self,
        format: (
            PySide6.QtGui.QSurfaceFormat | PySide6.QtGui.QSurfaceFormat.FormatOptions
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qoffscreensurface.html#setFormat

        **void QOffscreenSurface::setFormat(const QSurfaceFormat & format )**

        Sets the offscreen surface **format**.

        The surface format will be resolved in the **create** () function.
        Calling this function after **create** () will not re-resolve the
        surface format of the native surface.

        **See also** **format** (), **create** (), and **destroy** ().
        """
        ...
    def setScreen(self, screen: PySide6.QtGui.QScreen) -> None:
        """
        https://doc.qt.io/qt-6/qoffscreensurface.html#setScreen

        **void QOffscreenSurface::setScreen(QScreen * newScreen )**

        Sets the screen to which the offscreen surface is connected.

        If the offscreen surface has been created, it will be recreated on the
        **newScreen**.

        **See also** **screen** ().
        """
        ...
    def size(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qoffscreensurface.html#size

        **[override virtual] QSize QOffscreenSurface::size() const**

        Reimplements: **QSurface::size() const** .

        Returns the size of the offscreen surface.
        """
        ...
    def surfaceHandle(self) -> int: ...
    def surfaceType(self) -> PySide6.QtGui.QSurface.SurfaceType:
        """
        https://doc.qt.io/qt-6/qoffscreensurface.html#surfaceType

        **[override virtual] QSurface::SurfaceType
        QOffscreenSurface::surfaceType() const**

        Reimplements: **QSurface::surfaceType() const** .

        Returns the surface type of the offscreen surface.

        The surface type of an offscreen surface is always
        **QSurface::OpenGLSurface** .
        """
        ...
    @property
    def screenChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qoffscreensurface.html#screenChanged

        **[signal] void QOffscreenSurface::screenChanged(QScreen * screen )**

        This signal is emitted when an offscreen surface's **screen** changes,
        either by being set explicitly with **setScreen** (), or automatically
        when the window's screen is removed.
        """
        ...
