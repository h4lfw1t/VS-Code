import math

#####################
# Question 1
#####################

def repeater(s1,s2,n):
    """
    (str,str,int)->str
    Returns a string that is the concatenation of s1 and s2 n times.
    Preconditions: s1 and s2 are strings and n is a positive integer.
    """
    return "_"+((s1+s2)*n)+"_"

#####################
# Question 2
#####################
def roots(a,b,c):
    """
    (float,float,float)->None
    Prints two floats that are the roots of the quadratic equation ax^2+bx+c=0.
    Preconditions: a, b, and c are floats and a != 0. math.sqrt(b**2-4*a*c) > 0.
    """
    print(((-b+math.sqrt(b**2-4*a*c))/(2*a)), ((-b-math.sqrt(b**2-4*a*c))/(2*a)))

#####################
# Question 3
#####################
def real_roots(a,b,c):
    """
    (float,float,float)->bool
    Returns True if the quadratic equation ax^2+bx+c=0 has real roots.
    Preconditions: a, b, and c are floats and a != 0.
    """
    return (b**2-4*a*c)>=0

#####################
# Question 4
#####################
def reverse(x):
    """
    (int)->int
    Returns the reverse digits of x.
    Preconditions: x is a two-digit integer.
    """
    return (x%10)*10+(x//10)