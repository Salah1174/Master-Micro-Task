from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import Qt
from GUI import FunctionPlotter
import pytest


def test_gui_launch(qtbot):
    window = FunctionPlotter()
    qtbot.addWidget(window)
    window.show()  # Ensure window is visible
    assert window.isVisible()


def test_valid_input(qtbot):
    window = FunctionPlotter()
    qtbot.addWidget(window)
    window.show()

    qtbot.keyClicks(window.input1, "x^2")
    qtbot.keyClicks(window.input2, "x")
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)

    qtbot.waitUntil(lambda: len(window.ax.lines) > 0, timeout=3000)
    assert len(window.ax.lines) > 0  # Ensure the graph is plotted


def test_invalid_input(qtbot):
    window = FunctionPlotter()
    qtbot.addWidget(window)

    window.input1.setText("invalid_function")
    window.input2.setText("x^2")

    assert not window.find_intersection(), "Function should return False for invalid input"
