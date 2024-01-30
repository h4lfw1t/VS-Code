'''
Filename: LEC_8.py
Author: Patrick Geraghty
Date Created: 2023-01-30
Date Modified: 2023-01-30
Description: Defines a function that prints a two-dimensional list containg the elements of a 12x12 multiplication table.
'''
def mult_table():
    split_list = []
    master_list = []
    for i in range(12):
        for j in range(12):
            split_list.append((i+1) * (j+1))

    for i in range(0, len(split_list), 12):
        master_list.append(split_list[i:i+12])

    print(master_list)
