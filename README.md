# Function Intersection Finder

## Project Overview

Function Intersection Finder is a PySide2-based GUI application that allows users to input two mathematical functions, plot them, and find their intersection points. The application utilizes `matplotlib` for graph plotting and `scipy.optimize.fsolve` for finding intersection points.

## Features

- User-friendly GUI built with PySide2 (Qt for Python)
- Allows users to input two mathematical functions
- Parses functions and evaluates them using `numpy`
- Finds intersection points using `fsolve`
- Plots functions and marks intersection points

## Installation

### Prerequisites

Ensure you have Python installed (Python 3.7+ recommended). Install the required dependencies using:

```sh
pip install numpy scipy matplotlib PySide2 pytest pytest-qt
```

## Usage

Run the application using:

```sh
python GUI.py
```

### Steps to Use:

1. Enter two mathematical functions in the provided text fields (e.g., `x**2`, `sin(x)`).
2. Click the "Find Intersections" button.
3. The functions will be plotted, and their intersection points will be displayed.

## Function Parsing Rules

- Use `x` as the variable.
- Supported operations: `+, -, *, /, ^`.
- Supported functions: `sin`, `cos`, `tan`, `log10`, `sqrt`
- Use standard Python syntax for mathematical expressions.

## Testing

The project includes tests using `pytest`. To run tests:

```sh
pytest testing.py
```

## Author

**Mohamed Salah Fathy**

## License

This project is open-source and licensed under the MIT License.

![Description](images/Screenshot%202025-01-29%20155309.png)
![Description](images/Screenshot%202025-01-30%20140826.png)
![Description](images/Screenshot%202025-01-30%20140830.png)
![Description](images/Screenshot%202025-01-30%20140851.png)
![Description](images/Screenshot%202025-01-30%20140903.png)
![Description](images/Screenshot%202025-01-30%20143155.png)
