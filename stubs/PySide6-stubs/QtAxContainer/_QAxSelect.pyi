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

from enum import IntFlag

import PySide6.QtAxContainer
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QAxSelect(PySide6.QtWidgets.QDialog):
    """
    https://doc.qt.io/qt-6/qaxselect.html

    **Detailed Description**

    QAxSelect dialog can be used to provide users with a way to browse the
    registered COM components of the system and select one. It also provides a
    combo box for selecting desired sandboxing level. The CLSID of the selected
    component can then be used in the application to e.g. initialize a
    **QAxWidget** :

    **QAxSelect**  select;
        if (select.exec()) {
            **QAxWidget**
    *container = new **QAxWidget** ;
    container->setControl(select.clsid());
            container->show();
        }

    **See also** **QAxWidget**  and **ActiveQt Framework** .
    """

    SandboxingNone: QAxSelect.SandboxingLevel = ...
    SandboxingProcess: QAxSelect.SandboxingLevel = ...
    SandboxingLowIntegrity: QAxSelect.SandboxingLevel = ...

    class SandboxingLevel(IntFlag):
        SandboxingNone: QAxSelect.SandboxingLevel = ...
        SandboxingProcess: QAxSelect.SandboxingLevel = ...
        SandboxingLowIntegrity: QAxSelect.SandboxingLevel = ...
    def __init__(
        self,
        parent: PySide6.QtWidgets.QWidget | None = ...,
        flags: PySide6.QtCore.Qt.WindowFlags = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qaxselect.html#QAxSelect

        **QAxSelect::QAxSelect(QWidget * parent = nullptr, Qt::WindowFlags flags
        = Qt::WindowFlags())**

        Constructs a QAxSelect object. Dialog parent widget and window flags can
        be optionally specified with **parent** and **flags** parameters,
        respectively.
        """
        ...
    def clsid(self) -> str:
        """
        https://doc.qt.io/qt-6/qaxselect.html#clsid

        **QString QAxSelect::clsid() const**

        Returns the CLSID of the selected COM component.
        """
        ...
    def sandboxingLevel(self) -> PySide6.QtAxContainer.QAxSelect.SandboxingLevel:
        """
        https://doc.qt.io/qt-6/qaxselect.html#sandboxingLevel

        **[since 5.13] QAxSelect::SandboxingLevel QAxSelect::sandboxingLevel()
        const**

        Returns the desired level of sandboxing for the ActiveX control.

        This function was introduced in Qt 5.13.
        """
        ...
