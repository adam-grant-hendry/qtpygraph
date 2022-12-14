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

class QExtensionFactory(
    PySide6.QtCore.QObject, PySide6.QtDesigner.QAbstractExtensionFactory
):
    """
    https://doc.qt.io/qt-6/qextensionfactory.html

    **Detailed Description**

    In **Qt Designer** the extensions are not created until they are required.
    For that reason, when implementing a custom extension, you must also create
    a QExtensionFactory, i.e. a class that is able to make an instance of your
    extension, and register it using **Qt Designer** 's **extension manager** .

    The **QExtensionManager**  class provides extension management facilities
    for Qt Designer. When an extension is required, Qt Designer's **extension
    manager**  will run through all its registered factories calling
    **QExtensionFactory::createExtension** () for each until the first one that
    is able to create a requested extension for the selected object, is found.
    This factory will then make an instance of the extension.

    There are four available types of extensions in Qt Designer:
    **QDesignerContainerExtension**  , **QDesignerMemberSheetExtension** ,
    **QDesignerPropertySheetExtension**  and **QDesignerTaskMenuExtension** . Qt
    Designer's behavior is the same whether the requested extension is
    associated with a multi page container, a member sheet, a property sheet or
    a task menu.

    You can either create a new QExtensionFactory and reimplement the
    **QExtensionFactory::createExtension** () function. For example:

    **QObject**  *ANewExtensionFactory::createExtension(**QObject**  *object,
    const **QString**  &iid, **QObject**  *parent) const
                {
    if (iid != Q_TYPEID(**QDesignerContainerExtension** ))
    return 0;

                    if (MyCustomWidget *widget =
    qobject_cast<MyCustomWidget*>
                           (object))
    return new MyContainerExtension(widget, parent);

                    return
    0;
                }

    Or you can use an existing factory, expanding the
    **QExtensionFactory::createExtension** () function to make the factory able
    to create your extension as well. For example:

    **QObject**  *AGeneralExtensionFactory::createExtension(**QObject**
    *object,
                        const **QString**  &iid, **QObject**  *parent)
    const
                {
                    MyCustomWidget *widget =
    qobject_cast<MyCustomWidget*>(object);

                    if (widget &&
    (iid == Q_TYPEID(**QDesignerTaskMenuExtension** ))) {
    return new MyTaskMenuExtension(widget, parent);

                    } else
    if (widget && (iid == Q_TYPEID(**QDesignerContainerExtension** ))) {
    return new MyContainerExtension(widget, parent);

                    } else
    {
                        return 0;
                    }
                }

    For a complete example using the QExtensionFactory class, see the **Task
    Menu Extension example** . The example shows how to create a custom widget
    plugin for Qt Designer, and how to to use the **QDesignerTaskMenuExtension**
    class to add custom items to Qt Designer's task menu.

    **See also** **QExtensionManager**  and **QAbstractExtensionFactory** .
    """

    def __init__(self, parent: PySide6.QtDesigner.QExtensionManager | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qextensionfactory.html#QExtensionFactory

        **QExtensionFactory::QExtensionFactory(QExtensionManager * parent =
        nullptr)**

        Constructs an extension factory with the given **parent**.
        """
        ...
    def createExtension(
        self, object: PySide6.QtCore.QObject, iid: str, parent: PySide6.QtCore.QObject
    ) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qextensionfactory.html#createExtension

        **[virtual protected] QObject
        *QExtensionFactory::createExtension(QObject * object , const QString &
        iid , QObject * parent ) const**

        Creates an extension specified by **iid** for the given **object**. The
        extension object is created as a child of the specified **parent**.

        **See also** **extension** ().
        """
        ...
    def extension(
        self, object: PySide6.QtCore.QObject, iid: str
    ) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qextensionfactory.html#extension

        **[override virtual] QObject *QExtensionFactory::extension(QObject *
        object , const QString & iid ) const**

        Reimplements: **QAbstractExtensionFactory::extension(QObject *object,
        const QString &iid) const** .

        Returns the extension specified by **iid** for the given **object**.

        **See also** **createExtension** ().
        """
        ...
    def extensionManager(self) -> PySide6.QtDesigner.QExtensionManager:
        """
        https://doc.qt.io/qt-6/qextensionfactory.html#extensionManager

        **QExtensionManager *QExtensionFactory::extensionManager() const**

        Returns the extension manager for the extension factory.
        """
        ...
