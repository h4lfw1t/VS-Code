'''
Filename:       PHY1112_A3_Q1_Template.py
Author:         Patrick Geraghty
Date Created:   2024-01-08
Date Modified:  2024-20-28
Description:    Analyze given temperature data and report the minimum and maximum temperatures.
'''

# daily high temperatures in Ottawa for the month of Septermber 2023
# data retrieved from https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=49568&timeframe=2&StartYear=1840&EndYear=2023&Day=9&Year=2023&Month=9#
high_temperatures = [24.1, 25.0, 29.5, 30.3, 32.5, 32.6, 30.1, 20.2, 22.7, 21.7,
                     24.5, 19.8, 22.0, 16.4, 21.9, 22.9, 24.4, 21.6, 20.2, 18.6,
                     21.3, 22.8, 21.9, 24.8, 21.2, 18.8, 19.2, 22.0, 21.9, 24.0]  # in Celcius
low_temperatures = [08.2, 12.3, 15.6, 18.0, 18.2, 18.8, 20.5, 13.4, 10.6, 12.1,
                    10.8, 11.9, 12.0, 06.6, 04.8, 06.9, 12.5, 13.6, 10.4, 06.9,
                    05.4, 05.6, 07.1, 08.3, 11.4, 07.5, 04.5, 04.5, 09.4, 10.0]  # in Celcius

# 1a. Find the maximum and minimum temperatures for the month of September 2023.

def find_max_temperature(high_temperatures):
    '''
    (list) -> float
    Return the maximum value in the list.
    Precondition: the list is not empty.
    '''
    # define a variable to hold the current maximum value to reference against other values in the list
    current_max = high_temperatures[0]
    # loop through the list and compare each value to the current maximum value
    for i in high_temperatures:
        # if the value is greater than the current maximum value, set the current maximum value to the value
        if i > current_max:
            current_max = i
    # return the current maximum value
    return current_max

def find_min_temperature(low_temperatures):
    '''
    (list) -> float
    Return the minimum value in the list.
    Precondition: the list is not empty.
    '''
    # define a variable to hold the current minimum value to reference against other values in the list
    current_min = low_temperatures[0]
    # loop through the list and compare each value to the current minimum value
    for i in low_temperatures:
        # if the value is less than the current minimum value, set the current minimum value to the value
        if i < current_min:
            current_min = i
    # return the current minimum value
    return current_min

# 1b. Find the average temperature for each day in the month of September 2023.

def find_max_temperature_range(high_temperatures, low_temperatures):
    '''
    (list, list) -> list
    Return the day with the greatest temperature range.
    Precondition: the lists are not empty and have the same length.
    '''
    # define a list to hold the temperature ranges
    temperature_ranges = []
    # loop through the lists and calculate the temperature ranges for each day, appending the value to the list
    for i in range(30):
        temperature_ranges.append((high_temperatures[i] - low_temperatures[i]))
    # set the current maximum value to the first value in the list
    max_range = temperature_ranges[0]
    # loop through the list and compare each value to the current maximum value
    for i in temperature_ranges:
        if i > max_range:
            max_range = i
    # return the current maximum value, and the index of the value in the list, adding 1 to the index value to account for the first day being day 1 and not 0.
    return "The maximum temperature range was " + str(max_range) + "\u00B0C on day " + str(temperature_ranges.index(max_range) + 1) + "."


# 2. Quadratic root solver with complex root keyword argument

# function to find the discriminant of a quadratic equation (for simpler root finding)
def discriminant(a,b,c):
        '''
        (num,num,num) -> num or complex
        Takes three numbers as parameters 'a', 'b', and 'c', and returns the discriminant of the quadratic equation.
        '''
        return b**2 - 4*a*c

# function to find the roots of a quadratic equation
def quad_root_finder(a,b,c, complex_root = False):
        '''
        (num,num,num) - > NoneType
        Takes three numbers as parameters 'a', 'b', and 'c', as well as keyword argument 'complex_roots' and prints the roots of the quadratic equation. If 'complex_roots' is set to True, the function will print the roots as complex numbers (when applicable). By default, 'complex_roots' is set to False. Furthermore, if a is zero, the function will print the root of the linear equation.
        Preconditions: 'a', 'b', and 'c' are all numbers.
        '''
        # check the value of a to avoid division by zero. If a is zero, return the root of the linear equation
        if a == 0:
            print(-c/b)
        # check if the discriminant is positive, negative, complex, or zero and return the roots characteristic of the discriminant
        elif type(discriminant(a,b,c)) == complex:
            if complex_root == True:
                print(complex((-b)/(2*a), + (-(-discriminant(a,b,c))**0.5)/(2*a)), complex((-b)/(2*a), - (-(-discriminant(a,b,c))**0.5)/(2*a)))
            else:
                print(None)
        elif discriminant(a,b,c) < 0:
            # as this is the only case that could produce complex roots, check the complex_root keyword argument to see if the user wants complex roots.
            if complex_root == True:
                print(complex((-b)/(2*a), + (-(-discriminant(a,b,c))**0.5)/(2*a)), complex((-b)/(2*a), - (-(-discriminant(a,b,c))**0.5)/(2*a)))
            # if the user does not want complex roots, print None
            else:
                print(None)
        elif discriminant(a,b,c) == 0:
                print((-b)/(2*a))
        else:
                print((-b + (discriminant(a,b,c)**0.5))/(2*a), (-b - (discriminant(a,b,c)**0.5))/(2*a))