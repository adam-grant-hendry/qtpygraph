"""Test configuration file."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from qtpy import QtCore, QtWidgets

if TYPE_CHECKING:
    from collections.abc import Generator, Sequence

    from pytestqt.qtbot import QtBot

# Register plugins to use in testing
pytest_plugins: str | Sequence[str] = [
    'pytester',
]

# Exclude certain dirs from being collected by the ``pytest`` runner.
collect_ignore: list[str] = ['roots', '__init__.py']

SRC = str((Path(__file__).parent.parent / 'docs' / 'source').absolute())

# Qt fixtures


@pytest.fixture(autouse=True)
def clear_settings() -> Generator[None, None, None]:
    """Teardown fixture for clearing ``Qt`` settings.

    Yields
    ------
    Generator[None, None, None]
        Waits for program to exit.
    """
    # Run
    yield

    # Teardown
    QtCore.QSettings().clear()


@pytest.fixture(name='qmainwindow')
def fixture_qmainwindow(
    qtbot: QtBot,
) -> Generator[QtWidgets.QMainWindow, None, None]:
    """Fixture for testing a ``QMainWindow``.

    This is used to test custom ``qtpygraph`` widgets, which get added into a
    ``QMainWindow``.

    Parameters
    ----------
    qtbot : QtBot
        ``pytest-qt`` fixture for simulating user interaction with ``Qt`` widgets.

    Yields
    ------
    Generator[QtWidgets.QMainWindow, None, None]
        The ``QMainWindow`` widget added to ``qtbot``.
    """
    # Setup
    window = QtWidgets.QMainWindow()

    # When in windows mode (non-headless), window must have focus
    window.setWindowFlags(
        QtCore.Qt.WindowTypeWindow
        | QtCore.Qt.WindowTypeCustomizeWindowHint
        | QtCore.Qt.WindowTypeWindowStaysOnTopHint
    )

    layout = QtWidgets.QVBoxLayout()
    layout.setSpacing(0)
    layout.setContentsMargins(0, 0, 0, 0)

    window.setLayout(layout)

    window.setMouseTracking(True)
    window.show()

    qtbot.addWidget(window)

    # Run
    yield window

    # Teardown - None
