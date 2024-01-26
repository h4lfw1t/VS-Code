def is_square(m):
     '''2d-list => bool
     Return True if m is a square matrix, otherwise return False
     (Matrix is square if it has the same number of rows and columns'''
     for i in range(len(m)):
          if len(m[i]) != len(m):
               return False
     return True


def magic(m):
     '''2D list->bool
     Returns True if m forms a magic square
     Precondition: m is a matrix with at least 2 rows and 2 columns '''

     # this tests the condition that is implied by the definition
     # i.e. that m has to be a square matrix
     if(not(is_square(m))): # if matrix is not square
          return False      # return False

     # YOUR CODE GOES HERE
     # m has 2+ rows
     if len(m)<2:
          return False
     
     # m has 2+ columns
     for i in range(len(m)):
          if len(m[i])<2:
               return False
     
     x=sum(m[0])
     
     # m[0]==m[1]==m[2]==...m[n]==x
     if sum(m[0])!=sum(m[1]):
          return False
     
     # m[0][0]==m[1][0]==m[2][0]==...m[n][0]==x
     # m[1][0]==m[1][1]==m[1][2]==...m[1][n]==x
     # ...
     # m[n][0]==m[n][1]==m[n][2]==...m[n][n]==x
     for i in range(len(m)):
          if sum(m[0])!=sum(m[i]) or sum(m[i])!=x:
               return False
     
     # m[0][0]+m[1][1]+m[2][2]+...m[n][n]==m[0][n]+m[1][n-1]+m[2][n-2]+...m[n][0]     
     d1=[]
     d2=[]
     for j in range(len(m)):
          d1.append(m[j][j])
          d2.append(m[j][-j-1])
     if sum(d1)!=sum(d2) or sum(d1)!=x or sum(d2)!=x:
          return False
     
     n=len(m)
     l=[]
     for i in range(len(m)):
          for j in range(len(m[i])):
               l.append(m[i][j])
     # m contains all numbers from 1 to n^2
     for i in range(1,n**2+1):
          if i not in l:
               return False
     return True
     # TEST CONDITION 1

     # TEST CONDITION 2




# main
# TESTING OF magic functions

# this should print True

m0=[[2,7, 6],[9,5,1],[4,3,8]]
print(magic(m0))
    
# this should print True
m1 = [[16,3,2,13], [5,10,11,8],[9,6,7,12], [4,15,14,1]]
print(magic(m1))
    
# this should print False. Why? Which condition imposed on magic squares is not true for m3
m2 = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(magic(m2))
    
#this should print False. Why? Which condition imposed on magic squares is not true for m3
m3 =  [[1,1],[1,1]]
print(magic(m3))

# #this should print False. Why? Which condition imposed on magic squares is not 
m3 =  [[1,1],[1,1],[1,2]]
print(magic(m3))
