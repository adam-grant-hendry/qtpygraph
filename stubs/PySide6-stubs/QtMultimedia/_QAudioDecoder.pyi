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
PySide6.QtMultimedia, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtMultimedia

class QAudioDecoder(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qaudiodecoder.html

    **Detailed Description**

    The QAudioDecoder class is a high level class for decoding audio media
    files. It is similar to the **QMediaPlayer**  class except that audio is
    provided back through this API rather than routed directly to audio
    hardware.

    **See also** **QAudioBuffer** .
    """

    NoError: QAudioDecoder.Error = ...
    ResourceError: QAudioDecoder.Error = ...
    FormatError: QAudioDecoder.Error = ...
    AccessDeniedError: QAudioDecoder.Error = ...
    NotSupportedError: QAudioDecoder.Error = ...

    class Error(IntFlag):
        NoError: QAudioDecoder.Error = ...
        ResourceError: QAudioDecoder.Error = ...
        FormatError: QAudioDecoder.Error = ...
        AccessDeniedError: QAudioDecoder.Error = ...
        NotSupportedError: QAudioDecoder.Error = ...
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#QAudioDecoder

        **QAudioDecoder::QAudioDecoder(QObject * parent = nullptr)**

        Construct an QAudioDecoder instance with **parent**.
        """
        ...
    def audioFormat(self) -> PySide6.QtMultimedia.QAudioFormat:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#audioFormat

        **QAudioFormat QAudioDecoder::audioFormat() const**

        Returns the audio format the decoder is set to.

        **Note:** This may be different than the format of the decoded samples,
        if the audio format was set to an invalid one.

        **See also** **setAudioFormat** () and **formatChanged** ().
        """
        ...
    def bufferAvailable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#bufferAvailable

        **bool QAudioDecoder::bufferAvailable() const**

        Returns true if a buffer is available to be read, and false otherwise.
        If there is no buffer available, calling the **read** () function will
        return an invalid buffer.

        **Note:** Getter function for property bufferAvailable.
        """
        ...
    def duration(self) -> int:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#duration

        **qint64 QAudioDecoder::duration() const**

        Returns total duration (in milliseconds) of the audio stream or -1 if
        not available.
        """
        ...
    def errorString(self) -> str:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#errorString

        **QString QAudioDecoder::errorString() const**

        Returns a human readable description of the current error, or an empty
        string is there is no error.

        **Note:** Getter function for property **error** .
        """
        ...
    def isDecoding(self) -> bool:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#isDecoding-prop

        **[read-only] isDecoding : const bool**

        `true` if the decoder is currently running and decoding audio data.

        **Access functions:**

        bool **isDecoding** () const

        **Notifier signal:**

        void **isDecodingChanged** (bool)
        """
        ...
    def isSupported(self) -> bool:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#isSupported

        **bool QAudioDecoder::isSupported() const**

        Returns true is audio decoding is supported on this platform.
        """
        ...
    def position(self) -> int:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#position

        **qint64 QAudioDecoder::position() const**

        Returns position (in milliseconds) of the last buffer read from the
        decoder or -1 if no buffers have been read.
        """
        ...
    def read(self) -> PySide6.QtMultimedia.QAudioBuffer:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#read

        **QAudioBuffer QAudioDecoder::read() const**

        Read a buffer from the decoder, if one is available. Returns an invalid
        buffer if there are no decoded buffers currently available, or on
        failure. In both cases this function will not block.

        You should either respond to the **bufferReady** () signal or check the
        **bufferAvailable** () function before calling read() to make sure you
        get useful data.
        """
        ...
    def setAudioFormat(self, format: PySide6.QtMultimedia.QAudioFormat) -> None:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#setAudioFormat

        **void QAudioDecoder::setAudioFormat(const QAudioFormat & format )**

        Set the desired audio format for decoded samples to **format**.

        This property can only be set while the decoder is stopped. Setting this
        property at other times will be ignored.

        If the decoder does not support this format, **error** () will be set to
        `FormatError`.

        If you do not specify a format, the format of the decoded audio itself
        will be used. Otherwise, some format conversion will be applied.

        If you wish to reset the decoded format to that of the original audio
        file, you can specify an invalid **format**.

        **Warning:** Setting a desired audio format is not yet supported on
        Android.

        **See also** **audioFormat** ().
        """
        ...
    def setSource(self, fileName: PySide6.QtCore.QUrl | str) -> None:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#setSource

        **void QAudioDecoder::setSource(const QUrl & fileName )**

        Sets the current audio file name to **fileName**.

        When this property is set any current decoding is stopped, and any audio
        buffers are discarded.

        You can only specify either a source filename or a source **QIODevice**
        . Setting one will unset the other.

        **Note:** Setter function for property **source** .

        **See also** **source** ().
        """
        ...
    def setSourceDevice(self, device: PySide6.QtCore.QIODevice) -> None:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#setSourceDevice

        **void QAudioDecoder::setSourceDevice(QIODevice * device )**

        Sets the current audio **QIODevice**  to **device**.

        When this property is set any current decoding is stopped, and any audio
        buffers are discarded.

        You can only specify either a source filename or a source **QIODevice**
        . Setting one will unset the other.

        **See also** **sourceDevice** ().
        """
        ...
    def source(self) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#source

        **QUrl QAudioDecoder::source() const**

        Returns the current file name to decode. If **setSourceDevice**  was
        called, this will be empty.

        **Note:** Getter function for property source.

        **See also** **setSource** ().
        """
        ...
    def sourceDevice(self) -> PySide6.QtCore.QIODevice:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#sourceDevice

        **QIODevice *QAudioDecoder::sourceDevice() const**

        Returns the current source **QIODevice** , if one was set. If
        **setSource** () was called, this will be a nullptr.

        **See also** **setSourceDevice** ().
        """
        ...
    def start(self) -> None:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#start

        **[slot] void QAudioDecoder::start()**

        Starts decoding the audio resource.

        As data gets decoded, the **bufferReady** () signal will be emitted when
        enough data has been decoded. Calling **read** () will then return an
        audio buffer without blocking.

        If you call **read** () before a buffer is ready, an invalid buffer will
        be returned, again without blocking.

        **See also** **read** ().
        """
        ...
    def stop(self) -> None:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#stop

        **[slot] void QAudioDecoder::stop()**

        Stop decoding audio. Calling **start** () again will resume decoding
        from the beginning.
        """
        ...
    @property
    def bufferAvailableChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#bufferAvailableChanged

        **[signal] void QAudioDecoder::bufferAvailableChanged(bool available )**

        Signals the availability (if **available** is true) of a new buffer.

        If **available** is false, there are no buffers available.

        **Note:** Notifier signal for property **bufferAvailable** .

        **See also** **bufferAvailable** () and **bufferReady** ().
        """
        ...
    @property
    def bufferReady(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#bufferReady

        **[signal] void QAudioDecoder::bufferReady()**

        Signals that a new decoded audio buffer is available to be read.

        **See also** **read** () and **bufferAvailable** ().
        """
        ...
    @property
    def durationChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#durationChanged

        **[signal] void QAudioDecoder::durationChanged(qint64 duration )**

        Signals that the estimated **duration** of the decoded data has changed.

        **See also** **positionChanged** ().
        """
        ...
    @property
    def error(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#error-prop

        **[read-only] error : const QString**

        This property holds the current error state.

        **Access functions:**

        QString ****errorString** ** () const
        """
        ...
    @property
    def finished(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#finished

        **[signal] void QAudioDecoder::finished()**

        Signals that the decoding has finished successfully. If decoding fails,
        error signal is emitted instead.

        **See also** **start** (), **stop** (), and **error** ().
        """
        ...
    @property
    def formatChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#formatChanged

        **[signal] void QAudioDecoder::formatChanged(const QAudioFormat & format
        )**

        Signals that the current audio format of the decoder has changed to
        **format**.

        **See also** **audioFormat** () and **setAudioFormat** ().
        """
        ...
    @property
    def isDecodingChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def positionChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#positionChanged

        **[signal] void QAudioDecoder::positionChanged(qint64 position )**

        Signals that the current **position** of the decoder has changed.

        **See also** **durationChanged** ().
        """
        ...
    @property
    def sourceChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qaudiodecoder.html#sourceChanged

        **[signal] void QAudioDecoder::sourceChanged()**

        Signals that the current source of the decoder has changed.

        **Note:** Notifier signal for property **source** .

        **See also** **source** () and **sourceDevice** ().
        """
        ...