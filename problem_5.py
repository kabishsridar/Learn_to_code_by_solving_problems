print('''\nball is in the left cup (1) in beginning
A Swap the left and middle cups
B Swap the middle and right cups
C Swap the left and right cups
''') # it should be printed in terminal so that the user can understand the concept
sequence = input("Enter the sequence(like ABC or BCA by using only A,B,C): ") # get the input from the user for the sequence to move the cup
loc = 1 # as it is mentioned in the question that the ball is in first cup so loc means ball location and it is in 1st cup
for swap in sequence.upper(): # changing the sequence to upper for consistency and it loop through each single character (swap) in the input (sequence) and swap mentioned here is A or B or C 
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
    else: # if something is in the input other than a, b, c it should not return the output
        print(f"Please enter only A, B or C, the letter {swap} is not mentioned in the sequence")
if swap in "abcABC": # checks whether the swap is a,b,c,A,B,C
    print("The ball is in cup ",loc) # displaying the final output
