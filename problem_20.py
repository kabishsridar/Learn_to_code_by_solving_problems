filein = open('citystate.in', 'r')
fileout = open('citystate.out', 'w')

n = int(filein.readline())
pair_counts = {}

for i in range(n):
    parts = filein.readline().split()
    city = parts[0][:2]
    state = parts[1]

    if city != state:
        key = city + state
        if key not in pair_counts:
            pair_counts[key] = 1
        else:
            pair_counts[key] += 1

total = 0

for key in pair_counts:
    reverse_key = key[2:] + key[:2]
    if reverse_key in pair_counts:
        total += pair_counts[key] * pair_counts[reverse_key]

fileout.write(str(total // 2) + '\n')

filein.close()
fileout.close()
