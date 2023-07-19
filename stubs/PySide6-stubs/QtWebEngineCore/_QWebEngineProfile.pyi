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
PySide6.QtWebEngineCore, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from collections.abc import Sequence
from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtNetwork
import PySide6.QtWebChannel
import PySide6.QtWebEngineCore

class QWebEngineProfile(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qwebengineprofile.html

    **Detailed Description**

    A web engine profile contains settings, scripts, persistent cookie policy,
    and the list of visited links shared by all web engine pages that belong to
    the profile.

    All pages that belong to the profile share a common **QWebEngineSettings**
    instance, which can be accessed with the **settings** () method. Likewise,
    the **scripts** () method provides access to a common
    **QWebEngineScriptCollection**  instance.

    Information about visited links is stored together with persistent cookies
    and other persistent data in a storage returned by **storageName** ().
    Persistent data is stored in a subdirectory set by calling
    **setPersistentStoragePath** (), and the cache is located in a subdirectory
    set by calling **setCachePath** (). The cache type can be set to **in-
    memory** or **on-disk** by calling **setHttpCacheType** (). If only the
    storage name is set, the subdirectories are created and named automatically.
    If you set any of the values manually, you should do it before creating any
    pages that belong to the profile.

    The cache can be cleared of links by calling **clearVisitedLinks** () or
    **clearAllVisitedLinks** (). **PersistentCookiesPolicy**  describes whether
    session and persistent cookies are saved to and restored from memory or
    disk.

    Profiles can be used to isolate pages from each other. A typical use case is
    a dedicated **off-the-record profile** for a **private browsing** mode.
    Using QWebEngineProfile() without defining a storage name constructs a new
    off-the-record profile that leaves no record on the local machine, and has
    no persistent data or cache. The **isOffTheRecord** () method can be used to
    check whether a profile is off-the-record.

    The default profile can be accessed by **defaultProfile** (). It is a built-
    in profile that all web pages not specifically created with another profile
    belong to.

    Implementing the **QWebEngineUrlRequestInterceptor**  interface and
    registering the interceptor on a profile by **setUrlRequestInterceptor** ()
    enables intercepting, blocking, and modifying URL requests
    (**QWebEngineUrlRequestInfo** ) before they reach the networking stack of
    Chromium.

    A **QWebEngineUrlSchemeHandler**  can be registered for a profile by
    **installUrlSchemeHandler** () to add support for custom URL schemes.
    Requests for the scheme are then issued to
    **QWebEngineUrlSchemeHandler::requestStarted** () as
    **QWebEngineUrlRequestJob**  objects.

    Spellchecking HTML form fields can be enabled per profile by using the
    **setSpellCheckEnabled** () method and the current languages used for
    spellchecking can be set by using the **setSpellCheckLanguages** () method.
    """

    MemoryHttpCache: QWebEngineProfile.HttpCacheType = ...
    DiskHttpCache: QWebEngineProfile.HttpCacheType = ...
    NoCache: QWebEngineProfile.HttpCacheType = ...
    NoPersistentCookies: QWebEngineProfile.PersistentCookiesPolicy = ...
    AllowPersistentCookies: QWebEngineProfile.PersistentCookiesPolicy = ...
    ForcePersistentCookies: QWebEngineProfile.PersistentCookiesPolicy = ...

    class HttpCacheType(IntFlag):
        MemoryHttpCache: QWebEngineProfile.HttpCacheType = ...
        DiskHttpCache: QWebEngineProfile.HttpCacheType = ...
        NoCache: QWebEngineProfile.HttpCacheType = ...

    class PersistentCookiesPolicy(IntFlag):
        NoPersistentCookies: QWebEngineProfile.PersistentCookiesPolicy = ...
        AllowPersistentCookies: QWebEngineProfile.PersistentCookiesPolicy = ...
        ForcePersistentCookies: QWebEngineProfile.PersistentCookiesPolicy = ...
    @overload
    def __init__(self, name: str, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#QWebEngineProfile

        **QWebEngineProfile::QWebEngineProfile(QObject * parent = nullptr)**

        Constructs a new off-the-record profile with the parent **parent**.

        An off-the-record profile leaves no record on the local machine, and has
        no persistent data or cache. Thus, the HTTP cache can only be in memory
        and the cookies can only be non-persistent. Trying to change these
        settings will have no effect.

        **See also** **isOffTheRecord** ().
        """
        ...
    @overload
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#QWebEngineProfile-1

        **QWebEngineProfile::QWebEngineProfile(const QString & storageName ,
        QObject * parent = nullptr)**

        Constructs a new profile with the storage name **storageName** and
        parent **parent**.

        The storage name must be unique.

        A disk-based QWebEngineProfile should be destroyed on or before
        application exit, otherwise the cache and persistent data may not be
        fully flushed to disk.

        **See also** **storageName** ().
        """
        ...
    def cachePath(self) -> str:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#cachePath

        **QString QWebEngineProfile::cachePath() const**

        Returns the path used for caches.

        By default, this is below StandardPaths::CacheLocation in a
        QtWebengine/StorageName specific subdirectory.

        **Note:** Use **QStandardPaths::writableLocation**
        (**QStandardPaths::CacheLocation** ) to obtain the
        **QStandardPaths::CacheLocation**  path.

        **See also** **setCachePath** (), **storageName** (), and
        **QStandardPaths::writableLocation** ().
        """
        ...
    def clearAllVisitedLinks(self) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#clearAllVisitedLinks

        **void QWebEngineProfile::clearAllVisitedLinks()**

        Clears all links from the visited links database.

        **See also** **clearVisitedLinks** ().
        """
        ...
    def clearHttpCache(self) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#clearHttpCache

        **[since 5.7] void QWebEngineProfile::clearHttpCache()**

        Removes the profile's cache entries.

        This function was introduced in Qt 5.7.
        """
        ...
    def clearVisitedLinks(self, urls: Sequence[PySide6.QtCore.QUrl]) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#clearVisitedLinks

        **void QWebEngineProfile::clearVisitedLinks(const QList<QUrl> & urls )**

        Clears the links in **urls** from the visited links database.

        **See also** **clearAllVisitedLinks** ().
        """
        ...
    def cookieStore(self) -> PySide6.QtWebEngineCore.QWebEngineCookieStore:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#cookieStore

        **[since 5.6] QWebEngineCookieStore *QWebEngineProfile::cookieStore()**

        Returns the cookie store for this profile.

        This function was introduced in Qt 5.6.
        """
        ...
    @staticmethod
    def defaultProfile() -> PySide6.QtWebEngineCore.QWebEngineProfile:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#defaultProfile

        **[static] QWebEngineProfile *QWebEngineProfile::defaultProfile()**

        Returns the default profile.

        The default profile is off-the-record.

        **See also** **storageName** ().
        """
        ...
    def downloadPath(self) -> str:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#downloadPath

        **[since 5.13] QString QWebEngineProfile::downloadPath() const**

        The path to the location where the downloaded files are stored.

        **Note:** By default, the download path is
        **QStandardPaths::DownloadLocation** .

        This function was introduced in Qt 5.13.

        **See also** **setDownloadPath** () and
        **QStandardPaths::writableLocation** ().
        """
        ...
    def httpAcceptLanguage(self) -> str:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#httpAcceptLanguage

        **[since 5.6] QString QWebEngineProfile::httpAcceptLanguage() const**

        Returns the value of the Accept-Language HTTP request-header field.

        This function was introduced in Qt 5.6.

        **See also** **setHttpAcceptLanguage** ().
        """
        ...
    def httpCacheMaximumSize(self) -> int:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#httpCacheMaximumSize

        **int QWebEngineProfile::httpCacheMaximumSize() const**

        Returns the maximum size of the HTTP cache in bytes.

        Will return `0` if the size is automatically controlled by
        **QtWebEngine** .

        **See also** **setHttpCacheMaximumSize** () and **httpCacheType** ().
        """
        ...
    def httpCacheType(self) -> PySide6.QtWebEngineCore.QWebEngineProfile.HttpCacheType:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#httpCacheType

        **QWebEngineProfile::HttpCacheType QWebEngineProfile::httpCacheType()
        const**

        Returns the type of HTTP cache used.

        If the profile is off-the-record, **MemoryHttpCache**  is returned.

        **See also** **setHttpCacheType** () and **cachePath** ().
        """
        ...
    def httpUserAgent(self) -> str:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#httpUserAgent

        **QString QWebEngineProfile::httpUserAgent() const**

        Returns the user-agent string sent with HTTP to identify the browser.

        **Note:** On Windows 8.1 and newer, the default user agent will always
        report "Windows NT 6.2" (Windows 8), unless the application does contain
        a manifest that declares newer Windows versions as supported.

        **See also** **setHttpUserAgent** ().
        """
        ...
    def installUrlSchemeHandler(
        self,
        scheme: PySide6.QtCore.QByteArray | bytes,
        arg__2: PySide6.QtWebEngineCore.QWebEngineUrlSchemeHandler,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#installUrlSchemeHandler

        **[since 5.6] void QWebEngineProfile::installUrlSchemeHandler(const
        QByteArray & scheme , QWebEngineUrlSchemeHandler * handler )**

        Registers a handler **handler** for custom URL scheme **scheme** in the
        profile.

        It is necessary to first register the scheme with
        **QWebEngineUrlScheme::registerScheme**  at application startup.

        This function was introduced in Qt 5.6.
        """
        ...
    def isOffTheRecord(self) -> bool:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#isOffTheRecord

        **bool QWebEngineProfile::isOffTheRecord() const**

        Returns `true` if this is an off-the-record profile that leaves no
        record on the computer.

        This will force cookies and HTTP cache to be in memory, but also force
        all other normally persistent data to be stored in memory.
        """
        ...
    def isSpellCheckEnabled(self) -> bool:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#isSpellCheckEnabled

        **[since 5.8] bool QWebEngineProfile::isSpellCheckEnabled() const**

        Returns `true` if the spell checker is enabled; otherwise returns
        `false`.

        This function was introduced in Qt 5.8.

        **See also** **setSpellCheckEnabled** ().
        """
        ...
    def persistentCookiesPolicy(
        self,
    ) -> PySide6.QtWebEngineCore.QWebEngineProfile.PersistentCookiesPolicy:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#persistentCookiesPolicy

        **QWebEngineProfile::PersistentCookiesPolicy
        QWebEngineProfile::persistentCookiesPolicy() const**

        Returns the current policy for persistent cookies.

        If the profile is off-the-record, **NoPersistentCookies**  is returned.

        **See also** **setPersistentCookiesPolicy** ().
        """
        ...
    def persistentStoragePath(self) -> str:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#persistentStoragePath

        **QString QWebEngineProfile::persistentStoragePath() const**

        Returns the path used to store persistent data for the browser and web
        content.

        Persistent data includes persistent cookies, HTML5 local storage, and
        visited links.

        By default, this is below QStandardPaths::DataLocation in a
        QtWebengine/StorageName specific subdirectory.

        **Note:** Use **QStandardPaths::writableLocation**
        (QStandardPaths::DataLocation) to obtain the
        QStandardPaths::DataLocation path.

        **See also** **setPersistentStoragePath** (), **storageName** (), and
        **QStandardPaths::writableLocation** ().
        """
        ...
    def removeAllUrlSchemeHandlers(self) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#removeAllUrlSchemeHandlers

        **[since 5.6] void QWebEngineProfile::removeAllUrlSchemeHandlers()**

        Removes all custom URL scheme handlers installed in the profile.

        This function was introduced in Qt 5.6.
        """
        ...
    def removeUrlScheme(self, scheme: PySide6.QtCore.QByteArray | bytes) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#removeUrlScheme

        **[since 5.6] void QWebEngineProfile::removeUrlScheme(const QByteArray &
        scheme )**

        Removes the custom URL scheme **scheme** from the profile.

        This function was introduced in Qt 5.6.

        **See also** **removeUrlSchemeHandler** ().
        """
        ...
    def removeUrlSchemeHandler(
        self, arg__1: PySide6.QtWebEngineCore.QWebEngineUrlSchemeHandler
    ) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#removeUrlSchemeHandler

        **[since 5.6] void
        QWebEngineProfile::removeUrlSchemeHandler(QWebEngineUrlSchemeHandler *
        handler )**

        Removes the custom URL scheme handler **handler** from the profile.

        This function was introduced in Qt 5.6.

        **See also** **removeUrlScheme** ().
        """
        ...
    def scripts(self) -> PySide6.QtWebEngineCore.QWebEngineScriptCollection:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#scripts

        **QWebEngineScriptCollection *QWebEngineProfile::scripts() const**

        Returns the collection of scripts that are injected into all pages that
        share this profile.

        **See also** **QWebEngineScriptCollection** , **QWebEngineScript** ,
        **QWebEnginePage::scripts** (), and **Script Injection** .
        """
        ...
    def setCachePath(self, path: str) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#setCachePath

        **void QWebEngineProfile::setCachePath(const QString & path )**

        Overrides the default path used for disk caches, setting it to **path**.

        If set to the null string, the default path is restored.

        **See also** **cachePath** ().
        """
        ...
    def setDownloadPath(self, path: str) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#setDownloadPath

        **[since 5.13] void QWebEngineProfile::setDownloadPath(const QString &
        path )**

        Overrides the default path used for download location, setting it to
        **path**.

        If set to the null string, the default path is restored.

        This function was introduced in Qt 5.13.

        **See also** **downloadPath** ().
        """
        ...
    def setHttpAcceptLanguage(self, httpAcceptLanguage: str) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#setHttpAcceptLanguage

        **[since 5.6] void QWebEngineProfile::setHttpAcceptLanguage(const
        QString & httpAcceptLanguage )**

        Sets the value of the Accept-Language HTTP request-header field to
        **httpAcceptLanguage**.

        This function was introduced in Qt 5.6.

        **See also** **httpAcceptLanguage** ().
        """
        ...
    def setHttpCacheMaximumSize(self, maxSize: int) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#setHttpCacheMaximumSize

        **void QWebEngineProfile::setHttpCacheMaximumSize(int maxSize )**

        Sets the maximum size of the HTTP cache to **maxSize** bytes.

        Setting it to `0` means the size will be controlled automatically by
        **QtWebEngine** .

        **See also** **httpCacheMaximumSize** () and **setHttpCacheType** ().
        """
        ...
    def setHttpCacheType(
        self, arg__1: PySide6.QtWebEngineCore.QWebEngineProfile.HttpCacheType
    ) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#setHttpCacheType

        **void
        QWebEngineProfile::setHttpCacheType(QWebEngineProfile::HttpCacheType
        httpCacheType )**

        Sets the HTTP cache type to **httpCacheType**.

        **See also** **httpCacheType** () and **setCachePath** ().
        """
        ...
    def setHttpUserAgent(self, userAgent: str) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#setHttpUserAgent

        **void QWebEngineProfile::setHttpUserAgent(const QString & userAgent )**

        Overrides the default user-agent string, setting it to **userAgent**.

        **See also** **httpUserAgent** ().
        """
        ...
    def setPersistentCookiesPolicy(
        self, arg__1: PySide6.QtWebEngineCore.QWebEngineProfile.PersistentCookiesPolicy
    ) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#setPersistentCookiesPolicy

        **void QWebEngineProfile::setPersistentCookiesPolicy(QWebEngineProfile::
        PersistentCookiesPolicy newPersistentCookiesPolicy )**

        Sets the policy for persistent cookies to
        **newPersistentCookiesPolicy**.

        **See also** **persistentCookiesPolicy** ().
        """
        ...
    def setPersistentStoragePath(self, path: str) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#setPersistentStoragePath

        **void QWebEngineProfile::setPersistentStoragePath(const QString & path
        )**

        Overrides the default path used to store persistent web engine data.

        If **path** is set to the null string, the default path is restored.

        **See also** **persistentStoragePath** ().
        """
        ...
    def setSpellCheckEnabled(self, enabled: bool) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#setSpellCheckEnabled

        **[since 5.8] void QWebEngineProfile::setSpellCheckEnabled(bool enable
        )**

        Enables spell checker if **enable** is `true`, otherwise disables it.

        This function was introduced in Qt 5.8.

        **See also** **isSpellCheckEnabled** ().
        """
        ...
    def setSpellCheckLanguages(self, languages: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#setSpellCheckLanguages

        **[since 5.8] void QWebEngineProfile::setSpellCheckLanguages(const
        QStringList & languages )**

        Sets the current list of **languages** for the spell checker. Each
        language should match the name of the `.bdic` dictionary. For example,
        the language `en-US` will load the `en-US.bdic` dictionary file.

        See the **Spellchecker feature documentation**  for how dictionary files
        are searched.

        For more information about how to compile `.bdic` dictionaries, see the
        **Spellchecker Example** .

        This function was introduced in Qt 5.8.

        **See also** **spellCheckLanguages** ().
        """
        ...
    def setUrlRequestInterceptor(
        self, interceptor: PySide6.QtWebEngineCore.QWebEngineUrlRequestInterceptor
    ) -> None:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#setUrlRequestInterceptor

        **[since 5.13] void QWebEngineProfile::setUrlRequestInterceptor(QWebEngi
        neUrlRequestInterceptor * interceptor )**

        Registers a request interceptor singleton **interceptor** to intercept
        URL requests.

        The profile does not take ownership of the pointer.

        This function was introduced in Qt 5.13.

        **See also** **QWebEngineUrlRequestInfo**  and
        **QWebEngineUrlRequestInterceptor** .
        """
        ...
    def settings(self) -> PySide6.QtWebEngineCore.QWebEngineSettings:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#settings

        **QWebEngineSettings *QWebEngineProfile::settings() const**

        Returns the default settings for all pages in this profile.
        """
        ...
    def spellCheckLanguages(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#spellCheckLanguages

        **[since 5.8] QStringList QWebEngineProfile::spellCheckLanguages()
        const**

        Returns the list of languages used by the spell checker.

        This function was introduced in Qt 5.8.

        **See also** **setSpellCheckLanguages** ().
        """
        ...
    def storageName(self) -> str:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#storageName

        **QString QWebEngineProfile::storageName() const**

        Returns the storage name for the profile.

        The storage name is used to give each profile that uses the disk
        separate subdirectories for persistent data and cache.
        """
        ...
    def urlSchemeHandler(
        self, arg__1: PySide6.QtCore.QByteArray | bytes
    ) -> PySide6.QtWebEngineCore.QWebEngineUrlSchemeHandler:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#urlSchemeHandler

        **[since 5.6] const QWebEngineUrlSchemeHandler
        *QWebEngineProfile::urlSchemeHandler(const QByteArray & scheme ) const**

        Returns the custom URL scheme handler register for the URL scheme
        **scheme**.

        This function was introduced in Qt 5.6.
        """
        ...
    def visitedLinksContainsUrl(self, url: PySide6.QtCore.QUrl | str) -> bool:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#visitedLinksContainsUrl

        **bool QWebEngineProfile::visitedLinksContainsUrl(const QUrl & url )
        const**

        Returns `true` if **url** is considered a visited link by this profile.
        """
        ...
    @property
    def downloadRequested(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qwebengineprofile.html#downloadRequested

        **[signal, since 5.5] void
        QWebEngineProfile::downloadRequested(QWebEngineDownloadRequest *
        download )**

        This signal is emitted whenever a download has been triggered. The
        **download** argument holds the state of the download. The download has
        to be explicitly accepted with **QWebEngineDownloadRequest::accept** ()
        or it will be cancelled by default. The download item is parented by the
        profile. If it is not accepted, it will be deleted immediately after the
        signal emission. This signal cannot be used with a queued connection.

        This function was introduced in Qt 5.5.

        **See also** **QWebEngineDownloadRequest**  and
        **QWebEnginePage::download** ().
        """
        ...