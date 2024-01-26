# Welcome to lists
# Lists are a type of data structure that can hold multiple pieces of information.
# Lists are created using square brackets, with commas separating items.
# Lists can contain any mix and match of the data types you have seen so far.
# Lists can be assigned to variables, and values can be assigned to lists.
# Lists can be changed.
# Lists are mutable, meaning they can be changed in place.
# Lists of lists are possible to create a matrix, or a multi-dimensional list.
# Indexing allows you to access individual items in a list.
# Slicing allows you to access a range of items in a list.
# List methods allow you to perform specific tasks with lists.
# You can join two lists together using the + operator.
# List comprehensions provide a powerful way to create and manipulate lists.
l = [1, 2, 3, 4, 5]
l[0] # stores the first element in the list (1)
l[3] = 0 # changes the fourth element to 0
l[1:3] # returns a list containing the second and third elements (2 and 3)
l[3:1:-1] # returns a list containing the fourth and third elements (4 and 3)

# lists can be sorted using the sort method
l.sort() # sorts the list such that l[0] is now 0, l[1] is now 1, etc.