import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve


def functionstrtoexpression(function_str):
    function_str = function_str.lower()
    function_str = function_str.replace("^", "**")
    function_str = function_str.replace("log10", "np.log10")
    function_str = function_str.replace("sqrt", "np.sqrt")
    function_str = function_str.replace("sin", "np.sin")
    function_str = function_str.replace("cos", "np.cos")
    function_str = function_str.replace("tan", "np.tan")
    return string_to_function(function_str)


def string_to_function(expression):
    def function(x):
        try:
            return eval(expression, {"np": np, "x": x})
        except Exception:
            return np.nan
    return function


def find_intersection():
    function1_str = input("Enter the first function: ")
    function1 = functionstrtoexpression(function1_str)

    function2_str = input("Enter the second function: ")
    function2 = functionstrtoexpression(function2_str)

    def difference(x):
        return function1(x) - function2(x)

    x_values = np.linspace(-10, 10, 1000)
    intersection_points = []

    for i in range(len(x_values) - 1):
        root = fsolve(difference, x_values[i])
        root = root[0]
        if -10 <= root <= 10 and not any(np.isclose(root, p, atol=1e-2) for p in intersection_points):
            intersection_points.append(root)

    intersection_points = np.array(intersection_points)
    y_intersect = function1(intersection_points)
    valid_points = ~np.isnan(y_intersect)
    intersection_points, y_intersect = intersection_points[valid_points], y_intersect[valid_points]

    print("Intersection Points:")
    for x, y in zip(intersection_points, y_intersect):
        print(f"({x:.4f}, {y:.4f})")

    y1_values = function1(x_values)
    y2_values = function2(x_values)

    plt.plot(x_values, y1_values, label=f'{function1_str}', color='red')
    plt.plot(x_values, y2_values, label=f'{function2_str}', color='blue')

    plt.scatter(intersection_points, y_intersect, color='black',
                zorder=3, label='Intersection Points')
    for x, y in zip(intersection_points, y_intersect):
        plt.annotate(f'({x:.2f}, {y:.2f})', (x, y),
                     textcoords="offset points", xytext=(5, 5), ha='right')

    plt.title('Graph of the functions')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()


find_intersection()
