spaces = int(input("Enter total no. of parking spaces(1 to 100): ")) #no. of parking spaces
print("Enter c for occupied space and . for empty space for example C..C for 4 spaces") # explaining the user about this programme
yesterday = input("Enter the sequence: ") # checking whether seat is occupied or not c is occupied seat and . is empty seat
today = input("Enter the sequence: ") # checking whether the seat is occupied today or not and the same as yesterday
occupied = 0
for space in range(len(yesterday)): # loop through the number of characters in yesterday
    if (yesterday[space] == 'C' or yesterday[space] == 'c') and (today[space] == 'C' or today[space] == 'c'): # spacef both yesterday and today's space is occupied, it will increase for every loop
        occupied = occupied + 1  # the occupied variable should be increased for every space
print("number of spaces occupied on both days: ",occupied) # displaying the output
