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
PySide6.QtQml, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag

import PySide6.QtCore
import PySide6.QtNetwork
import PySide6.QtQml

class QQmlAbstractUrlInterceptor:
    """
    https://doc.qt.io/qt-6/qqmlabstracturlinterceptor.html

    **Detailed Description**

    QQmlAbstractUrlInterceptor is an interface which can be used to alter URLs
    before they are used by the QML engine. This is primarily useful for
    altering file urls into other file urls, such as selecting different
    graphical assets for the current platform.

    Relative URLs are intercepted after being resolved against the file path of
    the current QML context. URL interception also occurs after setting the base
    path for a loaded QML file. This means that the content loaded for that QML
    file uses the intercepted URL, but inside the file the pre-intercepted URL
    is used for resolving relative paths. This allows for interception of .qml
    file loading without needing all paths (or local types) inside intercepted
    content to insert a different relative path.

    Compared to setNetworkAccessManagerFactory, QQmlAbstractUrlInterceptor
    affects all URLs and paths, including local files and embedded resource
    files. QQmlAbstractUrlInterceptor is synchronous, and for asynchronous files
    must return a url with an asynchronous scheme (such as http or a custom
    scheme handled by your own custom QNetworkAccessManager). You can use a
    QQmlAbstractUrlInterceptor to change file URLs into networked URLs which are
    handled by your own custom QNetworkAccessManager.

    To implement support for a custom networked scheme, see
    setNetworkAccessManagerFactory.
    """

    QmlFile: QQmlAbstractUrlInterceptor.DataType = ...
    JavaScriptFile: QQmlAbstractUrlInterceptor.DataType = ...
    QmldirFile: QQmlAbstractUrlInterceptor.DataType = ...
    UrlString: QQmlAbstractUrlInterceptor.DataType = ...

    class DataType(IntFlag):
        QmlFile: QQmlAbstractUrlInterceptor.DataType = ...
        JavaScriptFile: QQmlAbstractUrlInterceptor.DataType = ...
        QmldirFile: QQmlAbstractUrlInterceptor.DataType = ...
        UrlString: QQmlAbstractUrlInterceptor.DataType = ...
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qqmlabstracturlinterceptor.html#QQmlAbstractUrlIn
        terceptor

        **QQmlAbstractUrlInterceptor::QQmlAbstractUrlInterceptor()**

        Constructor for QQmlAbstractUrlInterceptor.
        """
        ...
    def intercept(
        self,
        path: PySide6.QtCore.QUrl | str,
        type: PySide6.QtQml.QQmlAbstractUrlInterceptor.DataType,
    ) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qqmlabstracturlinterceptor.html#intercept

        **[pure virtual] QUrl QQmlAbstractUrlInterceptor::intercept(const QUrl &
        url , QQmlAbstractUrlInterceptor::DataType type )**

        A pure virtual function where you can intercept the **url**. The
        returned value is taken as the new value for the url. The type of url
        being intercepted is given by the **type** variable.

        Your implementation of this function must be thread-safe, as it can be
        called from multiple threads at the same time.
        """
        ...
