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

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtMultimedia

class QMediaDevices(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qmediadevices.html

    **Detailed Description**

    The QMediaDevices class provides information about the available multimedia
    devices and the system defaults. It monitors the following three groups:

    * Audio input devices (Microphones)
      * Audio output devices (Speakers,
    Headsets)
      * Video input devices (Cameras)

    QMediaDevices provides a separate list for each device group. If it detects
    that a new device has been connected to the system or an attached device has
    been disconnected from the system, it will update the corresponding device
    list and emit a signal notifying about the change.

    QMediaDevices monitors the system defaults for each device group. It will
    notify about any changes done through the system settings. For example, if
    the user selects a new default audio output in the system settings,
    QMediaDevices will update the default audio output accordingly and emit a
    signal. If the system does not provide a default for a camera or an audio
    input, QMediaDevices will select the first device from the list as the
    default device.

    While using the default input and output devices is often sufficient for
    playing back or recording multimedia, there is often a need to explicitly
    select the device to be used.

    QMediaDevices is a singleton object and all getters are thread-safe.
    """

    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None: ...
    @staticmethod
    def audioInputs() -> list[PySide6.QtMultimedia.QAudioDevice]:
        """
        https://doc.qt.io/qt-6/qmediadevices.html#audioInputs

        **[static] QList<QAudioDevice> QMediaDevices::audioInputs()**

        Returns a list of available audio input devices on the system.

        Those devices are usually microphones. Devices can be either built-in,
        or connected through for example USB or Bluetooth.

        **Note:** Getter function for property audioInputs.
        """
        ...
    @staticmethod
    def audioOutputs() -> list[PySide6.QtMultimedia.QAudioDevice]:
        """
        https://doc.qt.io/qt-6/qmediadevices.html#audioOutputs

        **[static] QList<QAudioDevice> QMediaDevices::audioOutputs()**

        Returns a list of available audio output devices on the system.

        Those devices are usually loudspeakers or head sets. Devices can be
        either built-in, or connected through for example USB or Bluetooth.

        **Note:** Getter function for property audioOutputs.
        """
        ...
    @staticmethod
    def defaultAudioInput() -> PySide6.QtMultimedia.QAudioDevice:
        """
        https://doc.qt.io/qt-6/qmediadevices.html#defaultAudioInput

        **[static] QAudioDevice QMediaDevices::defaultAudioInput()**

        Returns the default audio input device.

        The default device can change during the runtime of the application. The
        **audioInputsChanged** () signal is emitted in this case.

        **Note:** Getter function for property defaultAudioInput.
        """
        ...
    @staticmethod
    def defaultAudioOutput() -> PySide6.QtMultimedia.QAudioDevice:
        """
        https://doc.qt.io/qt-6/qmediadevices.html#defaultAudioOutput

        **[static] QAudioDevice QMediaDevices::defaultAudioOutput()**

        Returns the default audio output device.

        The default device can change during the runtime of the application. The
        **audioOutputsChanged** () signal is emitted in this case.

        **Note:** Getter function for property defaultAudioOutput.
        """
        ...
    @staticmethod
    def defaultVideoInput() -> PySide6.QtMultimedia.QCameraDevice:
        """
        https://doc.qt.io/qt-6/qmediadevices.html#defaultVideoInput

        **[static] QCameraDevice QMediaDevices::defaultVideoInput()**

        Returns the default camera on the system.

        /note The returned object should be checked using isNull() before being
        used, in case there is no default camera or no cameras at all.

        The default device can change during the runtime of the application. The
        **videoInputsChanged** () signal is emitted in that case.

        **Note:** Getter function for property defaultVideoInput.

        **See also** **videoInputs** ().
        """
        ...
    @staticmethod
    def videoInputs() -> list[PySide6.QtMultimedia.QCameraDevice]:
        """
        https://doc.qt.io/qt-6/qmediadevices.html#videoInputs

        **[static] QList<QCameraDevice> QMediaDevices::videoInputs()**

        Returns a list of available cameras on the system.

        **Note:** Getter function for property videoInputs.
        """
        ...
