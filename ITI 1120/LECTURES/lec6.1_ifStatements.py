# if statements are a one way statement that begins with "if" followed by a <condition> and closed with a colon.
# the next indented block is executed if the <condition> is true.
# if the <condition> is false, the indented block is skipped.
# NOTE: this counts as one if statement.

# if/else statements are two way statements that begin with "if" followed by a <condition> and closed with a colon, beginning the first indented block. In-line with the if statement, an else statement follows.
# the else statement begins with "else" and is followed by a colon, beginning the second indented block; no condition is required.
# if the initial condition is true, it executes the if block and skips the else block.
# if the initial condition is false, it skips the if block and executes the else block.
# NOTE: this counts as one if statement.

# if/elif/else statements are multi-way statements that begin with "if" followed by a <condition> and closed with a colon, beginning the first indented block. In-line with the if statement, an elif statement follows, beginning with "elif", followed by a <condition> and a colon. An else statement after.
# if the initial condition is true, it executes the if block and skips the elif and else blocks.
# if the initial condition is false, it skips the if block and analyzes the elif block.
# if the elif condition is true, it executes the elif block and skips the else block.
# if both conditions are false, it skips the elif block and executes the else block.
# NOTE: this counts as one if statement.

# if statements only ever execute one block of code.

# if examples

def abs(x):
    return -x if x < 0 else x

def formatAge(age):
    '''
    (int) -> (str)
    Takes an age and returns a string describing the age group.
    Preconditions: age >= 0
    '''
    if age<20:
        return str(age)
    elif age<30:
        return 'twenties'
    elif age<40:
        return 'thirties'
    else:
        return "ancient"
    
# a method is a function that is attached to an object
# methods are called using the dot operator
# object.method(arguments)
# the object is called the receiver
# the method is called the message
# the arguments are called the arguments
