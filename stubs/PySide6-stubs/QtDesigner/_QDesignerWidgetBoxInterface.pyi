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

from collections.abc import Sequence
from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtDesigner
import PySide6.QtGui
import PySide6.QtWidgets

class QDesignerWidgetBoxInterface(PySide6.QtWidgets.QWidget):
    """
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html

    **Detailed Description**

    QDesignerWidgetBoxInterface contains a collection of functions that is
    typically used to manipulate the contents of **Qt Designer** 's widget box.

    **Qt Designer** uses an XML file to populate its widget box. The name of
    that file is one of the widget box's properties, and you can retrieve it
    using the **fileName** () function.

    QDesignerWidgetBoxInterface also provides the **save** () function that
    saves the contents of the widget box in the file specified by the widget
    box's file name property. If you have made changes to the widget box, for
    example by dropping a widget into the widget box, without calling the
    **save** () function, the original content can be restored by a simple
    invocation of the **load** () function:

    **QDesignerWidgetBoxInterface**  *widgetBox = 0:
                widgetBox =
    formEditor->widgetBox();

                widgetBox->load();

    The QDesignerWidgetBoxInterface class is not intended to be instantiated
    directly. You can retrieve an interface to Qt Designer's widget box using
    the **QDesignerFormEditorInterface::widgetBox** () function. A pointer to
    **Qt Designer** 's current **QDesignerFormEditorInterface**  object
    (`formEditor` in the example above) is provided by the
    **QDesignerCustomWidgetInterface::initialize** () function's parameter. When
    implementing a custom widget plugin, you must subclass the
    **QDesignerCustomWidgetInterface**  to expose your plugin to **Qt
    Designer**.

    If you want to save your changes, and at the same time preserve the original
    contents, you can use the **save** () function combined with the
    **setFileName** () function to save your changes into another file. Remember
    to store the name of the original file first:

    **QString**  originalFile = widgetBox->fileName();
    widgetBox->setFileName("myWidgetBox.xml");
                widgetBox->save();

    Then you can restore the original contents of the widget box by resetting
    the file name to the original file and calling **load** ():

    widgetBox->setFileName(originalFile);
                widgetBox->load();

    In a similar way, you can later use your customized XML file:

    if (widgetBox->filename() != "myWidgetBox.xml") {
    widgetBox->setFileName("myWidgetBox.xml");
    widgetBox->load();
                }

    **See also** **QDesignerFormEditorInterface** .
    """

    class Category:
        Default: QDesignerWidgetBoxInterface.Category.Type = ...
        Scratchpad: QDesignerWidgetBoxInterface.Category.Type = ...

        class Type(IntFlag):
            Default: QDesignerWidgetBoxInterface.Category.Type = ...
            Scratchpad: QDesignerWidgetBoxInterface.Category.Type = ...
        @overload
        def __init__(
            self, Category: PySide6.QtDesigner.QDesignerWidgetBoxInterface.Category
        ) -> None: ...
        @overload
        def __init__(
            self,
            aname: str = ...,
            atype: PySide6.QtDesigner.QDesignerWidgetBoxInterface.Category.Type = ...,
        ) -> None: ...
        @staticmethod
        def __copy__() -> None: ...
        def addWidget(
            self, awidget: PySide6.QtDesigner.QDesignerWidgetBoxInterface.Widget
        ) -> None: ...
        def isNull(self) -> bool: ...
        def name(self) -> str: ...
        def removeWidget(self, idx: int) -> None: ...
        def setName(self, aname: str) -> None: ...
        def setType(
            self, atype: PySide6.QtDesigner.QDesignerWidgetBoxInterface.Category.Type
        ) -> None: ...
        def type(
            self,
        ) -> PySide6.QtDesigner.QDesignerWidgetBoxInterface.Category.Type: ...
        def widget(
            self, idx: int
        ) -> PySide6.QtDesigner.QDesignerWidgetBoxInterface.Widget: ...
        def widgetCount(self) -> int: ...

    class Widget:
        Default: QDesignerWidgetBoxInterface.Widget.Type = ...
        Custom: QDesignerWidgetBoxInterface.Widget.Type = ...

        class Type(IntFlag):
            Default: QDesignerWidgetBoxInterface.Widget.Type = ...
            Custom: QDesignerWidgetBoxInterface.Widget.Type = ...
        @overload
        def __init__(
            self,
            aname: str = ...,
            xml: str = ...,
            icon_name: str = ...,
            atype: PySide6.QtDesigner.QDesignerWidgetBoxInterface.Widget.Type = ...,
        ) -> None: ...
        @overload
        def __init__(
            self, w: PySide6.QtDesigner.QDesignerWidgetBoxInterface.Widget
        ) -> None: ...
        @staticmethod
        def __copy__() -> None: ...
        def domXml(self) -> str: ...
        def iconName(self) -> str: ...
        def isNull(self) -> bool: ...
        def name(self) -> str: ...
        def setDomXml(self, xml: str) -> None: ...
        def setIconName(self, icon_name: str) -> None: ...
        def setName(self, aname: str) -> None: ...
        def setType(
            self, atype: PySide6.QtDesigner.QDesignerWidgetBoxInterface.Widget.Type
        ) -> None: ...
        def type(self) -> PySide6.QtDesigner.QDesignerWidgetBoxInterface.Widget.Type: ...

    def __init__(
        self,
        parent: PySide6.QtWidgets.QWidget | None = ...,
        flags: PySide6.QtCore.Qt.WindowFlags = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#QDesignerWidgetB
        oxInterface

        **QDesignerWidgetBoxInterface::QDesignerWidgetBoxInterface(QWidget *
        parent = nullptr, Qt::WindowFlags flags = Qt::WindowFlags())**

        Constructs a widget box interface with the given **parent** and the
        specified window **flags**.
        """
        ...
    def addCategory(
        self, cat: PySide6.QtDesigner.QDesignerWidgetBoxInterface.Category
    ) -> None: ...
    def addWidget(
        self, cat_idx: int, wgt: PySide6.QtDesigner.QDesignerWidgetBoxInterface.Widget
    ) -> None: ...
    def category(
        self, cat_idx: int
    ) -> PySide6.QtDesigner.QDesignerWidgetBoxInterface.Category: ...
    def categoryCount(self) -> int: ...
    def dropWidgets(
        self,
        item_list: Sequence[PySide6.QtDesigner.QDesignerDnDItemInterface],
        global_mouse_pos: PySide6.QtCore.QPoint,
    ) -> None: ...
    def fileName(self) -> str:
        """
        https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#fileName

        **[pure virtual] QString QDesignerWidgetBoxInterface::fileName() const**

        Returns the name of the XML file **Qt Designer** is currently using to
        populate its widget box.

        **See also** **setFileName** ().
        """
        ...
    def findOrInsertCategory(self, categoryName: str) -> int: ...
    def load(self) -> bool:
        """
        https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#load

        **[pure virtual] bool QDesignerWidgetBoxInterface::load()**

        Populates **Qt Designer** 's widget box by loading (or reloading) the
        currently specified XML file. Returns true if the file is successfully
        loaded; otherwise false.

        **See also** **setFileName** ().
        """
        ...
    def removeCategory(self, cat_idx: int) -> None: ...
    def removeWidget(self, cat_idx: int, wgt_idx: int) -> None: ...
    def save(self) -> bool:
        """
        https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#save

        **[pure virtual] bool QDesignerWidgetBoxInterface::save()**

        Saves the contents of **Qt Designer** 's widget box in the file
        specified by the **fileName** () function. Returns true if the content
        is successfully saved; otherwise false.

        **See also** **fileName** () and **setFileName** ().
        """
        ...
    def setFileName(self, file_name: str) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#setFileName

        **[pure virtual] void QDesignerWidgetBoxInterface::setFileName(const
        QString & fileName )**

        Sets the XML file that **Qt Designer** will use to populate its widget
        box, to **fileName**. You must call **load** () to update the widget box
        with the new XML file.

        **See also** **fileName** () and **load** ().
        """
        ...
    def widget(
        self, cat_idx: int, wgt_idx: int
    ) -> PySide6.QtDesigner.QDesignerWidgetBoxInterface.Widget: ...
    def widgetCount(self, cat_idx: int) -> int: ...
