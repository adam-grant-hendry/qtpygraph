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
PySide6.QtXml, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import overload

import PySide6.QtCore
import PySide6.QtXml

class QDomProcessingInstruction(PySide6.QtXml.QDomNode):
    """
    https://doc.qt.io/qt-6/qdomprocessinginstruction.html

    **Detailed Description**

    Processing instructions are used in XML to keep processor-specific
    information in the text of the document.

    The XML declaration that appears at the top of an XML document, typically
    `<?xml version='1.0' encoding='UTF-8'?>`, is treated by QDom as a processing
    instruction. This is unfortunate, since the XML declaration is not a
    processing instruction; among other differences, it cannot be inserted into
    a document anywhere but on the first line.

    Do not use this function to create an xml declaration, since although it has
    the same syntax as a processing instruction, it isn't, and might not be
    treated by QDom as such.

    The content of the processing instruction is retrieved with **data** () and
    set with **setData** (). The processing instruction's target is retrieved
    with **target** ().

    For further information about the Document Object Model see **Level 1**  and
    **Level 2 Core** . For a more general introduction of the DOM implementation
    see the **QDomDocument**  documentation.
    """

    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qdomprocessinginstruction.html#QDomProcessingInst
        ruction

        **QDomProcessingInstruction::QDomProcessingInstruction()**

        Constructs an empty processing instruction. Use
        **QDomDocument::createProcessingInstruction** () to create a processing
        instruction with content.
        """
        ...
    @overload
    def __init__(self, x: PySide6.QtXml.QDomProcessingInstruction) -> None:
        """
        https://doc.qt.io/qt-6/qdomprocessinginstruction.html#QDomProcessingInst
        ruction-1

        **QDomProcessingInstruction::QDomProcessingInstruction(const
        QDomProcessingInstruction & x )**

        Constructs a copy of **x**.

        The data of the copy is shared (shallow copy): modifying one node will
        also change the other. If you want to make a deep copy, use
        **cloneNode** ().
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def data(self) -> str:
        """
        https://doc.qt.io/qt-6/qdomprocessinginstruction.html#data

        **QString QDomProcessingInstruction::data() const**

        Returns the content of this processing instruction.

        **See also** **setData** () and **target** ().
        """
        ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType:
        """
        https://doc.qt.io/qt-6/qdomprocessinginstruction.html#nodeType

        **QDomNode::NodeType QDomProcessingInstruction::nodeType() const**

        Returns `ProcessingInstructionNode`.
        """
        ...
    def setData(self, d: str) -> None:
        """
        https://doc.qt.io/qt-6/qdomprocessinginstruction.html#setData

        **void QDomProcessingInstruction::setData(const QString & d )**

        Sets the data contained in the processing instruction to **d**.

        **See also** **data** ().
        """
        ...
    def target(self) -> str:
        """
        https://doc.qt.io/qt-6/qdomprocessinginstruction.html#target

        **QString QDomProcessingInstruction::target() const**

        Returns the target of this processing instruction.

        **See also** **data** ().
        """
        ...
