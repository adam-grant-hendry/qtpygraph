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
PySide6.QtQuickControls2, except for defaults which are replaced by "...".
"""

from __future__ import annotations

class QQuickStyle:
    """
    https://doc.qt.io/qt-6/qquickstyle.html

    **Detailed Description**

    QQuickStyle provides API for querying and configuring the application
    **styles**  of Qt Quick Controls.

    #include <QGuiApplication>
        #include <QQmlApplicationEngine>
        #include
    <QQuickStyle>

        int main(int argc, char *argv[])
        {
    **QGuiApplication**  app(argc, argv);

            **QQuickStyle**
    ::setStyle("Material");

            **QQmlApplicationEngine**  engine;
    engine.load(**QUrl** ("qrc:/main.qml"));

            return app.exec();
    }

    **Note:** The style must be configured **before** loading QML that imports
    Qt Quick Controls. It is not possible to change the style after the QML
    types have been registered.

    **Note:** QQuickStyle is not supported when using **compile-time style
    selection** .

    To create your own custom style, see **Creating a Custom Style** . Custom
    styles do not need to implement all controls. By default, the styling system
    uses the **Basic style**  as a fallback for controls that a custom style
    does not provide. It is possible to specify a different fallback style to
    customize or extend one of the built-in styles.

    **QQuickStyle** ::setStyle("MyStyle");
        **QQuickStyle**
    ::setFallbackStyle("Material");

    **See also** **Styling Qt Quick Controls** .
    """

    def __init__(self) -> None: ...
    @staticmethod
    def name() -> str:
        """
        https://doc.qt.io/qt-6/qquickstyle.html#name

        **[static] QString QQuickStyle::name()**

        Returns the name of the application style.

        **Note:** The application style can be specified by passing a `-style`
        command line argument. Therefore `name()` may not return a fully
        resolved value if called before constructing a **QGuiApplication** .
        """
        ...
    @staticmethod
    def setFallbackStyle(style: str) -> None:
        """
        https://doc.qt.io/qt-6/qquickstyle.html#setFallbackStyle

        **[static, since 5.8] void QQuickStyle::setFallbackStyle(const QString &
        style )**

        Sets the application fallback style to **style**.

        **Note:** The fallback style must be the name of one of the built-in Qt
        Quick Controls styles, e.g. "Material".

        **Note:** The style must be configured **before** loading QML that
        imports Qt Quick Controls. It is not possible to change the style after
        the QML types have been registered.

        The fallback style can be also specified by setting the
        `QT_QUICK_CONTROLS_FALLBACK_STYLE` **environment variable** .

        This function was introduced in Qt 5.8.

        **See also** **setStyle** () and **Using Styles in Qt Quick Controls** .
        """
        ...
    @staticmethod
    def setStyle(style: str) -> None:
        """
        https://doc.qt.io/qt-6/qquickstyle.html#setStyle

        **[static] void QQuickStyle::setStyle(const QString & style )**

        Sets the application style to **style**.

        **Note:** The style must be configured **before** loading QML that
        imports Qt Quick Controls. It is not possible to change the style after
        the QML types have been registered.

        **See also** **setFallbackStyle** () and **Using Styles in Qt Quick
        Controls** .
        """
        ...