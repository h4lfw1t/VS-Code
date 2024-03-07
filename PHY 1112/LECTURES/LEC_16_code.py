import numpy as np
import matplotlib.pyplot as plt

def forward_diff_for(x, y):
    '''
    (np.array, np.array) -> np.array, np.array
    Uses the forward difference method to approximate the derivative of f at x.
    '''
    for i in range(len(x)-1):
        h = x[i+1] - x[i]
        y[i] = (y[i+1] - y[i])/h
    return x[:-1], y[:-1]

def forward_diff_vectorized(x,y):
    '''
    (np.array, np.array) -> np.array, np.array
    Uses the forward difference method to approximate the derivative of f at x.
    '''
    df = x[1:] - x[:-1]
    dx = y[1:] - y[:-1]
    return x[:-1], df/dx

def backward_diff_vectorized(x,y):
    '''
    (np.array, np.array) -> np.array, np.array
    Uses the backward difference method to approximate the derivative of f at x.
    '''
    dx = x[1:] - x[:-1]
    df = y[1:] - y[:-1]
    return x[1:], df/dx

def central_diff_vectorized(x,y):
    '''
    (np.array, np.array) -> np.array, np.array
    Uses the central difference method to approximate the derivative of f at x.
    '''

def diff_plot():
    x = np.linspace(-5, 5)
    y = x**2
    x1, y1 = central_diff_vectorized(x, y)
    plt.plot(x, y, label='f(x) = x^2')
    plt.plot(x1, y1, label='f\'(x) backward difference')
    plt.legend()
    plt.show()