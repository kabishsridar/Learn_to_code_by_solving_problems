input_data = input("Enter number of franchisees and number of days (separated by a space): ") # prompt the user for number of franchisees and number of days
lst = input_data.split() # split the data and store it as lst
f = int(lst[0])  # Number of franchisees (column)
d = int(lst[1])  # Number of days (row)

grid = [] # initiating grid as an empty list

for day_index in range(d): # loop through each days
    while True: # it breaks if the else statement executes
        # get input for sales data for the current day
        row_input = input(f"Enter sales for Day {day_index + 1} (space-separated for {f} franchisees): ").split() # convert into list and split it

        # Check that the user entered the correct number of values
        if len(row_input) != f:
            print(f"You must enter exactly {f} numbers. Try again.")
        else:
            row = [] # initiating row as an empty list
            for value in row_input: # loop through each sales data
                row.append(int(value)) # append those data to row
            grid.append(row) # append row to grid
            break

bonus = 0 # initiating bonus as 0

for day_index in range(d): # loop through each days
    day = grid[day_index]
    total = 0 # initiating total as 0
    for sale in day: 
        total += sale  # Sum all sales for the current day
    if total % 13 == 0:
        bonus += total // 13  # Add bonus if total is divisible by 13

# Calculate bonus from total franchisee sales
for i in range(f): # loop through each franchisee
    total = 0 # initiate total as 0
    for j in range(d): # loop through days
        total += grid[j][i]
    if total % 13 == 0:
        bonus += total // 13  # Add bonus if total is divisible by 13

print("Total bonus awarded:", bonus)
