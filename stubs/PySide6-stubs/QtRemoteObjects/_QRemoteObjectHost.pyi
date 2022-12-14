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
PySide6.QtRemoteObjects, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore
import PySide6.QtRemoteObjects

class QRemoteObjectHost(PySide6.QtRemoteObjects.QRemoteObjectHostBase):
    """
    https://doc.qt.io/qt-6/qremoteobjecthost.html

    **Detailed Description**

    The QRemoteObjectHost class provides an entry point to a **QtRemoteObjects**
    network. A network can be as simple as two nodes, or an arbitrarily complex
    set of processes and devices.

    QRemoteObjectHosts have the same capabilities as QRemoteObjectNodes, but
    they can also be connected to and can share source objects on the network.

    Nodes may connect to each other directly using **connectToNode** , or they
    can use the **QRemoteObjectRegistry**  to simplify connections.

    The **QRemoteObjectRegistry**  is a special replica available to every node
    that connects to the registry Url. It knows how to connect to every
    QRemoteObjectSource object on the network.

    **See also** **QRemoteObjectNode**  and **QRemoteObjectRegistryHost** .
    """

    @overload
    def __init__(
        self, address: PySide6.QtCore.QUrl | str, parent: PySide6.QtCore.QObject
    ) -> None:
        """
        https://doc.qt.io/qt-6/qremoteobjecthost.html#QRemoteObjectHost

        **QRemoteObjectHost::QRemoteObjectHost(QObject * parent = nullptr)**

        Constructs a new QRemoteObjectHost Node (i.e., a Node that supports
        exposing **Source**  objects on the QtRO network) with the given
        **parent**. This constructor is meant specific to support QML in the
        future as it will not be available to connect to until **setHostUrl**
        is called.

        **See also** **setHostUrl** () and **setRegistryUrl** ().
        """
        ...
    @overload
    def __init__(
        self,
        address: PySide6.QtCore.QUrl | str,
        registryAddress: PySide6.QtCore.QUrl | str = ...,
        allowedSchemas: PySide6.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas = ...,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qremoteobjecthost.html#QRemoteObjectHost-1

        **QRemoteObjectHost::QRemoteObjectHost(const QUrl & address , const QUrl
        & registryAddress = QUrl(), QRemoteObjectHostBase::AllowedSchemas
        allowedSchemas = BuiltInSchemasOnly, QObject * parent = nullptr)**

        Constructs a new QRemoteObjectHost Node (i.e., a Node that supports
        exposing **Source**  objects on the QtRO network) with address
        **address**. If set, **registryAddress** will be used to connect to the
        **QRemoteObjectRegistry**  at the provided address. The
        **allowedSchemas** parameter is only needed (and should be set to
        **AllowExternalRegistration** ) if the schema of the url should be used
        as an **External Schema**  by the registry.

        **See also** **setHostUrl** () and **setRegistryUrl** ().
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qremoteobjecthost.html#QRemoteObjectHost-2

        **QRemoteObjectHost::QRemoteObjectHost(const QUrl & address , QObject *
        parent )**

        Constructs a new QRemoteObjectHost Node (i.e., a Node that supports
        exposing **Source**  objects on the QtRO network) with a url of
        **address** and the given **parent**. This overload is provided as a
        convenience for specifying a **QObject**  parent without providing a
        registry address.

        **See also** **setHostUrl** () and **setRegistryUrl** ().
        """
        ...
    def hostUrl(self) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qremoteobjecthost.html#hostUrl

        **[override virtual] QUrl QRemoteObjectHost::hostUrl() const**

        Returns the host address for the **QRemoteObjectNode**  as a **QUrl** .
        If the Node is not a Host node, returns an empty **QUrl** .

        **Note:** Getter function for property hostUrl.

        **See also** **setHostUrl** ().
        """
        ...
    def setHostUrl(
        self,
        hostAddress: PySide6.QtCore.QUrl | str,
        allowedSchemas: PySide6.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas = ...,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qremoteobjecthost.html#setHostUrl

        **[override virtual] bool QRemoteObjectHost::setHostUrl(const QUrl &
        hostAddress , QRemoteObjectHostBase::AllowedSchemas allowedSchemas =
        BuiltInSchemasOnly)**

        Sets the **hostAddress** for a host **QRemoteObjectNode** .

        Returns `true` if the Host address is set, otherwise `false`.

        The **allowedSchemas** parameter is only needed (and should be set to
        **AllowExternalRegistration** ) if the schema of the url should be used
        as an **External Schema**  by the registry.

        **Note:** Setter function for property **hostUrl** .

        **See also** **hostUrl** ().
        """
        ...
    @property
    def hostUrlChanged(self) -> PySide6.QtCore.SignalInstance: ...
