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

from enum import IntFlag

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtOpenGL
import PySide6.QtQml
import PySide6.QtQuick

class QSGMaterial:
    """
    https://doc.qt.io/qt-6/qsgmaterial.html

    **Detailed Description**

    QSGMaterial and **QSGMaterialShader**  subclasses form a tight relationship.
    For one scene graph (including nested graphs), there is one unique
    **QSGMaterialShader**  instance which encapsulates the shaders the scene
    graph uses to render that material, such as a shader to flat coloring of
    geometry. Each **QSGGeometryNode**  can have a unique QSGMaterial containing
    the how the shader should be configured when drawing that node, such as the
    actual color to used to render the geometry.

    QSGMaterial has two virtual functions that both need to be implemented. The
    function **type** () should return a unique instance for all instances of a
    specific subclass. The **createShader** () function should return a new
    instance of **QSGMaterialShader** , specific to that subclass of
    QSGMaterial.

    A minimal QSGMaterial implementation could look like this:

    class Material : public QSGMaterial
        {
        public:
    **QSGMaterialType**  *type() const override { static **QSGMaterialType**
    type; return &type; }
            **QSGMaterialShader**
    *createShader(**QSGRendererInterface** ::RenderMode) const override { return
    new Shader; }
        };

    See the **Custom Material example**  for an introduction on implementing a
    **QQuickItem**  subclass backed by a **QSGGeometryNode**  and a custom
    material.

    **Note:****createShader** () is called only once per **QSGMaterialType** ,
    to reduce redundant work with shader preparation. If a QSGMaterial is backed
    by multiple sets of vertex and fragment shader combinations, the
    implementation of **type** () must return a different, unique
    **QSGMaterialType**  pointer for each combination of shaders.

    **Note:** All classes with QSG prefix should be used solely on the scene
    graph's rendering thread. See **Scene Graph and Rendering**  for more
    information.

    **See also** **QSGMaterialShader** , **Scene Graph - Custom Material** ,
    **Scene Graph - Two Texture Providers** , and **Scene Graph - Graph** .
    """

    Blending: QSGMaterial.Flag = ...
    RequiresDeterminant: QSGMaterial.Flag = ...
    RequiresFullMatrixExceptTranslate: QSGMaterial.Flag = ...
    RequiresFullMatrix: QSGMaterial.Flag = ...
    CustomCompileStep: QSGMaterial.Flag = ...

    class Flag(IntFlag):
        Blending: QSGMaterial.Flag = ...
        RequiresDeterminant: QSGMaterial.Flag = ...
        RequiresFullMatrixExceptTranslate: QSGMaterial.Flag = ...
        RequiresFullMatrix: QSGMaterial.Flag = ...
        CustomCompileStep: QSGMaterial.Flag = ...

    class Flags: ...

    def __init__(self) -> None: ...
    def compare(self, other: PySide6.QtQuick.QSGMaterial) -> int:
        """
        https://doc.qt.io/qt-6/qsgmaterial.html#compare

        **[virtual] int QSGMaterial::compare(const QSGMaterial * other ) const**

        Compares this material to **other** and returns 0 if they are equal; -1
        if this material should sort before **other** and 1 if **other** should
        sort before.

        The scene graph can reorder geometry nodes to minimize state changes.
        The compare function is called during the sorting process so that the
        materials can be sorted to minimize state changes in each call to
        QSGMaterialShader::updateState().

        The this pointer and **other** is guaranteed to have the same **type**
        ().
        """
        ...
    def createShader(
        self, renderMode: PySide6.QtQuick.QSGRendererInterface.RenderMode
    ) -> PySide6.QtQuick.QSGMaterialShader:
        """
        https://doc.qt.io/qt-6/qsgmaterial.html#createShader

        **[pure virtual] QSGMaterialShader
        *QSGMaterial::createShader(QSGRendererInterface::RenderMode renderMode )
        const**

        This function returns a new instance of a the **QSGMaterialShader**
        implementation used to render geometry for a specific implementation of
        **QSGMaterial** .

        The function will be called only once for each combination of material
        type and **renderMode** and will be cached internally.

        For most materials, the **renderMode** can be ignored. A few materials
        may need custom handling for specific render modes. For instance if the
        material implements antialiasing in a way that needs to account for
        perspective transformations when RenderMode3D is in use.
        """
        ...
    def flags(self) -> PySide6.QtQuick.QSGMaterial.Flags:
        """
        https://doc.qt.io/qt-6/qsgmaterial.html#flags

        **QSGMaterial::Flags QSGMaterial::flags() const**

        Returns the material's flags.
        """
        ...
    def setFlag(self, flags: PySide6.QtQuick.QSGMaterial.Flags, on: bool = ...) -> None:
        """
        https://doc.qt.io/qt-6/qsgmaterial.html#setFlag

        **void QSGMaterial::setFlag(QSGMaterial::Flags flags , bool on = true)**

        Sets the flags **flags** on this material if **on** is true; otherwise
        clears the attribute.
        """
        ...
    def type(self) -> PySide6.QtQuick.QSGMaterialType:
        """
        https://doc.qt.io/qt-6/qsgmaterial.html#type

        **[pure virtual] QSGMaterialType *QSGMaterial::type() const**

        This function is called by the scene graph to query an identifier that
        is unique to the **QSGMaterialShader**  instantiated by **createShader**
        ().

        For many materials, the typical approach will be to return a pointer to
        a static, and so globally available, **QSGMaterialType**  instance. The
        **QSGMaterialType**  is an opaque object. Its purpose is only to serve
        as a type-safe, simple way to generate unique material identifiers.

        **QSGMaterialType**  *type() const override
            {
                static
        **QSGMaterialType**  type;
                return &type;
            }
        """
        ...
