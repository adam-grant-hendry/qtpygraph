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
PySide6.QtDataVisualization, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtDataVisualization
import PySide6.QtGui

class Q3DScene(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/q3dscene.html

    **Detailed Description**

    The 3D scene contains a single active camera and a single active light
    source. Visualized data is assumed to be at a fixed location.

    The 3D scene also keeps track of the viewport in which visualization
    rendering is done, the primary subviewport inside the viewport where the
    main 3D data visualization view resides and the secondary subviewport where
    the 2D sliced view of the data resides. The subviewports are by default
    resized by the **Q3DScene**. To override the resize behavior you need to
    listen to both **viewportChanged** () and **slicingActiveChanged** ()
    signals and recalculate the subviewports accordingly.

    Also the scene has flag for tracking if the secondary 2D slicing view is
    currently active or not.

    **Note:** Not all visualizations support the secondary 2D slicing view.
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/q3dscene.html#Q3DScene

        **Q3DScene::Q3DScene(QObject * parent = nullptr)**

        Constructs a basic scene with one light and one camera in it. An
        optional **parent** parameter can be given and is then passed to
        **QObject**  constructor.
        """
        ...
    def activeCamera(self) -> PySide6.QtDataVisualization.Q3DCamera:
        """
        https://doc.qt.io/qt-6/q3dscene.html#activeCamera-prop

        **activeCamera : Q3DCamera***

        This property holds the currently active camera in the 3D scene.

        When a new **Q3DCamera**  object is set, it is automatically added as
        child of the scene.

        **Access functions:**

        Q3DCamera * **activeCamera** () const
        void **setActiveCamera**
        (Q3DCamera * **camera** )

        **Notifier signal:**

        void **activeCameraChanged** (Q3DCamera * **camera** )
        """
        ...
    def activeLight(self) -> PySide6.QtDataVisualization.Q3DLight:
        """
        https://doc.qt.io/qt-6/q3dscene.html#activeLight-prop

        **activeLight : Q3DLight***

        This property holds the currently active light in the 3D scene.

        When a new **Q3DLight**  objects is set, it is automatically added as
        child of the scene.

        **Access functions:**

        Q3DLight * **activeLight** () const
        void **setActiveLight** (Q3DLight
        * **light** )

        **Notifier signal:**

        void **activeLightChanged** (Q3DLight * **light** )
        """
        ...
    def devicePixelRatio(self) -> float:
        """
        https://doc.qt.io/qt-6/q3dscene.html#devicePixelRatio-prop

        **devicePixelRatio : float**

        This property holds the device pixel ratio that is used when mapping
        input coordinates to pixel coordinates.

        **Access functions:**

        float **devicePixelRatio** () const
        void **setDevicePixelRatio**
        (float **pixelRatio** )

        **Notifier signal:**

        void **devicePixelRatioChanged** (float **pixelRatio** )
        """
        ...
    def graphPositionQuery(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/q3dscene.html#graphPositionQuery-prop

        **graphPositionQuery : QPoint**

        This property holds the coordinates for the user input that should be
        processed by the scene as a graph position query.

        If this property is set to a value other than **invalidSelectionPoint**
        (), the graph tries to match a graph position to the specified
        coordinates within the primary viewport. After the rendering pass, this
        property is returned to its default state of **invalidSelectionPoint**
        (). The queried graph position can be read from the
        **QAbstract3DGraph::queriedGraphPosition**  property after the next
        render pass.

        There is no single correct 3D coordinate to match a particular screen
        position, so to be consistent, the queries are always done against the
        inner sides of an invisible box surrounding the graph.

        **Note:** Bar graphs allow graph position queries only at the graph
        floor level.

        **Access functions:**

        QPoint **graphPositionQuery** () const
        void **setGraphPositionQuery**
        (const QPoint & **point** )

        **Notifier signal:**

        void **graphPositionQueryChanged** (const QPoint & **position** )

        **See also** **QAbstract3DGraph::queriedGraphPosition** .
        """
        ...
    @staticmethod
    def invalidSelectionPoint() -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/q3dscene.html#invalidSelectionPoint

        **[static] QPoint Q3DScene::invalidSelectionPoint()**

        Returns a **QPoint**  signifying an invalid selection position.
        """
        ...
    def isPointInPrimarySubView(self, point: PySide6.QtCore.QPoint) -> bool:
        """
        https://doc.qt.io/qt-6/q3dscene.html#isPointInPrimarySubView

        **bool Q3DScene::isPointInPrimarySubView(const QPoint & point )**

        Returns whether the given **point** resides inside the primary subview
        or not. Returns `true` if the point is inside the primary subview.

        **Note:** If subviews are superimposed, and the given **point** resides
        inside both, result is `true` only when the primary subview is on top.
        """
        ...
    def isPointInSecondarySubView(self, point: PySide6.QtCore.QPoint) -> bool:
        """
        https://doc.qt.io/qt-6/q3dscene.html#isPointInSecondarySubView

        **bool Q3DScene::isPointInSecondarySubView(const QPoint & point )**

        Returns whether the given **point** resides inside the secondary subview
        or not. Returns `true` if the point is inside the secondary subview.

        **Note:** If subviews are superimposed, and the given **point** resides
        inside both, result is `true` only when the secondary subview is on top.
        """
        ...
    def isSecondarySubviewOnTop(self) -> bool: ...
    def isSlicingActive(self) -> bool: ...
    def primarySubViewport(self) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/q3dscene.html#primarySubViewport-prop

        **primarySubViewport : QRect**

        This property holds the current subviewport rectangle inside the
        viewport where the primary view of the data visualization is targeted.

        If **isSlicingActive** () is `false`, the primary sub viewport is equal
        to **viewport** (). If **isSlicingActive** () is `true` and the primary
        sub viewport has not been explicitly set, it will be one fifth of
        **viewport** ().

        **Note:** Setting primarySubViewport larger than or outside of the
        viewport resizes the viewport accordingly.

        **Access functions:**

        QRect **primarySubViewport** () const
        void **setPrimarySubViewport**
        (const QRect & **primarySubViewport** )

        **Notifier signal:**

        void **primarySubViewportChanged** (const QRect & **subViewport** )
        """
        ...
    def secondarySubViewport(self) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/q3dscene.html#secondarySubViewport-prop

        **secondarySubViewport : QRect**

        This property holds the secondary viewport rectangle inside the
        viewport.

        The secondary viewport is used for drawing the 2D slice view in some
        visualizations. If it has not been explicitly set, it will be equal to
        **QRect** . If **isSlicingActive** () is `true`, it will be equal to
        **viewport** .

        **Note:** If the secondary sub viewport is larger than or outside of the
        viewport, the viewport is resized accordingly.

        **Access functions:**

        QRect **secondarySubViewport** () const
        void
        **setSecondarySubViewport** (const QRect & **secondarySubViewport** )

        **Notifier signal:**

        void **secondarySubViewportChanged** (const QRect & **subViewport** )
        """
        ...
    def selectionQueryPosition(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/q3dscene.html#selectionQueryPosition-prop

        **selectionQueryPosition : QPoint**

        This property holds the coordinates for the user input that should be
        processed by the scene as a selection.

        If this property is set to a value other than **invalidSelectionPoint**
        (), the graph tries to select a data item, axis label, or a custom item
        at the specified coordinates within the primary viewport. After the
        rendering pass, the property is returned to its default state of
        **invalidSelectionPoint** ().

        **Access functions:**

        QPoint **selectionQueryPosition** () const
        void
        **setSelectionQueryPosition** (const QPoint & **point** )

        **Notifier signal:**

        void **selectionQueryPositionChanged** (const QPoint & **position** )

        **See also** **QAbstract3DGraph::selectedElement** .
        """
        ...
    def setActiveCamera(self, camera: PySide6.QtDataVisualization.Q3DCamera) -> None:
        """
        https://doc.qt.io/qt-6/q3dscene.html#activeCamera-prop

        **activeCamera : Q3DCamera***

        This property holds the currently active camera in the 3D scene.

        When a new **Q3DCamera**  object is set, it is automatically added as
        child of the scene.

        **Access functions:**

        Q3DCamera * **activeCamera** () const
        void **setActiveCamera**
        (Q3DCamera * **camera** )

        **Notifier signal:**

        void **activeCameraChanged** (Q3DCamera * **camera** )
        """
        ...
    def setActiveLight(self, light: PySide6.QtDataVisualization.Q3DLight) -> None:
        """
        https://doc.qt.io/qt-6/q3dscene.html#activeLight-prop

        **activeLight : Q3DLight***

        This property holds the currently active light in the 3D scene.

        When a new **Q3DLight**  objects is set, it is automatically added as
        child of the scene.

        **Access functions:**

        Q3DLight * **activeLight** () const
        void **setActiveLight** (Q3DLight
        * **light** )

        **Notifier signal:**

        void **activeLightChanged** (Q3DLight * **light** )
        """
        ...
    def setDevicePixelRatio(self, pixelRatio: float) -> None:
        """
        https://doc.qt.io/qt-6/q3dscene.html#devicePixelRatio-prop

        **devicePixelRatio : float**

        This property holds the device pixel ratio that is used when mapping
        input coordinates to pixel coordinates.

        **Access functions:**

        float **devicePixelRatio** () const
        void **setDevicePixelRatio**
        (float **pixelRatio** )

        **Notifier signal:**

        void **devicePixelRatioChanged** (float **pixelRatio** )
        """
        ...
    def setGraphPositionQuery(self, point: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/q3dscene.html#graphPositionQuery-prop

        **graphPositionQuery : QPoint**

        This property holds the coordinates for the user input that should be
        processed by the scene as a graph position query.

        If this property is set to a value other than **invalidSelectionPoint**
        (), the graph tries to match a graph position to the specified
        coordinates within the primary viewport. After the rendering pass, this
        property is returned to its default state of **invalidSelectionPoint**
        (). The queried graph position can be read from the
        **QAbstract3DGraph::queriedGraphPosition**  property after the next
        render pass.

        There is no single correct 3D coordinate to match a particular screen
        position, so to be consistent, the queries are always done against the
        inner sides of an invisible box surrounding the graph.

        **Note:** Bar graphs allow graph position queries only at the graph
        floor level.

        **Access functions:**

        QPoint **graphPositionQuery** () const
        void **setGraphPositionQuery**
        (const QPoint & **point** )

        **Notifier signal:**

        void **graphPositionQueryChanged** (const QPoint & **position** )

        **See also** **QAbstract3DGraph::queriedGraphPosition** .
        """
        ...
    def setPrimarySubViewport(self, primarySubViewport: PySide6.QtCore.QRect) -> None:
        """
        https://doc.qt.io/qt-6/q3dscene.html#primarySubViewport-prop

        **primarySubViewport : QRect**

        This property holds the current subviewport rectangle inside the
        viewport where the primary view of the data visualization is targeted.

        If **isSlicingActive** () is `false`, the primary sub viewport is equal
        to **viewport** (). If **isSlicingActive** () is `true` and the primary
        sub viewport has not been explicitly set, it will be one fifth of
        **viewport** ().

        **Note:** Setting primarySubViewport larger than or outside of the
        viewport resizes the viewport accordingly.

        **Access functions:**

        QRect **primarySubViewport** () const
        void **setPrimarySubViewport**
        (const QRect & **primarySubViewport** )

        **Notifier signal:**

        void **primarySubViewportChanged** (const QRect & **subViewport** )
        """
        ...
    def setSecondarySubViewport(self, secondarySubViewport: PySide6.QtCore.QRect) -> None:
        """
        https://doc.qt.io/qt-6/q3dscene.html#secondarySubViewport-prop

        **secondarySubViewport : QRect**

        This property holds the secondary viewport rectangle inside the
        viewport.

        The secondary viewport is used for drawing the 2D slice view in some
        visualizations. If it has not been explicitly set, it will be equal to
        **QRect** . If **isSlicingActive** () is `true`, it will be equal to
        **viewport** .

        **Note:** If the secondary sub viewport is larger than or outside of the
        viewport, the viewport is resized accordingly.

        **Access functions:**

        QRect **secondarySubViewport** () const
        void
        **setSecondarySubViewport** (const QRect & **secondarySubViewport** )

        **Notifier signal:**

        void **secondarySubViewportChanged** (const QRect & **subViewport** )
        """
        ...
    def setSecondarySubviewOnTop(self, isSecondaryOnTop: bool) -> None:
        """
        https://doc.qt.io/qt-6/q3dscene.html#secondarySubviewOnTop-prop

        **secondarySubviewOnTop : bool**

        This property holds whether the 2D slicing view or the 3D view is drawn
        on top.

        **Access functions:**

        bool **isSecondarySubviewOnTop** () const
        void
        **setSecondarySubviewOnTop** (bool **isSecondaryOnTop** )

        **Notifier signal:**

        void **secondarySubviewOnTopChanged** (bool **isSecondaryOnTop** )
        """
        ...
    def setSelectionQueryPosition(self, point: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/q3dscene.html#selectionQueryPosition-prop

        **selectionQueryPosition : QPoint**

        This property holds the coordinates for the user input that should be
        processed by the scene as a selection.

        If this property is set to a value other than **invalidSelectionPoint**
        (), the graph tries to select a data item, axis label, or a custom item
        at the specified coordinates within the primary viewport. After the
        rendering pass, the property is returned to its default state of
        **invalidSelectionPoint** ().

        **Access functions:**

        QPoint **selectionQueryPosition** () const
        void
        **setSelectionQueryPosition** (const QPoint & **point** )

        **Notifier signal:**

        void **selectionQueryPositionChanged** (const QPoint & **position** )

        **See also** **QAbstract3DGraph::selectedElement** .
        """
        ...
    def setSlicingActive(self, isSlicing: bool) -> None:
        """
        https://doc.qt.io/qt-6/q3dscene.html#slicingActive-prop

        **slicingActive : bool**

        This property holds whether the 2D slicing view is currently active.

        If `true`, **QAbstract3DGraph::selectionMode**  must have either
        **QAbstract3DGraph::SelectionRow**  or
        **QAbstract3DGraph::SelectionColumn**  set to a valid selection.

        **Note:** Not all visualizations support the 2D slicing view.

        **Access functions:**

        bool **isSlicingActive** () const
        void **setSlicingActive** (bool
        **isSlicing** )

        **Notifier signal:**

        void **slicingActiveChanged** (bool **isSlicingActive** )
        """
        ...
    def viewport(self) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/q3dscene.html#viewport-prop

        **[read-only] viewport : const QRect**

        This property holds a read only property that contains the current
        viewport rectangle where all the 3D rendering is targeted.

        **Access functions:**

        QRect **viewport** () const

        **Notifier signal:**

        void **viewportChanged** (const QRect & **viewport** )

        **Member Function Documentation**
        """
        ...
    @property
    def activeCameraChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def activeLightChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def devicePixelRatioChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def graphPositionQueryChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def primarySubViewportChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def secondarySubViewportChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def secondarySubviewOnTopChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def selectionQueryPositionChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def slicingActiveChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def viewportChanged(self) -> PySide6.QtCore.SignalInstance: ...
