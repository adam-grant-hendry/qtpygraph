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
PySide6.QtBluetooth, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag
from typing import overload

import PySide6.QtBluetooth
import PySide6.QtCore

class QBluetoothUuid(PySide6.QtCore.QUuid):
    """
    https://doc.qt.io/qt-6/qbluetoothuuid.html

    **Detailed Description**
    """

    class CharacteristicType(IntFlag):
        DeviceName: QBluetoothUuid.CharacteristicType = ...
        Appearance: QBluetoothUuid.CharacteristicType = ...
        PeripheralPrivacyFlag: QBluetoothUuid.CharacteristicType = ...
        ReconnectionAddress: QBluetoothUuid.CharacteristicType = ...
        PeripheralPreferredConnectionParameters: QBluetoothUuid.CharacteristicType = ...
        ServiceChanged: QBluetoothUuid.CharacteristicType = ...
        AlertLevel: QBluetoothUuid.CharacteristicType = ...
        TxPowerLevel: QBluetoothUuid.CharacteristicType = ...
        DateTime: QBluetoothUuid.CharacteristicType = ...
        DayOfWeek: QBluetoothUuid.CharacteristicType = ...
        DayDateTime: QBluetoothUuid.CharacteristicType = ...
        ExactTime256: QBluetoothUuid.CharacteristicType = ...
        DSTOffset: QBluetoothUuid.CharacteristicType = ...
        TimeZone: QBluetoothUuid.CharacteristicType = ...
        LocalTimeInformation: QBluetoothUuid.CharacteristicType = ...
        TimeWithDST: QBluetoothUuid.CharacteristicType = ...
        TimeAccuracy: QBluetoothUuid.CharacteristicType = ...
        TimeSource: QBluetoothUuid.CharacteristicType = ...
        ReferenceTimeInformation: QBluetoothUuid.CharacteristicType = ...
        TimeUpdateControlPoint: QBluetoothUuid.CharacteristicType = ...
        TimeUpdateState: QBluetoothUuid.CharacteristicType = ...
        GlucoseMeasurement: QBluetoothUuid.CharacteristicType = ...
        BatteryLevel: QBluetoothUuid.CharacteristicType = ...
        TemperatureMeasurement: QBluetoothUuid.CharacteristicType = ...
        TemperatureType: QBluetoothUuid.CharacteristicType = ...
        IntermediateTemperature: QBluetoothUuid.CharacteristicType = ...
        MeasurementInterval: QBluetoothUuid.CharacteristicType = ...
        BootKeyboardInputReport: QBluetoothUuid.CharacteristicType = ...
        SystemID: QBluetoothUuid.CharacteristicType = ...
        ModelNumberString: QBluetoothUuid.CharacteristicType = ...
        SerialNumberString: QBluetoothUuid.CharacteristicType = ...
        FirmwareRevisionString: QBluetoothUuid.CharacteristicType = ...
        HardwareRevisionString: QBluetoothUuid.CharacteristicType = ...
        SoftwareRevisionString: QBluetoothUuid.CharacteristicType = ...
        ManufacturerNameString: QBluetoothUuid.CharacteristicType = ...
        IEEE1107320601RegulatoryCertificationDataList: QBluetoothUuid.CharacteristicType = (
            ...
        )
        CurrentTime: QBluetoothUuid.CharacteristicType = ...
        MagneticDeclination: QBluetoothUuid.CharacteristicType = ...
        ScanRefresh: QBluetoothUuid.CharacteristicType = ...
        BootKeyboardOutputReport: QBluetoothUuid.CharacteristicType = ...
        BootMouseInputReport: QBluetoothUuid.CharacteristicType = ...
        GlucoseMeasurementContext: QBluetoothUuid.CharacteristicType = ...
        BloodPressureMeasurement: QBluetoothUuid.CharacteristicType = ...
        IntermediateCuffPressure: QBluetoothUuid.CharacteristicType = ...
        HeartRateMeasurement: QBluetoothUuid.CharacteristicType = ...
        BodySensorLocation: QBluetoothUuid.CharacteristicType = ...
        HeartRateControlPoint: QBluetoothUuid.CharacteristicType = ...
        AlertStatus: QBluetoothUuid.CharacteristicType = ...
        RingerControlPoint: QBluetoothUuid.CharacteristicType = ...
        RingerSetting: QBluetoothUuid.CharacteristicType = ...
        AlertCategoryIDBitMask: QBluetoothUuid.CharacteristicType = ...
        AlertCategoryID: QBluetoothUuid.CharacteristicType = ...
        AlertNotificationControlPoint: QBluetoothUuid.CharacteristicType = ...
        UnreadAlertStatus: QBluetoothUuid.CharacteristicType = ...
        NewAlert: QBluetoothUuid.CharacteristicType = ...
        SupportedNewAlertCategory: QBluetoothUuid.CharacteristicType = ...
        SupportedUnreadAlertCategory: QBluetoothUuid.CharacteristicType = ...
        BloodPressureFeature: QBluetoothUuid.CharacteristicType = ...
        HIDInformation: QBluetoothUuid.CharacteristicType = ...
        ReportMap: QBluetoothUuid.CharacteristicType = ...
        HIDControlPoint: QBluetoothUuid.CharacteristicType = ...
        Report: QBluetoothUuid.CharacteristicType = ...
        ProtocolMode: QBluetoothUuid.CharacteristicType = ...
        ScanIntervalWindow: QBluetoothUuid.CharacteristicType = ...
        PnPID: QBluetoothUuid.CharacteristicType = ...
        GlucoseFeature: QBluetoothUuid.CharacteristicType = ...
        RecordAccessControlPoint: QBluetoothUuid.CharacteristicType = ...
        RSCMeasurement: QBluetoothUuid.CharacteristicType = ...
        RSCFeature: QBluetoothUuid.CharacteristicType = ...
        SCControlPoint: QBluetoothUuid.CharacteristicType = ...
        CSCMeasurement: QBluetoothUuid.CharacteristicType = ...
        CSCFeature: QBluetoothUuid.CharacteristicType = ...
        SensorLocation: QBluetoothUuid.CharacteristicType = ...
        CyclingPowerMeasurement: QBluetoothUuid.CharacteristicType = ...
        CyclingPowerVector: QBluetoothUuid.CharacteristicType = ...
        CyclingPowerFeature: QBluetoothUuid.CharacteristicType = ...
        CyclingPowerControlPoint: QBluetoothUuid.CharacteristicType = ...
        LocationAndSpeed: QBluetoothUuid.CharacteristicType = ...
        Navigation: QBluetoothUuid.CharacteristicType = ...
        PositionQuality: QBluetoothUuid.CharacteristicType = ...
        LNFeature: QBluetoothUuid.CharacteristicType = ...
        LNControlPoint: QBluetoothUuid.CharacteristicType = ...
        Elevation: QBluetoothUuid.CharacteristicType = ...
        Pressure: QBluetoothUuid.CharacteristicType = ...
        Temperature: QBluetoothUuid.CharacteristicType = ...
        Humidity: QBluetoothUuid.CharacteristicType = ...
        TrueWindSpeed: QBluetoothUuid.CharacteristicType = ...
        TrueWindDirection: QBluetoothUuid.CharacteristicType = ...
        ApparentWindSpeed: QBluetoothUuid.CharacteristicType = ...
        ApparentWindDirection: QBluetoothUuid.CharacteristicType = ...
        GustFactor: QBluetoothUuid.CharacteristicType = ...
        PollenConcentration: QBluetoothUuid.CharacteristicType = ...
        UVIndex: QBluetoothUuid.CharacteristicType = ...
        Irradiance: QBluetoothUuid.CharacteristicType = ...
        Rainfall: QBluetoothUuid.CharacteristicType = ...
        WindChill: QBluetoothUuid.CharacteristicType = ...
        HeatIndex: QBluetoothUuid.CharacteristicType = ...
        DewPoint: QBluetoothUuid.CharacteristicType = ...
        DescriptorValueChanged: QBluetoothUuid.CharacteristicType = ...
        AerobicHeartRateLowerLimit: QBluetoothUuid.CharacteristicType = ...
        AerobicThreshold: QBluetoothUuid.CharacteristicType = ...
        Age: QBluetoothUuid.CharacteristicType = ...
        AnaerobicHeartRateLowerLimit: QBluetoothUuid.CharacteristicType = ...
        AnaerobicHeartRateUpperLimit: QBluetoothUuid.CharacteristicType = ...
        AnaerobicThreshold: QBluetoothUuid.CharacteristicType = ...
        AerobicHeartRateUpperLimit: QBluetoothUuid.CharacteristicType = ...
        DateOfBirth: QBluetoothUuid.CharacteristicType = ...
        DateOfThresholdAssessment: QBluetoothUuid.CharacteristicType = ...
        EmailAddress: QBluetoothUuid.CharacteristicType = ...
        FatBurnHeartRateLowerLimit: QBluetoothUuid.CharacteristicType = ...
        FatBurnHeartRateUpperLimit: QBluetoothUuid.CharacteristicType = ...
        FirstName: QBluetoothUuid.CharacteristicType = ...
        FiveZoneHeartRateLimits: QBluetoothUuid.CharacteristicType = ...
        Gender: QBluetoothUuid.CharacteristicType = ...
        HeartRateMax: QBluetoothUuid.CharacteristicType = ...
        Height: QBluetoothUuid.CharacteristicType = ...
        HipCircumference: QBluetoothUuid.CharacteristicType = ...
        LastName: QBluetoothUuid.CharacteristicType = ...
        MaximumRecommendedHeartRate: QBluetoothUuid.CharacteristicType = ...
        RestingHeartRate: QBluetoothUuid.CharacteristicType = ...
        SportTypeForAerobicAnaerobicThresholds: QBluetoothUuid.CharacteristicType = ...
        ThreeZoneHeartRateLimits: QBluetoothUuid.CharacteristicType = ...
        TwoZoneHeartRateLimits: QBluetoothUuid.CharacteristicType = ...
        VO2Max: QBluetoothUuid.CharacteristicType = ...
        WaistCircumference: QBluetoothUuid.CharacteristicType = ...
        Weight: QBluetoothUuid.CharacteristicType = ...
        DatabaseChangeIncrement: QBluetoothUuid.CharacteristicType = ...
        UserIndex: QBluetoothUuid.CharacteristicType = ...
        BodyCompositionFeature: QBluetoothUuid.CharacteristicType = ...
        BodyCompositionMeasurement: QBluetoothUuid.CharacteristicType = ...
        WeightMeasurement: QBluetoothUuid.CharacteristicType = ...
        WeightScaleFeature: QBluetoothUuid.CharacteristicType = ...
        UserControlPoint: QBluetoothUuid.CharacteristicType = ...
        MagneticFluxDensity2D: QBluetoothUuid.CharacteristicType = ...
        MagneticFluxDensity3D: QBluetoothUuid.CharacteristicType = ...
        Language: QBluetoothUuid.CharacteristicType = ...
        BarometricPressureTrend: QBluetoothUuid.CharacteristicType = ...

    class DescriptorType(IntFlag):
        UnknownDescriptorType: QBluetoothUuid.DescriptorType = ...
        CharacteristicExtendedProperties: QBluetoothUuid.DescriptorType = ...
        CharacteristicUserDescription: QBluetoothUuid.DescriptorType = ...
        ClientCharacteristicConfiguration: QBluetoothUuid.DescriptorType = ...
        ServerCharacteristicConfiguration: QBluetoothUuid.DescriptorType = ...
        CharacteristicPresentationFormat: QBluetoothUuid.DescriptorType = ...
        CharacteristicAggregateFormat: QBluetoothUuid.DescriptorType = ...
        ValidRange: QBluetoothUuid.DescriptorType = ...
        ExternalReportReference: QBluetoothUuid.DescriptorType = ...
        ReportReference: QBluetoothUuid.DescriptorType = ...
        EnvironmentalSensingConfiguration: QBluetoothUuid.DescriptorType = ...
        EnvironmentalSensingMeasurement: QBluetoothUuid.DescriptorType = ...
        EnvironmentalSensingTriggerSetting: QBluetoothUuid.DescriptorType = ...

    class ProtocolUuid(IntFlag):
        Sdp: QBluetoothUuid.ProtocolUuid = ...
        Udp: QBluetoothUuid.ProtocolUuid = ...
        Rfcomm: QBluetoothUuid.ProtocolUuid = ...
        Tcp: QBluetoothUuid.ProtocolUuid = ...
        TcsBin: QBluetoothUuid.ProtocolUuid = ...
        TcsAt: QBluetoothUuid.ProtocolUuid = ...
        Att: QBluetoothUuid.ProtocolUuid = ...
        Obex: QBluetoothUuid.ProtocolUuid = ...
        Ip: QBluetoothUuid.ProtocolUuid = ...
        Ftp: QBluetoothUuid.ProtocolUuid = ...
        Http: QBluetoothUuid.ProtocolUuid = ...
        Wsp: QBluetoothUuid.ProtocolUuid = ...
        Bnep: QBluetoothUuid.ProtocolUuid = ...
        Upnp: QBluetoothUuid.ProtocolUuid = ...
        Hidp: QBluetoothUuid.ProtocolUuid = ...
        HardcopyControlChannel: QBluetoothUuid.ProtocolUuid = ...
        HardcopyDataChannel: QBluetoothUuid.ProtocolUuid = ...
        HardcopyNotification: QBluetoothUuid.ProtocolUuid = ...
        Avctp: QBluetoothUuid.ProtocolUuid = ...
        Avdtp: QBluetoothUuid.ProtocolUuid = ...
        Cmtp: QBluetoothUuid.ProtocolUuid = ...
        UdiCPlain: QBluetoothUuid.ProtocolUuid = ...
        McapControlChannel: QBluetoothUuid.ProtocolUuid = ...
        McapDataChannel: QBluetoothUuid.ProtocolUuid = ...
        L2cap: QBluetoothUuid.ProtocolUuid = ...

    class ServiceClassUuid(IntFlag):
        ServiceDiscoveryServer: QBluetoothUuid.ServiceClassUuid = ...
        BrowseGroupDescriptor: QBluetoothUuid.ServiceClassUuid = ...
        PublicBrowseGroup: QBluetoothUuid.ServiceClassUuid = ...
        SerialPort: QBluetoothUuid.ServiceClassUuid = ...
        LANAccessUsingPPP: QBluetoothUuid.ServiceClassUuid = ...
        DialupNetworking: QBluetoothUuid.ServiceClassUuid = ...
        IrMCSync: QBluetoothUuid.ServiceClassUuid = ...
        ObexObjectPush: QBluetoothUuid.ServiceClassUuid = ...
        OBEXFileTransfer: QBluetoothUuid.ServiceClassUuid = ...
        IrMCSyncCommand: QBluetoothUuid.ServiceClassUuid = ...
        Headset: QBluetoothUuid.ServiceClassUuid = ...
        AudioSource: QBluetoothUuid.ServiceClassUuid = ...
        AudioSink: QBluetoothUuid.ServiceClassUuid = ...
        AV_RemoteControlTarget: QBluetoothUuid.ServiceClassUuid = ...
        AdvancedAudioDistribution: QBluetoothUuid.ServiceClassUuid = ...
        AV_RemoteControl: QBluetoothUuid.ServiceClassUuid = ...
        AV_RemoteControlController: QBluetoothUuid.ServiceClassUuid = ...
        HeadsetAG: QBluetoothUuid.ServiceClassUuid = ...
        PANU: QBluetoothUuid.ServiceClassUuid = ...
        NAP: QBluetoothUuid.ServiceClassUuid = ...
        GN: QBluetoothUuid.ServiceClassUuid = ...
        DirectPrinting: QBluetoothUuid.ServiceClassUuid = ...
        ReferencePrinting: QBluetoothUuid.ServiceClassUuid = ...
        BasicImage: QBluetoothUuid.ServiceClassUuid = ...
        ImagingResponder: QBluetoothUuid.ServiceClassUuid = ...
        ImagingAutomaticArchive: QBluetoothUuid.ServiceClassUuid = ...
        ImagingReferenceObjects: QBluetoothUuid.ServiceClassUuid = ...
        Handsfree: QBluetoothUuid.ServiceClassUuid = ...
        HandsfreeAudioGateway: QBluetoothUuid.ServiceClassUuid = ...
        DirectPrintingReferenceObjectsService: QBluetoothUuid.ServiceClassUuid = ...
        ReflectedUI: QBluetoothUuid.ServiceClassUuid = ...
        BasicPrinting: QBluetoothUuid.ServiceClassUuid = ...
        PrintingStatus: QBluetoothUuid.ServiceClassUuid = ...
        HumanInterfaceDeviceService: QBluetoothUuid.ServiceClassUuid = ...
        HardcopyCableReplacement: QBluetoothUuid.ServiceClassUuid = ...
        HCRPrint: QBluetoothUuid.ServiceClassUuid = ...
        HCRScan: QBluetoothUuid.ServiceClassUuid = ...
        SIMAccess: QBluetoothUuid.ServiceClassUuid = ...
        PhonebookAccessPCE: QBluetoothUuid.ServiceClassUuid = ...
        PhonebookAccessPSE: QBluetoothUuid.ServiceClassUuid = ...
        PhonebookAccess: QBluetoothUuid.ServiceClassUuid = ...
        HeadsetHS: QBluetoothUuid.ServiceClassUuid = ...
        MessageAccessServer: QBluetoothUuid.ServiceClassUuid = ...
        MessageNotificationServer: QBluetoothUuid.ServiceClassUuid = ...
        MessageAccessProfile: QBluetoothUuid.ServiceClassUuid = ...
        GNSS: QBluetoothUuid.ServiceClassUuid = ...
        GNSSServer: QBluetoothUuid.ServiceClassUuid = ...
        Display3D: QBluetoothUuid.ServiceClassUuid = ...
        Glasses3D: QBluetoothUuid.ServiceClassUuid = ...
        Synchronization3D: QBluetoothUuid.ServiceClassUuid = ...
        MPSProfile: QBluetoothUuid.ServiceClassUuid = ...
        MPSService: QBluetoothUuid.ServiceClassUuid = ...
        PnPInformation: QBluetoothUuid.ServiceClassUuid = ...
        GenericNetworking: QBluetoothUuid.ServiceClassUuid = ...
        GenericFileTransfer: QBluetoothUuid.ServiceClassUuid = ...
        GenericAudio: QBluetoothUuid.ServiceClassUuid = ...
        GenericTelephony: QBluetoothUuid.ServiceClassUuid = ...
        VideoSource: QBluetoothUuid.ServiceClassUuid = ...
        VideoSink: QBluetoothUuid.ServiceClassUuid = ...
        VideoDistribution: QBluetoothUuid.ServiceClassUuid = ...
        HDP: QBluetoothUuid.ServiceClassUuid = ...
        HDPSource: QBluetoothUuid.ServiceClassUuid = ...
        HDPSink: QBluetoothUuid.ServiceClassUuid = ...
        GenericAccess: QBluetoothUuid.ServiceClassUuid = ...
        GenericAttribute: QBluetoothUuid.ServiceClassUuid = ...
        ImmediateAlert: QBluetoothUuid.ServiceClassUuid = ...
        LinkLoss: QBluetoothUuid.ServiceClassUuid = ...
        TxPower: QBluetoothUuid.ServiceClassUuid = ...
        CurrentTimeService: QBluetoothUuid.ServiceClassUuid = ...
        ReferenceTimeUpdateService: QBluetoothUuid.ServiceClassUuid = ...
        NextDSTChangeService: QBluetoothUuid.ServiceClassUuid = ...
        Glucose: QBluetoothUuid.ServiceClassUuid = ...
        HealthThermometer: QBluetoothUuid.ServiceClassUuid = ...
        DeviceInformation: QBluetoothUuid.ServiceClassUuid = ...
        HeartRate: QBluetoothUuid.ServiceClassUuid = ...
        PhoneAlertStatusService: QBluetoothUuid.ServiceClassUuid = ...
        BatteryService: QBluetoothUuid.ServiceClassUuid = ...
        BloodPressure: QBluetoothUuid.ServiceClassUuid = ...
        AlertNotificationService: QBluetoothUuid.ServiceClassUuid = ...
        HumanInterfaceDevice: QBluetoothUuid.ServiceClassUuid = ...
        ScanParameters: QBluetoothUuid.ServiceClassUuid = ...
        RunningSpeedAndCadence: QBluetoothUuid.ServiceClassUuid = ...
        CyclingSpeedAndCadence: QBluetoothUuid.ServiceClassUuid = ...
        CyclingPower: QBluetoothUuid.ServiceClassUuid = ...
        LocationAndNavigation: QBluetoothUuid.ServiceClassUuid = ...
        EnvironmentalSensing: QBluetoothUuid.ServiceClassUuid = ...
        BodyComposition: QBluetoothUuid.ServiceClassUuid = ...
        UserData: QBluetoothUuid.ServiceClassUuid = ...
        WeightScale: QBluetoothUuid.ServiceClassUuid = ...
        BondManagement: QBluetoothUuid.ServiceClassUuid = ...
        ContinuousGlucoseMonitoring: QBluetoothUuid.ServiceClassUuid = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid

        **QBluetoothUuid::QBluetoothUuid()**

        Constructs a new null Bluetooth UUID.
        """
        ...
    @overload
    def __init__(
        self, uuid: PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid-1

        **QBluetoothUuid::QBluetoothUuid(QBluetoothUuid::ProtocolUuid uuid )**

        Constructs a new Bluetooth UUID from the protocol **uuid**.
        """
        ...
    @overload
    def __init__(self, uuid: PySide6.QtBluetooth.QBluetoothUuid.DescriptorType) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid-2

        **QBluetoothUuid::QBluetoothUuid(QBluetoothUuid::ServiceClassUuid uuid
        )**

        Constructs a new Bluetooth UUID from the service class **uuid**.
        """
        ...
    @overload
    def __init__(self, uuid: PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid-3

        **[since 5.4]
        QBluetoothUuid::QBluetoothUuid(QBluetoothUuid::CharacteristicType uuid
        )**

        Constructs a new Bluetooth UUID from the characteristic type **uuid**.

        This function was introduced in Qt 5.4.
        """
        ...
    @overload
    def __init__(self, uuid: PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid-4

        **[since 5.4]
        QBluetoothUuid::QBluetoothUuid(QBluetoothUuid::DescriptorType uuid )**

        Constructs a new Bluetooth UUID from the descriptor type **uuid**.

        This function was introduced in Qt 5.4.
        """
        ...
    @overload
    def __init__(self, uuid: PySide6.QtCore.QUuid) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid-5

        **QBluetoothUuid::QBluetoothUuid(quint16 uuid )**

        Constructs a new Bluetooth UUID from the 16 bit **uuid**.
        """
        ...
    @overload
    def __init__(self, uuid: str) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid-6

        **QBluetoothUuid::QBluetoothUuid(quint32 uuid )**

        Constructs a new Bluetooth UUID from the 32 bit **uuid**.
        """
        ...
    @overload
    def __init__(self, uuid: int) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid-7

        **QBluetoothUuid::QBluetoothUuid(quint128 uuid )**

        Constructs a new Bluetooth UUID from the 128 bit **uuid**.

        Note that **uuid** must be in big endian order.
        """
        ...
    @overload
    def __init__(self, uuid: int) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid-8

        **QBluetoothUuid::QBluetoothUuid(const QString & uuid )**

        Creates a QBluetoothUuid object from the string **uuid** , which must be
        formatted as five hex fields separated by '-', e.g., "{xxxxxxxx-xxxx-
        xxxx-xxxx-xxxxxxxxxxxx}" where 'x' is a hex digit. The curly braces
        shown here are optional, but it is normal to include them. If the
        conversion fails, a null UUID is created. See **QUuid::toString** () for
        an explanation of how the five hex fields map to the public data members
        in **QUuid** .
        """
        ...
    @overload
    def __init__(
        self,
        uuid: (
            PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType
            | PySide6.QtBluetooth.QBluetoothUuid.DescriptorType
            | PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid
            | PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid
            | PySide6.QtCore.QUuid
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid-10

        **QBluetoothUuid::QBluetoothUuid(const QUuid & uuid )**

        Constructs a new Bluetooth UUID that is a copy of **uuid**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, s: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, s: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    @staticmethod
    def characteristicToString(
        uuid: PySide6.QtBluetooth.QBluetoothUuid.CharacteristicType,
    ) -> str:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#characteristicToString

        **[static, since 5.4] QString QBluetoothUuid::characteristicToString(QBl
        uetoothUuid::CharacteristicType uuid )**

        Returns a human-readable and translated name for the given
        characteristic type represented by **uuid**.

        This function was introduced in Qt 5.4.

        **See also** **QBluetoothUuid::CharacteristicType** .
        """
        ...
    @staticmethod
    def descriptorToString(
        uuid: PySide6.QtBluetooth.QBluetoothUuid.DescriptorType,
    ) -> str:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#descriptorToString

        **[static, since 5.4] QString
        QBluetoothUuid::descriptorToString(QBluetoothUuid::DescriptorType uuid
        )**

        Returns a human-readable and translated name for the given descriptor
        type represented by **uuid**.

        This function was introduced in Qt 5.4.

        **See also** **QBluetoothUuid::DescriptorType** .
        """
        ...
    def minimumSize(self) -> int:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#minimumSize

        **int QBluetoothUuid::minimumSize() const**

        Returns the minimum size in bytes that this UUID can be represented in.
        For non-null UUIDs 2, 4 or 16 is returned. 0 is returned for null UUIDs.

        **See also** **isNull** (), **toUInt16** (), **toUInt32** (), and
        **toUInt128** ().
        """
        ...
    @staticmethod
    def protocolToString(uuid: PySide6.QtBluetooth.QBluetoothUuid.ProtocolUuid) -> str:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#protocolToString

        **[static, since 5.4] QString
        QBluetoothUuid::protocolToString(QBluetoothUuid::ProtocolUuid uuid )**

        Returns a human-readable and translated name for the given protocol
        represented by **uuid**.

        This function was introduced in Qt 5.4.

        **See also** **QBluetoothUuid::ProtocolUuid** .
        """
        ...
    @staticmethod
    def serviceClassToString(
        uuid: PySide6.QtBluetooth.QBluetoothUuid.ServiceClassUuid,
    ) -> str:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#serviceClassToString

        **[static, since Qt 5.4] QString
        QBluetoothUuid::serviceClassToString(QBluetoothUuid::ServiceClassUuid
        uuid )**

        Returns a human-readable and translated name for the given service class
        represented by **uuid**.

        This function was introduced in Qt 5.4.

        **See also** **QBluetoothUuid::ServiceClassUuid** .
        """
        ...
    def toUInt16(self) -> tuple[int, bool]:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#toUInt16

        **quint16 QBluetoothUuid::toUInt16(bool * ok = nullptr) const**

        Returns the 16 bit representation of this UUID. If **ok** is passed, it
        is set to true if the conversion is possible, otherwise it is set to
        false. The return value is undefined if **ok** is set to false.
        """
        ...
    def toUInt32(self) -> tuple[int, bool]:
        """
        https://doc.qt.io/qt-6/qbluetoothuuid.html#toUInt32

        **quint32 QBluetoothUuid::toUInt32(bool * ok = nullptr) const**

        Returns the 32 bit representation of this UUID. If **ok** is passed, it
        is set to true if the conversion is possible, otherwise it is set to
        false. The return value is undefined if **ok** is set to false.
        """
        ...
