import math
import random

def generate_books_list(file_path):
    file_lines = open(file_path).read().splitlines()
    raw_data = []
    book_data=[]
    final_data=[]
    for line in file_lines:
        raw_data.append(line.split('\t'))
    for item in raw_data:
        book_data=[]
        date_format = ''
        date_format+=((str((item[3].replace('/','-').split('-')[2])))+'-')
        date_format+=((str((item[3].replace('/','-').split('-')[0])))+'-')
        date_format+=str((item[3].replace('/','-').split('-')[1]))
        book_data.append(date_format)
        book_data.append(item[0])
        book_data.append(item[1])
        book_data.append(item[2])
        book_data.append(item[4])
        final_data.append(book_data)
    return final_data

def find_books_by_year(book_list,start_year,end_year):
    year_range = list(range(start_year,end_year+1))
    print("All titles between {} and {}:\n".format(start_year, end_year))
    for book in book_list:
        book_year = (book[0].split('-')[0])
        if int(book_year) in year_range:
            print(book[1] + ', by ' + book[2] + ' (' + book[0] + ')')

book_list=generate_books_list('NYT_short.txt')
find_books_by_year(book_list,1945,1999)