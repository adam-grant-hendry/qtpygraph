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

from enum import IntFlag
from typing import Any, overload

import PySide6.QtCore
import PySide6.QtGui

class QMovie(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qmovie.html

    **Detailed Description**

    This class is used to show simple animations without sound.

    First, create a QMovie object by passing either the name of a file or a
    pointer to a **QIODevice**  containing an animated image format to QMovie's
    constructor. You can call **isValid** () to check if the image data is
    valid, before starting the movie. To start the movie, call **start** ().
    QMovie will enter **Running**  state, and emit **started** () and
    **stateChanged** (). To get the current state of the movie, call **state**
    ().

    To display the movie in your application, you can pass your QMovie object to
    **QLabel::setMovie** (). Example:

    **QLabel**  label;
        **QMovie**  *movie = new **QMovie**
    ("animations/fire.gif");

        label.setMovie(movie);
        movie->start();

    Whenever a new frame is available in the movie, QMovie will emit **updated**
    (). If the size of the frame changes, **resized** () is emitted. You can
    call **currentImage** () or **currentPixmap** () to get a copy of the
    current frame. When the movie is done, QMovie emits **finished** (). If any
    error occurs during playback (i.e, the image file is corrupt), QMovie will
    emit **error** ().

    You can control the speed of the movie playback by calling **setSpeed** (),
    which takes the percentage of the original speed as an argument. Pause the
    movie by calling **setPaused** (true). QMovie will then enter **Paused**
    state and emit **stateChanged** (). If you call **setPaused** (false),
    QMovie will reenter **Running**  state and start the movie again. To stop
    the movie, call **stop** ().

    Certain animation formats allow you to set the background color. You can
    call **setBackgroundColor** () to set the color, or **backgroundColor** ()
    to retrieve the current background color.

    **currentFrameNumber** () returns the sequence number of the current frame.
    The first frame in the animation has the sequence number 0. **frameCount**
    () returns the total number of frames in the animation, if the image format
    supports this. You can call **loopCount** () to get the number of times the
    movie should loop before finishing. **nextFrameDelay** () returns the number
    of milliseconds the current frame should be displayed.

    QMovie can be instructed to cache frames of an animation by calling
    **setCacheMode** ().

    Call **supportedFormats** () for a list of formats that QMovie supports.

    **See also** **QLabel** , **QImageReader** , and **Movie Example** .
    """

    CacheNone: QMovie.CacheMode = ...
    CacheAll: QMovie.CacheMode = ...
    NotRunning: QMovie.MovieState = ...
    Paused: QMovie.MovieState = ...
    Running: QMovie.MovieState = ...

    class CacheMode(IntFlag):
        CacheNone: QMovie.CacheMode = ...
        CacheAll: QMovie.CacheMode = ...

    class MovieState(IntFlag):
        NotRunning: QMovie.MovieState = ...
        Paused: QMovie.MovieState = ...
        Running: QMovie.MovieState = ...
    @overload
    def __init__(
        self,
        device: PySide6.QtCore.QIODevice,
        format: PySide6.QtCore.QByteArray | bytes = ...,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#QMovie

        **QMovie::QMovie(QObject * parent = nullptr)**

        Constructs a QMovie object, passing the **parent** object to **QObject**
        's constructor.

        **See also** **setFileName** (), **setDevice** (), and **setFormat** ().
        """
        ...
    @overload
    def __init__(
        self,
        fileName: str,
        format: PySide6.QtCore.QByteArray | bytes = ...,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#QMovie-1

        **QMovie::QMovie(QIODevice * device , const QByteArray & format =
        QByteArray(), QObject * parent = nullptr)**

        Constructs a QMovie object. QMovie will use read image data from
        **device** , which it assumes is open and readable. If **format** is not
        empty, QMovie will use the image format **format** for decoding the
        image data. Otherwise, QMovie will attempt to guess the format.

        The **parent** object is passed to **QObject** 's constructor.
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#QMovie-2

        **QMovie::QMovie(const QString & fileName , const QByteArray & format =
        QByteArray(), QObject * parent = nullptr)**

        Constructs a QMovie object. QMovie will use read image data from
        **fileName**. If **format** is not empty, QMovie will use the image
        format **format** for decoding the image data. Otherwise, QMovie will
        attempt to guess the format.

        The **parent** object is passed to **QObject** 's constructor.
        """
        ...
    def backgroundColor(self) -> PySide6.QtGui.QColor:
        """
        https://doc.qt.io/qt-6/qmovie.html#backgroundColor

        **QColor QMovie::backgroundColor() const**

        Returns the background color of the movie. If no background color has
        been assigned, an invalid **QColor**  is returned.

        **See also** **setBackgroundColor** ().
        """
        ...
    def cacheMode(self) -> PySide6.QtGui.QMovie.CacheMode:
        """
        https://doc.qt.io/qt-6/qmovie.html#cacheMode-prop

        **[bindable] cacheMode : CacheMode**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the movie's cache mode

        Caching frames can be useful when the underlying animation format
        handler that **QMovie**  relies on to decode the animation data does not
        support jumping to particular frames in the animation, or even
        "rewinding" the animation to the beginning (for looping). Furthermore,
        if the image data comes from a sequential device, it is not possible for
        the underlying animation handler to seek back to frames whose data has
        already been read (making looping altogether impossible).

        To aid in such situations, a **QMovie**  object can be instructed to
        cache the frames, at the added memory cost of keeping the frames in
        memory for the lifetime of the object.

        By default, this property is set to **CacheNone** .

        **See also** **QMovie::CacheMode** .
        """
        ...
    def currentFrameNumber(self) -> int:
        """
        https://doc.qt.io/qt-6/qmovie.html#currentFrameNumber

        **int QMovie::currentFrameNumber() const**

        Returns the sequence number of the current frame. The number of the
        first frame in the movie is 0.
        """
        ...
    def currentImage(self) -> PySide6.QtGui.QImage:
        """
        https://doc.qt.io/qt-6/qmovie.html#currentImage

        **QImage QMovie::currentImage() const**

        Returns the current frame as a **QImage** .

        **See also** **currentPixmap** () and **updated** ().
        """
        ...
    def currentPixmap(self) -> PySide6.QtGui.QPixmap:
        """
        https://doc.qt.io/qt-6/qmovie.html#currentPixmap

        **QPixmap QMovie::currentPixmap() const**

        Returns the current frame as a **QPixmap** .

        **See also** **currentImage** () and **updated** ().
        """
        ...
    def device(self) -> PySide6.QtCore.QIODevice:
        """
        https://doc.qt.io/qt-6/qmovie.html#device

        **QIODevice *QMovie::device() const**

        Returns the device **QMovie**  reads image data from. If no device has
        currently been assigned, `nullptr` is returned.

        **See also** **setDevice** () and **fileName** ().
        """
        ...
    def fileName(self) -> str:
        """
        https://doc.qt.io/qt-6/qmovie.html#fileName

        **QString QMovie::fileName() const**

        Returns the name of the file that **QMovie**  reads image data from. If
        no file name has been assigned, or if the assigned device is not a file,
        an empty **QString**  is returned.

        **See also** **setFileName** () and **device** ().
        """
        ...
    def format(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qmovie.html#format

        **QByteArray QMovie::format() const**

        Returns the format that **QMovie**  uses when decoding image data. If no
        format has been assigned, an empty QByteArray() is returned.

        **See also** **setFormat** ().
        """
        ...
    def frameCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qmovie.html#frameCount

        **int QMovie::frameCount() const**

        Returns the number of frames in the movie.

        Certain animation formats do not support this feature, in which case 0
        is returned.
        """
        ...
    def frameRect(self) -> PySide6.QtCore.QRect:
        """
        https://doc.qt.io/qt-6/qmovie.html#frameRect

        **QRect QMovie::frameRect() const**

        Returns the rect of the last frame. If no frame has yet been updated, an
        invalid **QRect**  is returned.

        **See also** **currentImage** () and **currentPixmap** ().
        """
        ...
    def isValid(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmovie.html#isValid

        **bool QMovie::isValid() const**

        Returns `true` if the movie is valid (e.g., the image data is readable
        and the image format is supported); otherwise returns `false`.

        For information about why the movie is not valid, see **lastError** ().
        """
        ...
    def jumpToFrame(self, frameNumber: int) -> bool:
        """
        https://doc.qt.io/qt-6/qmovie.html#jumpToFrame

        **bool QMovie::jumpToFrame(int frameNumber )**

        Jumps to frame number **frameNumber**. Returns `true` on success;
        otherwise returns `false`.
        """
        ...
    def jumpToNextFrame(self) -> bool:
        """
        https://doc.qt.io/qt-6/qmovie.html#jumpToNextFrame

        **[slot] bool QMovie::jumpToNextFrame()**

        Jumps to the next frame. Returns `true` on success; otherwise returns
        `false`.
        """
        ...
    def lastError(self) -> PySide6.QtGui.QImageReader.ImageReaderError:
        """
        https://doc.qt.io/qt-6/qmovie.html#lastError

        **QImageReader::ImageReaderError QMovie::lastError() const**

        Returns the most recent error that occurred while attempting to read
        image data.

        **See also** **lastErrorString** ().
        """
        ...
    def lastErrorString(self) -> str:
        """
        https://doc.qt.io/qt-6/qmovie.html#lastErrorString

        **QString QMovie::lastErrorString() const**

        Returns a human-readable representation of the most recent error that
        occurred while attempting to read image data.

        **See also** **lastError** ().
        """
        ...
    def loopCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qmovie.html#loopCount

        **int QMovie::loopCount() const**

        Returns the number of times the movie will loop before it finishes. If
        the movie will only play once (no looping), loopCount returns 0. If the
        movie loops forever, loopCount returns -1.

        Note that, if the image data comes from a sequential device (e.g. a
        socket), **QMovie**  can only loop the movie if the **cacheMode**  is
        set to **QMovie::CacheAll** .
        """
        ...
    def nextFrameDelay(self) -> int:
        """
        https://doc.qt.io/qt-6/qmovie.html#nextFrameDelay

        **int QMovie::nextFrameDelay() const**

        Returns the number of milliseconds **QMovie**  will wait before updating
        the next frame in the animation.
        """
        ...
    def scaledSize(self) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qmovie.html#scaledSize

        **QSize QMovie::scaledSize()**

        Returns the scaled size of frames.

        **See also** **setScaledSize** () and **QImageReader::scaledSize** ().
        """
        ...
    def setBackgroundColor(
        self,
        color: (
            PySide6.QtGui.QColor
            | PySide6.QtGui.QRgba64
            | Any
            | PySide6.QtCore.Qt.GlobalColor
            | str
            | int
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#setBackgroundColor

        **void QMovie::setBackgroundColor(const QColor & color )**

        For image formats that support it, this function sets the background
        color to **color**.

        **See also** **backgroundColor** ().
        """
        ...
    def setCacheMode(self, mode: PySide6.QtGui.QMovie.CacheMode) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#cacheMode-prop

        **[bindable] cacheMode : CacheMode**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the movie's cache mode

        Caching frames can be useful when the underlying animation format
        handler that **QMovie**  relies on to decode the animation data does not
        support jumping to particular frames in the animation, or even
        "rewinding" the animation to the beginning (for looping). Furthermore,
        if the image data comes from a sequential device, it is not possible for
        the underlying animation handler to seek back to frames whose data has
        already been read (making looping altogether impossible).

        To aid in such situations, a **QMovie**  object can be instructed to
        cache the frames, at the added memory cost of keeping the frames in
        memory for the lifetime of the object.

        By default, this property is set to **CacheNone** .

        **See also** **QMovie::CacheMode** .
        """
        ...
    def setDevice(self, device: PySide6.QtCore.QIODevice) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#setDevice

        **void QMovie::setDevice(QIODevice * device )**

        Sets the current device to **device**. **QMovie**  will read image data
        from this device when the movie is running.

        **See also** **device** () and **setFormat** ().
        """
        ...
    def setFileName(self, fileName: str) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#setFileName

        **void QMovie::setFileName(const QString & fileName )**

        Sets the name of the file that **QMovie**  reads image data from, to
        **fileName**.

        **See also** **fileName** (), **setDevice** (), and **setFormat** ().
        """
        ...
    def setFormat(self, format: PySide6.QtCore.QByteArray | bytes) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#setFormat

        **void QMovie::setFormat(const QByteArray & format )**

        Sets the format that **QMovie**  will use when decoding image data, to
        **format**. By default, **QMovie**  will attempt to guess the format of
        the image data.

        You can call **supportedFormats** () for the full list of formats
        **QMovie**  supports.

        **See also** **format** () and **QImageReader::supportedImageFormats**
        ().
        """
        ...
    def setPaused(self, paused: bool) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#setPaused

        **[slot] void QMovie::setPaused(bool paused )**

        If **paused** is true, **QMovie**  will enter **Paused**  state and emit
        **stateChanged** (Paused); otherwise it will enter **Running**  state
        and emit **stateChanged** (Running).

        **See also** **state** ().
        """
        ...
    def setScaledSize(self, size: PySide6.QtCore.QSize) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#setScaledSize

        **void QMovie::setScaledSize(const QSize & size )**

        Sets the scaled frame size to **size**.

        **See also** **scaledSize** () and **QImageReader::setScaledSize** ().
        """
        ...
    def setSpeed(self, percentSpeed: int) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#speed-prop

        **[bindable] speed : int**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the movie's speed

        The speed is measured in percentage of the original movie speed. The
        default speed is 100%. Example:

        **QMovie**  movie("racecar.gif");
            movie.setSpeed(200); // 2x speed

        **Member Function Documentation**
        """
        ...
    def speed(self) -> int:
        """
        https://doc.qt.io/qt-6/qmovie.html#speed-prop

        **[bindable] speed : int**

        **Note:** This property supports **QProperty**  bindings.

        This property holds the movie's speed

        The speed is measured in percentage of the original movie speed. The
        default speed is 100%. Example:

        **QMovie**  movie("racecar.gif");
            movie.setSpeed(200); // 2x speed

        **Member Function Documentation**
        """
        ...
    def start(self) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#start

        **[slot] void QMovie::start()**

        Starts the movie. **QMovie**  will enter **Running**  state, and start
        emitting **updated** () and **resized** () as the movie progresses.

        If **QMovie**  is in the **Paused**  state, this function is equivalent
        to calling **setPaused** (false). If **QMovie**  is already in the
        **Running**  state, this function does nothing.

        **See also** **stop** () and **setPaused** ().
        """
        ...
    def state(self) -> PySide6.QtGui.QMovie.MovieState:
        """
        https://doc.qt.io/qt-6/qmovie.html#state

        **QMovie::MovieState QMovie::state() const**

        Returns the current state of **QMovie** .

        **See also** **MovieState**  and **stateChanged** ().
        """
        ...
    def stop(self) -> None:
        """
        https://doc.qt.io/qt-6/qmovie.html#stop

        **[slot] void QMovie::stop()**

        Stops the movie. **QMovie**  enters **NotRunning**  state, and stops
        emitting **updated** () and **resized** (). If **start** () is called
        again, the movie will restart from the beginning.

        If **QMovie**  is already in the **NotRunning**  state, this function
        does nothing.

        **See also** **start** () and **setPaused** ().
        """
        ...
    @staticmethod
    def supportedFormats() -> list[PySide6.QtCore.QByteArray]:
        """
        https://doc.qt.io/qt-6/qmovie.html#supportedFormats

        **[static] QList<QByteArray> QMovie::supportedFormats()**

        Returns the list of image formats supported by **QMovie** .

        **See also** **QImageReader::supportedImageFormats** ().
        """
        ...
    @property
    def error(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qmovie.html#error

        **[signal] void QMovie::error(QImageReader::ImageReaderError error )**

        This signal is emitted by **QMovie**  when the error **error** occurred
        during playback. **QMovie**  will stop the movie, and enter
        **QMovie::NotRunning**  state.

        **See also** **lastError** () and **lastErrorString** ().
        """
        ...
    @property
    def finished(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qmovie.html#finished

        **[signal] void QMovie::finished()**

        This signal is emitted when the movie has finished.

        **See also** **QMovie::stop** ().
        """
        ...
    @property
    def frameChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qmovie.html#frameChanged

        **[signal] void QMovie::frameChanged(int frameNumber )**

        This signal is emitted when the frame number has changed to
        **frameNumber**. You can call **currentImage** () or **currentPixmap**
        () to get a copy of the frame.
        """
        ...
    @property
    def resized(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qmovie.html#resized

        **[signal] void QMovie::resized(const QSize & size )**

        This signal is emitted when the current frame has been resized to
        **size**. This effect is sometimes used in animations as an alternative
        to replacing the frame. You can call **currentImage** () or
        **currentPixmap** () to get a copy of the updated frame.
        """
        ...
    @property
    def started(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qmovie.html#started

        **[signal] void QMovie::started()**

        This signal is emitted after **QMovie::start** () has been called, and
        **QMovie**  has entered **QMovie::Running**  state.
        """
        ...
    @property
    def stateChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qmovie.html#stateChanged

        **[signal] void QMovie::stateChanged(QMovie::MovieState state )**

        This signal is emitted every time the state of the movie changes. The
        new state is specified by **state**.

        **See also** **QMovie::state** ().
        """
        ...
    @property
    def updated(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qmovie.html#updated

        **[signal] void QMovie::updated(const QRect & rect )**

        This signal is emitted when the rect **rect** in the current frame has
        been updated. You can call **currentImage** () or **currentPixmap** ()
        to get a copy of the updated frame.
        """
        ...