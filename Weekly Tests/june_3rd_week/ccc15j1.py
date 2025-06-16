# first month
# next date
month = int(input())
date = int(input())

if month ==2 and date == 18:
    print("Special")
elif month <= 2:
    if month == 1:
        print("Before")
    elif month == 2:
        if date <= 18:
            print("Before")
        elif date > 18 and date < 31:
            print("After")
        else:
            print("There are only 31 days")
elif month >=3 and month <= 12:
    print("After")
else:
    print("There are only 12 months")