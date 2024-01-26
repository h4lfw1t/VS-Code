import random

# To open a file, use the open() function.
# The open() function returns a file object, which has a read() method for reading t#he content of the file.
# Follow the open() function with the name of the file you want to open in quotes and the read() function to view the file as a large string.

lines=open("lec.15.quiz.csv").read().splitlines()

def ask_question(q):
    print()
    print(q[5])
    print("Difficulty:",q[6])
    print(q[0])
    for i in range(1,5):
        print(i,q[i])

def read_answer_raw():
    # while True:
    #     answer=input("Enter your answer: ")
    #     if answer in ["1","2","3","4"]:
    #         return answer
    #     else:
    #         print("Invalid answer. Try again.")
    try:
        ans=int(input("Enter your answer: "))
        return ans
    except:
        print("Error. The answer must be a number between 1 and 4. Try again.")

# the try: block lets you test a block of code for errors.
# the except: block lets you handle the error.
# the finally: block lets you execute code, regardless of the result of the try- and except blocks.
# except ValueError: executes if the user enters a non-integer value.
# except ZeroDivisionError: executes if the user enters 0 as the denominator.

def read_answer():
    ans=read_answer_raw()
    while ans not in [1,2,3,4]:
        print("Invalid answer. Try again.")
        ans=read_answer_raw()
    return ans

questions=[]
for line in lines:
    #line contains info about one question
    question=line.split("\t")
    questions.append(question)

# questions[0] contains the question
# questions[1-4] contains the answers
# questions[1] is the correct answer
# questions[5] contains the category
# questions[6] contains the difficulty/point value

score=0
tries=3
while tries>0:
    q=random.choice(questions)
    ask_question(q)
    ans=read_answer()
    if ans==1:
        print("Correct!")
        score=score+int(q[6])
        print("Score:",score)
    else:
        print("Incorrect. The correct answer is",q[1])
        tries=tries-1
        print("Tries remaining:",tries)
print("Game over. Your score is",score)