print("Data Plan:")
mbpm = int(input("Enter amount of mb provided per month: ")) # get amount of mb provided per month (mbpm indicates mb per month)
months = int(input("Enter the number of months: ")) # get number of months

excess = 0

for i in range(months): # it repeats for every month
    used = int(input(f"Enter amount of mb used in month {i + 1}: "))  # get from user about amount of mb used per month
    excess = excess + mbpm - used # the remaining mb will be stored in variable named excess

print("The amount of mb for the next month: ",excess + mbpm)
# here we added mbpm again as it indicates the mb allotted for next month including the previous moth excess mb
