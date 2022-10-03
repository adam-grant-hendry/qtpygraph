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

class QWebEngineRegisterProtocolHandlerRequest:
    """
    https://doc.qt.io/qt-6/qwebengineregisterprotocolhandlerrequest.html

    **Detailed Description**

    **See also** **QWebEnginePage::registerProtocolHandlerRequested** ().
    """

    def __init__(self) -> None: ...
    def accept(self) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineregisterprotocolhandlerrequest.html#acc
        ept

        **[invokable] void QWebEngineRegisterProtocolHandlerRequest::accept()**

        Accepts the request

        Subsequent calls to accept() and **reject** () are ignored.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def origin(self) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qwebengineregisterprotocolhandlerrequest.html#ori
        gin-prop

        **[read-only] origin : const QUrl**

        This property holds the URL template for the protocol handler.

        This is the second parameter from the **registerProtocolHandler**  call.

        **Access functions:**

        QUrl **origin** () const
        """
        ...
    def reject(self) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineregisterprotocolhandlerrequest.html#rej
        ect

        **[invokable] void QWebEngineRegisterProtocolHandlerRequest::reject()**

        Rejects the request.

        Subsequent calls to **accept** () and reject() are ignored.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def scheme(self) -> str:
        """
        https://doc.qt.io/qt-6/qwebengineregisterprotocolhandlerrequest.html#sch
        eme-prop

        **[read-only] scheme : const QString**

        This property holds the URL scheme for the protocol handler.

        This is the first parameter from the **registerProtocolHandler**  call.

        **Access functions:**

        QString **scheme** () const

        **Member Function Documentation**
        """
        ...