quarters = int(input("Enter the number of quarters Martha has: "))
first_machine_count = int(input("Enter the number of times left for the FIRST machine: "))
second_machine_count = int(input("Enter the number of times left for the SECOND machine: "))
third_machine_count = int(input("Enter the number of times left for the THIRD machine: "))

plays = 0
machine = 0

while quarters >= 1:
    quarters = quarters - 1

    if machine == 0:
        first_machine_count += 1
        if first_machine_count == 35:
            first_machine_count = 0
            quarters += 30
    elif machine == 1:
        second_machine_count += 1
        if second_machine_count == 100:
            second_machine_count = 0
            quarters += 60
    elif machine == 2:
        third_machine_count += 1
        if third_machine_count == 10:
            third_machine_count = 0
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