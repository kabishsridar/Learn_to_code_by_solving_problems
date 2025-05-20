nm = input("Enter length and number of relatives separated by space (1 to 100000): ").split() # prompting user for length and number of relatives and split them to list
n = int(nm[0]) # the irst item is length, so storing it as n
m = int(nm[1]) # the second item is the number of relatives storing as m

scarf = input("Enter the scarf pattern as space-separated numbers: ").split() # prompting the user for scarf pattern seperated by space
for i in range(n): # loop through each foot of scarf
    scarf[i] = int(scarf[i]) # converting string to integer

leftmost_index = {} # initiating leftmost_index as an empty dictionary to track each color
rightmost_index = {} # initiating rightmost_index as an empty dictionary to track each color

for i in range(n): # loop through each foot
    color = scarf[i] #
    if color not in leftmost_index: # if the color of current foot never seen before, then current index serves as both leftmost and rightmost_index of this color
        leftmost_index[color] = i
        rightmost_index[color] = i
    else:
        rightmost_index[color] = i # else update only rightmost_index because we found an index to the right of old one

max_length = 0 # initiating max_length as 0

for i in range(m): # iterate for each relative
    relative = input(f"Enter relative {i+1} range (first and last color index separated by space): ").split() # prompt the user for range
    first = int(relative[0]) # assigning fist color index as first
    last = int(relative[1]) # assigning last color index as last
    if first in leftmost_index and last in leftmost_index:  # The maximum length of the desired scarf is the rightmost index of the color of the last foot, minus the leftmost index of the color of the first foot, plus one.
        length = rightmost_index[last] - leftmost_index[first] + 1
        if length > max_length:
            max_length = length

print("Maximum length of scarf:", max_length) # displaying the final output