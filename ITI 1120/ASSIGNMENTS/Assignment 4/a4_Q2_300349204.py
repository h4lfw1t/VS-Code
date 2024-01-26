def two_length_run(l):
    '''
    (list)->bool
    Given a list 'l', returns True if there are consecutive terms that are identical in the list, False otherwise.
    Preconditions: l is a list of numbers.
    '''
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            return True
    return False

#main
def main():
    '''
    ()->NoneType
    Given user input l, calls to function two_length_run and prints whether there are consecutive terms that are identical in the list.
    Preconditions: l is a list of numbers.
    '''
    l=[float(i) for i in (input("Please input a list of numbers separated by spaces: ").strip().split())]
    if two_length_run(l)==True:
        print("There are consecutive terms that are identical in the list.")
    else:
        print("There are no two-length runs in the list.")
main()