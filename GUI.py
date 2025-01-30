import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide2.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        button = QPushButton("Press me!")
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)


def functionstrtoexpression(function_str):
    function_str = function_str.lower()
    function_str = function_str.replace("^", "**")
    function_str = function_str.replace("log10", "np.log10")
    function_str = function_str.replace("sqrt", "np.sqrt")
    function_str = function_str.replace("sin", "np.sin")
    function_str = function_str.replace("cos", "np.cos")
    function_str = function_str.replace("tan", "np.tan")

    # Test if the expression is valid
    try:
        test_x = 0  # Test value
        eval(function_str, {"np": np, "x": test_x})
    except Exception as e:
        raise ValueError(f"Invalid function: {function_str}. Error: {e}")

    return string_to_function(function_str)


def string_to_function(expression):
    def function(x):
        try:
            return eval(expression, {"np": np, "x": x})
        except Exception:
            return np.nan
    return function


class FunctionPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Intersection Finder")
        self.setGeometry(100, 100, 800, 600)

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)

        self.label1 = QLabel("Enter the first function:")
        self.layout.addWidget(self.label1)

        self.input1 = QLineEdit()
        self.layout.addWidget(self.input1)

        self.label2 = QLabel("Enter the second function:")
        self.layout.addWidget(self.label2)

        self.input2 = QLineEdit()
        self.layout.addWidget(self.input2)

        self.plot_button = QPushButton("Find Intersections")
        self.plot_button.clicked.connect(self.find_intersection)
        self.layout.addWidget(self.plot_button)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def find_intersection(self):
        
        function1_str = self.input1.text()
        function2_str = self.input2.text()

        try:
            function1 = functionstrtoexpression(function1_str)
            function2 = functionstrtoexpression(function2_str)
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))
            return False  # Indicate failure

        def difference(x):
            return function1(x) - function2(x)

        x_values = np.linspace(-10, 10, 1000)
        intersection_points = []

        for i in range(len(x_values) - 1):
            root = fsolve(difference, x_values[i])[0]
            if -10 <= root <= 10 and not any(np.isclose(root, p, atol=1e-2) for p in intersection_points):
                intersection_points.append(root)

        intersection_points = np.array(intersection_points)
        y_intersect = function1(intersection_points)
        valid_points = ~np.isnan(y_intersect)
        intersection_points, y_intersect = intersection_points[
            valid_points], y_intersect[valid_points]

        self.ax.clear()
        self.ax.plot(x_values, function1(x_values),
                     label=f'{function1_str}', color='red')
        self.ax.plot(x_values, function2(x_values),
                     label=f'{function2_str}', color='blue')
        self.ax.scatter(intersection_points, y_intersect,
                        color='black', zorder=3, label='Intersection Points')

        for x, y in zip(intersection_points, y_intersect):
            self.ax.annotate(f'({x:.2f}, {y:.2f})', (x, y),
                             textcoords="offset points", xytext=(5, 5), ha='right')

        self.ax.set_title('Graph of the functions')
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.legend()
        self.ax.grid()

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    sys.exit(app.exec_())
    self.setCentralWidget(widget)
