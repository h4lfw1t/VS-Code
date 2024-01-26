import math

#########################
# Part 2.1
#########################

def  min_enclosing_rectangle(radius, x, y):
    '''
    (float, float, float) -> (float, float)
    Given the parameters radius(float), x(float), y(float), return bottom-left x-y coordinate of the minimum enclosing rectangle with the given x-y coordinate at it's center.
        >>> min_enclosing_rectangle(1,1,1)
        (0, 0)
        >>> min_enclosing_rectangle(4.5, 10, 2)
        (5.5, -2.5)
        >>> min_enclosing_rectangle(-1, 10, 2)
        >>> min_enclosing_rectangle(500, 1000, 2000)
        (500, 1500)
    Preconditions: All variables are numbers.
    '''
    if radius > 0 :
        return (x - radius, y - radius)
    else:
        return None

#########################
# Part 2.2
#########################

def vote_percentage(results):
    '''
    (string) -> (float)
    Given input string, return the percentage of votes for the winner by by counting the number of substrings 'yes' divided by total votes.
        >>> vote_percentage('yes yes yes yes yes abstained abstained yes yes yes yes')
        1.0
        >>> vote_percentage('yes,yes, no, yes, no, yes, abstained, yes, yes,no')
        0.6666666666666666
        >>> vote_percentage('abstained no abstained yes no yes no yes yes yes no')
        0.5555555555555556
        >>> vote_percentage('no yes no no no, yes yes yes no')
        0.4444444444444444
    Preconditions: Input string is a sequence of 'yes', 'abstained', and 'no' separated by spaces or commas.
    '''
    return results.count('yes') / (results.count('yes') + results.count('no'))

#########################
# Part 2.3
#########################

def vote():
    '''
    (string) -> NoneType
    Given input string, print a string indicating "unanimously" if all votes are yes, "super majority" if 2/3 =< votes are yes, "simple majority" if 1/2 =< votes are yes, and "no majority" otherwise.
        >>> vote()
        Enter the yes, no, abstained votes separated by commas or spaces: 
        yes yes yes yes yes abstained abstained yes yes yes yes
        The proposal passes unanimously.
        >>> vote()
        Enter the yes, no, abstained votes separated by commas or spaces: 
        yes,yes, no, yes, no, yes, abstained, yes, yes,no
        The proposal passes with super majority.
        >>> vote()
        Enter the yes, no, abstained votes separated by commas or spaces: 
        abstained no abstained yes no yes no yes yes yes no
        The proposal passes with simple majority.
        >>> vote()
        Enter the yes, no, abstained votes separated by commas or spaces: 
        no yes no no no, yes yes yes no
        There is no majority, thus the proposal does not pass.
    Preconditions: Input string is a sequence of 'yes', 'abstained', and 'no' separated by spaces or commas.
    '''
    results = input("Enter the yes, no, abstained votes separated by commas or spaces: ")
    vote_percentage(results)
    if vote_percentage(results) == 1:
        print("The proposal passes unanimously.")
    elif vote_percentage(results) >= 2/3:
        print("The proposal passes with super majority.")
    elif vote_percentage(results) >= 1/2:
        print("The proposal passes with simple majority.")
    else:
        print("There is no majority, thus the proposal does not pass.")