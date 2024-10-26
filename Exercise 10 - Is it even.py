def ooe(n):#stores a function for ooe
    if n%2==0:
        n=1
    else:
        n=0

answer=int(input("Enter your number: "))#gets user input
ooe(n=answer)#calls the function to determine if the userinput is odd or even
if answer==1:
    print("your number is odd")
else:
    print("yournumber is even")