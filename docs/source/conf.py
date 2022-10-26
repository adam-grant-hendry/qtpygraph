"""Documentation configuration file.

This file is read by the ``sphinx`` documentation builder to generate our documentation.
"""
# pylint: disable=invalid-name; sphinx variables are case-sensitive
from __future__ import annotations

import importlib.resources as rsrc
import os
import sys
from datetime import date

import qtpygraph

# -- Project information ----------------------------------------------------------------

project = 'QtPyGraph'
copyright = f'2022-{date.today().year}, Adam Hendry'  # pylint: disable=redefined-builtin
author = 'Adam Hendry'
root_package = 'qtpygraph'
version = qtpygraph.__version__
release = version

# -- Path setup -------------------------------------------------------------------------

with rsrc.path(root_package, '__init__.py') as file_:
    root = file_.parent.parent

packages = [
    root / root_package,
    root / r'docs',
    root / r'tests',
]

for pkg in packages:
    # In Python 3.6 and later it is recommended to use os.fspath() instead of str() if
    # you need to do an explicit conversion. This is a little safer as it will raise an
    # error if you accidentally try to convert an object that is not pathlike.
    sys.path.insert(0, os.fspath(pkg.resolve()))

# -- Extensions -------------------------------------------------------------------------

extensions: list[str] = [
    'numpydoc',
    'sphinx_book_theme',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinxcontrib.email',
    'sphinxcontrib.mermaid',
]

# -- General configuration --------------------------------------------------------------

# Paths are relative to ``source``
# templates_path = ['_templates']
# html_static_path = ['_static']

source_suffix = '.rst'
master_doc = 'index'

# List of files relative to ``source`` to ignore when looking for source files
exclude_patterns: list[str] = [
    '_build',
]

# -- HTML Output ------------------------------------------------------------------------

html_theme = 'sphinx_book_theme'
# html_css_files = [
#     'css/custom.css',
# ]
# html_style = 'css/style.css'

# html_logo = r'./_resources/img/qtpygraph_logo.png'

# String appended to project name with hyphen in ``<title>`` tag of individual pages and
# used in the navigation bar as the “topmost” element. It defaults to '<project>
# v<revision> documentation'. Remove so only project name appears in title.
html_title = 'QtPyGraph'

html_short_title = project

html_theme_options = {
    'repository_url': 'https://github.com/adam-grant-hendry/qtpygraph',
    'use_repository_button': True,
}

# Removes the "View Source" hyperlink
html_show_sourcelink = False

# Enable figure numbering. If true, figures, tables and code-blocks are automatically
# numbered if they have a caption. The numref role is enabled. Obeyed so far only by
# HTML and LaTeX builders. Default is False.
num_fig = True
