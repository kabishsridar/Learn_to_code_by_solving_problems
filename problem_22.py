filein = open("skidesign.in", "r") # opening file in read mode
fileout = open("skidesign.out", "w") # opening file in write mode

n = int(filein.readline()) # read first line(number of heights)

heights = [] # initiating heights to an empty list

for i in range(n): # read next n lines and append each height to the list
        h = int(filein.readline()) # read height and convert to integer
        heights.append(h) # append height(h) to list heights

min_cost = float('inf') # assigning min_cost to infinity

for low in range(0, 84): # Loop from 0 to 83 (since high = low + 17)
    high = low + 17 # Set high to 17 more than the low
    cost = 0 # initiating cost as 0

    for h in heights:  # Loop through each height to calculate the cost for making all the heights fall within the range [low, high]
        if h < low:  # If the height is below the lower bound, calculate the cost of raising it to the low value
            cost += (low - h) ** 2
        elif h > high:  # If the height is above the upper bound, calculate the cost of lowering it to the high value
            cost += (h - high) ** 2

    if cost < min_cost:  # If the cost for the current low-high range is less than the previously recorded minimum cost, update min_cost
        min_cost = cost

fileout.write(str(min_cost) + "\n") # write the min_cost and add a new line to the file fileout.txt 
