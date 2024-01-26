import math

##############################################
# Exercise 1
##############################################

def ah(l,x,y):
    '''
    
    Given a list 'l', and two integers 'x' and 'y', return two numbers such that the first is the number of elements between x and y in l and the second number is the minimum element of l between x and y.
    >>> l = [5, 1, -2.5, 10, 13, 8]
    >>> ah[l, 2, 11]
    (3,5)
    Preconditions: l is a list of numbers, x and y are numbers such that x <= y.
    '''
    count = 0
    least = math.inf
    for i in l:
        if x <= i <= y:
            count += 1
            if i < least:
                least = i
    return (count, least)

##############################################
# Exercise 2
##############################################

def is_perfect(x):
    '''
    (int) -> bool
    Given an integer 'x', return True if x is a perfect number (the sum of its factors excluding x == x) and False otherwise.
    Preconditions: x is an integer.
    '''
    div = 0
    for i in range(1, x):
        if x % i == 0:
            div += i
    return div == x

def finder():
    '''
    () -> NoneType
    Looks for all perfect numbers between 1 and 35000000.
    Preconditions: None
    '''
    for i in range(1, 10000):
        if is_perfect(i):
            print(i)

##############################################
# Exercise 3a
##############################################

def arithmetic(l):
    '''
    (list of numbers) -> bool
    Given a list 'l', return True if l is an arithmetic sequence and False otherwise.
    Preconditions: l is a list of numbers.
    '''
    diff = l[1] - l[0]
    for i in range(len(l)-1):
        if l[i+1] - l[i] != diff:
            return False
    return True

##############################################
# Exercise 3b
##############################################

def is_sorted(l):
    '''
    (list) -> bool
    Given a list 'l', return True if l is sorted in ascending order and False otherwise.
    Preconditions: l is a list of numbers.
    '''
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            return False
    return True