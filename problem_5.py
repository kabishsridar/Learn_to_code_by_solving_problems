sequence = input("Enter the sequence: ")

loc = 1
'''ball is in the left cup (1) at starting
A Swap the left and middle cups
B Swap the middle and right cups
C Swap the left and right cups
'''
for i in sequence.upper():
    if i == 'A' and loc == 1:
        loc = 2
    elif i == 'A' and loc == 2:
        loc = 1
    elif i =='B' and loc == 2:
        loc = 3
    elif i == 'B' and loc == 3:
        loc = 2
    elif i == 'C' and loc == 1:
        loc = 3
    elif i=='C' and loc == 3:
        loc = 1

print("The ball is in cup ",loc)