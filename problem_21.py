def num_covered(intervals, fired):
    covered = set()
    for i in range(len(intervals)):
        if  i != fired:
            interval = intervals[i]
            for j in range(interval[0], interval[1]):
                covered.add(j)
    return len(covered)

filein = open('lifeguardsin.txt', 'r')
fileout = open('lifegardout.txt', 'w')

n = int(filein.readline())

intervals =[]
for i in range(n):
    interval = filein.readline().split()
    interval[0] = int(interval[0])
    interval[1] = int(interval[1])
    intervals.append(interval)

max_covered = 0

for fired in range(n):
    result= num_covered(intervals,fired)
    if result > max_covered:
        max_covered = result
fileout.write(str(max_covered)+ '\n')

filein.close()
fileout.close()