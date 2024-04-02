'''
Filename:       lab_12.py
Author:         Patrick Geraghty
Date Created:   2024-04-02
Date Modified:  2024-04-02
Description:    Lab 12 - Functions
'''
import numpy as np
import matplotlib.pyplot as plt

# Part 1.

def bisection_root(f, a, b, tolerance):
    '''
    (float, float, function) -> float
    This function finds the root of a function f(x) using the bisection method.
    Preconditions: tolerance is positive.
    '''
    # Check if a and b are ordered correctly (i.e b > a). If they are not, swap them and continue.
    if a >= b:
        a, b = b, a
        print("a and b have been swapped due to ValueError: a >= b")
    
    # Check if f(a) and f(b) have the same sign. If they do, return None.
    if np.sign(f(a)) == np.sign(f(b)):
        print("ValueError: f(a) and f(b) have the same sign. Please choose different a and b.")
        return None
    
    # Check if f(a) or f(b) is zero. If they are, return the corresponding value (this is the root).
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    
    # Calculate the root using the bisection method within tolerance.
    while abs(b - a) > tolerance:
        # Calculate the midpoint of the interval.
        c = (a + b) / 2
        # Check if the midpoint is the root.
        if f(c) == 0:
            return c
        # Check if the root is in the left half of the interval.
        elif f(a) * f(c) < 0:
            # Update the interval if the root is within the bounds.
            b = c
        else:
            # Update the interval.
            a = c
    # Return the root.
    return c

# Part 2.

def f(x):
    '''
    (float) -> float
    This function defines the function f(x) = (x + 1)(x - 2)(x - 3).
    Preconditions: None.
    '''
    return (x + 1) * (x - 2) * (x - 3)

def f_x_plot():
    '''
    () -> None
    This function plots the function f(x) = (x + 1)(x - 2)(x - 3) over the interval [-5, 5].
    Preconditions: None.
    '''
    # Define the x values.
    x = np.linspace(-5, 5, 1000)
    # Define the y values.
    y = f(x)
    # Plot the function.
    plt.figure(1)
    plt.plot(x, y, label="f(x) = (x + 1)(x - 2)(x - 3)", color="blue")
    plt.axhline(0, color="red", linewidth=0.5)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.ylim(-10, 10)
    plt.title("f(x) = (x + 1)(x - 2)(x - 3)")
    plt.grid()
    plt.legend()
    plt.show()

def f_x_root_snapper():
    '''
    () -> None
    This function finds the roots of the function f(x) = (x + 1)(x - 2)(x - 3) using the bisection method for varying endpoints.
    Preconditions: None.
    '''
    print("Roots of f(x) = (x + 1)(x - 2)(x - 3) on:")
    print("[-5, -2]:", bisection_root(f, -5, -2, 1e-5))
    print()
    print("[-2, 1]:", bisection_root(f, -2, 1, 1e-5))
    print()
    print("[1, 2.5]:", bisection_root(f, 1, 2.5, 1e-5))
    print()
    print("[2.5, 3]:", bisection_root(f, 2.5, 3, 1e-5))
    print()
    print("[1, 4]:", bisection_root(f, 1, 4, 1e-5))

# Part 3.

def g(x):
    '''
    (float) -> float
    This function defines the function g(x) = (x - 3)(x - 2) / (x - 1)
    Preconditions: None.
    '''
    return (x - 3) * (x - 2) / (x - 1)

def g_x_plot():
    '''
    () -> None
    This function plots the function g(x) = (x - 3)(x - 2) / (x - 1) over the interval [-6, 6].
    Preconditions: None.
    '''
    # Define the x values.
    x = np.linspace(-6, 6, 1000)
    # Define the y values.
    y = g(x)
    # Plot the function.
    plt.figure(2)
    plt.plot(x, y, label="g(x) = (x - 3)(x - 2) / (x - 1)", color="green")
    plt.axhline(0, color="red", linewidth=0.5)
    plt.xlabel("x")
    plt.ylabel("g(x)")
    plt.ylim(-10, 10)
    plt.title("g(x) = (x - 3)(x - 2) / (x - 1)")
    plt.grid()
    plt.legend()
    plt.show()

def g_x_root_snapper():
    '''
    () -> None
    This function finds the roots of the function g(x) = (x - 3)(x - 2) / (x - 1) using the bisection method for varying endpoints.
    Preconditions: None.
    '''
    print("Roots of g(x) = (x - 3)(x - 2) / (x - 1) on:")
    print("[-2, 0]:", bisection_root(g, -2, 0, 1e-5))
    print()
    print("[0, 1.5]:", bisection_root(g, 0, 1.5, 1e-5))
    print()
    print("[1.5, 2.75]:", bisection_root(g, 1.5, 2.75, 1e-5))
    print()
    print("[2.75, 4]:", bisection_root(g, 2.75, 4, 1e-5))
    print()
    print("[4, 5.5]:", bisection_root(g, 4, 5.5, 1e-5))




def main():
    f_x_plot()
    f_x_root_snapper()
    g_x_plot()
    g_x_root_snapper()