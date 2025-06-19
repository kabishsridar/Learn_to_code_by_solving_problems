fin = open('Weekly Tests//june_3rd_week//lostcowin.txt', 'r') # open the input file
fout = open('lostcowout.py', 'w') # create or open the file

values = fin.readline().split() # read the file and split, then store it to values
x = int(values[0]) # the first index will be x and the next will be y
y = int(values[1])

dist = 0
pos = x # john's current position
direction = 1  # left to right is 1
step = 1 # step is how much steps farmer john moves

# distance will be doubled as 1, 2, 4, 8, etc..
while True:
    target = pos + direction * step
    # checking if y is between pos and target, then add the distance and then break
    if (pos <= y <= target) or (pos >= y >= target):
        dist += abs(pos - y)
        break
    else: # john moves to the target
        dist += abs(pos - target)
        pos = target # he reaches target
        dist += abs(pos - x) # return to the starting point
        pos = x # set the point where he started 
        step = step * 2 # for each time, distance should be double
        direction = -1 * direction # moves in the opposite direction

fout.write(str(dist)) # write the distance travelled be john to the output file