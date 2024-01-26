# Welcome to while loops
# while loops are used to repeat a block of code
# while loops are used when we don't know how many times we want to repeat the code
# while loops are used when we want to repeat the code until a condition is met
# a while loops is constructed similar to a for loop in that it begins with 'while' followed by a condition
# the condition is a boolean expression



answer = input("Yes, no do you want to buy this ticket?").lower()

while not(answer == "yes" or answer == "no"):
    print("Incorrect input")
    answer = input("Yes, no do you want to buy this ticket?").lower()
    
    
s = "smrt"

i = 0
while i < len(s) and s[i] not in "aeiouAEIOU":
    print(s[i])
    i = i+1
    
# Conjectures in a while loop
# Collatz conjecture
# The collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows:
# start with any positive integer n. Then each term is obtained from the previous term as follows:
# if the previous term is even, the next term is one half of the previous term.
# if the previous term is odd, the next term is 3 times the previous term plus 1.
# the conjecture is that no matter what value of n, the sequence will always reach 1.
# the property has also been called oneness

def collatz(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
    return True
    print(n)
for i in range(1, 1000001):
    collatz(i)
    
print("True for the first million")

import random
def guessing_game():
    print("I am thinking of a number between 1 and 100")
    x = random.randint(1, 100)
    tries = 5
    while tries > 0:
        guess = int(input("Guess a number: "))
        if guess == x:
            print("You guessed it!")
            return
        elif guess < x:
            print("Too low")
        elif guess > x:
            print("Too high")
        tries = tries - 1
    if tries == 0:
        print("You ran out of tries")
        return