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
PySide6.QtAxContainer, except for defaults which are replaced by "...".
"""
from __future__ import annotations

import PySide6.QtAxContainer
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QAxBaseObject(PySide6.QtCore.QObject, PySide6.QtAxContainer.QAxObjectInterface):
    """
    https://doc.qt.io/qt-6/qaxbaseobject.html

    **Detailed Description**
    """

    ...

    @property
    def exception(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qaxbaseobject.html#exception

        **[signal] void QAxBaseObject::exception(int code , const QString &
        source , const QString & desc , const QString & help )**

        This signal is emitted when the COM object throws an exception while
        called using the OLE automation interface IDispatch. **code** ,
        **source** , **desc** and **help** provide information about the
        exception as provided by the COM server and can be used to provide
        useful feedback to the end user. **help** includes the help file, and
        the help context ID in brackets, e.g. "filename [id]".

        **See also** **QAxBaseWidget::exception** ().
        """
        ...
    @property
    def propertyChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qaxbaseobject.html#propertyChanged

        **[signal] void QAxBaseObject::propertyChanged(const QString & name )**

        If the COM object supports property notification, this signal gets
        emitted when the property called **name** is changed.

        **See also** **QAxBaseWidget::propertyChanged** ().
        """
        ...
    @property
    def signal(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qaxbaseobject.html#signal

        **[signal] void QAxBaseObject::signal(const QString & name , int argc ,
        void * argv )**

        This generic signal gets emitted when the COM object issues the event
        **name**. **argc** is the number of parameters provided by the event
        (DISPPARAMS.cArgs), and **argv** is the pointer to the parameter values
        (DISPPARAMS.rgvarg). Note that the order of parameter values is turned
        around, ie. the last element of the array is the first parameter in the
        function.

        **See also** **QAxBaseWidget::signal** ().
        """
        ...
