n = int(input("Enter the number of villages (at least 3): "))  # get number of villages from user

if n < 3:
    print(" You need at least 3 villages to calculate neighborhoods.")
    exit() # it should exit if n is less than 3

#Get each village's position
positions = []
print("\nEnter the positions of the villages (one per line):")
for i in range(n): # repeats for every village
    pos = int(input(f"Position of village {i+1}: "))
    positions.append(pos) # the position of village will be added to positions

positions.sort()

min_size = float('inf')

for i in range(1, n - 1):  # exclude the first and last village
    previous= positions[i - 1]
    next = positions[i + 1]
    size = (next - previous) / 2

    if size < min_size: 
        min_size = size

print(f" The smallest neighborhood size is: {min_size:.1f}")
