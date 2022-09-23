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
PySide6.QtOpenGL, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtOpenGL

class QOpenGLVertexArrayObject(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qopenglvertexarrayobject.html

    **Detailed Description**

    A Vertex Array Object (VAO) is an OpenGL container object that encapsulates
    the state needed to specify per-vertex attribute data to the OpenGL
    pipeline. To put it another way, a VAO remembers the states of buffer
    objects (see **QOpenGLBuffer** ) and their associated state (e.g. vertex
    attribute divisors). This allows a very easy and efficient method of
    switching between OpenGL buffer states for rendering different "objects" in
    a scene. The QOpenGLVertexArrayObject class is a thin wrapper around an
    OpenGL VAO.

    For the desktop, VAOs are supported as a core feature in OpenGL 3.0 or newer
    and by the GL_ARB_vertex_array_object for older versions. On OpenGL ES 2,
    VAOs are provided by the optional GL_OES_vertex_array_object extension. You
    can check the version of OpenGL with QOpenGLContext::surfaceFormat() and
    check for the presence of extensions with **QOpenGLContext::hasExtension**
    ().

    As with the other Qt OpenGL classes, QOpenGLVertexArrayObject has a
    **create** () function to create the underlying OpenGL object. This is to
    allow the developer to ensure that there is a valid current OpenGL context
    at the time.

    Once you have successfully created a VAO the typical usage pattern is:

    * In scene initialization function, for each visual object:
        * Bind the
    VAO
        * Set vertex data state for this visual object (vertices, normals,
    texture coordinates etc.)
        * Unbind (**release** ()) the VAO
      * In
    render function, for each visual object:
        * Bind the VAO (and shader
    program if needed)
        * Call a glDraw*() function
        * Unbind (**release**
    ()) the VAO

    The act of binding the VAO in the render function has the effect of
    restoring all of the vertex data state setup in the initialization phase. In
    this way we can set a great deal of state when setting up a VAO and
    efficiently switch between state sets of objects to be rendered. Using VAOs
    also allows the OpenGL driver to amortise the validation checks of the
    vertex data.

    **Note:** Vertex Array Objects, like all other OpenGL container objects, are
    specific to the context for which they were created and cannot be shared
    amongst a context group.

    **See also** **QOpenGLVertexArrayObject::Binder**  and **QOpenGLBuffer** .
    """

    class Binder:
        def __init__(self, v: PySide6.QtOpenGL.QOpenGLVertexArrayObject) -> None: ...
        def rebind(self) -> None: ...
        def release(self) -> None: ...

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#QOpenGLVertexArrayO
        bject

        **QOpenGLVertexArrayObject::QOpenGLVertexArrayObject(QObject * parent =
        nullptr)**

        Creates a QOpenGLVertexArrayObject with the given **parent**. You must
        call **create** () with a valid OpenGL context before using.
        """
        ...
    def bind(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#bind

        **void QOpenGLVertexArrayObject::bind()**

        Binds this vertex array object to the OpenGL binding point. From this
        point on and until **release** () is called or another vertex array
        object is bound, any modifications made to vertex data state are stored
        inside this vertex array object.

        If another vertex array object is then bound you can later restore the
        set of state associated with this object by calling bind() on this
        object once again. This allows efficient changes between vertex data
        states in rendering functions.
        """
        ...
    def create(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#create

        **bool QOpenGLVertexArrayObject::create()**

        Creates the underlying OpenGL vertex array object. There must be a valid
        OpenGL context that supports vertex array objects current for this
        function to succeed.

        Returns `true` if the OpenGL vertex array object was successfully
        created.

        When the return value is `false`, vertex array object support is not
        available. This is not an error: on systems with OpenGL 2.x or OpenGL ES
        2.0 vertex array objects may not be supported. The application is free
        to continue execution in this case, but it then has to be prepared to
        operate in a VAO-less manner too. This means that instead of merely
        calling **bind** (), the value of **isCreated** () must be checked and
        the vertex arrays has to be initialized in the traditional way when
        there is no vertex array object present.

        **See also** **isCreated** ().
        """
        ...
    def destroy(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#destroy

        **void QOpenGLVertexArrayObject::destroy()**

        Destroys the underlying OpenGL vertex array object. There must be a
        valid OpenGL context that supports vertex array objects current for this
        function to succeed.
        """
        ...
    def isCreated(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#isCreated

        **bool QOpenGLVertexArrayObject::isCreated() const**

        Returns `true` is the underlying OpenGL vertex array object has been
        created. If this returns `true` and the associated OpenGL context is
        current, then you are able to **bind** () this object.
        """
        ...
    def objectId(self) -> int:
        """
        https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#objectId

        **GLuint QOpenGLVertexArrayObject::objectId() const**

        Returns the id of the underlying OpenGL vertex array object.
        """
        ...
    def release(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#release

        **void QOpenGLVertexArrayObject::release()**

        Unbinds this vertex array object by binding the default vertex array
        object (id = 0).
        """
        ...
