# first get all the input from user for all type of shots and store it.
Apples_3 = int(input("Enter number of successful three-point shots for the Apples: ")) 
Apples_2 = int(input("Enter number of successful two-point shots for the Apples: "))
Apples_1 = int(input("Enter number of successful one-point free throw for the Apples: "))

Bananas_3 = int(input("Enter number of successful three-point shots for the Bananas: "))
Bananas_2 = int(input("Enter number of successful two-point shots for the Bananas: "))
Bananas_1 = int(input("Enter number of successful one-point free throw for the Banana: "))

# Here three point shots represent that for one shot the number of points we get will be multiplied by three
# For two point shots the number of points we get will be multiplied by two
# For one point shot the number of point we get will be multiplied by one

Apples_total = Apples_3 *3 + Apples_2 * 2 + Apples_1 * 1  # apples_3 is multiplied by 3 because it is a three point shot, apples_2 is multiplied by 2 for 2 point shots and apples_1 is multiplied by 1 for one point shot
Bananas_total = Bananas_3*3 + Bananas_2 * 2 + Bananas_1 * 1  # the same phenomenon like apples for bananas

if Apples_total > Bananas_total:  # checking the condition if apples_total is higher than bananas_total it should print apples won
    print("Apples Won")
elif Bananas_total> Apples_total: # checking the condition if bananas_total is higher than apples_total it should print bananas won
    print("Bananas won")
else:
    print("Tie")  # if both are in the same point it returns tie, it returns only when both the if and elif character is false
