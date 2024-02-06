'''
Filename:       a4_part2.py
Author:         Patrick Geraghty
Date Created:   2024-02-05
Date Modified:  2024-02-05
Description:    
'''
import itertools as it

def for_loop_dice_roller(n):
    '''
    (int) -> list
    Takes an integer n and returns a list of all possible combinations of four n-sided dice rolls.
    Precondition: n is an integer.
    '''
    # Create an empty list to store the combinations.
    combinations = []
    net_sum = []
    # Iterate through the range of n four times.
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    # Append each combination to the list.
                    combinations.append((i+1, j+1, k+1, l+1))
                    # Append the sum of each combination to the list.
                    net_sum.append(i+j+k+l+4)
    # Return the list net_sum and combinations.
    return net_sum, combinations

def average_roll(net_sum):
    '''
    (list) -> float
    Takes a list of net sums and returns the average net sum.
    Precondition: net_sum is a list of integers.
    '''
    # Return the average of the net sums.
    return sum(net_sum) / len(net_sum)

def iter_dice_roller(n):
    '''
    (int) -> list
    Takes an integer n and returns a list of all possible combinations of four n-sided dice rolls.
    Preconditions: n is an integer.
    '''
    # Create an empty list to store the combinations.
    combinations = []
    for_loop_sum = []
    # Iterate through the range of n four times.
    for i in it.product(range(1, n+1), repeat=4):
        # Append each combination to the list.
        combinations.append(i)
        # Append the sum of each combination to the list.
        for_loop_sum.append(sum(i))
    net_sum = sum(map(sum, combinations))
    # Return the list net_sum and combinations.
    return net_sum
