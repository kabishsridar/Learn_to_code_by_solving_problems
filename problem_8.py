quarters = int(input("No. of quarters: "))
a = int(input("No. of times in first machine: "))
b = int(input("No. of times in second machine: "))
c = int(input("No. of times in third machine: "))
plays = 0
machine = 0
while quarters >= 1:
    quarters = quarters - 1

    if machine == 0:
        a += 1
        if a == 35:
            a = 0
            quarters += 30
    elif machine == 1:
        b += 1
        if b == 100:
            b = 0
            quarters += 60
    elif machine == 2:
        c += 1
        if c == 10:
            c = 0
            quarters += 9

    plays += 1
    machine += 1
    if machine == 3:
        machine = 0  


plays = plays + 1
machine = machine + 1
if machine == 3:
    machine = 0
    
print('Martha plays', plays, 'times.')