# The load of a function is the number of times it is called, the number of processes it runs, and the number of times it is called by other functions.
# Always consider the load of a function when writing code, and determine if it can be written with a smaller load.

def maximum(l):
    '''
    [list] -> num
    Given the list of numbers l, the function returns the maximum number in the list.
    Preconditions: l is a list of numbers.
    '''
    current_max = l[0] # 1 (load = 1)
    for i in l: # n (load = 1+n)
        if i > current_max: # n (load = 1+2n)
            current_max = i # n (load = 1+3n)
    return current_max # 1 (load = 2+3n)

def duplicates(l):
    '''
    [list] -> bool
    Given the list of numbers l, the function returns True if there are any duplicates in the list, and False otherwise.
    Preconditions: l is a list of numbers.
    '''
    n = len(l)
    for i in range(n): # n (load = n)
        for j in range(i + 1, n): # n^2/2 + n (load = n^2/2 + 3n/2)
            if l[i] == l[j]: # n^2/2 + n (load = n^2 + 5n/2)
                return True # 1 
    return False # 1 
# load = n^2 + 5n/2 +1 = O(n^2)

def duplicates2(l):
    n = len(l)
    for i in range(n): # n (load = n)
        rep = l.count(l[i]) # n^2 (load = n^2 + n)
        if rep >= 2: # n (load = n^2 + 2n)
            return True # 1
    return False # 1
# load = n^2 + 2n + 1 = O(n^2)

def duplicates3(l):
    n = len(l)
    l.sort() # nlogn (load = nlogn)
    for i in range(n-1): # n-1 (load = n-1 + nlogn)
        if l[i] == l[i+1]: # n-1 (load = 2n-1 + nlogn)
            return True # 1
    return False # 1
# load = 2n-1 + 1 + nlogn = O(nlogn)