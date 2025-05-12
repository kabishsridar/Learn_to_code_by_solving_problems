n = int(input(" Enter the number of villages (at least 3): "))

if n < 3:
    print(" You need at least 3 villages to calculate neighborhoods.")
    exit()

#Get each village's position
positions = []
print("\n Enter the positions of the villages (one per line):")
for i in range(n):
    pos = int(input(f"  Position of village {i+1}: "))
    positions.append(pos)

positions.sort()

min_size = float('inf')

for i in range(1, n - 1):  # exclude the first and last village
    left = positions[i - 1]
    right = positions[i + 1]
    size = (right - left) / 2
    if size < min_size:
        min_size = size

print(f"\n The smallest neighborhood size is: {min_size:.1f}")