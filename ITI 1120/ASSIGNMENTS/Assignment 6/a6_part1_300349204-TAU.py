import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    while True:
        try:
            file=input("Enter the name of a file: ").strip()
            fp=open(file).read()
            return fp
        except FileNotFoundError:
            print("File not found. Please try again.")
        except:
            print("Error. Please try again.")

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    d={}
    lines = fp.splitlines()
    words = [line.split() for line in lines]
    for i in range(len(words)):
        for j in range(len(words[i])):
            words[i][j]=words[i][j].strip(string.punctuation).lower()
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] not in d:
                d[words[i][j]]=[i+1]
            else:
                d[words[i][j]].append(i+1)
    for i in d:
        d[i]=set(d[i])
    return d

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    l = []
    query = query.strip(string.punctuation).lower()
    query = query.split()
    for i in query:
        if query[query.index(i)] in D:
            l.append(D[query[query.index(i)]])
    coexistance = list(l[-1])
    return coexistance

##############################
# main
##############################
# file=open_file()
# d=read_file(file)
# query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# # YOUR CODE GOES HERE
# find_coexistance(d,query)
# while query!='q':
#     l=find_coexistance(d,query)
#     if len(l)==0:
#         print("Word co-occurance for",query,"not found")
#     else:
#         print("Words that co-occur with",query,":")
#         for word in l:
#             print(word,end=' ')
#         print()
#     query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
# print("Thanks for using the program. Bye!")
