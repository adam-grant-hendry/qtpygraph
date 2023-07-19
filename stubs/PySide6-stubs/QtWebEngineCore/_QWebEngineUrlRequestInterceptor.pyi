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
PySide6.QtWebEngineCore, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtNetwork
import PySide6.QtWebChannel
import PySide6.QtWebEngineCore

class QWebEngineUrlRequestInterceptor(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qwebengineurlrequestinterceptor.html

    **Detailed Description**

    Implementing the **QWebEngineUrlRequestInterceptor**  interface and
    installing the interceptor on the profile enables intercepting, blocking,
    and modifying URL requests before they reach the networking stack of
    Chromium.

    You can install the interceptor on a profile via
    **QWebEngineProfile::setUrlRequestInterceptor** () or
    **QQuickWebEngineProfile::setUrlRequestInterceptor** ().

    When using the **Qt WebEngine Widgets Module** ,
    **QWebEnginePage::acceptNavigationRequest** () offers further options to
    accept or block requests.

    **See also** **interceptRequest** () and **QWebEngineUrlRequestInfo** .
    """

    def __init__(self, p: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineurlrequestinterceptor.html#QWebEngineUr
        lRequestInterceptor-1

        **QWebEngineUrlRequestInterceptor::QWebEngineUrlRequestInterceptor(QObje
        ct * p = nullptr)**

        Creates a new QWebEngineUrlRequestInterceptor object with **p** as
        parent.
        """
        ...
    def interceptRequest(
        self, info: PySide6.QtWebEngineCore.QWebEngineUrlRequestInfo
    ) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineurlrequestinterceptor.html#interceptReq
        uest

        **[pure virtual] void QWebEngineUrlRequestInterceptor::interceptRequest(
        QWebEngineUrlRequestInfo & info )**

        Reimplementing this virtual function makes it possible to intercept URL
        requests. This method will be stalling the URL request until handled.

        **info** contains the information about the URL request and will track
        internally whether its members have been altered.

        **Warning:** All method calls to the profile on the main thread will
        block until execution of this function is finished.
        """
        ...