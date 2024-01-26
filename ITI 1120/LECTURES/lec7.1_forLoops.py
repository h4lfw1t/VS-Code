# The len[] function returns the number of elements in a list.
# For example len([1,2,3]) returns 3 as there are three characters in the list. This can be used with any type of input (int, float, str, bool, etc.)
# If you want to find the specific character at a certain index, you can use the [] operator. For example, if you want to find the character at index 2 in the list [1,2,3], you can use [2] to return 3.
# If you want to find the index of a certain character, you can use the .index() function. For example, if you want to find the index of 3 in the list [1,2,3], you can use .index(3) to return 2.
# You can also use negative indexes to specify the character at that value counting from the last index. For example, if you want to find the character at index -1 in the list [1,2,3], you can use [-1] to return 3.
# Using square brackets indicates an index, while using parentheses indicates a function.
# If the string "Hello" is stored in the variable x, then x[1] is "e" and x[0] is "H", while x[-1] = "o".
# Using the above variable, x[1:4,2] while start counting from character 1 to character 4, counting every second character, and then return the character at index 2.


s = "string"

# This will print out each character in the string s using a for loop on a new line followed by an asterisk
for ch in s:
    print(ch)
    print("*")
    
print("Done")

# A for loop will iterate through each character in a string or each element in a list.
# For example, if you have a string s = "string", then the for loop will iterate through each character in the string.
# The for loop will start at the first character and then go through each character until it reaches the end of the string.
# The for loop will then stop and the program will continue to the next line of code.
# The for loop will then repeat this process until it reaches the end of the string.


def printVowels(phrase):
    '''(str) -> NoneType
    This function reads a phrase, identifies each character that is a vowel, and prints it.
    NOTE: The vowels must be identified using the in operator.
    Preconditions: phrase must be a string.
    '''
    for ch in phrase:
        if ch in "aeiouAEIOU":
            print(ch)
            
            
def countVowels(phrase):
    '''(str) -> int
    This function reads a phrase, identifies each character that is a vowel, and returns the number of vowels.
    NOTE: The vowels must be identified using the in operator.
    Preconditions: phrase must be a string.
    '''
    count = 0
    for ch in phrase:
        if ch in "aeiouAEIOU":
            count = count + 1
    return count
