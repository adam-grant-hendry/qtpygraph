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

class QDesignerFormWindowInterface(PySide6.QtWidgets.QWidget):
    """
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html

    **Detailed Description**

    QDesignerFormWindowInterface provides information about the associated form
    window as well as allowing its properties to be altered. The interface is
    not intended to be instantiated directly, but to provide access to **Qt
    Designer** 's current form windows controlled by **Qt Designer** 's **form
    window manager** .

    If you are looking for the form window containing a specific widget, you can
    use the static **QDesignerFormWindowInterface::findFormWindow** () function:

    **QDesignerFormWindowInterface**  *formWindow;
            formWindow =
    **QDesignerFormWindowInterface** ::findFormWindow(myWidget);

    But in addition, you can access any of the current form windows through **Qt
    Designer** 's form window manager: Use the
    **QDesignerFormEditorInterface::formWindowManager** () function to retrieve
    an interface to the manager. Once you have this interface, you have access
    to all of **Qt Designer** 's current form windows through the
    **QDesignerFormWindowManagerInterface::formWindow** () function. For
    example:

    **QList** <**QDesignerFormWindowInterface**  *> forms;
    **QDesignerFormWindowInterface**  *formWindow;
    **QDesignerFormWindowManagerInterface**  *manager =
    formEditor->formWindowManager();

            for (int i = 0; i <
    manager->formWindowCount(); i++) {
                formWindow =
    manager->formWindow(i);
                forms.append(formWindow);
            }

    The pointer to **Qt Designer** 's current **QDesignerFormEditorInterface**
    object (`formEditor` in the example above) is provided by the
    **QDesignerCustomWidgetInterface::initialize** () function's parameter. When
    implementing a custom widget plugin, you must subclass the
    **QDesignerCustomWidgetInterface**  class to expose your plugin to **Qt
    Designer**.

    Once you have the form window, you can query its properties. For example, a
    plain custom widget plugin is managed by **Qt Designer** only at its top
    level, i.e. none of its child widgets can be resized in **Qt Designer** 's
    workspace. But QDesignerFormWindowInterface provides you with functions that
    enables you to control whether a widget should be managed by **Qt Designer**
    , or not:

    if (formWindow->isManaged(myWidget))
    formWindow->manageWidget(myWidget->childWidget);

    The complete list of functions concerning widget management is:
    **isManaged** (), **manageWidget** () and **unmanageWidget** (). There is
    also several associated signals: **widgetManaged** (), **widgetRemoved** (),
    **aboutToUnmanageWidget** () and **widgetUnmanaged** ().

    In addition to controlling the management of widgets, you can control the
    current selection in the form window using the **selectWidget** (),
    **clearSelection** () and **emitSelectionChanged** () functions, and the
    **selectionChanged** () signal.

    You can also retrieve information about where the form is stored using
    **absoluteDir** (), its include files using **includeHints** (), and its
    layout and pixmap functions using **layoutDefault** (), **layoutFunction**
    () and **pixmapFunction** (). You can find out whether the form window has
    been modified (but not saved) or not, using the **isDirty** () function. You
    can retrieve its **author** (), its **contents** (), its **fileName** (),
    associated **comment** () and **exportMacro** (), its mainContainer(), its
    **features** (), its **grid** () and its **resourceFiles** ().

    The interface provides you with functions and slots allowing you to alter
    most of this information as well. The exception is the directory storing the
    form window. Finally, there is several signals associated with changes to
    the information mentioned above and to the form window in general.

    **See also** **QDesignerFormWindowCursorInterface** ,
    **QDesignerFormEditorInterface** , and
    **QDesignerFormWindowManagerInterface** .
    """

    EditFeature: QDesignerFormWindowInterface.FeatureFlag = ...
    GridFeature: QDesignerFormWindowInterface.FeatureFlag = ...
    DefaultFeature: QDesignerFormWindowInterface.FeatureFlag = ...
    TabOrderFeature: QDesignerFormWindowInterface.FeatureFlag = ...
    SaveAllResourceFiles: QDesignerFormWindowInterface.ResourceFileSaveMode = ...
    SaveOnlyUsedResourceFiles: QDesignerFormWindowInterface.ResourceFileSaveMode = ...
    DontSaveResourceFiles: QDesignerFormWindowInterface.ResourceFileSaveMode = ...

    class Feature: ...

    class FeatureFlag(IntFlag):
        EditFeature: QDesignerFormWindowInterface.FeatureFlag = ...
        GridFeature: QDesignerFormWindowInterface.FeatureFlag = ...
        DefaultFeature: QDesignerFormWindowInterface.FeatureFlag = ...
        TabOrderFeature: QDesignerFormWindowInterface.FeatureFlag = ...

    class ResourceFileSaveMode(IntFlag):
        SaveAllResourceFiles: QDesignerFormWindowInterface.ResourceFileSaveMode = ...
        SaveOnlyUsedResourceFiles: QDesignerFormWindowInterface.ResourceFileSaveMode = ...
        DontSaveResourceFiles: QDesignerFormWindowInterface.ResourceFileSaveMode = ...
    def __init__(
        self,
        parent: PySide6.QtWidgets.QWidget | None = ...,
        flags: PySide6.QtCore.Qt.WindowFlags = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#QDesignerFormWi
        ndowInterface

        **QDesignerFormWindowInterface::QDesignerFormWindowInterface(QWidget *
        parent = nullptr, Qt::WindowFlags flags = {})**

        Constructs a form window interface with the given **parent** and the
        specified window **flags**.
        """
        ...
    def absoluteDir(self) -> PySide6.QtCore.QDir:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#absoluteDir

        **[pure virtual] QDir QDesignerFormWindowInterface::absoluteDir()
        const**

        Returns the absolute location of the directory containing the form shown
        in the form window.
        """
        ...
    def activateResourceFilePaths(self, paths: Sequence[str]) -> tuple[int, str]:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#activateResourc
        eFilePaths

        **[slot, since 5.0] void
        QDesignerFormWindowInterface::activateResourceFilePaths(const
        QStringList & paths , int * errorCount = nullptr, QString *
        errorMessages = nullptr)**

        Activates the resource (.qrc) file paths **paths** , returning the count
        of errors in **errorCount** and error message in **errorMessages**. **Qt
        Designer** loads the resources using the **QResource**  class, making
        them available for form editing.

        In IDE integrations, a list of the project's resource (.qrc) file can be
        activated, making them available to **Qt Designer**.

        This function was introduced in Qt 5.0.

        **See also** **activeResourceFilePaths** () and **QResource** .
        """
        ...
    def activeResourceFilePaths(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#activeResourceF
        ilePaths

        **[since 5.0] QStringList
        QDesignerFormWindowInterface::activeResourceFilePaths() const**

        Returns the active resource (.qrc) file paths currently loaded in **Qt
        Designer**.

        This function was introduced in Qt 5.0.

        **See also** **activateResourceFilePaths** ().
        """
        ...
    def addResourceFile(self, path: str) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#addResourceFile

        **[pure virtual] void
        QDesignerFormWindowInterface::addResourceFile(const QString & path )**

        Adds the resource file at the given **path** to those used by the form.

        **See also** **resourceFiles** () and **resourceFilesChanged** ().
        """
        ...
    def author(self) -> str:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#author

        **[pure virtual] QString QDesignerFormWindowInterface::author() const**

        Returns details of the author or creator of the form currently being
        displayed in the window.

        **See also** **setAuthor** ().
        """
        ...
    def beginCommand(self, description: str) -> None: ...
    def checkContents(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#checkContents

        **[pure virtual, since 5.0] QStringList
        QDesignerFormWindowInterface::checkContents() const**

        Performs checks on the current form and returns a list of richtext
        warnings about potential issues (for example, top level spacers on
        unlaid-out forms).

        IDE integrations can call this before handling starting a save
        operation.

        This function was introduced in Qt 5.0.
        """
        ...
    def clearSelection(self, changePropertyDisplay: bool = ...) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#clearSelection

        **[pure virtual slot] void
        QDesignerFormWindowInterface::clearSelection(bool update = true)**

        Clears the current selection in the form window. If **update** is true,
        the **emitSelectionChanged** () function is called, emitting the
        **selectionChanged** () signal.

        **See also** **selectWidget** ().
        """
        ...
    def commandHistory(self) -> PySide6.QtGui.QUndoStack: ...
    def comment(self) -> str:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#comment

        **[pure virtual] QString QDesignerFormWindowInterface::comment() const**

        Returns comments about the form currently being displayed in the window.

        **See also** **setComment** ().
        """
        ...
    def contents(self) -> str:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#contents

        **[pure virtual] QString QDesignerFormWindowInterface::contents()
        const**

        Returns details of the contents of the form currently being displayed in
        the window.

        **See also** **setContents** ().
        """
        ...
    def core(self) -> PySide6.QtDesigner.QDesignerFormEditorInterface:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#core

        **[virtual] QDesignerFormEditorInterface
        *QDesignerFormWindowInterface::core() const**

        Returns a pointer to **Qt Designer** 's current
        **QDesignerFormEditorInterface**  object.
        """
        ...
    def currentTool(self) -> int: ...
    def cursor(self) -> PySide6.QtDesigner.QDesignerFormWindowCursorInterface:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#cursor

        **[pure virtual] QDesignerFormWindowCursorInterface
        *QDesignerFormWindowInterface::cursor() const**

        Returns the cursor interface used by the form window.
        """
        ...
    def editWidgets(self) -> None: ...
    def emitSelectionChanged(self) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#emitSelectionCh
        anged

        **[pure virtual] void
        QDesignerFormWindowInterface::emitSelectionChanged()**

        Emits the **selectionChanged** () signal.

        **See also** **selectWidget** () and **clearSelection** ().
        """
        ...
    def endCommand(self) -> None: ...
    def ensureUniqueObjectName(self, object: PySide6.QtCore.QObject) -> None: ...
    def exportMacro(self) -> str:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#exportMacro

        **[pure virtual] QString QDesignerFormWindowInterface::exportMacro()
        const**

        Returns the export macro associated with the form currently being
        displayed in the window. The export macro is used when the form is
        compiled to create a widget plugin.

        **See also** **setExportMacro** () and **Creating Custom Widgets for Qt
        Designer** .
        """
        ...
    def features(self) -> PySide6.QtDesigner.QDesignerFormWindowInterface.Feature:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#features

        **[pure virtual] QDesignerFormWindowInterface::Feature
        QDesignerFormWindowInterface::features() const**

        Returns a combination of the features provided by the form window
        associated with the interface. The value returned can be tested against
        the **Feature**  enum values to determine which features are supported
        by the window.

        **See also** **setFeatures** () and **hasFeature** ().
        """
        ...
    def fileName(self) -> str:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#fileName

        **[pure virtual] QString QDesignerFormWindowInterface::fileName()
        const**

        Returns the file name of the UI file that describes the form currently
        being shown.

        **See also** **setFileName** ().
        """
        ...
    @overload
    @staticmethod
    def findFormWindow(
        obj: PySide6.QtCore.QObject,
    ) -> PySide6.QtDesigner.QDesignerFormWindowInterface:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#findFormWindow

        **[static] QDesignerFormWindowInterface
        *QDesignerFormWindowInterface::findFormWindow(QWidget * widget )**

        Returns the form window interface for the given **widget**.
        """
        ...
    @overload
    @staticmethod
    def findFormWindow(
        w: PySide6.QtWidgets.QWidget,
    ) -> PySide6.QtDesigner.QDesignerFormWindowInterface:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#findFormWindow-
        1

        **[static] QDesignerFormWindowInterface
        *QDesignerFormWindowInterface::findFormWindow(QObject * object )**

        Returns the form window interface for the given **object**.
        """
        ...
    def formContainer(self) -> PySide6.QtWidgets.QWidget:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#formContainer

        **[pure virtual, since 5.0] QWidget
        *QDesignerFormWindowInterface::formContainer() const**

        Returns the form the widget containing the main container widget.

        This function was introduced in Qt 5.0.
        """
        ...
    def grid(self) -> PySide6.QtCore.QPoint:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#grid

        **[pure virtual] QPoint QDesignerFormWindowInterface::grid() const**

        Returns the grid spacing used by the form window.

        **See also** **setGrid** ().
        """
        ...
    def hasFeature(
        self, f: PySide6.QtDesigner.QDesignerFormWindowInterface.Feature
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#hasFeature

        **[pure virtual] bool QDesignerFormWindowInterface::hasFeature(QDesigner
        FormWindowInterface::Feature feature ) const**

        Returns true if the form window offers the specified **feature** ;
        otherwise returns false.

        **See also** **features** ().
        """
        ...
    def includeHints(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#includeHints

        **[pure virtual] QStringList
        QDesignerFormWindowInterface::includeHints() const**

        Returns a list of the header files that will be included in the form
        window's associated UI file.

        Header files may be local, i.e. relative to the project's directory,
        `"mywidget.h"`, or global, i.e. part of Qt or the compilers standard
        libraries: `<QtGui/QWidget>`.

        **See also** **setIncludeHints** ().
        """
        ...
    def isDirty(self) -> bool:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#isDirty

        **[pure virtual] bool QDesignerFormWindowInterface::isDirty() const**

        Returns true if the form window is "dirty" (modified but not saved);
        otherwise returns false.

        **See also** **setDirty** ().
        """
        ...
    def isManaged(self, widget: PySide6.QtWidgets.QWidget) -> bool:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#isManaged

        **[pure virtual] bool QDesignerFormWindowInterface::isManaged(QWidget *
        widget ) const**

        Returns true if the specified **widget** is managed by the form window;
        otherwise returns false.

        **See also** **manageWidget** ().
        """
        ...
    def layoutDefault(self) -> tuple[int, int]:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#layoutDefault

        **[pure virtual] void QDesignerFormWindowInterface::layoutDefault(int *
        margin , int * spacing )**

        Fills in the default margin and spacing for the form's default layout in
        the **margin** and **spacing** variables specified.

        **See also** **setLayoutDefault** ().
        """
        ...
    def layoutFunction(self) -> tuple[str, str]:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#layoutFunction

        **[pure virtual] void
        QDesignerFormWindowInterface::layoutFunction(QString * margin , QString
        * spacing )**

        Fills in the current margin and spacing for the form's layout in the
        **margin** and **spacing** variables specified.

        **See also** **setLayoutFunction** ().
        """
        ...
    def mainContainer(self) -> PySide6.QtWidgets.QWidget: ...
    def manageWidget(self, widget: PySide6.QtWidgets.QWidget) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#manageWidget

        **[pure virtual slot] void
        QDesignerFormWindowInterface::manageWidget(QWidget * widget )**

        Instructs the form window to manage the specified **widget**.

        **See also** **isManaged** (), **unmanageWidget** (), and
        **widgetManaged** ().
        """
        ...
    def pixmapFunction(self) -> str:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#pixmapFunction

        **[pure virtual] QString QDesignerFormWindowInterface::pixmapFunction()
        const**

        Returns the name of the function used to load pixmaps into the form
        window.

        **See also** **setPixmapFunction** ().
        """
        ...
    def registerTool(
        self, tool: PySide6.QtDesigner.QDesignerFormWindowToolInterface
    ) -> None: ...
    def removeResourceFile(self, path: str) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#removeResourceF
        ile

        **[pure virtual] void
        QDesignerFormWindowInterface::removeResourceFile(const QString & path
        )**

        Removes the resource file at the specified **path** from the list of
        those used by the form.

        **See also** **resourceFiles** () and **resourceFilesChanged** ().
        """
        ...
    def resourceFileSaveMode(
        self,
    ) -> PySide6.QtDesigner.QDesignerFormWindowInterface.ResourceFileSaveMode:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#resourceFileSav
        eMode

        **[pure virtual] QDesignerFormWindowInterface::ResourceFileSaveMode
        QDesignerFormWindowInterface::resourceFileSaveMode() const**

        Returns the resource file save mode behavior.

        **See also** **setResourceFileSaveMode** ().
        """
        ...
    def resourceFiles(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#resourceFiles

        **[pure virtual] QStringList
        QDesignerFormWindowInterface::resourceFiles() const**

        Returns a list of paths to resource files that are currently being used
        by the form window.

        **See also** **addResourceFile** () and **removeResourceFile** ().
        """
        ...
    def selectWidget(self, w: PySide6.QtWidgets.QWidget, select: bool = ...) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#selectWidget

        **[pure virtual slot] void
        QDesignerFormWindowInterface::selectWidget(QWidget * widget , bool
        select = true)**

        If **select** is true, the given **widget** is selected; otherwise the
        **widget** is deselected.

        **See also** **clearSelection** () and **selectionChanged** ().
        """
        ...
    def setAuthor(self, author: str) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setAuthor

        **[pure virtual] void QDesignerFormWindowInterface::setAuthor(const
        QString & author )**

        Sets the details for the author or creator of the form to the **author**
        specified.

        **See also** **author** ().
        """
        ...
    def setComment(self, comment: str) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setComment

        **[pure virtual] void QDesignerFormWindowInterface::setComment(const
        QString & comment )**

        Sets the information about the form to the **comment** specified. This
        information should be a human-readable comment about the form.

        **See also** **comment** ().
        """
        ...
    @overload
    def setContents(self, contents: str) -> bool:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setContents

        **[pure virtual] bool
        QDesignerFormWindowInterface::setContents(QIODevice * device , QString *
        errorMessage = 0)**

        Sets the form's contents using data obtained from the given **device**
        and returns whether loading succeeded. If it fails, the error message is
        returned in **errorMessage**.

        Data can be read from **QFile**  objects or any other subclass of
        **QIODevice** .

        **See also** **contents** ().
        """
        ...
    @overload
    def setContents(self, dev: PySide6.QtCore.QIODevice) -> tuple[bool, str]:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setContents-1

        **[pure virtual slot] bool
        QDesignerFormWindowInterface::setContents(const QString & contents )**

        Sets the contents of the form using data read from the specified
        **contents** string and returns whether the operation succeeded.

        **See also** **contents** ().
        """
        ...
    def setCurrentTool(self, index: int) -> None: ...
    def setDirty(self, dirty: bool) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setDirty

        **[pure virtual slot] void QDesignerFormWindowInterface::setDirty(bool
        dirty )**

        If **dirty** is true, the form window is marked as dirty, meaning that
        it is modified but not saved. If **dirty** is false, the form window is
        considered to be unmodified.

        **See also** **isDirty** ().
        """
        ...
    def setExportMacro(self, exportMacro: str) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setExportMacro

        **[pure virtual] void QDesignerFormWindowInterface::setExportMacro(const
        QString & exportMacro )**

        Sets the form window's export macro to **exportMacro**. The export macro
        is used when building a widget plugin to export the form's interface to
        other components.

        **See also** **exportMacro** ().
        """
        ...
    def setFeatures(
        self, f: PySide6.QtDesigner.QDesignerFormWindowInterface.Feature
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setFeatures

        **[pure virtual slot] void QDesignerFormWindowInterface::setFeatures(QDe
        signerFormWindowInterface::Feature features )**

        Enables the specified **features** for the form window.

        **See also** **features** () and **featureChanged** ().
        """
        ...
    def setFileName(self, fileName: str) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setFileName

        **[pure virtual slot] void
        QDesignerFormWindowInterface::setFileName(const QString & fileName )**

        Sets the file name for the form to the given **fileName**.

        **See also** **fileName** () and **fileNameChanged** ().
        """
        ...
    def setGrid(self, grid: PySide6.QtCore.QPoint) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setGrid

        **[pure virtual slot] void QDesignerFormWindowInterface::setGrid(const
        QPoint & grid )**

        Sets the grid size for the form window to the point specified by
        **grid**. In this function, the coordinates in the **QPoint**  are used
        to specify the dimensions of a rectangle in the grid.

        **See also** **grid** ().
        """
        ...
    def setIncludeHints(self, includeHints: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setIncludeHints

        **[pure virtual] void
        QDesignerFormWindowInterface::setIncludeHints(const QStringList &
        includeHints )**

        Sets the header files that will be included in the form window's
        associated UI file to the specified **includeHints**.

        Header files may be local, i.e. relative to the project's directory,
        `"mywidget.h"`, or global, i.e. part of Qt or the compilers standard
        libraries: `<QtGui/QWidget>`.

        **See also** **includeHints** ().
        """
        ...
    def setLayoutDefault(self, margin: int, spacing: int) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setLayoutDefaul
        t

        **[pure virtual] void QDesignerFormWindowInterface::setLayoutDefault(int
        margin , int spacing )**

        Sets the default **margin** and **spacing** for the form's layout.

        **See also** **layoutDefault** ().
        """
        ...
    def setLayoutFunction(self, margin: str, spacing: str) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setLayoutFuncti
        on

        **[pure virtual] void
        QDesignerFormWindowInterface::setLayoutFunction(const QString & margin ,
        const QString & spacing )**

        Sets the **margin** and **spacing** for the form's layout.

        The default layout properties will be replaced by the corresponding
        layout functions when `uic` generates code for the form, that is, if the
        functions are specified. This is useful when different environments
        requires different layouts for the same form.

        **See also** **layoutFunction** ().
        """
        ...
    def setMainContainer(self, mainContainer: PySide6.QtWidgets.QWidget) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setMainContaine
        r

        **[pure virtual] void
        QDesignerFormWindowInterface::setMainContainer(QWidget * mainContainer
        )**

        Sets the main container widget on the form to the specified
        **mainContainer**.

        **See also** **mainContainerChanged** ().
        """
        ...
    def setPixmapFunction(self, pixmapFunction: str) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setPixmapFuncti
        on

        **[pure virtual] void
        QDesignerFormWindowInterface::setPixmapFunction(const QString &
        pixmapFunction )**

        Sets the function used to load pixmaps into the form window to the given
        **pixmapFunction**.

        **See also** **pixmapFunction** ().
        """
        ...
    def setResourceFileSaveMode(
        self,
        behaviour: PySide6.QtDesigner.QDesignerFormWindowInterface.ResourceFileSaveMode,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setResourceFile
        SaveMode

        **[pure virtual] void QDesignerFormWindowInterface::setResourceFileSaveM
        ode(QDesignerFormWindowInterface::ResourceFileSaveMode behavior )**

        Sets the resource file save mode **behavior**.

        **See also** **resourceFileSaveMode** ().
        """
        ...
    def simplifySelection(self, widgets: Sequence[PySide6.QtWidgets.QWidget]) -> None: ...
    def tool(self, index: int) -> PySide6.QtDesigner.QDesignerFormWindowToolInterface: ...
    def toolCount(self) -> int: ...
    def unmanageWidget(self, widget: PySide6.QtWidgets.QWidget) -> None:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#unmanageWidget

        **[pure virtual slot] void
        QDesignerFormWindowInterface::unmanageWidget(QWidget * widget )**

        Instructs the form window not to manage the specified **widget**.

        **See also** **aboutToUnmanageWidget** () and **widgetUnmanaged** ().
        """
        ...
    @property
    def aboutToUnmanageWidget(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#aboutToUnmanage
        Widget

        **[signal] void
        QDesignerFormWindowInterface::aboutToUnmanageWidget(QWidget * widget )**

        This signal is emitted whenever a widget on the form is about to become
        unmanaged. When this signal is emitted, the specified **widget** is
        still managed, and a **widgetUnmanaged** () signal will follow,
        indicating when it is no longer managed.

        **See also** **unmanageWidget** () and **isManaged** ().
        """
        ...
    @property
    def activated(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#activated

        **[signal] void QDesignerFormWindowInterface::activated(QWidget * widget
        )**

        This signal is emitted whenever a widget is activated on the form. The
        activated widget is specified by **widget**.
        """
        ...
    @property
    def changed(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#changed

        **[signal] void QDesignerFormWindowInterface::changed()**

        This signal is emitted whenever a form is changed.
        """
        ...
    @property
    def featureChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#featureChanged

        **[signal] void QDesignerFormWindowInterface::featureChanged(QDesignerFo
        rmWindowInterface::Feature feature )**

        This signal is emitted whenever a feature changes in the form. The new
        feature is specified by **feature**.

        **See also** **setFeatures** ().
        """
        ...
    @property
    def fileNameChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#fileNameChanged

        **[signal] void QDesignerFormWindowInterface::fileNameChanged(const
        QString & fileName )**

        This signal is emitted whenever the file name of the form changes. The
        new file name is specified by **fileName**.

        **See also** **setFileName** ().
        """
        ...
    @property
    def geometryChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#geometryChanged

        **[signal] void QDesignerFormWindowInterface::geometryChanged()**

        This signal is emitted whenever the form's geometry changes.
        """
        ...
    @property
    def mainContainerChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#mainContainerCh
        anged

        **[signal] void
        QDesignerFormWindowInterface::mainContainerChanged(QWidget *
        mainContainer )**

        This signal is emitted whenever the main container changes. The new
        container is specified by **mainContainer**.

        **See also** **setMainContainer** ().
        """
        ...
    @property
    def objectRemoved(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#objectRemoved

        **[signal] void QDesignerFormWindowInterface::objectRemoved(QObject *
        object )**

        This signal is emitted whenever an object (such as an action or a
        **QButtonGroup** ) is removed from the form. The object that was removed
        is specified by **object**.
        """
        ...
    @property
    def resourceFilesChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#resourceFilesCh
        anged

        **[signal] void QDesignerFormWindowInterface::resourceFilesChanged()**

        This signal is emitted whenever the list of resource files used by the
        form changes.

        **See also** **resourceFiles** ().
        """
        ...
    @property
    def selectionChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#selectionChange
        d

        **[signal] void QDesignerFormWindowInterface::selectionChanged()**

        This signal is emitted whenever the selection in the form changes.

        **See also** **selectWidget** () and **clearSelection** ().
        """
        ...
    @property
    def widgetManaged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#widgetManaged

        **[signal] void QDesignerFormWindowInterface::widgetManaged(QWidget *
        widget )**

        This signal is emitted whenever a widget on the form becomes managed.
        The newly managed widget is specified by **widget**.

        **See also** **manageWidget** ().
        """
        ...
    @property
    def widgetRemoved(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#widgetRemoved

        **[signal] void QDesignerFormWindowInterface::widgetRemoved(QWidget *
        widget )**

        This signal is emitted whenever a widget is removed from the form. The
        widget that was removed is specified by **widget**.
        """
        ...
    @property
    def widgetUnmanaged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#widgetUnmanaged

        **[signal] void QDesignerFormWindowInterface::widgetUnmanaged(QWidget *
        widget )**

        This signal is emitted whenever a widget on the form becomes unmanaged.
        The newly released widget is specified by **widget**.

        **See also** **unmanageWidget** () and **aboutToUnmanageWidget** ().
        """
        ...
