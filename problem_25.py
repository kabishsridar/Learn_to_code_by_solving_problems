# Get ribbon length and number of paint strokes from the user
ns = input("Enter the length of ribbon and number of paint strokes (separated by a space between 1 and 100000): ").split()
n = int(ns[0])  # Ribbon length
stroke = int(ns[1])  # Number of paint strokes

ribbon = [0] * n  # 0 means purple, 1 means blue

# Process each paint stroke
for i in range(stroke):
    position_range = input("Enter starting and ending position of painting stroke separated by a space: ").split()
    starting_position = int(position_range[0])
    ending_position = int(position_range[1])

    # Mark the positions as painted (blue)
    for j in range(starting_position, ending_position):
        ribbon[j] = 1  # Change to blue

# Calculate the results
purple_units = ribbon.count(0)
blue_units = ribbon.count(1)

# Print the output
print(purple_units, blue_units)
