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
PySide6.QtWebEngineQuick, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from collections.abc import Sequence
from enum import IntFlag

import PySide6.QtCore
import PySide6.QtWebEngineQuick

class QQuickWebEngineProfile(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qquickwebengineprofile.html

    **Detailed Description**

    A web engine profile contains settings, scripts, persistent cookie policy,
    and the list of visited links shared by all web engine pages that belong to
    the profile.

    Information about visited links is stored together with persistent cookies
    and other persistent data in a storage determined by the **storageName**
    property. Persistent data is stored in a subdirectory determined by the
    **persistentStoragePath**  property and the cache in a subdirectory
    determined by the **cachePath**  property. The **httpCacheType**  property
    describes the type of the cache: **in-memory** or **on-disk**. If only the
    **storageName**  property is set, the other values are generated
    automatically based on it. If you specify any of the values manually, you
    should do it before creating any pages that belong to the profile.

    Profiles can be used to isolate pages from each other. A typical use case is
    a dedicated **off-the-record profile** for a **private browsing** mode. An
    off-the-record profile forces cookies, the HTTP cache, and other normally
    persistent data to be stored only in memory. The **offTheRecord**  property
    holds whether a profile is off-the-record.

    The default profile can be accessed by **defaultProfile** (). It is a built-
    in profile that all web pages not specifically created with another profile
    belong to.

    A **WebEngineProfile**  instance can be created and accessed from C++
    through the QQuickWebEngineProfile class, which exposes further
    functionality in C++. This allows Qt Quick applications to intercept URL
    requests (QQuickWebEngineProfile::setRequestInterceptor), or register custom
    URL schemes (**QQuickWebEngineProfile::installUrlSchemeHandler** ).

    Spellchecking HTML form fields can be enabled per profile by setting the
    **spellCheckEnabled**  property and the current languages used for
    spellchecking can be set by using the **spellCheckLanguages**  property.
    """

    MemoryHttpCache: QQuickWebEngineProfile.HttpCacheType = ...
    DiskHttpCache: QQuickWebEngineProfile.HttpCacheType = ...
    NoCache: QQuickWebEngineProfile.HttpCacheType = ...
    NoPersistentCookies: QQuickWebEngineProfile.PersistentCookiesPolicy = ...
    AllowPersistentCookies: QQuickWebEngineProfile.PersistentCookiesPolicy = ...
    ForcePersistentCookies: QQuickWebEngineProfile.PersistentCookiesPolicy = ...

    class HttpCacheType(IntFlag):
        MemoryHttpCache: QQuickWebEngineProfile.HttpCacheType = ...
        DiskHttpCache: QQuickWebEngineProfile.HttpCacheType = ...
        NoCache: QQuickWebEngineProfile.HttpCacheType = ...

    class PersistentCookiesPolicy(IntFlag):
        NoPersistentCookies: QQuickWebEngineProfile.PersistentCookiesPolicy = ...
        AllowPersistentCookies: QQuickWebEngineProfile.PersistentCookiesPolicy = ...
        ForcePersistentCookies: QQuickWebEngineProfile.PersistentCookiesPolicy = ...
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#QQuickWebEngineProfil
        e

        **QQuickWebEngineProfile::QQuickWebEngineProfile(QObject * parent =
        nullptr)**

        Constructs a new profile with the parent **parent**.
        """
        ...
    def cachePath(self) -> str:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#cachePath-prop

        **cachePath : QString**

        The path to the location where the profile's caches are stored, in
        particular the HTTP cache.

        By default, the caches are stored below
        **QStandardPaths::writableLocation** (**QStandardPaths::CacheLocation**
        ) in a directory named using **storageName** .

        **Access functions:**

        QString **cachePath** () const
        void **setCachePath** (const QString &
        **path** )

        **Notifier signal:**

        void **cachePathChanged** ()
        """
        ...
    def clearHttpCache(self) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#clearHttpCache

        **[invokable, since 5.7] void QQuickWebEngineProfile::clearHttpCache()**

        Removes the profile's cache entries.

        **Note:** This function can be invoked via the meta-object system and
        from QML. See **Q_INVOKABLE** .

        This function was introduced in Qt 5.7.

        **See also** **WebEngineProfile::clearHttpCache** .
        """
        ...
    @staticmethod
    def defaultProfile() -> PySide6.QtWebEngineQuick.QQuickWebEngineProfile:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#defaultProfile

        **[static] QQuickWebEngineProfile
        *QQuickWebEngineProfile::defaultProfile()**

        Returns the default profile.

        The default profile uses the storage name "Default".

        **See also** **storageName** ().
        """
        ...
    def downloadPath(self) -> str:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#downloadPath-prop

        **[since QtWebEngine 1.9] downloadPath : QString**

        The path to the location where the downloaded files are stored.

        Overrides the default path used for download location, setting it to
        **path**.

        If set to an empty string, the default path is restored.

        **Note:** By default, the download path is
        **QStandardPaths::DownloadLocation** .

        This property was introduced in QtWebEngine 1.9.

        **Access functions:**

        QString **downloadPath** () const
        void **setDownloadPath** (const
        QString & **path** )

        **Notifier signal:**

        void **downloadPathChanged** ()
        """
        ...
    def httpAcceptLanguage(self) -> str:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpAcceptLanguage-
        prop

        **httpAcceptLanguage : QString**

        The value of the Accept-Language HTTP request-header field.

        **Access functions:**

        QString **httpAcceptLanguage** () const
        void **setHttpAcceptLanguage**
        (const QString & **httpAcceptLanguage** )

        **Notifier signal:**

        void **httpAcceptLanguageChanged** ()
        """
        ...
    def httpCacheMaximumSize(self) -> int:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpCacheMaximumSize-
        prop

        **httpCacheMaximumSize : int**

        The maximum size of the HTTP cache. If `0`, the size will be controlled
        automatically by **QtWebEngine** . The default value is `0`.

        **Access functions:**

        int **httpCacheMaximumSize** () const
        void **setHttpCacheMaximumSize**
        (int **maxSize** )

        **Notifier signal:**

        void **httpCacheMaximumSizeChanged** ()

        **See also** **httpCacheType** .
        """
        ...
    def httpCacheType(
        self,
    ) -> PySide6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpCacheType-prop

        **httpCacheType : HttpCacheType**

        This enumeration describes the type of the HTTP cache.

        If the profile is off-the-record, **MemoryHttpCache**  is returned.

        **Access functions:**

        QQuickWebEngineProfile::HttpCacheType **httpCacheType** () const
        void
        **setHttpCacheType** (QQuickWebEngineProfile::HttpCacheType)

        **Notifier signal:**

        void **httpCacheTypeChanged** ()
        """
        ...
    def httpUserAgent(self) -> str:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpUserAgent-prop

        **httpUserAgent : QString**

        The user-agent string sent with HTTP to identify the browser.

        **Access functions:**

        QString **httpUserAgent** () const
        void **setHttpUserAgent** (const
        QString & **userAgent** )

        **Notifier signal:**

        void **httpUserAgentChanged** ()
        """
        ...
    def isOffTheRecord(self) -> bool: ...
    def isSpellCheckEnabled(self) -> bool: ...
    def persistentCookiesPolicy(
        self,
    ) -> PySide6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#persistentCookiesPoli
        cy-prop

        **persistentCookiesPolicy : PersistentCookiesPolicy**

        This enumeration describes the policy of cookie persistency. If the
        profile is off-the-record, **NoPersistentCookies**  is returned.

        **Access functions:**

        QQuickWebEngineProfile::PersistentCookiesPolicy
        **persistentCookiesPolicy** () const
        void
        **setPersistentCookiesPolicy**
        (QQuickWebEngineProfile::PersistentCookiesPolicy)

        **Notifier signal:**

        void **persistentCookiesPolicyChanged** ()
        """
        ...
    def persistentStoragePath(self) -> str:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#persistentStoragePath
        -prop

        **persistentStoragePath : QString**

        The path to the location where the persistent data for the browser and
        web content are stored. Persistent data includes persistent cookies,
        HTML5 local storage, and visited links.

        By default, the storage is located below
        **QStandardPaths::writableLocation** (QStandardPaths::DataLocation) in a
        directory named using **storageName** .

        **Access functions:**

        QString **persistentStoragePath** () const
        void
        **setPersistentStoragePath** (const QString & **path** )

        **Notifier signal:**

        void **persistentStoragePathChanged** ()
        """
        ...
    def removeAllUrlSchemeHandlers(self) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#removeAllUrlSchemeHan
        dlers

        **void QQuickWebEngineProfile::removeAllUrlSchemeHandlers()**

        Removes all custom URL scheme handlers installed in the profile.
        """
        ...
    def removeUrlScheme(self, scheme: PySide6.QtCore.QByteArray | bytes) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#removeUrlScheme

        **void QQuickWebEngineProfile::removeUrlScheme(const QByteArray & scheme
        )**

        Removes the custom URL scheme **scheme** from the profile.

        **See also** **removeUrlSchemeHandler** ().
        """
        ...
    def setCachePath(self, path: str) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#cachePath-prop

        **cachePath : QString**

        The path to the location where the profile's caches are stored, in
        particular the HTTP cache.

        By default, the caches are stored below
        **QStandardPaths::writableLocation** (**QStandardPaths::CacheLocation**
        ) in a directory named using **storageName** .

        **Access functions:**

        QString **cachePath** () const
        void **setCachePath** (const QString &
        **path** )

        **Notifier signal:**

        void **cachePathChanged** ()
        """
        ...
    def setDownloadPath(self, path: str) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#downloadPath-prop

        **[since QtWebEngine 1.9] downloadPath : QString**

        The path to the location where the downloaded files are stored.

        Overrides the default path used for download location, setting it to
        **path**.

        If set to an empty string, the default path is restored.

        **Note:** By default, the download path is
        **QStandardPaths::DownloadLocation** .

        This property was introduced in QtWebEngine 1.9.

        **Access functions:**

        QString **downloadPath** () const
        void **setDownloadPath** (const
        QString & **path** )

        **Notifier signal:**

        void **downloadPathChanged** ()
        """
        ...
    def setHttpAcceptLanguage(self, httpAcceptLanguage: str) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpAcceptLanguage-
        prop

        **httpAcceptLanguage : QString**

        The value of the Accept-Language HTTP request-header field.

        **Access functions:**

        QString **httpAcceptLanguage** () const
        void **setHttpAcceptLanguage**
        (const QString & **httpAcceptLanguage** )

        **Notifier signal:**

        void **httpAcceptLanguageChanged** ()
        """
        ...
    def setHttpCacheMaximumSize(self, maxSize: int) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpCacheMaximumSize-
        prop

        **httpCacheMaximumSize : int**

        The maximum size of the HTTP cache. If `0`, the size will be controlled
        automatically by **QtWebEngine** . The default value is `0`.

        **Access functions:**

        int **httpCacheMaximumSize** () const
        void **setHttpCacheMaximumSize**
        (int **maxSize** )

        **Notifier signal:**

        void **httpCacheMaximumSizeChanged** ()

        **See also** **httpCacheType** .
        """
        ...
    def setHttpCacheType(
        self, arg__1: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType
    ) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpCacheType-prop

        **httpCacheType : HttpCacheType**

        This enumeration describes the type of the HTTP cache.

        If the profile is off-the-record, **MemoryHttpCache**  is returned.

        **Access functions:**

        QQuickWebEngineProfile::HttpCacheType **httpCacheType** () const
        void
        **setHttpCacheType** (QQuickWebEngineProfile::HttpCacheType)

        **Notifier signal:**

        void **httpCacheTypeChanged** ()
        """
        ...
    def setHttpUserAgent(self, userAgent: str) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpUserAgent-prop

        **httpUserAgent : QString**

        The user-agent string sent with HTTP to identify the browser.

        **Access functions:**

        QString **httpUserAgent** () const
        void **setHttpUserAgent** (const
        QString & **userAgent** )

        **Notifier signal:**

        void **httpUserAgentChanged** ()
        """
        ...
    def setOffTheRecord(self, offTheRecord: bool) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#offTheRecord-prop

        **offTheRecord : bool**

        Whether the web engine profile is **off-the-record**. An off-the-record
        profile forces cookies, the HTTP cache, and other normally persistent
        data to be stored only in memory.

        **Access functions:**

        bool **isOffTheRecord** () const
        void **setOffTheRecord** (bool
        **offTheRecord** )

        **Notifier signal:**

        void **offTheRecordChanged** ()
        """
        ...
    def setPersistentCookiesPolicy(
        self,
        arg__1: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#persistentCookiesPoli
        cy-prop

        **persistentCookiesPolicy : PersistentCookiesPolicy**

        This enumeration describes the policy of cookie persistency. If the
        profile is off-the-record, **NoPersistentCookies**  is returned.

        **Access functions:**

        QQuickWebEngineProfile::PersistentCookiesPolicy
        **persistentCookiesPolicy** () const
        void
        **setPersistentCookiesPolicy**
        (QQuickWebEngineProfile::PersistentCookiesPolicy)

        **Notifier signal:**

        void **persistentCookiesPolicyChanged** ()
        """
        ...
    def setPersistentStoragePath(self, path: str) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#persistentStoragePath
        -prop

        **persistentStoragePath : QString**

        The path to the location where the persistent data for the browser and
        web content are stored. Persistent data includes persistent cookies,
        HTML5 local storage, and visited links.

        By default, the storage is located below
        **QStandardPaths::writableLocation** (QStandardPaths::DataLocation) in a
        directory named using **storageName** .

        **Access functions:**

        QString **persistentStoragePath** () const
        void
        **setPersistentStoragePath** (const QString & **path** )

        **Notifier signal:**

        void **persistentStoragePathChanged** ()
        """
        ...
    def setSpellCheckEnabled(self, enabled: bool) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#spellCheckEnabled-
        prop

        **[since QtWebEngine 1.4] spellCheckEnabled : bool**

        This property holds whether the web engine spell checker is enabled.

        This property was introduced in QtWebEngine 1.4.

        **Access functions:**

        bool **isSpellCheckEnabled** () const
        void **setSpellCheckEnabled**
        (bool **enabled** )

        **Notifier signal:**

        void **spellCheckEnabledChanged** ()
        """
        ...
    def setSpellCheckLanguages(self, languages: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#spellCheckLanguages

        **[since 5.8] QStringList QQuickWebEngineProfile::spellCheckLanguages()
        const**

        Returns the list of languages used by the spell checker.

        **Note:** Getter function for property spellCheckLanguages.

        This function was introduced in Qt 5.8.

        **See also** **setSpellCheckLanguages** ().
        """
        ...
    def setStorageName(self, name: str) -> None:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#storageName-prop

        **storageName : QString**

        The storage name that is used to create separate subdirectories for each
        profile that uses the disk for storing persistent data and cache.

        **Access functions:**

        QString **storageName** () const
        void **setStorageName** (const
        QString & **name** )

        **Notifier signal:**

        void **storageNameChanged** ()

        **See also** **persistentStoragePath**  and **cachePath** .

        **Member Function Documentation**
        """
        ...
    def spellCheckLanguages(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#spellCheckLanguages-
        prop

        **[since QtWebEngine 1.4] spellCheckLanguages : QStringList**

        This property holds the languages used by the spell checker.

        This property was introduced in QtWebEngine 1.4.

        **Access functions:**

        QStringList ****spellCheckLanguages** ** () const
        void
        **setSpellCheckLanguages** (const QStringList & **languages** )

        **Notifier signal:**

        void **spellCheckLanguagesChanged** ()
        """
        ...
    def storageName(self) -> str:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#storageName-prop

        **storageName : QString**

        The storage name that is used to create separate subdirectories for each
        profile that uses the disk for storing persistent data and cache.

        **Access functions:**

        QString **storageName** () const
        void **setStorageName** (const
        QString & **name** )

        **Notifier signal:**

        void **storageNameChanged** ()

        **See also** **persistentStoragePath**  and **cachePath** .

        **Member Function Documentation**
        """
        ...
    @property
    def cachePathChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def downloadFinished(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#downloadFinished

        **[signal] void
        QQuickWebEngineProfile::downloadFinished(QQuickWebEngineDownloadRequest
        * download )**

        This signal is emitted whenever downloading stops, because it finished
        successfully, was cancelled, or was interrupted (for example, because
        connectivity was lost). The **download** argument holds the state of the
        finished download instance.
        """
        ...
    @property
    def downloadPathChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def downloadRequested(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#downloadRequested

        **[signal] void
        QQuickWebEngineProfile::downloadRequested(QQuickWebEngineDownloadRequest
        * download )**

        This signal is emitted whenever a download has been triggered. The
        **download** argument holds the state of the download. The download has
        to be explicitly accepted with `QWebEngineDownloadRequest::accept()` or
        it will be cancelled by default. The download item is parented by the
        profile. If it is not accepted, it will be deleted immediately after the
        signal emission. This signal cannot be used with a queued connection.
        """
        ...
    @property
    def httpAcceptLanguageChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def httpCacheMaximumSizeChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def httpCacheTypeChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def httpUserAgentChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def offTheRecordChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def persistentCookiesPolicyChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def persistentStoragePathChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def presentNotification(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qquickwebengineprofile.html#presentNotification

        **[signal] void
        QQuickWebEngineProfile::presentNotification(QWebEngineNotification *
        notification )**

        This signal is emitted whenever there is a newly created user
        notification. The **notification** argument holds the
        **QWebEngineNotification**  instance to query data and interact with.

        **See also** **WebEngineProfile::presentNotification** .
        """
        ...
    @property
    def spellCheckEnabledChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def spellCheckLanguagesChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def storageNameChanged(self) -> PySide6.QtCore.SignalInstance: ...