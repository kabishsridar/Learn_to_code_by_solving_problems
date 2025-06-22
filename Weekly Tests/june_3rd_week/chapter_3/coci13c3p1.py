# A converted to B
# B converted to BA
# got the idea through comments to track only letter counts and not the letters
presses = int(input()) # number of presses
a_count = 1 # initialising first it is A
b_count = 0

for changes in range(presses): # loop through each presses
    new_a_count = b_count # after one press a bcount will be the new a count
    new_b_count = a_count + b_count # the new b count will be the sum of both counts
    
    a_count = new_a_count
    b_count = new_b_count
print(a_count, b_count) # display the output