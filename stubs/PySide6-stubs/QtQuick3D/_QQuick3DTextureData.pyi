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
PySide6.QtQuick3D, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtQml
import PySide6.QtQuick3D

class QQuick3DTextureData(PySide6.QtQuick3D.QQuick3DObject):
    """
    https://doc.qt.io/qt-6/qquick3dtexturedata.html

    **Detailed Description**

    The QQuick3DTextureData class can be used to specify custom texture data for
    a **Texture**  in a Qt Quick 3D scene.

    While not strictly required, the typical usage is to inherit from this
    class. The subclass is then exposed to QML by registering it to the type
    system. The **textureData**  property of a **Texture**  can then be set to
    reference an instance of the registered type.

    Example implementation:

    class CustomTextureData : public QQuick3DTextureData
        {
            Q_OBJECT
    ... properties ...

        public:
            CustomTextureData() {
    regenerateTextureData(); }

            void setProperty(...)
            {
    // Change relevant internal data.
                // ...

                //
    Update the texture data
                regenerateTextureData();
    // Finally, trigger an update. This is relevant in case nothing else
    // is changed in the scene; this way we make sure a new frame will
    // be rendered
                update();
            }
        private:
            void
    regenerateTextureData()
            {
                **QByteArray**  textureData;
    textureData = generateTextureData();
    setTextureData(textureData);
                setSize(**QSize** (256, 256));
    setFormat(QQuick3DTextureData::Format::RGBA8)
    setHasTransparency(true);
            }
        };

    This class can then be registered as a QML type and used with **Texture** .

    In Qt 5 type registration happened with **qmlRegisterType** :

    qmlRegisterType<MyCustomTextureData>("Example", 1, 0,
    "MyCustomTextureData");

    In Qt 6 the default approach is to use automatic registration with the help
    of the build system. Instead of calling **qmlRegisterType** , the `.pro`
    file can now contain:

    CONFIG += qmltypes
        QML_IMPORT_NAME = Example
    QML_IMPORT_MAJOR_VERSION = 1

    With CMake, automatic registration is the default behavior, so no special
    settings are needed beyond basic QML module setup:

    qt_add_qml_module(application
            URI Example
            VERSION 1.0
        )

    The class implementation should add **QML_NAMED_ELEMENT** :

    class CustomTextureData : public QQuick3DTextureData
        {
            Q_OBJECT
    QML_NAMED_ELEMENT(MyCustomTextureData)
            ...
        };

    The QML code can then use the custom type:

    import Example 1.0

        Model {
            source: "#Cube"
    materials: [
                DefaultMaterial {
                    diffuseMap:
    diffuseMapCustomTexture
                }
            ]
            Texture {
    id: diffuseMapCustomTexture
                textureData: MyCustomTextureData { }
    }
        }
    """

    None_: QQuick3DTextureData.Format = ...
    RGBA8: QQuick3DTextureData.Format = ...
    RGBA16F: QQuick3DTextureData.Format = ...
    RGBA32F: QQuick3DTextureData.Format = ...
    RGBE8: QQuick3DTextureData.Format = ...
    R8: QQuick3DTextureData.Format = ...
    R16: QQuick3DTextureData.Format = ...
    R16F: QQuick3DTextureData.Format = ...
    R32F: QQuick3DTextureData.Format = ...
    BC1: QQuick3DTextureData.Format = ...
    BC2: QQuick3DTextureData.Format = ...
    BC3: QQuick3DTextureData.Format = ...
    BC4: QQuick3DTextureData.Format = ...
    BC5: QQuick3DTextureData.Format = ...
    BC6H: QQuick3DTextureData.Format = ...
    BC7: QQuick3DTextureData.Format = ...
    DXT1_RGBA: QQuick3DTextureData.Format = ...
    DXT1_RGB: QQuick3DTextureData.Format = ...
    DXT3_RGBA: QQuick3DTextureData.Format = ...
    DXT5_RGBA: QQuick3DTextureData.Format = ...
    ETC2_RGB8: QQuick3DTextureData.Format = ...
    ETC2_RGB8A1: QQuick3DTextureData.Format = ...
    ETC2_RGBA8: QQuick3DTextureData.Format = ...
    ASTC_4x4: QQuick3DTextureData.Format = ...
    ASTC_5x4: QQuick3DTextureData.Format = ...
    ASTC_5x5: QQuick3DTextureData.Format = ...
    ASTC_6x5: QQuick3DTextureData.Format = ...
    ASTC_6x6: QQuick3DTextureData.Format = ...
    ASTC_8x5: QQuick3DTextureData.Format = ...
    ASTC_8x6: QQuick3DTextureData.Format = ...
    ASTC_8x8: QQuick3DTextureData.Format = ...
    ASTC_10x5: QQuick3DTextureData.Format = ...
    ASTC_10x6: QQuick3DTextureData.Format = ...
    ASTC_10x8: QQuick3DTextureData.Format = ...
    ASTC_10x10: QQuick3DTextureData.Format = ...
    ASTC_12x10: QQuick3DTextureData.Format = ...
    ASTC_12x12: QQuick3DTextureData.Format = ...

    class Format(IntFlag):
        None_: QQuick3DTextureData.Format = ...
        RGBA8: QQuick3DTextureData.Format = ...
        RGBA16F: QQuick3DTextureData.Format = ...
        RGBA32F: QQuick3DTextureData.Format = ...
        RGBE8: QQuick3DTextureData.Format = ...
        R8: QQuick3DTextureData.Format = ...
        R16: QQuick3DTextureData.Format = ...
        R16F: QQuick3DTextureData.Format = ...
        R32F: QQuick3DTextureData.Format = ...
        BC1: QQuick3DTextureData.Format = ...
        BC2: QQuick3DTextureData.Format = ...
        BC3: QQuick3DTextureData.Format = ...
        BC4: QQuick3DTextureData.Format = ...
        BC5: QQuick3DTextureData.Format = ...
        BC6H: QQuick3DTextureData.Format = ...
        BC7: QQuick3DTextureData.Format = ...
        DXT1_RGBA: QQuick3DTextureData.Format = ...
        DXT1_RGB: QQuick3DTextureData.Format = ...
        DXT3_RGBA: QQuick3DTextureData.Format = ...
        DXT5_RGBA: QQuick3DTextureData.Format = ...
        ETC2_RGB8: QQuick3DTextureData.Format = ...
        ETC2_RGB8A1: QQuick3DTextureData.Format = ...
        ETC2_RGBA8: QQuick3DTextureData.Format = ...
        ASTC_4x4: QQuick3DTextureData.Format = ...
        ASTC_5x4: QQuick3DTextureData.Format = ...
        ASTC_5x5: QQuick3DTextureData.Format = ...
        ASTC_6x5: QQuick3DTextureData.Format = ...
        ASTC_6x6: QQuick3DTextureData.Format = ...
        ASTC_8x5: QQuick3DTextureData.Format = ...
        ASTC_8x6: QQuick3DTextureData.Format = ...
        ASTC_8x8: QQuick3DTextureData.Format = ...
        ASTC_10x5: QQuick3DTextureData.Format = ...
        ASTC_10x6: QQuick3DTextureData.Format = ...
        ASTC_10x8: QQuick3DTextureData.Format = ...
        ASTC_10x10: QQuick3DTextureData.Format = ...
        ASTC_12x10: QQuick3DTextureData.Format = ...
        ASTC_12x12: QQuick3DTextureData.Format = ...
    def __init__(self, parent: PySide6.QtQuick3D.QQuick3DObject | None = ...) -> None: ...
    def format(self) -> PySide6.QtQuick3D.QQuick3DTextureData.Format:
        """
        https://doc.qt.io/qt-6/qquick3dtexturedata.html#format

        **QQuick3DTextureData::Format QQuick3DTextureData::format() const**

        Returns the format of the texture data.

        **See also** **setFormat** ().
        """
        ...
    def hasTransparency(self) -> bool:
        """
        https://doc.qt.io/qt-6/qquick3dtexturedata.html#hasTransparency

        **bool QQuick3DTextureData::hasTransparency() const**

        Returns `true` if the texture data has transparency.

        The default value is `false`.

        **See also** **setHasTransparency** ().
        """
        ...
    def markAllDirty(self) -> None: ...
    def setFormat(self, format: PySide6.QtQuick3D.QQuick3DTextureData.Format) -> None:
        """
        https://doc.qt.io/qt-6/qquick3dtexturedata.html#setFormat

        **void QQuick3DTextureData::setFormat(QQuick3DTextureData::Format format
        )**

        Sets the **format** of the texture data.

        The default format is /c RGBA8

        **See also** **format** ().
        """
        ...
    def setHasTransparency(self, hasTransparency: bool) -> None:
        """
        https://doc.qt.io/qt-6/qquick3dtexturedata.html#setHasTransparency

        **void QQuick3DTextureData::setHasTransparency(bool hasTransparency )**

        Set **hasTransparency** to true if the texture data has an active alpha
        channel with non-opaque values.

        This is used as an optimization by the engine so that for formats that
        do support an alpha channel do not need to have each value checked for
        non-opaque values.

        **See also** **hasTransparency** ().
        """
        ...
    def setSize(self, size: PySide6.QtCore.QSize) -> None:
        """
        https://doc.qt.io/qt-6/qquick3dtexturedata.html#setSize

        **void QQuick3DTextureData::setSize(const QSize & size )**

        Sets the **size** of the texture data in pixels.

        **See also** **size** ().
        """
        ...
    def setTextureData(self, data: PySide6.QtCore.QByteArray | bytes) -> None:
        """
        https://doc.qt.io/qt-6/qquick3dtexturedata.html#setTextureData

        **void QQuick3DTextureData::setTextureData(const QByteArray & data )**

        Sets the texture data. The contents of **data** must respect the
        **size**  and **format**  properties as the backend will try and upload
        and use the data as if it were a texture of size and format, and if
        there is any deviation the result will be somewhere between incorrect
        rendering of the texture, or potentially a crash.

        **See also** **textureData** ().
        """
        ...
    def size(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qquick3dtexturedata.html#size

        **QSize QQuick3DTextureData::size() const**

        Returns the size of the texture data in pixels.

        **See also** **setSize** ().
        """
        ...
    def textureData(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qquick3dtexturedata.html#textureData

        **const QByteArray QQuick3DTextureData::textureData() const**

        Returns the current texture data defined by this item.

        **See also** **setTextureData** ().
        """
        ...