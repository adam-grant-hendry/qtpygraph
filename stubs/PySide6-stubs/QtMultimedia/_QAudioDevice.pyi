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
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtMultimedia

class QAudioDevice:
    """
    https://doc.qt.io/qt-6/qaudiodevice.html

    **Detailed Description**

    QAudioDevice describes an audio device available in the system, either for
    input or for playback.

    A QAudioDevice is used by Qt to construct classes that communicate with the
    device -- such as **QAudioSource** , and **QAudioSink** . It is also used to
    determine the input or output device to use in a capture session or during
    media playback.

    You can also query each device for the formats it supports. A format in this
    context is a set consisting of a channel count, sample rate, and sample
    type. A format is represented by the **QAudioFormat**  class.

    The values supported by the device for each of these parameters can be
    fetched with **minimumChannelCount** (), **maximumChannelCount** (),
    **minimumSampleRate** (), **maximumSampleRate** () and
    **supportedSampleFormats** (). The combinations supported are dependent on
    the audio device capabilities. If you need a specific format, you can check
    if the device supports it with **isFormatSupported** (), or fetch a
    supported format that is as close as possible to the format with
    nearestFormat(). For instance:

    **QAudioFormat**  format;
        format.setSampleRate(44100);
        // ... other
    format parameters
        format.setSampleFormat(**QAudioFormat** ::Int16);

    The set of available devices can be retrieved from the **QMediaDevices**
    class.

    For instance:

    const auto deviceInfos = **QMediaDevices**
    ::availableDevices(**QAudioDevice** ::Output);
        for (const
    **QAudioDevice**  &deviceInfo : deviceInfos)
            **qDebug** () <<
    "Device: " << deviceInfo.description();

    In this code sample, we loop through all devices that are able to output
    sound, i.e., play an audio stream in a supported format. For each device we
    find, we simply print the deviceName().

    **See also** **QAudioSink**  and **QAudioSource** .
    """

    Null: QAudioDevice.Mode = ...
    Input: QAudioDevice.Mode = ...
    Output: QAudioDevice.Mode = ...

    class Mode(IntFlag):
        Null: QAudioDevice.Mode = ...
        Input: QAudioDevice.Mode = ...
        Output: QAudioDevice.Mode = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#QAudioDevice

        **QAudioDevice::QAudioDevice()**

        Constructs a null QAudioDevice object.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtMultimedia.QAudioDevice) -> None:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#QAudioDevice-1

        **QAudioDevice::QAudioDevice(const QAudioDevice & other )**

        Constructs a copy of **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def description(self) -> str:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#description

        **QString QAudioDevice::description() const**

        Returns a human readable name of the audio device.

        Use this string to present the device to the user.

        **Note:** Getter function for property description.
        """
        ...
    def id(self) -> PySide6.QtCore.QByteArray:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#id

        **QByteArray QAudioDevice::id() const**

        Returns an identifier for the audio device.

        Device names vary depending on the platform/audio plugin being used.

        They are a unique identifier for the audio device.

        **Note:** Getter function for property id.
        """
        ...
    def isDefault(self) -> bool:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#isDefault

        **bool QAudioDevice::isDefault() const**

        Returns true if this is the default audio device.

        **Note:** Getter function for property isDefault.
        """
        ...
    def isFormatSupported(self, format: PySide6.QtMultimedia.QAudioFormat) -> bool:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#isFormatSupported

        **bool QAudioDevice::isFormatSupported(const QAudioFormat & settings )
        const**

        Returns true if the supplied **settings** are supported by the audio
        device described by this **QAudioDevice** .
        """
        ...
    def isNull(self) -> bool:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#isNull

        **bool QAudioDevice::isNull() const**

        Returns whether this **QAudioDevice**  object holds a valid device
        definition.
        """
        ...
    def maximumChannelCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#maximumChannelCount

        **int QAudioDevice::maximumChannelCount() const**

        Returns the maximum number of supported channel counts.

        This is typically 1 for mono sound, or 2 for stereo sound.
        """
        ...
    def maximumSampleRate(self) -> int:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#maximumSampleRate

        **int QAudioDevice::maximumSampleRate() const**

        Returns the maximum supported sample rate (in Hertz).
        """
        ...
    def minimumChannelCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#minimumChannelCount

        **int QAudioDevice::minimumChannelCount() const**

        Returns the minimum number of supported channel counts.

        This is typically 1 for mono sound, or 2 for stereo sound.
        """
        ...
    def minimumSampleRate(self) -> int:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#minimumSampleRate

        **int QAudioDevice::minimumSampleRate() const**

        Returns the minimum supported sample rate (in Hertz).
        """
        ...
    def mode(self) -> PySide6.QtMultimedia.QAudioDevice.Mode:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#mode

        **QAudioDevice::Mode QAudioDevice::mode() const**

        returns whether this device is an input or output device.

        **Note:** Getter function for property mode.
        """
        ...
    def preferredFormat(self) -> PySide6.QtMultimedia.QAudioFormat:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#preferredFormat

        **QAudioFormat QAudioDevice::preferredFormat() const**

        Returns the default audio format settings for this device.

        These settings are provided by the platform/audio plugin being used.

        They are also dependent on the **QAudio** ::Mode being used.

        A typical audio system would provide something like:

        * Input settings: 48000Hz mono 16 bit.
          * Output settings: 48000Hz
        stereo 16 bit.
        """
        ...
    def supportedSampleFormats(
        self,
    ) -> list[PySide6.QtMultimedia.QAudioFormat.SampleFormat]:
        """
        https://doc.qt.io/qt-6/qaudiodevice.html#supportedSampleFormats

        **QList<QAudioFormat::SampleFormat>
        QAudioDevice::supportedSampleFormats() const**

        Returns a list of supported sample types.
        """
        ...
    def swap(self, other: PySide6.QtMultimedia.QAudioDevice) -> None: ...
