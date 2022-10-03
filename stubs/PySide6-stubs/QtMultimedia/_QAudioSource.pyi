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

from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtMultimedia

class QAudioSource(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qaudiosource.html

    **Detailed Description**

    You can construct an audio input with the system's default audio input
    device. It is also possible to create QAudioSource with a specific
    **QAudioDevice** . When you create the audio input, you should also send in
    the **QAudioFormat**  to be used for the recording (see the **QAudioFormat**
    class description for details).

    To record to a file:

    QAudioSource lets you record audio with an audio input device. The default
    constructor of this class will use the systems default audio device, but you
    can also specify a **QAudioDevice**  for a specific device. You also need to
    pass in the **QAudioFormat**  in which you wish to record.

    Starting up the QAudioSource is simply a matter of calling **start** () with
    a **QIODevice**  opened for writing. For instance, to record to a file, you
    can:

    **QFile**  destinationFile;   // Class member
        **QAudioSource** * audio;
    // Class member
        {
            destinationFile.setFileName("/tmp/test.raw");
    destinationFile.open( **QIODevice** ::WriteOnly | **QIODevice** ::Truncate
    );

            **QAudioFormat**  format;
            // Set up the desired
    format, for example:
            format.setSampleRate(8000);
    format.setChannelCount(1);
            format.setSampleFormat(**QAudioFormat**
    ::UInt8);

            **QAudioDevice**  info = **QMediaDevices**
    ::defaultAudioInput();
            if (!info.isFormatSupported(format)) {
    **qWarning** () << "Default format not supported, trying to use the
    nearest.";
            }

            audio = new **QAudioSource** (format,
    this);
            connect(audio, SIGNAL(stateChanged(QAudio::State)), this,
    SLOT(handleStateChanged(QAudio::State)));

            **QTimer**
    ::singleShot(3000, this, SLOT(stopRecording()));
    audio->start(&destinationFile);
            // Records audio for 3000ms
        }

    This will start recording if the format specified is supported by the input
    device (you can check this with **QAudioDevice::isFormatSupported** (). In
    case there are any snags, use the **error** () function to check what went
    wrong. We stop recording in the `stopRecording()` slot.

    void AudioInputExample::stopRecording()
        {
            audio->stop();
    destinationFile.close();
            delete audio;
        }

    At any point in time, QAudioSource will be in one of four states: active,
    suspended, stopped, or idle. These states are specified by the
    **QAudio::State**  enum. You can request a state change directly through
    **suspend** (), **resume** (), **stop** (), **reset** (), and **start** ().
    The current state is reported by **state** (). **QAudioSink**  will also
    signal you when the state changes (**stateChanged** ()).

    QAudioSource provides several ways of measuring the time that has passed
    since the **start** () of the recording. The `processedUSecs()` function
    returns the length of the stream in microseconds written, i.e., it leaves
    out the times the audio input was suspended or idle. The **elapsedUSecs** ()
    function returns the time elapsed since **start** () was called regardless
    of which states the QAudioSource has been in.

    If an error should occur, you can fetch its reason with **error** (). The
    possible error reasons are described by the **QAudio::Error**  enum. The
    QAudioSource will enter the **StoppedState**  when an error is encountered.
    Connect to the **stateChanged** () signal to handle the error:

    void AudioInputExample::handleStateChanged(QAudio::State newState)
        {
    switch (newState) {
                case QAudio::StoppedState:
    if (audio->error() != QAudio::NoError) {
                        // Error
    handling
                    } else {
                        // Finished recording
    }
                    break;

                case QAudio::ActiveState:
    // Started recording - read from IO device
                    break;
    default:
                    // ... other cases as appropriate
    break;
            }
        }

    **See also** **QAudioSink**  and **QAudioDevice** .
    """

    @overload
    def __init__(
        self,
        audioDeviceInfo: PySide6.QtMultimedia.QAudioDevice,
        format: PySide6.QtMultimedia.QAudioFormat = ...,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#QAudioSource

        **QAudioSource::QAudioSource(const QAudioFormat & format =
        QAudioFormat(), QObject * parent = nullptr)**

        Construct a new audio input and attach it to **parent**. The default
        audio input device is used with the output **format** parameters.
        """
        ...
    @overload
    def __init__(
        self,
        format: PySide6.QtMultimedia.QAudioFormat = ...,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#QAudioSource-1

        **QAudioSource::QAudioSource(const QAudioDevice & audioDevice , const
        QAudioFormat & format = QAudioFormat(), QObject * parent = nullptr)**

        Construct a new audio input and attach it to **parent**. The device
        referenced by **audioDevice** is used with the input **format**
        parameters.
        """
        ...
    def bufferSize(self) -> int:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#bufferSize

        **qsizetype QAudioSource::bufferSize() const**

        Returns the audio buffer size in bytes.

        If called before **start** (), returns platform default value. If called
        before **start** () but **setBufferSize** () was called prior, returns
        value set by **setBufferSize** (). If called after **start** (), returns
        the actual buffer size being used. This may not be what was set
        previously by **setBufferSize** ().

        **See also** **setBufferSize** ().
        """
        ...
    def bytesAvailable(self) -> int:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#bytesAvailable

        **qsizetype QAudioSource::bytesAvailable() const**

        Returns the amount of audio data available to read in bytes.

        Note: returned value is only valid while in **QAudio::ActiveState**  or
        **QAudio::IdleState**  state, otherwise returns zero.
        """
        ...
    def elapsedUSecs(self) -> int:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#elapsedUSecs

        **qint64 QAudioSource::elapsedUSecs() const**

        Returns the microseconds since **start** () was called, including time
        in Idle and Suspend states.
        """
        ...
    def error(self) -> PySide6.QtMultimedia.QAudio.Error:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#error

        **QAudio::Error QAudioSource::error() const**

        Returns the error state.
        """
        ...
    def format(self) -> PySide6.QtMultimedia.QAudioFormat:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#format

        **QAudioFormat QAudioSource::format() const**

        Returns the **QAudioFormat**  being used.
        """
        ...
    def isNull(self) -> bool: ...
    def processedUSecs(self) -> int:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#processedUSecs

        **qint64 QAudioSource::processedUSecs() const**

        Returns the amount of audio data processed since **start** () was called
        in microseconds.
        """
        ...
    def reset(self) -> None:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#reset

        **void QAudioSource::reset()**

        Drops all audio data in the buffers, resets buffers to zero.
        """
        ...
    def resume(self) -> None:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#resume

        **void QAudioSource::resume()**

        Resumes processing audio data after a **suspend** ().

        Sets **error** () to **QAudio::NoError** . Sets **state** () to
        **QAudio::ActiveState**  if you previously called start(**QIODevice**
        *). Sets **state** () to **QAudio::IdleState**  if you previously called
        **start** (). emits **stateChanged** () signal.
        """
        ...
    def setBufferSize(self, bytes: int) -> None:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#setBufferSize

        **void QAudioSource::setBufferSize(qsizetype value )**

        Sets the audio buffer size to **value** bytes.

        Note: This function can be called anytime before **start** (), calls to
        this are ignored after **start** (). It should not be assumed that the
        buffer size set is the actual buffer size used, calling **bufferSize**
        () anytime after **start** () will return the actual buffer size being
        used.

        **See also** **bufferSize** ().
        """
        ...
    def setVolume(self, volume: float) -> None:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#setVolume

        **void QAudioSource::setVolume(qreal volume )**

        Sets the input volume to **volume**.

        The volume is scaled linearly from `0.0` (silence) to `1.0` (full
        volume). Values outside this range will be clamped.

        If the device does not support adjusting the input volume then
        **volume** will be ignored and the input volume will remain at 1.0.

        The default volume is `1.0`.

        Note: Adjustments to the volume will change the volume of this audio
        stream, not the global volume.

        **See also** **volume** ().
        """
        ...
    @overload
    def start(self) -> PySide6.QtCore.QIODevice:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#start

        **void QAudioSource::start(QIODevice * device )**

        Starts transferring audio data from the system's audio input to the
        **device**. The **device** must have been opened in the **WriteOnly** ,
        **Append**  or **ReadWrite**  modes.

        If the **QAudioSource**  is able to successfully get audio data,
        **state** () returns either **QAudio::ActiveState**  or
        **QAudio::IdleState** , **error** () returns **QAudio::NoError**  and
        the **stateChanged** () signal is emitted.

        If a problem occurs during this process, **error** () returns
        **QAudio::OpenError** , **state** () returns **QAudio::StoppedState**
        and the **stateChanged** () signal is emitted.

        **See also** **QIODevice** .
        """
        ...
    @overload
    def start(self, device: PySide6.QtCore.QIODevice) -> None:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#start-1

        **QIODevice *QAudioSource::start()**

        Returns a pointer to the internal **QIODevice**  being used to transfer
        data from the system's audio input. The device will already be open and
        **read** () can read data directly from it.

        **Note:** The pointer will become invalid after the stream is stopped or
        if you start another stream.

        If the **QAudioSource**  is able to access the system's audio device,
        **state** () returns **QAudio::IdleState** , **error** () returns
        **QAudio::NoError**  and the **stateChanged** () signal is emitted.

        If a problem occurs during this process, **error** () returns
        **QAudio::OpenError** , **state** () returns **QAudio::StoppedState**
        and the **stateChanged** () signal is emitted.

        **See also** **QIODevice** .
        """
        ...
    def state(self) -> PySide6.QtMultimedia.QAudio.State:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#state

        **QAudio::State QAudioSource::state() const**

        Returns the state of audio processing.
        """
        ...
    def stop(self) -> None:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#stop

        **void QAudioSource::stop()**

        Stops the audio input, detaching from the system resource.

        Sets **error** () to **QAudio::NoError** , **state** () to
        **QAudio::StoppedState**  and emit **stateChanged** () signal.
        """
        ...
    def suspend(self) -> None:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#suspend

        **void QAudioSource::suspend()**

        Stops processing audio data, preserving buffered audio data.

        Sets **error** () to **QAudio::NoError** , **state** () to
        **QAudio::SuspendedState**  and emit **stateChanged** () signal.
        """
        ...
    def volume(self) -> float:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#volume

        **qreal QAudioSource::volume() const**

        Returns the input volume.

        If the device does not support adjusting the input volume the returned
        value will be 1.0.

        **See also** **setVolume** ().
        """
        ...
    @property
    def stateChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qaudiosource.html#stateChanged

        **[signal] void QAudioSource::stateChanged(QAudio::State state )**

        This signal is emitted when the device **state** has changed.
        """
        ...