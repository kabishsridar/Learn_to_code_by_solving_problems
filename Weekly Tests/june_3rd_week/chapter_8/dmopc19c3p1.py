# find the number which repeats more
n = int(input()) # prompt for number of digits
numbers = input().split() # get the digits space seperated

numbers_lst = [] # initiate number_lst as an empty list

for num in numbers: # loop through each numbers in the list
    numbers_lst.append(int(num)) # append them to numbers_lst after converting as an integer

count = {} # initiating count as an empty dictionary
for num in numbers_lst: # loop through each number in the list
    if num in count: # if already exists, increment count by 1
        count[num] += 1
    else:
        count[num] = 1 # if not, set it to 1
max_count = max(count.values()) # get the maximum count in the values

modes = [] # initiate modes as an empty list
for num, freq in count.items():
    if freq == max_count: # if the frequency is the maximum count, then append the key(num) to the modes
        modes.append(num)
modes.sort() # sort it

for mode in modes:
    print(mode) # display it