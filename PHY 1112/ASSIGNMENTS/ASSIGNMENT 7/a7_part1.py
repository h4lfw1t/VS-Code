'''
Filename:       a7_part1.py
Author:         Patrick Geraghty
Date Created:   2024-03-04
Date ModifiedL  2024-03-05
Description:    Assignment 7: Question 1. The Weatherperson is Never Exact Enough
'''
import numpy as np
import matplotlib.pyplot as plt

# Question 1: The Weatherperson is Never Exact Enough

def load_March_data():
    '''
    () -> np.array
    This function loads the high and low temperatures for Ottawa in March 2022.
    Preconditions: None
    '''
    return np.genfromtxt('weather_data_lab5.csv', delimiter=',', usecols=(9,11), skip_header=1, dtype=float)[59:90]

def error_array(error=0.1):
    '''
    (float) -> np.array
    This function returns an array of errors for the high and low temperatures in March 2022.
    Preconditions: If error is defined, it is a real number.
    '''
    data = load_March_data()    # load the data
    return np.array(np.abs([data[:,0]*error, data[:,1]*error])) # return the array of errors

def print_error():
    '''
    () -> None
    This function prints the error array for the high and low temperatures in March 2022 as f-strings.
    Preconditions: None
    '''
    data = error_array()        # load the data
    for i in range(len(data)):  # print the error array for each element
        for j in (data[i]):     
            print(f'{j:.2f}', end=', ')

def plot_temperature_data():
    '''
    () -> None
    This function plots the high and low temperatures for Ottawa in March 2022 with error bars.
    Preconditions: high_temperatures and low_temperatures data exist and are both np.arrays of the same length
    '''
    plt.figure(1)
    
    data = load_March_data()        # load the data
    day = np.arange(1,32)           # specify the days of the month
    high_temperatures = data[:,0]   # specify the high temperatures
    low_temperatures = data[:,1]    # specify the low temperatures
    errors = error_array(data)      # specify the errors
    # plot the high and low temperatures with error bars
    plt.errorbar(day, high_temperatures, yerr=np.abs(errors[0]), fmt='ro', capsize=3, label='Highs')
    plt.errorbar(day, low_temperatures, yerr=np.abs(errors[1]), fmt='co', capsize=3, label='Lows')
    # label the plot and show it
    plt.xlabel('Day of the Month')
    plt.ylabel('Temperature (Celsius)')
    plt.title('Monthly High and Low Temperatures for Ottawa in March 2022')
    plt.grid()
    plt.legend()
    plt.show()

def daily_temperature_range():
    '''
    () -> np.array
    This function returns the daily temperature range for Ottawa in March 2022.
    Preconditions: None
    '''
    data = load_March_data()                    # load the data
    high_temperatures = data[:,0]               # specify the high temperatures
    low_temperatures = data[:,1]                # specify the low temperatures
    return high_temperatures - low_temperatures # return the daily temperature range

def range_error():
    '''
    () -> np.array
    This function returns the error for the daily temperature range for Ottawa in March 2022.
    Preconditions: None
    '''
    high_error = error_array()[0]                           # specify the high temperature error
    low_error = error_array()[1]                            # specify the low temperature error
    return np.sqrt(np.abs(high_error**2 - low_error**2))    # return the daily temperature range error

def plot_temperature_range():
    '''
    () -> None
    This function plots the daily temperature range for Ottawa in March 2022 with error bars.
    Preconditions: daily_temperature_range and range_error functions exist
    '''
    plt.figure(2)
    
    day = np.arange(1,32)                   # specify the days of the month
    range_data = daily_temperature_range()  # specify the daily temperature range
    range_errors = range_error()            # specify the daily temperature range error
    # plot the daily temperature range with error bars
    plt.errorbar(day, range_data, yerr=range_errors, fmt='go', capsize=3, label='Temperature Range')
    # label the plot and show it
    plt.xlabel('Day of the Month')
    plt.ylabel('Temperature Range (Celsius)')
    plt.title('Daily Temperature Range for Ottawa in March 2022')
    plt.grid()
    plt.legend()
    plt.show()

def average_daily_temperature():
    '''
    () -> np.array
    This function returns the average daily temperature for Ottawa in March 2022.
    Preconditions: None
    '''
    data = load_March_data()                            # load the data
    high_temperatures = data[:,0]                       # specify the high temperatures
    low_temperatures = data[:,1]                        # specify the low temperatures
    return (high_temperatures + low_temperatures) / 2   # return the average daily temperature

def average_daily_error():
    '''
    () -> np.array
    This function returns the error for the average daily temperature for Ottawa in March 2022.
    Preconditions: None
    '''
    high_error = error_array()[0]                                       # specify the high temperature error
    low_error = error_array()[1]                                        # specify the low temperature error
    return np.sqrt(np.abs(0.25 * high_error**2 + 0.25 * low_error**2))  # return the average daily temperature error

def plot_average_temperature():
    '''
    () -> None
    This function plots the average daily temperature for Ottawa in March 2022 with error bars.
    Preconditions: average_daily_temperature and average_daily_error functions exist
    '''
    plt.figure(3)
    
    day = np.arange(1,32)                       # specify the days of the month
    average_data = average_daily_temperature()  # specify the average daily temperature
    average_errors = average_daily_error()      # specify the average daily temperature error
    # plot the average daily temperature with error bars
    plt.errorbar(day, average_data, yerr=average_errors, fmt='yo', capsize=3, label='Average Temperature')
    # label the plot and show it
    plt.xlabel('Day of the Month')
    plt.ylabel('Temperature (Celsius)')
    plt.title('Average Daily Temperature for Ottawa in March 2022')
    plt.grid()
    plt.legend()
    plt.show()
