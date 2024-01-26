import math
import random


def elementary_school_quiz(flag, n):
    '''
    (int, int) -> (str)
    This function has two parameters, namely an integer flag that takes only values 0 or 1 and
    an integer n that takes only values 1 or 2. If flag is 0, elementary_school_quiz helps practice subtraction. But if
    flag is 1, elementary_school_quiz helps practice exponentiation. The function, elementary_school_quiz then
    generates n math problems that a pupil must answer in turn. For each question, it generates two random positive,
    single-digit numbers and asks the pupil for the answer to the math problem with those two numbers (either subtract the second number from the first,
    or raise the first number to the power of the second number). elementary_school_quiz then prompts the pupil for
    the answer, and checks if her answer is correct. At the end of n questions, elementary_school_quiz returns the
    number of questions answered correctly.
    Preconditions: flag is 0 or 1, n is 1 or 2
    '''
    if flag == 0:
        points = 0
        nn = "a" * n
        for i in nn:
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            ans = input("What is " + str(a) + " - " + str(b) + "? ")
            if ans == str(a - b):
                points += 1
        return points
    elif flag == 1:
        points = 0
        nn = "a" * n
        for i in nn:
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            ans = input("What is " + str(a) + " ^ " + str(b) + "? ")
            if ans == str(a ** b):
                points += 1
        return points
    else:
        return "Error"
    
def high_school_quiz(a,b,c):
    '''
    (int, int, int) -> NoneType
    This function has three parameters representing three real numbers for the coefficients of the quadratic
    equation ax^2+bx +c = 0. The function displays/prints the equation frist and then prints its solutions. The function
    must display correct and meaningful solutions given any three real numbers for coefficients a, b and c.
    Preconditions: none
    '''
    print("The equation " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0")
    if a == 0 and b == 0 and c == 0:
        print ("has infinitely many solutions")
    elif a == 0 and b == 0 and c != 0:
        print ("has no solution")
    elif a == 0 and b != 0 and c == 0:
        print ("has the following solution: x = 0")
    elif a != 0 and b == 0 and c == 0:
        print ("has the following solution: x = 0")
    elif a == 0 and b != 0 and c != 0:
        print ("has the following solution: x = " + str(-c / b))
    elif a != 0 and b != 0 and c == 0:
        print ("has the following solutions: 0 and x = " + str(-b / a))
    elif a != 0 and b == 0 and c != 0:
        if -c / a < 0:
            print ("has the following solutions: x = " + str(math.sqrt(c / a)) + "i and x = " + str(-math.sqrt(c / a)) + "i")
        else:
            print ("has the following solutions: x = " + str(math.sqrt(-c / a)) + " and x = " + str(-math.sqrt(-c / a)))
    elif a != 0 and b != 0 and c != 0:
        if b ** 2 - 4 * a * c < 0:
            print ("has the following solution: x = " + str(-b / (2 * a)) + " + " + str(math.sqrt(4 * a * c - b ** 2) / (2 * a)) + "i and x = " + str(-b / (2 * a)) + " - " + str(math.sqrt(4 * a * c - b ** 2) / (2 * a)) + "i")
        elif b ** 2 - 4 * a * c == 0:
            print ("has the following solution: x = " + str(-b / (2 * a)))
        else:
            print("has the following solution: x = " + str((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)) + " and x = " + str((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)))

# main

print("*****************************************")
print("*                                       *")
print("* __Welcome to my math quiz generator__ *")
print("*                                       *")
print("*****************************************")

print("Please answer the following questions\n")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':
    print("**" + (len(name) + 66) * "*" + "**")
    print("* " + (len(name) + 66) * " " + " *")
    print("* __" + name + ", Welcome to my quiz generator for elementary school students.__ *")
    print("* " + (len(name) + 66) * " " + " *")
    print("**" + (len(name) + 66) * "*" + "**")
    
    m = input("What kind of questions would you like to practice? \n0 for subtraction\n1 for exponentiation\n")
    if m == "0":
        n = int(input("How many practice questions would you like to do? Enter 1 or 2: "))
        points = elementary_school_quiz(0, n)
        if points == n:
            print("Congratulations " +name+ "! You'll probably get an A tomorrow.")
        elif points == n/2:
            print("You did ok " +name+ ", but I know you can do better.")
        else:
            print("I think you need some more practice " +name+ ".")
    elif m == "1":
        n = int(input("How many practice questions would you like to do? Enter 1 or 2: "))
        points = elementary_school_quiz(1, n)
        if points == n:
            print("Congratulations " +name+ "! You'll probably get an A tomorrow.")
        elif points == n/2:
            print("You did ok " +name+ ", but I know you can do better.")
        else:
            print("I think you need some more practice " +name+ ".")

elif status=='2':

    print("**" + (len(name) + 34) * "*" + "**")
    print("* " + (len(name) + 34) * " " + " *")
    print("* __Quadratic equation solver for " + name + "__ *")
    print("* " + (len(name) + 34) * " " + " *")
    print("**" + (len(name) + 34) * "*" + "**")
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")
        if "yes" in question.lower():
            question = "yes"

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            a = float(input("Enter the coefficient a: "))
            b = float(input("Enter the coefficient b: "))
            c = float(input("Enter the coefficient c: "))
            high_school_quiz(a, b, c)

elif status == "I hate math":
    print("I hate math too! Let's suffer together!")

else:
    print("If you would still like to use the program, re-run it and type '1' for  subtraction/exponent practice, or 2 for a quadratic equation solver.")

print("Good bye "+name+"!")
