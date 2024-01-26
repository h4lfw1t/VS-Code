import math

def onlyVowels(s):
    '''
    (str) -> str
    Given a string 's', return a string containing only the vowels in 's'.
    >>> onlyVowels('hello')
    'eo'
    >>> onlyVowels('smrt')
    ''
    Preconditions: s is a string
    '''
    vowels = ''
    for ch in s:
        if ch in 'aeiouAEIOU':
            vowels += ch
            
    return vowels


# The sequence range() returns a sequence of numbers from 0 to n-1. Remember that in python, the first index of a sequence is 0, thus a range of 10 includes 10 numbers, from 0 to 9.
for i in range(5):
    print(i)
    # prints 0, 1, 2, 3, 4

# The sequence range(a, b) returns a sequence of numbers from a to b-1.
for i in range(2, 5):
    print(i)
    # prints 2, 3, 4
    
# The sequence range(a, b, c) returns a sequence of numbers from a to b-1, with a step of c.
for i in range(0, 10, 2):
    print(i)
    # prints 0, 2, 4, 6, 8

#NOTE: range() does not work with floats. If you want to use floats, use the numpy function arange() instead.
# To count a range backwards, use a negative step. Ex: range(10, 0, -1)

# You can use range() to iterate over a string.
s = 'abcde'
for i in range(5):
    print(s[i])
    # prints a, b, c, d, e

