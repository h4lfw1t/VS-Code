import math
radius=float(input("Enter the radius of the circle: "))
def areaOfCircle(radius):
    '''
    (number)-> None
    Precondition: radius>=0
    Given a radius, returns the area of a circle
    '''
    area=areaOfCircle(radius)
    return math.pi*radius**2


print("the area of the circle with radius",radius,"is",area)
