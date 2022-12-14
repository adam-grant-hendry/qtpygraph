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

import PySide6.QtCore
import PySide6.QtGui

class QTextBlockGroup(PySide6.QtGui.QTextObject):
    """
    https://doc.qt.io/qt-6/qtextblockgroup.html

    **Detailed Description**

    Block groups can be used to organize blocks of text within a document. They
    maintain an up-to-date list of the text blocks that belong to them, even
    when text blocks are being edited.

    Each group has a parent document which is specified when the group is
    constructed.

    Text blocks can be inserted into a group with **blockInserted** (), and
    removed with **blockRemoved** (). If a block's format is changed,
    **blockFormatChanged** () is called.

    The list of blocks in the group is returned by **blockList** (). Note that
    the blocks in the list are not necessarily adjacent elements in the
    document; for example, the top-level items in a multi-level list will be
    separated by the items in lower levels of the list.

    **See also** **QTextBlock**  and **QTextDocument** .
    """

    def __init__(self, doc: PySide6.QtGui.QTextDocument) -> None:
        """
        https://doc.qt.io/qt-6/qtextblockgroup.html#QTextBlockGroup

        **[protected] QTextBlockGroup::QTextBlockGroup(QTextDocument * document
        )**

        Creates a new new block group for the given **document**.

        **Warning:** This function should only be called from
        **QTextDocument::createObject** ().
        """
        ...
    def blockFormatChanged(self, block: PySide6.QtGui.QTextBlock) -> None:
        """
        https://doc.qt.io/qt-6/qtextblockgroup.html#blockFormatChanged

        **[virtual protected] void QTextBlockGroup::blockFormatChanged(const
        QTextBlock & block )**

        This function is called whenever the specified **block** of text is
        changed. The text block is a member of this group.

        The base class implementation does nothing.
        """
        ...
    def blockInserted(self, block: PySide6.QtGui.QTextBlock) -> None:
        """
        https://doc.qt.io/qt-6/qtextblockgroup.html#blockInserted

        **[virtual protected] void QTextBlockGroup::blockInserted(const
        QTextBlock & block )**

        Appends the given **block** to the end of the group.

        **Warning:** If you reimplement this function you must call the base
        class implementation.
        """
        ...
    def blockList(self) -> list[PySide6.QtGui.QTextBlock]:
        """
        https://doc.qt.io/qt-6/qtextblockgroup.html#blockList

        **[protected] QList<QTextBlock> QTextBlockGroup::blockList() const**

        Returns a (possibly empty) list of all the blocks that are part of the
        block group.
        """
        ...
    def blockRemoved(self, block: PySide6.QtGui.QTextBlock) -> None:
        """
        https://doc.qt.io/qt-6/qtextblockgroup.html#blockRemoved

        **[virtual protected] void QTextBlockGroup::blockRemoved(const
        QTextBlock & block )**

        Removes the given **block** from the group; the block itself is not
        deleted, it simply isn't a member of this group anymore.
        """
        ...
