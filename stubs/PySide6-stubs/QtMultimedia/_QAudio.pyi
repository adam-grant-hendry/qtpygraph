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

class QAudio:
    """
    https://doc.qt.io/qt-6/qaudio.html

    **Detailed Description**
    """

    NoError: QAudio.Error = ...
    OpenError: QAudio.Error = ...
    IOError: QAudio.Error = ...
    UnderrunError: QAudio.Error = ...
    FatalError: QAudio.Error = ...
    ActiveState: QAudio.State = ...
    SuspendedState: QAudio.State = ...
    StoppedState: QAudio.State = ...
    IdleState: QAudio.State = ...
    LinearVolumeScale: QAudio.VolumeScale = ...
    CubicVolumeScale: QAudio.VolumeScale = ...
    LogarithmicVolumeScale: QAudio.VolumeScale = ...
    DecibelVolumeScale: QAudio.VolumeScale = ...

    class Error(IntFlag):
        NoError: QAudio.Error = ...
        OpenError: QAudio.Error = ...
        IOError: QAudio.Error = ...
        UnderrunError: QAudio.Error = ...
        FatalError: QAudio.Error = ...

    class State(IntFlag):
        ActiveState: QAudio.State = ...
        SuspendedState: QAudio.State = ...
        StoppedState: QAudio.State = ...
        IdleState: QAudio.State = ...

    class VolumeScale(IntFlag):
        LinearVolumeScale: QAudio.VolumeScale = ...
        CubicVolumeScale: QAudio.VolumeScale = ...
        LogarithmicVolumeScale: QAudio.VolumeScale = ...
        DecibelVolumeScale: QAudio.VolumeScale = ...
    @staticmethod
    def convertVolume(
        volume: float,
        from_: PySide6.QtMultimedia.QAudio.VolumeScale,
        to: PySide6.QtMultimedia.QAudio.VolumeScale,
    ) -> float:
        """
        https://doc.qt.io/qt-6/qaudio.html#convertVolume

        **float QAudio::convertVolume(float volume , QAudio::VolumeScale from ,
        QAudio::VolumeScale to )**

        Converts an audio **volume** **from** a volume scale **to** another, and
        returns the result.

        Depending on the context, different scales are used to represent audio
        volume. All Qt Multimedia classes that have an audio volume use a linear
        scale, the reason is that the loudness of a speaker is controlled by
        modulating its voltage on a linear scale. The human ear on the other
        hand, perceives loudness in a logarithmic way. Using a logarithmic scale
        for volume controls is therefore appropriate in most applications. The
        decibel scale is logarithmic by nature and is commonly used to define
        sound levels, it is usually used for UI volume controls in professional
        audio applications. The cubic scale is a computationally cheap
        approximation of a logarithmic scale, it provides more control over
        lower volume levels.

        The following example shows how to convert the volume value from a
        slider control before passing it to a **QMediaPlayer** . As a result,
        the perceived increase in volume is the same when increasing the volume
        slider from 20 to 30 as it is from 50 to 60:

        void applyVolume(int volumeSliderValue)
            {
                //
        volumeSliderValue is in the range [0..100]

                **qreal**
        linearVolume = QAudio::convertVolume(volumeSliderValue / **qreal**
        (100.0),
        QAudio::LogarithmicVolumeScale,
        QAudio::LinearVolumeScale);

                player.setVolume(**qRound**
        (linearVolume * 100));
            }

        **See also** **VolumeScale** , **QAudioSink::setVolume** (),
        **QAudioSource::setVolume** (), and **QSoundEffect::setVolume** ().
        """
        ...