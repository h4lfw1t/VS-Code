'''
Filename:       a5_300349204.py
Author:         Patrick Geraghty
Date Created:   2024-02-11
Date Modified:  2024-02-11
Description:    
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

