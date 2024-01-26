# Family name: Vida Dujmovic 
# Student number:  123456
# Course: IT1 1120 
# Assignment Number 1
# year 2020

import turtle 

########################
# Question 1
########################

def area_of_triangle(base, height):
     ''' (number,number)->number
     Returns the area of a triangle with a given base and height
     Precondition: base and height are non-negative numbers
     '''
     return base*height/2

#######################
# Question 2
#######################

def area_of_triangle_nice_print(base, height):
     '''(number,number)->None
      Prints a message about the area of a triangle with a given base and height
      Precondition: base and height are non-negative numbers
     '''
     print("A triangle of a base", base,"and height", height, "has area", area_of_triangle(base,height) )


#######################
# Question 3
#######################
     

def draw_smily_face():
     '''()->None
     Draws a simlly face using turtle graphics'''
     s=turtle.Screen() 
     t=turtle.Turtle() 

     # since this starts with # it is just a comment and thus ignored by python interpreter

     # draw the head, i.e. circle of radius 70  
     t.circle(70)

     #move the pen
     t.penup()
     t.goto(15, 80)
     t.pendown()

     # draw right eye as a rectangle
     t.forward(20)
     t.left(90)
     t.forward(20)
     t.left(90)
     t.forward(20)
     t.left(90)
     t.forward(20)

     #move the pen
     t.up()
     t.goto(-15, 80)
     t.pendown()

     #make the pen face up
     t.setheading(90) 

     # draw left eye as a rectangle
     t.forward(20)
     t.left(90)
     t.forward(20)
     t.left(90)
     t.forward(20)
     t.left(90)
     t.forward(20)

     #make the pen
     t.up()
     t.goto(-15, 35)
     t.pendown()

     # draw a smile as a half circle
     t.setheading(-45)
     t.circle(30,90)

     s.exitonclick()
