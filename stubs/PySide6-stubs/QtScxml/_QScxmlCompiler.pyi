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
PySide6.QtScxml, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtScxml

class QScxmlCompiler:
    """
    https://doc.qt.io/qt-6/qscxmlcompiler.html

    **Detailed Description**

    Parses an **SCXML**  file and dynamically instantiates a state machine for a
    successfully parsed SCXML file. If parsing fails, the new state machine
    cannot start. All errors are returned by **QScxmlStateMachine::parseErrors**
    ().

    To load an SCXML file, **QScxmlStateMachine::fromFile**  or
    **QScxmlStateMachine::fromData**  should be used. Using QScxmlCompiler
    directly is only needed when the compiler needs to use a custom
    **QScxmlCompiler::Loader** .
    """

    class Loader:
        def __init__(self) -> None: ...
        def load(
            self, name: str, baseDir: str
        ) -> tuple[PySide6.QtCore.QByteArray, list[str]]: ...

    def __init__(self, xmlReader: PySide6.QtCore.QXmlStreamReader) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlcompiler.html#QScxmlCompiler

        **QScxmlCompiler::QScxmlCompiler(QXmlStreamReader * reader )**

        Creates a new SCXML compiler for the specified **reader**.
        """
        ...
    def compile(self) -> PySide6.QtScxml.QScxmlStateMachine:
        """
        https://doc.qt.io/qt-6/qscxmlcompiler.html#compile

        **QScxmlStateMachine *QScxmlCompiler::compile()**

        Parses an SCXML file and creates a new state machine from it.

        If parsing is successful, the returned state machine can be initialized
        and started. If parsing fails, **QScxmlStateMachine::parseErrors** ()
        can be used to retrieve a list of errors.
        """
        ...
    def errors(self) -> list[PySide6.QtScxml.QScxmlError]:
        """
        https://doc.qt.io/qt-6/qscxmlcompiler.html#errors

        **QList<QScxmlError> QScxmlCompiler::errors() const**

        Returns the list of parse errors.
        """
        ...
    def fileName(self) -> str:
        """
        https://doc.qt.io/qt-6/qscxmlcompiler.html#fileName

        **QString QScxmlCompiler::fileName() const**

        Returns the file name associated with the current input.

        **See also** **setFileName** ().
        """
        ...
    def loader(self) -> PySide6.QtScxml.QScxmlCompiler.Loader:
        """
        https://doc.qt.io/qt-6/qscxmlcompiler.html#loader

        **QScxmlCompiler::Loader *QScxmlCompiler::loader() const**

        Returns the loader that is currently used to resolve and load URIs for
        the SCXML compiler.

        **See also** **setLoader** ().
        """
        ...
    def setFileName(self, fileName: str) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlcompiler.html#setFileName

        **void QScxmlCompiler::setFileName(const QString & fileName )**

        Sets the file name for the current input to **fileName**.

        The file name is used for error reporting and for resolving relative
        path URIs.

        **See also** **fileName** ().
        """
        ...
    def setLoader(self, newLoader: PySide6.QtScxml.QScxmlCompiler.Loader) -> None:
        """
        https://doc.qt.io/qt-6/qscxmlcompiler.html#setLoader

        **void QScxmlCompiler::setLoader(QScxmlCompiler::Loader * newLoader )**

        Sets **newLoader** to be used for resolving and loading URIs for the
        SCXML compiler.

        **See also** **loader** ().
        """
        ...