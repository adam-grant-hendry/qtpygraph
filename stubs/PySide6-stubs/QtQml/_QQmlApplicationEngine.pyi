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
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtNetwork
import PySide6.QtQml

class QQmlApplicationEngine(PySide6.QtQml.QQmlEngine):
    """
    https://doc.qt.io/qt-6/qqmlapplicationengine.html

    **Detailed Description**

    This class combines a **QQmlEngine**  and **QQmlComponent**  to provide a
    convenient way to load a single QML file. It also exposes some central
    application functionality to QML, which a C++/QML hybrid application would
    normally control from C++.

    It can be used like so:

    #include <QGuiApplication>
        #include <QQmlApplicationEngine>

        int
    main(int argc, char *argv[])
        {
            **QGuiApplication**  app(argc,
    argv);
            **QQmlApplicationEngine**  engine("main.qml");
            return
    app.exec();
        }

    Unlike **QQuickView** , QQmlApplicationEngine does not automatically create
    a root window. If you are using visual items from Qt Quick, you will need to
    place them inside of a **Window** .

    You can also use **QCoreApplication**  with QQmlApplicationEngine, if you
    are not using any QML modules which require a **QGuiApplication**  (such as
    `QtQuick`).

    List of configuration changes from a default **QQmlEngine** :

    * Connecting Qt.**quit** () to **QCoreApplication::quit** ()
      *
    Automatically loads translation files from an i18n directory adjacent to the
    main QML file.
        * Translation files must have "qml_" prefix e.g.
    qml_ja_JP.qm.
      * Translations are reloaded when the `QJSEngine::uiLanguage`
    / `Qt.uiLanguage` property is changed.
      * Automatically sets an incubation
    controller if the scene contains a **QQuickWindow** .
      * Automatically sets
    a `QQmlFileSelector` as the url interceptor, applying file selectors to all
    QML files and assets.

    The engine behavior can be further tweaked by using the inherited methods
    from **QQmlEngine** .
    """

    @overload
    def __init__(
        self, filePath: str, parent: PySide6.QtCore.QObject | None = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlapplicationengine.html#QQmlApplicationEngine

        **QQmlApplicationEngine::QQmlApplicationEngine(QObject * parent =
        nullptr)**

        Create a new QQmlApplicationEngine with the given **parent**. You will
        have to call **load** () later in order to load a QML file.
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qqmlapplicationengine.html#QQmlApplicationEngine-
        1

        **QQmlApplicationEngine::QQmlApplicationEngine(const QUrl & url ,
        QObject * parent = nullptr)**

        Create a new QQmlApplicationEngine and loads the QML file at the given
        **url**. This is provided as a convenience, and is the same as using the
        empty constructor and calling load afterwards.
        """
        ...
    @overload
    def __init__(
        self,
        url: PySide6.QtCore.QUrl | str,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlapplicationengine.html#QQmlApplicationEngine-
        2

        **QQmlApplicationEngine::QQmlApplicationEngine(const QString & filePath
        , QObject * parent = nullptr)**

        Create a new QQmlApplicationEngine and loads the QML file at the given
        **filePath** , which must be a local file path. If a relative path is
        given then it will be interpreted as relative to the working directory
        of the application.

        This is provided as a convenience, and is the same as using the empty
        constructor and calling load afterwards.
        """
        ...
    @overload
    def load(self, filePath: str | bytes | os.PathLike) -> None:
        """
        https://doc.qt.io/qt-6/qqmlapplicationengine.html#load

        **[slot] void QQmlApplicationEngine::load(const QUrl & url )**

        Loads the root QML file located at **url**. The object tree defined by
        the file is created immediately for local file urls. Remote urls are
        loaded asynchronously, listen to the **objectCreated**  signal to
        determine when the object tree is ready.

        If an error occurs, the **objectCreated**  signal is emitted with a null
        pointer as parameter and error messages are printed with **qWarning** .
        """
        ...
    @overload
    def load(self, url: PySide6.QtCore.QUrl | str) -> None:
        """
        https://doc.qt.io/qt-6/qqmlapplicationengine.html#load-1

        **[slot] void QQmlApplicationEngine::load(const QString & filePath )**

        Loads the root QML file located at **filePath**. **filePath** must be a
        path to a local file. If **filePath** is a relative path, it is taken as
        relative to the application's working directory. The object tree defined
        by the file is instantiated immediately.

        If an error occurs, error messages are printed with **qWarning** .
        """
        ...
    def loadData(
        self,
        data: PySide6.QtCore.QByteArray | bytes,
        url: PySide6.QtCore.QUrl | str = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlapplicationengine.html#loadData

        **[slot] void QQmlApplicationEngine::loadData(const QByteArray & data ,
        const QUrl & url = QUrl())**

        Loads the QML given in **data**. The object tree defined by **data** is
        instantiated immediately.

        If a **url** is specified it is used as the base url of the component.
        This affects relative paths within the data and error messages.

        If an error occurs, error messages are printed with **qWarning** .
        """
        ...
    def rootObjects(self) -> list[PySide6.QtCore.QObject]:
        """
        https://doc.qt.io/qt-6/qqmlapplicationengine.html#rootObjects

        **QList<QObject *> QQmlApplicationEngine::rootObjects() const**

        Returns a list of all the root objects instantiated by the
        **QQmlApplicationEngine** . This will only contain objects loaded via
        **load** () or a convenience constructor.

        **Note:** In Qt versions prior to 5.9, this function is marked as
        non-`const`.
        """
        ...
    def setExtraFileSelectors(self, extraFileSelectors: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qqmlapplicationengine.html#setExtraFileSelectors

        **[slot, since 6.0] void
        QQmlApplicationEngine::setExtraFileSelectors(const QStringList &
        extraFileSelectors )**

        Sets the **extraFileSelectors** to be passed to the internal
        **QQmlFileSelector**  used for resolving URLs to local files. The
        **extraFileSelectors** are applied when the first QML file is loaded.
        Setting them afterwards has no effect.

        This function was introduced in Qt 6.0.

        **See also** **QQmlFileSelector**  and
        **QFileSelector::setExtraSelectors** .
        """
        ...
    def setInitialProperties(self, initialProperties: dict[str, Any]) -> None:
        """
        https://doc.qt.io/qt-6/qqmlapplicationengine.html#setInitialProperties

        **[slot, since 5.14] void
        QQmlApplicationEngine::setInitialProperties(const QVariantMap &
        initialProperties )**

        Sets the **initialProperties** with which the QML component gets
        initialized after it gets loaded.

        **QQmlApplicationEngine**  engine;

            EventDatabase eventDatabase;
        EventMonitor eventMonitor;

            engine.setInitialProperties({
        { "eventDatabase", **QVariant** ::fromValue(&eventDatabase) },
                {
        "eventMonitor", **QVariant** ::fromValue(&eventMonitor) }
            });

        This function was introduced in Qt 5.14.

        **See also** **QQmlComponent::setInitialProperties** ,
        **QQmlApplicationEngine::load** , and
        **QQmlApplicationEngine::loadData** .
        """
        ...
    @property
    def objectCreated(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qqmlapplicationengine.html#objectCreated

        **[signal] void QQmlApplicationEngine::objectCreated(QObject * object ,
        const QUrl & url )**

        This signal is emitted when an object finishes loading. If loading was
        successful, **object** contains a pointer to the loaded object,
        otherwise the pointer is NULL.

        The **url** to the component the **object** came from is also provided.

        **Note:** If the path to the component was provided as a **QString**
        containing a relative path, the **url** will contain a fully resolved
        path to the file.
        """
        ...
