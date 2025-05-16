line = input("Enter number of franchisees and number of days (separated by a space): ")
lst = line.split()
f = int(lst[0])  # Number of franchisees (column)
d = int(lst[1])  # Number of days (row)

grid = []

for day_index in range(d):
    while True:
        # get input for sales data for the current day
        row_input = input(f"Enter sales for Day {day_index + 1} (space-separated for {f} franchisees): ").split()

        # Check that the user entered the correct number of values
        if len(row_input) != f:
            print(f"You must enter exactly {f} numbers. Try again.")
        else:
            row = []
            for value in row_input:
                row.append(int(value))
            grid.append(row)
            break

bonus = 0 

for day_index in range(d):
    day = grid[day_index]
    total = 0
    for sale in day:
        total += sale  # Sum all sales for the current day
    if total % 13 == 0:
        bonus += total // 13  # Add bonus if total is divisible by 13

# Calculate bonus from total franchisee sales
for i in range(f):
    total = 0
    for j in range(d):
        total += grid[j][i]
    if total % 13 == 0:
        bonus += total // 13  # Add bonus if total is divisible by 13

print("Total bonus awarded:", bonus)