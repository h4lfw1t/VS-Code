'''
Filename:       lab3.py
Author:         Patrick Geraghty
Date Created:   2023-10-10
Date Modified:  2024-01-23
Description:    Contains a function that categorizes average daily temperatures into 'hot', 'warm', and 'temperate' from a given list. Contains an additional function that returns the roots of a quadratic equation given its 'a', 'b', and 'c' values as parameters.
'''

# daily high temperatures in Ottawa for the month of Septermber 2023
# data retrieved from https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=49568&timeframe=2&StartYear=1840&EndYear=2023&Day=9&Year=2023&Month=9#
temperatures = [24.1, 25.0, 29.5, 30.3, 32.5, 32.6, 30.1, 20.2, 22.7, 21.7,
        24.5, 19.8, 22.0, 16.4, 21.9, 22.9, 24.4, 21.6, 20.2, 18.6, 21.3, 22.8,
        21.9, 24.8, 21.2, 18.8, 19.2, 22.0, 21.9, 24.0] # Celsius

# Part 1
def temp_stats():
        '''
        () -> list or bool
        Counts the number of days the temperature was above 30 C, between 20 C and 30 C, and less than 20 C, listing them as 'hot', 'warm', and 'temperate' respectively. Additionally, it checks if the summation of 'hot', 'warm', and 'temperate' days matches the number of days in 'temperatures'. If the summation does not match, the function returns False.
        Preconditions: predetermined list of temperatures 'temperatures'.
        '''
        # categorize temperatures into blank values (0)
        hot = 0
        warm = 0
        temperate = 0
        
        # iterate through list of temperatures and categorize them into respective categories
        for i in temperatures:
                if i >= 30:
                        hot += 1
                elif 30 > i >= 20:
                        warm += 1
                else:
                        temperate += 1

        # create a list of the categorized temperatures
        stats = [hot, warm, temperate]
        
        # check if the summation of the categorized temperatures matches the number of days in 'temperatures'
        count = 0
        for i in stats:
                count += i
        if count != len(temperatures):
                return False
        # return the list of categorized temperatures only if the count loop passes (does not return False)
        return stats

# Part 2

# function to find the discriminant of a quadratic equation (for simpler root finding)
def discriminant(a,b,c):
        '''
        (num,num,num) -> num or complex
        Takes three numbers as parameters 'a', 'b', and 'c', and returns the discriminant of the quadratic equation.
        '''
        return b**2 - 4*a*c

# function to find the roots of a quadratic equation
def quad_root_finder(a,b,c):
        '''
        (num,num,num) - > tuple or num
        Takes three numbers as parameters 'a', 'b', and 'c', and returns the roots of the quadratic equation.
        Preconditions: 'a', 'b', and 'c' are all numbers.
        '''
        # check if the discriminant is positive, negative, or zero and return the roots characteristic of the discriminant
        if discriminant(a,b,c) < 0:
                return complex((-b)/(2*a), + (-(-discriminant(a,b,c))**0.5)/(2*a)), complex((-b)/(2*a), - (-(-discriminant(a,b,c))**0.5)/(2*a))
        elif discriminant(a,b,c) == 0:
                return (-b)/(2*a)
        else:
                return (-b + (discriminant(a,b,c)**0.5))/(2*a), (-b - (discriminant(a,b,c)**0.5))/(2*a)