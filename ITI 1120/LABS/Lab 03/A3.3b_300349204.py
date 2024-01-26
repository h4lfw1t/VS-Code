# Course: ITI 1120
# Assignment number: 
# Geraghty, Patrick
# 300349204

def is_divisible(m, n):
    '''
    (int, int) -> bool
    Return whether or not the first number is divisible by the second.
    Preconditions: both numbers are positive integers
    '''
    return m%n == 0

def is_divisible23n8(l):
    '''
    (int) -> string
    Return whether or not the input l is divisible by 2 or 3 but not 8.
    Preconditions: l is a positive integer
    '''
    if is_divisible(l, 8) == True or (is_divisible(l, 2) == False and is_divisible(l, 3) == False):
        return "It is not true that " + str(l) + " is divisible by 2 or 3 but not 8."
    else:
        return "It is true that " + str(l) + " is divisible by 2 or 3 but not 8."
l = int(input("Enter a positive integer: "))
print(is_divisible23n8(l))