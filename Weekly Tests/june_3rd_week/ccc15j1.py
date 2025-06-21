# first month
# next, the date
month = int(input()) # get month and date
date = int(input())

if month ==2 and date == 18: # if it is feb 18th, print special
    print("Special")
elif month <= 2:
    if month == 1: # if month is 1 display before
        print("Before")
    elif month == 2:
        if date <= 18: # if month is 2 and date is before 18, display before
            print("Before")
        elif date > 18 and date < 31: # date is between 19 and 31, then After
            print("After")
        else:
            print("There are only 31 days")
elif month >=3 and month <= 12: # from month 3, print After
    print("After")
else:
    print("There are only 12 months")