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

import PySide6.QtCore
import PySide6.QtRemoteObjects

class QRemoteObjectRegistryHost(PySide6.QtRemoteObjects.QRemoteObjectHostBase):
    """
    https://doc.qt.io/qt-6/qremoteobjectregistryhost.html

    **Detailed Description**

    The QRemoteObjectRegistryHost class provides an entry point to a
    **QtRemoteObjects**  network. A network can be as simple as two Nodes, or an
    arbitrarily complex set of processes and devices.

    A QRemoteObjectRegistryHost has the same capability that a
    **QRemoteObjectHost**  has (which includes everything a
    **QRemoteObjectNode**  supports), and in addition is the owner of the
    Registry. Any **QRemoteObjectHost**  node that connects to this Node will
    have all of their Source objects made available by the Registry.

    Nodes only support connection to one **registry** , calling
    **QRemoteObjectNode::setRegistryUrl**  when a Registry is already set is
    considered an error. For something like a secure and insecure network (where
    different Registries would be applicable), the recommendation is to create
    separate Nodes to connect to each, in effect creating two independent Qt
    Remote Objects networks.

    Nodes may connect to each other directly using **connectToNode** , or they
    can use the **QRemoteObjectRegistry**  to simplify connections.

    The **QRemoteObjectRegistry**  is a special Replica available to every Node
    that connects to the Registry Url. It knows how to connect to every
    QRemoteObjectSource object on the network.

    **See also** **QRemoteObjectNode**  and **QRemoteObjectHost** .
    """

    def __init__(
        self,
        registryAddress: PySide6.QtCore.QUrl | str = ...,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qremoteobjectregistryhost.html#QRemoteObjectRegis
        tryHost

        **QRemoteObjectRegistryHost::QRemoteObjectRegistryHost(const QUrl &
        registryAddress = QUrl(), QObject * parent = nullptr)**

        Constructs a new QRemoteObjectRegistryHost Node with the given
        **parent**. RegistryHost Nodes have the same functionality as
        **QRemoteObjectHost**  Nodes, except rather than being able to connect
        to a **QRemoteObjectRegistry** , the provided Host **QUrl**  (
        **registryAddress** ) becomes the address of the registry for other
        Nodes to connect to.
        """
        ...
    def setRegistryUrl(self, registryUrl: PySide6.QtCore.QUrl | str) -> bool:
        """
        https://doc.qt.io/qt-6/qremoteobjectregistryhost.html#setRegistryUrl

        **[override virtual] bool
        QRemoteObjectRegistryHost::setRegistryUrl(const QUrl & registryUrl )**

        Reimplements an access function for property:
        **QRemoteObjectNode::registryUrl** .

        This method can be used to set the address of this Node to
        **registryUrl** (used for other Nodes to connect to this one), if the
        **QUrl**  isn't set in the constructor. Since this Node becomes the
        Registry, calling this setter method causes this Node to use the url as
        the host address. All other Node's use the
        **QRemoteObjectNode::setRegistryUrl**  method initiate a connection to
        the Registry.

        Returns `true` if the registry address is set, otherwise `false`.

        **See also** **QRemoteObjectRegistryHost** () and
        **QRemoteObjectNode::setRegistryUrl** .
        """
        ...