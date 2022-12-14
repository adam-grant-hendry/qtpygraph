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

class QCamera(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qcamera.html

    **Detailed Description**

    QCamera can be used within a **QMediaCaptureSession**  for video recording
    and image taking.

    You can use **QCameraDevice**  to list available cameras and choose which
    one to use.

    const **QList** <**QCameraDevice** > cameras = **QMediaDevices**
    ::videoInputs();
        for (const **QCameraDevice**  &cameraDevice : cameras)
    {
            if (cameraDevice.description() == "mycamera")
                camera =
    new **QCamera** (cameraDevice);
        }

    On hardware that supports it, QCamera lets you adjust the focus and zoom.
    This also includes functionality such as a "Macro" mode for close up work
    (e.g. reading barcodes, or recognizing letters), or "touch to focus" -
    indicating an interesting area of the image for the hardware to attempt to
    focus on.

    camera->setFocusPointMode(**QCamera** ::FocusModeManual);
    camera->setCustomFocusPoint(**QPointF** (0.25f, 0.75f)); // A point near the
    bottom left, 25% away from the corner, near that shiny vase

    The **minimumZoomFactor** () and **maximumZoomFactor** () methods provide
    the range of supported zoom factors. The **zoomTo** () method allows
    changing the zoom factor.

    camera->setZoomFactor(3.0);

    After capturing the raw data for a camera frame, the camera hardware and
    software performs various image processing tasks to produce the final image.
    This includes compensating for ambient light color, reducing noise, as well
    as making some other adjustments to the image.

    You can control many of these processing steps through the Camera
    properties. For example, you can set the white balance (or color
    temperature) used for processing images:

    camera->setWhiteBalanceMode(**QCamera** ::WhiteBalanceFluorescent);

    For more information on image processing of camera frames, see **Camera
    Image Processing** .

    See the **camera overview**  for more information.
    """

    NoError: QCamera.Error = ...
    CameraError: QCamera.Error = ...
    ExposureAuto: QCamera.ExposureMode = ...
    ExposureManual: QCamera.ExposureMode = ...
    ExposurePortrait: QCamera.ExposureMode = ...
    ExposureNight: QCamera.ExposureMode = ...
    ExposureSports: QCamera.ExposureMode = ...
    ExposureSnow: QCamera.ExposureMode = ...
    ExposureBeach: QCamera.ExposureMode = ...
    ExposureAction: QCamera.ExposureMode = ...
    ExposureLandscape: QCamera.ExposureMode = ...
    ExposureNightPortrait: QCamera.ExposureMode = ...
    ExposureTheatre: QCamera.ExposureMode = ...
    ExposureSunset: QCamera.ExposureMode = ...
    ExposureSteadyPhoto: QCamera.ExposureMode = ...
    ExposureFireworks: QCamera.ExposureMode = ...
    ExposureParty: QCamera.ExposureMode = ...
    ExposureCandlelight: QCamera.ExposureMode = ...
    ExposureBarcode: QCamera.ExposureMode = ...
    FlashOff: QCamera.FlashMode = ...
    FlashOn: QCamera.FlashMode = ...
    FlashAuto: QCamera.FlashMode = ...
    FocusModeAuto: QCamera.FocusMode = ...
    FocusModeAutoNear: QCamera.FocusMode = ...
    FocusModeAutoFar: QCamera.FocusMode = ...
    FocusModeHyperfocal: QCamera.FocusMode = ...
    FocusModeInfinity: QCamera.FocusMode = ...
    FocusModeManual: QCamera.FocusMode = ...
    TorchOff: QCamera.TorchMode = ...
    TorchOn: QCamera.TorchMode = ...
    TorchAuto: QCamera.TorchMode = ...
    WhiteBalanceAuto: QCamera.WhiteBalanceMode = ...
    WhiteBalanceManual: QCamera.WhiteBalanceMode = ...
    WhiteBalanceSunlight: QCamera.WhiteBalanceMode = ...
    WhiteBalanceCloudy: QCamera.WhiteBalanceMode = ...
    WhiteBalanceShade: QCamera.WhiteBalanceMode = ...
    WhiteBalanceTungsten: QCamera.WhiteBalanceMode = ...
    WhiteBalanceFluorescent: QCamera.WhiteBalanceMode = ...
    WhiteBalanceFlash: QCamera.WhiteBalanceMode = ...
    WhiteBalanceSunset: QCamera.WhiteBalanceMode = ...

    class Error(IntFlag):
        NoError: QCamera.Error = ...
        CameraError: QCamera.Error = ...

    class ExposureMode(IntFlag):
        ExposureAuto: QCamera.ExposureMode = ...
        ExposureManual: QCamera.ExposureMode = ...
        ExposurePortrait: QCamera.ExposureMode = ...
        ExposureNight: QCamera.ExposureMode = ...
        ExposureSports: QCamera.ExposureMode = ...
        ExposureSnow: QCamera.ExposureMode = ...
        ExposureBeach: QCamera.ExposureMode = ...
        ExposureAction: QCamera.ExposureMode = ...
        ExposureLandscape: QCamera.ExposureMode = ...
        ExposureNightPortrait: QCamera.ExposureMode = ...
        ExposureTheatre: QCamera.ExposureMode = ...
        ExposureSunset: QCamera.ExposureMode = ...
        ExposureSteadyPhoto: QCamera.ExposureMode = ...
        ExposureFireworks: QCamera.ExposureMode = ...
        ExposureParty: QCamera.ExposureMode = ...
        ExposureCandlelight: QCamera.ExposureMode = ...
        ExposureBarcode: QCamera.ExposureMode = ...

    class Feature(IntFlag):
        ColorTemperature: QCamera.Feature = ...
        ExposureCompensation: QCamera.Feature = ...
        IsoSensitivity: QCamera.Feature = ...
        ManualExposureTime: QCamera.Feature = ...
        CustomFocusPoint: QCamera.Feature = ...
        FocusDistance: QCamera.Feature = ...

    class Features: ...

    class FlashMode(IntFlag):
        FlashOff: QCamera.FlashMode = ...
        FlashOn: QCamera.FlashMode = ...
        FlashAuto: QCamera.FlashMode = ...

    class FocusMode(IntFlag):
        FocusModeAuto: QCamera.FocusMode = ...
        FocusModeAutoNear: QCamera.FocusMode = ...
        FocusModeAutoFar: QCamera.FocusMode = ...
        FocusModeHyperfocal: QCamera.FocusMode = ...
        FocusModeInfinity: QCamera.FocusMode = ...
        FocusModeManual: QCamera.FocusMode = ...

    class TorchMode(IntFlag):
        TorchOff: QCamera.TorchMode = ...
        TorchOn: QCamera.TorchMode = ...
        TorchAuto: QCamera.TorchMode = ...

    class WhiteBalanceMode(IntFlag):
        WhiteBalanceAuto: QCamera.WhiteBalanceMode = ...
        WhiteBalanceManual: QCamera.WhiteBalanceMode = ...
        WhiteBalanceSunlight: QCamera.WhiteBalanceMode = ...
        WhiteBalanceCloudy: QCamera.WhiteBalanceMode = ...
        WhiteBalanceShade: QCamera.WhiteBalanceMode = ...
        WhiteBalanceTungsten: QCamera.WhiteBalanceMode = ...
        WhiteBalanceFluorescent: QCamera.WhiteBalanceMode = ...
        WhiteBalanceFlash: QCamera.WhiteBalanceMode = ...
        WhiteBalanceSunset: QCamera.WhiteBalanceMode = ...
    @overload
    def __init__(
        self,
        cameraDevice: PySide6.QtMultimedia.QCameraDevice,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#QCamera

        **QCamera::QCamera(QObject * parent = nullptr)**

        Construct a QCamera with a **parent**.

        Selects the default camera on the system if more than one camera is
        available.
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#QCamera-1

        **QCamera::QCamera(const QCameraDevice & cameraDevice , QObject * parent
        = nullptr)**

        Construct a QCamera from a camera description **cameraDevice** and
        **parent**.
        """
        ...
    @overload
    def __init__(
        self,
        position: PySide6.QtMultimedia.QCameraDevice.Position,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#QCamera-2

        **QCamera::QCamera(QCameraDevice::Position position , QObject * parent =
        nullptr)**

        Construct a QCamera which uses a hardware camera located a the specified
        **position**.

        For example on a mobile phone it can be used to easily choose between
        front-facing and back-facing cameras.

        If no camera is available at the specified **position** or if
        **position** is **QCameraDevice::UnspecifiedPosition** , the default
        camera is used.
        """
        ...
    def cameraDevice(self) -> PySide6.QtMultimedia.QCameraDevice:
        """
        https://doc.qt.io/qt-6/qcamera.html#cameraDevice

        **QCameraDevice QCamera::cameraDevice() const**

        Returns the **QCameraDevice**  object associated with this camera.

        **Note:** Getter function for property cameraDevice.

        **See also** **setCameraDevice** ().
        """
        ...
    def cameraFormat(self) -> PySide6.QtMultimedia.QCameraFormat:
        """
        https://doc.qt.io/qt-6/qcamera.html#cameraFormat

        **QCameraFormat QCamera::cameraFormat() const**

        Returns the camera format currently used by the camera.

        **Note:** Getter function for property cameraFormat.

        **See also** **setCameraFormat** () and **QCameraDevice::videoFormats**
        .
        """
        ...
    def captureSession(self) -> PySide6.QtMultimedia.QMediaCaptureSession:
        """
        https://doc.qt.io/qt-6/qcamera.html#captureSession

        **QMediaCaptureSession *QCamera::captureSession() const**

        Returns the capture session this camera is connected to, or a nullptr if
        the camera is not connected to a capture session.

        use **QMediaCaptureSession::setCamera** () to connect the camera to a
        session.
        """
        ...
    def colorTemperature(self) -> int:
        """
        https://doc.qt.io/qt-6/qcamera.html#colorTemperature

        **int QCamera::colorTemperature() const**

        Returns the current color temperature if the current white balance mode
        is `WhiteBalanceManual`. For other modes the return value is undefined.

        **Note:** Getter function for property colorTemperature.

        **See also** **setColorTemperature** ().
        """
        ...
    def customFocusPoint(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qcamera.html#customFocusPoint-prop

        **customFocusPoint : QPointF**

        This property represents the position of the custom focus point, in
        relative frame coordinates: **QPointF** (0,0) points to the left top
        frame point, **QPointF** (0.5,0.5) points to the frame center.

        The custom focus point property is used only in `FocusPointCustom` focus
        mode.

        You can check whether custom focus points are supported by querying
        **supportedFeatures** () with the Feature.**CustomFocusPoint**  flag.

        **Access functions:**

        QPointF **customFocusPoint** () const
        void **setCustomFocusPoint**
        (const QPointF & **point** )

        **Notifier signal:**

        void **customFocusPointChanged** ()
        """
        ...
    def error(self) -> PySide6.QtMultimedia.QCamera.Error:
        """
        https://doc.qt.io/qt-6/qcamera.html#error

        **QCamera::Error QCamera::error() const**

        Returns the error state of the camera.

        **Note:** Getter function for property error.
        """
        ...
    def errorString(self) -> str:
        """
        https://doc.qt.io/qt-6/qcamera.html#errorString

        **QString QCamera::errorString() const**

        Returns a human readable string describing a camera's error state.

        **Note:** Getter function for property errorString.
        """
        ...
    def exposureCompensation(self) -> float:
        """
        https://doc.qt.io/qt-6/qcamera.html#exposureCompensation-prop

        **exposureCompensation : float**

        Exposure compensation in EV units.

        Exposure compensation property allows to adjust the automatically
        calculated exposure.

        **Access functions:**

        float **exposureCompensation** () const
        void
        **setExposureCompensation** (float **ev** )

        **Notifier signal:**

        void ****exposureCompensationChanged** ** (float **value** )
        """
        ...
    def exposureMode(self) -> PySide6.QtMultimedia.QCamera.ExposureMode:
        """
        https://doc.qt.io/qt-6/qcamera.html#exposureMode-prop

        **exposureMode : QCamera::ExposureMode**

        This property holds the exposure mode being used.

        **Access functions:**

        QCamera::ExposureMode **exposureMode** () const
        void
        **setExposureMode** (QCamera::ExposureMode **mode** )

        **Notifier signal:**

        void **exposureModeChanged** ()

        **See also** **QCamera::isExposureModeSupported** .
        """
        ...
    def exposureTime(self) -> float:
        """
        https://doc.qt.io/qt-6/qcamera.html#exposureTime

        **float QCamera::exposureTime() const**

        Returns the current exposure time in seconds.

        **Note:** Getter function for property exposureTime.
        """
        ...
    def flashMode(self) -> PySide6.QtMultimedia.QCamera.FlashMode:
        """
        https://doc.qt.io/qt-6/qcamera.html#flashMode-prop

        **flashMode : QCamera::FlashMode**

        This property holds the flash mode being used.

        Enables a certain flash mode if the camera has a flash.

        **Access functions:**

        QCamera::FlashMode **flashMode** () const
        void **setFlashMode**
        (QCamera::FlashMode **mode** )

        **Notifier signal:**

        void **flashModeChanged** ()

        **See also** **QCamera::FlashMode** , **QCamera::isFlashModeSupported**
        , and **QCamera::isFlashReady** .
        """
        ...
    def focusDistance(self) -> float:
        """
        https://doc.qt.io/qt-6/qcamera.html#focusDistance-prop

        **focusDistance : float**

        This property return an approximate focus distance of the camera. The
        value reported is between 0 and 1, 0 being the closest possible focus
        distance, 1 being as far away as possible. Note that 1 is often, but not
        always infinity.

        Setting the focus distance will be ignored unless the focus mode is set
        to **FocusModeManual** .

        **Access functions:**

        float **focusDistance** () const
        void **setFocusDistance** (float
        **d** )

        **Notifier signal:**

        void **focusDistanceChanged** (float)
        """
        ...
    def focusMode(self) -> PySide6.QtMultimedia.QCamera.FocusMode:
        """
        https://doc.qt.io/qt-6/qcamera.html#focusMode-prop

        **focusMode : FocusMode**

        This property holds the current camera focus mode.

        Sets up different focus modes for the camera. All auto focus modes will
        focus continuously. Locking the focus is possible by setting the focus
        mode to **FocusModeManual** . This will keep the current focus and stop
        any automatic focusing.

        **Access functions:**

        QCamera::FocusMode **focusMode** () const
        void **setFocusMode**
        (QCamera::FocusMode **mode** )

        **See also** **isFocusModeSupported** .
        """
        ...
    def focusPoint(self) -> PySide6.QtCore.QPointF:
        """
        https://doc.qt.io/qt-6/qcamera.html#focusPoint

        **QPointF QCamera::focusPoint() const**

        Returns the point currently used by the auto focus system to focus onto.

        **Note:** Getter function for property focusPoint.
        """
        ...
    def isActive(self) -> bool:
        """
        https://doc.qt.io/qt-6/qcamera.html#isActive

        **bool QCamera::isActive() const**

        Returns true if the camera is currently active.

        **Note:** Getter function for property **active** .
        """
        ...
    def isAvailable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qcamera.html#isAvailable

        **bool QCamera::isAvailable() const**

        Returns true if the camera can be used.
        """
        ...
    def isExposureModeSupported(
        self, mode: PySide6.QtMultimedia.QCamera.ExposureMode
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qcamera.html#isExposureModeSupported

        **[invokable] bool
        QCamera::isExposureModeSupported(QCamera::ExposureMode mode ) const**

        Returns true if the exposure **mode** is supported.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def isFlashModeSupported(self, mode: PySide6.QtMultimedia.QCamera.FlashMode) -> bool:
        """
        https://doc.qt.io/qt-6/qcamera.html#isFlashModeSupported

        **[invokable] bool QCamera::isFlashModeSupported(QCamera::FlashMode mode
        ) const**

        Returns true if the flash **mode** is supported.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def isFlashReady(self) -> bool:
        """
        https://doc.qt.io/qt-6/qcamera.html#isFlashReady

        **[invokable] bool QCamera::isFlashReady() const**

        Returns true if flash is charged.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        **Note:** Getter function for property **flashReady** .
        """
        ...
    def isFocusModeSupported(self, mode: PySide6.QtMultimedia.QCamera.FocusMode) -> bool:
        """
        https://doc.qt.io/qt-6/qcamera.html#isFocusModeSupported

        **[invokable] bool QCamera::isFocusModeSupported(QCamera::FocusMode mode
        ) const**

        Returns true if the focus **mode** is supported by the camera.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def isTorchModeSupported(self, mode: PySide6.QtMultimedia.QCamera.TorchMode) -> bool:
        """
        https://doc.qt.io/qt-6/qcamera.html#isTorchModeSupported

        **[invokable] bool QCamera::isTorchModeSupported(QCamera::TorchMode mode
        ) const**

        Returns true if the torch **mode** is supported.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def isWhiteBalanceModeSupported(
        self, mode: PySide6.QtMultimedia.QCamera.WhiteBalanceMode
    ) -> bool:
        """
        https://doc.qt.io/qt-6/qcamera.html#isWhiteBalanceModeSupported

        **[invokable] bool
        QCamera::isWhiteBalanceModeSupported(QCamera::WhiteBalanceMode mode )
        const**

        Returns true if the white balance **mode** is supported.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def isoSensitivity(self) -> int:
        """
        https://doc.qt.io/qt-6/qcamera.html#isoSensitivity-prop

        **[read-only] isoSensitivity : const int**

        This property holds the sensor ISO sensitivity.

        Describes the ISO sensitivity currently used by the camera.

        **Access functions:**

        int **isoSensitivity** () const

        **Notifier signal:**

        void ****isoSensitivityChanged** ** (int **value** )

        **See also** **setAutoIsoSensitivity** () and
        **setManualIsoSensitivity** ().
        """
        ...
    def manualExposureTime(self) -> float:
        """
        https://doc.qt.io/qt-6/qcamera.html#manualExposureTime

        **float QCamera::manualExposureTime() const**

        Returns the manual exposure time in seconds, or -1 if the camera is
        using automatic exposure times.

        **Note:** Getter function for property manualExposureTime.

        **See also** **setManualExposureTime** ().
        """
        ...
    def manualIsoSensitivity(self) -> int:
        """
        https://doc.qt.io/qt-6/qcamera.html#manualIsoSensitivity-prop

        **manualIsoSensitivity : int**

        Describes a manually set ISO sensitivity

        Setting this property to -1 (the default), implies that the camera
        automatically adjusts the ISO sensitivity.

        **Access functions:**

        int **manualIsoSensitivity** () const
        void **setManualIsoSensitivity**
        (int **iso** )

        **Notifier signal:**

        void **manualIsoSensitivityChanged** (int)
        """
        ...
    def maximumExposureTime(self) -> float:
        """
        https://doc.qt.io/qt-6/qcamera.html#maximumExposureTime

        **float QCamera::maximumExposureTime() const**

        The maximal exposure time in seconds.
        """
        ...
    def maximumIsoSensitivity(self) -> int:
        """
        https://doc.qt.io/qt-6/qcamera.html#maximumIsoSensitivity

        **int QCamera::maximumIsoSensitivity() const**

        Returns the maximum ISO sensitivity supported by the camera.
        """
        ...
    def maximumZoomFactor(self) -> float:
        """
        https://doc.qt.io/qt-6/qcamera.html#maximumZoomFactor

        **float QCamera::maximumZoomFactor() const**

        Returns the maximum zoom factor.

        This will be `1.0` on cameras that do not support zooming.

        **Note:** Getter function for property maximumZoomFactor.
        """
        ...
    def minimumExposureTime(self) -> float:
        """
        https://doc.qt.io/qt-6/qcamera.html#minimumExposureTime

        **float QCamera::minimumExposureTime() const**

        The minimal exposure time in seconds.
        """
        ...
    def minimumIsoSensitivity(self) -> int:
        """
        https://doc.qt.io/qt-6/qcamera.html#minimumIsoSensitivity

        **int QCamera::minimumIsoSensitivity() const**

        Returns the minimum ISO sensitivity supported by the camera.
        """
        ...
    def minimumZoomFactor(self) -> float:
        """
        https://doc.qt.io/qt-6/qcamera.html#minimumZoomFactor

        **float QCamera::minimumZoomFactor() const**

        Returns the minimum zoom factor.

        This will be `1.0` on cameras that do not support zooming.

        **Note:** Getter function for property minimumZoomFactor.
        """
        ...
    def setActive(self, active: bool) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#setActive

        **[slot] void QCamera::setActive(bool active )**

        Turns the camera on if **active** is `true`, or off if it's `false`.

        **Note:** Setter function for property **active** .

        **See also** **isActive** ().
        """
        ...
    def setAutoExposureTime(self) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#setAutoExposureTime

        **[slot] void QCamera::setAutoExposureTime()**

        Use automatically calculated exposure time
        """
        ...
    def setAutoIsoSensitivity(self) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#setAutoIsoSensitivity

        **[slot] void QCamera::setAutoIsoSensitivity()**

        Turn on auto sensitivity
        """
        ...
    def setCameraDevice(self, cameraDevice: PySide6.QtMultimedia.QCameraDevice) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#setCameraDevice

        **void QCamera::setCameraDevice(const QCameraDevice & cameraDevice )**

        Connects the camera object to the physical camera device described by
        **cameraDevice**. Using a default constructed **QCameraDevice**  object
        as **cameraDevice** will connect the camera to the system default camera
        device.

        **Note:** Setter function for property **cameraDevice** .

        **See also** **cameraDevice** ().
        """
        ...
    def setCameraFormat(self, format: PySide6.QtMultimedia.QCameraFormat) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#setCameraFormat

        **void QCamera::setCameraFormat(const QCameraFormat & format )**

        Tells the camera to use the format desribed by **format**. This can be
        used to define as specific resolution and frame rate to be used for
        recording and image capture.

        **Note:** Setter function for property **cameraFormat** .

        **See also** **cameraFormat** ().
        """
        ...
    def setColorTemperature(self, colorTemperature: int) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#setColorTemperature

        **[slot] void QCamera::setColorTemperature(int colorTemperature )**

        Sets manual white balance to **colorTemperature**. This is used when
        **whiteBalanceMode** () is set to `WhiteBalanceManual`. The units are
        Kelvin.

        Setting a color temperature will only have an effect if
        **WhiteBalanceManual**  is supported. In this case, setting a
        temperature greater 0 will automatically set the white balance mode to
        **WhiteBalanceManual** . Setting the temperature to 0 will reset the
        white balance mode to **WhiteBalanceAuto** .

        **Note:** Setter function for property **colorTemperature** .

        **See also** **colorTemperature** ().
        """
        ...
    def setCustomFocusPoint(
        self,
        point: (
            PySide6.QtCore.QPointF
            | PySide6.QtCore.QPoint
            | PySide6.QtGui.QPainterPath.Element
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#customFocusPoint-prop

        **customFocusPoint : QPointF**

        This property represents the position of the custom focus point, in
        relative frame coordinates: **QPointF** (0,0) points to the left top
        frame point, **QPointF** (0.5,0.5) points to the frame center.

        The custom focus point property is used only in `FocusPointCustom` focus
        mode.

        You can check whether custom focus points are supported by querying
        **supportedFeatures** () with the Feature.**CustomFocusPoint**  flag.

        **Access functions:**

        QPointF **customFocusPoint** () const
        void **setCustomFocusPoint**
        (const QPointF & **point** )

        **Notifier signal:**

        void **customFocusPointChanged** ()
        """
        ...
    def setExposureCompensation(self, ev: float) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#exposureCompensation-prop

        **exposureCompensation : float**

        Exposure compensation in EV units.

        Exposure compensation property allows to adjust the automatically
        calculated exposure.

        **Access functions:**

        float **exposureCompensation** () const
        void
        **setExposureCompensation** (float **ev** )

        **Notifier signal:**

        void ****exposureCompensationChanged** ** (float **value** )
        """
        ...
    def setExposureMode(self, mode: PySide6.QtMultimedia.QCamera.ExposureMode) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#exposureMode-prop

        **exposureMode : QCamera::ExposureMode**

        This property holds the exposure mode being used.

        **Access functions:**

        QCamera::ExposureMode **exposureMode** () const
        void
        **setExposureMode** (QCamera::ExposureMode **mode** )

        **Notifier signal:**

        void **exposureModeChanged** ()

        **See also** **QCamera::isExposureModeSupported** .
        """
        ...
    def setFlashMode(self, mode: PySide6.QtMultimedia.QCamera.FlashMode) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#flashMode-prop

        **flashMode : QCamera::FlashMode**

        This property holds the flash mode being used.

        Enables a certain flash mode if the camera has a flash.

        **Access functions:**

        QCamera::FlashMode **flashMode** () const
        void **setFlashMode**
        (QCamera::FlashMode **mode** )

        **Notifier signal:**

        void **flashModeChanged** ()

        **See also** **QCamera::FlashMode** , **QCamera::isFlashModeSupported**
        , and **QCamera::isFlashReady** .
        """
        ...
    def setFocusDistance(self, d: float) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#focusDistance-prop

        **focusDistance : float**

        This property return an approximate focus distance of the camera. The
        value reported is between 0 and 1, 0 being the closest possible focus
        distance, 1 being as far away as possible. Note that 1 is often, but not
        always infinity.

        Setting the focus distance will be ignored unless the focus mode is set
        to **FocusModeManual** .

        **Access functions:**

        float **focusDistance** () const
        void **setFocusDistance** (float
        **d** )

        **Notifier signal:**

        void **focusDistanceChanged** (float)
        """
        ...
    def setFocusMode(self, mode: PySide6.QtMultimedia.QCamera.FocusMode) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#focusMode-prop

        **focusMode : FocusMode**

        This property holds the current camera focus mode.

        Sets up different focus modes for the camera. All auto focus modes will
        focus continuously. Locking the focus is possible by setting the focus
        mode to **FocusModeManual** . This will keep the current focus and stop
        any automatic focusing.

        **Access functions:**

        QCamera::FocusMode **focusMode** () const
        void **setFocusMode**
        (QCamera::FocusMode **mode** )

        **See also** **isFocusModeSupported** .
        """
        ...
    def setManualExposureTime(self, seconds: float) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#setManualExposureTime

        **[slot] void QCamera::setManualExposureTime(float seconds )**

        Set the manual exposure time to **seconds**

        **Note:** Setter function for property **manualExposureTime** .

        **See also** **manualExposureTime** ().
        """
        ...
    def setManualIsoSensitivity(self, iso: int) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#manualIsoSensitivity-prop

        **manualIsoSensitivity : int**

        Describes a manually set ISO sensitivity

        Setting this property to -1 (the default), implies that the camera
        automatically adjusts the ISO sensitivity.

        **Access functions:**

        int **manualIsoSensitivity** () const
        void **setManualIsoSensitivity**
        (int **iso** )

        **Notifier signal:**

        void **manualIsoSensitivityChanged** (int)
        """
        ...
    def setTorchMode(self, mode: PySide6.QtMultimedia.QCamera.TorchMode) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#torchMode-prop

        **torchMode : QCamera::TorchMode**

        This property holds the torch mode being used.

        A torch is a continuous source of light. It can be used during video
        recording in low light conditions. Enabling torch mode will usually
        override any currently set flash mode.

        **Access functions:**

        QCamera::TorchMode **torchMode** () const
        void **setTorchMode**
        (QCamera::TorchMode **mode** )

        **Notifier signal:**

        void **torchModeChanged** ()

        **See also** **QCamera::TorchMode** , **QCamera::isTorchModeSupported**
        , and **QCamera::flashMode** .
        """
        ...
    def setWhiteBalanceMode(
        self, mode: PySide6.QtMultimedia.QCamera.WhiteBalanceMode
    ) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#setWhiteBalanceMode

        **[slot] void QCamera::setWhiteBalanceMode(QCamera::WhiteBalanceMode
        mode )**

        Sets the white balance to **mode**.

        **Note:** Setter function for property **whiteBalanceMode** .

        **See also** **whiteBalanceMode** ().
        """
        ...
    def setZoomFactor(self, factor: float) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#setZoomFactor

        **void QCamera::setZoomFactor(float factor )**

        Zooms to a zoom factor **factor** at a rate of 1 factor per second.

        **Note:** Setter function for property **zoomFactor** .

        **See also** **zoomFactor** ().
        """
        ...
    def start(self) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#start

        **[slot] void QCamera::start()**

        Starts the camera.

        Same as **setActive** (true).

        If the camera can't be started for some reason, the **errorOccurred** ()
        signal is emitted.
        """
        ...
    def stop(self) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#stop

        **[slot] void QCamera::stop()**

        Stops the camera. Same as **setActive** (false).
        """
        ...
    def supportedFeatures(self) -> PySide6.QtMultimedia.QCamera.Features:
        """
        https://doc.qt.io/qt-6/qcamera.html#supportedFeatures

        **QCamera::Features QCamera::supportedFeatures() const**

        Returns the features supported by this camera.

        **Note:** Getter function for property supportedFeatures.

        **See also** **QCamera::Feature** .
        """
        ...
    def torchMode(self) -> PySide6.QtMultimedia.QCamera.TorchMode:
        """
        https://doc.qt.io/qt-6/qcamera.html#torchMode-prop

        **torchMode : QCamera::TorchMode**

        This property holds the torch mode being used.

        A torch is a continuous source of light. It can be used during video
        recording in low light conditions. Enabling torch mode will usually
        override any currently set flash mode.

        **Access functions:**

        QCamera::TorchMode **torchMode** () const
        void **setTorchMode**
        (QCamera::TorchMode **mode** )

        **Notifier signal:**

        void **torchModeChanged** ()

        **See also** **QCamera::TorchMode** , **QCamera::isTorchModeSupported**
        , and **QCamera::flashMode** .
        """
        ...
    def whiteBalanceMode(self) -> PySide6.QtMultimedia.QCamera.WhiteBalanceMode:
        """
        https://doc.qt.io/qt-6/qcamera.html#whiteBalanceMode

        **QCamera::WhiteBalanceMode QCamera::whiteBalanceMode() const**

        Returns the white balance mode being used.

        **Note:** Getter function for property whiteBalanceMode.

        **See also** **setWhiteBalanceMode** ().
        """
        ...
    def zoomFactor(self) -> float:
        """
        https://doc.qt.io/qt-6/qcamera.html#zoomFactor-prop

        **zoomFactor : float**

        This property holds the current zoom factor.

        Gets or sets the current zoom factor. Values will be clamped between
        **minimumZoomFactor**  and **maximumZoomFactor** .

        **Access functions:**

        float **zoomFactor** () const
        void ****setZoomFactor** ** (float
        **factor** )

        **Notifier signal:**

        void **zoomFactorChanged** (float)

        **Member Function Documentation**
        """
        ...
    def zoomTo(self, zoom: float, rate: float) -> None:
        """
        https://doc.qt.io/qt-6/qcamera.html#zoomTo

        **[slot] void QCamera::zoomTo(float factor , float rate )**

        Zooms to a zoom factor **factor** using **rate**.

        The **rate** is specified in powers of two per second. At a rate of 1 it
        would take 2 seconds to go from a zoom factor of 1 to 4.

        **Note:** Using a specific rate is not supported on all cameras. If not
        supported, zooming will happen as fast as possible.
        """
        ...
    @property
    def activeChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def customFocusPointChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def errorOccurred(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qcamera.html#errorOccurred

        **[signal] void QCamera::errorOccurred(QCamera::Error error , const
        QString & errorString )**

        This signal is emitted when error state changes to **error**. A
        description of the error is provided as **errorString**.
        """
        ...
    @property
    def exposureCompensationChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qcamera.html#exposureCompensationChanged

        **[signal] void QCamera::exposureCompensationChanged(float value )**

        Signal emitted when the exposure compensation changes to **value**.

        **Note:** Notifier signal for property **exposureCompensation** .
        """
        ...
    @property
    def exposureModeChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def exposureTimeChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qcamera.html#exposureTimeChanged

        **[signal] void QCamera::exposureTimeChanged(float speed )**

        Signals that a camera's exposure **speed** has changed.

        **Note:** Notifier signal for property **exposureTime** .
        """
        ...
    @property
    def flashModeChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def flashReady(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qcamera.html#flashReady

        **[signal] void QCamera::flashReady(bool ready )**

        Signal the flash **ready** status has changed.

        **Note:** Notifier signal for property flashReady.
        """
        ...
    @property
    def focusDistanceChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def isoSensitivityChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qcamera.html#isoSensitivityChanged

        **[signal] void QCamera::isoSensitivityChanged(int value )**

        Signal emitted when sensitivity changes to **value**.

        **Note:** Notifier signal for property **isoSensitivity** .
        """
        ...
    @property
    def manualIsoSensitivityChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def torchModeChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def zoomFactorChanged(self) -> PySide6.QtCore.SignalInstance: ...
