'''
Filename:       a4_part2.py
Author:         Patrick Geraghty
Date Created:   2024-02-05
Date Modified:  2024-02-05
Description:    
'''
# Import the itertools and time modules.
import itertools as it
import time as t

# Define a function to roll four n-sided dice using a for loop.
def for_loop_dice_roller(n):
    '''
    (int) -> list, list
    Takes an integer n and returns a list of all possible combinations of four n-sided dice rolls.
    Precondition: n is an integer.
    '''
    # Create an empty list to store the combinations and a list to store the net sum of each combination.
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

# Define a general function to calculate the average of a list of net sums.
def average_roll(net_sum):
    '''
    (list) -> float
    Takes a list of net sums and returns the average net sum.
    Precondition: net_sum is a list of integers.
    '''
    # Return the average of the net sums.
    return sum(net_sum) / len(net_sum)

# Define a function to roll four n-sided dice using the itertools module.
def iter_dice_roller(n):
    '''
    (int) -> list, list
    Takes an integer n and returns a list of all possible combinations of four n-sided dice rolls.
    Preconditions: n is an integer.
    '''
    # Create an empty list to store the combinations and a list to store the net sum of each combination.
    combinations = []
    net_sum = []
    # Iterate through the range of n four times.
    for i in it.product(range(1, n+1), repeat=4):
        # Append each combination to the list.
        combinations.append(i)
        # Append the sum of each combination to the list.
        net_sum.append(sum(i))
    # Return the list net_sum and combinations.
    return net_sum, combinations

# Test the functions.

# Initiate a for loop to test the functions for 10, 20, and 50-sided dice.
for n in [10, 20, 50]:
    # Record the time it takes to run the for loop functions.
    t0_for = t.perf_counter()
    for_loop_dice_roller(n)
    average_roll(for_loop_dice_roller(n)[0])    # Note that the average_roll function takes the first element of the tuple returned by for_loop_dice_roller as that is the element which contains the net sum of each combination.
    t1_for = t.perf_counter()
    
    # Record the time it takes to run the itertools functions.
    t0_iter = t.perf_counter()
    iter_dice_roller(n)
    average_roll(iter_dice_roller(n)[0])    # Note that the average_roll function takes the first element of the tuple returned by for_loop_dice_roller as that is the element which contains the net sum of each combination.
    t1_iter = t.perf_counter()

    # Print the stats for each n-sided dice.
    print(f'Stats for {n}-sided dice:')
    print(f'Total number of combinations: {len(iter_dice_roller(n)[1])}')
    print(f'For loop time: {t1_for - t0_for}')
    print(f'Itertools time: {t1_iter - t0_iter}')
    print()
