a=int(input("First Integer: "))
b=int(input("Second Integer: "))
c=int(input("Third Integer: "))
d=int(input("Fourth Integer: "))
# it prints ignore if the first and last numbers are either 8 or 9 and the second and third numbers are same
#otherwise it prints answer
print(a,b,c,d)
if (a==8 or a==9) and (d==8 or d==9) and (b==c):
    print("ignore")
else:
    print("answer")
'''
We can also use the below format by using split function so that the user can type in single line and it can be faster
num = input("enter four number with seperating spaces: ")
lst = num.split()
num1 = int(lst[0])
num2 = int(lst[1])
num3 = int(lst[2])
num4 = int(lst[3])

if (num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num3):
    print("ignore")
else:
    print("answer")
'''
