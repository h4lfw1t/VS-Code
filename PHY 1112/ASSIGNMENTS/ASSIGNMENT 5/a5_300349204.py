'''
Filename:       a5_300349204.py
Author:         Patrick Geraghty
Date Created:   2024-02-11
Date Modified:  2024-02-11
Description:    Contains functions for Assignment 5 and additional functions. Functions include: 'fibonacci_term', 'fibonacci_sequence_loop', 'fibber_rec', 'fibber_loop', 'recursive_multiplication', 'rec_mult_loop_output', 'velocity', 'position', 'distance_from_origin', 'velocity_magnitude', 'closest_body', and 'fastest_body'. See docstrings for details.
'''

import time as t
import numpy as np

# Fibonacci Frenzy

# define function 'fibonacci_term'
def fibonacci_term(n):
    '''
    (int) -> int
    Returns the nth term of the Fibonacci sequence using recursion.
    Preconditions: n >= 0, n is an integer.
    '''
    # define cases
    if n == 0:                      # if n is 0, return first term
        return 0
    elif n == 1:                    # if n is 1, return second term
        return 1
    else:                           # if n is greater than 1, calculate nth term
                                    # calculate nth term using recursion
        return fibonacci_term(n-1) + fibonacci_term(n-2)

# define function 'fibonacci_sequence_loop'
def fibonacci_sequence_loop(n):
    '''
    (int) -> int
    Returns the nth term of the Fibonacci sequence.
    Precondition: n >= 0, n is an integer.
    '''
    n0 = 0                          # set first term of sequence
    n1 = 1                          # set second term of sequence
    
    # define cases
    if n == 0:                      # if n is 0, return first term
        return n0
    elif n == 1:                    # if n is 1, return second term
        return n1
    else:                           # if n is greater than 1, calculate nth term
                                    # loop through sequence to calculate nth term
        for i in range(2, n+1):     # set range from 2 to n+1 as cases for 0 and 1 are already defined
                                    # calculate nth term
            n2 = n0 + n1
            n0 = n1
            n1 = n2
        # return nth term
        return n2

# simple function to loop through n cases of fibonacci_term
def fibber_rec(x):
    # use time module to measure time
    t0 = t.perf_counter()
    for i in range(x):
        print(fibonacci_term(i))
    t1 = t.perf_counter()
    print(f"Recursion time: {t1-t0}")

# simple function to loop through n cases of fibonacci_sequence_loop
def fibber_loop(x):
    # use time module to measure time
    t0 = t.perf_counter()
    for i in range(x):
        print(fibonacci_sequence_loop(i))
    t1 = t.perf_counter()
    print(f"Loop time: {t1-t0}")



# 2. A Quest for Quality

# define function 'recursive_multiplication'
def recursive_multiplication(a, b):
    '''
    (int, int) -> int
    Returns the product of two integers using recursion.
    Preconditions: a and b are integers.
    '''
    # define base case
    if b == 0:                      # if b is 0, return 0
        return 0
    elif a == 0:                      # if a is 0, return 0
        return 0
    elif a < 0 and b < 0:             # if a and b are both negative, return positive product
        return recursive_multiplication(-a, -b)
    elif a < 0:                       # if a is negative, return negative product
        return -recursive_multiplication(-a, b)
    elif b < 0:                       # if b is negative, return negative product
        return -recursive_multiplication(a, -b)
    else:                           # if b is not 0, calculate product using recursion
        return a + recursive_multiplication(a, b-1)

# define simple loop for test cases
def rec_mult_loop_output(a, b):
    '''
    (int, int) -> None
    Returns the products of a range of two integers using recursion.
    Preconditions: a and b are integers.
    '''
    # note that the range of a is equal to the range of b
    for i in range(a, b):
        for j in range(a, b):
            print(f"{i} * {j} = {recursive_multiplication(i, j)}")



# 3. Rigid Read-In

# define function 'velocity' to contain the data from 'PHY1112_A5_Q3_Velocities.csv' in an array
def velocity():
    '''
    () -> np.array
    Returns an array of velocities containing the relevant data in 'PHY1112_A5_Q3_Velocities.csv'.
    Preconditions: 'PHY1112_A5_Q3_Velocities.csv' is a valid file.
    '''
    # load the data from the file using np.genfromtxt. Define necessary columns, skip the header, identify the separator, and define the data type as float
    return np.genfromtxt('PHY1112_A5_Q3_Velocities.csv', skip_header=1, usecols=(1,2,3), delimiter=',', dtype=float)

# define function 'position' to contain the data from 'PHY1112_A5_Q3_Positions.csv' in an array
def position():
    '''
    () -> np.array
    Returns an array of positions containing the relevant data in 'PHY1112_A5_Q3_Positions.csv'.
    Preconditions: 'PHY1112_A5_Q3_Positions.csv' is a valid file.
    '''
    # load the data from the file using np.genfromtxt. Define necessary columns, skip the header, identify the separator
    return np.genfromtxt('PHY1112_A5_Q3_Positions.csv', skip_header=1, usecols=(1,2,3), delimiter=',', dtype=float)

# define function 'distance_from_origin' to calculate the distance of each body from the origin
def distance_from_origin():
    '''
    () -> np.array
    Returns an array of distances from the origin for each body using data from the 'position()' function.
    Preconditions: None
    '''
    pos_x = position()[:,0]     # set x position to the first column of the position array
    pos_y = position()[:,1]     # set y position to the second column of the position array
    pos_z = position()[:,2]     # set z position to the third column of the position array
    # calculate the distance from the origin using the Pythagorean theorem and return the array
    return np.array([np.sqrt(pos_x[i]**2 + pos_y[i]**2 + pos_z[i]**2) for i in range(len(pos_x))])

# define function 'velocity_magnitude' to calculate the magnitude of the velocity of each body    
def velocity_magnitude():
    '''
    () -> np.array
    Returns an array of the magnitude of the velocity for each body using data from the 'velocity()' function.
    Preconditions: None
    '''
    vel_x = velocity()[:,0]     # set x velocity to the first column of the velocity array
    vel_y = velocity()[:,1]     # set y velocity to the second column of the velocity array
    vel_z = velocity()[:,2]     # set z velocity to the third column of the velocity array
    # calculate the magnitude of the velocity using the Pythagorean theorem and return the array
    return np.array([np.sqrt(vel_x[i]**2 + vel_y[i]**2 + vel_z[i]**2) for i in range(len(vel_x))])

# define function 'closest_body' to find the body closest to the origin
def closest_body():
    '''
    () -> None
    Prints the body closest to the origin and the distance from the origin.
    Preconditions: None
    '''
    distances = distance_from_origin() # set distances to the array of distances from the origin
    # print the body closest to the origin and the distance from the origin using an f-string
    print(f'The closest body to the origin is body {np.argmin(distances) + 1} at a distance of {np.min(distances)}')

# define function 'fastest_body' to find the body with the fastest velocity
def fastest_body():
    '''
    () -> None
    Prints the body with the fastest velocity and the velocity.
    Preconditions: None
    '''
    velocities = velocity_magnitude() # set velocities to the array of magnitudes of the velocity
    # print the body with the fastest velocity and the velocity using an f-string
    print(f'The fastest body is body {np.argmax(velocities) + 1} with a velocity of {np.max(velocities)}')