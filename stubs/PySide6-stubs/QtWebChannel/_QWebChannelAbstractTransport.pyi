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
PySide6.QtWebChannel, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtWebChannel

class QWebChannelAbstractTransport(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qwebchannelabstracttransport.html

    **Detailed Description**

    Users of the **QWebChannel**  must implement this interface and connect
    instances of it to the **QWebChannel**  server for every client that should
    be connected to the **QWebChannel** . The **Qt WebChannel Standalone
    Example**  shows how this can be done using **Qt WebSockets** .

    **Note:** The JSON message protocol is considered internal and might change
    over time.

    **See also** **Qt WebChannel Standalone Example** .
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qwebchannelabstracttransport.html#QWebChannelAbst
        ractTransport

        **QWebChannelAbstractTransport::QWebChannelAbstractTransport(QObject *
        parent = nullptr)**

        Constructs a transport object with the given **parent**.
        """
        ...
    def sendMessage(self, message: dict[str, PySide6.QtCore.QJsonValue]) -> None:
        """
        https://doc.qt.io/qt-6/qwebchannelabstracttransport.html#sendMessage

        **[pure virtual slot] void
        QWebChannelAbstractTransport::sendMessage(const QJsonObject & message
        )**

        Sends a JSON **message** to the remote client. An implementation would
        serialize the message and transmit it to the remote JavaScript client.
        """
        ...
    @property
    def messageReceived(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qwebchannelabstracttransport.html#messageReceived

        **[signal] void QWebChannelAbstractTransport::messageReceived(const
        QJsonObject & message , QWebChannelAbstractTransport * transport )**

        This signal must be emitted when a new JSON **message** was received
        from the remote client. The **transport** argument should be set to this
        transport object.
        """
        ...
