'''
Filename:       part2.py
Author:         Patrick Geraghty
Date Created:   2024-01-24
Date Modified:  2024-01-24
Description:    Contains a program that takes the 'a', 'b', and 'c' values of a quadratic equation as parameters, and returns the roots of the equation as well as the type of roots (real and distinct, real and equal, or complex).
'''

# Input for variables 'a', 'b', and 'c'
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Print statements for the roots of the quadratic equation dependant on the discriminant
if (b**2-4*a*c) < 0:
    print(complex((-b)/(2*a), + (-(-(b**2-4*a*c))**0.5)/(2*a)), complex((-b)/(2*a), - (-(-(b**2-4*a*c))**0.5)/(2*a)))
    print("The roots are complex.")
elif (b**2-4*a*c) == 0:
    print((-b)/(2*a))
    print("The roots are real and equal.")
else:
    print((-b + ((b**2-4*a*c)**0.5))/(2*a), (-b - ((b**2-4*a*c)**0.5))/(2*a))
    print("The roots are real and distinct.")