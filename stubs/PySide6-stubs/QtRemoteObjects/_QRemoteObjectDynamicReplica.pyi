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

class QRemoteObjectDynamicReplica(PySide6.QtRemoteObjects.QRemoteObjectReplica):
    """
    https://doc.qt.io/qt-6/qremoteobjectdynamicreplica.html

    **Detailed Description**

    There are generated replicas (replicas having the header files produced by
    the **Replica Compiler** ), and dynamic replicas, that are generated on-the-
    fly. This is the class for the dynamic type of replica.

    When the connection to the **Source**  object is made, the initialization
    step passes the current property values (see **Replica Initialization** ).
    In a DynamicReplica, the property/signal/slot details are also sent,
    allowing the replica object to be created on-the-fly. This can be convenient
    in QML or scripting, but has two primary disadvantages. First, the object is
    in effect "empty" until it is successfully initialized by the **Source** .
    Second, in C++, calls must be made using **QMetaObject::invokeMethod** (),
    as the moc generated lookup will not be available.

    This class does not have a public constructor. It can only be instantiated
    by using the dynamic **QRemoteObjectNode::acquire**  method.
    """

    ...
