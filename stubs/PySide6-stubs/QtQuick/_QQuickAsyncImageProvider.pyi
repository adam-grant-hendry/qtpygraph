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

class QQuickAsyncImageProvider(PySide6.QtQuick.QQuickImageProvider):
    """
    https://doc.qt.io/qt-6/qquickasyncimageprovider.html

    **Detailed Description**

    See the **Image Response Provider Example**  for a complete implementation.

    **See also** **QQuickImageProvider** .
    """

    def __init__(self) -> None: ...
    def requestImageResponse(
        self, id: str, requestedSize: PySide6.QtCore.QSize
    ) -> PySide6.QtQuick.QQuickImageResponse:
        """
        https://doc.qt.io/qt-6/qquickasyncimageprovider.html#requestImageRespons
        e

        **[pure virtual] QQuickImageResponse
        *QQuickAsyncImageProvider::requestImageResponse(const QString & id ,
        const QSize & requestedSize )**

        Implement this method to return the job that will provide the texture
        with **id**.

        The **id** is the requested image source, with the "image:" scheme and
        provider identifier removed. For example, if the image **source**  was
        "image://myprovider/icons/home", the given **id** would be "icons/home".

        The **requestedSize** corresponds to the **Image::sourceSize**
        requested by an Image item. If **requestedSize** is a valid size, the
        image returned should be of that size.

        **Note:** this method may be called by multiple threads, so ensure the
        implementation of this method is reentrant.
        """
        ...
