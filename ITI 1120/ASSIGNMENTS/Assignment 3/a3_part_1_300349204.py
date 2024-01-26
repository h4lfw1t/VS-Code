import math

# is_up_monotone function


def is_up_monotone(X, d):
    '''
    (str) -> int
    Given parameters 'X' and 'd', this function returns a string where 'X' is split into consecutive sets of integers of size 'd' by its digits.
    Preconditions: X is a string and d is a string greater than 0.
    '''
    digit = '0123456789'
    for i in str(X):
        if not i in digit:
            print('Error: The input can only be an integer. Try again.')
            return "i-Error"
    for i in str(d):
        if not i in digit:
            print('Error: d can only be an integer. Try again.')
            return "i-Error"
    else:
        X = str(X)
        d = int(d)
        if '.' in X:
            print('Error: The input can only be an integer. Try again.')
            return "i-Error"
        elif int(X) < 1:
            print('Error: The input can only be a positive integer. Try again.')
            return "p-Error"
        elif d == 0:
            print('Error: d cannot be 0. Try again.')
            return "0-Error"
        elif len(X) % d != 0:
            print('Error: the length of X is not a multiple of d. Try again.')
            return "X-Error"
        else:
            ns = ''
            result = True
            for i in range(0, len(X), d):
                chunk = X[i:i+d]
                next_chunk = X[i+d:i+(2*d)]
                if next_chunk != '':
                    if int(chunk) > int(next_chunk):
                        result = False
                ns = ns + chunk + ' '

            ns = ns.strip()
            print(ns.replace(' ', ', '))
            return result


# main
print("**************************************")
print("*                                    *")
print("* __Welcome to up-monotone inquiry__ *")
print("*                                    *")
print("**************************************")

name = input("What is your name?    ")

print("**" + (len(name) + 37) * "*" + "**")
print("* " + (len(name) + 37) * " " + " *")
print("* __" + name + ", Welcome to up-monotone inquiry.__ *")
print("* " + (len(name) + 37) * " " + " *")
print("**" + (len(name) + 37) * "*" + "**")

flag = True
while flag:
    question = input(
        name+", would you like to test if a number admits an up-monotone split of given size? ")
    question = (question.strip()).lower()
    if question == 'no':
        flag = False
    elif question == 'yes':
        print("Good choice!")
        X = input("Enter a positive integer:   ")
        d = (input("Input the split. The split has to divide the length of 123456 i.e. 6:   "))
        function = is_up_monotone(X, d)
        if function == True:
            print("The sequence is up-monotone.")
        elif function == False:
            print("The sequence is not up-monotone.")
        elif function == "0-Error":
            pass
        elif function == "X-Error":
            pass
        elif function == "i-Error":
            pass
        elif function == "p-Error":
            pass
    else:
        print("Please answer with yes or no. Try again.")
print("*" * (len(name) + 31))
print("*" + (len(name) + 29) * " " + "*")
print("* __Goodbye " + name + "! See you soon.__ *")
print("*" + (len(name) + 29) * " " + "*")
print("*" * (len(name) + 31))
