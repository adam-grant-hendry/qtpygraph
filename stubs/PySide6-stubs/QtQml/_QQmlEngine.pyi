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
PySide6.QtQml, except for defaults which are replaced by "...".
"""
from __future__ import annotations

import os
from collections.abc import Sequence

import PySide6.QtCore
import PySide6.QtNetwork
import PySide6.QtQml

class QQmlEngine(PySide6.QtQml.QJSEngine):
    """
    https://doc.qt.io/qt-6/qqmlengine.html

    **Detailed Description**

    Each QML component is instantiated in a **QQmlContext** . **QQmlContext** 's
    are essential for passing data to QML components. In QML, contexts are
    arranged hierarchically and this hierarchy is managed by the QQmlEngine.

    Prior to creating any QML components, an application must have created a
    QQmlEngine to gain access to a QML context. The following example shows how
    to create a simple Text item.

    **QQmlEngine**  engine;
        **QQmlComponent**  component(&engine);
    component.setData("import QtQuick 2.0\\nText { text: \\"Hello world!\\" }",
    **QUrl** ());
        **QQuickItem**  *item = qobject_cast<**QQuickItem**
    *>(component.create());

        //add item to view, etc
        ...

    In this case, the Text item will be created in the engine's **root context**
    .

    **See also** **QQmlComponent** , **QQmlContext** , and **QML Global Object**
    .
    """

    def __init__(self, p: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#QQmlEngine

        **QQmlEngine::QQmlEngine(QObject * parent = nullptr)**

        Create a new QQmlEngine with the given **parent**.
        """
        ...
    def addImageProvider(
        self, id: str, arg__2: PySide6.QtQml.QQmlImageProviderBase
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#addImageProvider

        **void QQmlEngine::addImageProvider(const QString & providerId ,
        QQmlImageProviderBase * provider )**

        Sets the **provider** to use for images requested via the **image** :
        url scheme, with host **providerId**. The **QQmlEngine**  takes
        ownership of **provider**.

        Image providers enable support for pixmap and threaded image requests.
        See the **QQuickImageProvider**  documentation for details on
        implementing and using image providers.

        All required image providers should be added to the engine before any
        QML sources files are loaded.

        **See also** **removeImageProvider** (), **QQuickImageProvider** , and
        **QQmlImageProviderBase** .
        """
        ...
    def addImportPath(self, dir: str | bytes | os.PathLike) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#addImportPath

        **void QQmlEngine::addImportPath(const QString & path )**

        Adds **path** as a directory where the engine searches for installed
        modules in a URL-based directory structure.

        The **path** may be a local filesystem directory, a **Qt Resource**
        path (`:/imports`), a **Qt Resource**  url (`qrc:/imports`) or a URL.

        The **path** will be converted into canonical form before it is added to
        the import path list.

        The newly added **path** will be first in the **importPathList** ().

        **See also** **setImportPathList** () and **QML Modules** .
        """
        ...
    def addNamedBundle(self, arg__1: str, arg__2: str) -> bool: ...
    def addPluginPath(self, dir: str | bytes | os.PathLike) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#addPluginPath

        **void QQmlEngine::addPluginPath(const QString & path )**

        Adds **path** as a directory where the engine searches for native
        plugins for imported modules (referenced in the `qmldir` file).

        By default, the list contains only `.`, i.e. the engine searches in the
        directory of the `qmldir` file itself.

        The newly added **path** will be first in the **pluginPathList** ().

        **See also** **setPluginPathList** ().
        """
        ...
    def addUrlInterceptor(
        self, urlInterceptor: PySide6.QtQml.QQmlAbstractUrlInterceptor
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#addUrlInterceptor

        **void QQmlEngine::addUrlInterceptor(QQmlAbstractUrlInterceptor *
        urlInterceptor )**

        Adds a **urlInterceptor** to be used when resolving URLs in QML. This
        also applies to URLs used for loading script files and QML types. The
        URL interceptors should not be modifed while the engine is loading
        files, or URL selection may be inconsistent. Multiple URL interceptors,
        when given, will be called in the order they were added for each URL.

        **QQmlEngine**  does not take ownership of the interceptor and won't
        delete it.
        """
        ...
    def baseUrl(self) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#baseUrl

        **QUrl QQmlEngine::baseUrl() const**

        Return the base URL for this engine. The base URL is only used to
        resolve components when a relative URL is passed to the
        **QQmlComponent**  constructor.

        If a base URL has not been explicitly set, this method returns the
        application's current working directory.

        **See also** **setBaseUrl** ().
        """
        ...
    def captureProperty(
        self, object: PySide6.QtCore.QObject, property: PySide6.QtCore.QMetaProperty
    ) -> None: ...
    def clearComponentCache(self) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#clearComponentCache

        **void QQmlEngine::clearComponentCache()**

        Clears the engine's internal component cache.

        This function causes the property metadata of all components previously
        loaded by the engine to be destroyed. All previously loaded components
        and the property bindings for all extant objects created from those
        components will cease to function.

        This function returns the engine to a state where it does not contain
        any loaded component data. This may be useful in order to reload a
        smaller subset of the previous component set, or to load a new version
        of a previously loaded component.

        Once the component cache has been cleared, components must be loaded
        before any new objects can be created.

        **Note:** Any existing objects created from QML components retain their
        types, even if you clear the component cache. This includes singleton
        objects. If you create more objects from the same QML code after
        clearing the cache, the new objects will be of different types than the
        old ones. Assigning such a new object to a property of its declared type
        belonging to an object created before clearing the cache won't work.

        As a general rule of thumb, make sure that no objects created from QML
        components are alive when you clear the component cache.

        **See also** **trimComponentCache** ().
        """
        ...
    @staticmethod
    def contextForObject(arg__1: PySide6.QtCore.QObject) -> PySide6.QtQml.QQmlContext:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#contextForObject

        **[static] QQmlContext *QQmlEngine::contextForObject(const QObject *
        object )**

        Returns the **QQmlContext**  for the **object** , or 0 if no context has
        been set.

        When the **QQmlEngine**  instantiates a **QObject** , the context is set
        automatically.

        **See also** **setContextForObject** (), **qmlContext** (), and
        **qmlEngine** ().
        """
        ...
    def event(self, arg__1: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#event

        **[override virtual protected] bool QQmlEngine::event(QEvent * e )**

        Reimplements: **QObject::event** (QEvent *e).
        """
        ...
    def imageProvider(self, id: str) -> PySide6.QtQml.QQmlImageProviderBase:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#imageProvider

        **QQmlImageProviderBase *QQmlEngine::imageProvider(const QString &
        providerId ) const**

        Returns the image provider set for **providerId** if found; otherwise
        returns `nullptr`.

        **See also** **QQuickImageProvider** .
        """
        ...
    def importPathList(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#importPathList

        **QStringList QQmlEngine::importPathList() const**

        Returns the list of directories where the engine searches for installed
        modules in a URL-based directory structure.

        For example, if `/opt/MyApp/lib/imports` is in the path, then QML that
        imports `com.mycompany.Feature` will cause the **QQmlEngine**  to look
        in `/opt/MyApp/lib/imports/com/mycompany/Feature/` for the components
        provided by that module. A `qmldir` file is required for defining the
        type version mapping and possibly QML extensions plugins.

        By default, the list contains the directory of the application
        executable, paths specified in the `QML_IMPORT_PATH` environment
        variable, and the builtin `QmlImportsPath` from **QLibraryInfo** .

        **See also** **addImportPath** () and **setImportPathList** ().
        """
        ...
    def importPlugin(
        self, filePath: str, uri: str, errors: Sequence[PySide6.QtQml.QQmlError]
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#importPlugin

        **bool QQmlEngine::importPlugin(const QString & filePath , const QString
        & uri , QList<QQmlError> * errors )**

        Imports the plugin named **filePath** with the **uri** provided. Returns
        true if the plugin was successfully imported; otherwise returns false.

        On failure and if non-null, the **errors** list will have any errors
        which occurred prepended to it.

        The plugin has to be a Qt plugin which implements the
        **QQmlEngineExtensionPlugin**  interface.
        """
        ...
    def incubationController(self) -> PySide6.QtQml.QQmlIncubationController:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#incubationController

        **QQmlIncubationController *QQmlEngine::incubationController() const**

        Returns the currently set incubation controller, or 0 if no controller
        has been set.

        **See also** **setIncubationController** ().
        """
        ...
    def interceptUrl(
        self,
        url: PySide6.QtCore.QUrl | str,
        type: PySide6.QtQml.QQmlAbstractUrlInterceptor.DataType,
    ) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#interceptUrl

        **QUrl QQmlEngine::interceptUrl(const QUrl & url ,
        QQmlAbstractUrlInterceptor::DataType type ) const**

        Run the current URL interceptors on the given **url** of the given
        **type** and return the result.
        """
        ...
    def networkAccessManager(self) -> PySide6.QtNetwork.QNetworkAccessManager:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#networkAccessManager

        **QNetworkAccessManager *QQmlEngine::networkAccessManager() const**

        Returns a common QNetworkAccessManager which can be used by any QML type
        instantiated by this engine.

        If a **QQmlNetworkAccessManagerFactory**  has been set and a
        QNetworkAccessManager has not yet been created, the
        **QQmlNetworkAccessManagerFactory**  will be used to create the
        QNetworkAccessManager; otherwise the returned QNetworkAccessManager will
        have no proxy or cache set.

        **See also** **setNetworkAccessManagerFactory** ().
        """
        ...
    def networkAccessManagerFactory(
        self,
    ) -> PySide6.QtQml.QQmlNetworkAccessManagerFactory:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#networkAccessManagerFactory

        **QQmlNetworkAccessManagerFactory
        *QQmlEngine::networkAccessManagerFactory() const**

        Returns the current **QQmlNetworkAccessManagerFactory** .

        **See also** **setNetworkAccessManagerFactory** ().
        """
        ...
    def offlineStorageDatabaseFilePath(self, databaseName: str) -> str:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#offlineStorageDatabaseFilePath

        **[since 5.9] QString QQmlEngine::offlineStorageDatabaseFilePath(const
        QString & databaseName ) const**

        Returns the file path where a **Local Storage**  database with the
        identifier **databaseName** is (or would be) located.

        This function was introduced in Qt 5.9.

        **See also** **LocalStorage.openDatabaseSync()** .
        """
        ...
    def offlineStoragePath(self) -> str:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#offlineStoragePath-prop

        **offlineStoragePath : QString**

        This property holds the directory for storing offline user data

        Returns the directory where SQL and other offline storage is placed.

        The SQL databases created with `openDatabaseSync()` are stored here.

        The default is QML/OfflineStorage in the platform-standard user
        application data directory.

        Note that the path may not currently exist on the filesystem, so callers
        wanting to **create** new files at this location should create it first
        - see **QDir::mkpath** ().

        **Access functions:**

        QString **offlineStoragePath** () const
        void **setOfflineStoragePath**
        (const QString & **dir** )

        **See also**  l{Qt Quick Local Storage QML Types}.

        **Member Function Documentation**
        """
        ...
    def outputWarningsToStandardError(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#outputWarningsToStandardError

        **bool QQmlEngine::outputWarningsToStandardError() const**

        Returns true if warning messages will be output to stderr in addition to
        being emitted by the **warnings** () signal, otherwise false.

        The default value is true.

        **See also** **setOutputWarningsToStandardError** ().
        """
        ...
    def pluginPathList(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#pluginPathList

        **QStringList QQmlEngine::pluginPathList() const**

        Returns the list of directories where the engine searches for native
        plugins for imported modules (referenced in the `qmldir` file).

        By default, the list contains only `.`, i.e. the engine searches in the
        directory of the `qmldir` file itself.

        **See also** **addPluginPath** () and **setPluginPathList** ().
        """
        ...
    def removeImageProvider(self, id: str) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#removeImageProvider

        **void QQmlEngine::removeImageProvider(const QString & providerId )**

        Removes the image provider for **providerId**.

        **See also** **addImageProvider** () and **QQuickImageProvider** .
        """
        ...
    def removeUrlInterceptor(
        self, urlInterceptor: PySide6.QtQml.QQmlAbstractUrlInterceptor
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#removeUrlInterceptor

        **void QQmlEngine::removeUrlInterceptor(QQmlAbstractUrlInterceptor *
        urlInterceptor )**

        Remove a **urlInterceptor** that was previously added using
        **addUrlInterceptor** . The URL interceptors should not be modifed while
        the engine is loading files, or URL selection may be inconsistent.

        This does not delete the interceptor, but merely removes it from the
        engine. You can re-use it on the same or a different engine afterwards.
        """
        ...
    def retranslate(self) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#retranslate

        **[slot, since 5.10] void QQmlEngine::retranslate()**

        Refreshes all binding expressions that use strings marked for
        translation.

        Call this function after you have installed a new translator with
        **QCoreApplication::installTranslator** , to ensure that your user-
        interface shows up-to-date translations.

        This function was introduced in Qt 5.10.
        """
        ...
    def rootContext(self) -> PySide6.QtQml.QQmlContext:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#rootContext

        **QQmlContext *QQmlEngine::rootContext() const**

        Returns the engine's root context.

        The root context is automatically created by the **QQmlEngine** . Data
        that should be available to all QML component instances instantiated by
        the engine should be put in the root context.

        Additional data that should only be available to a subset of component
        instances should be added to sub-contexts parented to the root context.
        """
        ...
    def setBaseUrl(self, arg__1: PySide6.QtCore.QUrl | str) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#setBaseUrl

        **void QQmlEngine::setBaseUrl(const QUrl & url )**

        Set the base URL for this engine to **url**.

        **See also** **baseUrl** ().
        """
        ...
    @staticmethod
    def setContextForObject(
        arg__1: PySide6.QtCore.QObject, arg__2: PySide6.QtQml.QQmlContext
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#setContextForObject

        **[static] void QQmlEngine::setContextForObject(QObject * object ,
        QQmlContext * context )**

        Sets the **QQmlContext**  for the **object** to **context**. If the
        **object** already has a context, a warning is output, but the context
        is not changed.

        When the **QQmlEngine**  instantiates a **QObject** , the context is set
        automatically.

        **See also** **contextForObject** ().
        """
        ...
    def setImportPathList(self, paths: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#setImportPathList

        **void QQmlEngine::setImportPathList(const QStringList & paths )**

        Sets **paths** as the list of directories where the engine searches for
        installed modules in a URL-based directory structure.

        By default, the list contains the directory of the application
        executable, paths specified in the `QML_IMPORT_PATH` environment
        variable, and the builtin `QmlImportsPath` from **QLibraryInfo** .

        **See also** **importPathList** () and **addImportPath** ().
        """
        ...
    def setIncubationController(
        self, arg__1: PySide6.QtQml.QQmlIncubationController
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#setIncubationController

        **void QQmlEngine::setIncubationController(QQmlIncubationController *
        controller )**

        Sets the engine's incubation **controller**. The engine can only have
        one active controller and it does not take ownership of it.

        **See also** **incubationController** ().
        """
        ...
    def setNetworkAccessManagerFactory(
        self, arg__1: PySide6.QtQml.QQmlNetworkAccessManagerFactory
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#setNetworkAccessManagerFactory

        **void QQmlEngine::setNetworkAccessManagerFactory(QQmlNetworkAccessManag
        erFactory * factory )**

        Sets the **factory** to use for creating QNetworkAccessManager(s).

        QNetworkAccessManager is used for all network access by QML. By
        implementing a factory it is possible to create custom
        QNetworkAccessManager with specialized caching, proxy and cookie
        support.

        The factory must be set before executing the engine.

        **Note:****QQmlEngine**  does not take ownership of the factory.

        **See also** **networkAccessManagerFactory** ().
        """
        ...
    def setOfflineStoragePath(self, dir: str) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#offlineStoragePath-prop

        **offlineStoragePath : QString**

        This property holds the directory for storing offline user data

        Returns the directory where SQL and other offline storage is placed.

        The SQL databases created with `openDatabaseSync()` are stored here.

        The default is QML/OfflineStorage in the platform-standard user
        application data directory.

        Note that the path may not currently exist on the filesystem, so callers
        wanting to **create** new files at this location should create it first
        - see **QDir::mkpath** ().

        **Access functions:**

        QString **offlineStoragePath** () const
        void **setOfflineStoragePath**
        (const QString & **dir** )

        **See also**  l{Qt Quick Local Storage QML Types}.

        **Member Function Documentation**
        """
        ...
    def setOutputWarningsToStandardError(self, arg__1: bool) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#setOutputWarningsToStandardError

        **void QQmlEngine::setOutputWarningsToStandardError(bool enabled )**

        Set whether warning messages will be output to stderr to **enabled**.

        If **enabled** is true, any warning messages generated by QML will be
        output to stderr and emitted by the **warnings** () signal. If
        **enabled** is false, only the **warnings** () signal will be emitted.
        This allows applications to handle warning output themselves.

        The default value is true.

        **See also** **outputWarningsToStandardError** ().
        """
        ...
    def setPluginPathList(self, paths: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#setPluginPathList

        **void QQmlEngine::setPluginPathList(const QStringList & paths )**

        Sets the list of directories where the engine searches for native
        plugins for imported modules (referenced in the `qmldir` file) to
        **paths**.

        By default, the list contains only `.`, i.e. the engine searches in the
        directory of the `qmldir` file itself.

        **See also** **pluginPathList** () and **addPluginPath** ().
        """
        ...
    def setUrlInterceptor(
        self, urlInterceptor: PySide6.QtQml.QQmlAbstractUrlInterceptor
    ) -> None: ...
    def trimComponentCache(self) -> None:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#trimComponentCache

        **void QQmlEngine::trimComponentCache()**

        Trims the engine's internal component cache.

        This function causes the property metadata of any loaded components
        which are not currently in use to be destroyed.

        A component is considered to be in use if there are any extant instances
        of the component itself, any instances of other components that use the
        component, or any objects instantiated by any of those components.

        **See also** **clearComponentCache** ().
        """
        ...
    def urlInterceptor(self) -> PySide6.QtQml.QQmlAbstractUrlInterceptor: ...
    def urlInterceptors(self) -> list[PySide6.QtQml.QQmlAbstractUrlInterceptor]:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#urlInterceptors

        **QList<QQmlAbstractUrlInterceptor *> QQmlEngine::urlInterceptors()
        const**

        Returns the list of currently active URL interceptors.
        """
        ...
    @property
    def exit(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#exit

        **[signal, since 5.8] void QQmlEngine::exit(int retCode )**

        This signal is emitted when the QML loaded by the engine would like to
        exit from the event loop with the specified return code **retCode**.

        This function was introduced in Qt 5.8.

        **See also** **quit** ().
        """
        ...
    @property
    def quit(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#quit

        **[signal] void QQmlEngine::quit()**

        This signal is emitted when the QML loaded by the engine would like to
        quit.

        **See also** **exit** ().
        """
        ...
    @property
    def warnings(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qqmlengine.html#warnings

        **[signal] void QQmlEngine::warnings(const QList<QQmlError> & warnings
        )**

        This signal is emitted when **warnings** messages are generated by QML.
        """
        ...
