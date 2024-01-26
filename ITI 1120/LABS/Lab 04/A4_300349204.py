import math
import random

##############################################
# Task 1
##############################################


def stringer():
    s1 = 'good'
    s2 = 'bad'
    s3 = 'silly'
    # a) 'll' appears in s3
    print('ll' in s3)
    # b) the blank space does not appear in s1
    print(' ' not in s1)
    # c) the concatenation of s1, s2, and s3
    print(s1 + s2 + s3)
    # d) the blank space appears in the concatenation of s1, s2, and s3
    print(' ' in s1 + s2 + s3)
    # e) the concatenation of 10 copies of s3
    print(s3 * 10)
    # f) the total number of characters in concatenation of s1, s2, s3
    print(len(s1 + s2 + s3))

##############################################
# Task 2
##############################################


def slicer():
    aha = 'abcdefgh'
    # a) 'abcd'
    print(aha[:4])
    # b) 'def'
    print(aha[3:5])
    # c) 'h'
    print(aha[-1])
    # d) 'fg'
    print(aha[5:7])
    # e) 'defgh'
    print(aha[3:])
    # f) 'fgh'
    print(aha[5:])
    # g) 'adg'
    print(aha[::3])
    # h) 'be'
    print(aha[1:5:3])

##############################################
# Task 3
##############################################


def cities():
    s = '''It was the best of times, it was the worst of times; 
    it was the age of wisdom, it was the age of foolishness; 
    it was the epoch of belief, it was the epoch of incredulity; 
    it was ...'''
    # a) sequence 'newS' produces copy with '.' ',' ';' and '\n' removed
    newS = s.replace('.', '').replace(
        ',', '').replace(';', '').replace('\n', '')
    print(newS)
    # b) remove excess spaces from newS
    newS = newS.replace('  ', '')
    print(newS)
    # c) make newS all lower case
    newS = newS.lower()
    print(newS)
    # d) compute # of occurences 'it was' in newS
    print(newS.count('it was'))
    # e) replace 'was' with 'is' in newS
    newS = newS.replace('was', 'is')
    print(newS)

##############################################
# Exercise 2
##############################################


def mess(phrase):
    '''
    (str) -> str
    Returns a string where each character that is one of the 8 last consonants of the alphabet is capitalized and each space is replaced by '-'.
    Precondition: s is a string of at least one character.
    >>> mes('Random access memory  .')
    'Random-acceSS--memoRY--.'
    >>> mess('central processing   unit.')
    'central-proceSSinG---unIT.'
    '''
    for i in phrase:
        if i in 'rstvwxyz':
            phrase = phrase.replace(i, i.upper())
        if i == ' ':
            phrase = phrase.replace(i, '-')
    return phrase


##############################################
# Exercise 4
##############################################

def triangle(n):
    '''
    (int) -> NoneType
    Prints a triangle of $'s with n rows.
    Precondition: n is a positive integer.
    '''
    n = int(input('Enter a positive integer: '))
    for i in range(n):
        print('$' * (i + 1))
        
##############################################
# Exercise 5
##############################################

def factor():
    '''
    (int) -> NoneType
    Prints the factors of a positive integer n.
    Precondition: n is a positive integer.
    '''
    n = int(input('Enter a positive integer: '))
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

def prime():
    '''
    (int) -> NoneType
    Prints whether or not a positive integer n is prime.
    Precondition: n is a positive integer.
    '''
    n = int(input('Enter a positive integer: '))
    for i in range(2, n):
        if n % i == 0:
            print('Not prime')
            break
    else:
        print('Prime')