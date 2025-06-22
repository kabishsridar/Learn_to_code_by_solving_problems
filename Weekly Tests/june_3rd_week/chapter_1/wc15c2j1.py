num_far = int(input()) # prompt number of far
output = ""
for i in range(num_far): # loop for number of fars
    if i == num_far - 1: # the comma should not be printed for the last far
        output += "far"
    else:
        output += "far, " # comma to be printed on rest of the far
print(f"A long time ago in a galaxy {output} away...") # displaying the final output