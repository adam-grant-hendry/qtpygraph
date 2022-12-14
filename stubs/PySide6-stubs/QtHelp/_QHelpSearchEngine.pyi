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
PySide6.QtHelp, except for defaults which are replaced by "...".
"""
from __future__ import annotations

from collections.abc import Sequence
from typing import overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtHelp
import PySide6.QtWidgets

class QHelpSearchEngine(PySide6.QtCore.QObject):
    """
    https://doc.qt.io/qt-6/qhelpsearchengine.html

    **Detailed Description**

    Before the search engine can be used, one has to instantiate at least a
    **QHelpEngineCore**  object that needs to be passed to the search engines
    constructor. This is required as the search engine needs to be connected to
    the help engines setupFinished() signal to know when it can start to index
    documentation.

    After starting the indexing process the signal **indexingStarted** () is
    emitted and on the end of the indexing process the **indexingFinished** ()
    is emitted. To stop the indexing one can call **cancelIndexing** ().

    When the indexing process has finished, the search engine can be used to
    search through the index for a given term using the search() function. When
    the search input is passed to the search engine, the **searchingStarted** ()
    signal is emitted. When the search finishes, the **searchingFinished** ()
    signal is emitted. The search process can be stopped by calling
    **cancelSearching** ().

    If the search succeeds, **searchingFinished** () is called with the search
    result count to fetch the search results from the search engine. Calling the
    **searchResults** () function with a range returns a list of
    **QHelpSearchResult**  objects within the range. The results consist of the
    document title and URL, as well as a snippet from the document that contains
    the best match for the search input.

    To display the given search results use the **QHelpSearchResultWidget**  or
    build up your own one if you need more advanced functionality. Note that the
    **QHelpSearchResultWidget**  can not be instantiated directly, you must
    retrieve the widget from the search engine in use as all connections will be
    established for you by the widget itself.
    """

    def __init__(
        self,
        helpEngine: PySide6.QtHelp.QHelpEngineCore,
        parent: PySide6.QtCore.QObject | None = ...,
    ) -> None:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#QHelpSearchEngine

        **QHelpSearchEngine::QHelpSearchEngine(QHelpEngineCore * helpEngine ,
        QObject * parent = nullptr)**

        Constructs a new search engine with the given **parent**. The search
        engine uses the given **helpEngine** to access the documentation that
        needs to be indexed. The **QHelpEngine** 's setupFinished() signal is
        automatically connected to the QHelpSearchEngine's indexing function, so
        that new documentation will be indexed after the signal is emitted.
        """
        ...
    def cancelIndexing(self) -> None:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#cancelIndexing

        **[slot] void QHelpSearchEngine::cancelIndexing()**

        Stops the indexing process.
        """
        ...
    def cancelSearching(self) -> None:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#cancelSearching

        **[slot] void QHelpSearchEngine::cancelSearching()**

        Stops the search process.
        """
        ...
    def hitCount(self) -> int: ...
    def hits(self, start: int, end: int) -> list[tuple[str, str]]: ...
    def hitsCount(self) -> int: ...
    def query(self) -> list[PySide6.QtHelp.QHelpSearchQuery]: ...
    def queryWidget(self) -> PySide6.QtHelp.QHelpSearchQueryWidget:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#queryWidget

        **QHelpSearchQueryWidget *QHelpSearchEngine::queryWidget()**

        Returns a widget to use as input widget. Depending on your search engine
        configuration you will get a different widget with more or less
        subwidgets.
        """
        ...
    def reindexDocumentation(self) -> None:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#reindexDocumentation

        **[slot] void QHelpSearchEngine::reindexDocumentation()**

        Forces the search engine to reindex all documentation files.
        """
        ...
    def resultWidget(self) -> PySide6.QtHelp.QHelpSearchResultWidget:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#resultWidget

        **QHelpSearchResultWidget *QHelpSearchEngine::resultWidget()**

        Returns a widget that can hold and display the search results.
        """
        ...
    def scheduleIndexDocumentation(self) -> None: ...
    @overload
    def search(self, queryList: Sequence[PySide6.QtHelp.QHelpSearchQuery]) -> None:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#search-1

        **[slot, since 5.9] void QHelpSearchEngine::search(const QString &
        searchInput )**

        Starts the search process using the given search phrase **searchInput**.

        The phrase may consist of several words. By default, the search engine
        returns the list of documents that contain all the specified words. The
        phrase may contain any combination of the logical operators AND, OR, and
        NOT. The operator must be written in all capital letters, otherwise it
        will be considered a part of the search phrase.

        If double quotation marks are used to group the words, the search engine
        will search for an exact match of the quoted phrase.

        For more information about the text query syntax, see **SQLite FTS5
        Extension** .

        This function was introduced in Qt 5.9.
        """
        ...
    @overload
    def search(self, searchInput: str) -> None:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#search-1

        **[slot, since 5.9] void QHelpSearchEngine::search(const QString &
        searchInput )**

        Starts the search process using the given search phrase **searchInput**.

        The phrase may consist of several words. By default, the search engine
        returns the list of documents that contain all the specified words. The
        phrase may contain any combination of the logical operators AND, OR, and
        NOT. The operator must be written in all capital letters, otherwise it
        will be considered a part of the search phrase.

        If double quotation marks are used to group the words, the search engine
        will search for an exact match of the quoted phrase.

        For more information about the text query syntax, see **SQLite FTS5
        Extension** .

        This function was introduced in Qt 5.9.
        """
        ...
    def searchInput(self) -> str:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#searchInput

        **[since 5.9] QString QHelpSearchEngine::searchInput() const**

        Returns the phrase that was last searched for.

        This function was introduced in Qt 5.9.
        """
        ...
    def searchResultCount(self) -> int:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#searchResultCount

        **[since 5.9] int QHelpSearchEngine::searchResultCount() const**

        Returns the number of results the search engine found.

        This function was introduced in Qt 5.9.
        """
        ...
    def searchResults(
        self, start: int, end: int
    ) -> list[PySide6.QtHelp.QHelpSearchResult]:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#searchResults

        **[since 5.9] QList<QHelpSearchResult>
        QHelpSearchEngine::searchResults(int start , int end ) const**

        Returns a list of search results within the range from the index
        specified by **start** to the index specified by **end**.

        This function was introduced in Qt 5.9.
        """
        ...
    @property
    def indexingFinished(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#indexingFinished

        **[signal] void QHelpSearchEngine::indexingFinished()**

        This signal is emitted when the indexing process is complete.
        """
        ...
    @property
    def indexingStarted(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#indexingStarted

        **[signal] void QHelpSearchEngine::indexingStarted()**

        This signal is emitted when indexing process is started.
        """
        ...
    @property
    def searchingFinished(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#searchingFinished

        **[signal] void QHelpSearchEngine::searchingFinished(int
        searchResultCount )**

        This signal is emitted when the search process is complete. The search
        result count is stored in **searchResultCount**.
        """
        ...
    @property
    def searchingStarted(self) -> PySide6.QtCore.SignalInstance:
        """
        https://doc.qt.io/qt-6/qhelpsearchengine.html#searchingStarted

        **[signal] void QHelpSearchEngine::searchingStarted()**

        This signal is emitted when the search process is started.
        """
        ...
