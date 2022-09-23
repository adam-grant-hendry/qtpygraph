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

import os
from collections.abc import Sequence
from enum import IntFlag
from typing import overload

import PySide6.QtCore
import PySide6.QtGui

class QIcon:
    """
    https://doc.qt.io/qt-6/qicon.html

    **Detailed Description**

    A QIcon can generate smaller, larger, active, and disabled pixmaps from the
    set of pixmaps it is given. Such pixmaps are used by Qt widgets to show an
    icon representing a particular action.

    The simplest use of QIcon is to create one from a **QPixmap**  file or
    resource, and then use it, allowing Qt to work out all the required icon
    styles and sizes. For example:

    **QToolButton**  *button = new **QToolButton** ;
    button->setIcon(**QIcon** ("open.xpm"));

    To undo a QIcon, simply set a null icon in its place:

    button->setIcon(**QIcon** ());

    Use the **QImageReader::supportedImageFormats** () and
    **QImageWriter::supportedImageFormats** () functions to retrieve a complete
    list of the supported file formats.

    When you retrieve a pixmap using pixmap(**QSize** , Mode, State), and no
    pixmap for this given size, mode and state has been added with **addFile**
    () or **addPixmap** (), then QIcon will generate one on the fly. This pixmap
    generation happens in a **QIconEngine** . The default engine scales pixmaps
    down if required, but never up, and it uses the current style to calculate a
    disabled appearance. By using custom icon engines, you can customize every
    aspect of generated icons. With **QIconEnginePlugin**  it is possible to
    register different icon engines for different file suffixes, making it
    possible for third parties to provide additional icon engines to those
    included with Qt.

    **Note:** Since Qt 4.2, an icon engine that supports SVG is included.

    **Making Classes that Use QIcon**

    If you write your own widgets that have an option to set a small pixmap,
    consider allowing a QIcon to be set for that pixmap. The Qt class
    **QToolButton**  is an example of such a widget.

    Provide a method to set a QIcon, and when you draw the icon, choose
    whichever pixmap is appropriate for the current state of your widget. For
    example:

    void MyWidget::drawIcon(**QPainter**  *painter, **QPoint**  pos)
        {
    **QPixmap**  pixmap = icon.pixmap(**QSize** (22, 22),
    isEnabled() ? **QIcon** ::Normal
    : **QIcon** ::Disabled,
                                           isChecked() ?
    **QIcon** ::On
                                                       :
    **QIcon** ::Off);
            painter->drawPixmap(pos, pixmap);
        }

    You might also make use of the `Active` mode, perhaps making your widget
    `Active` when the mouse is over the widget (see **QWidget::enterEvent** ()),
    while the mouse is pressed pending the release that will activate the
    function, or when it is the currently selected item. If the widget can be
    toggled, the "On" mode might be used to draw a different icon.

    ![QIcon](images/icon.png)

    **Note:** QIcon needs a **QGuiApplication**  instance before the icon is
    created.

    **High DPI Icons**

    There are two ways that QIcon supports **high DPI**  icons: via **addFile**
    () and **fromTheme** ().

    **addFile** () is useful if you have your own custom directory structure and
    do not need to use the **freedesktop.org Icon Theme Specification** . Icons
    created via this approach use Qt's **"@nx" high DPI syntax** .

    Using **fromTheme** () is necessary if you plan on following the Icon Theme
    Specification. To make QIcon use the high DPI version of an image, add an
    additional entry to the appropriate `index.theme` file:

    [Icon Theme]
        Name=Test
        Comment=Test Theme
    Directories=32x32/actions,32x32@2/actions

        [32x32/actions]
    Size=32
        Context=Actions
        Type=Fixed

        # High DPI version of
    the entry above.
        [32x32@2/actions]
        Size=32
        Scale=2
    Type=Fixed

    Your icon theme directory would then look something like this:

    ├── 32x32
        │   └── actions
        │       └── appointment-new.png
        ├──
    32x32@2
        │   └── actions
        │       └── appointment-new.png
        └──
    index.theme

    **See also** **GUI Design Handbook: Iconic Label**  and **Icons Example** .
    """

    Normal: QIcon.Mode = ...
    Disabled: QIcon.Mode = ...
    Active: QIcon.Mode = ...
    Selected: QIcon.Mode = ...
    On: QIcon.State = ...
    Off: QIcon.State = ...

    class Mode(IntFlag):
        Normal: QIcon.Mode = ...
        Disabled: QIcon.Mode = ...
        Active: QIcon.Mode = ...
        Selected: QIcon.Mode = ...

    class State(IntFlag):
        On: QIcon.State = ...
        Off: QIcon.State = ...
    @overload
    def __init__(self) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#QIcon

        **QIcon::QIcon()**

        Constructs a null icon.
        """
        ...
    @overload
    def __init__(self, engine: PySide6.QtGui.QIconEngine) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#QIcon-1

        **QIcon::QIcon(const QPixmap & pixmap )**

        Constructs an icon from a **pixmap**.
        """
        ...
    @overload
    def __init__(self, fileName: str) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#QIcon-2

        **QIcon::QIcon(const QIcon & other )**

        Constructs a copy of **other**. This is very fast.
        """
        ...
    @overload
    def __init__(self, other: PySide6.QtGui.QIcon | PySide6.QtGui.QPixmap) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#QIcon-3

        **QIcon::QIcon(QIcon && other )**

        Move-constructs a QIcon instance, making it point to the same object
        that **other** was pointing to.
        """
        ...
    @overload
    def __init__(
        self, pixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage | str
    ) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#QIcon-4

        **QIcon::QIcon(const QString & fileName )**

        Constructs an icon from the file with the given **fileName**. The file
        will be loaded on demand.

        If **fileName** contains a relative path (e.g. the filename only) the
        relevant file must be found relative to the runtime working directory.

        The file name can refer to an actual file on disk or to one of the
        application's embedded resources. See the **Resource System**  overview
        for details on how to embed images and other resource files in the
        application's executable.

        Use the **QImageReader::supportedImageFormats** () and
        **QImageWriter::supportedImageFormats** () functions to retrieve a
        complete list of the supported file formats.
        """
        ...
    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(
        self, arg__1: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(
        self, arg__1: PySide6.QtCore.QDataStream
    ) -> PySide6.QtCore.QDataStream: ...
    @overload
    def actualSize(
        self,
        size: PySide6.QtCore.QSize,
        mode: PySide6.QtGui.QIcon.Mode = ...,
        state: PySide6.QtGui.QIcon.State = ...,
    ) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qicon.html#actualSize

        **QSize QIcon::actualSize(const QSize & size , QIcon::Mode mode =
        Normal, QIcon::State state = Off) const**

        Returns the actual size of the icon for the requested **size** ,
        **mode** , and **state**. The result might be smaller than requested,
        but never larger. The returned size is in device-independent pixels
        (This is relevant for high-dpi pixmaps.)

        **See also** **pixmap** () and **paint** ().
        """
        ...
    @overload
    def actualSize(
        self,
        window: PySide6.QtGui.QWindow,
        size: PySide6.QtCore.QSize,
        mode: PySide6.QtGui.QIcon.Mode = ...,
        state: PySide6.QtGui.QIcon.State = ...,
    ) -> PySide6.QtCore.QSize:
        """
        https://doc.qt.io/qt-6/qicon.html#actualSize

        **QSize QIcon::actualSize(const QSize & size , QIcon::Mode mode =
        Normal, QIcon::State state = Off) const**

        Returns the actual size of the icon for the requested **size** ,
        **mode** , and **state**. The result might be smaller than requested,
        but never larger. The returned size is in device-independent pixels
        (This is relevant for high-dpi pixmaps.)

        **See also** **pixmap** () and **paint** ().
        """
        ...
    def addFile(
        self,
        fileName: str,
        size: PySide6.QtCore.QSize = ...,
        mode: PySide6.QtGui.QIcon.Mode = ...,
        state: PySide6.QtGui.QIcon.State = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#addFile

        **void QIcon::addFile(const QString & fileName , const QSize & size =
        QSize(), QIcon::Mode mode = Normal, QIcon::State state = Off)**

        Adds an image from the file with the given **fileName** to the icon, as
        a specialization for **size** , **mode** and **state**. The file will be
        loaded on demand. Note: custom icon engines are free to ignore
        additionally added pixmaps.

        If **fileName** contains a relative path (e.g. the filename only) the
        relevant file must be found relative to the runtime working directory.

        The file name can refer to an actual file on disk or to one of the
        application's embedded resources. See the **Resource System**  overview
        for details on how to embed images and other resource files in the
        application's executable.

        Use the **QImageReader::supportedImageFormats** () and
        **QImageWriter::supportedImageFormats** () functions to retrieve a
        complete list of the supported file formats.

        If a high resolution version of the image exists (identified by the
        suffix `@2x` on the base name), it is automatically loaded and added
        with the **device pixel ratio** set to a value of 2. This can be
        disabled by setting the environment variable
        `QT_HIGHDPI_DISABLE_2X_IMAGE_LOADING` (see **QImageReader** ).

        **Note:** When you add a non-empty filename to a **QIcon** , the icon
        becomes non-null, even if the file doesn't exist or points to a corrupt
        file.

        **See also** **addPixmap** () and **QPixmap::devicePixelRatio** ().
        """
        ...
    @overload
    def addPixmap(self, path: str | bytes | os.PathLike) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#addPixmap

        **void QIcon::addPixmap(const QPixmap & pixmap , QIcon::Mode mode =
        Normal, QIcon::State state = Off)**

        Adds **pixmap** to the icon, as a specialization for **mode** and
        **state**.

        Custom icon engines are free to ignore additionally added pixmaps.

        **See also** **addFile** ().
        """
        ...
    @overload
    def addPixmap(
        self,
        pixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage | str,
        mode: PySide6.QtGui.QIcon.Mode = ...,
        state: PySide6.QtGui.QIcon.State = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#addPixmap

        **void QIcon::addPixmap(const QPixmap & pixmap , QIcon::Mode mode =
        Normal, QIcon::State state = Off)**

        Adds **pixmap** to the icon, as a specialization for **mode** and
        **state**.

        Custom icon engines are free to ignore additionally added pixmaps.

        **See also** **addFile** ().
        """
        ...
    def availableSizes(
        self,
        mode: PySide6.QtGui.QIcon.Mode = ...,
        state: PySide6.QtGui.QIcon.State = ...,
    ) -> list[PySide6.QtCore.QSize]:
        """
        https://doc.qt.io/qt-6/qicon.html#availableSizes

        **QList<QSize> QIcon::availableSizes(QIcon::Mode mode = Normal,
        QIcon::State state = Off) const**

        Returns a list of available icon sizes for the specified **mode** and
        **state**.
        """
        ...
    def cacheKey(self) -> int:
        """
        https://doc.qt.io/qt-6/qicon.html#cacheKey

        **qint64 QIcon::cacheKey() const**

        Returns a number that identifies the contents of this **QIcon**  object.
        Distinct **QIcon**  objects can have the same key if they refer to the
        same contents.

        The cacheKey() will change when the icon is altered via **addPixmap** ()
        or **addFile** ().

        Cache keys are mostly useful in conjunction with caching.

        **See also** **QPixmap::cacheKey** ().
        """
        ...
    @staticmethod
    def fallbackSearchPaths() -> list[str]:
        """
        https://doc.qt.io/qt-6/qicon.html#fallbackSearchPaths

        **[static, since 5.11] QStringList QIcon::fallbackSearchPaths()**

        Returns the fallback search paths for icons.

        The default value will depend on the platform.

        This function was introduced in Qt 5.11.

        **See also** **setFallbackSearchPaths** () and **themeSearchPaths** ().
        """
        ...
    @staticmethod
    def fallbackThemeName() -> str:
        """
        https://doc.qt.io/qt-6/qicon.html#fallbackThemeName

        **[static, since 5.12] QString QIcon::fallbackThemeName()**

        Returns the name of the fallback icon theme.

        On X11, if not set, the fallback icon theme depends on your desktop
        settings. On other platforms it is not set by default.

        This function was introduced in Qt 5.12.

        **See also** **setFallbackThemeName** () and **themeName** ().
        """
        ...
    @overload
    @staticmethod
    def fromTheme(name: str) -> PySide6.QtGui.QIcon:
        """
        https://doc.qt.io/qt-6/qicon.html#fromTheme

        **[static] QIcon QIcon::fromTheme(const QString & name )**

        Returns the **QIcon**  corresponding to **name** in the current icon
        theme.

        The latest version of the freedesktop icon specification and naming
        specification can be obtained here:

        * <http://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-
        latest.html>
          * <http://standards.freedesktop.org/icon-naming-
        spec/icon-naming-spec-latest.html>

        To fetch an icon from the current icon theme:

        **QIcon**  undoicon = **QIcon** ::fromTheme("edit-undo");

        **Note:** By default, only X11 will support themed icons. In order to
        use themed icons on Mac and Windows, you will have to bundle a compliant
        theme in one of your **themeSearchPaths** () and set the appropriate
        **themeName** ().

        **Note:** Qt will make use of GTK's icon-theme.cache if present to speed
        up the lookup. These caches can be generated using gtk-update-icon-
        cache: <https://developer.gnome.org/gtk3/stable/gtk-update-icon-
        cache.html>.

        **Note:** If an icon can't be found in the current theme, then it will
        be searched in **fallbackSearchPaths** () as an unthemed icon.

        **See also** **themeName** (), **setThemeName** (), **themeSearchPaths**
        (), and **fallbackSearchPaths** ().
        """
        ...
    @overload
    @staticmethod
    def fromTheme(
        name: str, fallback: PySide6.QtGui.QIcon | PySide6.QtGui.QPixmap
    ) -> PySide6.QtGui.QIcon:
        """
        https://doc.qt.io/qt-6/qicon.html#fromTheme-1

        **[static] QIcon QIcon::fromTheme(const QString & name , const QIcon &
        fallback )**

        This is an overloaded function.

        Returns the **QIcon**  corresponding to **name** in the current icon
        theme. If no such icon is found in the current theme **fallback** is
        returned instead.

        If you want to provide a guaranteed fallback for platforms that do not
        support theme icons, you can use the second argument:

        **QIcon**  undoicon = **QIcon** ::fromTheme("edit-undo", **QIcon**
        (":/undo.png"));
        """
        ...
    @staticmethod
    def hasThemeIcon(name: str) -> bool:
        """
        https://doc.qt.io/qt-6/qicon.html#hasThemeIcon

        **[static] bool QIcon::hasThemeIcon(const QString & name )**

        Returns `true` if there is an icon available for **name** in the current
        icon theme, otherwise returns `false`.

        **See also** **themeSearchPaths** (), **fromTheme** (), and
        **setThemeName** ().
        """
        ...
    def isMask(self) -> bool:
        """
        https://doc.qt.io/qt-6/qicon.html#isMask

        **[since 5.6] bool QIcon::isMask() const**

        Returns `true` if this icon has been marked as a mask image. Certain
        platforms render mask icons differently (for example, menu icons on
        macOS).

        This function was introduced in Qt 5.6.

        **See also** **setIsMask** ().
        """
        ...
    def isNull(self) -> bool:
        """
        https://doc.qt.io/qt-6/qicon.html#isNull

        **bool QIcon::isNull() const**

        Returns `true` if the icon is empty; otherwise returns `false`.

        An icon is empty if it has neither a pixmap nor a filename.

        Note: Even a non-null icon might not be able to create valid pixmaps,
        eg. if the file does not exist or cannot be read.
        """
        ...
    def name(self) -> str:
        """
        https://doc.qt.io/qt-6/qicon.html#name

        **QString QIcon::name() const**

        Returns the name used to create the icon, if available.

        Depending on the way the icon was created, it may have an associated
        name. This is the case for icons created with **fromTheme** () or icons
        using a **QIconEngine**  which supports the QIconEngine::IconNameHook.

        **See also** **fromTheme** () and **QIconEngine** .
        """
        ...
    @overload
    def paint(
        self,
        painter: PySide6.QtGui.QPainter,
        rect: PySide6.QtCore.QRect,
        alignment: PySide6.QtCore.Qt.Alignment = ...,
        mode: PySide6.QtGui.QIcon.Mode = ...,
        state: PySide6.QtGui.QIcon.State = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#paint

        **void QIcon::paint(QPainter * painter , const QRect & rect ,
        Qt::Alignment alignment = Qt::AlignCenter, QIcon::Mode mode = Normal,
        QIcon::State state = Off) const**

        Uses the **painter** to paint the icon with specified **alignment** ,
        required **mode** , and **state** into the rectangle **rect**.

        **See also** **actualSize** () and **pixmap** ().
        """
        ...
    @overload
    def paint(
        self,
        painter: PySide6.QtGui.QPainter,
        x: int,
        y: int,
        w: int,
        h: int,
        alignment: PySide6.QtCore.Qt.Alignment = ...,
        mode: PySide6.QtGui.QIcon.Mode = ...,
        state: PySide6.QtGui.QIcon.State = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#paint-1

        **void QIcon::paint(QPainter * painter , int x , int y , int w , int h ,
        Qt::Alignment alignment = Qt::AlignCenter, QIcon::Mode mode = Normal,
        QIcon::State state = Off) const**

        This is an overloaded function.

        Paints the icon into the rectangle **QRect** ( **x** , **y** , **w** ,
        **h** ).
        """
        ...
    @overload
    def pixmap(
        self,
        extent: int,
        mode: PySide6.QtGui.QIcon.Mode = ...,
        state: PySide6.QtGui.QIcon.State = ...,
    ) -> PySide6.QtGui.QPixmap:
        """
        https://doc.qt.io/qt-6/qicon.html#pixmap

        **QPixmap QIcon::pixmap(const QSize & size , QIcon::Mode mode = Normal,
        QIcon::State state = Off) const**

        Returns a pixmap with the requested **size** , **mode** , and **state**
        , generating one if necessary. The pixmap might be smaller than
        requested, but never larger, unless the device-pixel ratio of the
        returned pixmap is larger than 1.

        **See also** **actualSize** () and **paint** ().
        """
        ...
    @overload
    def pixmap(
        self,
        size: PySide6.QtCore.QSize,
        devicePixelRatio: float,
        mode: PySide6.QtGui.QIcon.Mode = ...,
        state: PySide6.QtGui.QIcon.State = ...,
    ) -> PySide6.QtGui.QPixmap:
        """
        https://doc.qt.io/qt-6/qicon.html#pixmap-1

        **QPixmap QIcon::pixmap(int w , int h , QIcon::Mode mode = Normal,
        QIcon::State state = Off) const**

        This is an overloaded function.

        Returns a pixmap of size **QSize** ( **w** , **h** ). The pixmap might
        be smaller than requested, but never larger, unless the device-pixel
        ratio of the returned pixmap is larger than 1.
        """
        ...
    @overload
    def pixmap(
        self,
        size: PySide6.QtCore.QSize,
        mode: PySide6.QtGui.QIcon.Mode = ...,
        state: PySide6.QtGui.QIcon.State = ...,
    ) -> PySide6.QtGui.QPixmap:
        """
        https://doc.qt.io/qt-6/qicon.html#pixmap-2

        **QPixmap QIcon::pixmap(int extent , QIcon::Mode mode = Normal,
        QIcon::State state = Off) const**

        This is an overloaded function.

        Returns a pixmap of size **QSize** ( **extent** , **extent** ). The
        pixmap might be smaller than requested, but never larger, unless the
        device-pixel ratio of the returned pixmap is larger than 1.
        """
        ...
    @overload
    def pixmap(
        self,
        w: int,
        h: int,
        mode: PySide6.QtGui.QIcon.Mode = ...,
        state: PySide6.QtGui.QIcon.State = ...,
    ) -> PySide6.QtGui.QPixmap:
        """
        https://doc.qt.io/qt-6/qicon.html#pixmap-3

        **[since 6.0] QPixmap QIcon::pixmap(const QSize & size , qreal
        devicePixelRatio , QIcon::Mode mode = Normal, QIcon::State state = Off)
        const**

        This is an overloaded function.

        Returns a pixmap with the requested **size** , **devicePixelRatio** ,
        **mode** , and **state** , generating one if necessary.

        This function was introduced in Qt 6.0.

        **See also** **actualSize** () and **paint** ().
        """
        ...
    @overload
    def pixmap(
        self,
        window: PySide6.QtGui.QWindow,
        size: PySide6.QtCore.QSize,
        mode: PySide6.QtGui.QIcon.Mode = ...,
        state: PySide6.QtGui.QIcon.State = ...,
    ) -> PySide6.QtGui.QPixmap:
        """
        https://doc.qt.io/qt-6/qicon.html#pixmap

        **QPixmap QIcon::pixmap(const QSize & size , QIcon::Mode mode = Normal,
        QIcon::State state = Off) const**

        Returns a pixmap with the requested **size** , **mode** , and **state**
        , generating one if necessary. The pixmap might be smaller than
        requested, but never larger, unless the device-pixel ratio of the
        returned pixmap is larger than 1.

        **See also** **actualSize** () and **paint** ().
        """
        ...
    @staticmethod
    def setFallbackSearchPaths(paths: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#setFallbackSearchPaths

        **[static, since 5.11] void QIcon::setFallbackSearchPaths(const
        QStringList & paths )**

        Sets the fallback search paths for icons to **paths**.

        **Note:** To add some path without replacing existing ones:

        **QIcon** ::setFallbackSearchPaths(**QIcon** ::fallbackSearchPaths() <<
        "my/search/path");

        This function was introduced in Qt 5.11.

        **See also** **fallbackSearchPaths** () and **setThemeSearchPaths** ().
        """
        ...
    @staticmethod
    def setFallbackThemeName(name: str) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#setFallbackThemeName

        **[static, since 5.12] void QIcon::setFallbackThemeName(const QString &
        name )**

        Sets the fallback icon theme to **name**.

        The **name** should correspond to a directory name in the
        themeSearchPath() containing an index.theme file describing its
        contents.

        **Note:** This should be done before creating **QGuiApplication** , to
        ensure correct initialization.

        This function was introduced in Qt 5.12.

        **See also** **fallbackThemeName** (), **themeSearchPaths** (), and
        **themeName** ().
        """
        ...
    def setIsMask(self, isMask: bool) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#setIsMask

        **[since 5.6] void QIcon::setIsMask(bool isMask )**

        Indicate that this icon is a mask image(boolean **isMask** ), and hence
        can potentially be modified based on where it's displayed.

        This function was introduced in Qt 5.6.

        **See also** **isMask** ().
        """
        ...
    @staticmethod
    def setThemeName(path: str) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#setThemeName

        **[static] void QIcon::setThemeName(const QString & name )**

        Sets the current icon theme to **name**.

        The **name** should correspond to a directory name in the
        themeSearchPath() containing an index.theme file describing its
        contents.

        **See also** **themeSearchPaths** () and **themeName** ().
        """
        ...
    @staticmethod
    def setThemeSearchPaths(searchpath: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#setThemeSearchPaths

        **[static] void QIcon::setThemeSearchPaths(const QStringList & paths )**

        Sets the search paths for icon themes to **paths**.

        **See also** **themeSearchPaths** (), **fromTheme** (), and
        **setThemeName** ().
        """
        ...
    def swap(self, other: PySide6.QtGui.QIcon | PySide6.QtGui.QPixmap) -> None:
        """
        https://doc.qt.io/qt-6/qicon.html#swap

        **void QIcon::swap(QIcon & other )**

        Swaps icon **other** with this icon. This operation is very fast and
        never fails.
        """
        ...
    @staticmethod
    def themeName() -> str:
        """
        https://doc.qt.io/qt-6/qicon.html#themeName

        **[static] QString QIcon::themeName()**

        Returns the name of the current icon theme.

        On X11, the current icon theme depends on your desktop settings. On
        other platforms it is not set by default.

        **See also** **setThemeName** (), **themeSearchPaths** (), **fromTheme**
        (), and **hasThemeIcon** ().
        """
        ...
    @staticmethod
    def themeSearchPaths() -> list[str]:
        """
        https://doc.qt.io/qt-6/qicon.html#themeSearchPaths

        **[static] QStringList QIcon::themeSearchPaths()**

        Returns the search paths for icon themes.

        The default value will depend on the platform:

        On X11, the search path will use the XDG_DATA_DIRS environment variable
        if available.

        By default all platforms will have the resource directory `:\\icons` as a
        fallback. You can use "rcc -project" to generate a resource file from
        your icon theme.

        **See also** **setThemeSearchPaths** (), **fromTheme** (), and
        **setThemeName** ().
        """
        ...
