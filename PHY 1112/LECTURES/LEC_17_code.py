import numpy as np

def trapezoidal_rule(f, a, b, n):
    """
    Approximate the definite integral of the function f(x) over the interval [a, b] using the trapezoidal rule.
    
    Parameters
    ----------
    f : function
        The function to integrate.
    a : float
        The lower limit of integration.
    b : float
        The upper limit of integration.
    n : int
        The number of subintervals to use.
        
    Returns
    -------
    float
        An approximation of the definite integral of f(x) over the interval [a, b] using the trapezoidal rule.
    """
    # Compute the width of each subinterval
    dx = (b - a) / n

    # Compute the values of the function at the left and right endpoints of each subinterval
    x = np.linspace(a, b, num= n + 1)
    y = f(x)

    return dx * (np.sum(y) - 0.5 * (y[0] + y[-1]))

def sin(x):
    return np.sin(x)

def trap_alt(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    dx = x[1:] - x[:-1]
    dy = (y[1:] - y[:-1])/2
    return np.sum(dx*dy)

def trap_class(f, a, b, n):
    dx = (b - a)/n
    x = np.linspace(a, b, n+1)
    return dx*(np.sum(f(x)) - 0.5*(f(a) + f(b)))