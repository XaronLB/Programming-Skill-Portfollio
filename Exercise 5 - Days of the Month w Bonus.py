dim= {'January' : 31, 'February' : 28, 'March' : 31, 'April' : 30, 'May' : 31, 'June' : 30, 'July' : 31, 'August' : 31, 'September' : 30, 'October' : 31, 'November' : 30, 'December' : 31}

mth=input("Enter the month: ")
if mth.lower()==("february"):
    lpy=input("Account for leapyear?")#if the user input is february this command line ask if is to consider leapyear or not
    if lpy.lower()==("yes"):
        dim["February"]=29#command line to replace the valua of february on the dictionary if its a leapyear
        print("There are", dim[mth.capitalize()], "days in the month of",  mth.capitalize())
    else:
        print("There are", dim[mth.capitalize()], "days in the month of",  mth.capitalize())
elif mth.lower()==("january"):#this command line and below this is a series of command to print the users month and how many days it has
    print("There are", dim[mth.capitalize()], "days in the month of", mth.capitalize())
elif mth.lower()==("march"):
    print("There are", dim[mth.capitalize()], "days in the month of", mth.capitalize())
elif mth.lower()==("april"):
    print("There are", dim[mth.capitalize()], "days in the month of", mth.capitalize())
elif mth.lower()==("may"):
    print("There are", dim[mth.capitalize()], "days in the month of", mth.capitalize())
elif mth.lower()==("june"):
    print("There are", dim[mth.capitalize()], "days in the month of", mth.capitalize())
elif mth.lower()==("july"):
    print("There are", dim[mth.capitalize()], "days in the month of", mth.capitalize())
elif mth.lower()==("august"):
    print("There are", dim[mth.capitalize()], "days in the month of", mth.capitalize())
elif mth.lower()==("september"):
    print("There are", dim[mth.capitalize()], "days in the month of", mth.capitalize())
elif mth.lower()==("october"):
    print("There are", dim[mth.capitalize()], "days in the month of", mth.capitalize())
elif mth.lower()==("november"):
    print("There are", dim[mth.capitalize()], "days in the month of", mth.capitalize())
elif mth.lower()==("december"):
    print("There are", dim[mth.capitalize()], "days in the month of", mth.capitalize())
