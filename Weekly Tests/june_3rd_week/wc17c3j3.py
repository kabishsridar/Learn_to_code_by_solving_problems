# atleast 8 to 12 charecters
# 3 lower, 2 upper, 1 digit
passwd = input()
status = False

if len(passwd) <= 12 and len(passwd) >= 8:
    status = True

digit = False
for char in passwd:
    if char.isdigit():
        digit = True
        break
if digit == True:
    status = status and True
else:
    status = False

upper = 0
for char in passwd:
    if char.isupper():
        upper += 1
if upper >= 2:
    status = status and True
else:
    status = False

lower = 0
for char in passwd:
    if char.islower():
        lower += 1
if lower >= 3:
    status = status and True
else:
    status = False

if status == True:
    print("Valid")
else:
    print("Invalid")
