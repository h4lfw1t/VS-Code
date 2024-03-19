import numpy as np

def eulers_method(f, n, a, b, y0):
    h = (b - a) / n
    x = np.linspace(a, b, num=n)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y

def euler_loop(f, a, b, y0, n):
    h = (b - a) / n
    x = np.linspace(a, b, num=n)
    for i in range(n):
        y0 = y0 + h * f(x[i], y0)
    return y0

def fx(x, y):
    return x + y

def gx(x, y):
    return -y * x

# def eulers_method_vectorized(f, n, a, b, y0):
#     h = (b - a) / n
#     x = np.linspace(a, b, num=n)
#     y = np.zeros(n)
#     y[0] = y0
#     y[1:] = h * f(x[:-1], y[:-1]).cumsum() + y[:-1]
#     return x, y

# print(f'Vectorized: {eulers_method_vectorized(fx, 10, 0, 1, 1)}')

# print(f'Loop: {eulers_method(fx, 10, 0, 1, 1)}')