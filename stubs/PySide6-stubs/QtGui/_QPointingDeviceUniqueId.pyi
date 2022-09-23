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
PySide6.QtGui, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore
import PySide6.QtGui

class QPointingDeviceUniqueId:
    """
    https://doc.qt.io/qt-6/qpointingdeviceuniqueid.html

    **Detailed Description**

    QPointingDeviceUniqueIds can be compared for equality, and can be used as
    keys in a **QHash** . You get access to the numerical ID via **numericId**
    (), if the device supports such IDs. For future extensions, though, you
    should not use that function, but compare objects of this type using the
    equality operator.

    This class is a thin wrapper around an integer ID. You pass it into and out
    of functions by value.

    **See also** **QEventPoint** .
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qpointingdeviceuniqueid.html#QPointingDeviceUniqu
        eId

        **QPointingDeviceUniqueId::QPointingDeviceUniqueId()**

        Constructs an invalid unique pointer ID.
        """
        ...
    @overload
    def __init__(
        self, QPointingDeviceUniqueId: PySide6.QtGui.QPointingDeviceUniqueId
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpointingdeviceuniqueid.html#QPointingDeviceUniqu
        eId

        **QPointingDeviceUniqueId::QPointingDeviceUniqueId()**

        Constructs an invalid unique pointer ID.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    @staticmethod
    def fromNumericId(id: int) -> PySide6.QtGui.QPointingDeviceUniqueId:
        """
        https://doc.qt.io/qt-6/qpointingdeviceuniqueid.html#fromNumericId

        **[static] QPointingDeviceUniqueId
        QPointingDeviceUniqueId::fromNumericId(qint64 id )**

        Constructs a unique pointer ID from numeric ID **id**.
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qpointingdeviceuniqueid.html#isValid

        **bool QPointingDeviceUniqueId::isValid() const**

        Returns whether this unique pointer ID is valid, that is, it represents
        an actual pointer.
        """
        ...
    def numericId(self) -> int:
        """
        https://doc.qt.io/qt-6/qpointingdeviceuniqueid.html#numericId-prop

        **[read-only] numericId : const qint64**

        This property holds the numeric unique ID of the token represented by a
        touchpoint

        If the device provides a numeric ID, **isValid** () returns true, and
        this property provides the numeric ID; otherwise it is -1.

        You should not use the value of this property in portable code, but
        instead rely on equality to identify pointers.

        **Access functions:**

        qint64 **numericId** () const

        **See also** **isValid** ().

        **Member Function Documentation**
        """
        ...
