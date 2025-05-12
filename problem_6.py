seats = int(input()) #no. of seats
yesterday = input() # checking whether seat is occupied or not c is occupied seat and . is empty seat
today = input()
occupied = 0
for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied = occupied + 1
print(occupied)