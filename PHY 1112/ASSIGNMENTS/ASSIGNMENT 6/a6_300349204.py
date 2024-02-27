'''
Filename:       a6_300349204.py
Author:         Patrick Geraghty
Date Created:   2024-02-20
Date Modified:  2024-02-26
Description:    Conatins functions for Assignment 6. Functions include: 'dice_array', 'hand_histogram_2d6', 'combo_sum', 'unique_combinations', 'unique_occurrences', 'dice_histogram', 'velocity', 'position', 'rigid_position_xy_scatterplot', 'mass', average_speed', 'average_mass', 'average_speed_std_dev', 'average_mass_std_dev', 'x_center_of_mass', 'y_center_of_mass', 'system_center_of_mass', and 'system_scatterplot'. See docstrings for details.
'''

import matplotlib.pyplot as plt
import numpy as np
import itertools as it

# Question 1

# define a function to calculate the sum of two n-sided dice
def dice_array(number_of_dice, number_of_sides):
    '''
    (int, int) -> np.array
    Returns an array of combinations of a number of n-sided dice.
    Preconditions: number_of_dice > 0, number_of_sides > 0, number_of_dice and number_of_sides are integers.
    '''
    # create a list to store all possible combinations of the dice
    combinations = []
    # iterate through the product of the range of the number of sides and the number of dice
    for i in it.product(range(1, number_of_sides+1), repeat=number_of_dice):
        # append the sum of the combination to the list
        combinations.append(i)
        # return the list as an array
    return np.array(combinations)

# define a function to display the histogram of the sum of 2d6 using pre-existing data
def hand_histogram_2d6():
    '''
    () -> None
    Plots a histogram of the sum of two six-sided dice and their occurence using data collected by observation.
    Preconditions: None
    '''
    # define the x and y values for the histogram
    x = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    y = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])
    # initialize a new figure for the plot
    plt.figure(1)
    # plot the histogram as a bar graph
    plt.bar(x, y, label = '2d6 combinations')
    # set the title and labels for the plot
    plt.title('Histogram of the occurences of dice combinations of 2d6')
    plt.xlabel('Sum of dice')
    plt.ylabel('Occurences')
    # set the x-axis ticks to the values of the dice combinations (matplot lib shows only even values by default, so we need to set the ticks manually)
    plt.xticks(x)
    # display the legend
    plt.legend()
    # display the plot
    plt.show()

def combo_sum(array):
    '''
    (np.array) -> np.array
    Returns an array of the sums of the rows of the input array.
    Preconditions: array is a 2D numpy array.
    '''
    # return the sum of the rows of the array
    return np.sum(array, axis=1)

def unique_combinations(array):
    '''
    (np.array) -> np.array
    Returns an array of the unique combinations of the input array.
    Preconditions: array is a 1D numpy array.
    '''
    # return the unique values of the input array
    return np.unique(array)

def unique_occurrences(array):
    '''
    (np.array) -> np.array
    Returns an array of the occurrences of the unique values of the input array.
    Preconditions: array is a 1D numpy array.
    '''
    # define the occurences of the unique values (which are equal to the index number) of the input array
    bin_occurences =  np.bincount(array)
    # simplify the array to remove the 0 values and return result
    return bin_occurences[bin_occurences != 0]

def dice_histogram(number_of_dice, number_of_sides):
    '''
    () -> None
    Plots a histogram of the unique sums of m n-sided dice combinations and the frequency of their occurences.
    Preconditions: None
    '''
    # define the x and y values for the histogram
    x = unique_combinations(combo_sum(dice_array(number_of_dice, number_of_sides)))
    y = unique_occurrences(combo_sum(dice_array(number_of_dice, number_of_sides)))
    # initialize a new figure for the plot
    plt.figure(2)
    # plot the histogram as a bar graph
    plt.bar(x, y, label='{}d{} combinations'.format(number_of_dice, number_of_sides))
    # set the title and labels for the plot
    plt.title('Histogram of the occurences of dice combinations of {}d{}'.format(number_of_dice, number_of_sides))
    plt.xlabel('Sum of dice')
    plt.ylabel('Occurences')
    # set the x-axis ticks to the values of the dice combinations (matplot lib shows only even values by default, so we need to set the ticks manually)
    plt.xticks(x)
    # display the legend
    plt.legend()
    # display the plot
    plt.show()

# Question 2

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

def rigid_position_xy_scatterplot():
    '''
    () -> None
    Plots a scatterplot of the x-y position data from the 'PHY1112_A5_Q3_Positions.csv' and 'PHY1112_A5_Q3_Velocities.csv' files.
    Preconditions: None
    '''
    # initialize a new figure for the plot
    plt.figure(3)
    # plot the scatterplot of the position and velocity data
    x = position()[:,0]
    y = position()[:,1]
    plt.scatter(x, y, label='Rigid Body Position', color='black', marker='o', s=5)
    # set the title and labels for the plot
    plt.title('Scatterplot of x-y position data')
    plt.xlabel('x position')
    plt.ylabel('y position')
    # display the legend
    plt.legend()
    # display the plot
    # plt.show()

# define function to read mass data from 'PHY1112_A6_Q2_Masses.csv'
def mass():
    '''
    () -> np.array
    Returns an array of masses containing the relevant data in 'PHY1112_A6_Q2_Masses.csv'.'
    Preconditions: 'PHY1112_A6_Q2_Masses.csv' is a valid file.
    '''
    # load the data from the file using np.genfromtxt. Define necessary columns, skip the header, identify the separator, and define the data type as float
    return np.genfromtxt('PHY1112_A6_Q2_Masses.csv', skip_header=1, usecols=(1), delimiter=',', dtype=float)

# import velocity_magnitude from a5_300349204.py for later use
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

# define function average_speed to calculate the average speed of the bodies using the data from velocity_magnitude
def average_speed():
    '''
    () -> float
    Returns the average speed of the bodies using the data from the 'velocity()' function.
    Preconditions: None
    '''
    # return the average speed of the bodies using the magnitude of the velocity and the number of bodies
    return np.mean(velocity_magnitude())

# define function average_mass to calculate the average mass of the bodies using the data from mass
def average_mass():
    '''
    () -> float
    Returns the average mass of the bodies using the data from the 'mass()' function
    Preconditions: None
    '''
    # return the average mass of the bodies using the mass array
    return np.mean(mass())

# define function average_speed_std_dev to calculate the standard deviation of the average speed of the bodies using the data from velocity_magnitude
def average_speed_std_dev():
    '''
    () -> float
    Returns the standard deviation of the average speed of the bodies using the data from the 'velocity()' function.
    Preconditions: None
    '''
    # return the standard deviation of the average speed of the bodies using the magnitude of the velocity
    return np.std(velocity_magnitude())

# define function average_mass_std_dev to calculate the standard deviation of the average mass of the bodies using the data from mass
def average_mass_std_dev():
    '''
    () -> float
    Returns the standard deviation of the average mass of the bodies using the data from the 'mass()' function
    Preconditions: None
    '''
    # return the standard deviation of the average mass of the bodies using the mass array
    return np.std(mass())

# define function x_center_of_mass to calculate the x-coordinate of the center of mass of the overall system using the data from mass and position
def x_center_of_mass():
    '''
    () -> float
    Returns the x-coordinate of the center of mass of the overall system using the data from the 'mass()' and 'position()' functions.
    Preconditions: None
    '''
    # calculate the x-coordinate of the center of mass
    return np.sum(mass() * position()[:,0]) / np.sum(mass())

# define function y_center_of_mass to calculate the y-coordinate of the center of mass of the overall system using the data from mass and position
def y_center_of_mass():
    '''
    () -> float
    Returns the y-coordinate of the center of mass of the overall system using the data from the 'mass()' and 'position()' functions.
    Preconditions: None
    '''
    # calculate the y-coordinate of the center of mass
    return np.sum(mass() * position()[:,1]) / np.sum(mass())

# define function system_center_of_mass to display the x and y coordinates of the center of mass of the overall system on the plot
def system_center_of_mass():
    '''
    () -> None
    Prints the x and y coordinates of the center of mass of the overall system on the plot.
    Preconditions: None
    '''
    
    x = x_center_of_mass()
    y = y_center_of_mass()
    # # initialize the original figure for the plot
    plt.figure(3)
    # plot the center of mass on the scatterplot
    plt.scatter(x, y, label='System Center of Mass', color='red', marker='s', s=100)
    # show legend
    plt.legend()
    # display the plot
    # plt.show()

# define function system_scatterplot to plot the scatterplot of the x-y position data from the 'PHY1112_A5_Q3_Positions.csv' and 'PHY1112_A5_Q3_Velocities.csv' files, as well as the center of mass of the system
def system_scatterplot():
    '''
    () -> None
    Plots a scatterplot of the x-y position data from the 'PHY1112_A5_Q3_Positions.csv' and 'PHY1112_A5_Q3_Velocities.csv' files, as well as the center of mass of the system.
    Preconditions: None
    '''
    # call the rigid_position_xy_scatterplot function to plot the position of each individual body
    rigid_position_xy_scatterplot()
    # call the system_center_of_mass function to plot the center of mass of the system
    system_center_of_mass()
    # show the plot
    plt.show()