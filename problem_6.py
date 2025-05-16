spaces = int(input("Enter total no. of parking spaces(1 to 100)")) #no. of parking spaces
print("Enter c for occupied space and . for empty space for example C..C for 4 spaces")
yesterday = input("Enter the sequence: ") # checking whether seat is occupied or not c is occupied seat and . is empty seat
today = input("Enter the sequence: ") # checking whether the seat is occupied today or not and the same as yesterday
occupied = 0
for i in range(len(yesterday)):
    if (yesterday[i] == 'C' or yesterday[i] == 'c') and (today[i] == 'C' or today[i] == 'c'):
        occupied = occupied + 1  # the occupied variable should be increased for every match
print("number of spaces occupied on both days: ",occupied)
