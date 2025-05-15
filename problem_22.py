filein = open("skidesign.in", "r")
fileout = open("skidesign.out", "w")

n = int(filein.readline())

heights = []

for i in range(n):
        h = int(filein.readline())
        heights.append(h)

min_cost = float('inf')

for low in range(0, 84):
    high = low + 17
    cost = 0

    for h in heights:
        if h < low:
            cost += (low - h) ** 2
        elif h > high:
            cost += (h - high) ** 2

    if cost < min_cost:
        min_cost = cost

fileout.write(str(min_cost) + "\n")