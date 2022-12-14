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

from enum import IntFlag

import PySide6.QtCore
import PySide6.QtGui

class QPagedPaintDevice(PySide6.QtGui.QPaintDevice):
    """
    https://doc.qt.io/qt-6/qpagedpaintdevice.html

    **Detailed Description**

    Paged paint devices are used to generate output for printing or for formats
    like PDF. **QPdfWriter**  and **QPrinter**  inherit from it.
    """

    PdfVersion_1_4: QPagedPaintDevice.PdfVersion = ...
    PdfVersion_A1b: QPagedPaintDevice.PdfVersion = ...
    PdfVersion_1_6: QPagedPaintDevice.PdfVersion = ...

    class PdfVersion(IntFlag):
        PdfVersion_1_4: QPagedPaintDevice.PdfVersion = ...
        PdfVersion_A1b: QPagedPaintDevice.PdfVersion = ...
        PdfVersion_1_6: QPagedPaintDevice.PdfVersion = ...
    def newPage(self) -> bool:
        """
        https://doc.qt.io/qt-6/qpagedpaintdevice.html#newPage

        **[pure virtual] bool QPagedPaintDevice::newPage()**

        Starts a new page. Returns `true` on success.
        """
        ...
    def pageLayout(self) -> PySide6.QtGui.QPageLayout:
        """
        https://doc.qt.io/qt-6/qpagedpaintdevice.html#pageLayout

        **[since 5.3] QPageLayout QPagedPaintDevice::pageLayout() const**

        Returns the current page layout. Use this method to access the current
        **QPageSize** , **QPageLayout::Orientation** , **QMarginsF** ,
        fullRect() and paintRect().

        Note that you cannot use the setters on the returned object, you must
        either call the individual **QPagedPaintDevice**  setters or use
        **setPageLayout** ().

        This function was introduced in Qt 5.3.

        **See also** **setPageLayout** (), **setPageSize** (),
        **setPageOrientation** (), and **setPageMargins** ().
        """
        ...
    def pageRanges(self) -> PySide6.QtGui.QPageRanges:
        """
        https://doc.qt.io/qt-6/qpagedpaintdevice.html#pageRanges

        **[since 6.0] QPageRanges QPagedPaintDevice::pageRanges() const**

        Returns the page ranges associated with this device.

        This function was introduced in Qt 6.0.

        **See also** **setPageRanges** (), **QPageRanges** ,
        **QPrinter::fromPage** (), and **QPrinter::toPage** ().
        """
        ...
    def setPageLayout(self, pageLayout: PySide6.QtGui.QPageLayout) -> bool:
        """
        https://doc.qt.io/qt-6/qpagedpaintdevice.html#setPageLayout

        **[virtual, since 5.3] bool QPagedPaintDevice::setPageLayout(const
        QPageLayout & newPageLayout )**

        Sets the page layout to **newPageLayout**.

        You should call this before calling **QPainter::begin** (), or
        immediately before calling **newPage** () to apply the new page layout
        to a new page. You should not call any painting methods between a call
        to setPageLayout() and **newPage** () as the wrong paint metrics may be
        used.

        Returns true if the page layout was successfully set to
        **newPageLayout**.

        This function was introduced in Qt 5.3.

        **See also** **pageLayout** ().
        """
        ...
    def setPageMargins(
        self,
        margins: PySide6.QtCore.QMarginsF | PySide6.QtCore.QMargins,
        units: PySide6.QtGui.QPageLayout.Unit = ...,
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qpagedpaintdevice.html#setPageMargins

        **[virtual, since 5.3] bool QPagedPaintDevice::setPageMargins(const
        QMarginsF & margins , QPageLayout::Unit units =
        QPageLayout::Millimeter)**

        Set the page **margins** defined in the given **units**.

        You should call this before calling **QPainter::begin** (), or
        immediately before calling **newPage** () to apply the new margins to a
        new page. You should not call any painting methods between a call to
        setPageMargins() and **newPage** () as the wrong paint metrics may be
        used.

        To get the current page margins use **pageLayout** ().margins().

        Returns true if the page margins were successfully set to **margins**.

        This function was introduced in Qt 5.3.

        **See also** **pageLayout** ().
        """
        ...
    def setPageOrientation(
        self, orientation: PySide6.QtGui.QPageLayout.Orientation
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qpagedpaintdevice.html#setPageOrientation

        **[virtual, since 5.3] bool
        QPagedPaintDevice::setPageOrientation(QPageLayout::Orientation
        orientation )**

        Sets the page **orientation**.

        The page orientation is used to define the orientation of the page size
        when obtaining the page rect.

        You should call this before calling **QPainter::begin** (), or
        immediately before calling **newPage** () to apply the new orientation
        to a new page. You should not call any painting methods between a call
        to setPageOrientation() and **newPage** () as the wrong paint metrics
        may be used.

        To get the current **QPageLayout::Orientation**  use **pageLayout**
        ().orientation().

        Returns true if the page orientation was successfully set to
        **orientation**.

        This function was introduced in Qt 5.3.

        **See also** **pageLayout** ().
        """
        ...
    def setPageRanges(self, ranges: PySide6.QtGui.QPageRanges) -> None:
        """
        https://doc.qt.io/qt-6/qpagedpaintdevice.html#setPageRanges

        **[virtual, since 6.0] void QPagedPaintDevice::setPageRanges(const
        QPageRanges & ranges )**

        Sets the page ranges for this device to **ranges**.

        This function was introduced in Qt 6.0.

        **See also** **pageRanges** ().
        """
        ...
    def setPageSize(
        self,
        pageSize: (
            PySide6.QtGui.QPageSize
            | PySide6.QtGui.QPageSize.PageSizeId
            | PySide6.QtCore.QSize
        ),
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qpagedpaintdevice.html#setPageSize

        **[virtual, since 5.3] bool QPagedPaintDevice::setPageSize(const
        QPageSize & pageSize )**

        Sets the page size to **pageSize**.

        To get the current **QPageSize**  use **pageLayout** ().pageSize().

        You should call this before calling **QPainter::begin** (), or
        immediately before calling **newPage** () to apply the new page size to
        a new page. You should not call any painting methods between a call to
        setPageSize() and **newPage** () as the wrong paint metrics may be used.

        Returns true if the page size was successfully set to **pageSize**.

        This function was introduced in Qt 5.3.

        **See also** **pageLayout** ().
        """
        ...
