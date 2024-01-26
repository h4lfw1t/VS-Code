import random
n=int(input("Enter a positive even integer for the size of the list?" ))

####################
# Part 1.a
####################
a=[]
i = 0
while i < n:
   a.append(0)
   i+=1
print(a)

####################
# Part 1.b
####################
a=[0]*n
print(a)

####################
# Part 2.a
####################
b=[]
i = 0
while i < n:
    b.append(random.randint(1,100))
    i+=1
print(b)

####################
# Part 2.b
####################
b=[0]*n
i = 0
while i < n:
    b[i]=random.randint(1,100)
    i+=1
print(b)

####################
# Part 3
####################
c = b

####################
# Part 4
####################
i = 0
while i < (n//2):
    c[i]=0
    i+=1
print(c)
print(b)

####################
# Part 5.a 
####################
d=[]
i = 0
while i < n:
    d.append(b[i])
    i+=1
print(d)

####################
# Part 5.b
####################
d=b[:]
print(d)

####################
# Part 6
####################
e=[]
i = 0
while i < n:
    e.append(b[i])
    i+=2
print(e)