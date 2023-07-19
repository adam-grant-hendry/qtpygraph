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

from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtOpenGL
import PySide6.QtQml
import PySide6.QtQuick

class QQuickItemGrabResult(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qquickitemgrabresult.html

    **Detailed Description**

    **See also** **QQuickItem::grabToImage** ().
    """

    def event(self, arg__1: PySide6.QtCore.QEvent) -> bool: ...
    def image(self) -> PySide6.QtGui.QImage:
        """
        https://doc.qt.io/qt-6/qquickitemgrabresult.html#image-prop

        **[read-only] image : const QImage**

        This property holds the pixel results from a grab.

        If the grab is not yet complete or if it failed, a null image is
        returned (`image.isNull()` will return `true`).

        **Access functions:**

        QImage **image** () const
        """
        ...
    @overload
    def saveToFile(self, fileName: str) -> bool:
        """
        https://doc.qt.io/qt-6/qquickitemgrabresult.html#saveToFile

        **[invokable] bool QQuickItemGrabResult::saveToFile(const QString &
        fileName ) const**

        Saves the grab result as an image to **fileName**. Returns `true` if
        successful; otherwise returns `false`.

        **Note:** In Qt versions prior to 5.9, this function is marked as
        non-`const`.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    @overload
    def saveToFile(self, fileName: PySide6.QtCore.QUrl | str) -> bool:
        """
        https://doc.qt.io/qt-6/qquickitemgrabresult.html#saveToFile-1

        **[invokable, since 6.2] bool QQuickItemGrabResult::saveToFile(const
        QUrl & filePath ) const**

        Saves the grab result as an image to **filePath** , which must refer to
        a **local file name**  with a **supported image format**  extension.
        Returns `true` if successful; otherwise returns `false`.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 6.2.
        """
        ...
    def url(self) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qquickitemgrabresult.html#url-prop

        **[read-only] url : const QUrl**

        This property holds a URL which can be used in conjunction with URL
        based image consumers, such as the QtQuick::Image type.

        The URL is valid until the **QQuickItemGrabResult**  object is deleted.

        The URL does not represent a valid file or location to read it from, it
        is primarily a key to access images through Qt Quick's image-based
        types.

        **Access functions:**

        QUrl **url** () const

        **Member Function Documentation**
        """
        ...
    @property
    def ready(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qquickitemgrabresult.html#ready

        **[signal] void QQuickItemGrabResult::ready()**

        This signal is emitted when the grab has completed.
        """
        ...