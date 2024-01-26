def m(i):
    if i == 0:
        return 0
    if i == 1:
        return 1/3
    else:
        return i/(2*i+1) + m(i-1)

def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n//10)

def is_palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

def is_palindrome_v2(s):
    if len(s) < 2:
        return True
    if not s[0].isalpha():
        return is_palindrome_v2(s[1:])
    if not s[-1].isalpha():
        return is_palindrome_v2(s[:-1])
    if s[0].lower() != s[-1].lower():
        return False
    return is_palindrome_v2(s[1:-1])

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)