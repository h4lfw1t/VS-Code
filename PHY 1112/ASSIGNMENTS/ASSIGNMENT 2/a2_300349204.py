# Family name: Patrick Geraghty
# Student number:  300349204
# Course: PHY 1112
# Assignment: 2
# Year 2024


# Question 1

def question1():
    
    num = input("Enter a number: ")
    #End of part a
    print (num*30)
    #End of part b. At this step, when question1 is run, the program will prompt the user for a string input. When any input is entered, the program attempts to multiply the input by 30. However, since the input is a string, the program will print the input 30 times.
    num = float(num)
    print (num*30)
    #End of part c. At this step, when question1 is run, the program will prompt the user for a string input. When any input is entered, the program attempts to multiply the input by 30. However, since the input is a string, the program will print the input 30 times. Then, the input is converted to a float, and the program will print the input multiplied by 30. In the case that a decimal is entered, the number is multiplied by 30.
    num = int(num)
    print (num*30)
    #End of part d. At this step, when question1 is run, the program will prompt the user for a string input. When any input is entered, the program attempts to multiply the input by 30. However, since the input is a string, the program will print the input 30 times. Then, the input is converted to an integer, and the program will print the input multiplied by 30. In the case that a decimal is entered, the number is rounded to the nearest whole number and the rounded value is multiplied by 30.

# Question 2

def question2():
    
    deg = float(input("Please enter an angle measured in degrees: "))
    rad = deg*3.14159/180
    smallest_rad = rad%(2*3.14159)
    print(smallest_rad)
    print(str(smallest_rad/3.13159) + "\u03C0")
    #Upon testing with an angle of 960 degrees, the program prints 4.188786666666665. This is because the program is calculating the smallest radian measure of the angle, which is 4.188786666666665 radians (240 degrees).

# Question 3

def question3():
    
    condition1 = input("Enter a boolean value (T/F): ").lower()
    condition2 = input("Enter a boolean value (T/F): ").lower()
    if condition1 == "t":
        condition1 = True
    else:
        condition1 = False
    if condition2 == "t":
        condition2 = True
    else:
        condition2 = False
    nor = not (condition1 or condition2)
    print(nor)
    xor = condition1 ^ condition2
    print(xor)
    #Results of testing:
    #True True: False False
    #True False: False True
    #False True: False True
    #False False: True False

# Question 4

def question4():
    l = [1, 2, 3, 1j, "2.0"]
    for i in range (len(l)):
        print(type(l[i]))
    print(len(l))
    l.append(4)
    l.append(5)
    l.append(6)
    print(l)
    l.extend([7, 8, 9])
    print(l)
    l.insert(0, 0)
    print(l)
    l.index(1j)
    print(l)
    l.pop(l.index(1j))
    print(l)
    l.remove("2.0")
    print(l)
    l2 = l[2:5]
    print(l2)
    l3 = l[1:-1]
    print(l3)