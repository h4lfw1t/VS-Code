############################################################
# Exercise 0
############################################################

def get_year():
    '''
    ()->int
    Returns the four-digit year entered by the user
    Preconditions: None
    '''
    try:
        year = int(input("Enter a year: "))
        if year < 1000 or year > 9999:
            print("The year must be a four-digit integer")
            return get_year()
        return year
    except ValueError:
        print("The year must be a four-digit integer")
        return get_year()

############################################################
# Exercise 1
############################################################

# an implementation with while loop
def linear_search_v1(lst, value):
    """ (list, object) -> int
    Return the index of the last occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search_v1([2, 5, 1, -3], 5)
    1
    >>> linear_search_v1([2, 4, 2], 2)
    0
    >>> linear_search_v1([2, 5, 1, -3], 4)
    -1
    >>> linear_search_v1([], 5)
    -1
    """

    i = -1 # The index of the next item in lst to examine.
    # Keep going until we reach the end of lst or until we find value.
    while i != -len(lst) and lst[i] != value:
        i=i-1
    # If we fell off the end of the list, we didn't find value.
    if i == len(lst):
        return -1
    else:
        return len(lst)+i


# an implementation with for loop
def linear_search_v2(lst, value):
    """ same docstring as above
    """

    for i in range(len(lst)):
        if lst[-i-1] == value:
            return len(lst)-i-1
    return -1


# an implementation with sentinel

# all three versions are correct and do roughly n operations on a list of size n
# the following solution uses no branching (i.e. if statements)

def linear_search_v3(lst, value):
    """ same docstring as above
    """     
    lst.append(value)
    i=len(lst)-2
    # Keep going until we find value.
    while lst[i] != value:
        i = i-1
    # Remove the sentinel.
    lst.pop()
    # If we reached the end of the list we didn't find value.
    if i == len(lst):
        return -1
    else:
        return i

############################################################
# Exercise 2
############################################################

def min_or_max_index(lst, flag):
    '''
    (list, str)->int
    Returns the index of the minimum or maximum value in the list
    Preconditions: None
    '''
    lst.sort()
    if flag == True:
        index = lst[0]
        return index
    elif flag == False:
        index = lst.index(lst[-1])
        return index
    else:
        print("Invalid flag")
        return None

############################################################
# Exercise 3
############################################################

def first_one(L):
    '''
    (list)->int
    Returns the index of the first occurrence of 1 in the list
    Preconditions: L is a list of 0s followed by 1s
    '''
    b=0
    v=1
    e=len(L)-1
    while b<=e:
        m=(b+e)//2
        if v<L[m]:
            e=m-1
        elif v>L[m]:
            b=m+1
        else:
            return m
    return -1

def last_zero(L):
    '''
    (list)->int
    Returns the index of the last occurrence of 0 in the list
    Preconditions: L is a list of 0s followed by 1s
    '''
    if first_one(L) == -1:
        return len(L)-1
    else:
        return first_one(L)-1

############################################################
# Exercise 4
############################################################

# QUESTION 1

def element_uniqueness(L):
    '''(list)->bool
    Returns True if all the elements in the list are distinct,
    in other words, if there is no element in the list that appears more than once.
    Precondition: L is not empty

    >>> element_uniqueness([2, 2,2, 2, 8])
    False
    >>> element_uniqueness([1,-20,-1])
    True
    >>> element_uniqueness([3,2,4,0,3])
    False
    >>> element_uniqueness([10])
    True
    >>> element_uniqueness([10,10])
    False
    >>> element_uniqueness([10,-1])
    True
    '''
    L.sort()
    for i in range(len(L)-1):
        if L[i] == L[i+1]:
            return False
    return True

# QUESTION 2

def one_unique_at_least(L):
    '''(list)->bool
    Returns True if there exist at least one element in L that is unique,
    in other words, that appears exactlly once in the list
    Precondition: L is not empty
    >>> one_unique_at_least([2,2,2,2,8])
    True
    >>> one_unique_at_least([2,1,2])
    True
    >>> one_unique_at_least([1,-20,-1])
    True
    >>> one_unique_at_least([3,2,2,3,3])
    False
    >>> one_unique_at_least([10])
    True
    >>> one_unique_at_least([10,10])
    False
    >>> one_unique_at_least([10,-1])
    True
    '''
    x = 0
    if element_uniqueness(L) == True:
        return True
    else:
        L.sort()
        for i in range(len(L)-1):
            if (L[i] != L[i+1]) and (L[i] != L[i-1]):
                x = 1
        if L[-1] != L[-2]:
            x = 1
    if x != 1:
        return False
    return True

# QUESTION 3
    
def all_unique(L):
    ''' (list,int)->list
    Return a list of elements of L that appear exactlly once in L. 
    Precondition: L is not empty

    >>> all_unique([2, 2,2, 2, 8])
    [8]
    >>> all_unique([1,-20,-1])
    [-20,-1,,1]
    >>> all_unique([3,2,2,3,3])
    []
    >>> all_unique([10])
    [10]
    >>> all_unique([10,10])
    []
    >>> all_unique([10,-1])
    [-1,10]
    '''
    x = []
    if element_uniqueness(L) == True:
        return L
    L.sort()
    for i in range(len(L)-1):
        if (L[i] != L[i+1]) and (L[i] != L[i-1]):
            x.append(L[i])
    if L[-1] != L[-2]:
        x.append(L[-1])
    return x


# QUESTION 1 again

def element_uniqueness_v2(L):
    # make now a 2nd solution to element_uniqueness
    # by making a call to all_unique
    if all_unique(L) == L:
        return True
    return False


# QUESTION 2 again

def one_unique_at_least_v2(L):
    # make now a 2nd solution to one_unique_at_least_v2
    # by making a call to all_unique
    if len(all_unique(L)) >= 1:
        return True
    return False

# QUESTION 4

def count_unique(L):
    '''(list,int)->int
    Return the number of unique elements of L,
    i.e. the number of elements that appear exactlly once in L
    Precondition: L is not empty

    >>> count_unique([2, 2,2, 2, 8])
    1
    >>> count_unique([1,-20,-1])
    3
    >>> count_unique([3,2,2,3,3])
    0
    >>> count_unique([10])
    1
    >>> count_unique([10,10])
    0
    >>> count_unique([10,-1])
    2
    '''
    return len(all_unique(L))


# QUESTION 5                               

def duplicates(L):
    ''' (list)->int
    Returns True if the given list L has duplicates, in other,
    if it has at least one element that appears two or more times.
    Precondition: L is not empty

    >>> duplicates([2, 2,2, 2, 8])
    True
    >>> duplicates([1,-20,-1])
    False
    >>> duplicates([3,2,2,3,3])
    True
    >>> duplicates([10])
    False
    >>> duplicates([10,10])
    True
    >>> duplicates([10,-1])
    False
    '''
    L.sort()
    for i in range(len(L)-1):
        if L[i] == L[i+1]:
            return True
    return False

# QUESTION 6

def majority(L):
    '''(list)->
    An element of a list is called "majority" if MORE THAN half of the elements of the list are equal to it.
    This function returns the majority element of L if such an element exsits, otherwise it returns None
    >>> majority([2,1,2])
    2
    >>> majority([10,5,1,5,5])
    5
    >>> majority([5,5,1,1])
    
    >>> majority([3])
    3
    >>> majority([8,8,2,8])
    8
    '''
    L.sort()
    for i in range(len(L)-1):
        if L.count(L[i]) > len(L)/2:
            return L[i]
    return None
