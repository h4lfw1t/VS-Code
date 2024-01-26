# problem:
# messify a given string s returns a new string where:
# if a charachter x in s is non-digit value, you skip it
# if a charachter x in s is a prime number, replace it with 'pr'
# if a character x is not a prime number, add that digit x times to the new string

import math


def messify(s):
    """
    (str) -> str
    >>> messify('12')
    '1pr'
    >>> messify('345a01')
    'pr4444pr1'
    >>> messify('000')
    ''
    """

    ns = ""
    for ch in s:
        if ch.isdigit():
            if ch in "2357":
                ns += "pr"
            else:
                ns += ch * int(ch)
        else:
            pass
    return ns


# Given a string s, produce a new string as follows:
# The string is broken up into chunks of size 2 charachters.
# Reverse each chunk
# If the chunk has a vowel, add a '*' to the end of the chunk
# If the chunk has no vowels, add a '@' to the end of the chunk

def has_vowel(s):
    for ch in s:
        if ch in "aeiouAEIOU":
            return True
    return False

def flork(s):
    """
    (str) -> str
    Precondition: k >= 1
    >>> flork('abcdef')
    'ab*dc@fe*'
    >>> flork('abcdefg')
    'ab*dc@fe*g'
    >>>flork('f')
    'f'
    >>> flork('')
    ''
    """
    
    if len(s) <= k-1:
        return s
    
    
    
    ns = ""
    
    for i in range(0, len(s), 2):
        chunk = s[i:i+k]
        chunk = chunk[::-1]
        ns = ns + chunk
        if has_vowel(chunk):
            ns += chunk + "*"
        else:
            ns += chunk + "@"
            
    if len(s) % 2 == 1:
        ns = ns[:-1] + s[-1]
    return ns