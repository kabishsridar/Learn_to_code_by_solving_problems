filein = open('citystatein.txt', 'r') # opening the file in read mode
fileout = open('citystateout.txt', 'w') # opening the file in write mode

n = int(filein.readline()) # reads the first line(number of cities) and store as integer.
pair_counts = {}

for i in range(n): # loop to each city and state combination
    parts = filein.readline().split() # split city and state
    city = parts[0][:2] # get first two characters of city
    state = parts[1]

    if city != state: # if city bbrevation not same as state abbrevation
        key = city + state # creating a key combining state and city abbrevation
        if key not in pair_counts:
            pair_counts[key] = 1
        else:
            pair_counts[key] += 1

total = 0

for key in pair_counts: # Loop through all the keys in the dictionary
    reverse_key = key[2:] + key[:2] # Generate the reverse key by swapping city and state abbrevations
    if reverse_key in pair_counts: # If the reverse key exists, it forms a special pair
        total += pair_counts[key] * pair_counts[reverse_key] # Add the product of the counts for the current key and its reverse key to total

fileout.write(str(total // 2) + '\n')

# closing the files
filein.close()
fileout.close()
