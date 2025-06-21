# atleast 8 to 12 charecters
# 3 lower, 2 upper, 1 digit
passwd = input() # get the password
status = False

if len(passwd) <= 12 and len(passwd) >= 8: # pasword length is between 8 and 12
    status = True

digit = False
for char in passwd:
    if char.isdigit(): # if the password contains a digit, it is true
        digit = True
        break
if digit == True:
    status = status and True
else:
    status = False

upper = 0
for char in passwd:
    if char.isupper():
        upper += 1 # counting the number of uppercases
if upper >= 2: # count of uppercase should be atleast 2
    status = status and True
else:
    status = False

lower = 0
for char in passwd:
    if char.islower(): # counting lower cases
        lower += 1
if lower >= 3: # count of lowercase should be atleast 3
    status = status and True
else:
    status = False

if status == True:
    print("Valid")
else:
    print("Invalid")
