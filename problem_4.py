num1=int(input("First Integer: "))  # getting the integers one by one and be stored as a variable
num2=int(input("Second Integer: "))
num3=int(input("Third Integer: "))
num4=int(input("Fourth Integer: "))

print(num1,num2,num3,num4)
if (num1==8 or num1==9) and (num4==8 or num4==9) and (num3==num2): # it checks and prints ignore if the first and last numbers are either 8 or 9 and also the second and third numbers are same
    print("ignore")
else:
    print("answer")  #it prints answer if the if statement is false
'''
We can also use the below format by using split function so that the user can type in single line and it can be faster
num = input("enter four number with seperating by spaces: ")  # the user can give all four numbers in a single go which makes user friendly
lst = num.split() # it removes the spaces and store the integers sepearately in form ['num1','num2','num3','num4']
num1 = int(lst[0])
num2 = int(lst[1])
num3 = int(lst[2])
num4 = int(lst[3])

if (num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num3):
    print("ignore")
else:
    print("answer")
'''
