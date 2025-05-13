line = input("Enter number of franchisees and number of days (separated by a space): ")
lst = line.split()
f = int(lst[0])
d = int(lst[1])

grid = []

for day_index in range(d):
    while True:
        row_input = input(f"Enter sales for Day {day_index + 1} (space-separated for {f} franchisees): ").split()
        if len(row_input) != f:
            print(f"You must enter exactly {f} numbers. Try again.")
        else:
            row = []
            for value in row_input:
                row.append(int(value))
            grid.append(row)
            break

bonus = 0

# Bonus from total sales per day (row-wise)
for day_index in range(d):
    day = grid[day_index]
    total = 0
    for sale in day:
        total += sale
    if total % 13 == 0:
        bonus += total // 13

# Bonus from total sales per franchisee (column-wise)
for i in range(f):
    total = 0
    for j in range(d):
        total += grid[j][i]
    if total % 13 == 0:
        bonus += total // 13

print("Total bonus awarded:", bonus)