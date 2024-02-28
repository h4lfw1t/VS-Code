'''
Filename:       lab7.py
Author:         Patrick Geraghty
Date Created:   2024-02-27
Date Modified:  2024-02-27
Description:    
'''
import numpy as np
import matplotlib.pyplot as plt

# Part 1

# import given plot program as a function and make changes for March
def temperature_plot():
    '''
    () -> None
    This function plots the high and low temperatures for Ottawa in March 2022.
    Preconditions: high_temperatures and low_temperatures data exist and are both np.arrays of the same length
    '''
    #initialize the figure
    plt.figure(1)
    # specify the month and the days of the month
    month = "March 2022"
    day = range(1,32)
    measurement_error = 1.5 # +/- in degrees Celsius
    # specify the high and low temperatures so that they 'exist'
    high_temperatures = (load_data()[:,0])[59:90]
    low_temperatures = (load_data()[:,1])[59:90]

    plt.plot(day, high_temperatures, 'r', label="Highs") 
    plt.plot(day, low_temperatures,  'b', label="Lows")

    # the plot_errors function called below is to be defined by the student
    plot_errors(day, high_temperatures, measurement_error, 'mistyrose', "Highs Uncertainty") 
    plot_errors(day, low_temperatures, measurement_error, 'lightblue', "Lows Uncertainty") 

    plt.title(f"High and Low Temperatures for Ottawa in {month}")
    plt.xlabel("Day of the Month")
    plt.ylabel("Temperature (Celcius)")
    plt.xlim(1,day[-1])
    plt.grid()
    plt.legend()
    plt.show()

# define a function to load the necessary data
def load_data():
    '''
    () -> np.array
    This function loads the high and low temperatures for Ottawa in 2022.
    Preconditions: None
    '''
    return np.genfromtxt('weather_data_lab5.csv', usecols=(9,11), skip_header=1, delimiter=',', dtype=float)

# define a function to plot the errors
def plot_errors(day, temperature, measurement_error, color, label):
    '''
    (range, np.array, float) -> None
    This function plots the errors as a shaded region for each day in the given temperature data.
    Preconditions: day and error are numbers, temperature is an np.array.
    '''
    # calculate the upper and lower bounds of the error
    upper_bound = temperature + measurement_error
    lower_bound = temperature - measurement_error
    # fill the area between the upper and lower bounds
    plt.fill_between(day, upper_bound, lower_bound, color=color, label=label)

# Part 2

# import code from lab worksheet
def line(x, intercept, slope):
    return slope*x + intercept

# define a function to plot the linear fits
def linear_fit(day, b, m, label, color):
    # plot the fits
    plt.plot(day, line(day, b, m), color, 
            label=f"{label} fit to a line with m={m:.2f} and b={b:.2f}")

# clone temperature_plot() and edit to account for linear fits
def temperature_plot_with_fits():
    '''
    () -> None
    This function plots the high and low temperatures for Ottawa in March 2022.
    Preconditions: high_temperatures and low_temperatures data exist and are both np.arrays of the same length
    '''
    #initialize the figure
    plt.figure(2)
    # specify the month and the days of the month
    month = "March 2022"
    day = range(1,32)
    measurement_error = 1.5 # +/- in degrees Celsius
    # specify the high and low temperatures so that they 'exist'
    high_temperatures = (load_data()[:,0])[59:90]
    low_temperatures = (load_data()[:,1])[59:90]

    plt.plot(day, high_temperatures, 'r', label="Highs") 
    plt.plot(day, low_temperatures,  'b', label="Lows")

    # the plot_errors function called below is to be defined by the student
    plot_errors(day, high_temperatures, measurement_error, 'mistyrose', "Highs Uncertainty") 
    plot_errors(day, low_temperatures, measurement_error, 'lightblue', "Lows Uncertainty") 
    
    # define the linear fits
    b_highs, m_highs = np.polynomial.polynomial.polyfit( day, high_temperatures, 1 )
    b_lows,  m_lows  = np.polynomial.polynomial.polyfit( day, low_temperatures,  1 )

    # plot the linear fits
    linear_fit(day, b_highs, m_highs, 'Highs', 'r--')
    linear_fit(day, b_lows, m_lows, 'Lows', 'b--')
    
    plt.title(f"High and Low Temperatures for Ottawa in {month}")
    plt.xlabel("Day of the Month")
    plt.ylabel("Temperature (Celcius)")
    plt.xlim(1,day[-1])
    plt.grid()
    plt.legend()
    plt.show()

# Part 3

# define functions to calculate gravitational force and normal force on an incline
def gravitational_force(mass, base, height):
    '''
    (int, int, int) -> np.array
    Calculates the gravitational force vector acting on an object on an inclined surface given the objects mass, and the base and height lengths oh the inclined surface. The x and y vector coordinates are given with the surface representing the positive x-axis and perpendicular to the surface representing the positive y-axis.
    Preconditions: mass, base, and height are all numbers, the mass is positioned at the topmost point of the surface.
    '''
    angle = np.arctan(height/base)
    return mass*9.8*np.array([-np.sin(angle), -np.cos(angle)])

# define a function to calculate the normal force
def normal_force(mass, base, height):
    '''
    (int, int, int) -> np.array
    Calculates the normal force vector acting on an object on an inclined surface given the objects mass, and the base and height lengths oh the inclined surface.
    Preconditions: mass, base, and height are all numbers, the mass is positioned at the topmost point of the surface.
    '''
    # use standard equation for normal force Fn = mg*cos(angle) where g is the acceleration due to gravity (9.8 m/s^2)
    # note that the x component is 0 because the normal force is perpendicular to the surface (solely the y-axis)
    angle = np.arctan(height/base)
    return mass*9.8*np.array([0, np.cos(angle)])

# define a function to calculate the acceleration of the mass
def acceleration(mass, base, height):
    '''
    (int, int, int) -> np.array
    Calculates the acceleration vector acting on an object on an inclined surface given the objects mass, and the base and height lengths oh the inclined surface. The x and y vector coordinates are given with the surface representing the positive x-axis and perpendicular to the surface representing the positive y-axis.
    Preconditions: mass, base, and height are all numbers, the mass is positioned at the topmost point of the surface.
    '''
    # use standard equation for acceleration a = (Fg + Fn)/m
    return (gravitational_force(mass, base, height) + normal_force(mass, base, height))/mass

# define a function to calculate the frictional force vector
def frictional_force(mass, base, height, friction_coefficient):
    '''
    (int, int, int, float) -> np.array
    Calculates the frictional force vector acting on an object on an inclined surface given the objects mass, and the base and height lengths oh the inclined surface. The x and y vector coordinates are given with the surface representing the positive x-axis and perpendicular to the surface representing the positive y-axis.
    Preconditions: mass, base, and height are all numbers, the mass is positioned at the topmost point of the surface.
    '''
    # use standard equation for frictional force Ff = -u*|Fn|, use np.linalg.norm to calculate the magnitude of the normal force
    return np.array([-friction_coefficient*np.linalg.norm(normal_force(mass, base, height)), 0])

# define a function to calculate acceleration of the mass taking friction into consideration
def acceleration_with_friction(mass, base, height, friction_coefficient):
    '''
    (int, int, int, float) -> np.array
    Calculates the acceleration vector acting on an object on an inclined surface given the objects mass, and the base and height lengths oh the inclined surface. The x and y vector coordinates are given with the surface representing the positive x-axis and perpendicular to the surface representing the positive y-axis.
    Preconditions: mass, base, and height are all numbers, the mass is positioned at the topmost point of the surface.
    '''
    # use standard equation for acceleration with friction a = (Fg + Fn - Ff)/m
    return (gravitational_force(mass, base, height) + normal_force(mass, base, height))/mass - frictional_force(mass, base, height, friction_coefficient)/mass

# define a function to calculate the velocity of the mass after t seconds
def velocity_wrt_time(mass, base, height, friction_coefficient, t):
    '''
    (int, int, int, float, int) -> np.array
    Calculates the velocity vector acting on an object on an inclined surface given the objects mass, and the base and height lengths oh the inclined surface. The x and y vector coordinates are given with the surface representing the positive x-axis and perpendicular to the surface representing the positive y-axis.
    Preconditions: mass, base, and height are all numbers, the mass is positioned at the topmost point of the surface.
    '''
    # use standard equation for velocity v = at
    return acceleration_with_friction(mass, base, height, friction_coefficient)*t