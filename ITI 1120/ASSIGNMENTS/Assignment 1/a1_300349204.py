# Family name: Patrick Geraghty
# Student number:  300349204
# Course: ITI 1120
# Assignment Number 1
# year 2020

import math

########################
# Question 1
########################

def f_to_k(t): 
    '''
    (number)->(float)
    Returns the temperature in Kelvin given a temperature in Fahrenheit (t)
    Precondition: t is a float or int
    '''
    return (t-32)*(5/9)+273.15

########################
# Question 2
########################

def poem_generator():
    '''
    (string,string)->None
    Requests user input and prints a poem using user's name and date of birth
    Preconditions: None
    '''
    name = input("What is your name? ")
    city = input("What city were you born in? ")
    print("Beneath the boughs of ancient trees,\nWhere whispers float on gentle breeze,\nAdventures call, in lands untold,\nLegends woven, in stories old.\n\n"+name+" of "+city+", you are the one,\nTo whom the quest is now begun.\nSo onward, "+name+", to lands unknown,\nYour destiny, it waits alone.")
    
########################
# Question 3
########################

def impl2loz(w):
    '''
    (number)->(int,float))
    Takes w as input and returns a pair of numbers such that w=l+o/16
    Preconditions: w is a non-negative float
    '''
    w = float(input("Enter a value greater than or equal to zero: "))
    l = math.floor(w)
    o = (w-math.floor(w))*16
    return (l,o)

########################
# Question 4
########################

def pale(n):
    '''
    (number)->(bool)
    Returns "False" if n is not pale (i.e. two or more consecutive digits = 3 or last digit /= 4) and "True" otherwise
    Preconditions: n is an int with 4 digits
    '''
    n = int(input("Enter a four digit number: "))
    return (((n % 10) != 0 and (n % 10) != 4 and (n % 10) != 8) and ((((n % 10) != (n % 100 // 10)) and ((n % 100 // 10) != (n % 1000 // 100)) and ((n % 1000 // 100 != n % 10000 // 1000))) or (not((n % 10) == 3 and (n % 100 // 10) == 3) and not((n % 100 // 10) == 3 and (n % 1000 // 100) == 3) and not((n % 1000 // 100) == 3 and (n % 10000 // 1000) == 3))))

########################
# Question 5
########################

def bibformat(author,title,city,publisher,year):
    '''
    (string,string,string,string,int)->(string)
    Returns a string in biblography format author (year). title. city: publisher.
    Preconditions: author, title, city, publisher are strings
    '''
    return (author+" ("+str(year)+"). "+title+". "+city+": "+publisher+".")

########################
# Question 6
########################

def bibformat_display():
    '''
    (string)->(string)
    Takes input from user and returns a string in biblography format author (year). title. city: publisher.
    Preconditions: author, title, city, publisher are strings
    '''
    author = input("Enter the author's name: ")
    title = input("Enter the title: ")
    city = input("Enter the city: ")
    publisher = input("Enter the publisher: ")
    year = int(input("Enter the year of publication: "))
    bib = bibformat(author, title, city, publisher, year)
    print(bib)

########################
# Question 7
########################

def compound(x,y,z):
    '''
    (number)->(int)
    Takes input from user and returns True if x is the only even number and if at least on pair of the three numbers add to a number greater than 100.
    Preconditions: x,y,z are ints
    '''
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    z=int(input("Enter the third number: "))
    return (x%2==0 and y%2!=0 and z%2!=0) and (x+y>100 or x+z>100 or y+z>100)

########################
# Question 8
########################

def funct(p):
    '''
    (number)->(none)
    Takes input(p) from user and solves for r in the equation 5^(r^2)-p+10=0
    Preconditions: p is a number
    '''
    p = float(input("Enter a number: "))
    print("r = ",math.sqrt((math.log(p-10,5))))
    
########################
# Question 9
########################

def gol(n):
    '''
    (number)->(int)
    Takes input(n) from user and returns the minimum number of times n needs to be divided by 2 to equal =< 1
    Preconditions: n is a number >= 1
    '''
    n = float(input("Enter a number greater than or equal to 1: "))
    return math.ceil(math.log(n,2))

########################
# Question 10
########################
import turtle

def draw_rocket():
    '''
    ()->(none)
    Draws an Imperial TIE Advanced x1 Starfighter from Star Wars using turtle graphics
    Preconditions: None
    '''
    s=turtle.Screen()
    t=turtle.Turtle()
    
    #setup
    t.speed(0)
    t.hideturtle()
    t.width(15)
    t.penup()
    
    #background
    s.bgcolor("black")
    t.pencolor("white")
    t.penup()
    from random import randint
    n=1
    while n <= 500:
    
        t.speed(0)
        t.color("white")
        t.dot(3)
        t.penup()
        t.goto(randint(-800, 800), randint(-500, 470))
        n+=1
    
    #fuselage fill
    t.goto(0,0)
    t.pencolor("#6f7173")
    t.pendown()
    t.dot(300)
    t.penup()
    
    #cockpit window fill
    t.pencolor("black")
    t.pendown()
    t.dot(200)
    t.penup()
    
    #center support structure
    t.pencolor("#404142")
    t.goto(0,-50)
    t.pendown()
    t.circle(50)
    t.penup()
    t.goto(0,50)
    t.pendown()
    t.setheading(90)
    t.forward(50)
    t.penup()
    t.goto(35.3553390593,35.3553390593)
    t.pendown()
    t.setheading(45)
    t.forward(50)
    t.penup()
    t.goto(50,0)
    t.pendown()
    t.setheading(0)
    t.forward(50)
    t.penup()
    t.goto(35.3553390593,-35.3553390593)
    t.pendown()
    t.setheading(315)
    t.forward(50)
    t.penup()
    t.goto(0,-50)
    t.pendown()
    t.setheading(270)
    t.forward(50)
    t.penup()
    t.goto(-35.3553390593,-35.3553390593)
    t.pendown()
    t.setheading(225)
    t.forward(50)
    t.penup()
    t.goto(-50,0)
    t.pendown()
    t.setheading(180)
    t.forward(50)
    t.penup()
    t.goto(-35.3553390593,35.3553390593)
    t.pendown()
    t.setheading(135)
    t.forward(50)
    t.penup()
    
    #outer support structure
    t.pencolor("#404142")
    t.goto(0,-100)
    t.pendown()
    t.setheading(0)
    t.circle(100)
    t.penup()
    
    #portside strut
    t.goto(220, 50)
    t.pendown()
    t.setheading(0)
    t.fillcolor("#6f7173")
    t.begin_fill()
    t.forward(30)
    t.setheading(270)
    t.forward(100)
    t.setheading(180)
    t.forward(30)
    t.setheading(90)
    t.forward(100)
    t.goto(122.8728066433,86.0364654527)
    t.penup()
    t.goto(122.8728066433,-86.0364654527)
    t.pendown()
    t.goto(220,-50)
    t.end_fill()
    t.penup()
    t.goto(250,-50)
    t.begin_fill()
    t.pendown()
    t.goto(300,-90)
    t.goto(300,90)
    t.goto(250,50)
    t.goto(250,-50)
    t.penup()
    t.end_fill()
    
    #starboard strut
    t.goto(-220, 50)
    t.pendown()
    t.setheading(180)
    t.begin_fill()
    t.forward(30)
    t.setheading(270)
    t.forward(100)
    t.setheading(0)
    t.forward(30)
    t.setheading(90)
    t.forward(100)
    t.goto(-122.8728066433,86.0364654527)
    t.penup()
    t.goto(-122.8728066433,-86.0364654527)
    t.pendown()
    t.goto(-220,-50)
    t.end_fill()
    t.penup()
    t.goto(-250,-50)
    t.begin_fill()
    t.pendown()
    t.goto(-300,-90)
    t.goto(-300,90)
    t.goto(-250,50)
    t.goto(-250,-50)
    t.end_fill()
    t.penup()
    
    #portside radiator
    t.goto(-300,0)
    t.setheading(90)
    t.begin_fill()
    t.pendown()
    t.forward(100)
    t.setheading(60)
    t.forward(250)
    t.setheading(105)
    t.forward(15)
    t.setheading(235)
    t.forward(260)
    t.setheading(270)
    t.forward(236.3836843)
    t.setheading(305)
    t.forward(260)
    t.setheading(75)
    t.forward(15)
    t.setheading(120)
    t.forward(250)
    t.setheading(90)
    t.forward(100)
    t.penup()
    t.goto(-328.0121591,110)
    t.pendown()
    t.setheading(210)
    t.forward(30)
    t.setheading(270)
    t.forward(190)
    t.setheading(330)
    t.forward(30)
    t.end_fill()
    t.penup()
    
    #starboard radiator
    t.goto(300,0)
    t.setheading(90)
    t.begin_fill()
    t.pendown()
    t.forward(100)
    t.setheading(120)
    t.forward(250)
    t.setheading(75)
    t.forward(15)
    t.setheading(305)
    t.forward(260)
    t.setheading(270)
    t.forward(236.3836843)
    t.setheading(235)
    t.forward(260)
    t.setheading(105)
    t.forward(15)
    t.setheading(60)
    t.forward(250)
    t.setheading(90)
    t.forward(100)
    t.penup()
    t.goto(328.0121591,110)
    t.pendown()
    t.setheading(330)
    t.forward(30)
    t.setheading(270)
    t.forward(190)
    t.setheading(210)
    t.forward(30)
    t.end_fill()
    t.penup()
    
    #fuselage
    t.goto(0,-150)
    t.pendown()
    t.setheading(0)
    t.circle(150)
    t.penup()
    
    #hardpoints
    t.goto(-20,-125)
    t.pendown()
    t.pencolor("#cc0606")
    t.dot(10)
    t.penup()
    t.goto(20,-125)
    t.pendown()
    t.dot(10)
    t.penup()
    t.width(4)
    t.pencolor("#404142")
    t.goto(-20,-130)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(20,-130)
    t.pendown()
    t.circle(5)
    t.penup()

########################
# Question 11
########################

def cad_cashier(price,payment):
    '''
    (float,float)->(none)
    Takes input(price,payment) from user and returns the change owed to the nearest nickel
    Preconditions: price and payment are floats ending in 0 or 5 and payment >= price
    '''
    price = float(input("Enter the price of the item: "))
    payment = float(input("Enter the amount paid: "))
    change = payment - price
    return round(change*20)/20
    
########################
# Question 12
########################

def min_CAD_coins(price,payment):
    '''
    (float,float)->(none)
    Takes input(price,payment) from user and returns the change in Canadian currency
    Preconditions: price and payment are floats ending in 0 or 5 and payment >= price
    '''
    price = float(input("Enter the price of the item: "))
    payment = float(input("Enter the amount paid: "))
    change = payment - price
    t="Toonies: ",int(change//2)
    change = change%2
    l="Loonies: ",int(change//1)
    change = change%1
    q="Quarters: ",int(change//0.25)
    change = change%0.25
    d="Dimes: ",int(change//0.1)
    change = change%0.1
    n="Nickels: ",int(change//0.05)
    change = change%0.05
        
    return t,l,q,d,n