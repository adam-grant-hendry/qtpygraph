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
PySide6.QtNetwork, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtNetwork

class QNetworkInformation(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qnetworkinformation.html

    **Detailed Description**

    QNetworkInformation provides a cross-platform interface to network-related
    information through plugins.

    Various plugins can have various functionality supported, and so you can
    **load** () plugins based on which features are needed.

    QNetworkInformation is a singleton and stays alive from the first successful
    **load** () until destruction of the **QCoreApplication**  object. If you
    destroy and re-create the **QCoreApplication**  object you must call
    **load** () again.

    **See also** **QNetworkInformation::Feature** .
    """

    class Feature(IntFlag):
        Reachability: QNetworkInformation.Feature = ...
        CaptivePortal: QNetworkInformation.Feature = ...

    class Features: ...

    class Reachability(IntFlag):
        Unknown: QNetworkInformation.Reachability = ...
        Disconnected: QNetworkInformation.Reachability = ...
        Local: QNetworkInformation.Reachability = ...
        Site: QNetworkInformation.Reachability = ...
        Online: QNetworkInformation.Reachability = ...
    @staticmethod
    def availableBackends() -> list[str]:
        """
        https://doc.qt.io/qt-6/qnetworkinformation.html#availableBackends

        **[static] QStringList QNetworkInformation::availableBackends()**

        Returns a list of the names of all currently available backends.
        """
        ...
    def backendName(self) -> str:
        """
        https://doc.qt.io/qt-6/qnetworkinformation.html#backendName

        **QString QNetworkInformation::backendName() const**

        Returns the name of the currently loaded backend.
        """
        ...
    @staticmethod
    def instance() -> PySide6.QtNetwork.QNetworkInformation:
        """
        https://doc.qt.io/qt-6/qnetworkinformation.html#instance

        **[static] QNetworkInformation *QNetworkInformation::instance()**

        Returns a pointer to the instance of the **QNetworkInformation** , if
        any.

        **See also** **load** ().
        """
        ...
    def isBehindCaptivePortal(self) -> bool:
        """
        https://doc.qt.io/qt-6/qnetworkinformation.html#isBehindCaptivePortal-
        prop

        **[read-only, since 6.2] isBehindCaptivePortal : const bool**

        Lets you know if the user's device is behind a captive portal.

        This property indicates if the user's device is currently known to be
        behind a captive portal. This functionality relies on the operating
        system's detection of captive portals and is not supported on systems
        that don't report this. On systems where this is not supported this will
        always return `false`.

        This property was introduced in Qt 6.2.

        **Access functions:**

        bool **isBehindCaptivePortal** () const

        **Notifier signal:**

        void **isBehindCaptivePortalChanged** (bool **state** )
        """
        ...
    @overload
    @staticmethod
    def load(backend: str) -> bool:
        """
        https://doc.qt.io/qt-6/qnetworkinformation.html#load

        **[static] bool QNetworkInformation::load(QStringView backend )**

        Attempts to load a backend whose name matches **backend** (case
        insensitively).

        Returns `true` if it managed to load the requested backend or if it was
        already loaded. Returns `false` otherwise

        **See also** **instance** .
        """
        ...
    @overload
    @staticmethod
    def load(features: PySide6.QtNetwork.QNetworkInformation.Features) -> bool:
        """
        https://doc.qt.io/qt-6/qnetworkinformation.html#load-1

        **[static] bool QNetworkInformation::load(QNetworkInformation::Features
        features )**

        Load a backend which supports **features**.

        Returns `true` if it managed to load the requested backend or if it was
        already loaded. Returns `false` otherwise

        **See also** **instance** .
        """
        ...
    def reachability(self) -> PySide6.QtNetwork.QNetworkInformation.Reachability:
        """
        https://doc.qt.io/qt-6/qnetworkinformation.html#reachability-prop

        **[read-only] reachability : const Reachability**

        This property holds the current state of the system's network
        connectivity.

        Indicates the level of connectivity that can be expected. Do note that
        this is only based on what the plugin/operating system reports. In
        certain scenarios this is known to be wrong. For example, on Windows the
        'Online' check, by default, is performed by Windows connecting to a
        Microsoft-owned server. If this server is for any reason blocked then it
        will assume it does not have Online reachability. Because of this you
        should not use this as a pre-check before attempting to make a
        connection.

        **Access functions:**

        QNetworkInformation::Reachability **reachability** () const

        **Notifier signal:**

        void **reachabilityChanged** (QNetworkInformation::Reachability
        **newReachability** )

        **Member Function Documentation**
        """
        ...
    def supports(self, features: PySide6.QtNetwork.QNetworkInformation.Features) -> bool:
        """
        https://doc.qt.io/qt-6/qnetworkinformation.html#supports

        **bool QNetworkInformation::supports(QNetworkInformation::Features
        features ) const**

        Returns `true` if the currently loaded backend supports **features**.
        """
        ...
    @property
    def isBehindCaptivePortalChanged(self) -> PySide6.QtCore.SignalInstance: ...
    @property
    def reachabilityChanged(self) -> PySide6.QtCore.SignalInstance: ...
