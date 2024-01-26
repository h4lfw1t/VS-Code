def longest_run(l):
    '''
    (list)->int
    Given a list 'l', returns the length of the longest run in the list.
    Preconditions: l is a list of numbers.
    '''
    length=1
    max_length=1
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            length+=1
        else:
            length=1
        if length>max_length:
            max_length=length
    return max_length

# main
def main():
    '''
    ()->NoneType
    Given user input l, calls to function longest_run and prints the length of the longest run in the list.
    Preconditions: l is a list of numbers.
    '''
    l=[float(i) for i in (input("Please input a list of numbers separated by spaces: ").strip().split())]
    x=longest_run(l)
    if x==1:
        print("There are no runs in the list.")
    else:
        print("The length of the longest run in the list is",x)
main()