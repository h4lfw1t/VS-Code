######################################
# Exercise 1
######################################

def sum_odd_while_v2(n):
   '''
   (int)->int
   Returns the sum of all odd integers between 5 and n
   Preconditions: 
   '''
   i = 5
   sum = 0
   while i <= n:
      sum = sum + i
      i = i + 2
   return sum

######################################
# Exercise 2
######################################

def summarizer():
   '''
   (None) -> int
   Prints the sum of x1 and x2
   Preconditions: x1 and x2 are numbers
   '''
   flag = True
   while flag == True:
      x1 = int(input("Enter a number: "))
      x2 = int(input("Enter another number: "))
      sum = x1 + x2
      print("The sum of", x1, "and", x2, "is", sum)
      yn = input("Would you like to enter another pair of numbers? (y/n): ")
      if yn.lower() == "yes":
         flag = True
      else:
         flag = False

######################################
# Exercise 3
######################################

def first_neg(l):
   '''
   (list) -> int
   Returns the index of the first negative number in a list.
   Preconditions: l is a list of numbers
   '''
   i = 0
   while i < len(l):
      if l[i] < 0:
         return i
      i = i + 1
   return None

######################################
# Exercise 4
######################################

def sum_5_consecutive(l):
   '''
   (list) -> bool
   Returns true if the list 'l' contains 5 consecutive numbers whose sum is zero.
   Preconditions: l is a list of numbers
   '''
   i = 0
   while i < len(l) - 4:
      if l[i] + l[i + 1] + l[i + 2] + l[i + 3] + l[i + 4] == 0:
         return True
      i += 1
   return False

######################################
# Exercise 6
######################################

def fib(n):
   '''
   (int) -> list
   Returns a list of the first n Fibonacci numbers
   Preconditions: n is a positive integer
   '''
   i = 0
   fib_list = []
   while i < n:
      if i == 0 or i == 1:
         fib_list.append(1)
      else:
         fib_list.append(fib_list[i - 1] + fib_list[i - 2])
      i += 1
   return fib_list

######################################
# Exercise 7
######################################

def inner_product(l1, l2):
   n = 1
   sum = 0
   while n <= len(l1):
      sum += l1[n - 1] * l2[n - 1]
      n += 1
   return sum