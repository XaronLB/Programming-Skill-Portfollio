print("THE CAPITAL OF EUROPEAN COUNTRIES QUIZ!!!")
scr=0
ans=input("What is the capital of France? ") #one string is enough for the user input for all the answers of the user as it changes after the score tally command
if ans.lower()==("paris"):#upper and capitalized can also be used but lower is faster cause i dont have to press the shift or capslock
    scr=scr+1#command line for updating the users score
ans=input("What is the capital of Germany? ")
if ans.lower()==("berlin"):
    scr=scr+1
ans=input("What is the capital of Russia? ")
if ans.lower()==("moscow"):
    scr=scr+1
ans=input("What is the capital of Poland? ")
if ans.lower()==("warsaw"):
    scr=scr+1
ans=input("What is the capital of Portugal? ")
if ans.lower()==("lisbon"):
    scr=scr+1
ans=input("What is the capital of Netherlands? ")
if ans.lower()==("amsterdam"):
    scr=scr+1
ans=input("What is the capital of Spain? ")
if ans.lower()==("madrid"):
    scr=scr+1
ans=input("What is the capital of Denmark? ")
if ans.lower()==("copenhagen"):
    scr=scr+1
ans=input("What is the capital of Italy? ")
if ans.lower()==("rome"):
    scr=scr+1
ans=input("What is the capital of Finland? ")
if ans.lower()==("helsinki"):
    scr=scr+1

print("Your score is:", scr)
    