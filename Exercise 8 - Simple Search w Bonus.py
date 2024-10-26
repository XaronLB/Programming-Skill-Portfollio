n=("Jake Roberts", "Zac Efron", "Ian Hecox", "Ron Henley", "Sam Bowie", "Dave Batista")
s=input("Search name: ")

""" this block compares the value of the list to the input given by the user the commands accounts for capitalization of userinput"""
if s.lower()==("jake") or s.lower()==("roberts") or s.lower()==n[0].lower():
    print("Found:", n[0])
elif s.lower()==("zac") or s.lower()==("efron") or s.lower()==n[1].lower():
    print("Found:", n[1])
elif s.lower()==("ian") or s.lower()==("hecox") or s.lower()==n[2].lower():
    print("Found:", n[2])
elif s.lower()==("ron") or s.lower()==("henley") or s.lower()==n[3].lower():
    print("Found:", n[3])
elif s.lower()==("sam") or s.lower()==("bowie") or s.lower()==n[4].lower():
    print("Found:", n[4])
elif s.lower()==("dave") or s.lower()==("batista") or s.lower()==n[5].lower():
    print("Found:", n[5])
else:
    print("Nothing Found")