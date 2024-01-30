'''
Filename:       lab4.py
Author:         Patrick Geraghty
Date Created:   2023-01-30
Date Modified:  2023-01-30
Description:    
'''
# Import math module for square root and pi per lab instructions. Import as m for brevity.
import math as m

class Vector2:
    # Initialize the class with the x and y coordinates
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
    # Define the string representation of the class
    def __str__(self):
        return '[' + str(self.x) + ', ' + str(self.y) + ']'
    # Define a method to represent the polar magnitude of the class
    def magnitude(self):
        return m.sqrt(self.x**2 + self.y**2)
    # Define a method to represent the polar angle of the class
    def angle_from_x_axis(self):
        if m.atan2(self.y, self.x) < 0:
            return m.atan2(self.y, self.x) + 2*m.pi
        return m.atan2(self.y, self.x)
    # Define a method to represent the polar representation of the class
    def polar_representation(self):
        return [self.magnitude(), self.angle_from_x_axis()]

# Define the test cases
a = Vector2(1, 0)
b = Vector2(3.2, 3.2)
c = Vector2(-1, -5.5)
d = Vector2(0, 0)
e = Vector2(3, 9j)

# Simple loop to print test cases, excluding error case
for i in [a, b, c, d]:
    print(i)
    print(str(i.polar_representation()))
    print()

# Try to print the error case, and print the error message
try:
    print(e)
    print(str(e.polar_representation()))
except TypeError:
    print('Error: Cannot convert complex number to polar representation')
