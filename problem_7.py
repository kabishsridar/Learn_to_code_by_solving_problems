x = int(input("Enter amount of mb: "))
n = int(input("Enter the number of months: "))

excess = 0
for i in range(n):
    used = int(input(f"Enter amount of mb used in month {i + 1}: "))
    excess = excess + x - used

print("The amount of mb for the next month: ",excess + x)
