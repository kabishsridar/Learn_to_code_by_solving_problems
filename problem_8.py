quarters = int(input("Enter the number of quarters Martha has(1 yo 1000): "))  # here quarter mean the ticket to play in casino 
print("Enter the number of times that the slot machine has been played since it last paid")
first_machine_count = int(input("FIRST machine: ")) #the number of times that the slot machine has been played since it last paid
second_machine_count = int(input("SECOND machine: "))
third_machine_count = int(input("THIRD machine: "))

plays = 0
machine = 0

while quarters >= 1:  # she can play only if she has 1 or more than 1 quarters
    quarters = quarters - 1 # one quarter is reduced for one play

    if machine == 0:
        first_machine_count += 1
        if first_machine_count == 35:
            first_machine_count = 0  # for every 35th count it should start new
            quarters += 30  # it pays 30 quarters for every 35th time played
    elif machine == 1:
        second_machine_count += 1
        if second_machine_count == 100:
            second_machine_count = 0
            quarters += 60 # it pays 60 quarter for every 100th time played
    elif machine == 2:
        third_machine_count += 1
        if third_machine_count == 10:
            third_machine_count = 0
            quarters += 9 # it pays 9 quarters every 10th time played

    plays += 1  # it should increase for every number of plays
    machine += 1
    if machine == 3:
        machine = 0  # because it is mentioned that she plays them in order until she has no quarters left

plays = plays + 1
machine = machine + 1
if machine == 3:
    machine = 0
    
print('Martha plays', plays, 'times before she has 1 quarters.')
