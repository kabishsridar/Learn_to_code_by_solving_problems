print("Data Plan Programme:") # displaying programme name
mbpm = int(input("Enter amount of mb provided per month: ")) # getting amount of mb provided per month (mbpm indicates mb per month)
months = int(input("Enter the number of months: ")) # getting number of months to calculate

excess = 0 # initiating excess as 0

for i in range(months): # it repeats for every month
    used = int(input(f"Enter amount of mb used in month {i + 1}: "))  # get input from user about amount of mb used in that particular month
    excess = excess + mbpm - used # the remaining mb will be stored in variable named excess

print("The amount of mb for the next month: ",excess + mbpm)
# here we added mbpm again as it indicates the mb allotted for next month including the previous moth excess mb
