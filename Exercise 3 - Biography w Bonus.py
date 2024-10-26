dc={"Name" : "Xavier", "Hometown" : "Sharjah", "Age" : 24}

name=input("Enter your name: ")
dc["Name"]=name#replaces the key of name with the user input
hometown=input("Enter your hometown: ")
dc["Hometown"]=hometown#replaces the key of hometown with the user input
while True:
    age = input("Enter your age: ")
    try:
        int(age)#breaks the loop when the user input is an interger 
        dc["Age"]=age#replaces the key of age with the user input
        print(dc)
        break
    except ValueError:#command line for looping when error occurs
        print("Age must be NUMERICAL i.e. 20")#this is a looping message for the user to input an interger value
