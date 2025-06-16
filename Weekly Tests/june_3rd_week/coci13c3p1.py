# A converted to B
# B converted to BA
# got the idea through comments to track only letter counts and not the letters
presses = int(input())
a_count = 1
b_count = 0

for changes in range(presses):
    new_a_count = b_count
    new_b_count = a_count + b_count
    
    a_count = new_a_count
    b_count = new_b_count
print(a_count, b_count)