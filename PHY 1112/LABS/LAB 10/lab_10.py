'''
Filename:       lab_10.py
Author:         Patrick Geraghty
Date Created:   2024-03-19
Date Modified:  2024-03-19
Description:    Lab 10
'''

import numpy as np
import matplotlib.pyplot as plt

# Part 1

def eulers_method(f, n, a, b, y0):
    h = (b - a) / n
    x = np.linspace(a, b, num=n+1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y

# Part 2

def test_function(x, y):
    '''
    (float, np.array, np.array) -> np.array
    Takes in two np.arrays and returns the product of the two arrays such that f(x, y) = -yx.
    Preconditions: x and y are of the same length
    '''
    return -y * x

def main():
    '''
    () -> None
    Plots the results of eulers_method using the test_function with n = 10, 100, 1000, c = -1, a = 0, b = 3, and y0 = 1.
    Preconditions: None
    '''
    
    x = np.linspace(0, 3, 10000)
    y = np.e ** (-x**2 / 2)

    x1, y1 = eulers_method(test_function, 10, 0, 3, 1)
    x2, y2 = eulers_method(test_function, 100, 0, 3, 1)
    x3, y3 = eulers_method(test_function, 1000, 0, 3, 1)

    plt.figure(1)
    plt.plot(x, y, 'r', label='y = e^(-x^2 / 2)', linewidth=4, alpha=1)
    plt.plot(x3, y3, 'yo', label='n = 1000', markersize=2, alpha=0.5)
    plt.plot(x2, y2, 'go', label='n = 100', markersize=2, alpha=0.5)
    plt.plot(x1, y1, 'bo', label='n = 10', markersize=2, alpha=0.5)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Euler\'s Method Implementation of y\' = -yx')
    plt.legend()
    plt.grid()
    plt.show()

    # plt.figure(2)
    
    # n = np.arange(10, 1001, 10)
    # error = np.zeros(len(n))
    
    # for i in range(len(n)):
    #     x, y = eulers_method(test_function, n[i], 0, 3, 1)
    
    

    # plt.plot(n, error, 'b')
    # plt.xlabel('n')
    # plt.ylabel('error')
    # plt.title('Error of Euler\'s Method Implementation of y\' = -yx')
    # plt.grid()
    # plt.show()