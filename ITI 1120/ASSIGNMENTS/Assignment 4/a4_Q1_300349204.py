def number_divisible(l,n):
    '''
    (list,int)->int
    Given parameters l and n, returns number of items in l divisible by n.
    Preconditions: l is a list of integers, n is an integer.
    >>> number_divisible([6, 10, 2, 3, 4, 5, 6, 0], 3)
    4
    '''
    count=0
    for i in l:
        if i%n==0:
            count+=1
    return count

# main
def main():
    '''
    ()->NoneType
    Given user input l and n, calls to function number_divisible and prints the number of items in l divisible by n.
    Preconditions: l is a list of integers, n is an integer.
    '''
    l=[int(i) for i in (input("Enter a list of integers separated by spaces: ").strip().split())]
    n = int(input("Enter an integer: "))
    x = number_divisible(l,n)
    print("There are",x,"items divisible by",n,"in the list",l)
main()
