from bisect import bisect_left, bisect_right # importing the module named bisect for binary search
filein = open('baseballin.txt', 'r') # opening file in read mode
fileout = open('baseballout.txt', 'w') # opening file in write mode

n = int(filein.readline()) # reading first line to find number of cows 
pos = [] # initiating pos as an empty list
for i in range(n):  # loop through each cows
    pos.append(int(filein.readline())) # append the first line to pos

pos.sort() # sorting in ascending order

for i in range(n): # track our index where we are at
    for j in range(i + 1, n): # Iterate through all possible second positions in the sorted list
        first_two_diff = pos[j] - pos[i]
        low = pos[j] +first_two_diff
        high = pos[j] + first_two_diff * 2

        left = bisect_left(pos, low) # this is used instead of while loops to find left border
        right = bisect_right(pos, high) # this is used instead of while loops to find right border
        
        total = total + right - left

fileout.write(str(total) + '\n') # writing to the file lifeguardsout.txt

# closing the files
filein.close()
fileout.close()
