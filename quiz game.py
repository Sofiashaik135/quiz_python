questions = {"what is python? \n" : "programming language",
"who introduced python? \n" : "Guido van rossum",
"which function takes input in python ?\n" : "input()",
"which function is used to print the text  \n" :"print()",
"which symbol is used for single line comment in python \n": "#"}
questions 
score = 0
for question in questions:
    answer = input(question + " ")
    if answer == questions[question]:
        print("correct")
        score = score + 1

    else:
        print("wrong")


print("final score",score)









