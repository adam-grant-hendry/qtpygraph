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
PySide6.QtOpenGL, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtOpenGL

class QOpenGLPaintDevice(PySide6.QtGui.QPaintDevice):
    """
    https://doc.qt.io/qt-6/qopenglpaintdevice.html

    **Detailed Description**

    The QOpenGLPaintDevice uses the **current** QOpenGL context to render
    **QPainter**  draw commands. The context is captured upon construction. It
    requires support for OpenGL (ES) 2.0 or higher.

    **Performance**

    The QOpenGLPaintDevice is almost always hardware accelerated and has the
    potential of being much faster than software rasterization. However, it is
    more sensitive to state changes, and therefore requires the drawing commands
    to be carefully ordered to achieve optimal performance.

    **Antialiasing and Quality**

    Antialiasing in the OpenGL paint engine is done using multisampling. Most
    hardware require significantly more memory to do multisampling and the
    resulting quality is not on par with the quality of the software paint
    engine. The OpenGL paint engine's strength lies in its performance, not its
    visual rendering quality.

    **State Changes**

    When painting to a QOpenGLPaintDevice using **QPainter** , the state of the
    current OpenGL context will be altered by the paint engine to reflect its
    needs. Applications should not rely upon the OpenGL state being reset to its
    original conditions, particularly the current shader program, OpenGL
    viewport, texture units, and drawing modes.

    **Mixing QPainter and OpenGL**

    When intermixing **QPainter**  and OpenGL, it is important to notify
    **QPainter**  that the OpenGL state may have been cluttered so it can
    restore its internal state. This is achieved by calling
    **QPainter::beginNativePainting** () before starting the OpenGL rendering
    and calling **QPainter::endNativePainting** () after finishing.

    **See also** **OpenGL Window Example** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#QOpenGLPaintDevice

        **QOpenGLPaintDevice::QOpenGLPaintDevice()**

        Constructs a QOpenGLPaintDevice.

        The QOpenGLPaintDevice is only valid for the current context.

        **See also** **QOpenGLContext::currentContext** ().
        """
        ...
    @overload
    def __init__(self, size: PySide6.QtCore.QSize) -> None:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#QOpenGLPaintDevice-1

        **QOpenGLPaintDevice::QOpenGLPaintDevice(const QSize & size )**

        Constructs a QOpenGLPaintDevice with the given **size**.

        The QOpenGLPaintDevice is only valid for the current context.

        **See also** **QOpenGLContext::currentContext** ().
        """
        ...
    @overload
    def __init__(self, width: int, height: int) -> None:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#QOpenGLPaintDevice-2

        **QOpenGLPaintDevice::QOpenGLPaintDevice(int width , int height )**

        Constructs a QOpenGLPaintDevice with the given **width** and **height**.

        The QOpenGLPaintDevice is only valid for the current context.

        **See also** **QOpenGLContext::currentContext** ().
        """
        ...
    def context(self) -> PySide6.QtGui.QOpenGLContext:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#context

        **QOpenGLContext *QOpenGLPaintDevice::context() const**

        Returns the OpenGL context associated with the paint device.
        """
        ...
    def devType(self) -> int: ...
    def dotsPerMeterX(self) -> float:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#dotsPerMeterX

        **qreal QOpenGLPaintDevice::dotsPerMeterX() const**

        Returns the number of pixels per meter horizontally.

        **See also** **setDotsPerMeterX** ().
        """
        ...
    def dotsPerMeterY(self) -> float:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#dotsPerMeterY

        **qreal QOpenGLPaintDevice::dotsPerMeterY() const**

        Returns the number of pixels per meter vertically.

        **See also** **setDotsPerMeterY** ().
        """
        ...
    def ensureActiveTarget(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#ensureActiveTarget

        **[virtual] void QOpenGLPaintDevice::ensureActiveTarget()**

        This virtual method is provided as a callback to allow re-binding a
        target frame buffer object or context when different
        **QOpenGLPaintDevice**  instances are issuing draw calls alternately.

        **beginNativePainting** () will also trigger this method.

        The default implementation does nothing.
        """
        ...
    def metric(self, metric: PySide6.QtGui.QPaintDevice.PaintDeviceMetric) -> int:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#metric

        **[override virtual protected] int
        QOpenGLPaintDevice::metric(QPaintDevice::PaintDeviceMetric metric )
        const**

        Reimplements: **QPaintDevice::metric(QPaintDevice::PaintDeviceMetric
        metric) const** .
        """
        ...
    def paintEngine(self) -> PySide6.QtGui.QPaintEngine:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#paintEngine

        **[override virtual] QPaintEngine *QOpenGLPaintDevice::paintEngine()
        const**

        Reimplements: **QPaintDevice::paintEngine() const** .
        """
        ...
    def paintFlipped(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#paintFlipped

        **bool QOpenGLPaintDevice::paintFlipped() const**

        Returns `true` if painting is flipped around the Y-axis.

        **See also** **setPaintFlipped** ().
        """
        ...
    def setDevicePixelRatio(self, devicePixelRatio: float) -> None:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#setDevicePixelRatio

        **void QOpenGLPaintDevice::setDevicePixelRatio(qreal devicePixelRatio
        )**

        Sets the device pixel ratio for the paint device to
        **devicePixelRatio**.
        """
        ...
    def setDotsPerMeterX(self, arg__1: float) -> None:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#setDotsPerMeterX

        **void QOpenGLPaintDevice::setDotsPerMeterX(qreal dpmx )**

        Sets the number of pixels per meter horizontally to **dpmx**.

        **See also** **dotsPerMeterX** ().
        """
        ...
    def setDotsPerMeterY(self, arg__1: float) -> None:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#setDotsPerMeterY

        **void QOpenGLPaintDevice::setDotsPerMeterY(qreal dpmy )**

        Sets the number of pixels per meter vertically to **dpmy**.

        **See also** **dotsPerMeterY** ().
        """
        ...
    def setPaintFlipped(self, flipped: bool) -> None:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#setPaintFlipped

        **void QOpenGLPaintDevice::setPaintFlipped(bool flipped )**

        Sets whether painting should be flipped around the Y-axis or not to
        **flipped**.

        **See also** **paintFlipped** ().
        """
        ...
    def setSize(self, size: PySide6.QtCore.QSize) -> None:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#setSize

        **void QOpenGLPaintDevice::setSize(const QSize & size )**

        Sets the pixel size of the paint device to **size**.

        **See also** **size** ().
        """
        ...
    def size(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qopenglpaintdevice.html#size

        **QSize QOpenGLPaintDevice::size() const**

        Returns the pixel size of the paint device.

        **See also** **setSize** ().
        """
        ...
