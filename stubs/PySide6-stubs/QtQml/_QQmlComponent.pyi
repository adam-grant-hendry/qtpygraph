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

from enum import IntFlag
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtNetwork
import PySide6.QtQml

class QQmlComponent(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qqmlcomponent.html

    **Detailed Description**

    Components are reusable, encapsulated QML types with well-defined
    interfaces.

    A QQmlComponent instance can be created from a QML file. For example, if
    there is a `main.qml` file like this:

    import QtQuick 2.0

        **Item**  {
            width: 200
            height:
    200
        }

    The following code loads this QML file as a component, creates an instance
    of this component using **create** (), and then queries the **Item** 's
    **width**  value:

    **QQmlEngine**  *engine = new **QQmlEngine** ;
        QQmlComponent
    component(engine, **QUrl** ::fromLocalFile("main.qml"));
    **QObject**  *myObject = component.create();
        **QQuickItem**  *item =
    qobject_cast<**QQuickItem** *>(myObject);
        int width = item->width();  //
    width = 200

    To create instances of a component in code where a **QQmlEngine**  instance
    is not available, you can use **qmlContext** () or **qmlEngine** (). For
    example, in the scenario below, child items are being created within a
    **QQuickItem**  subclass:

    void MyCppItem::init()
        {
            **QQmlEngine**  *engine =
    qmlEngine(this);
            // Or:
            // QQmlEngine *engine =
    qmlContext(this)->engine();
            QQmlComponent component(engine, **QUrl**
    ::fromLocalFile("MyItem.qml"));
            **QQuickItem**  *childItem =
    qobject_cast<**QQuickItem** *>(component.create());
    childItem->setParentItem(this);
        }

    Note that these functions will return `null` when called inside the
    constructor of a **QObject**  subclass, as the instance will not yet have a
    context nor engine.

    **Network Components**

    If the URL passed to QQmlComponent is a network resource, or if the QML
    document references a network resource, the QQmlComponent has to fetch the
    network data before it is able to create objects. In this case, the
    QQmlComponent will have a **Loading**  **status** . An application will have
    to wait until the component is **Ready**  before calling
    **QQmlComponent::create** ().

    The following example shows how to load a QML file from a network resource.
    After creating the QQmlComponent, it tests whether the component is loading.
    If it is, it connects to the **QQmlComponent::statusChanged** () signal and
    otherwise calls the `continueLoading()` method directly. Note that
    **QQmlComponent::isLoading** () may be false for a network component if the
    component has been cached and is ready immediately.

    MyApplication::MyApplication()
        {
            // ...
            component = new
    QQmlComponent(engine, **QUrl** ("http://www.example.com/main.qml"));
    if (component->isLoading()) {
                **QObject** ::connect(component,
    &QQmlComponent::statusChanged,
                                 this,
    &MyApplication::continueLoading);
            } else {
    continueLoading();
            }
        }

        void
    MyApplication::continueLoading()
        {
            if (component->isError()) {
    **qWarning** () << component->errors();
            } else {
    **QObject**  *myObject = component->create();
            }
        }
    """

    PreferSynchronous: QQmlComponent.CompilationMode = ...
    Asynchronous: QQmlComponent.CompilationMode = ...
    Null: QQmlComponent.Status = ...
    Ready: QQmlComponent.Status = ...
    Loading: QQmlComponent.Status = ...
    Error: QQmlComponent.Status = ...

    class CompilationMode(IntFlag):
        PreferSynchronous: QQmlComponent.CompilationMode = ...
        Asynchronous: QQmlComponent.CompilationMode = ...

    class Status(IntFlag):
        Null: QQmlComponent.Status = ...
        Ready: QQmlComponent.Status = ...
        Loading: QQmlComponent.Status = ...
        Error: QQmlComponent.Status = ...
    @overload
    def __init__(
        self,
        arg__1: PySide6.QtQml.QQmlEngine,
        fileName: str,
        mode: PySide6.QtQml.QQmlComponent.CompilationMode,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent-1

        **QQmlComponent::QQmlComponent(QQmlEngine * engine , QObject * parent =
        nullptr)**

        Create a QQmlComponent with no data and give it the specified **engine**
        and **parent**. Set the data with **setData** ().
        """
        ...
    @overload
    def __init__(
        self,
        arg__1: PySide6.QtQml.QQmlEngine,
        fileName: str,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent-2

        **QQmlComponent::QQmlComponent(QQmlEngine * engine , const QString &
        fileName , QObject * parent = nullptr)**

        Create a QQmlComponent from the given **fileName** and give it the
        specified **parent** and **engine**.

        **See also** **loadUrl** ().
        """
        ...
    @overload
    def __init__(
        self,
        arg__1: PySide6.QtQml.QQmlEngine,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent-3

        **QQmlComponent::QQmlComponent(QQmlEngine * engine , const QString &
        fileName , QQmlComponent::CompilationMode mode , QObject * parent =
        nullptr)**

        Create a QQmlComponent from the given **fileName** and give it the
        specified **parent** and **engine**. If **mode** is **Asynchronous** ,
        the component will be loaded and compiled asynchronously.

        **See also** **loadUrl** ().
        """
        ...
    @overload
    def __init__(
        self,
        arg__1: PySide6.QtQml.QQmlEngine,
        url: PySide6.QtCore.QUrl | str,
        mode: PySide6.QtQml.QQmlComponent.CompilationMode,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent-4

        **QQmlComponent::QQmlComponent(QQmlEngine * engine , const QUrl & url ,
        QObject * parent = nullptr)**

        Create a QQmlComponent from the given **url** and give it the specified
        **parent** and **engine**.

        Ensure that the URL provided is full and correct, in particular, use
        **QUrl::fromLocalFile** () when loading a file from the local
        filesystem.

        Relative paths will be resolved against **QQmlEngine::baseUrl** (),
        which is the current working directory unless specified.

        **See also** **loadUrl** ().
        """
        ...
    @overload
    def __init__(
        self,
        arg__1: PySide6.QtQml.QQmlEngine,
        url: PySide6.QtCore.QUrl | str,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent-5

        **QQmlComponent::QQmlComponent(QQmlEngine * engine , const QUrl & url ,
        QQmlComponent::CompilationMode mode , QObject * parent = nullptr)**

        Create a QQmlComponent from the given **url** and give it the specified
        **parent** and **engine**. If **mode** is **Asynchronous** , the
        component will be loaded and compiled asynchronously.

        Ensure that the URL provided is full and correct, in particular, use
        **QUrl::fromLocalFile** () when loading a file from the local
        filesystem.

        Relative paths will be resolved against **QQmlEngine::baseUrl** (),
        which is the current working directory unless specified.

        **See also** **loadUrl** ().
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent-1

        **QQmlComponent::QQmlComponent(QQmlEngine * engine , QObject * parent =
        nullptr)**

        Create a QQmlComponent with no data and give it the specified **engine**
        and **parent**. Set the data with **setData** ().
        """
        ...
    def beginCreate(self, arg__1: PySide6.QtQml.QQmlContext) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#beginCreate

        **[virtual] QObject *QQmlComponent::beginCreate(QQmlContext * context
        )**

        Create an object instance from this component, within the specified
        **context**. Returns `nullptr` if creation failed.

        **Note:** This method provides advanced control over component instance
        creation. In general, programmers should use **QQmlComponent::create**
        () to create object instances.

        When **QQmlComponent**  constructs an instance, it occurs in three
        steps:

        1. The object hierarchy is created, and constant values are assigned.
        2. Property bindings are evaluated for the first time.
          3. If
        applicable, **QQmlParserStatus::componentComplete** () is called on
        objects.

        QQmlComponent::beginCreate() differs from **QQmlComponent::create** ()
        in that it only performs step 1. **QQmlComponent::completeCreate** ()
        must be called to complete steps 2 and 3.

        This breaking point is sometimes useful when using attached properties
        to communicate information to an instantiated component, as it allows
        their initial values to be configured before property bindings take
        effect.

        The ownership of the returned object instance is transferred to the
        caller.

        **See also** **completeCreate** () and **QQmlEngine::ObjectOwnership** .
        """
        ...
    def completeCreate(self) -> None:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#completeCreate

        **[virtual] void QQmlComponent::completeCreate()**

        This method provides advanced control over component instance creation.
        In general, programmers should use **QQmlComponent::create** () to
        create a component.

        This function completes the component creation begun with
        **QQmlComponent::beginCreate** () and must be called afterwards.

        **See also** **beginCreate** ().
        """
        ...
    @overload
    def create(
        self,
        arg__1: PySide6.QtQml.QQmlIncubator,
        context: PySide6.QtQml.QQmlContext | None = ...,
        forContext: PySide6.QtQml.QQmlContext | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#create

        **[virtual] QObject *QQmlComponent::create(QQmlContext * context =
        nullptr)**

        Create an object instance from this component, within the specified
        **context**. Returns `nullptr` if creation failed.

        If **context** is `nullptr` (the default), it will create the instance
        in the **root context**  of the engine.

        The ownership of the returned object instance is transferred to the
        caller.

        If the object being created from this component is a visual item, it
        must have a visual parent, which can be set by calling
        **QQuickItem::setParentItem** (). See **Concepts - Visual Parent in Qt
        Quick**  for more details.

        **See also** **QQmlEngine::ObjectOwnership** .
        """
        ...
    @overload
    def create(
        self, context: PySide6.QtQml.QQmlContext | None = ...
    ) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#create-1

        **void QQmlComponent::create(QQmlIncubator & incubator , QQmlContext *
        context = nullptr, QQmlContext * forContext = nullptr)**

        Create an object instance from this component using the provided
        **incubator**. **context** specifies the context within which to create
        the object instance.

        If **context** is `nullptr` (by default), it will create the instance in
        the engine's **root context** .

        **forContext** specifies a context that this object creation depends
        upon. If the **forContext** is being created asynchronously, and the
        **QQmlIncubator::IncubationMode**  is
        **QQmlIncubator::AsynchronousIfNested** , this object will also be
        created asynchronously. If **forContext** is `nullptr` (by default), the
        **context** will be used for this decision.

        The created object and its creation status are available via the
        **incubator**.

        **See also** **QQmlIncubator** .
        """
        ...
    def createWithInitialProperties(
        self,
        initialProperties: dict[str, Any],
        context: PySide6.QtQml.QQmlContext | None = ...,
    ) -> PySide6.QtCore.QObject:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#createWithInitialProperties

        **[since 5.14] QObject *QQmlComponent::createWithInitialProperties(const
        QVariantMap & initialProperties , QQmlContext * context = nullptr)**

        Create an object instance of this component, within the specified
        **context** , and initialize its top-level properties with
        **initialProperties**.

        If any of the `initialProperties` cannot be set, **isError** () will
        return `true`, and the **errors** () function can be used to get
        detailed information about the error(s).

        This function was introduced in Qt 5.14.

        **See also** **QQmlComponent::create** .
        """
        ...
    def creationContext(self) -> PySide6.QtQml.QQmlContext:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#creationContext

        **QQmlContext *QQmlComponent::creationContext() const**

        Returns the **QQmlContext**  the component was created in. This is only
        valid for components created directly from QML.
        """
        ...
    def engine(self) -> PySide6.QtQml.QQmlEngine:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#engine

        **[since 5.12] QQmlEngine *QQmlComponent::engine() const**

        Returns the **QQmlEngine**  of this component.

        This function was introduced in Qt 5.12.
        """
        ...
    def errorString(self) -> str: ...
    def errors(self) -> list[PySide6.QtQml.QQmlError]:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#errors

        **QList<QQmlError> QQmlComponent::errors() const**

        Returns the list of errors that occurred during the last compile or
        create operation. An empty list is returned if **isError** () is not
        set.
        """
        ...
    def isError(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#isError

        **bool QQmlComponent::isError() const**

        Returns true if **status** () == **QQmlComponent::Error** .
        """
        ...
    def isLoading(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#isLoading

        **bool QQmlComponent::isLoading() const**

        Returns true if **status** () == **QQmlComponent::Loading** .
        """
        ...
    def isNull(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#isNull

        **bool QQmlComponent::isNull() const**

        Returns true if **status** () == **QQmlComponent::Null** .
        """
        ...
    def isReady(self) -> bool:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#isReady

        **bool QQmlComponent::isReady() const**

        Returns true if **status** () == **QQmlComponent::Ready** .
        """
        ...
    @overload
    def loadUrl(self, url: PySide6.QtCore.QUrl | str) -> None:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#loadUrl

        **[slot] void QQmlComponent::loadUrl(const QUrl & url )**

        Load the **QQmlComponent**  from the provided **url**.

        Ensure that the URL provided is full and correct, in particular, use
        **QUrl::fromLocalFile** () when loading a file from the local
        filesystem.

        Relative paths will be resolved against **QQmlEngine::baseUrl** (),
        which is the current working directory unless specified.
        """
        ...
    @overload
    def loadUrl(
        self,
        url: PySide6.QtCore.QUrl | str,
        mode: PySide6.QtQml.QQmlComponent.CompilationMode,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#loadUrl-1

        **[slot] void QQmlComponent::loadUrl(const QUrl & url ,
        QQmlComponent::CompilationMode mode )**

        Load the **QQmlComponent**  from the provided **url**. If **mode** is
        **Asynchronous** , the component will be loaded and compiled
        asynchronously.

        Ensure that the URL provided is full and correct, in particular, use
        **QUrl::fromLocalFile** () when loading a file from the local
        filesystem.

        Relative paths will be resolved against **QQmlEngine::baseUrl** (),
        which is the current working directory unless specified.
        """
        ...
    def progress(self) -> float:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#progress-prop

        **[read-only] progress : const qreal**

        The progress of loading the component, from 0.0 (nothing loaded) to 1.0
        (finished).

        **Access functions:**

        qreal **progress** () const

        **Notifier signal:**

        void ****progressChanged** ** (qreal **progress** )
        """
        ...
    def setData(
        self,
        arg__1: PySide6.QtCore.QByteArray | bytes,
        baseUrl: PySide6.QtCore.QUrl | str,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#setData

        **[slot] void QQmlComponent::setData(const QByteArray & data , const
        QUrl & url )**

        Sets the **QQmlComponent**  to use the given QML **data**. If **url** is
        provided, it is used to set the component name and to provide a base
        path for items resolved by this component.
        """
        ...
    def setInitialProperties(
        self, component: PySide6.QtCore.QObject, properties: dict[str, Any]
    ) -> None:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#setInitialProperties

        **[since 5.14] void QQmlComponent::setInitialProperties(QObject *
        component , const QVariantMap & properties )**

        Set top-level **properties** of the **component**.

        This method provides advanced control over component instance creation.
        In general, programmers should use
        **QQmlComponent::createWithInitialProperties**  to create a component.

        Use this method after **beginCreate**  and before **completeCreate**
        has been called. If a provided property does not exist, a warning is
        issued.

        This function was introduced in Qt 5.14.
        """
        ...
    def status(self) -> PySide6.QtQml.QQmlComponent.Status:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#status-prop

        **[read-only] status : const Status**

        The component's current **status** .

        **Access functions:**

        QQmlComponent::Status **status** () const

        **Notifier signal:**

        void ****statusChanged** ** (QQmlComponent::Status **status** )
        """
        ...
    def url(self) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#url-prop

        **[read-only] url : const QUrl**

        The component URL. This is the URL passed to either the constructor, or
        the **loadUrl** (), or **setData** () methods.

        **Access functions:**

        QUrl **url** () const

        **Member Function Documentation**
        """
        ...
    @property
    def progressChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#progressChanged

        **[signal] void QQmlComponent::progressChanged(qreal progress )**

        Emitted whenever the component's loading progress changes. **progress**
        will be the current progress between 0.0 (nothing loaded) and 1.0
        (finished).

        **Note:** Notifier signal for property **progress** .
        """
        ...
    @property
    def statusChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qqmlcomponent.html#statusChanged

        **[signal] void QQmlComponent::statusChanged(QQmlComponent::Status
        status )**

        Emitted whenever the component's status changes. **status** will be the
        new status.

        **Note:** Notifier signal for property **status** .
        """
        ...
