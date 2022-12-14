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

class QSGDynamicTexture(PySide6.QtQuick.QSGTexture):
    """
    https://doc.qt.io/qt-6/qsgdynamictexture.html

    **Detailed Description**

    To update the content of the texture, call **updateTexture** () explicitly.

    **Note:** All classes with QSG prefix should be used solely on the scene
    graph's rendering thread. See **Scene Graph and Rendering**  for more
    information.
    """

    def __init__(self) -> None: ...
    def updateTexture(self) -> bool:
        """
        https://doc.qt.io/qt-6/qsgdynamictexture.html#updateTexture

        **[pure virtual] bool QSGDynamicTexture::updateTexture()**

        Call this function to explicitly update the dynamic texture.

        The function returns true if the texture was changed as a resul of the
        update; otherwise returns false.

        **Note:** This function is typically called from
        **QQuickItem::updatePaintNode** () or **QSGNode::preprocess** (),
        meaning during the `synchronization` or the `node preprocessing` phases
        of the scenegraph. Calling it at other times is discouraged and can lead
        to unexpected behavior.
        """
        ...
