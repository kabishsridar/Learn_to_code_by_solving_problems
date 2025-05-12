mb = int(input("Enter amount of mb: "))
months = int(input("Enter the number of months: "))

excess = 0
for i in range(months):
    used = int(input(f"Enter amount of mb used in month {i + 1}: "))
    excess = excess + mb - used

print("The amount of mb for the next month: ",excess + mb)