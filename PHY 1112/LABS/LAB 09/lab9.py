'''
Filename:       lab9.py
Author:         Patrick Geraghty
Date Created:   2024-03-12
Date Modified:  2024-03-12
Description:    Contains the functions central_diff, forward_diff_vectorized, backward_diff_vectorized, diff_plot, trapezoidal_rule, sin_function, rule_test, and trapz_plot for lab 9.
'''
import numpy as np
import matplotlib.pyplot as plt

# Part 1

def central_diff(x, y):
    '''
    (np.array, np.array) -> np.array, np.array
    Uses the central difference method to approximate the derivative of f at x.
    Preconditions: x and y are np.arrays of the same length.
    '''
    # Compute the differences in x and y using the same indices seen in class
    df = y[1:] - y[:-1]
    dx = x[1:] - x[:-1]
    
    # Return the x values and the approximations of the derivative of f at x
    # The x values are shifted by 0.5 * dx to align with the central difference method
    return x[:-1] + (0.5 * dx), df/dx

# Define the forward and backward difference methods for comparison
def forward_diff_vectorized(x,y):
    '''
    (np.array, np.array) -> np.array, np.array
    Uses the forward difference method to approximate the derivative of f at x.
    '''
    df = y[1:] - y[:-1]
    dx = x[1:] - x[:-1]
    return x[:-1], df/dx

def backward_diff_vectorized(x,y):
    '''
    (np.array, np.array) -> np.array, np.array
    Uses the backward difference method to approximate the derivative of f at x.
    '''
    dx = x[1:] - x[:-1]
    df = y[1:] - y[:-1]
    return x[1:], df/dx

# plot the approximations of the derivative of f(x) = (x - 1)^2 + 1
def diff_plot():
    # initialize the figure
    plt.figure(1)
    # specify the x and y values
    # set the x values to align with those seen in class for easy comparison
    x = np.linspace(-2, 3, num=11)
    y = np.square(x - 1) + 1
    # compute the true derivative of f at x
    dy = 2 * (x - 1)
    # compute the approximations of the derivative of f at x using the central difference method, forward difference method, and backward difference method
    x1, y1 = central_diff(x, y)
    x2, y2 = forward_diff_vectorized(x, y)
    x3, y3 = backward_diff_vectorized(x, y)
    # plot the true derivative of f at x and the approximations of the derivative of f at x using the central difference method, forward difference method, and backward difference method
    plt.plot(x, dy, 'k', label='f\'(x) = 2(x - 1)')
    plt.plot(x1, y1, 'bo', label='f\'(x) central difference')
    plt.plot(x2, y2, 'ro', label='f\'(x) forward difference')
    plt.plot(x3, y3,'go', label='f\'(x) backward difference')
    # add a title, x-axis label, y-axis label, and legend to the plot    
    plt.title('Approximations of the Derivative of f(x) = (x - 1)^2 + 1')
    plt.xlabel('x')
    plt.ylabel('f\'(x)')
    plt.grid()
    plt.legend()
    plt.show()


# Part 2

def trapezoidal_rule(f, a, b, n):
    '''
    (function, float, float, int) -> float
    Approximate the definite integral of the function f(x) over the interval [a, b] using the trapezoidal rule with n subintervals.
    Preconditions: f is a function, a and b are numbers, and n is an int.
    '''
    # Compute the width of each subinterval
    dx = (b - a) / n

    # Compute the values of the function at the left and right endpoints of each subinterval
    x = np.linspace(a, b, num= n + 1)
    y = f(x)
    # Compute the area of each trapezoid and sum them to approximate the definite integral of f over [a, b] using the trapezoidal rule formula
    return dx * (np.sum(y) - 0.5 * (y[0] + y[-1]))

# define the function f(x) = sin(pi * x)
def sin_function(x):
    '''
    (float) -> float
    Returns the sine of pi * x.
    '''
    return np.sin(np.pi * x)

# test the trapezoidal_rule function
def rule_test():
    '''
    () -> None
    Tests the trapezoidal_rule function with the sin_function.
    '''
    print('n = 20, I =', trapezoidal_rule(sin_function, 0, np.pi, 20))
    print('n = 100, I =', trapezoidal_rule(sin_function, 0, np.pi, 100))
    print('n = 200, I =', trapezoidal_rule(sin_function, 0, np.pi, 200))
    print('n = 1000, I =', trapezoidal_rule(sin_function, 0, np.pi, 1000))
    print('n = 2000, I =', trapezoidal_rule(sin_function, 0, np.pi, 2000))

# plot the true value of the definite integral from 0 to pi of sin(pi * x) with its trapezoidal rule values for n = 20, 100, 200, 1000, and 2000
def trapz_plot():
    '''
    () -> None
    Plots the true value of the definite integral from 0 to pi of sin(pi * x) with its trapezoidal rule values for n = 20, 100, 200, 1000, and 2000.
    Preconditions: None
    '''
    # initialize the figure
    plt.figure(2)
    # plot the trapezoidal rule values for n = 20, 100, 200, 1000, and 2000
    plt.plot(20, trapezoidal_rule(sin_function, 0, np.pi, 20), 'bx', label=f'n = 20, I = {trapezoidal_rule(sin_function, 0, np.pi, 20) :.6f}', markersize=10)
    plt.plot(100, trapezoidal_rule(sin_function, 0, np.pi, 100), 'rx', label=f'n = 100, I = {trapezoidal_rule(sin_function, 0, np.pi, 100) :.6f}', markersize=10)
    plt.plot(200, trapezoidal_rule(sin_function, 0, np.pi, 200), 'gx', label=f'n = 200, I = {trapezoidal_rule(sin_function, 0, np.pi, 200) :.6f}', markersize=10)
    plt.plot(1000, trapezoidal_rule(sin_function, 0, np.pi, 1000), 'kx', label=f'n = 1000, I = {trapezoidal_rule(sin_function, 0, np.pi, 1000) :.6f}', markersize=10)
    plt.plot(2000, trapezoidal_rule(sin_function, 0, np.pi, 2000), 'mx', label=f'n = 2000, I = {trapezoidal_rule(sin_function, 0, np.pi, 2000) :.6f}', markersize=10)
    # plot the true value of the definite integral from 0 to pi of sin(pi * x) as a horizontal line
    plt.axhline(y=(1/np.pi) * (-np.cos(np.square(np.pi)) + 1), color='r', linestyle='-')
    # add a title, x-axis label, y-axis label, and legend to the plot    
    plt.title('Trapezoidal Rule Approximations of the Definite Integral of sin(pi * x) from 0 to pi')
    plt.xlabel('n')
    plt.ylabel('I')
    plt.grid()
    plt.legend()
    plt.show()