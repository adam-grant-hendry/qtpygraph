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

from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtOpenGL

class QOpenGLBuffer:
    """
    https://doc.qt.io/qt-6/qopenglbuffer.html

    **Detailed Description**

    Buffer objects are created in the OpenGL server so that the client
    application can avoid uploading vertices, indices, texture image data, etc
    every time they are needed.

    QOpenGLBuffer objects can be copied around as a reference to the underlying
    OpenGL buffer object:

    **QOpenGLBuffer**  buffer1(**QOpenGLBuffer** ::IndexBuffer);
    buffer1.create();

        **QOpenGLBuffer**  buffer2 = buffer1;

    QOpenGLBuffer performs a shallow copy when objects are copied in this
    manner, but does not implement copy-on-write semantics. The original object
    will be affected whenever the copy is modified.
    """

    ReadOnly: QOpenGLBuffer.Access = ...
    WriteOnly: QOpenGLBuffer.Access = ...
    ReadWrite: QOpenGLBuffer.Access = ...
    RangeRead: QOpenGLBuffer.RangeAccessFlag = ...
    RangeWrite: QOpenGLBuffer.RangeAccessFlag = ...
    RangeInvalidate: QOpenGLBuffer.RangeAccessFlag = ...
    RangeInvalidateBuffer: QOpenGLBuffer.RangeAccessFlag = ...
    RangeFlushExplicit: QOpenGLBuffer.RangeAccessFlag = ...
    RangeUnsynchronized: QOpenGLBuffer.RangeAccessFlag = ...
    VertexBuffer: QOpenGLBuffer.Type = ...
    IndexBuffer: QOpenGLBuffer.Type = ...
    PixelPackBuffer: QOpenGLBuffer.Type = ...
    PixelUnpackBuffer: QOpenGLBuffer.Type = ...
    StreamDraw: QOpenGLBuffer.UsagePattern = ...
    StreamRead: QOpenGLBuffer.UsagePattern = ...
    StreamCopy: QOpenGLBuffer.UsagePattern = ...
    StaticDraw: QOpenGLBuffer.UsagePattern = ...
    StaticRead: QOpenGLBuffer.UsagePattern = ...
    StaticCopy: QOpenGLBuffer.UsagePattern = ...
    DynamicDraw: QOpenGLBuffer.UsagePattern = ...
    DynamicRead: QOpenGLBuffer.UsagePattern = ...
    DynamicCopy: QOpenGLBuffer.UsagePattern = ...

    class Access(IntFlag):
        ReadOnly: QOpenGLBuffer.Access = ...
        WriteOnly: QOpenGLBuffer.Access = ...
        ReadWrite: QOpenGLBuffer.Access = ...

    class RangeAccessFlag(IntFlag):
        RangeRead: QOpenGLBuffer.RangeAccessFlag = ...
        RangeWrite: QOpenGLBuffer.RangeAccessFlag = ...
        RangeInvalidate: QOpenGLBuffer.RangeAccessFlag = ...
        RangeInvalidateBuffer: QOpenGLBuffer.RangeAccessFlag = ...
        RangeFlushExplicit: QOpenGLBuffer.RangeAccessFlag = ...
        RangeUnsynchronized: QOpenGLBuffer.RangeAccessFlag = ...

    class RangeAccessFlags: ...

    class Type(IntFlag):
        VertexBuffer: QOpenGLBuffer.Type = ...
        IndexBuffer: QOpenGLBuffer.Type = ...
        PixelPackBuffer: QOpenGLBuffer.Type = ...
        PixelUnpackBuffer: QOpenGLBuffer.Type = ...

    class UsagePattern(IntFlag):
        StreamDraw: QOpenGLBuffer.UsagePattern = ...
        StreamRead: QOpenGLBuffer.UsagePattern = ...
        StreamCopy: QOpenGLBuffer.UsagePattern = ...
        StaticDraw: QOpenGLBuffer.UsagePattern = ...
        StaticRead: QOpenGLBuffer.UsagePattern = ...
        StaticCopy: QOpenGLBuffer.UsagePattern = ...
        DynamicDraw: QOpenGLBuffer.UsagePattern = ...
        DynamicRead: QOpenGLBuffer.UsagePattern = ...
        DynamicCopy: QOpenGLBuffer.UsagePattern = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#QOpenGLBuffer

        **QOpenGLBuffer::QOpenGLBuffer()**

        Constructs a new buffer object of type **QOpenGLBuffer::VertexBuffer** .

        Note: this constructor just creates the QOpenGLBuffer instance. The
        actual buffer object in the OpenGL server is not created until
        **create** () is called.

        **See also** **create** ().
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtOpenGL.QOpenGLBuffer) -> None:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#QOpenGLBuffer-1

        **QOpenGLBuffer::QOpenGLBuffer(QOpenGLBuffer::Type type )**

        Constructs a new buffer object of **type**.

        Note: this constructor just creates the QOpenGLBuffer instance. The
        actual buffer object in the OpenGL server is not created until
        **create** () is called.

        **See also** **create** ().
        """
        ...
    @overload
    def __init__(self, type: PySide6.QtOpenGL.QOpenGLBuffer.Type) -> None:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#QOpenGLBuffer-2

        **QOpenGLBuffer::QOpenGLBuffer(const QOpenGLBuffer & other )**

        Constructs a shallow copy of **other**.

        Note: QOpenGLBuffer does not implement copy-on-write semantics, so
        **other** will be affected whenever the copy is modified.
        """
        ...
    @overload
    def allocate(self, count: int) -> None:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#allocate

        **void QOpenGLBuffer::allocate(const void * data , int count )**

        Allocates **count** bytes of space to the buffer, initialized to the
        contents of **data**. Any previous contents will be removed.

        It is assumed that **create** () has been called on this buffer and that
        it has been bound to the current context.

        **See also** **create** (), **read** (), and **write** ().
        """
        ...
    @overload
    def allocate(self, data: int, count: int) -> None:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#allocate-1

        **void QOpenGLBuffer::allocate(int count )**

        This is an overloaded function.

        Allocates **count** bytes of space to the buffer. Any previous contents
        will be removed.

        It is assumed that **create** () has been called on this buffer and that
        it has been bound to the current context.

        **See also** **create** () and **write** ().
        """
        ...
    def bind(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#bind

        **bool QOpenGLBuffer::bind()**

        Binds the buffer associated with this object to the current OpenGL
        context. Returns `false` if binding was not possible, usually because
        **type** () is not supported on this OpenGL implementation.

        The buffer must be bound to the same **QOpenGLContext**  current when
        **create** () was called, or to another **QOpenGLContext**  that is
        sharing with it. Otherwise, false will be returned from this function.

        **See also** **release** () and **create** ().
        """
        ...
    def bufferId(self) -> int:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#bufferId

        **GLuint QOpenGLBuffer::bufferId() const**

        Returns the OpenGL identifier associated with this buffer; zero if the
        buffer has not been created.

        **See also** **isCreated** ().
        """
        ...
    def create(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#create

        **bool QOpenGLBuffer::create()**

        Creates the buffer object in the OpenGL server. Returns `true` if the
        object was created; false otherwise.

        This function must be called with a current **QOpenGLContext** . The
        buffer will be bound to and can only be used in that context (or any
        other context that is shared with it).

        This function will return false if the OpenGL implementation does not
        support buffers, or there is no current **QOpenGLContext** .

        **See also** **isCreated** (), **allocate** (), **write** (), and
        **destroy** ().
        """
        ...
    def destroy(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#destroy

        **void QOpenGLBuffer::destroy()**

        Destroys this buffer object, including the storage being used in the
        OpenGL server. All references to the buffer will become invalid.
        """
        ...
    def isCreated(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#isCreated

        **bool QOpenGLBuffer::isCreated() const**

        Returns `true` if this buffer has been created; false otherwise.

        **See also** **create** () and **destroy** ().
        """
        ...
    def map(self, access: PySide6.QtOpenGL.QOpenGLBuffer.Access) -> int:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#map

        **void *QOpenGLBuffer::map(QOpenGLBuffer::Access access )**

        Maps the contents of this buffer into the application's memory space and
        returns a pointer to it. Returns null if memory mapping is not possible.
        The **access** parameter indicates the type of access to be performed.

        It is assumed that **create** () has been called on this buffer and that
        it has been bound to the current context.

        **Note:** This function is only supported under OpenGL ES 2.0 or earlier
        if the `GL_OES_mapbuffer` extension is present.

        **Note:** On OpenGL ES 3.0 and newer, or, in case if desktop OpenGL, if
        `GL_ARB_map_buffer_range` is supported, this function uses
        `glMapBufferRange` instead of `glMapBuffer`.

        **See also** **unmap** (), **create** (), **bind** (), and **mapRange**
        ().
        """
        ...
    def mapRange(
        self,
        offset: int,
        count: int,
        access: PySide6.QtOpenGL.QOpenGLBuffer.RangeAccessFlags,
    ) -> int:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#mapRange

        **void *QOpenGLBuffer::mapRange(int offset , int count ,
        QOpenGLBuffer::RangeAccessFlags access )**

        Maps the range specified by **offset** and **count** of the contents of
        this buffer into the application's memory space and returns a pointer to
        it. Returns null if memory mapping is not possible. The **access**
        parameter specifies a combination of access flags.

        It is assumed that **create** () has been called on this buffer and that
        it has been bound to the current context.

        **Note:** This function is not available on OpenGL ES 2.0 and earlier.

        **See also** **unmap** (), **create** (), and **bind** ().
        """
        ...
    def read(self, offset: int, data: int, count: int) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#read

        **bool QOpenGLBuffer::read(int offset , void * data , int count )**

        Reads the **count** bytes in this buffer starting at **offset** into
        **data**. Returns `true` on success; false if reading from the buffer is
        not supported. Buffer reading is not supported under OpenGL/ES.

        It is assumed that this buffer has been bound to the current context.

        **See also** **write** () and **bind** ().
        """
        ...
    @overload
    def release(self) -> None:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#release

        **void QOpenGLBuffer::release()**

        Releases the buffer associated with this object from the current OpenGL
        context.

        This function must be called with the same **QOpenGLContext**  current
        as when **bind** () was called on the buffer.

        **See also** **bind** ().
        """
        ...
    @overload
    @staticmethod
    def release(type: PySide6.QtOpenGL.QOpenGLBuffer.Type) -> None:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#release-1

        **[static] void QOpenGLBuffer::release(QOpenGLBuffer::Type type )**

        Releases the buffer associated with **type** in the current
        **QOpenGLContext** .

        This function is a direct call to `glBindBuffer(type, 0)` for use when
        the caller does not know which **QOpenGLBuffer**  has been bound to the
        context but wants to make sure that it is released.

        **QOpenGLBuffer** ::release(**QOpenGLBuffer** ::VertexBuffer);
        """
        ...
    def setUsagePattern(self, value: PySide6.QtOpenGL.QOpenGLBuffer.UsagePattern) -> None:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#setUsagePattern

        **void QOpenGLBuffer::setUsagePattern(QOpenGLBuffer::UsagePattern value
        )**

        Sets the usage pattern for this buffer object to **value**. This
        function must be called before **allocate** () or **write** ().

        **See also** **usagePattern** (), **allocate** (), and **write** ().
        """
        ...
    def size(self) -> int:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#size

        **int QOpenGLBuffer::size() const**

        Returns the size of the data in this buffer, for reading operations.
        Returns -1 if fetching the buffer size is not supported, or the buffer
        has not been created.

        It is assumed that this buffer has been bound to the current context.

        **See also** **isCreated** () and **bind** ().
        """
        ...
    def type(self) -> PySide6.QtOpenGL.QOpenGLBuffer.Type:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#type

        **QOpenGLBuffer::Type QOpenGLBuffer::type() const**

        Returns the type of buffer represented by this object.
        """
        ...
    def unmap(self) -> bool:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#unmap

        **bool QOpenGLBuffer::unmap()**

        Unmaps the buffer after it was mapped into the application's memory
        space with a previous call to **map** (). Returns `true` if the unmap
        succeeded; false otherwise.

        It is assumed that this buffer has been bound to the current context,
        and that it was previously mapped with **map** ().

        **Note:** This function is only supported under OpenGL ES 2.0 and
        earlier if the `GL_OES_mapbuffer` extension is present.

        **See also** **map** ().
        """
        ...
    def usagePattern(self) -> PySide6.QtOpenGL.QOpenGLBuffer.UsagePattern:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#usagePattern

        **QOpenGLBuffer::UsagePattern QOpenGLBuffer::usagePattern() const**

        Returns the usage pattern for this buffer object. The default value is
        **StaticDraw** .

        **See also** **setUsagePattern** ().
        """
        ...
    def write(self, offset: int, data: int, count: int) -> None:
        """
        https://doc.qt.io/qt-6/qopenglbuffer.html#write

        **void QOpenGLBuffer::write(int offset , const void * data , int count
        )**

        Replaces the **count** bytes of this buffer starting at **offset** with
        the contents of **data**. Any other bytes in the buffer will be left
        unmodified.

        It is assumed that **create** () has been called on this buffer and that
        it has been bound to the current context.

        **See also** **create** (), **read** (), and **allocate** ().
        """
        ...
