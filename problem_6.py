seats = int(input("Enter total no. of seats")) #no. of seats
print("Enter c for occupied seat and . for empty seat for example C..C for 4 seats")
yesterday = input("Enter the sequence: ") # checking whether seat is occupied or not c is occupied seat and . is empty seat
today = input("Enter the sequence: ")
occupied = 0
for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied = occupied + 1
print(occupied)