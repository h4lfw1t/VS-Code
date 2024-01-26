def triplicates(l):
    n = len(l)   # 1
    for i in range(n):   # 1 * n
        for j in range(i + 1, n):   # 1 * n * n
            for k in range(j + 1, n):   # 1 * n * n * n
                if l[i] == l[j] == l[k] and i!=j and j!=k and i!=k:   # 5 * n^3
                    return True   # <= 1
    return False   # <= 1
# 2 + n + n^2 + 6n^3 = O(n^3)
# 2 + n + n^2 + 6n^3 <= 2n^3 + n^3 + n^3 + 6n^3 = 10n^3 = O(n^3)
# The function triplicates has a load of O(n^3).
# This is a very high load, and it is not necessary.

def triplicates_sorted(l):
    '''
    (list)->bool
    Returns True if there are any triplicates in the list l.
    Preconditions: l is a list of integers.
    '''
    n=len(l)   # 1
    l.sort()   # nlogn
    for i in range(n-2):   # n-2
        if l[i]==l[i+2]:   # 2(n-2)
            return True   # <= 1
        return False   # <= 1
# 1 + nlogn + n-2 + 2n-4 = O(nlogn)

def triplicates_counted(l):
    '''
    (list)->bool)
    Returns True if there are any triplicates in the list l.
    Preconditions: l is a list of integers.
    '''
    for item in l:   # 1 * n
        if l.count(item)>=3:   # 2 * n^2
            return True   # <= 1
    return False   # <= 1
# 1 + 2n^2 + n = O(n^2)

def tuples(l, k):
    n = len(l)
    l.sort()
    for i in range(n-(k-1)):
        if l[i]==l[i+(k-1)]:
            return True
    return False

def majority(l):
    l.sort()
    candidate=l[len(l)//2]
    if l.count(candidate)