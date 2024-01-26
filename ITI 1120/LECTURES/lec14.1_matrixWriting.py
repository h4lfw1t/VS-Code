def matrix():
    m=[]
    n=int(input("Enter the number of rows: "))
    for i in range(n):
        raw=[1]*nm.append(raw)
        
    for raw in m:
        for num in raw:
            print(num,end=" ")
        print()
        
def identity_matrix(m):
    '''
    (list)->bool
    Returns True if m is an identity matrix (square matrix with ones on the diagonal and zeros elsewhere)
    Precondition: m is a 2D matrix
    '''
    for i in range(len(m)):
        if len(m)!=len(m[i]):
            return False
        for i in range(len(m)):
            for j in range(len(m[i])):
                if i==j and m[i][j]!=1:
                    return False
                elif i!=j and m[i][j]!=0:
                    return False
    return True

def frequency(a):
    '''
    (list)->list
    Given list 'a', counts the number of occurences of each new item.
    Preconditions: a is a list
    '''
    f=[]
    for i in range(len(a)):
        city=a[i]
        flag=False
        for j in range(len(f)):
            if city==f[j][0]:
                f[j][1]+=1
                flag=True
        if flag==False:
            f.append([city,1])
    return f

def main():
    cities=["Toronto","Ottawa","Montreal","Vancouver","Calgary","Edmonton","Winnipeg","Halifax","Fredericton","St.John's", "Ottawa", "Winnipeg", "Toronto"]
    freq=frequency(cities)
    print(freq)