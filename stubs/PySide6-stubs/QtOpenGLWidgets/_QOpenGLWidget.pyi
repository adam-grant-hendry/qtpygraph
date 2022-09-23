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
PySide6.QtOpenGLWidgets, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtOpenGLWidgets
import PySide6.QtWidgets

class QOpenGLWidget(PySide6.QtWidgets.QWidget):
    """
    https://doc.qt.io/qt-6/qopenglwidget.html

    **Detailed Description**

    QOpenGLWidget provides functionality for displaying OpenGL graphics
    integrated into a Qt application. It is very simple to use: Make your class
    inherit from it and use the subclass like any other **QWidget** , except
    that you have the choice between using **QPainter**  and standard OpenGL
    rendering commands.

    QOpenGLWidget provides three convenient virtual functions that you can
    reimplement in your subclass to perform the typical OpenGL tasks:

    * **paintGL** () - Renders the OpenGL scene. Gets called whenever the widget
    needs to be updated.
      * **resizeGL** () - Sets up the OpenGL viewport,
    projection, etc. Gets called whenever the widget has been resized (and also
    when it is shown for the first time because all newly created widgets get a
    resize event automatically).
      * **initializeGL** () - Sets up the OpenGL
    resources and state. Gets called once before the first time **resizeGL** ()
    or **paintGL** () is called.

    If you need to trigger a repaint from places other than **paintGL** () (a
    typical example is when using **timers**  to animate scenes), you should
    call the widget's **update** () function to schedule an update.

    Your widget's OpenGL rendering context is made current when **paintGL** (),
    **resizeGL** (), or **initializeGL** () is called. If you need to call the
    standard OpenGL API functions from other places (e.g. in your widget's
    constructor or in your own paint functions), you must call **makeCurrent**
    () first.

    All rendering happens into an OpenGL framebuffer object. **makeCurrent** ()
    ensure that it is bound in the context. Keep this in mind when creating and
    binding additional framebuffer objects in the rendering code in **paintGL**
    (). Never re-bind the framebuffer with ID 0. Instead, call
    **defaultFramebufferObject** () to get the ID that should be bound.

    QOpenGLWidget allows using different OpenGL versions and profiles when the
    platform supports it. Just set the requested format via **setFormat** ().
    Keep in mind however that having multiple QOpenGLWidget instances in the
    same window requires that they all use the same format, or at least formats
    that do not make the contexts non-sharable. To overcome this issue, prefer
    using **QSurfaceFormat::setDefaultFormat** () instead of **setFormat** ().

    **Note:** Calling **QSurfaceFormat::setDefaultFormat** () before
    constructing the **QApplication**  instance is mandatory on some platforms
    (for example, macOS) when an OpenGL core profile context is requested. This
    is to ensure that resource sharing between contexts stays functional as all
    internal contexts are created using the correct version and profile.

    **Painting Techniques**

    As described above, subclass QOpenGLWidget to render pure 3D content in the
    following way:

    * Reimplement the **initializeGL** () and **resizeGL** () functions to set
    up the OpenGL state and provide a perspective transformation.
      *
    Reimplement **paintGL** () to paint the 3D scene, calling only OpenGL
    functions.

    It is also possible to draw 2D graphics onto a QOpenGLWidget subclass using
    **QPainter** :

    * In **paintGL** (), instead of issuing OpenGL commands, construct a
    **QPainter**  object for use on the widget.
      * Draw primitives using
    **QPainter** 's member functions.
      * Direct OpenGL commands can still be
    issued. However, you must make sure these are enclosed by a call to the
    painter's beginNativePainting() and endNativePainting().

    When performing drawing using **QPainter**  only, it is also possible to
    perform the painting like it is done for ordinary widgets: by reimplementing
    **paintEvent** ().

    * Reimplement the **paintEvent** () function.
      * Construct a **QPainter**
    object targeting the widget. Either pass the widget to the constructor or
    the **QPainter::begin** () function.
      * Draw primitives using **QPainter**
    's member functions.
      * Painting finishes then the **QPainter**  instance
    is destroyed. Alternatively, call **QPainter::end** () explicitly.

    **OpenGL Function Calls, Headers and QOpenGLFunctions**

    When making OpenGL function calls, it is strongly recommended to avoid
    calling the functions directly. Instead, prefer using **QOpenGLFunctions**
    (when making portable applications) or the versioned variants (for example,
    **QOpenGLFunctions_3_2_Core**  and similar, when targeting modern, desktop-
    only OpenGL). This way the application will work correctly in all Qt build
    configurations, including the ones that perform dynamic OpenGL
    implementation loading which means applications are not directly linking to
    an GL implementation and thus direct function calls are not feasible.

    In **paintGL** () the current context is always accessible by caling
    **QOpenGLContext::currentContext** (). From this context an already
    initialized, ready-to-be-used **QOpenGLFunctions**  instance is retrievable
    by calling **QOpenGLContext::functions** (). An alternative to prefixing
    every GL call is to inherit from **QOpenGLFunctions**  and call
    **QOpenGLFunctions::initializeOpenGLFunctions** () in **initializeGL** ().

    As for the OpenGL headers, note that in most cases there will be no need to
    directly include any headers like GL.h. The OpenGL-related Qt headers will
    include qopengl.h which will in turn include an appropriate header for the
    system. This might be an OpenGL ES 3.x or 2.0 header, the highest version
    that is available, or a system-provided gl.h. In addition, a copy of the
    extension headers (called glext.h on some systems) is provided as part of Qt
    both for OpenGL and OpenGL ES. These will get included automatically on
    platforms where feasible. This means that constants and function pointer
    typedefs from ARB, EXT, OES extensions are automatically available.

    **Code Examples**

    To get started, the simplest QOpenGLWidget subclass could like like the
    following:

    class MyGLWidget : public **QOpenGLWidget**
        {
        public:
    MyGLWidget(**QWidget**  *parent) : **QOpenGLWidget** (parent) { }
    protected:
            void initializeGL() override
            {
                // Set
    up the rendering context, load shaders and other resources, etc.:
    **QOpenGLFunctions**  *f = **QOpenGLContext**
    ::currentContext()->functions();
                f->glClearColor(1.0f, 1.0f,
    1.0f, 1.0f);
                ...
            }

            void resizeGL(int w, int
    h) override
            {
                // Update projection matrix and other size
    related settings:
                m_projection.setToIdentity();
    m_projection.perspective(45.0f, w / float(h), 0.01f, 100.0f);
    ...
            }

            void paintGL() override
            {
                //
    Draw the scene:
                **QOpenGLFunctions**  *f = **QOpenGLContext**
    ::currentContext()->functions();
    f->glClear(GL_COLOR_BUFFER_BIT);
                ...
            }

        };

    Alternatively, the prefixing of each and every OpenGL call can be avoided by
    deriving from **QOpenGLFunctions**  instead:

    class MyGLWidget : public **QOpenGLWidget** , protected **QOpenGLFunctions**
    {
            ...
            void initializeGL() override
            {
    initializeOpenGLFunctions();
                glClearColor(...);
                ...
    }
            ...
        };

    To get a context compatible with a given OpenGL version or profile, or to
    request depth and stencil buffers, call **setFormat** ():

    **QOpenGLWidget**  *widget = new **QOpenGLWidget** (parent);
    **QSurfaceFormat**  format;
        format.setDepthBufferSize(24);
    format.setStencilBufferSize(8);
        format.setVersion(3, 2);
    format.setProfile(**QSurfaceFormat** ::CoreProfile);
    widget->setFormat(format); // must be called before the widget or its parent
    window gets shown

    With OpenGL 3.0+ contexts, when portability is not important, the versioned
    **QOpenGLFunctions**  variants give easy access to all the modern OpenGL
    functions available in a given version:

    ...
            void paintGL() override
            {
    QOpenGLFunctions_3_2_Core *f = **QOpenGLContext**
    ::currentContext()->versionFunctions<QOpenGLFunctions_3_2_Core>();
    ...
                f->glDrawArraysInstanced(...);
                ...
            }
    ...

    As described above, it is simpler and more robust to set the requested
    format globally so that it applies to all windows and contexts during the
    lifetime of the application. Below is an example of this:

    int main(int argc, char **argv)
        {
            **QApplication**  app(argc,
    argv);

            **QSurfaceFormat**  format;
    format.setDepthBufferSize(24);
            format.setStencilBufferSize(8);
    format.setVersion(3, 2);
            format.setProfile(**QSurfaceFormat**
    ::CoreProfile);
            **QSurfaceFormat** ::setDefaultFormat(format);
    MyWidget widget;
            widget.show();

            return app.exec();
    }

    **Multisampling**

    To enable multisampling, set the number of requested samples on the
    **QSurfaceFormat**  that is passed to **setFormat** (). On systems that do
    not support it the request may get ignored.

    Multisampling support requires support for multisampled renderbuffers and
    framebuffer blits. On OpenGL ES 2.0 implementations it is likely that these
    will not be present. This means that multisampling will not be available.
    With modern OpenGL versions and OpenGL ES 3.0 and up this is usually not a
    problem anymore.

    **Threading**

    Performing offscreen rendering on worker threads, for example to generate
    textures that are then used in the GUI/main thread in **paintGL** (), are
    supported by exposing the widget's **QOpenGLContext**  so that additional
    contexts sharing with it can be created on each thread.

    Drawing directly to the QOpenGLWidget's framebuffer outside the GUI/main
    thread is possible by reimplementing **paintEvent** () to do nothing. The
    context's thread affinity has to be changed via **QObject::moveToThread**
    (). After that, **makeCurrent** () and **doneCurrent** () are usable on the
    worker thread. Be careful to move the context back to the GUI/main thread
    afterwards.

    Triggering a buffer swap just for the QOpenGLWidget is not possible since
    there is no real, onscreen native surface for it. It is up to the widget
    stack to manage composition and buffer swaps on the gui thread. When a
    thread is done updating the framebuffer, call **update** () **on the
    GUI/main thread** to schedule composition.

    Extra care has to be taken to avoid using the framebuffer when the GUI/main
    thread is performing compositing. The signals **aboutToCompose** () and
    **frameSwapped** () will be emitted when the composition is starting and
    ending. They are emitted on the GUI/main thread. This means that by using a
    direct connection **aboutToCompose** () can block the GUI/main thread until
    the worker thread has finished its rendering. After that, the worker thread
    must perform no further rendering until the **frameSwapped** () signal is
    emitted. If this is not acceptable, the worker thread has to implement a
    double buffering mechanism. This involves drawing using an alternative
    render target, that is fully controlled by the thread, e.g. an additional
    framebuffer object, and blitting to the QOpenGLWidget's framebuffer at a
    suitable time.

    **Context Sharing**

    When multiple QOpenGLWidgets are added as children to the same top-level
    widget, their contexts will share with each other. This does not apply for
    QOpenGLWidget instances that belong to different windows.

    This means that all QOpenGLWidgets in the same window can access each
    other's sharable resources, like textures, and there is no need for an extra
    "global share" context.

    To set up sharing between QOpenGLWidget instances belonging to different
    windows, set the **Qt::AA_ShareOpenGLContexts**  application attribute
    before instantiating **QApplication** . This will trigger sharing between
    all QOpenGLWidget instances without any further steps.

    Creating extra **QOpenGLContext**  instances that share resources like
    textures with the QOpenGLWidget's context is also possible. Simply pass the
    pointer returned from **context** () to **QOpenGLContext::setShareContext**
    () before calling **QOpenGLContext::create** (). The resulting context can
    also be used on a different thread, allowing threaded generation of textures
    and asynchronous texture uploads.

    Note that QOpenGLWidget expects a standard conformant implementation of
    resource sharing when it comes to the underlying graphics drivers. For
    example, some drivers, in particular for mobile and embedded hardware, have
    issues with setting up sharing between an existing context and others that
    are created later. Some other drivers may behave in unexpected ways when
    trying to utilize shared resources between different threads.

    **Resource Initialization and Cleanup**

    The QOpenGLWidget's associated OpenGL context is guaranteed to be current
    whenever **initializeGL** () and **paintGL** () are invoked. Do not attempt
    to create OpenGL resources before **initializeGL** () is called. For
    example, attempting to compile shaders, initialize vertex buffer objects or
    upload texture data will fail when done in a subclass's constructor. These
    operations must be deferred to **initializeGL** (). Some of Qt's OpenGL
    helper classes, like **QOpenGLBuffer**  or **QOpenGLVertexArrayObject** ,
    have a matching deferred behavior: they can be instantiated without a
    context, but all initialization is deferred until a **create** (), or
    similar, call. This means that they can be used as normal (non-pointer)
    member variables in a QOpenGLWidget subclass, but the **create** () or
    similar function can only be called from **initializeGL** (). Be aware
    however that not all classes are designed like this. When in doubt, make the
    member variable a pointer and create and destroy the instance dynamically in
    **initializeGL** () and the destructor, respectively.

    Releasing the resources also needs the context to be current. Therefore
    destructors that perform such cleanup are expected to call **makeCurrent**
    () before moving on to destroy any OpenGL resources or wrappers. Avoid
    deferred deletion via **deleteLater** () or the parenting mechanism of
    **QObject** . There is no guarantee the correct context will be current at
    the time the instance in question is really destroyed.

    A typical subclass will therefore often look like the following when it
    comes to resource initialization and destruction:

    class MyGLWidget : public **QOpenGLWidget**
        {
            ...
    private:
            **QOpenGLVertexArrayObject**  m_vao;
    **QOpenGLBuffer**  m_vbo;
            **QOpenGLShaderProgram**  *m_program;
    **QOpenGLShader**  *m_shader;
            **QOpenGLTexture**  *m_texture;
        };
    MyGLWidget::MyGLWidget()
            : m_program(0), m_shader(0), m_texture(0)
    {
            // No OpenGL resource initialization is done here.
        }
    MyGLWidget::~MyGLWidget()
        {
            // Make sure the context is current
    and then explicitly
            // destroy all underlying OpenGL resources.
    makeCurrent();

            delete m_texture;
            delete m_shader;
    delete m_program;

            m_vbo.destroy();
            m_vao.destroy();
    doneCurrent();
        }

        void MyGLWidget::initializeGL()
        {
    m_vao.create();
            if (m_vao.isCreated())
                m_vao.bind();
    m_vbo.create();
            m_vbo.bind();
            m_vbo.allocate(...);
    m_texture = new **QOpenGLTexture** (**QImage** (...));

            m_shader
    = new **QOpenGLShader** (...);
            m_program = new
    **QOpenGLShaderProgram** (...);

            ...
        }

    This is naturally not the only possible solution. One alternative is to use
    the **aboutToBeDestroyed** () signal of **QOpenGLContext** . By connecting a
    slot, using direct connection, to this signal, it is possible to perform
    cleanup whenever the underlying native context handle, or the entire
    **QOpenGLContext**  instance, is going to be released. The following snippet
    is in principle equivalent to the previous one:

    void MyGLWidget::initializeGL()
        {
            // context() and
    QOpenGLContext::currentContext() are equivalent when called from
    initializeGL or paintGL.
            connect(context(), &**QOpenGLContext**
    ::aboutToBeDestroyed, this, &MyGLWidget::cleanup);
        }

        void
    MyGLWidget::cleanup()
        {
            makeCurrent();
            delete m_texture;
    m_texture = 0;
            ...
            doneCurrent();
        }

    **Note:** For widgets that change their associated top-level window multiple
    times during their lifetime, a combined approach is essential. Whenever the
    widget or a parent of it gets reparented so that the top-level window
    becomes different, the widget's associated context is destroyed and a new
    one is created. This is then followed by a call to **initializeGL** () where
    all OpenGL resources must get reinitialized. Due to this the only option to
    perform proper cleanup is to connect to the context's aboutToBeDestroyed()
    signal. Note that the context in question may not be the current one when
    the signal gets emitted. Therefore it is good practice to call
    **makeCurrent** () in the connected slot. Additionally, the same cleanup
    steps must be performed from the derived class' destructor, since the slot
    connected to the signal will not get invoked when the widget is being
    destroyed.

    **Note:** When **Qt::AA_ShareOpenGLContexts**  is set, the widget's context
    never changes, not even when reparenting because the widget's associated
    texture is guaranteed to be accessible also from the new top-level's
    context.

    Proper cleanup is especially important due to context sharing. Even though
    each QOpenGLWidget's associated context is destroyed together with the
    QOpenGLWidget, the sharable resources in that context, like textures, will
    stay valid until the top-level window, in which the QOpenGLWidget lived, is
    destroyed. Additionally, settings like **Qt::AA_ShareOpenGLContexts**  and
    some Qt modules may trigger an even wider scope for sharing contexts,
    potentially leading to keeping the resources in question alive for the
    entire lifetime of the application. Therefore the safest and most robust is
    always to perform explicit cleanup for all resources and resource wrappers
    used in the QOpenGLWidget.

    **Limitations**

    Putting other widgets underneath and making the QOpenGLWidget transparent
    will not lead to the expected results: The widgets underneath will not be
    visible. This is because in practice the QOpenGLWidget is drawn before all
    other regular, non-OpenGL widgets, and so see-through type of solutions are
    not feasible. Other type of layouts, like having widgets on top of the
    QOpenGLWidget, will function as expected.

    When absolutely necessary, this limitation can be overcome by setting the
    **Qt::WA_AlwaysStackOnTop**  attribute on the QOpenGLWidget. Be aware
    however that this breaks stacking order, for example it will not be possible
    to have other widgets on top of the QOpenGLWidget, so it should only be used
    in situations where a semi-transparent QOpenGLWidget with other widgets
    visible underneath is required.

    Note that this does not apply when there are no other widgets underneath and
    the intention is to have a semi-transparent window. In that case the
    traditional approach of setting **Qt::WA_TranslucentBackground**  on the
    top-level window is sufficient. Note that if the transparent areas are only
    desired in the QOpenGLWidget, then **Qt::WA_NoSystemBackground**  will need
    to be turned back to `false` after enabling **Qt::WA_TranslucentBackground**
    . Additionally, requesting an alpha channel for the QOpenGLWidget's context
    via **setFormat** () may be necessary too, depending on the system.

    QOpenGLWidget supports multiple update behaviors, just like
    **QOpenGLWindow** . In preserved mode the rendered content from the previous
    **paintGL** () call is available in the next one, allowing incremental
    rendering. In non-preserved mode the content is lost and **paintGL** ()
    implementations are expected to redraw everything in the view.

    Before Qt 5.5 the default behavior of QOpenGLWidget was to preserve the
    rendered contents between **paintGL** () calls. Since Qt 5.5 the default
    behavior is non-preserved because this provides better performance and the
    majority of applications have no need for the previous content. This also
    resembles the semantics of an OpenGL-based **QWindow**  and matches the
    default behavior of **QOpenGLWindow**  in that the color and ancillary
    buffers are invalidated for each frame. To restore the preserved behavior,
    call **setUpdateBehavior** () with `PartialUpdate`.

    **Note:** Displaying a QOpenGLWidget requires an alpha channel in the
    associated top-level window's backing store due to the way composition with
    other **QWidget** -based content works. If there is no alpha channel, the
    content rendered by the QOpenGLWidget will not be visible. This can become
    particularly relevant on Linux/X11 in remote display setups (such as, with
    Xvnc), when using a color depth lower than 24. For example, a color depth of
    16 will typically map to using a backing store image with the format
    **QImage::Format_RGB16**  (RGB565), leaving no room for an alpha channel.
    Therefore, if experiencing problems with getting the contents of a
    QOpenGLWidget composited correctly with other the widgets in the window,
    make sure the server (such as, vncserver) is configured with a 24 or 32 bit
    depth instead of 16.

    **Alternatives**

    Adding a QOpenGLWidget into a window turns on OpenGL-based compositing for
    the entire window. In some special cases this may not be ideal, and the old
    QGLWidget-style behavior with a separate, native child window is desired.
    Desktop applications that understand the limitations of this approach (for
    example when it comes to overlaps, transparency, scroll views and MDI
    areas), can use **QOpenGLWindow**  with **QWidget::createWindowContainer**
    (). This is a modern alternative to QGLWidget and is faster than
    QOpenGLWidget due to the lack of the additional composition step. It is
    strongly recommended to limit the usage of this approach to cases where
    there is no other choice. Note that this option is not suitable for most
    embedded and mobile platforms, and it is known to have issues on certain
    desktop platforms (e.g. macOS) too. The stable, cross-platform solution is
    always QOpenGLWidget.

    **OpenGL is a trademark of Silicon Graphics, Inc. in the United States and
    other countries.**

    **See also** **QOpenGLFunctions** , **QOpenGLWindow** ,
    **Qt::AA_ShareOpenGLContexts** , and **UpdateBehavior** .
    """

    NoPartialUpdate: QOpenGLWidget.UpdateBehavior = ...
    PartialUpdate: QOpenGLWidget.UpdateBehavior = ...

    class UpdateBehavior(IntFlag):
        NoPartialUpdate: QOpenGLWidget.UpdateBehavior = ...
        PartialUpdate: QOpenGLWidget.UpdateBehavior = ...
    def __init__(
        self,
        parent: PySide6.QtWidgets.QWidget | None = ...,
        f: PySide6.QtCore.Qt.WindowFlags = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#QOpenGLWidget

        **QOpenGLWidget::QOpenGLWidget(QWidget * parent = nullptr,
        Qt::WindowFlags f = Qt::WindowFlags())**

        Constructs a widget which is a child of **parent** , with widget flags
        set to **f**.
        """
        ...
    def context(self) -> PySide6.QtGui.QOpenGLContext:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#context

        **QOpenGLContext *QOpenGLWidget::context() const**

        Returns The **QOpenGLContext**  used by this widget or `0` if not yet
        initialized.

        **Note:** The context and the framebuffer object used by the widget
        changes when reparenting the widget via **setParent** ().

        **See also** **QOpenGLContext::setShareContext** () and
        **defaultFramebufferObject** ().
        """
        ...
    def defaultFramebufferObject(self) -> int:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#defaultFramebufferObject

        **GLuint QOpenGLWidget::defaultFramebufferObject() const**

        Returns The framebuffer object handle or `0` if not yet initialized.

        **Note:** The framebuffer object belongs to the context returned by
        **context** () and may not be accessible from other contexts.

        **Note:** The context and the framebuffer object used by the widget
        changes when reparenting the widget via **setParent** (). In addition,
        the framebuffer object changes on each resize.

        **See also** **context** ().
        """
        ...
    def doneCurrent(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#doneCurrent

        **void QOpenGLWidget::doneCurrent()**

        Releases the context.

        It is not necessary to call this function in most cases, since the
        widget will make sure the context is bound and released properly when
        invoking **paintGL** ().
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#event

        **[override virtual protected] bool QOpenGLWidget::event(QEvent * e )**

        Reimplements: **QWidget::event** (QEvent *event).
        """
        ...
    def format(self) -> PySide6.QtGui.QSurfaceFormat:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#format

        **QSurfaceFormat QOpenGLWidget::format() const**

        Returns the context and surface format used by this widget and its
        toplevel window.

        After the widget and its toplevel have both been created, resized and
        shown, this function will return the actual format of the context. This
        may differ from the requested format if the request could not be
        fulfilled by the platform. It is also possible to get larger color
        buffer sizes than requested.

        When the widget's window and the related OpenGL resources are not yet
        initialized, the return value is the format that has been set via
        **setFormat** ().

        **See also** **setFormat** () and **context** ().
        """
        ...
    def grabFramebuffer(self) -> PySide6.QtGui.QImage:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#grabFramebuffer

        **QImage QOpenGLWidget::grabFramebuffer()**

        Renders and returns a 32-bit RGB image of the framebuffer.

        **Note:** This is a potentially expensive operation because it relies on
        glReadPixels() to read back the pixels. This may be slow and can stall
        the GPU pipeline.
        """
        ...
    def initializeGL(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#initializeGL

        **[virtual protected] void QOpenGLWidget::initializeGL()**

        This virtual function is called once before the first call to
        **paintGL** () or **resizeGL** (). Reimplement it in a subclass.

        This function should set up any required OpenGL resources and state.

        There is no need to call **makeCurrent** () because this has already
        been done when this function is called. Note however that the
        framebuffer is not yet available at this stage, so avoid issuing draw
        calls from here. Defer such calls to **paintGL** () instead.

        **See also** **paintGL** () and **resizeGL** ().
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#isValid

        **bool QOpenGLWidget::isValid() const**

        Returns **true** if the widget and OpenGL resources, like the context,
        have been successfully initialized. Note that the return value is always
        false until the widget is shown.
        """
        ...
    def makeCurrent(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#makeCurrent

        **void QOpenGLWidget::makeCurrent()**

        Prepares for rendering OpenGL content for this widget by making the
        corresponding context current and binding the framebuffer object in that
        context.

        It is not necessary to call this function in most cases, because it is
        called automatically before invoking **paintGL** ().

        **See also** **context** (), **paintGL** (), and **doneCurrent** ().
        """
        ...
    def metric(self, metric: PySide6.QtGui.QPaintDevice.PaintDeviceMetric) -> int:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#metric

        **[override virtual protected] int
        QOpenGLWidget::metric(QPaintDevice::PaintDeviceMetric metric ) const**

        Reimplements: **QWidget::metric(QPaintDevice::PaintDeviceMetric m)
        const** .
        """
        ...
    def paintEngine(self) -> PySide6.QtGui.QPaintEngine:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#paintEngine

        **[override virtual protected] QPaintEngine
        *QOpenGLWidget::paintEngine() const**

        Reimplements: **QWidget::paintEngine() const** .
        """
        ...
    def paintEvent(self, e: PySide6.QtGui.QPaintEvent) -> None:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#paintEvent

        **[override virtual protected] void
        QOpenGLWidget::paintEvent(QPaintEvent * e )**

        Reimplements: **QWidget::paintEvent** (QPaintEvent *event).

        Handles paint events.

        Calling **QWidget::update** () will lead to sending a paint event **e**
        , and thus invoking this function. (NB this is asynchronous and will
        happen at some point after returning from **update** ()). This function
        will then, after some preparation, call the virtual **paintGL** () to
        update the contents of the **QOpenGLWidget** 's framebuffer. The
        widget's top-level window will then composite the framebuffer's texture
        with the rest of the window.
        """
        ...
    def paintGL(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#paintGL

        **[virtual protected] void QOpenGLWidget::paintGL()**

        This virtual function is called whenever the widget needs to be painted.
        Reimplement it in a subclass.

        There is no need to call **makeCurrent** () because this has already
        been done when this function is called.

        Before invoking this function, the context and the framebuffer are
        bound, and the viewport is set up by a call to glViewport(). No other
        state is set and no clearing or drawing is performed by the framework.

        **See also** **initializeGL** () and **resizeGL** ().
        """
        ...
    def redirected(self, p: PySide6.QtCore.QPoint) -> PySide6.QtGui.QPaintDevice:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#redirected

        **[override virtual protected] QPaintDevice
        *QOpenGLWidget::redirected(QPoint * p ) const**
        """
        ...
    def resizeEvent(self, e: PySide6.QtGui.QResizeEvent) -> None:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#resizeEvent

        **[override virtual protected] void
        QOpenGLWidget::resizeEvent(QResizeEvent * e )**

        Reimplements: **QWidget::resizeEvent** (QResizeEvent *event).

        Handles resize events that are passed in the **e** event parameter.
        Calls the virtual function **resizeGL** ().

        **Note:** Avoid overriding this function in derived classes. If that is
        not feasible, make sure that **QOpenGLWidget** 's implementation is
        invoked too. Otherwise the underlying framebuffer object and related
        resources will not get resized properly and will lead to incorrect
        rendering.
        """
        ...
    def resizeGL(self, w: int, h: int) -> None:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#resizeGL

        **[virtual protected] void QOpenGLWidget::resizeGL(int w , int h )**

        This virtual function is called whenever the widget has been resized.
        Reimplement it in a subclass. The new size is passed in **w** and **h**.

        There is no need to call **makeCurrent** () because this has already
        been done when this function is called. Additionally, the framebuffer is
        also bound.

        **See also** **initializeGL** () and **paintGL** ().
        """
        ...
    def setFormat(
        self,
        format: (
            PySide6.QtGui.QSurfaceFormat | PySide6.QtGui.QSurfaceFormat.FormatOptions
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#setFormat

        **void QOpenGLWidget::setFormat(const QSurfaceFormat & format )**

        Sets the requested surface **format**.

        When the format is not explicitly set via this function, the format
        returned by **QSurfaceFormat::defaultFormat** () will be used. This
        means that when having multiple OpenGL widgets, individual calls to this
        function can be replaced by one single call to
        **QSurfaceFormat::setDefaultFormat** () before creating the first
        widget.

        **Note:** Requesting an alpha buffer via this function will not lead to
        the desired results when the intention is to make other widgets beneath
        visible. Instead, use **Qt::WA_AlwaysStackOnTop**  to enable semi-
        transparent **QOpenGLWidget**  instances with other widgets visible
        underneath. Keep in mind however that this breaks the stacking order, so
        it will no longer be possible to have other widgets on top of the
        **QOpenGLWidget** .

        **See also** **format** (), **Qt::WA_AlwaysStackOnTop** , and
        **QSurfaceFormat::setDefaultFormat** ().
        """
        ...
    def setTextureFormat(self, texFormat: int) -> None:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#setTextureFormat

        **[since 5.10] void QOpenGLWidget::setTextureFormat(GLenum texFormat )**

        Sets a custom internal texture format of **texFormat**.

        When working with sRGB framebuffers, it will be necessary to specify a
        format like `GL_SRGB8_ALPHA8`. This can be achieved by calling this
        function.

        **Note:** This function has no effect if called after the widget has
        already been shown and thus it performed initialization.

        **Note:** This function will typically have to be used in combination
        with a **QSurfaceFormat::setDefaultFormat** () call that sets the color
        space to **QSurfaceFormat::sRGBColorSpace** .

        This function was introduced in Qt 5.10.

        **See also** **textureFormat** ().
        """
        ...
    def setUpdateBehavior(
        self, updateBehavior: PySide6.QtOpenGLWidgets.QOpenGLWidget.UpdateBehavior
    ) -> None:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#setUpdateBehavior

        **[since 5.5] void
        QOpenGLWidget::setUpdateBehavior(QOpenGLWidget::UpdateBehavior
        updateBehavior )**

        Sets this widget's update behavior to **updateBehavior**.

        This function was introduced in Qt 5.5.

        **See also** **updateBehavior** ().
        """
        ...
    def textureFormat(self) -> int:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#textureFormat

        **[since 5.10] GLenum QOpenGLWidget::textureFormat() const**

        Returns the active internal texture format if the widget has already
        initialized, the requested format if one was set but the widget has not
        yet been made visible, or `nullptr` if **setTextureFormat** () was not
        called and the widget has not yet been made visible.

        This function was introduced in Qt 5.10.

        **See also** **setTextureFormat** ().
        """
        ...
    def updateBehavior(self) -> PySide6.QtOpenGLWidgets.QOpenGLWidget.UpdateBehavior:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#updateBehavior

        **[since 5.5] QOpenGLWidget::UpdateBehavior
        QOpenGLWidget::updateBehavior() const**

        Returns the update behavior of the widget.

        This function was introduced in Qt 5.5.

        **See also** **setUpdateBehavior** ().
        """
        ...
    @property
    def aboutToCompose(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#aboutToCompose

        **[signal] void QOpenGLWidget::aboutToCompose()**

        This signal is emitted when the widget's top-level window is about to
        begin composing the textures of its **QOpenGLWidget**  children and the
        other widgets.
        """
        ...
    @property
    def aboutToResize(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#aboutToResize

        **[signal] void QOpenGLWidget::aboutToResize()**

        This signal is emitted when the widget's size is changed and therefore
        the framebuffer object is going to be recreated.
        """
        ...
    @property
    def frameSwapped(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#frameSwapped

        **[signal] void QOpenGLWidget::frameSwapped()**

        This signal is emitted after the widget's top-level window has finished
        composition and returned from its potentially blocking
        **QOpenGLContext::swapBuffers** () call.
        """
        ...
    @property
    def resized(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qopenglwidget.html#resized

        **[signal] void QOpenGLWidget::resized()**

        This signal is emitted right after the framebuffer object has been
        recreated due to resizing the widget.
        """
        ...
