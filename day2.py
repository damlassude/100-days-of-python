#tip calculator
print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12 or 15? "))
split=int(input("How many people to split the bill? "))
total=(bill+(bill*tip/100))/split
total=round(total, 2)
print("Each person should pay: $"+str(total))