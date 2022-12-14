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
PySide6.QtWebSockets, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag

class QWebSocketProtocol:
    """
    https://doc.qt.io/qt-6/qwebsocketprotocol.html

    **Detailed Description**
    """

    CloseCodeNormal: QWebSocketProtocol.CloseCode = ...
    CloseCodeGoingAway: QWebSocketProtocol.CloseCode = ...
    CloseCodeProtocolError: QWebSocketProtocol.CloseCode = ...
    CloseCodeDatatypeNotSupported: QWebSocketProtocol.CloseCode = ...
    CloseCodeReserved1004: QWebSocketProtocol.CloseCode = ...
    CloseCodeMissingStatusCode: QWebSocketProtocol.CloseCode = ...
    CloseCodeAbnormalDisconnection: QWebSocketProtocol.CloseCode = ...
    CloseCodeWrongDatatype: QWebSocketProtocol.CloseCode = ...
    CloseCodePolicyViolated: QWebSocketProtocol.CloseCode = ...
    CloseCodeTooMuchData: QWebSocketProtocol.CloseCode = ...
    CloseCodeMissingExtension: QWebSocketProtocol.CloseCode = ...
    CloseCodeBadOperation: QWebSocketProtocol.CloseCode = ...
    CloseCodeTlsHandshakeFailed: QWebSocketProtocol.CloseCode = ...
    VersionUnknown: QWebSocketProtocol.Version = ...
    Version0: QWebSocketProtocol.Version = ...
    Version4: QWebSocketProtocol.Version = ...
    Version5: QWebSocketProtocol.Version = ...
    Version6: QWebSocketProtocol.Version = ...
    Version7: QWebSocketProtocol.Version = ...
    Version8: QWebSocketProtocol.Version = ...
    Version13: QWebSocketProtocol.Version = ...
    VersionLatest: QWebSocketProtocol.Version = ...

    class CloseCode(IntFlag):
        CloseCodeNormal: QWebSocketProtocol.CloseCode = ...
        CloseCodeGoingAway: QWebSocketProtocol.CloseCode = ...
        CloseCodeProtocolError: QWebSocketProtocol.CloseCode = ...
        CloseCodeDatatypeNotSupported: QWebSocketProtocol.CloseCode = ...
        CloseCodeReserved1004: QWebSocketProtocol.CloseCode = ...
        CloseCodeMissingStatusCode: QWebSocketProtocol.CloseCode = ...
        CloseCodeAbnormalDisconnection: QWebSocketProtocol.CloseCode = ...
        CloseCodeWrongDatatype: QWebSocketProtocol.CloseCode = ...
        CloseCodePolicyViolated: QWebSocketProtocol.CloseCode = ...
        CloseCodeTooMuchData: QWebSocketProtocol.CloseCode = ...
        CloseCodeMissingExtension: QWebSocketProtocol.CloseCode = ...
        CloseCodeBadOperation: QWebSocketProtocol.CloseCode = ...
        CloseCodeTlsHandshakeFailed: QWebSocketProtocol.CloseCode = ...

    class Version(IntFlag):
        VersionUnknown: QWebSocketProtocol.Version = ...
        Version0: QWebSocketProtocol.Version = ...
        Version4: QWebSocketProtocol.Version = ...
        Version5: QWebSocketProtocol.Version = ...
        Version6: QWebSocketProtocol.Version = ...
        Version7: QWebSocketProtocol.Version = ...
        Version8: QWebSocketProtocol.Version = ...
        Version13: QWebSocketProtocol.Version = ...
        VersionLatest: QWebSocketProtocol.Version = ...
