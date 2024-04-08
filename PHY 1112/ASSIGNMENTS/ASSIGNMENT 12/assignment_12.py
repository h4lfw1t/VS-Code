'''
Filename:       assignment_12.py
Author:         Patrick Geraghty
Date Created:   2024-04-08
Date Modified:  2024-04-08
Description:    Contains the functions quartic_function, gradient_descent, plot_quartic_function, gradient_ascent, and main. Upon execution, main tests the gradient_descent function and the gradient_ascent function using provided initial x positions and a graph for comparison.
'''
import numpy as np
import matplotlib.pyplot as plt

def quartic_function(x):
    '''
    (float) -> float
    This function returns the value of the quartic function x^4 - 3x^2 + x + 1 at x.
    Preconditions: x is a number
    '''
    return x**4 - 3*x**2 + x + 1

def gradient_descent(f, x, h, gamma, tol, max_iter):
    '''
    (function, float, float, float, float, int) -> float
    This function finds the minimum of a function using the gradient descent method for a single variable function.
    Preconditions: f is a single variable function, tol > 0, max_iter > 0
    '''
    for _ in range(max_iter):                                       # iterate through the maximum number of iterations
        grad = (f(x + h / 2) - f(x - h / 2)) / h                                # calculate the gradient for f(x) at x
        x -= gamma * grad                                           # update x
        # if np.linalg.norm(grad) < tol:                            # if the norm of the gradient is less than the tolerance, break (method 1)
        if np.linalg.norm(f(x) - f(x + gamma * grad)) < tol:        # if the difference between f(x_new) and f(x_current) is less than the tolerance, break (method 2)
            break
        if _ == max_iter - 1:                                       # if the maximum number of iterations is reached, print a message and return None
            print("Max iterations reached")
            return None
    return x                                                        # return the minimum of the function

def plot_quartic_function():
    '''
    () -> None
    This function plots the quartic function x^4 - 3x^2 + x + 1.
    Preconditions: None
    '''
    x = np.linspace(-2, 2, 1000)                                    # create an array of x values within the necessary bounds
    y = quartic_function(x)                                         # create an array of y values for the quartic function
    
    plt.figure()                                                    # create a new figure
    
    plt.plot(x, y, label='f(x)')                                    # plot the quartic function
    plt.xlabel('x')                                                 # label the x-axis
    plt.ylabel('y')                                                 # label the y-axis
    plt.title('Quartic Function')                                   # title the plot
    plt.grid()                                                      # add a grid to the plot
    plt.legend()                                                    # add a legend to the plot
    plt.show()                                                      # show the plot

def gradient_ascent(f, x, h, gamma, tol, max_iter):
    '''
    (function, float, float, float, float, int) -> float
    This function finds the maximum of a function using the gradient ascent method for a single variable function.
    Preconditions: f is a single variable function, tol > 0, max_iter > 0
    '''
    for _ in range(max_iter):                                       # iterate through the maximum number of iterations
        grad = (f(x + h / 2) - f(x - h / 2)) / h                                # calculate the gradient for f(x) at x
        x += gamma * grad                                           # update x
        # if np.linalg.norm(grad) < tol:                            # if the norm of the gradient is less than the tolerance, break (method 1)
        if np.linalg.norm(f(x) - f(x + gamma * grad)) < tol:        # if the difference between f(x_new) and f(x_current) is less than the tolerance, break (method 2)
            break
        if _ == max_iter - 1:                                       # if the maximum number of iterations is reached, print a message and return None
            print("Max iterations reached")
            return None
    return x                                                        # return the maximum of the function

def main():
    '''
    () -> None
    This function tests the gradient_descent function and the gradient_ascent function using provided initial x positions and a graph for comparison.
    Preconditions: None
    '''
    print(f'The minimum of f(x) from initial position x = 1 is: x = {gradient_descent(quartic_function, 1, 0.01, 0.1, 1e-6, 1000)}')
    print()
    print(f'The minimum of f(x) from initial position x = 0 is: x = {gradient_descent(quartic_function, 0, 0.01, 0.1, 1e-6, 1000)}')
    print()
    print(f'The minimum of f(x) from initial position x = -1 is: x = {gradient_descent(quartic_function, -1, 0.01, 0.1, 1e-6, 1000)}')
    print()
    plot_quartic_function()
    print()
    print(f'The maximum of f(x) from initial position x = 1 is: x = {gradient_ascent(quartic_function, 1, 0.01, 0.1, 1e-6, 1000)}')
    print()
    print(f'The maximum of f(x) from initial position x = 0 is: x = {gradient_ascent(quartic_function, 0, 0.01, 0.1, 1e-6, 1000)}')
    print()
    print(f'The maximum of f(x) from initial position x = -1 is: x = {gradient_ascent(quartic_function, -1, 0.01, 0.1, 1e-6, 1000)}')

main()