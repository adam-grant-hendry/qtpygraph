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
PySide6.QtGui, except for defaults which are replaced by "...".
"""

from __future__ import annotations

import PySide6.QtCore
import PySide6.QtGui

class QDesktopServices:
    """
    https://doc.qt.io/qt-6/qdesktopservices.html

    **Detailed Description**

    Many desktop environments provide services that can be used by applications
    to perform common tasks, such as opening a web page, in a way that is both
    consistent and takes into account the user's application preferences.

    This class contains functions that provide simple interfaces to these
    services that indicate whether they succeeded or failed.

    The **openUrl** () function is used to open files located at arbitrary URLs
    in external applications. For URLs that correspond to resources on the local
    filing system (where the URL scheme is "file"), a suitable application will
    be used to open the file; otherwise, a web browser will be used to fetch and
    display the file.

    The user's desktop settings control whether certain executable file types
    are opened for browsing, or if they are executed instead. Some desktop
    environments are configured to prevent users from executing files obtained
    from non-local URLs, or to ask the user's permission before doing so.

    **URL Handlers**

    The behavior of the **openUrl** () function can be customized for individual
    URL schemes to allow applications to override the default handling behavior
    for certain types of URLs.

    The dispatch mechanism allows only one custom handler to be used for each
    URL scheme; this is set using the **setUrlHandler** () function. Each
    handler is implemented as a slot which accepts only a single **QUrl**
    argument.

    The existing handlers for each scheme can be removed with the
    **unsetUrlHandler** () function. This returns the handling behavior for the
    given scheme to the default behavior.

    This system makes it easy to implement a help system, for example. Help
    could be provided in labels and text browsers using
    **help://myapplication/mytopic** URLs, and by registering a handler it
    becomes possible to display the help text inside the application:

    class MyHelpHandler : public **QObject**
        {
            Q_OBJECT
        public:
    // ...
        public slots:
            void showHelp(const **QUrl**  &url);
        };
    **QDesktopServices** ::setUrlHandler("help", helpInstance, "showHelp");

    If inside the handler you decide that you can't open the requested URL, you
    can just call **QDesktopServices::openUrl** () again with the same argument,
    and it will try to open the URL using the appropriate mechanism for the
    user's desktop environment.

    Combined with platform specific settings, the schemes registered by the
    **openUrl** () function can also be exposed to other applications, opening
    up for application deep linking or a very basic URL-based IPC mechanism.

    **See also** **QSystemTrayIcon** , **QProcess** , and **QStandardPaths** .
    """

    def __init__(self) -> None: ...
    @staticmethod
    def openUrl(url: PySide6.QtCore.QUrl | str) -> bool:
        """
        https://doc.qt.io/qt-6/qdesktopservices.html#openUrl

        **[static] bool QDesktopServices::openUrl(const QUrl & url )**

        Opens the given **url** in the appropriate Web browser for the user's
        desktop environment, and returns `true` if successful; otherwise returns
        `false`.

        If the URL is a reference to a local file (i.e., the URL scheme is
        "file") then it will be opened with a suitable application instead of a
        Web browser.

        The following example opens a file on the Windows file system residing
        on a path that contains spaces:

        **QDesktopServices** ::openUrl(**QUrl** ("file:///C:/Documents and
        Settings/All Users/Desktop", **QUrl** ::TolerantMode));

        If a `mailto` URL is specified, the user's e-mail client will be used to
        open a composer window containing the options specified in the URL,
        similar to the way `mailto` links are handled by a Web browser.

        For example, the following URL contains a recipient (`user@foo.com`), a
        subject (`Test`), and a message body (`Just a test`):

        mailto:user@foo.com?subject=Test&body=Just a test

        **Warning:** Although many e-mail clients can send attachments and are
        Unicode-aware, the user may have configured their client without these
        features. Also, certain e-mail clients (e.g., Lotus Notes) have problems
        with long URLs.

        **Warning:** A return value of `true` indicates that the application has
        successfully requested the operating system to open the URL in an
        external application. The external application may still fail to launch
        or fail to open the requested URL. This result will not be reported back
        to the application.

        **Warning:** URLs passed to this function on iOS will not load unless
        their schemes are listed in the `LSApplicationQueriesSchemes` key of the
        application's Info.plist file. For more information, see the Apple
        Developer Documentation for **canOpenURL:** . For example, the following
        lines enable URLs with the HTTPS scheme:

        <key>LSApplicationQueriesSchemes</key>
            <array>
        <string>https</string>
            </array>

        **See also** **setUrlHandler** ().
        """
        ...
    @staticmethod
    def setUrlHandler(
        scheme: str, receiver: PySide6.QtCore.QObject, method: bytes
    ) -> None:
        """
        https://doc.qt.io/qt-6/qdesktopservices.html#setUrlHandler

        **[static] void QDesktopServices::setUrlHandler(const QString & scheme ,
        QObject * receiver , const char * method )**

        Sets the handler for the given **scheme** to be the handler **method**
        provided by the **receiver** object.

        This function provides a way to customize the behavior of **openUrl**
        (). If **openUrl** () is called with a URL with the specified **scheme**
        then the given **method** on the **receiver** object is called instead
        of **QDesktopServices**  launching an external application.

        The provided method must be implemented as a slot that only accepts a
        single **QUrl**  argument.

        class MyHelpHandler : public **QObject**
            {
                Q_OBJECT
        public:
                // ...
            public slots:
                void showHelp(const
        **QUrl**  &url);
            };

        If setUrlHandler() is used to set a new handler for a scheme which
        already has a handler, the existing handler is simply replaced with the
        new one. Since **QDesktopServices**  does not take ownership of
        handlers, no objects are deleted when a handler is replaced.

        Note that the handler will always be called from within the same thread
        that calls **QDesktopServices::openUrl** ().

        **iOS**

        To use this function for receiving data from other apps on iOS you also
        need to add the custom scheme to the `CFBundleURLSchemes` list in your
        Info.plist file:

        <key>CFBundleURLTypes</key>
            <array>
                <dict>
        <key>CFBundleURLSchemes</key>
                    <array>
        <string>myapp</string>
                    </array>
                </dict>
            </array>

        For more information, see the Apple Developer Documentation for
        **Defining a Custom URL Scheme for Your App** .

        **Warning:** It is not possible to claim support for some well known URL
        schemes, including http and https. This is only allowed for Universal
        Links.

        To claim support for http and https the above entry in the Info.plist
        file is not allowed. This is only possible when you add your domain to
        the Entitlements file:

        <key>com.apple.developer.associated-domains</key>
            <array>
        <string>applinks:your.domain.com</string>
            </array>

        iOS will search for /.well-known/apple-app-site-association on your
        domain, when the application is installed. If you want to listen to
        `https://your.domain.com/help?topic=ABCDEF` you need to provide the
        following content there:

        {
                "applinks": {
                    "apps": [],
                    "details":
        [{
                        "appIDs" : [ "ABCDE12345.com.example.app" ],
        "components": [{
                            "/": "/help",
        "?": { "topic": "?*"}
                        }]
                    }]
                }
            }

        For more information, see the Apple Developer Documentation for
        **Supporting Associated Domains** .

        **Android**

        To use this function for receiving data from other apps on Android, you
        need to add one or more intent filter to the `activity` in your app
        manifest:

        <intent-filter>
                <action
        android:name="android.intent.action.VIEW" />
                <category
        android:name="android.intent.category.DEFAULT" />
                <category
        android:name="android.intent.category.BROWSABLE" />
                <data
        android:scheme="https" android:host="your.domain.com"
        android:port="1337" android:path="/help"/>
            </intent-filter>

        For more information, see the Android Developer Documentation for
        **Create Deep Links to App Content** .

        To immediately open the corresponding content in your Android app,
        without requiring the user to select the app, you need to verify your
        link. To enable the verification, add an additional parameter to your
        intent filter:

        <intent-filter android:autoVerify="true">

        Android will look for `https://your.domain.com/.well-
        known/assetlinks.json`, when the application is installed. If you want
        to listen to `https://your.domain.com:1337/help`, you need to provide
        the following content there:

        [{
              "relation": ["delegate_permission/common.handle_all_urls"],
        "target": {
                "namespace": "android_app",
                "package_name":
        "com.example.app",
                "sha256_cert_fingerprints":
                ["14:6D:E
        9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83:42:E6:1D:BE:A8:8A:04:9
        6:B2:3F:CF:44:E5"]
              }
            }]

        For more information, see the Android Developer Documentation for
        **Verify Android App Links** .

        **See also** **openUrl** () and **unsetUrlHandler** ().
        """
        ...
    @staticmethod
    def unsetUrlHandler(scheme: str) -> None:
        """
        https://doc.qt.io/qt-6/qdesktopservices.html#unsetUrlHandler

        **[static] void QDesktopServices::unsetUrlHandler(const QString & scheme
        )**

        Removes a previously set URL handler for the specified **scheme**.

        **See also** **setUrlHandler** ().
        """
        ...
