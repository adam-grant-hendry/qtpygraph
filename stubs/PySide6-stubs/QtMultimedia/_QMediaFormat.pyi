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

class QMediaFormat:
    """
    https://doc.qt.io/qt-6/qmediaformat.html

    **Detailed Description**

    QMediaFormat describes an encoding format for a multimedia file or stream.

    You can check whether a certain media format can be used for encoding or
    decoding using QMediaFormat.
    """

    Encode: QMediaFormat.ConversionMode = ...
    Decode: QMediaFormat.ConversionMode = ...
    UnspecifiedFormat: QMediaFormat.FileFormat = ...
    WMV: QMediaFormat.FileFormat = ...
    AVI: QMediaFormat.FileFormat = ...
    Matroska: QMediaFormat.FileFormat = ...
    MPEG4: QMediaFormat.FileFormat = ...
    Ogg: QMediaFormat.FileFormat = ...
    QuickTime: QMediaFormat.FileFormat = ...
    WebM: QMediaFormat.FileFormat = ...
    Mpeg4Audio: QMediaFormat.FileFormat = ...
    AAC: QMediaFormat.FileFormat = ...
    WMA: QMediaFormat.FileFormat = ...
    MP3: QMediaFormat.FileFormat = ...
    FLAC: QMediaFormat.FileFormat = ...
    LastFileFormat: QMediaFormat.FileFormat = ...
    Wave: QMediaFormat.FileFormat = ...
    NoFlags: QMediaFormat.ResolveFlags = ...
    RequiresVideo: QMediaFormat.ResolveFlags = ...

    class AudioCodec(IntFlag):
        Unspecified: QMediaFormat.AudioCodec = ...
        MP3: QMediaFormat.AudioCodec = ...
        AAC: QMediaFormat.AudioCodec = ...
        AC3: QMediaFormat.AudioCodec = ...
        EAC3: QMediaFormat.AudioCodec = ...
        FLAC: QMediaFormat.AudioCodec = ...
        DolbyTrueHD: QMediaFormat.AudioCodec = ...
        Opus: QMediaFormat.AudioCodec = ...
        Vorbis: QMediaFormat.AudioCodec = ...
        Wave: QMediaFormat.AudioCodec = ...
        WMA: QMediaFormat.AudioCodec = ...
        ALAC: QMediaFormat.AudioCodec = ...
        LastAudioCodec: QMediaFormat.AudioCodec = ...

    class ConversionMode(IntFlag):
        Encode: QMediaFormat.ConversionMode = ...
        Decode: QMediaFormat.ConversionMode = ...

    class FileFormat(IntFlag):
        UnspecifiedFormat: QMediaFormat.FileFormat = ...
        WMV: QMediaFormat.FileFormat = ...
        AVI: QMediaFormat.FileFormat = ...
        Matroska: QMediaFormat.FileFormat = ...
        MPEG4: QMediaFormat.FileFormat = ...
        Ogg: QMediaFormat.FileFormat = ...
        QuickTime: QMediaFormat.FileFormat = ...
        WebM: QMediaFormat.FileFormat = ...
        Mpeg4Audio: QMediaFormat.FileFormat = ...
        AAC: QMediaFormat.FileFormat = ...
        WMA: QMediaFormat.FileFormat = ...
        MP3: QMediaFormat.FileFormat = ...
        FLAC: QMediaFormat.FileFormat = ...
        LastFileFormat: QMediaFormat.FileFormat = ...
        Wave: QMediaFormat.FileFormat = ...

    class ResolveFlags(IntFlag):
        NoFlags: QMediaFormat.ResolveFlags = ...
        RequiresVideo: QMediaFormat.ResolveFlags = ...

    class VideoCodec(IntFlag):
        Unspecified: QMediaFormat.VideoCodec = ...
        MPEG1: QMediaFormat.VideoCodec = ...
        MPEG2: QMediaFormat.VideoCodec = ...
        MPEG4: QMediaFormat.VideoCodec = ...
        H264: QMediaFormat.VideoCodec = ...
        H265: QMediaFormat.VideoCodec = ...
        VP8: QMediaFormat.VideoCodec = ...
        VP9: QMediaFormat.VideoCodec = ...
        AV1: QMediaFormat.VideoCodec = ...
        Theora: QMediaFormat.VideoCodec = ...
        WMV: QMediaFormat.VideoCodec = ...
        LastVideoCodec: QMediaFormat.VideoCodec = ...
        MotionJPEG: QMediaFormat.VideoCodec = ...
    @overload
    def __init__(
        self, format: PySide6.QtMultimedia.QMediaFormat.FileFormat = ...
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#QMediaFormat

        **QMediaFormat::QMediaFormat(QMediaFormat::FileFormat format =
        UnspecifiedFormat)**

        Constructs a QMediaFormat object for **format**.
        """
        ...
    @overload
    def __init__(
        self,
        other: (
            PySide6.QtMultimedia.QMediaFormat
            | PySide6.QtMultimedia.QMediaFormat.FileFormat
        ),
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#QMediaFormat-1

        **QMediaFormat::QMediaFormat(const QMediaFormat & other )**

        Constructs a QMediaFormat object by copying from **other**.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def audioCodec(self) -> PySide6.QtMultimedia.QMediaFormat.AudioCodec:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#audioCodec

        **QMediaFormat::AudioCodec QMediaFormat::audioCodec() const**

        Returns the audio codec used in this format.

        **Note:** Getter function for property audioCodec.

        **See also** **setAudioCodec** () and **QMediaFormat::AudioCodec** .
        """
        ...
    @staticmethod
    def audioCodecDescription(
        codec: PySide6.QtMultimedia.QMediaFormat.AudioCodec,
    ) -> str:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#audioCodecDescription

        **[static invokable] QString
        QMediaFormat::audioCodecDescription(QMediaFormat::AudioCodec codec )**

        Returns a description for **codec**.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    @staticmethod
    def audioCodecName(codec: PySide6.QtMultimedia.QMediaFormat.AudioCodec) -> str:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#audioCodecName

        **[static invokable] QString
        QMediaFormat::audioCodecName(QMediaFormat::AudioCodec codec )**

        Returns a string based name for **codec**.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def fileFormat(self) -> PySide6.QtMultimedia.QMediaFormat.FileFormat:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#fileFormat-prop

        **fileFormat : FileFormat**

        This property holds the file (container) format of the media.

        **Access functions:**

        QMediaFormat::FileFormat **fileFormat** () const
        void
        **setFileFormat** (QMediaFormat::FileFormat **f** )

        **See also** **QMediaFormat::FileFormat** .
        """
        ...
    @staticmethod
    def fileFormatDescription(
        fileFormat: PySide6.QtMultimedia.QMediaFormat.FileFormat,
    ) -> str:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#fileFormatDescription

        **[static invokable] QString
        QMediaFormat::fileFormatDescription(QMediaFormat::FileFormat fileFormat
        )**

        Returns a description for **fileFormat**.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    @staticmethod
    def fileFormatName(fileFormat: PySide6.QtMultimedia.QMediaFormat.FileFormat) -> str:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#fileFormatName

        **[static invokable] QString
        QMediaFormat::fileFormatName(QMediaFormat::FileFormat fileFormat )**

        Returns a string based name for **fileFormat**.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def isSupported(self, mode: PySide6.QtMultimedia.QMediaFormat.ConversionMode) -> bool:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#isSupported

        **[invokable] bool
        QMediaFormat::isSupported(QMediaFormat::ConversionMode mode ) const**

        Returns `true` if Qt Multimedia can encode or decode this format,
        depending on **mode**.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    def mimeType(self) -> PySide6.QtCore.QMimeType:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#mimeType

        **QMimeType QMediaFormat::mimeType() const**

        Returns the **MIME type**  for the file format used in this media
        format.
        """
        ...
    def resolveForEncoding(
        self, flags: PySide6.QtMultimedia.QMediaFormat.ResolveFlags
    ) -> None:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#resolveForEncoding

        **void QMediaFormat::resolveForEncoding(QMediaFormat::ResolveFlags flags
        )**

        Resolves the format, based on **flags** , to a format that is supported
        by **QMediaRecorder** .

        This method tries to find the best possible match for unspecified
        settings. Settings that are not supported by the recorder will be
        modified to the closest match that is supported.

        When resolving, priority is given in the following order:

        1. File format
          2. Video codec
          3. Audio codec
        """
        ...
    def setAudioCodec(self, codec: PySide6.QtMultimedia.QMediaFormat.AudioCodec) -> None:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#setAudioCodec

        **void QMediaFormat::setAudioCodec(QMediaFormat::AudioCodec codec )**

        Sets the audio codec to **codec**.

        **Note:** Setter function for property **audioCodec** .

        **See also** **audioCodec** () and **QMediaFormat::AudioCodec** .
        """
        ...
    def setFileFormat(self, f: PySide6.QtMultimedia.QMediaFormat.FileFormat) -> None:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#fileFormat-prop

        **fileFormat : FileFormat**

        This property holds the file (container) format of the media.

        **Access functions:**

        QMediaFormat::FileFormat **fileFormat** () const
        void
        **setFileFormat** (QMediaFormat::FileFormat **f** )

        **See also** **QMediaFormat::FileFormat** .
        """
        ...
    def setVideoCodec(self, codec: PySide6.QtMultimedia.QMediaFormat.VideoCodec) -> None:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#setVideoCodec

        **void QMediaFormat::setVideoCodec(QMediaFormat::VideoCodec codec )**

        Sets the video codec to **codec**.

        **Note:** Setter function for property **videoCodec** .

        **See also** **videoCodec** () and **QMediaFormat::VideoCodec** .
        """
        ...
    def supportedAudioCodecs(
        self, m: PySide6.QtMultimedia.QMediaFormat.ConversionMode
    ) -> list[PySide6.QtMultimedia.QMediaFormat.AudioCodec]:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#supportedAudioCodecs

        **[invokable] QList<QMediaFormat::AudioCodec>
        QMediaFormat::supportedAudioCodecs(QMediaFormat::ConversionMode m )**

        Returns a list of audio codecs for the chosen file format and video
        codec ( **m** ).

        To get all supported audio codecs, run this query on a default
        constructed **QMediaFormat** .

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        **See also** **QMediaFormat::ConversionMode** .
        """
        ...
    def supportedFileFormats(
        self, m: PySide6.QtMultimedia.QMediaFormat.ConversionMode
    ) -> list[PySide6.QtMultimedia.QMediaFormat.FileFormat]:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#supportedFileFormats

        **[invokable] QList<QMediaFormat::FileFormat>
        QMediaFormat::supportedFileFormats(QMediaFormat::ConversionMode m )**

        Returns a list of file formats for the audio and video codec indicated
        by **m**.

        To get all supported file formats, run this query on a default
        constructed **QMediaFormat** .

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        **See also** **QMediaFormat::ConversionMode** .
        """
        ...
    def supportedVideoCodecs(
        self, m: PySide6.QtMultimedia.QMediaFormat.ConversionMode
    ) -> list[PySide6.QtMultimedia.QMediaFormat.VideoCodec]:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#supportedVideoCodecs

        **[invokable] QList<QMediaFormat::VideoCodec>
        QMediaFormat::supportedVideoCodecs(QMediaFormat::ConversionMode m )**

        Returns a list of video codecs for the chosen file format and audio
        codec ( **m** ).

        To get all supported video codecs, run this query on a default
        constructed MediaFormat.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        **See also** **QMediaFormat::ConversionMode** .
        """
        ...
    def swap(
        self,
        other: (
            PySide6.QtMultimedia.QMediaFormat
            | PySide6.QtMultimedia.QMediaFormat.FileFormat
        ),
    ) -> None: ...
    def videoCodec(self) -> PySide6.QtMultimedia.QMediaFormat.VideoCodec:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#videoCodec

        **QMediaFormat::VideoCodec QMediaFormat::videoCodec() const**

        Returns the video codec used in this format.

        **Note:** Getter function for property videoCodec.

        **See also** **setVideoCodec** () and **QMediaFormat::VideoCodec** .
        """
        ...
    @staticmethod
    def videoCodecDescription(
        codec: PySide6.QtMultimedia.QMediaFormat.VideoCodec,
    ) -> str:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#videoCodecDescription

        **[static invokable] QString
        QMediaFormat::videoCodecDescription(QMediaFormat::VideoCodec codec )**

        Returns a description for **codec**.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...
    @staticmethod
    def videoCodecName(codec: PySide6.QtMultimedia.QMediaFormat.VideoCodec) -> str:
        """
        https://doc.qt.io/qt-6/qmediaformat.html#videoCodecName

        **[static invokable] QString
        QMediaFormat::videoCodecName(QMediaFormat::VideoCodec codec )**

        Returns a string based name for **codec**.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .
        """
        ...