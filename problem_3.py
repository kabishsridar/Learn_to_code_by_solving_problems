Apples_3 = int(input("Enter number of successful three-point shots for the Apples: ")) 
Apples_2 = int(input("Enter number of successful two-point shots for the Apples: "))
Apples_1 = int(input("Enter number of successful one-point free throw for the Apples: "))

Bananas_3 = int(input("Enter number of successful three-point shots for the Bananas: "))
Bananas_2 = int(input("Enter number of successful two-point shots for the Bananas: "))
Bananas_1 = int(input("Enter number of successful one-point free throw for the Banana: "))

Apples_total = Apples_3 *3 + Apples_2 * 2 + Apples_1 *1 #apples_3 is multiplied by 3 because it is a three point shot same as for rest of those 
Bananas_total = Bananas_3*3 + Bananas_2 * 2 + Bananas_1 * 1

if Apples_total > Bananas_total:
    print("Apples Won")
elif Bananas_total> Apples_total:
    print("Bananas won")
else:
    print("Tie")