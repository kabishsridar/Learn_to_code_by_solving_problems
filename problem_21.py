def num_covered(intervals, fired):
    covered = set()
    for i in range(len(intervals)): # Loop through all lifeguards' intervals
        if  i != fired: # Skip the lifeguard who is fired
            interval = intervals[i]
            for j in range(interval[0], interval[1]): # Loop through each time unit covered by the current lifeguard's interval
                covered.add(j)
    return len(covered)

filein = open('lifeguardsin.txt', 'r') # opening file in read mode
fileout = open('lifegardout.txt', 'w') # opening file in write mode

n = int(filein.readline()) # read first line (number of lifeguards)

intervals =[]

for i in range(n):
    interval = filein.readline().split() # Read the interval (start, end)
    interval[0] = int(interval[0]) # convert start time to integer
    interval[1] = int(interval[1]) # convert stop time to integer
    intervals.append(interval)

max_covered = 0

for fired in range(n): # repeat for each lifeguards
    result= num_covered(intervals,fired)
    if result > max_covered:
        max_covered = result
fileout.write(str(max_covered)+ '\n') # write to lifeguarsout file

# closing the files
filein.close()
fileout.close()
