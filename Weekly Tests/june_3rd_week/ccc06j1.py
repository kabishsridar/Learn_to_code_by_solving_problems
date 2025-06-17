total = 0
burger = int(input()) # get input for type of food and add the respective calories to the total
if burger == 1:
    total += 461
elif burger == 2:
    total += 431
elif burger == 3:
    total += 420
elif burger == 4:
    pass
else:
    print("Enter valid integer")

side = int(input())
if side == 1:
    total += 100
elif side == 2:
    total += 57
elif side == 3:
    total += 70
elif side == 4:
    pass
else:
    print("Enter valid integer")

drink = int(input())
if drink == 1:
    total += 130
elif drink == 2:
    total += 160
elif drink == 3:
    total += 118
elif drink == 4:
    pass
else:
    print("Enter valid integer")

dessert = int(input())
if dessert == 1:
    total += 167
elif dessert == 2:
    total += 266
elif dessert == 3:
    total += 75
elif dessert == 4:
    pass
else:
    print("Enter valid integer")

print(f"Your total Calorie count is {total}.") # display the total calories