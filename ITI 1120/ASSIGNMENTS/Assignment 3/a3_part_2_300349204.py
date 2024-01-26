import math

##################################################
# 2.1 sum_odd_divisors(n)
##################################################


def sum_odd_divisors(n):
    '''
    (int) -> int
    Given parameter 'n', this function returns the sum of all odd divisors of 'n'. If n == 0, returns None.
    Preconditions: n is an integer.
    '''
    n = abs(n)
    if n == 0:
        return None
    sum = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 != 0:
            sum += i
    return sum


##################################################
# 2.2 series_sum()
##################################################

def series_sum():
    '''
    (int) -> float
    Given user input of positive integer 'n', this function returns the sum of the series 1000 + 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/n^2.
    Preconditions: n is a positive integer.
    '''
    n = int(input("Enter a positive integer: "))
    if n < 0:
        return None
    sum = 1000
    for i in range(1, 1+n):
        sum += (1/(i**2))
    return sum

##################################################
# 2.3 pell(n)
##################################################


def pell(n):
    '''
    (int) -> int
    Given parameter 'n', this function returns the nth Pell number. If n < 0, returns None.
    Preconditions: n is an integer.
    '''
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n_1 = 1
        n_2 = 0
        for i in range(2, n+1):
            _n = 2*n_1 + n_2
            n_2 = n_1
            n_1 = _n
        return _n

##################################################
# 2.4 countMembers(s)
##################################################


def countMembers(s):
    '''
    (str) -> int
    Given parameter 's', this function returns the number of characters in 's' that are alphanumeric.
    Preconditions: s is a string.
    '''
    count = 0
    for i in s:
        if i in ['e', 'f', 'g', 'h', 'i', 'j', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', '2', '3', '4', '5', '6', '!', ',', '\\']:
            count += 1
    return count

##################################################
# 2.5 casual_number(s)
##################################################


def casual_number(s):
    '''
    (str) -> int
    Given parameter 's', this function returns s as an integer made up of only digits. If s contains any non-digit characters, returns None.
    Preconditions: s is a string.
    '''
    num = False
    cas = '0'
    x = -1
    for i in s:
        x += 1
        if i not in ['-', ',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return None
        else:
            if i == ',':
                pass
            elif (i == '-'):
                if cas[x] == '-':
                    return None
                cas += '-'
            else:
                num = True
                cas += str(i)
    if num == False:
        return None
    return int(cas[1:])

##################################################
# 2.6 alienNumbers(s)
##################################################


def alienNumbers(s):
    '''
    (str) -> int
    Given parameter 's', this function returns an integer representing the value of 's' by summiarizing the alien value of its characters.
    Preconditions: s is a string.
    '''
    value = 0
    for i in s:
        if i == 'T':
            value += 1024
        elif i == 'y':
            value += 598
        elif i == '!':
            value += 121
        elif i == 'a':
            value += 42
        elif i == 'N':
            value += 6
        elif i == 'U':
            value += 1
    return value

##################################################
# 2.7 alienNumbersAgain(s)
##################################################


def alienNumbersAgain(s):
    '''
    (str) -> int
    Given parameter 's', this function returns an integer representing the value of 's' by summiarizing the alien value of its characters.
    Preconditions: s is a string.
    '''
    value = 0
    for i in s:
        if i == 'T':
            value += 1024
        elif i == 'y':
            value += 598
        elif i == '!':
            value += 121
        elif i == 'a':
            value += 42
        elif i == 'N':
            value += 6
        elif i == 'U':
            value += 1
    return value

##################################################
# 2.8 encrypt(s)
##################################################


def encrypt(s):
    '''
    (str) -> str
    Given parameter 's', this function returns a string where the characters in 's' are reversed, and then the first and last characters become the first and second respectively; the second and second last become the third and fourth respectively, etc.
    Preconditions: s is a string.
    '''
    reversed = s[-1::-1]
    swap = ''
    if len(s) % 2 == 0:
        for i in range(0, (len(s)//2)):
            swap += reversed[i]
            swap += s[i]
    else:
        for i in range(0, (len(s)//2)):
            swap += reversed[i]
            swap += s[i]
        swap += reversed[len(s)//2]
    print(swap)

##################################################
# 2.9 weaveop(s):
##################################################


def weaveop(s):
    '''
    (str) -> str
    Weaves together consecutive characters with 'o' and 'p' in lower or upper case depending on the case of the character. If at least one consecutive character is not in the alphapbet, it does not insert any case of 'o' or 'p' between the character.
    Preconditions: s is a string.
    '''
    mod = ''
    if len(s) <= 1:
        pass
    else:
        for i in range(len(s)-1):
            if s[i].isalpha() and s[i+1].isalpha():
                if s[i].islower() and s[i+1].islower():
                    mod += s[i] + 'op'
                elif s[i].isupper() and s[i+1].isupper():
                    mod += s[i] + 'OP'
                elif s[i].islower() and s[i+1].isupper():
                    mod += s[i] + 'oP'
                elif s[i].isupper() and s[i+1].islower():
                    mod += s[i] + 'Op'
            else:
                mod += s[i]
        return mod + s[-1]

##################################################
# 2.10 squarefree(s)
##################################################


def squarefree(s):
    '''
    (str) -> bool
    Given parameter 's', this function returns True if 's' has no identical consecutive groups of characters, False otherwise.
    Preconditions: s is a string.
    '''
    if len(s) < 2:
        return True
    else:
        for i in range(0, len(s)):
            if s[i] in ('0', '1,', '2', '3', '4', '5', '6', '7', '8', '9'):
                return False
            for k in range(0, len(s)):
                if s[i:i+(k+2)] == s[i+(k+1):i+(k+2)+(k+1)]:
                    return False
                else:
                    pass
    return True
