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
PySide6.QtDesigner, except for defaults which are replaced by "...".
"""
from __future__ import annotations

import PySide6.QtCore
import PySide6.QtDesigner
import PySide6.QtGui
import PySide6.QtWidgets

class QAbstractExtensionFactory:
    """
    https://doc.qt.io/qt-6/qabstractextensionfactory.html

    **Detailed Description**

    QAbstractExtensionFactory is not intended to be instantiated directly; use
    the **QExtensionFactory**  instead.

    In **Qt Designer** , extension factories are used to look up and create
    named extensions as they are required. For that reason, when implementing a
    custom extension, you must also create a **QExtensionFactory** , i.e a class
    that is able to make an instance of your extension, and register it using
    **Qt Designer** 's **extension manager** .

    When an extension is required, **Qt Designer** 's **extension manager**
    will run through all its registered factories calling
    **QExtensionFactory::createExtension** () for each until the first one that
    is able to create the requested extension for the selected object, is found.
    This factory will then make an instance of the extension.

    **See also** **QExtensionFactory**  and **QExtensionManager** .
    """

    def __init__(self) -> None: ...
    def extension(
        self, object: PySide6.QtCore.QObject, iid: str
    ) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qabstractextensionfactory.html#extension

        **[pure virtual] QObject *QAbstractExtensionFactory::extension(QObject *
        object , const QString & iid ) const**

        Returns the extension specified by **iid** for the given **object**.
        """
        ...
