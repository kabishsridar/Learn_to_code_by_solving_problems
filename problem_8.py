quarters = int(input("Enter the number of quarters Martha has(1 yo 1000): "))  # get the number of querters from user and store it in integer form (here quarter mean the ticket to play in casino) 
print("Enter the number of times that the slot machine has been played since it last paid")
first_machine_count = int(input("FIRST machine: ")) # get the input from user for the number of times that the slot machine has been played since it last paid
second_machine_count = int(input("SECOND machine: "))
third_machine_count = int(input("THIRD machine: "))

plays = 0 # initiating plays and machine as 0
machine = 0

while quarters >= 1:  # she can play only if she has 1 or more than 1 quarters
    quarters = quarters - 1 # one quarter is reduced for one play

    if machine == 0: # at starting we initiated machine as 0, so it will start from here and repeat as 0,1,2,0,1,2... and so on
        first_machine_count += 1 # the number of first_machine_count should increase once when the first machine is used 
        if first_machine_count == 35:
            first_machine_count = 0  # for every 35th count it should start new as it is awarded 30 quarters for each 35th time
            quarters += 30  # it pays 30 quarters for every 35th time played
    elif machine == 1: # after the execution of first if statement, in the last we added machine = machine + 1 so that now it will be 1 and it will pass to elif condition (machine = 1) 
        second_machine_count += 1
        if second_machine_count == 100:
            second_machine_count = 0
            quarters += 60 # it pays 60 quarter for every 100th time played
    elif machine == 2: # after the execution of elif statement, in the last we added machine = machine + 1 so that now it will be 2 and it will pass to elif condition (machine = 2) 
        third_machine_count += 1
        if third_machine_count == 10:
            third_machine_count = 0
            quarters += 9 # it pays 9 quarters every 10th time played

    plays += 1  # these both should increase for every number of plays
    machine += 1
    if machine == 3:
        machine = 0  # because it is mentioned that she plays them in order until she has no quarters left as 0,1,2,0,1,2...

print('Martha plays', plays, 'times before she has 1 quarters.') # displaying the output
