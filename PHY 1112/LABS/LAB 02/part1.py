'''
Filename:       part1.py
Author:         Patrick Geraghty
Date Created:   2024-01-23
Date Modified:  2024-01-24
Description:    Contains variables with explicit and implicit typing, and type conversion.
'''
# Part 1

# Variables with explicit typing
greeting: str = "Hello"
ultimate_answer: int = 42
something_complex: complex = (24.5 + 17.5j)

# Variables with implicit typing
place = "World"
anti_real_ultimate_answer = -42.0
class_info = {"subject": "PHY", "number": 1112}

# Type conversion
real_ultimate_answer = float(ultimate_answer)

# Print statements for type and value of each variable
print(type(greeting))
print(greeting)
print()
print(type(ultimate_answer))
print(ultimate_answer)
print()
print(type(something_complex))
print(something_complex)
print()
print(type(place))
print(place)
print()
print(type(anti_real_ultimate_answer))
print(anti_real_ultimate_answer)
print()
print(type(class_info))
print(class_info)
print()
print(type(real_ultimate_answer))
print(real_ultimate_answer)