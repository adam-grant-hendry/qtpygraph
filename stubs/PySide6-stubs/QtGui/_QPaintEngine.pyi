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

from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtGui

class QPaintEngine:
    """
    https://doc.qt.io/qt-6/qpaintengine.html

    **Detailed Description**

    Qt provides several premade implementations of QPaintEngine for the
    different painter backends we support. The primary paint engine provided is
    the raster paint engine, which contains a software rasterizer which supports
    the full feature set on all supported platforms. This is the default for
    painting on **QWidget** -based classes in e.g. on Windows, X11 and macOS, it
    is the backend for painting on **QImage**  and it is used as a fallback for
    paint engines that do not support a certain capability. In addition we
    provide QPaintEngine implementations for OpenGL (accessible through
    **QOpenGLWidget** ) and printing (which allows using **QPainter**  to draw
    on a **QPrinter**  object).

    If one wants to use **QPainter**  to draw to a different backend, one must
    subclass QPaintEngine and reimplement all its virtual functions. The
    QPaintEngine implementation is then made available by subclassing
    **QPaintDevice**  and reimplementing the virtual function
    **QPaintDevice::paintEngine** ().

    QPaintEngine is created and owned by the **QPaintDevice**  that created it.

    **See also** **QPainter** , **QPaintDevice::paintEngine** (), and **Paint
    System** .
    """

    DirtyPen: QPaintEngine.DirtyFlag = ...
    DirtyBrush: QPaintEngine.DirtyFlag = ...
    DirtyBrushOrigin: QPaintEngine.DirtyFlag = ...
    DirtyFont: QPaintEngine.DirtyFlag = ...
    DirtyBackground: QPaintEngine.DirtyFlag = ...
    DirtyBackgroundMode: QPaintEngine.DirtyFlag = ...
    DirtyTransform: QPaintEngine.DirtyFlag = ...
    DirtyClipRegion: QPaintEngine.DirtyFlag = ...
    DirtyClipPath: QPaintEngine.DirtyFlag = ...
    DirtyHints: QPaintEngine.DirtyFlag = ...
    DirtyCompositionMode: QPaintEngine.DirtyFlag = ...
    DirtyClipEnabled: QPaintEngine.DirtyFlag = ...
    DirtyOpacity: QPaintEngine.DirtyFlag = ...
    AllDirty: QPaintEngine.DirtyFlag = ...
    AllFeatures: QPaintEngine.PaintEngineFeature = ...
    PrimitiveTransform: QPaintEngine.PaintEngineFeature = ...
    PatternTransform: QPaintEngine.PaintEngineFeature = ...
    PixmapTransform: QPaintEngine.PaintEngineFeature = ...
    PatternBrush: QPaintEngine.PaintEngineFeature = ...
    LinearGradientFill: QPaintEngine.PaintEngineFeature = ...
    RadialGradientFill: QPaintEngine.PaintEngineFeature = ...
    ConicalGradientFill: QPaintEngine.PaintEngineFeature = ...
    AlphaBlend: QPaintEngine.PaintEngineFeature = ...
    PorterDuff: QPaintEngine.PaintEngineFeature = ...
    PainterPaths: QPaintEngine.PaintEngineFeature = ...
    Antialiasing: QPaintEngine.PaintEngineFeature = ...
    BrushStroke: QPaintEngine.PaintEngineFeature = ...
    ConstantOpacity: QPaintEngine.PaintEngineFeature = ...
    MaskedBrush: QPaintEngine.PaintEngineFeature = ...
    PerspectiveTransform: QPaintEngine.PaintEngineFeature = ...
    BlendModes: QPaintEngine.PaintEngineFeature = ...
    ObjectBoundingModeGradients: QPaintEngine.PaintEngineFeature = ...
    RasterOpModes: QPaintEngine.PaintEngineFeature = ...
    PaintOutsidePaintEvent: QPaintEngine.PaintEngineFeature = ...
    OddEvenMode: QPaintEngine.PolygonDrawMode = ...
    WindingMode: QPaintEngine.PolygonDrawMode = ...
    ConvexMode: QPaintEngine.PolygonDrawMode = ...
    PolylineMode: QPaintEngine.PolygonDrawMode = ...
    X11: QPaintEngine.Type = ...
    Windows: QPaintEngine.Type = ...
    QuickDraw: QPaintEngine.Type = ...
    CoreGraphics: QPaintEngine.Type = ...
    MacPrinter: QPaintEngine.Type = ...
    QWindowSystem: QPaintEngine.Type = ...
    OpenGL: QPaintEngine.Type = ...
    Picture: QPaintEngine.Type = ...
    SVG: QPaintEngine.Type = ...
    Raster: QPaintEngine.Type = ...
    Direct3D: QPaintEngine.Type = ...
    Pdf: QPaintEngine.Type = ...
    OpenVG: QPaintEngine.Type = ...
    OpenGL2: QPaintEngine.Type = ...
    PaintBuffer: QPaintEngine.Type = ...
    Blitter: QPaintEngine.Type = ...
    Direct2D: QPaintEngine.Type = ...
    User: QPaintEngine.Type = ...
    MaxUser: QPaintEngine.Type = ...

    class DirtyFlag(IntFlag):
        DirtyPen: QPaintEngine.DirtyFlag = ...
        DirtyBrush: QPaintEngine.DirtyFlag = ...
        DirtyBrushOrigin: QPaintEngine.DirtyFlag = ...
        DirtyFont: QPaintEngine.DirtyFlag = ...
        DirtyBackground: QPaintEngine.DirtyFlag = ...
        DirtyBackgroundMode: QPaintEngine.DirtyFlag = ...
        DirtyTransform: QPaintEngine.DirtyFlag = ...
        DirtyClipRegion: QPaintEngine.DirtyFlag = ...
        DirtyClipPath: QPaintEngine.DirtyFlag = ...
        DirtyHints: QPaintEngine.DirtyFlag = ...
        DirtyCompositionMode: QPaintEngine.DirtyFlag = ...
        DirtyClipEnabled: QPaintEngine.DirtyFlag = ...
        DirtyOpacity: QPaintEngine.DirtyFlag = ...
        AllDirty: QPaintEngine.DirtyFlag = ...

    class DirtyFlags: ...

    class PaintEngineFeature(IntFlag):
        AllFeatures: QPaintEngine.PaintEngineFeature = ...
        PrimitiveTransform: QPaintEngine.PaintEngineFeature = ...
        PatternTransform: QPaintEngine.PaintEngineFeature = ...
        PixmapTransform: QPaintEngine.PaintEngineFeature = ...
        PatternBrush: QPaintEngine.PaintEngineFeature = ...
        LinearGradientFill: QPaintEngine.PaintEngineFeature = ...
        RadialGradientFill: QPaintEngine.PaintEngineFeature = ...
        ConicalGradientFill: QPaintEngine.PaintEngineFeature = ...
        AlphaBlend: QPaintEngine.PaintEngineFeature = ...
        PorterDuff: QPaintEngine.PaintEngineFeature = ...
        PainterPaths: QPaintEngine.PaintEngineFeature = ...
        Antialiasing: QPaintEngine.PaintEngineFeature = ...
        BrushStroke: QPaintEngine.PaintEngineFeature = ...
        ConstantOpacity: QPaintEngine.PaintEngineFeature = ...
        MaskedBrush: QPaintEngine.PaintEngineFeature = ...
        PerspectiveTransform: QPaintEngine.PaintEngineFeature = ...
        BlendModes: QPaintEngine.PaintEngineFeature = ...
        ObjectBoundingModeGradients: QPaintEngine.PaintEngineFeature = ...
        RasterOpModes: QPaintEngine.PaintEngineFeature = ...
        PaintOutsidePaintEvent: QPaintEngine.PaintEngineFeature = ...

    class PaintEngineFeatures: ...

    class PolygonDrawMode(IntFlag):
        OddEvenMode: QPaintEngine.PolygonDrawMode = ...
        WindingMode: QPaintEngine.PolygonDrawMode = ...
        ConvexMode: QPaintEngine.PolygonDrawMode = ...
        PolylineMode: QPaintEngine.PolygonDrawMode = ...

    class Type(IntFlag):
        X11: QPaintEngine.Type = ...
        Windows: QPaintEngine.Type = ...
        QuickDraw: QPaintEngine.Type = ...
        CoreGraphics: QPaintEngine.Type = ...
        MacPrinter: QPaintEngine.Type = ...
        QWindowSystem: QPaintEngine.Type = ...
        OpenGL: QPaintEngine.Type = ...
        Picture: QPaintEngine.Type = ...
        SVG: QPaintEngine.Type = ...
        Raster: QPaintEngine.Type = ...
        Direct3D: QPaintEngine.Type = ...
        Pdf: QPaintEngine.Type = ...
        OpenVG: QPaintEngine.Type = ...
        OpenGL2: QPaintEngine.Type = ...
        PaintBuffer: QPaintEngine.Type = ...
        Blitter: QPaintEngine.Type = ...
        Direct2D: QPaintEngine.Type = ...
        User: QPaintEngine.Type = ...
        MaxUser: QPaintEngine.Type = ...
    def __init__(
        self, features: PySide6.QtGui.QPaintEngine.PaintEngineFeatures = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#QPaintEngine

        **QPaintEngine::QPaintEngine(QPaintEngine::PaintEngineFeatures caps =
        PaintEngineFeatures())**

        Creates a paint engine with the featureset specified by **caps**.
        """
        ...
    def begin(self, pdev: PySide6.QtGui.QPaintDevice) -> bool:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#begin

        **[pure virtual] bool QPaintEngine::begin(QPaintDevice * pdev )**

        Reimplement this function to initialise your paint engine when painting
        is to start on the paint device **pdev**. Return true if the
        initialization was successful; otherwise return false.

        **See also** **end** () and **isActive** ().
        """
        ...
    def clearDirty(self, df: PySide6.QtGui.QPaintEngine.DirtyFlags) -> None: ...
    def coordinateOffset(self) -> PySide6.QtCore.QPoint: ...
    def createPixmap(self, size: PySide6.QtCore.QSize) -> PySide6.QtGui.QPixmap: ...
    def createPixmapFromImage(
        self,
        image: PySide6.QtGui.QImage | str,
        flags: PySide6.QtCore.Qt.ImageConversionFlags = ...,
    ) -> PySide6.QtGui.QPixmap: ...
    @overload
    def drawEllipse(self, r: PySide6.QtCore.QRect) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawEllipse

        **[virtual] void QPaintEngine::drawEllipse(const QRectF & rect )**

        Reimplement this function to draw the largest ellipse that can be
        contained within rectangle **rect**.

        The default implementation calls **drawPolygon** ().
        """
        ...
    @overload
    def drawEllipse(self, r: PySide6.QtCore.QRectF | PySide6.QtCore.QRect) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawEllipse-1

        **[virtual] void QPaintEngine::drawEllipse(const QRect & rect )**

        The default implementation of this function calls the floating point
        version of this function
        """
        ...
    def drawImage(
        self,
        r: PySide6.QtCore.QRectF | PySide6.QtCore.QRect,
        pm: PySide6.QtGui.QImage | str,
        sr: PySide6.QtCore.QRectF | PySide6.QtCore.QRect,
        flags: PySide6.QtCore.Qt.ImageConversionFlags = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawImage

        **[virtual] void QPaintEngine::drawImage(const QRectF & rectangle ,
        const QImage & image , const QRectF & sr , Qt::ImageConversionFlags
        flags = Qt::AutoColor)**

        Reimplement this function to draw the part of the **image** specified by
        the **sr** rectangle in the given **rectangle** using the given
        conversion flags **flags** , to convert it to a pixmap.
        """
        ...
    @overload
    def drawLines(self, lines: PySide6.QtCore.QLine, lineCount: int) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawLines

        **[virtual] void QPaintEngine::drawLines(const QLineF * lines , int
        lineCount )**

        The default implementation splits the list of lines in **lines** into
        **lineCount** separate calls to **drawPath** () or **drawPolygon** ()
        depending on the feature set of the paint engine.
        """
        ...
    @overload
    def drawLines(
        self, lines: PySide6.QtCore.QLineF | PySide6.QtCore.QLine, lineCount: int
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawLines-1

        **[virtual] void QPaintEngine::drawLines(const QLine * lines , int
        lineCount )**

        This is an overloaded function.

        The default implementation converts the first **lineCount** lines in
        **lines** to a **QLineF**  and calls the floating point version of this
        function.
        """
        ...
    def drawPath(self, path: PySide6.QtGui.QPainterPath) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawPath

        **[virtual] void QPaintEngine::drawPath(const QPainterPath & path )**

        The default implementation ignores the **path** and does nothing.
        """
        ...
    def drawPixmap(
        self,
        r: PySide6.QtCore.QRectF | PySide6.QtCore.QRect,
        pm: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage | str,
        sr: PySide6.QtCore.QRectF | PySide6.QtCore.QRect,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawPixmap

        **[pure virtual] void QPaintEngine::drawPixmap(const QRectF & r , const
        QPixmap & pm , const QRectF & sr )**

        Reimplement this function to draw the part of the **pm** specified by
        the **sr** rectangle in the given **r**.
        """
        ...
    @overload
    def drawPoints(self, points: PySide6.QtCore.QPoint, pointCount: int) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawPoints

        **[virtual] void QPaintEngine::drawPoints(const QPointF * points , int
        pointCount )**

        Draws the first **pointCount** points in the buffer **points**
        """
        ...
    @overload
    def drawPoints(
        self,
        points: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        pointCount: int,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawPoints-1

        **[virtual] void QPaintEngine::drawPoints(const QPoint * points , int
        pointCount )**

        Draws the first **pointCount** points in the buffer **points**

        The default implementation converts the first **pointCount** QPoints in
        **points** to QPointFs and calls the floating point version of
        drawPoints.
        """
        ...
    @overload
    def drawPolygon(
        self,
        points: PySide6.QtCore.QPoint,
        pointCount: int,
        mode: PySide6.QtGui.QPaintEngine.PolygonDrawMode,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawPolygon

        **[virtual] void QPaintEngine::drawPolygon(const QPointF * points , int
        pointCount , QPaintEngine::PolygonDrawMode mode )**

        Reimplement this virtual function to draw the polygon defined by the
        **pointCount** first points in **points** , using mode **mode**.

        **Note:** At least one of the drawPolygon() functions must be
        reimplemented.
        """
        ...
    @overload
    def drawPolygon(
        self,
        points: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        pointCount: int,
        mode: PySide6.QtGui.QPaintEngine.PolygonDrawMode,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawPolygon-1

        **[virtual] void QPaintEngine::drawPolygon(const QPoint * points , int
        pointCount , QPaintEngine::PolygonDrawMode mode )**

        This is an overloaded function.

        Reimplement this virtual function to draw the polygon defined by the
        **pointCount** first points in **points** , using mode **mode**.

        **Note:** At least one of the drawPolygon() functions must be
        reimplemented.
        """
        ...
    @overload
    def drawRects(self, rects: PySide6.QtCore.QRect, rectCount: int) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawRects

        **[virtual] void QPaintEngine::drawRects(const QRectF * rects , int
        rectCount )**

        Draws the first **rectCount** rectangles in the buffer **rects**. The
        default implementation of this function calls **drawPath** () or
        **drawPolygon** () depending on the feature set of the paint engine.
        """
        ...
    @overload
    def drawRects(
        self, rects: PySide6.QtCore.QRectF | PySide6.QtCore.QRect, rectCount: int
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawRects-1

        **[virtual] void QPaintEngine::drawRects(const QRect * rects , int
        rectCount )**

        This is an overloaded function.

        The default implementation converts the first **rectCount** rectangles
        in the buffer **rects** to a **QRectF**  and calls the floating point
        version of this function.
        """
        ...
    def drawTextItem(
        self,
        p: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
        textItem: PySide6.QtGui.QTextItem,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawTextItem

        **[virtual] void QPaintEngine::drawTextItem(const QPointF & p , const
        QTextItem & textItem )**

        This function draws the text item **textItem** at position **p**. The
        default implementation of this function converts the text to a
        **QPainterPath**  and paints the resulting path.
        """
        ...
    def drawTiledPixmap(
        self,
        r: PySide6.QtCore.QRectF | PySide6.QtCore.QRect,
        pixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage | str,
        s: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#drawTiledPixmap

        **[virtual] void QPaintEngine::drawTiledPixmap(const QRectF & rect ,
        const QPixmap & pixmap , const QPointF & p )**

        Reimplement this function to draw the **pixmap** in the given **rect** ,
        starting at the given **p**. The pixmap will be drawn repeatedly until
        the **rect** is filled.
        """
        ...
    def end(self) -> bool:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#end

        **[pure virtual] bool QPaintEngine::end()**

        Reimplement this function to finish painting on the current paint
        device. Return true if painting was finished successfully; otherwise
        return false.

        **See also** **begin** () and **isActive** ().
        """
        ...
    def hasFeature(self, feature: PySide6.QtGui.QPaintEngine.PaintEngineFeatures) -> bool:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#hasFeature

        **bool QPaintEngine::hasFeature(QPaintEngine::PaintEngineFeatures
        feature ) const**

        Returns `true` if the paint engine supports the specified **feature** ;
        otherwise returns `false`.
        """
        ...
    def isActive(self) -> bool:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#isActive

        **bool QPaintEngine::isActive() const**

        Returns `true` if the paint engine is actively drawing; otherwise
        returns `false`.

        **See also** **setActive** ().
        """
        ...
    def isExtended(self) -> bool: ...
    def paintDevice(self) -> PySide6.QtGui.QPaintDevice:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#paintDevice

        **QPaintDevice *QPaintEngine::paintDevice() const**

        Returns the device that this engine is painting on, if painting is
        active; otherwise returns `nullptr`.
        """
        ...
    def painter(self) -> PySide6.QtGui.QPainter:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#painter

        **QPainter *QPaintEngine::painter() const**

        Returns the paint engine's painter.
        """
        ...
    def setActive(self, newState: bool) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#setActive

        **void QPaintEngine::setActive(bool state )**

        Sets the active state of the paint engine to **state**.

        **See also** **isActive** ().
        """
        ...
    def setDirty(self, df: PySide6.QtGui.QPaintEngine.DirtyFlags) -> None: ...
    def setSystemClip(
        self,
        baseClip: (
            PySide6.QtGui.QRegion
            | PySide6.QtGui.QBitmap
            | PySide6.QtGui.QPolygon
            | PySide6.QtCore.QRect
        ),
    ) -> None: ...
    def setSystemRect(self, rect: PySide6.QtCore.QRect) -> None: ...
    def syncState(self) -> None: ...
    def systemClip(self) -> PySide6.QtGui.QRegion: ...
    def systemRect(self) -> PySide6.QtCore.QRect: ...
    def testDirty(self, df: PySide6.QtGui.QPaintEngine.DirtyFlags) -> bool: ...
    def type(self) -> PySide6.QtGui.QPaintEngine.Type:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#type

        **[pure virtual] QPaintEngine::Type QPaintEngine::type() const**

        Reimplement this function to return the paint engine **Type** .
        """
        ...
    def updateState(self, state: PySide6.QtGui.QPaintEngineState) -> None:
        """
        https://doc.qt.io/qt-6/qpaintengine.html#updateState

        **[pure virtual] void QPaintEngine::updateState(const QPaintEngineState
        & state )**

        Reimplement this function to update the state of a paint engine.

        When implemented, this function is responsible for checking the paint
        engine's current **state** and update the properties that are changed.
        Use the **QPaintEngineState::state** () function to find out which
        properties that must be updated, then use the corresponding **get
        function**  to retrieve the current values for the given properties.

        **See also** **QPaintEngineState** .
        """
        ...