print('''ball is in the left cup (1) in beginning
A Swap the left and middle cups
B Swap the middle and right cups
C Swap the left and right cups
''') # it should be printed in terminal so that the user can understand the concept
sequence = input("Enter the sequence(like ABC or BCA by using only A,B,C): ")
loc = 1 # as it is mentioned that the ball is in first cup so loc means ball location
for swap in sequence.upper():
    if swap == 'A' and loc == 1:
        loc = 2
    elif swap == 'A' and loc == 2:
        loc = 1  # it is given so that if A repeats 2 or 3 times the location should change
    elif swap =='B' and loc == 2:
        loc = 3
    elif swap == 'B' and loc == 3:
        loc = 2
    elif swap == 'C' and loc == 1:
        loc = 3
    elif swap=='C' and loc == 3:
        loc = 1

print("The ball is in cup ",loc)
