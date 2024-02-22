'''
Filename:       a6_300349204.py
Author:         Patrick Geraghty
Date Created:   2024-02-20
Date Modified:  2024-02-20
Description:    
'''

import matplotlib.pyplot as plt
import numpy as np
import itertools as it

# Question 1

def dice_array(number_of_dice, number_of_sides):
    '''
    (int, int) -> np.array
    Returns an array of combinations of a number of n-sided dice.
    Preconditions: number_of_dice > 0, number_of_sides > 0, number_of_dice and number_of_sides are integers.
    '''
    combinations = []
    for i in it.product(range(1, number_of_sides+1), repeat=number_of_dice):
        combinations.append(i)
    return np.array(combinations)