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