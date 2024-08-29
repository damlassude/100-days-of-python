print("Welcome to Python Pizza Deliveries!")
size=input("What size do you want your pizza? S,M or L: ")
pepperoni=input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese=input("Do you want extra cheese? Y or N: ")

if size=="S":
    bill=15
    if pepperoni=="Y":
        bill+=2
elif size=="M":
    bill=20
    if pepperoni=="Y":
        bill+=3
    if extra_cheese=="Y":
        bill+=1
elif size=="L":
    bill=25
    if pepperoni=="Y":
        bill+=3
    if extra_cheese=="Y":
        bill+=1
print("Your bill is $"+str(bill))