n = int(input("Enter the number of villages (at least 3): "))  # get number of villages from user

if n < 3:
    print(" You need at least 3 villages to calculate neighborhoods.")
    exit() # it should exit if n is less than 3 as if the number of villlages is less than 3, we cannot calculate neighbourhoods

#Get each village's position
positions = [] # initiating positions as an empty list
print("\nEnter the positions of the villages (one per line):") # prompt the user for positions of villages one by one
for i in range(n): # repeats for every village
    pos = int(input(f"Position of village {i+1}: ")) # prompt for the position of each villag one by one
    positions.append(pos) # the position of each village will be appended to positions

positions.sort() # arranging them in an order to calculate

min_size = float('inf') # setting min_size to infinity as a starting value to find the smallest neighborhood size

for i in range(1, n - 1):  # exclude the first and last village because the first village doesn't has previous village whereas the last village doesn't has the next village
    previous= positions[i - 1]  # getting the previous village's position
    next = positions[i + 1]  # getting the next village's position
    size = (next - previous) / 2

    if size < min_size:  # update min_size if a smaller neighborhood size is found
        min_size = size

print(f" The smallest neighborhood size is: {min_size:.1f}")
