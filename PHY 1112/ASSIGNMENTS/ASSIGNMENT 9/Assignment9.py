'''
Filename:       Assignment9.py
Author:         Patrick Geraghty
Date Created:   2024-03-18
Date Modified:  2024-03-18
Description:    Contains relevant functions for Assignment 9.
'''

import numpy as np
import matplotlib.pyplot as plt

# Part 1

def load_data():
    '''
    () -> (np.array, np.array)
    Load the data from the file and return the x and y values as arrays.
    Preconditions: The file is in the same directory as the program.
    '''
    # Load the data from the file
    data = np.genfromtxt('baseball_height.csv', delimiter=',')
    # Split the data into x and y arrays
    x_data = data[:, 0]
    y_data = data[:, 1]
    return x_data, y_data

def height_plot():
    '''
    () -> None
    Create a scatter plot of the data from 'baseball_height.csv'.
    Preconditions: None
    '''
    # Load the data from the file
    x_data, y_data = load_data()
    
    # Initialize the first figure
    plt.figure(1)
    # Create a scatter plot of the data with relevant labels and titles
    plt.scatter(load_data()[0], load_data()[1], c='k', marker='o', label='Baseball Height (m)')
    plt.title('Baseball Height Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Height (m)')
    plt.legend()
    plt.grid()
    plt.show()

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

def first_derivative_plot():
    '''
    () -> None
    Create a scatterplot of the first central difference for the data in 'baseball_height.csv'.
    Preconditions: None
    '''
    # Load the data from the file
    x_data, y_data = load_data()
    
    # Compute the first central difference of the data
    dx, dy = central_diff(x_data, y_data)
    
    # Initialize the second figure
    plt.figure(2)
    # Create a scatter plot of the data with relevant labels and titles
    plt.scatter(dx, dy, c='k', marker='o', label='Velocity of Baseball')
    plt.title('Velocity of Baseball Over Time Using Central Difference Method')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.legend()
    plt.grid()
    plt.show()

def second_derivative_plot():
    '''
    () -> None
    Creates a scatterplot of the second central difference for the data in 'baseball_height.csv'.
    Preconditions: None
    '''
    # Load the data from the file
    x_data, y_data = load_data()
    
    # Compute the first central difference of the data
    dx, dy = central_diff(x_data, y_data)
    
    # Compute the second central difference from the first difference
    ddx, ddy = central_diff(dx, dy)
    
    # Round all values to account for floating point errors making the plot unbelievably wrong
    dx = np.around(dx, 1)
    dy = np.around(dy, 3)
    ddx = np.around(ddx, 1)
    ddy = np.around(ddy, 3)
    
    # Initialize the third figure
    plt.figure(3)
    # Create a scatter plot of the data with relevant labels and titles
    plt.scatter(ddx, ddy, c='k', marker='o', label='Acceleration of Baseball (m/s\u00B2)')
    plt.title('Acceleration of Baseball Over Time Using Central Difference Method')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s\u00B2)')
    plt.legend()
    plt.grid()
    plt.show()

# Part 2

def trap_integration(x, y):
    '''
    (np.array, np.array) -> np.array
    Approximate the definite integral of y with respect to x using the trapezoidal rule.
    Preconditions: x and y are arrays of the same length.
    '''
    # Compute the width of each subinterval
    delta_x = np.diff(x)

    # Compute the cumulative sum of y, multiplied by the width of the subintervals
    integral = np.cumsum(0.5 * (y[:-1] + y[1:]) * delta_x)

    # Prepend a zero to the start of the integral array, because the integral at the first point is always zero
    integral = np.concatenate(([0], integral))

    return integral

def first_integral_plot():
    '''
    () -> None
    Create a scatterplot of the first integral of the data in 'baseball_height.csv'.
    Preconditions: None
    '''
    # Load the data from the file
    x_data, y_data = load_data()
    
    # Compute the first central difference of the data
    dx, dy = central_diff(x_data, y_data)
    
    # Compute the second central difference from the first difference
    ddx, ddy = central_diff(dx, dy)
    
    # Round all values to account for floating point errors making the plot unbelievably wrong
    dx = np.around(dx, 1)
    dy = np.around(dy, 3)
    ddx = np.around(ddx, 1)
    ddy = np.around(ddy, 3)
    
    # Compute the first integral of the data from the second central difference
    integral = trap_integration(dx[:-1], ddy)
    
    # Initialize the fourth figure
    plt.figure(4)
    # Create a scatter plot of the data with relevant labels and titles
    plt.scatter(dx[:-1], integral, c='k', marker='o', label='Velocity of Baseball (m/s)')
    plt.title('Velocity of Baseball Over Time Using Trapezoidal Rule')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.legend()
    plt.grid()
    plt.show()

def second_integral_plot():
    '''
    () -> None
    Create a scatterplot of the second integral of the data in 'baseball_height.csv'.
    Preconditions: None
    '''
    # Load the data from the file
    x_data, y_data = load_data()
    
    # Compute the first central difference of the data
    dx, dy = central_diff(x_data, y_data)
    
    # Compute the second central difference from the first difference
    ddx, ddy = central_diff(dx, dy)
    
    # Round all values to account for floating point errors making the plot unbelievably wrong
    dx = np.around(dx, 1)
    dy = np.around(dy, 3)
    ddx = np.around(ddx, 1)
    ddy = np.around(ddy, 3)
    
    # Compute the first integral of the data from the second central difference
    i = np.around(trap_integration(dx[:-1], ddy), 3)
    # Compute the second integral of the data from the first integral
    ii = np.around(trap_integration(x_data[:-2], i), 3)
    
    # Initialize the fifth figure
    plt.figure(5)
    # Create a scatter plot of the data with relevant labels and titles
    plt.scatter(x_data[:-2], ii, c='k', marker='o', label='Baseball Height (m)')
    plt.title('Baseball Height Over Time Using Trapezoidal Rule')
    plt.xlabel('Time (s)')
    plt.ylabel('Height (m)')
    plt.legend()
    plt.grid()
    plt.show()
    
def second_integral_plot_adjusted():
    '''
    () -> None
    Create a scatterplot of the second integral of the data in 'baseball_height.csv'.
    Preconditions: None
    '''
    # Load the data from the file
    x_data, y_data = load_data()
    
    # Compute the first central difference of the data
    dx, dy = central_diff(x_data, y_data)
    
    # Compute the second central difference from the first difference
    ddx, ddy = central_diff(dx, dy)
    
    # Round all values to account for floating point errors making the plot unbelievably wrong
    dx = np.around(dx, 1)
    dy = np.around(dy, 3)
    ddx = np.around(ddx, 1)
    ddy = np.around(ddy, 3)
    
    # Compute the first integral of the data from the second central difference
    i = np.around(trap_integration(dx[:-1], ddy), 3) + 4.853    # Constant added to make the graph look as expected; found by dy[0] - i[0]
    # Compute the second integral of the data from the first integral
    ii = np.around(trap_integration(x_data[:-2], i), 3)
    
    # Initialize the sixth figure
    plt.figure(6)
    # Create a scatter plot of the data with relevant labels and titles
    plt.scatter(x_data[:-2], ii, c='k', marker='o', label='Baseball Height (m)')
    plt.title('Baseball Height Over Time with Adjusted Initial Velocity Using Trapezoidal Rule')
    plt.xlabel('Time (s)')
    plt.ylabel('Height (m)')
    plt.legend()
    plt.grid()
    plt.show()


def main():
    '''
    () -> None
    Executes relevant functions for Assignment 9.
    Preconditions: None
    '''
    # Load the data from the file
    x, y = load_data()
    # Print the data
    print(f'Baseball Height Over Time:\n x: {x}\n y: {y}')
    # Show the scatter plot of the data
    height_plot()
    
    # Compute the first central difference of the data
    dx, dy = central_diff(x, y)
    # Print the first central difference
    print(f'First Central Difference of Baseball Height Over Time:\n dx: {dx}\n dy: {dy}')
    # Show the scatter plot of the first central difference
    first_derivative_plot()
    
    # Compute the second central difference from the first difference
    ddx, ddy = central_diff(dx, dy)
    # Print the second central difference
    print(f'Second Central Difference of Baseball Height Over Time:\n ddx: {ddx}\n ddy: {ddy}')
    # Show the scatter plot of the second central difference
    second_derivative_plot()
    
    # Compute the first integral of the data from the second central difference
    i = trap_integration(dx[:-1], ddy)
    # Print the first integral
    print(f'First Integral of Baseball Height Over Time:\n dx: {dx[:-1]}\n dy: {i}')
    # Show the scatter plot of the first integral
    first_integral_plot()
    
    # Compute the second integral of the data from the first integral
    ii = trap_integration(x[:-2], i)
    # Adjust the initial velocity to make the graph look as expected
    ii_adjusted = trap_integration(x[:-2], i + 4.853)
    # Print the second integral
    print(f'Second Integral of Baseball Height Over Time:\n x: {x[:-2]}\n y: {ii}')
    # Print the second integral with adjusted initial velocity
    print(f'Second Integral of Baseball Height Over Time w/ Adjusted Initial Velocity:\n x: {x[:-2]}\n y: {ii_adjusted}')
    # Show the scatter plot of the second integral
    second_integral_plot()
    # Show the scatter plot of the second integral with adjusted initial velocity
    second_integral_plot_adjusted()