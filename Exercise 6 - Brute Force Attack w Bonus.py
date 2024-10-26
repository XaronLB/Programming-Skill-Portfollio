atmp=5#base amount of attempts inputing the password
crps="CodingIsCool10"
for i in range(6):
    psw=input("Enter your password: ")#gets a user input for the password
    if psw==crps:
        print("Login Completed")
        break#break the loop when the input is correct
    else:
        if atmp<=1:#Checks if the user has no more attempts left
            print("Number of attempts have been exhausted. Proper authorities have been notified")
            break#break the loop when there is no more attempts left
        elif atmp>=1:
            atmp=atmp-1#subtracts 1 attempt each loop
            print("Password Incorrect Attempts Remaining:", atmp)#informs user how many remaining attempts they have
            
        