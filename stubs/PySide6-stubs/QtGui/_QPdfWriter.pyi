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

class QPdfWriter(PySide6.QtCore.QObject, PySide6.QtGui.QPagedPaintDevice):
    """
    https://doc.qt.io/qt-6/qpdfwriter.html

    **Detailed Description**

    QPdfWriter generates PDF out of a series of drawing commands using
    **QPainter** . The **newPage** () method can be used to create several
    pages.
    """

    @overload
    def __init__(self, device: PySide6.QtCore.QIODevice) -> None:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#QPdfWriter

        **QPdfWriter::QPdfWriter(const QString & filename )**

        Constructs a PDF writer that will write the pdf to **filename**.
        """
        ...
    @overload
    def __init__(self, filename: str) -> None:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#QPdfWriter-1

        **QPdfWriter::QPdfWriter(QIODevice * device )**

        Constructs a PDF writer that will write the pdf to **device**.
        """
        ...
    def addFileAttachment(
        self,
        fileName: str,
        data: PySide6.QtCore.QByteArray | bytes,
        mimeType: str = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#addFileAttachment

        **[since 5.15] void QPdfWriter::addFileAttachment(const QString &
        fileName , const QByteArray & data , const QString & mimeType =
        QString())**

        Adds **fileName** attachment to the PDF with (optional) **mimeType**.
        **data** contains the raw file data to embed into the PDF file.

        This function was introduced in Qt 5.15.
        """
        ...
    def creator(self) -> str:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#creator

        **QString QPdfWriter::creator() const**

        Returns the creator of the document.

        **See also** **setCreator** ().
        """
        ...
    def documentXmpMetadata(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#documentXmpMetadata

        **[since 5.15] QByteArray QPdfWriter::documentXmpMetadata() const**

        Gets the document metadata, as it was provided with a call to
        **setDocumentXmpMetadata** . It will not return the default metadata.

        This function was introduced in Qt 5.15.

        **See also** **setDocumentXmpMetadata** ().
        """
        ...
    def metric(self, id: PySide6.QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def newPage(self) -> bool:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#newPage

        **[override virtual] bool QPdfWriter::newPage()**

        Reimplements: **QPagedPaintDevice::newPage** ().
        """
        ...
    def paintEngine(self) -> PySide6.QtGui.QPaintEngine:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#paintEngine

        **[override virtual protected] QPaintEngine *QPdfWriter::paintEngine()
        const**

        Reimplements: **QPaintDevice::paintEngine() const** .
        """
        ...
    def pdfVersion(self) -> PySide6.QtGui.QPagedPaintDevice.PdfVersion:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#pdfVersion

        **[since 5.10] QPagedPaintDevice::PdfVersion QPdfWriter::pdfVersion()
        const**

        Returns the PDF version for this writer. The default is
        `PdfVersion_1_4`.

        This function was introduced in Qt 5.10.

        **See also** **setPdfVersion** ().
        """
        ...
    def resolution(self) -> int:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#resolution

        **[since 5.3] int QPdfWriter::resolution() const**

        Returns the resolution of the PDF in DPI.

        This function was introduced in Qt 5.3.

        **See also** **setResolution** ().
        """
        ...
    def setCreator(self, creator: str) -> None:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#setCreator

        **void QPdfWriter::setCreator(const QString & creator )**

        Sets the creator of the document to **creator**.

        **See also** **creator** ().
        """
        ...
    def setDocumentXmpMetadata(
        self, xmpMetadata: PySide6.QtCore.QByteArray | bytes
    ) -> None:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#setDocumentXmpMetadata

        **[since 5.15] void QPdfWriter::setDocumentXmpMetadata(const QByteArray
        & xmpMetadata )**

        Sets the document metadata. This metadata is not influenced by the
        **setTitle**  / **setCreator**  methods, so is up to the user to keep it
        consistent. **xmpMetadata** contains XML formatted metadata to embed
        into the PDF file.

        This function was introduced in Qt 5.15.

        **See also** **documentXmpMetadata** ().
        """
        ...
    def setPdfVersion(self, version: PySide6.QtGui.QPagedPaintDevice.PdfVersion) -> None:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#setPdfVersion

        **[since 5.10] void
        QPdfWriter::setPdfVersion(QPagedPaintDevice::PdfVersion version )**

        Sets the PDF version for this writer to **version**.

        If **version** is the same value as currently set then no change will be
        made.

        This function was introduced in Qt 5.10.

        **See also** **pdfVersion** ().
        """
        ...
    def setResolution(self, resolution: int) -> None:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#setResolution

        **[since 5.3] void QPdfWriter::setResolution(int resolution )**

        Sets the PDF **resolution** in DPI.

        This setting affects the coordinate system as returned by, for example
        **QPainter::viewport** ().

        This function was introduced in Qt 5.3.

        **See also** **resolution** ().
        """
        ...
    def setTitle(self, title: str) -> None:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#setTitle

        **void QPdfWriter::setTitle(const QString & title )**

        Sets the title of the document being created to **title**.

        **See also** **title** ().
        """
        ...
    def title(self) -> str:
        """
        https://doc.qt.io/qt-6/qpdfwriter.html#title

        **QString QPdfWriter::title() const**

        Returns the title of the document.

        **See also** **setTitle** ().
        """
        ...
