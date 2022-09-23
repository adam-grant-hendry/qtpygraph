"""Test configuration file."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Iterator, Sequence

import pytest
from _pytest.fixtures import SubRequest
from bs4 import BeautifulSoup
from sphinx.testing.path import path
from sphinx.testing.util import SphinxTestApp

# Register plugins to use in testing
pytest_plugins: str | Sequence[str] = [
    'sphinx.testing.fixtures',
    'pytester',
]


# Exclude certain dirs from being collected by the ``pytest`` runner.
collect_ignore: list[str] = ['roots', '__init__.py']

SRC = str((Path(__file__).parent.parent / 'docs' / 'source').absolute())

# -- Sphinx fixtures ---------------------------------------------------------------------


@pytest.fixture(name='rootdir')
def fixture_rootdir() -> Iterator[str]:
    """``emmy`` fixture yielding the source directory for ``sphinx`` documentation.

    Yields
    ------
    str
        The source directory for ``sphinx`` documentation.
    """
    yield path(SRC).abspath()


@pytest.fixture(name='content')
def fixture_content(
    make_app: Callable[..., Any],
    rootdir: str,
) -> Iterator[SphinxTestApp]:
    """``emmy`` fixture yielding the HTML content of the docs.

    Parameters
    ----------
    make_app : Callable[..., Any]
        A ``sphinx.testing`` fixture. This is a function that creates a ``SphinxTestApp``
        from provided source and build directories and a provided build generator (e.g.
        html)
    rootdir : str
        Test root directory

    Yields
    ------
    SphinxTestApp
        The ``SphinxTestApp``.
    """
    sphinx_app = make_app(
        buildername='html',
        srcdir=rootdir,
        builddir=path(SRC).abspath(),
    )
    sphinx_app.build()
    yield sphinx_app


@pytest.fixture(name='page')
def fixture_page(
    content: SphinxTestApp,
    request: SubRequest,
) -> Iterator[BeautifulSoup]:
    """Fixture yielding a ``BeautifulSoup`` web scraper for a provided ``page``
    of the docs.

    Parameters
    ----------
    content : SphinxTestApp
        The HTML content of the docs.
    request : SubRequest
        A built-in ``pytest`` fixture for passing information to and from fixtures

    Yields
    ------
    BeautifulSoup
        A web scraper for the provided ``page`` of the docs. (Uses ``html5lib``.)
    """
    page_name = request.param
    page_content = (content.outdir / page_name).read_text()

    yield BeautifulSoup(page_content, 'html5lib')
