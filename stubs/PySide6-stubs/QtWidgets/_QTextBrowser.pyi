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

from collections.abc import Sequence
from typing import Any

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class QTextBrowser(PySide6.QtWidgets.QTextEdit):
    """
    https://doc.qt.io/qt-6/qtextbrowser.html

    **Detailed Description**

    This class extends **QTextEdit**  (in read-only mode), adding some
    navigation functionality so that users can follow links in hypertext
    documents.

    If you want to provide your users with an editable rich text editor, use
    **QTextEdit** . If you want a text browser without hypertext navigation use
    **QTextEdit** , and use **QTextEdit::setReadOnly** () to disable editing. If
    you just need to display a small piece of rich text use **QLabel** .

    **Document Source and Contents**

    The contents of **QTextEdit**  are set with **setHtml** () or
    **setPlainText** (), but QTextBrowser also implements the **setSource** ()
    function, making it possible to use a named document as the source text. The
    name is looked up in a list of search paths and in the directory of the
    current document factory.

    If a document name ends with an anchor (for example, "`#anchor"`), the text
    browser automatically scrolls to that position (using **scrollToAnchor**
    ()). When the user clicks on a hyperlink, the browser will call
    **setSource** () itself with the link's `href` value as argument. You can
    track the current source by connecting to the **sourceChanged** () signal.

    **Navigation**

    QTextBrowser provides **backward** () and **forward** () slots which you can
    use to implement Back and Forward buttons. The **home** () slot sets the
    text to the very first document displayed. The **anchorClicked** () signal
    is emitted when the user clicks an anchor. To override the default
    navigation behavior of the browser, call the **setSource** () function to
    supply new document text in a slot connected to this signal.

    If you want to load documents stored in the Qt resource system use `qrc` as
    the scheme in the URL to load. For example, for the document resource path
    `:/docs/index.html` use `qrc:/docs/index.html` as the URL with **setSource**
    ().

    **See also** **QTextEdit**  and **QTextDocument** .
    """

    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#QTextBrowser

        **QTextBrowser::QTextBrowser(QWidget * parent = nullptr)**

        Constructs an empty QTextBrowser with parent **parent**.
        """
        ...
    def backward(self) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#backward

        **[virtual slot] void QTextBrowser::backward()**

        Changes the document displayed to the previous document in the list of
        documents built by navigating links. Does nothing if there is no
        previous document.

        **See also** **forward** () and **backwardAvailable** ().
        """
        ...
    def backwardHistoryCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#backwardHistoryCount

        **int QTextBrowser::backwardHistoryCount() const**

        Returns the number of locations backward in the history.
        """
        ...
    def clearHistory(self) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#clearHistory

        **void QTextBrowser::clearHistory()**

        Clears the history of visited documents and disables the forward and
        backward navigation.

        **See also** **backward** () and **forward** ().
        """
        ...
    def doSetSource(
        self,
        name: PySide6.QtCore.QUrl | str,
        type: PySide6.QtGui.QTextDocument.ResourceType = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#doSetSource

        **[virtual protected] void QTextBrowser::doSetSource(const QUrl & url ,
        QTextDocument::ResourceType type = QTextDocument::UnknownResource)**

        Attempts to load the document at the given **url** with the specified
        **type**.

        **setSource** () calls doSetSource. In Qt 5, **setSource** (const
        **QUrl**  &url) was virtual. In Qt 6, doSetSource() is virtual instead,
        so that it can be overridden in subclasses.
        """
        ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#event

        **[override virtual protected] bool QTextBrowser::event(QEvent * e )**

        Reimplements: **QAbstractScrollArea::event** (QEvent *event).
        """
        ...
    def focusNextPrevChild(self, next: bool) -> bool:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#focusNextPrevChild

        **[override virtual protected] bool
        QTextBrowser::focusNextPrevChild(bool next )**

        Reimplements: **QTextEdit::focusNextPrevChild** (bool next).
        """
        ...
    def focusOutEvent(self, ev: PySide6.QtGui.QFocusEvent) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#focusOutEvent

        **[override virtual protected] void
        QTextBrowser::focusOutEvent(QFocusEvent * ev )**

        Reimplements: **QTextEdit::focusOutEvent** (QFocusEvent *e).
        """
        ...
    def forward(self) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#forward

        **[virtual slot] void QTextBrowser::forward()**

        Changes the document displayed to the next document in the list of
        documents built by navigating links. Does nothing if there is no next
        document.

        **See also** **backward** () and **forwardAvailable** ().
        """
        ...
    def forwardHistoryCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#forwardHistoryCount

        **int QTextBrowser::forwardHistoryCount() const**

        Returns the number of locations forward in the history.
        """
        ...
    def historyTitle(self, arg__1: int) -> str:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#historyTitle

        **QString QTextBrowser::historyTitle(int i ) const**

        Returns the **documentTitle** () of the HistoryItem.

        InputReturn
        **i** < 0**backward** () history
        **i** == 0current, see
        **QTextBrowser::source** ()
        **i** > 0**forward** () history

        backaction.setToolTip(browser.historyTitle(-1));
        forwardaction.setToolTip(browser.historyTitle(+1));
        """
        ...
    def historyUrl(self, arg__1: int) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#historyUrl

        **QUrl QTextBrowser::historyUrl(int i ) const**

        Returns the url of the HistoryItem.

        InputReturn
        **i** < 0**backward** () history
        **i** == 0current, see
        **QTextBrowser::source** ()
        **i** > 0**forward** () history
        """
        ...
    def home(self) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#home

        **[virtual slot] void QTextBrowser::home()**

        Changes the document displayed to be the first document from the
        history.
        """
        ...
    def isBackwardAvailable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#isBackwardAvailable

        **bool QTextBrowser::isBackwardAvailable() const**

        Returns `true` if the text browser can go backward in the document
        history using **backward** ().

        **See also** **backwardAvailable** () and **backward** ().
        """
        ...
    def isForwardAvailable(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#isForwardAvailable

        **bool QTextBrowser::isForwardAvailable() const**

        Returns `true` if the text browser can go forward in the document
        history using **forward** ().

        **See also** **forwardAvailable** () and **forward** ().
        """
        ...
    def keyPressEvent(self, ev: PySide6.QtGui.QKeyEvent) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#keyPressEvent

        **[override virtual protected] void
        QTextBrowser::keyPressEvent(QKeyEvent * ev )**

        Reimplements: **QTextEdit::keyPressEvent** (QKeyEvent *e).

        The event **ev** is used to provide the following keyboard shortcuts:

        KeypressAction
        Alt+Left Arrow**backward** ()
        Alt+Right
        Arrow**forward** ()
        Alt+Up Arrow**home** ()
        """
        ...
    def loadResource(self, type: int, name: PySide6.QtCore.QUrl | str) -> Any:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#loadResource

        **[override virtual] QVariant QTextBrowser::loadResource(int type ,
        const QUrl & name )**

        Reimplements: **QTextEdit::loadResource** (int type, const QUrl &name).

        This function is called when the document is loaded and for each image
        in the document. The **type** indicates the type of resource to be
        loaded. An invalid **QVariant**  is returned if the resource cannot be
        loaded.

        The default implementation ignores **type** and tries to locate the
        resources by interpreting **name** as a file name. If it is not an
        absolute path it tries to find the file in the paths of the
        **searchPaths**  property and in the same directory as the current
        source. On success, the result is a **QVariant**  that stores a
        **QByteArray**  with the contents of the file.

        If you reimplement this function, you can return other **QVariant**
        types. The table below shows which variant types are supported depending
        on the resource type:

        ResourceType**QMetaType::Type**
        **QTextDocument::HtmlResource**
        **QString**  or **QByteArray**
        **QTextDocument::ImageResource**
        **QImage** , **QPixmap**  or **QByteArray**
        **QTextDocument::StyleSheetResource** **QString**  or **QByteArray**
        **QTextDocument::MarkdownResource** **QString**  or **QByteArray**
        """
        ...
    def mouseMoveEvent(self, ev: PySide6.QtGui.QMouseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#mouseMoveEvent

        **[override virtual protected] void
        QTextBrowser::mouseMoveEvent(QMouseEvent * e )**

        Reimplements: **QTextEdit::mouseMoveEvent** (QMouseEvent *e).
        """
        ...
    def mousePressEvent(self, ev: PySide6.QtGui.QMouseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#mousePressEvent

        **[override virtual protected] void
        QTextBrowser::mousePressEvent(QMouseEvent * e )**

        Reimplements: **QTextEdit::mousePressEvent** (QMouseEvent *e).
        """
        ...
    def mouseReleaseEvent(self, ev: PySide6.QtGui.QMouseEvent) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#mouseReleaseEvent

        **[override virtual protected] void
        QTextBrowser::mouseReleaseEvent(QMouseEvent * e )**

        Reimplements: **QTextEdit::mouseReleaseEvent** (QMouseEvent *e).
        """
        ...
    def openExternalLinks(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#openExternalLinks-prop

        **openExternalLinks : bool**

        Specifies whether **QTextBrowser**  should automatically open links to
        external sources using **QDesktopServices::openUrl** () instead of
        emitting the **anchorClicked**  signal. Links are considered external if
        their scheme is neither file or qrc.

        The default value is false.

        **Access functions:**

        bool **openExternalLinks** () const
        void **setOpenExternalLinks**
        (bool **open** )
        """
        ...
    def openLinks(self) -> bool:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#openLinks-prop

        **openLinks : bool**

        This property specifies whether **QTextBrowser**  should automatically
        open links the user tries to activate by mouse or keyboard.

        Regardless of the value of this property the **anchorClicked**  signal
        is always emitted.

        The default value is true.

        **Access functions:**

        bool **openLinks** () const
        void **setOpenLinks** (bool **open** )
        """
        ...
    def paintEvent(self, e: PySide6.QtGui.QPaintEvent) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#paintEvent

        **[override virtual protected] void QTextBrowser::paintEvent(QPaintEvent
        * e )**

        Reimplements: **QTextEdit::paintEvent** (QPaintEvent *event).
        """
        ...
    def reload(self) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#reload

        **[virtual slot] void QTextBrowser::reload()**

        Reloads the current set source.
        """
        ...
    def searchPaths(self) -> list[str]:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#searchPaths-prop

        **searchPaths : QStringList**

        This property holds the search paths used by the text browser to find
        supporting content

        **QTextBrowser**  uses this list to locate images and documents.

        By default, this property contains an empty string list.

        **Access functions:**

        QStringList **searchPaths** () const
        void **setSearchPaths** (const
        QStringList & **paths** )
        """
        ...
    def setOpenExternalLinks(self, open: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#openExternalLinks-prop

        **openExternalLinks : bool**

        Specifies whether **QTextBrowser**  should automatically open links to
        external sources using **QDesktopServices::openUrl** () instead of
        emitting the **anchorClicked**  signal. Links are considered external if
        their scheme is neither file or qrc.

        The default value is false.

        **Access functions:**

        bool **openExternalLinks** () const
        void **setOpenExternalLinks**
        (bool **open** )
        """
        ...
    def setOpenLinks(self, open: bool) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#openLinks-prop

        **openLinks : bool**

        This property specifies whether **QTextBrowser**  should automatically
        open links the user tries to activate by mouse or keyboard.

        Regardless of the value of this property the **anchorClicked**  signal
        is always emitted.

        The default value is true.

        **Access functions:**

        bool **openLinks** () const
        void **setOpenLinks** (bool **open** )
        """
        ...
    def setSearchPaths(self, paths: Sequence[str]) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#searchPaths-prop

        **searchPaths : QStringList**

        This property holds the search paths used by the text browser to find
        supporting content

        **QTextBrowser**  uses this list to locate images and documents.

        By default, this property contains an empty string list.

        **Access functions:**

        QStringList **searchPaths** () const
        void **setSearchPaths** (const
        QStringList & **paths** )
        """
        ...
    def setSource(
        self,
        name: PySide6.QtCore.QUrl | str,
        type: PySide6.QtGui.QTextDocument.ResourceType = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#setSource

        **[slot] void QTextBrowser::setSource(const QUrl & url ,
        QTextDocument::ResourceType type = QTextDocument::UnknownResource)**

        Attempts to load the document at the given **url** with the specified
        **type**.

        If **type** is **UnknownResource**  (the default), the document type
        will be detected: that is, if the url ends with an extension of `.md`,
        `.mkd` or `.markdown`, the document will be loaded via
        **QTextDocument::setMarkdown** (); otherwise it will be loaded via
        **QTextDocument::setHtml** (). This detection can be bypassed by
        specifying the **type** explicitly.

        **Note:** Setter function for property **source** .

        **See also** **source** ().
        """
        ...
    def source(self) -> PySide6.QtCore.QUrl:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#source-prop

        **source : QUrl**

        This property holds the name of the displayed document.

        This is a an invalid url if no document is displayed or if the source is
        unknown.

        When setting this property **QTextBrowser**  tries to find a document
        with the specified name in the paths of the **searchPaths**  property
        and directory of the current source, unless the value is an absolute
        file path. It also checks for optional anchors and scrolls the document
        accordingly

        If the first tag in the document is `<qt type=detail>`, the document is
        displayed as a popup rather than as new document in the browser window
        itself. Otherwise, the document is displayed normally in the text
        browser with the text set to the contents of the named document with
        **QTextDocument::setHtml** () or **QTextDocument::setMarkdown** (),
        depending on whether the filename ends with any of the known Markdown
        file extensions.

        If you would like to avoid automatic type detection and specify the type
        explicitly, call **setSource** () rather than setting this property.

        By default, this property contains an empty URL.

        **Access functions:**

        QUrl **source** () const
        void ****setSource** ** (const QUrl & **url**
        , QTextDocument::ResourceType **type** = QTextDocument::UnknownResource)
        """
        ...
    def sourceType(self) -> PySide6.QtGui.QTextDocument.ResourceType:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#sourceType-prop

        **[read-only] sourceType : const QTextDocument::ResourceType**

        This property holds the type of the displayed document

        This is **QTextDocument::UnknownResource**  if no document is displayed
        or if the type of the source is unknown. Otherwise it holds the type
        that was detected, or the type that was specified when **setSource** ()
        was called.

        **Access functions:**

        QTextDocument::ResourceType **sourceType** () const
        """
        ...
    @property
    def anchorClicked(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#anchorClicked

        **[signal] void QTextBrowser::anchorClicked(const QUrl & link )**

        This signal is emitted when the user clicks an anchor. The URL referred
        to by the anchor is passed in **link**.

        Note that the browser will automatically handle navigation to the
        location specified by **link** unless the **openLinks**  property is set
        to false or you call **setSource** () in a slot connected. This
        mechanism is used to override the default navigation features of the
        browser.
        """
        ...
    @property
    def backwardAvailable(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#backwardAvailable

        **[signal] void QTextBrowser::backwardAvailable(bool available )**

        This signal is emitted when the availability of **backward** () changes.
        **available** is false when the user is at **home** (); otherwise it is
        true.
        """
        ...
    @property
    def forwardAvailable(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#forwardAvailable

        **[signal] void QTextBrowser::forwardAvailable(bool available )**

        This signal is emitted when the availability of **forward** () changes.
        **available** is true after the user navigates **backward** () and false
        when the user navigates or goes **forward** ().
        """
        ...
    @property
    def highlighted(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#highlighted

        **[signal] void QTextBrowser::highlighted(const QUrl & link )**

        This signal is emitted when the user has selected but not activated an
        anchor in the document. The URL referred to by the anchor is passed in
        **link**.
        """
        ...
    @property
    def historyChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#historyChanged

        **[signal] void QTextBrowser::historyChanged()**

        This signal is emitted when the history changes.

        **See also** **historyTitle** () and **historyUrl** ().
        """
        ...
    @property
    def sourceChanged(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qtextbrowser.html#sourceChanged

        **[signal] void QTextBrowser::sourceChanged(const QUrl & src )**

        This signal is emitted when the source has changed, **src** being the
        new source.

        Source changes happen both programmatically when calling **setSource**
        (), **forward** (), **backward** () or **home** () or when the user
        clicks on links or presses the equivalent key sequences.
        """
        ...
