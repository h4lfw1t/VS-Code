import random

# A linear search algorithm is a simple algorithm that searches for a value in a list by checking each element in turn until it finds the desired value.
# The algorithm returns the index of the value if it is found, or -1 if it is not found.
# The algorithm is implemented in the function linear_search below.
def linear_search(l,v):
    '''
    (list, obj)->int
    >>> l=random.sample(range(1,1000001),1000)
    >>> l[:100]
    >>> linear_search(l,50)
    -1
    >>> linear_search(l,420315)
    70
    >>> linear_search(l,316159)
    0
    '''
    n=len(l)    # load=1
    for i in range(n):  # load=n
        if l[i]==v: # load=n
            return i # load<=1
    return -1  # load<=1
    # load=2n+2  --> O(n)

# A binary search algorithm is a more efficient algorithm that searches for a value in a sorted list by checking the middle element of the list.
# If the middle element is the desired value, the algorithm returns the index of the value.
# If the middle element is greater than the desired value, the algorithm searches the left half of the list.
# If the middle element is less than the desired value, the algorithm searches the right half of the list.
# The algorithm returns -1 if the value is not found.
# The algorithm is implemented in the function binary_search below.
def binary_search(l,v):
    '''
    (list,obj)->int
    Preconditions: l is sorted
    '''
    # left=0
    # right=len(l)-1
    # while left<=right:
    #     mid=(left+right)//2
    #     if l[mid]==v:
    #         return mid
    #     elif l[mid]>v:
    #         right=mid-1
    #     else:
    #         left=mid+1
    # return -1
    b=0
    e=len(l)-1
    while b<=e:
        m=(b+e)//2
        if v<l[m]:
            e=m-1
        elif v>l[m]:
            b=m+1
        else:
            return m
    return False
    # load=2log(n)+3 --> O(log(n))
