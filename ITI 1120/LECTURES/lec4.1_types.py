#Call a positive integer leap if it is divisible by four, except that any number divisible by 100 is not leap unless it is also divisible by 400. Write a program that takes a year from the user and outputs True if it is a leap year, or False otherwise.

def leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#Python recognizes whole numbers as an input called an integer (int)
#Python recognizes numbers with decimals as an input called a float (float)
#Python recognizes text as an input called a string (str)
#Python recognizes True and False as an input called a boolean (bool)

#"These are double quotes"
#These are single quotes'
#"To include quotes within quotes, such as 'this', use a separate quote from the opener and closer"
#"To include quotes without changing quote type, use '\ ' to escape the quote"

#Use \n at the end of a string to start a new line
#Use \t at the end of a string to tab

#len() returns the length of a string; len("Hello") returns 5
#str() converts a value to a string; str(5) returns "5". str() is useful for concatenation of strings and numbers; if year = 2016, "The year is " + str(year) returns "The year is 2016"
#int() converts a value to an integer; int("5") returns 5. int() is useful for converting user input to an integer; if year = int(input("Enter a year: ")), then year will be an integer
#bool() converts a value to a boolean; bool(5) returns True. bool() is useful for converting user input to a boolean; if leap = bool(input("Is it a leap year? ")), then leap will be a boolean
#input() takes user input; input("Enter a year: ") returns a string. input() is useful for taking user input; if year = int(input("Enter a year: ")), then year will be an integer
#input() only allows for data from one string; if you want to include multiple inputs in one function, concatenate them with a + sign

name = input("What is your name? ")
location = input("Where are you from? ")
duration = input("How long have you been here? ")