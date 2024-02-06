'''
Filename:       lab5.py
Author:         Patrick Geraghty
Date Created:   2024/02/06
Date Modified:  2024/02/06
Description:    
'''
# Part 1: Factorials

# define a function 'recursive_factorial'
def recursive_factorial(n):
    '''
    (int) -> int
    This function takes an integer n and returns the factorial of n. The function uses recursion to calculate the factorial of n.
    Preconditions: n is an integer
    '''
    # base cases
    # if n is 1, return 1
    if n == 1:
        return 1
    # if n is 0, return 1 (product of no values)
    elif n == 0:
        return 1
    # if n is negative, return an error message
    elif n < 0:
        return "Error: Factorial of negative number is undefined"
    # recursive case
    else:
        return n * recursive_factorial(n-1)

# define a function to test the recursive_factorial function
def factorial_test(test_cases):
    '''
    (list) -> None
    This function takes a list of integers and prints the factorial of each integer in the list and compares it to a long-hand computation of the factorial.
    Preconditions: test_cases is a list of integers
    '''
    # iterate through the test cases
    for i in range(len(test_cases)):
        # set the factorial to 1
        factorial = 1
        # iterate through the range of the test case and multiply the factorial by the value
        for j in range(1, test_cases[i] + 1):
            factorial *= j
        # print the factorial and the comparison as a boolean
        print(f'{test_cases[i]}! = {factorial}, comparison: {factorial == recursive_factorial(test_cases[i])}')


# Part 2: Handling Large Data Sets

import numpy as np

# define a function to load the data
def load_data():
    '''
    () -> np.array
    This function returns a numpy array of the data in the 'weather_data_lab5.csv'.
    Preconditions: filename is a string
    '''
    # load the data from the file using np.genfromtxt. Define necessary columns, skip the header, identify the separator, and define the data type as float
    return np.genfromtxt('weather_data_lab5.csv', usecols=(9,11), skip_header=1, delimiter=',', dtype=float)

# define a function to calculate the weather statistics
def weather_stats():
    '''
    () -> None
    Prints the lowest and highest temperatures as well as the day (0-364) when they occurred. Furthermore, prints the largest difference between the daily high and low in any one day, as well as the day which it occured.
    Preconditions: None
    '''
    # load the data
    data = load_data()
    # define the high and low temperatures
    high = data[:,0]
    low = data[:,1]
    # calculate the difference between the high and low temperatures
    diff = high - low
    # print the statistics
    # use np.nanmin and np.nanmax to ignore NaN values and find the max and min within the high and low lists. Use np.nanargmin and np.nanargmax to find the index of the max and min values.
    print(f'Lowest temperature: {np.nanmin(low)} on day {np.nanargmin(low)}')
    print(f'Highest temperature: {np.nanmax(high)} on day {np.nanargmax(high)}')
    # use np.nanmax to ignore NaN values and find the max difference between high and low. Use np.nanargmax to find the index of the max difference.
    print(f'Largest difference between high and low: {np.nanmax(diff)} on day {np.nanargmax(diff)}')
    