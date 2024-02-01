'''
Filename:       a4_300349204.py
Author:         Patrick Geraghty
Date Created:   2024-02-01
Date Modified:  2024-02-01
Description:    Contains the Vector3 class, which initializes a 3D vector and contains methods to calculate the magnitude, addition, subtraction, inner product, and angle (rad and deg) between two vectors.
'''
# Begin by importing the math module. Import as m for brevity.
import math as m

# Define the Vector3 class.
class Vector3:
    # Initialize the class with x, y, and z coordinates.
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # Define the __str__ method to return the vector as a string.
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    
    # Define the magnitude method to return the magnitude of the vector.
    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    # Define the addition and subtraction methods to return the sum and difference of two vectors, respectively.
    # Addition = (x1+x2, y1+y2, z1+z2), Subtraction = (x1-x2, y1-y2, z1-z2)
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    # Define the inner_product method to return the inner product of two vectors.
    # Inner product = x1*x2 + y1*y2 + z1*z2
    def inner_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    # Define the angle_between_rad method to return the angle between two vectors in radians.
    # Angle = arccos((a * b) / (magnitude(a) * magnitude(b)))
    def angle_between_rad(self, other):
        return m.acos(self.inner_product(other) / (self.magnitude() * other.magnitude()))
    
    # Convert the angle between two vectors from radians to degrees.
    # Angle = degrees(angle_between_rad)
    # Why do math when you can just use the math module?
    def angle_between_deg(self, other):
        return m.degrees(self.angle_between_rad(other))