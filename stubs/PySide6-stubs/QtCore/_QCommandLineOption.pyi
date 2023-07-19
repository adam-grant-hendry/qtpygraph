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
PySide6.QtCore, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from collections.abc import Sequence
from enum import IntFlag
from typing import overload

import PySide6.QtCore

class QCommandLineOption:
    """
    https://doc.qt.io/qt-6/qcommandlineoption.html

    **Detailed Description**

    This class is used to describe an option on the command line. It allows
    different ways of defining the same option with multiple aliases possible.
    It is also used to describe how the option is used - it may be a flag (e.g.
    `-v`) or take a value (e.g. `-o file`).

    Examples:

    **QCommandLineOption**  verboseOption("verbose", "Verbose mode. Prints out
    more information.");
        **QCommandLineOption**
    outputOption(**QStringList** () << "o" << "output", "Write generated data
    into <file>.", "file");

    **See also** **QCommandLineParser** .
    """

    HiddenFromHelp: QCommandLineOption.Flag = ...
    ShortOptionStyle: QCommandLineOption.Flag = ...

    class Flag(IntFlag):
        HiddenFromHelp: QCommandLineOption.Flag = ...
        ShortOptionStyle: QCommandLineOption.Flag = ...

    class Flags: ...

    @overload
    def __init__(self, name: str) -> None:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#QCommandLineOption

        **QCommandLineOption::QCommandLineOption(const QString & name )**

        Constructs a command line option object with the name **name**.

        The name can be either short or long. If the name is one character in
        length, it is considered a short name. Option names must not be empty,
        must not start with a dash or a slash character, must not contain a `=`
        and cannot be repeated.

        **See also** **setDescription** (), **setValueName** (), and
        **setDefaultValues** ().
        """
        ...
    @overload
    def __init__(
        self, name: str, description: str, valueName: str = ..., defaultValue: str = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#QCommandLineOption-1

        **QCommandLineOption::QCommandLineOption(const QStringList & names )**

        Constructs a command line option object with the names **names**.

        This overload allows to set multiple names for the option, for instance
        `o` and `output`.

        The names can be either short or long. Any name in the list that is one
        character in length is a short name. Option names must not be empty,
        must not start with a dash or a slash character, must not contain a `=`
        and cannot be repeated.

        **See also** **setDescription** (), **setValueName** (), and
        **setDefaultValues** ().
        """
        ...
    @overload
    def __init__(self, names: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#QCommandLineOption-2

        **QCommandLineOption::QCommandLineOption(const QString & name , const
        QString & description , const QString & valueName = QString(), const
        QString & defaultValue = QString())**

        Constructs a command line option object with the given arguments.

        The name of the option is set to **name**. The name can be either short
        or long. If the name is one character in length, it is considered a
        short name. Option names must not be empty, must not start with a dash
        or a slash character, must not contain a `=` and cannot be repeated.

        The description is set to **description**. It is customary to add a "."
        at the end of the description.

        In addition, the **valueName** needs to be set if the option expects a
        value. The default value for the option is set to **defaultValue**.

        In Qt versions before 5.4, this constructor was `explicit`. In Qt 5.4
        and later, it no longer is and can be used for C++11-style uniform
        initialization:

        **QCommandLineParser**  parser;
            parser.addOption({"verbose",
        "Verbose mode. Prints out more information."});

        **See also** **setDescription** (), **setValueName** (), and
        **setDefaultValues** ().
        """
        ...
    @overload
    def __init__(
        self,
        names: Sequence[str],
        description: str,
        valueName: str = ...,
        defaultValue: str = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#QCommandLineOption-3

        **QCommandLineOption::QCommandLineOption(const QStringList & names ,
        const QString & description , const QString & valueName = QString(),
        const QString & defaultValue = QString())**

        Constructs a command line option object with the given arguments.

        This overload allows to set multiple names for the option, for instance
        `o` and `output`.

        The names of the option are set to **names**. The names can be either
        short or long. Any name in the list that is one character in length is a
        short name. Option names must not be empty, must not start with a dash
        or a slash character, must not contain a `=` and cannot be repeated.

        The description is set to **description**. It is customary to add a "."
        at the end of the description.

        In addition, the **valueName** needs to be set if the option expects a
        value. The default value for the option is set to **defaultValue**.

        In Qt versions before 5.4, this constructor was `explicit`. In Qt 5.4
        and later, it no longer is and can be used for C++11-style uniform
        initialization:

        **QCommandLineParser**  parser;
            parser.addOption({{"o", "output"},
        "Write generated data into <file>.", "file"});

        **See also** **setDescription** (), **setValueName** (), and
        **setDefaultValues** ().
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtCore.QCommandLineOption) -> None:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#QCommandLineOption-4

        **QCommandLineOption::QCommandLineOption(const QCommandLineOption &
        other )**

        Constructs a QCommandLineOption object that is a copy of the
        QCommandLineOption object **other**.

        **See also** **operator=** ().
        """
        ...
    def defaultValues(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#defaultValues

        **QStringList QCommandLineOption::defaultValues() const**

        Returns the default values set for this option.

        **See also** **setDefaultValues** ().
        """
        ...
    def description(self) -> str:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#description

        **QString QCommandLineOption::description() const**

        Returns the description set for this option.

        **See also** **setDescription** ().
        """
        ...
    def flags(self) -> PySide6.QtCore.QCommandLineOption.Flags:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#flags

        **[since 5.8] QCommandLineOption::Flags QCommandLineOption::flags()
        const**

        Returns a set of flags that affect this command-line option.

        This function was introduced in Qt 5.8.

        **See also** **setFlags** () and **QCommandLineOption::Flags** .
        """
        ...
    def names(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#names

        **QStringList QCommandLineOption::names() const**

        Returns the names set for this option.
        """
        ...
    def setDefaultValue(self, defaultValue: str) -> None:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#setDefaultValue

        **void QCommandLineOption::setDefaultValue(const QString & defaultValue
        )**

        Sets the default value used for this option to **defaultValue**.

        The default value is used if the user of the application does not
        specify the option on the command line.

        If **defaultValue** is empty, the option has no default values.

        **See also** **defaultValues** () and **setDefaultValues** ().
        """
        ...
    def setDefaultValues(self, defaultValues: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#setDefaultValues

        **void QCommandLineOption::setDefaultValues(const QStringList &
        defaultValues )**

        Sets the list of default values used for this option to
        **defaultValues**.

        The default values are used if the user of the application does not
        specify the option on the command line.

        **See also** **defaultValues** () and **setDefaultValue** ().
        """
        ...
    def setDescription(self, description: str) -> None:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#setDescription

        **void QCommandLineOption::setDescription(const QString & description
        )**

        Sets the description used for this option to **description**.

        It is customary to add a "." at the end of the description.

        The description is used by **QCommandLineParser::showHelp** ().

        **See also** **description** ().
        """
        ...
    def setFlags(self, aflags: PySide6.QtCore.QCommandLineOption.Flags) -> None:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#setFlags

        **[since 5.8] void
        QCommandLineOption::setFlags(QCommandLineOption::Flags flags )**

        Set the set of flags that affect this command-line option to **flags**.

        This function was introduced in Qt 5.8.

        **See also** **flags** () and **QCommandLineOption::Flags** .
        """
        ...
    def setValueName(self, name: str) -> None:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#setValueName

        **void QCommandLineOption::setValueName(const QString & valueName )**

        Sets the name of the expected value, for the documentation, to
        **valueName**.

        Options without a value assigned have a boolean-like behavior: either
        the user specifies --option or they don't.

        Options with a value assigned need to set a name for the expected value,
        for the documentation of the option in the help output. An option with
        names `o` and `output`, and a value name of `file` will appear as `-o,
        --output <file>`.

        Call **QCommandLineParser::value** () if you expect the option to be
        present only once, and **QCommandLineParser::values** () if you expect
        that option to be present multiple times.

        **See also** **valueName** ().
        """
        ...
    def swap(self, other: PySide6.QtCore.QCommandLineOption) -> None:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#swap

        **void QCommandLineOption::swap(QCommandLineOption & other )**

        Swaps option **other** with this option. This operation is very fast and
        never fails.
        """
        ...
    def valueName(self) -> str:
        """
        https://doc.qt.io/qt-6/qcommandlineoption.html#valueName

        **QString QCommandLineOption::valueName() const**

        Returns the name of the expected value.

        If empty, the option doesn't take a value.

        **See also** **setValueName** ().
        """
        ...