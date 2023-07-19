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
PySide6.QtWidgets, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from typing import Any, overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QSplashScreen(PySide6.QtWidgets.QWidget):
    """
    https://doc.qt.io/qt-6/qsplashscreen.html

    **Detailed Description**

    A splash screen is a widget that is usually displayed when an application is
    being started. Splash screens are often used for applications that have long
    start up times (e.g. database or networking applications that take time to
    establish connections) to provide the user with feedback that the
    application is loading.

    The splash screen appears in the center of the screen. It may be useful to
    add the **Qt::WindowStaysOnTopHint**  to the splash widget's window flags if
    you want to keep it above all the other windows on the desktop.

    Some X11 window managers do not support the "stays on top" flag. A solution
    is to set up a timer that periodically calls **raise** () on the splash
    screen to simulate the "stays on top" effect.

    The most common usage is to show a splash screen before the main widget is
    displayed on the screen. This is illustrated in the following code snippet
    in which a splash screen is displayed and some initialization tasks are
    performed before the application's main window is shown:

    int main(int argc, char *argv[])
        {
            **QApplication**  app(argc,
    argv);
            **QPixmap**  pixmap(":/splash.png");
    **QSplashScreen**  splash(pixmap);
            splash.show();
    app.processEvents();
            ...
            **QMainWindow**  window;
    window.show();
            splash.finish(&window);
            return app.exec();
    }

    The user can hide the splash screen by clicking on it with the mouse. Since
    the splash screen is typically displayed before the event loop has started
    running, it is necessary to periodically call
    **QCoreApplication::processEvents** () to receive the mouse clicks.

    It is sometimes useful to update the splash screen with messages, for
    example, announcing connections established or modules loaded as the
    application starts up:

    **QPixmap**  pixmap(":/splash.png");
        **QSplashScreen**  *splash = new
    **QSplashScreen** (pixmap);
        splash->show();

        ... // Loading some
    items
        splash->showMessage("Loaded modules");
    **QCoreApplication** ::processEvents();

        ... // Establishing
    connections
        splash->showMessage("Established connections");
    **QCoreApplication** ::processEvents();

    QSplashScreen supports this with the **showMessage** () function. If you
    wish to do your own drawing you can get a pointer to the pixmap used in the
    splash screen with **pixmap** (). Alternatively, you can subclass
    QSplashScreen and reimplement **drawContents** ().

    In case of having multiple screens, it is also possible to show the splash
    screen on a different screen than the primary one. For example:

    **QScreen**  *screen = **QGuiApplication** ::screens().at(1);
    **QPixmap**  pixmap(":/splash.png");
        **QSplashScreen**  splash(screen,
    pixmap);
        splash.show();
    """

    @overload
    def __init__(
        self,
        pixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage | str = ...,
        f: PySide6.QtCore.Qt.WindowFlags = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsplashscreen.html#QSplashScreen

        **QSplashScreen::QSplashScreen(const QPixmap & pixmap = QPixmap(),
        Qt::WindowFlags f = Qt::WindowFlags())**

        Construct a splash screen that will display the **pixmap**.

        There should be no need to set the widget flags, **f** , except perhaps
        **Qt::WindowStaysOnTopHint** .
        """
        ...
    @overload
    def __init__(
        self,
        screen: PySide6.QtGui.QScreen,
        pixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage | str = ...,
        f: PySide6.QtCore.Qt.WindowFlags = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsplashscreen.html#QSplashScreen-1

        **[since 5.15] QSplashScreen::QSplashScreen(QScreen * screen , const
        QPixmap & pixmap = QPixmap(), Qt::WindowFlags f = Qt::WindowFlags())**

        This is an overloaded function.

        This function allows you to specify the screen for your splashscreen.
        The typical use for this constructor is if you have multiple screens and
        prefer to have the splash screen on a different screen than your primary
        one. In that case pass the proper **screen**.

        This function was introduced in Qt 5.15.
        """
        ...
    def clearMessage(self) -> None:
        """
        https://doc.qt.io/qt-6/qsplashscreen.html#clearMessage

        **[slot] void QSplashScreen::clearMessage()**

        Removes the message being displayed on the splash screen

        **See also** **showMessage** ().
        """
        ...
    def drawContents(self, painter: PySide6.QtGui.QPainter) -> None:
        """
        https://doc.qt.io/qt-6/qsplashscreen.html#drawContents

        **[virtual protected] void QSplashScreen::drawContents(QPainter *
        painter )**

        Draw the contents of the splash screen using painter **painter**. The
        default implementation draws the message passed by **showMessage** ().
        Reimplement this function if you want to do your own drawing on the
        splash screen.
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qsplashscreen.html#event

        **[override virtual protected] bool QSplashScreen::event(QEvent * e )**

        Reimplements: **QWidget::event** (QEvent *event).
        """
        ...
    def finish(self, w: PySide6.QtWidgets.QWidget) -> None:
        """
        https://doc.qt.io/qt-6/qsplashscreen.html#finish

        **void QSplashScreen::finish(QWidget * mainWin )**

        Makes the splash screen wait until the widget **mainWin** is displayed
        before calling **close** () on itself.
        """
        ...
    def message(self) -> str:
        """
        https://doc.qt.io/qt-6/qsplashscreen.html#message

        **[since 5.2] QString QSplashScreen::message() const**

        Returns the message that is currently displayed on the splash screen.

        This function was introduced in Qt 5.2.

        **See also** **showMessage** () and **clearMessage** ().
        """
        ...
    def mousePressEvent(self, arg__1: PySide6.QtGui.QMouseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qsplashscreen.html#mousePressEvent

        **[override virtual protected] void
        QSplashScreen::mousePressEvent(QMouseEvent *)**

        Reimplements: **QWidget::mousePressEvent** (QMouseEvent *event).
        """
        ...
    def pixmap(self) -> PySide6.QtGui.QPixmap:
        """
        https://doc.qt.io/qt-6/qsplashscreen.html#pixmap

        **const QPixmap QSplashScreen::pixmap() const**

        Returns the pixmap that is used in the splash screen. The image does not
        have any of the text drawn by **showMessage** () calls.

        **See also** **setPixmap** ().
        """
        ...
    def setPixmap(
        self, pixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage | str
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsplashscreen.html#setPixmap

        **void QSplashScreen::setPixmap(const QPixmap & pixmap )**

        Sets the pixmap that will be used as the splash screen's image to
        **pixmap**.

        **See also** **pixmap** ().
        """
        ...
    def showMessage(
        self,
        message: str,
        alignment: int = ...,
        color: (
            PySide6.QtGui.QColor
            | PySide6.QtGui.QRgba64
            | Any
            | PySide6.QtCore.Qt.GlobalColor
            | str
            | int
        ) = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qsplashscreen.html#showMessage

        **[slot] void QSplashScreen::showMessage(const QString & message , int
        alignment = Qt::AlignLeft, const QColor & color = Qt::black)**

        Draws the **message** text onto the splash screen with color **color**
        and aligns the text according to the flags in **alignment**. This
        function calls **repaint** () to make sure the splash screen is
        repainted immediately. As a result the message is kept up to date with
        what your application is doing (e.g. loading files).

        **See also** **Qt::Alignment** , **clearMessage** (), and **message**
        ().
        """
        ...
    @property
    def messageChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qsplashscreen.html#messageChanged

        **[signal] void QSplashScreen::messageChanged(const QString & message
        )**

        This signal is emitted when the message on the splash screen changes.
        **message** is the new message and is a null-string when the message has
        been removed.

        **See also** **showMessage** () and **clearMessage** ().
        """
        ...