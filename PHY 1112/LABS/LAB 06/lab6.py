'''
Filename:       lab6.py
Author:         Patrick Geraghty
Date Created:   2024-02-13
Date Modified:  2024-02-13
Description:    This file contains the functions for the lab 6 exercises and one additional function. The functions include sin_cosine_plot, tan_plot, f_strings, load_data, year_weather_graph, and july_weather_graph.
'''

import matplotlib.pyplot as plt
import numpy as np
import math as m

def sin_cosine_plot():
    '''
    () -> None
    This function creates a plot of the sine and cosine functions on the same graph.
    Precondition: None
    '''
    # Specify the x-axis values
    x = np.linspace(0, 2*np.pi)

    # Create the figure.
    plt.figure(1)

    # Create the graphs for sin and cosine. Differentiate with color.
    plt.plot(x, np.cos(x), color = 'b', label = 'cos(x)')
    
    plt.plot(x, np.sin(x), color = 'g', label = 'sin(x)')

    # Draw the x-axis and y-axis at y=0 and x=0, respectively. The color is red, the line style is dashed, and the line width is 2.
    plt.hlines(0, 0, 2*np.pi, colors = 'r', linestyles = 'dashed', linewidths = 2)

    # Label the graph
    plt.title('y = cos(x) & y = sin(x)')
    plt.xlabel('x (radians)')
    plt.ylabel('y')

    # Set the x-axis limits
    plt.xlim(0, 2*np.pi)

    # Set the x-axis tick values and labels
    xtick_values = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    xtick_labels = ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
    plt.xticks(xtick_values, xtick_labels)

    # Add a legend to identify the graphs
    plt.legend()
    
    # Add a grid
    plt.grid()

    plt.show()

def tan_plot():
    '''
    () -> None
    This function creates a plot of the tangent function.
    Precondition: None
    '''
    # define the x-axis values and the y-axis values
    x = np.linspace(-np.pi/2, np.pi/2, 1000)
    y = np.tan(x)
    
    # Create the figure
    plt.figure(2)
    # Create the graph for tan(x)
    plt.plot(x, y, color = 'r', label = 'tan(x)')
    # Draw the x-axis and y-axis at y=0 and x=0, respectively. The color is black, the line style is solid, and the line width is 2.
    plt.hlines(0, -np.pi, np.pi, colors = 'k', linestyles = '-', linewidths = 2)
    # Draw the vertical asymptotes at x = -pi/2 and x = pi/2. The color is black, the line style is dashed, and the line width is 2.
    plt.vlines(-np.pi/2, -5, 5, colors = 'k', linestyles = '--', linewidths = 2)
    plt.vlines(np.pi/2, -5, 5, colors = 'k', linestyles = '--', linewidths = 2)
    # Label the graph
    plt.title('y = tan(x)')
    plt.xlabel('x (radians)')
    plt.ylabel('y')
    # Set the x-axis limits and y-axis limits
    plt.xlim(-np.pi, np.pi)
    plt.ylim(-5, 5)
    # Set the x-axis tick values and labels
    xtick_values = [-np.pi/2, 0, np.pi/2]
    xtick_labels = [r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$']
    plt.xticks(xtick_values, xtick_labels)
    # Add a legend to identify the graph
    plt.legend()
    # Add a grid
    plt.grid()
    
    plt.show()

def f_strings():
    '''
    () -> None
    This function demonstrates the use of f-strings.
    Precondition: None
    '''
    # Print the following values using f-strings
    print(f'{m.pi:.6f}')        # math.pi to 6 decimal places
    print(f'{10000.3:.1e}')     # 10000.3 in scientific notation to 1 decimal place
    print(f'0x{733:04X}')       # 733 in hexadecimal with 4 digits
    print(f'{chr(4242)}')       # Unicode character 4242
    print(f'{72.6942:.0f}')     # 72.6942 to 0 decimal places

# define a function to load the data
def load_data():
    '''
    () -> np.array
    This function returns a numpy array of the data in the 'weather_data_lab6.csv'.
    Precondition: filename is a string
    '''
    # load the data from the file using np.genfromtxt. Define necessary columns, skip the header, identify the separator, and define the data type as float
    return np.genfromtxt('weather_data_lab5.csv', usecols=(9,11), skip_header=1, delimiter=',', dtype=float)

# define a function to calculate the weather statistics
def year_weather_graph():
    '''
    () -> None
    Creates a graph of the weather data.
    Precondition: None
    '''
    # load the data
    data = load_data()
    # create the figure
    plt.figure(3)
    # define highs and lows
    highs = data[:,0]
    lows = data[:,1]
    # plot the highs and lows
    plt.plot(highs, label = 'Highs', color = 'r')
    plt.plot(lows, label = 'Lows', color = 'b')
    # define the x-limit
    plt.xlim(1, 365)
    # label the graph
    plt.title('High and Low Temperatures')
    plt.xlabel('Day of the Year')
    plt.ylabel('Temperature (Celcius)')
    # add a legend to identify the graphs
    plt.legend()
    # add a grid
    plt.grid()
    # show the graph
    plt.show()

def july_weather_graph():
    '''
    () -> None
    Creates a graph of the weather data for July.
    Precondition: None
    '''
    # load the data
    data = load_data()
    # create the figure
    plt.figure(4)
    # define the days in July
    days = np.arange(181, 212)
    highs = data[180:211,0]
    lows = data[180:211,1]
    # plot the highs and lows
    plt.plot(days, highs, label = 'Highs', color = 'r')
    plt.plot(days, lows, label = 'Lows', color = 'b')
    # define average highs and lows
    avg_high = np.mean(highs)
    avg_low = np.mean(lows)
    # represent the average highs and lows with a horizontal line
    plt.hlines(avg_high, 181, 211, colors = 'r', linestyles = '--', label = f'Average High ({avg_high:.2f})')
    plt.hlines(avg_low, 181, 211, colors = 'b', linestyles = '--', label = f'Average Low ({avg_low:.2f})')
    # label the graph
    plt.title('High and Low Temperatures in July')
    plt.xlabel('Day of the Year')
    plt.ylabel('Temperature (Celcius)')
    # identify the x-limit
    plt.xlim(181, 211)
    # change x-axis ticks
    xtick_labels = np.arange(1, 32, 2)
    xtick_values = np.arange(181, 212, 2)
    plt.xticks(xtick_values, xtick_labels)
    # define the standard deviations of the highs and lows
    high_std = np.std(highs)
    low_std = np.std(lows)
    # fill the area between the upper and lower standard deviations
    plt.fill_between(days, avg_high + high_std, avg_high - high_std, color = 'r', alpha = 0.2)
    plt.fill_between(days, avg_low + low_std, avg_low - low_std, color = 'b', alpha = 0.2)
    # add a legend to identify the graphs
    plt.legend(fontsize = 'small')
    # add a grid
    plt.grid()
    # show the graph
    plt.show()