"""QtPyGraph's entry point script."""

from __future__ import annotations

from PySide6 import QtWidgets


def main() -> None:
    """Entrypoint script for ``qtpygraph``."""
    app = QtWidgets.QApplication()

    window = QtWidgets.QMainWindow()
    window.setWindowTitle('Sup')
    layout = QtWidgets.QVBoxLayout()

    label = QtWidgets.QLabel('i need to poop')

    layout.addWidget(label)
    window.setCentralWidget(label)
    # window.setLayout(layout)

    window.show()

    app.exec()


if __name__ == '__main__':
    main()
