#checks if a given year is a leap year
def is_leap_year(year):
    if year % 4==0:
        if year % 100==0:
            if year % 400==0:
                return True
            else:
                return False
        else:
            return False
    return False
    
x=int(input("Year: "))
print(is_leap_year(x))