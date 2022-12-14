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
PySide6.QtHelp, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtHelp
import PySide6.QtWidgets

class QHelpContentWidget(PySide6.QtWidgets.QTreeView):
    """
    https://doc.qt.io/qt-6/qhelpcontentwidget.html

    **Detailed Description**
    """

    def indexOf(self, link: PySide6.QtCore.QUrl | str) -> PySide6.QtCore.QModelIndex:
        """
        https://doc.qt.io/qt-6/qhelpcontentwidget.html#indexOf

        **QModelIndex QHelpContentWidget::indexOf(const QUrl & link )**

        Returns the index of the content item with the **link**. An invalid
        index is returned if no such an item exists.
        """
        ...
    @property
    def linkActivated(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qhelpcontentwidget.html#linkActivated

        **[signal] void QHelpContentWidget::linkActivated(const QUrl & link )**

        This signal is emitted when a content item is activated and its
        associated **link** should be shown.
        """
        ...
