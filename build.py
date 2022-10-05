"""QtPyGraph setup script for building wheel."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import toml
from setuptools import find_packages

FILE_45 = Path.cwd() / '45'

if FILE_45.exists():
    # `poetry` seems to generate a file corresponding to requested version of `setuptools`
    # in the `pyproject.toml` table `build-system` whenever we build.
    # We delete this to avoid erroneously commiting it to our repository.
    FILE_45.unlink()

if Path.cwd().stem != 'qtpygraph':
    raise OSError(
        'The `poetry` commands `install` and `build` must be run from the same directory'
        ' where `pyproject.toml` resides. You are currently in the following'
        ' directory:\n\n'
        f'{Path.cwd()}',
    )

metadata = toml.load('pyproject.toml')['tool']['poetry']
short_description = (  # pylint: disable=invalid-name
    'A pythonic interface to the Qt Graphics View Framework using qtpy.'
)
long_description = Path('README.rst').read_text(encoding='utf-8')

kwargs = {
    'author': metadata['authors'],
    'classifiers': metadata['classifiers'],
    'description': short_description,
    'license': metadata['license'],
    'long_description_content_type': 'text/x-rst',
    'long_description': long_description,
    'name': metadata['name'],
    'packages': find_packages(),
    'python_requires': '>=3.8,<3.11',
    'version': metadata['version'],
    'zip_safe': False,
}


def build(setup_kwargs: dict[str, Any]) -> None:
    """Force poetry to build with these kwargs."""
    setup_kwargs.update(**kwargs)
