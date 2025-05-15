from bisect import bisect_left, bisect_right
filein = open('baseballin.txt', 'r')
fileout = open('baseballout.txt', 'w')

n = int(filein.readline())
pos = []
for i in range(n):
    pos.append(int(filein.readline()))

pos.sort()

for i in range(n):
    for j in range(i + 1, n):
        first_two_diff = pos[j] - pos[i]
        low = pos[j] +first_two_diff
        high = pos[j] + first_two_diff * 2

        left = bisect_left(pos, low)
        right = bisect_right(pos, high)
        
        total = total + right - left

fileout.write(str(total) + '\n')

filein.close()
fileout.close()