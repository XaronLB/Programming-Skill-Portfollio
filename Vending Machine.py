# This are list and dictionaries to establish the vending machines stock prices so it can be used to be called when needed
menu = ["hot coffee", "hot chocolate", "chai latte", "green tea", "ginger tea", "expresso", "mineral water", "iced coffee", "orange juice", "apple juice", "soda pop", "iced tea", "donut", "buscuits", "chips"]
prices = {"hot coffee": 8, "hot chocolate": 7, "chai latte": 8, "green tea": 4, "ginger tea": 4, "expresso": 8, "mineral water": 2, "iced coffee": 8, "orange juice": 5, "apple juice": 4, "soda pop": 5, "iced tea": 4, "donut": 5, "buscuits": 4, "chips" : 5}
stock = {"hot coffee": 5, "hot chocolate": 5, "chai latte": 5, "green tea": 0, "ginger tea": 4, "expresso": 3, "mineral water": 3, "iced coffee": 5, "orange juice": 2, "apple juice": 1, "soda pop": 2, "iced tea": 1, "donut": 6, "buscuits": 7, "chips" : 5}

#User Interface must be present for users to see first thing
print ("==================================\n==================================\n|-HOT DRINKS-|\n1.Hot Coffee - 8$\n2.Hot Chocolate - 7$\n3.Chai Latte - 8$\n4.Green Tea - 4$\n5.Ginger Tea - 4$\n6.Expresso - 8$\n|-COLD DRINKS-|\n7.Mineral Water - 2$\n8.Iced Coffee - 8$\n9.Orange Juice 5$\n10.Apple Juice - 4$\n11.Soda Pop - 5$\n12.Iced Tea = 4$\n|-SNACKS-|\n13.Donut - 5$\n14.Biscuits - 4$\n15.Chips - 5$\n=================================")

while True:#loop command to prevent an error when entering a string value
    try:
        ordernumber = int(input("Input your order number:"))
    except ValueError:
        print("Invalid order number")
        continue
    else:
        break

#these are establing variables that are gonna be used down the tree of commands
ordernumber = ordernumber-1 #nessecary to offset the value that the user gave so it starts at 0 instead of 1
order = (menu[ordernumber]) 
orderprice = (prices[order])
orderstock = (stock[order])
another = ("none") # this is for establishing the end
cash2 = 0 # i used this to prevent error message that was popping when arriving at the end of the checkout

if orderstock <= 0:
    print ("Sorry we are currently out of", order)#informs the user when the stock of the items is out
    while True:#loop command to prevent an error when entering a string value
       try:
           ordernumber = int(input("Input your order number:"))
       except ValueError:
           print("Invalid order number")
           continue
       else:
           break

#the following set of command lines are for offering different deals for the user such as donut for coffee, i made the suggestions have a deal so users are more incentive to buy it
if ordernumber == 0:# this suggestion triggered when user choose to buy a coffee
    add = input("Would you like order a Donut for dollar off(4$)(yes or no):")#user interface that offers a deal to the user with a discount
    if add == ("yes"):
        orderprice2 = (prices["donut"])
        finalprice = (orderprice+(orderprice2-1))
        print ("That will be", (finalprice),"$")#shows the user how much they will need to complete the purchase
        cash = int(input("Insert cash:"))# asks for user to insert their cash into the machine
        if cash >= finalprice :# checks if the users cash is enough to make the purchase
            change = (cash-finalprice)
            print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n")#User interface to display the change of the user relative to their cash and purchase and also thanking the user
        else:
            while cash < finalprice:# loops the insert cash prompt until the accumalative cash input is enough for the purchase
               short = (cash-finalprice)
               print ("Insufficient funds", short)
               cash2 = int(input("Insert cash:"))
               cash = cash+cash2# adds the previous and current cash thats been inserted into the machine
            if cash >= finalprice:#breaks the loop when there is enough cash that has been inserted
               change = (cash-finalprice)# variable thats called out below this command line
               print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n")# User interface to display the change of the user relative to their cash and purchase and also thanking the user
    elif add == ("no"):
        print ("that will be", orderprice,"$")#displays the price of the purchase without the deal
        another = input("Would you like to purchase another item(yes or no):")#asks user if they wanna add another item in addition to their current one

elif ordernumber == 1:# this suggestion triggered when user choose to buy a Hot Chocolate
    add = input("Would you like order a Biscuit for a dollar off(3$)(yes or no):")#user interface that offers a deal to the user with a discount
    if add == ("yes"):
        orderprice2 = (prices["buscuits"])
        finalprice = (orderprice+(orderprice2-1))
        print ("That will be", (finalprice),"$")#shows the user how much they will need to complete the purchase
        cash = int(input("Insert cash:"))# asks for user to insert their cash into the machine
        if cash >= finalprice :# checks if the users cash is enough to make the purchase
            change = (cash-finalprice)
            print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n")#User interface to display the change of the user relative to their cash and purchase and also thanking the user
        else:
            while cash < finalprice:# loops the insert cash prompt until the accumalative cash input is enough for the purchase
               short = (cash-finalprice)
               print ("Insufficient funds", short)
               cash2 = int(input("Insert cash:"))
               cash = cash+cash2# adds the previous and current cash thats been inserted into the machine
            if cash >= finalprice:#breaks the loop when there is enough cash that has been inserted
               change = (cash-finalprice)# variable thats called out below this command line
               print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n")# User interface to display the change of the user relative to their cash and purchase and also thanking the user
    elif add == ("no"):
        print ("that will be", orderprice,"$")#displays the price of the purchase without the deal
        another = input("Would you like to purchase another item(yes or no):")#asks user if they wanna add another item in addition to their current one

elif ordernumber == 5:# this suggestion triggered when user choose to buy a expresso
    add = input("Would you like order a Donut for dollar off(4$)(yes or no):")#user interface that offers a deal to the user with a discount
    if add == ("yes"):
        orderprice2 = (prices["donut"])
        finalprice = (orderprice+(orderprice2-1))
        print ("That will be", (finalprice),"$")#shows the user how much they will need to complete the purchase
        cash = int(input("Insert cash:"))# asks for user to insert their cash into the machine
        if cash >= finalprice :# checks if the users cash is enough to make the purchase
            change = (cash-finalprice)
            print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n")#User interface to display the change of the user relative to their cash and purchase and also thanking the user
        else:
            while cash < finalprice:# loops the insert cash prompt until the accumalative cash input is enough for the purchase
               short = (cash-finalprice)
               print ("Insufficient funds", short)
               cash2 = int(input("Insert cash:"))
               cash = cash+cash2# adds the previous and current cash thats been inserted into the machine
            if cash >= finalprice:#breaks the loop when there is enough cash that has been inserted
               change = (cash-finalprice)# variable thats called out below this command line
               print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n")# User interface to display the change of the user relative to their cash and purchase and also thanking the user
    elif add == ("no"):
        print ("that will be", orderprice,"$")#displays the price of the purchase without the deal
        another = input("Would you like to purchase another item(yes or no):")#asks user if they wanna add another item in addition to their current one

elif ordernumber == 8:# this suggestion triggered when user choose to buy a orange juice
    add = input("Would you like order a Biscuit for a dollar off(3$)(yes or no):")#user interface that offers a deal to the user with a discount
    if add == ("yes"):
        orderprice2 = (prices["biscuits"])
        finalprice = (orderprice+(orderprice2-1))
        print ("That will be", (finalprice),"$")#shows the user how much they will need to complete the purchase
        cash = int(input("Insert cash:"))# asks for user to insert their cash into the machine
        if cash >= finalprice :# checks if the users cash is enough to make the purchase
            change = (cash-finalprice)
            print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n")#User interface to display the change of the user relative to their cash and purchase and also thanking the user
        else:
            while cash < finalprice:# loops the insert cash prompt until the accumalative cash input is enough for the purchase
               short = (cash-finalprice)
               print ("Insufficient funds", short)
               cash2 = int(input("Insert cash:"))
               cash = cash+cash2# adds the previous and current cash thats been inserted into the machine
            if cash >= finalprice:#breaks the loop when there is enough cash that has been inserted
               change = (cash-finalprice)# variable thats called out below this command line
               print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n")# User interface to display the change of the user relative to their cash and purchase and also thanking the user
    elif add == ("no"):
        print ("that will be", orderprice,"$")#displays the price of the purchase without the deal
        another = input("Would you like to purchase another item(yes or no):")#asks user if they wanna add another item in addition to their current one

elif ordernumber == 9:# this suggestion triggered when user choose to buy a apple juice
    add = input("Would you like order a Biscuit for a dollar off(3$)(yes or no):")#user interface that offers a deal to the user with a discount
    if add == ("yes"):
        orderprice2 = (prices["buscuits"])
        finalprice = (orderprice+(orderprice2-1))
        print ("That will be", (finalprice),"$")#shows the user how much they will need to complete the purchase
        cash = int(input("Insert cash:"))# asks for user to insert their cash into the machine
        if cash >= finalprice :# checks if the users cash is enough to make the purchase
            change = (cash-finalprice)
            print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n")#User interface to display the change of the user relative to their cash and purchase and also thanking the user
        else:
            while cash < finalprice:# loops the insert cash prompt until the accumalative cash input is enough for the purchase
               short = (cash-finalprice)
               print ("Insufficient funds", short)
               cash2 = int(input("Insert cash:"))
               cash = cash+cash2# adds the previous and current cash thats been inserted into the machine
            if cash >= finalprice:#breaks the loop when there is enough cash that has been inserted
               change = (cash-finalprice)# variable thats called out below this command line
               print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n")# User interface to display the change of the user relative to their cash and purchase and also thanking the user
    elif add == ("no"):
        print ("that will be", orderprice,"$")#displays the price of the purchase without the deal
        another = input("Would you like to purchase another item(yes or no):")#asks user if they wanna add another item in addition to their current one

elif ordernumber == 10:# this suggestion triggered when user choose to buy a soda pop
    add = input("Would you like order a Chips for a dollar off(4$)(yes or no):")#user interface that offers a deal to the user with a discount
    if add == ("yes"):
        orderprice2 = (prices["chips"])
        finalprice = (orderprice+(orderprice2-1))
        print ("That will be", (finalprice),"$")#shows the user how much they will need to complete the purchase
        cash = int(input("Insert cash:"))# asks for user to insert their cash into the machine
        if cash >= finalprice :# checks if the users cash is enough to make the purchase
            change = (cash-finalprice)
            print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n")#User interface to display the change of the user relative to their cash and purchase and also thanking the user
        else:
            while cash < finalprice:# loops the insert cash prompt until the accumalative cash input is enough for the purchase
               short = (cash-finalprice)
               print ("Insufficient funds", short)
               cash2 = int(input("Insert cash:"))
               cash = cash+cash2# adds the previous and current cash thats been inserted into the machine
            if cash >= finalprice:#breaks the loop when there is enough cash that has been inserted
               change = (cash-finalprice)# variable thats called out below this command line
               print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n")# User interface to display the change of the user relative to their cash and purchase and also thanking the user
    elif add == ("no"):
        print ("that will be", orderprice,"$")#displays the price of the purchase without the deal
        another = input("Would you like to purchase another item(yes or no):")#asks user if they wanna add another item in addition to their current one
            
else:
    print ("that will be", orderprice,"$")
    another = input("Would you like to purchase another item:")


if another.lower()==("yes"):
    print ("==================================\n==================================\n|-HOT DRINKS-|\n1.Hot Coffee - 8$\n2.Hot Chocolate - 7$\n3.Chai Latte - 8$\n4.Green Tea - 4$\n5.Ginger Tea - 4$\n6.Expresso - 8$\n|-COLD DRINKS-|\n7.Mineral Water - 2$\n8.Iced Coffee - 8$\n9.Orange Juice 5$\n10.Apple Juice - 4$\n11.Soda Pop - 5$\n12.Iced Tea = 4$\n|-SNACKS-|\n13.Donut - 5$\n14.Biscuits - 4$\n15.Chips - 5$\n=================================")
    while True:#loop command to prevent an error when entering a string value
        try:
            ordernumber2 = int(input("Input your order number:"))
        except ValueError:
            print("Invalid order number")
            continue
        else:
            break    
    
    ordernumber2

    while ordernumber2 <= 0 or ordernumber2 >= 15:#establish a loop until the required input is met so that it only register an input that has an output
        ordernumber2 = int(input("Invalid Order\nInput your order number:"))

    #establish a couple of variables for the second item
    order2 = (menu[ordernumber2])
    orderprice2 = (prices[order2])
    orderstock2 = (stock[order2])

    while orderstock2 <= 0:
        print ("Sorry we are currently out of", order)#informs the user when the stock of the items is out
        while True:#loop command to prevent an error when entering a string value
            try:
                ordernumber2 = int(input("Input your order number:"))
            except ValueError:
                print("Invalid order number")
                continue
            else:
                break

    print("that will be", (orderprice+orderprice2))#shows user the total amount of the purchase
    cash = int(input("Insert cash:"))
    while cash < orderprice:# loops the insert cash prompt until the accumalative cash input is enough for the purchase
        short = (cash-orderprice)
        print ("Insufficient funds", short)
        cash2 = int(input("Insert cash:"))
        cash = cash+cash2# adds the previous and current cash thats been inserted into the machine
    if cash >= orderprice:#breaks the loop when there is enough cash that has been inserted
        change = (cash-orderprice)# variable thats called out below this command line
        print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n \n=================================")# User interface to display the change of the user relative to their cash and purchase and also thanking the user

elif another.lower()==("no"):
    cash = int(input("Insert cash:"))
    while cash < orderprice:# loops the insert cash prompt until the accumalative cash input is enough for the purchase
        short = (cash-orderprice)
        print ("Insufficient funds", short)
        cash2 = int(input("Insert cash:"))
        cash = cash+cash2# adds the previous and current cash thats been inserted into the machine
    if cash >= orderprice:#breaks the loop when there is enough cash that has been inserted
        change = (cash-orderprice)# variable thats called out below this command line
        print ("=================================\n \nThank you for your purchase\nYour change is :", change,"$\n \n=================================")# User interface to display the change of the user relative to their cash and purchase and also thanking the user

     
elif another.lower()==("none"):
    print ("==================================")