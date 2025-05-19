cost = [12, 10, 7, 5] # 1st year = $12, 2nd year = $10, 3rd year = $7, 4th year = $5

# Loop for 10 trips
for i in range(10):
    tcost = int(input("Trip cost($) between 50 and 50000: ")) # prompt the user for total trip cost

    num_students = int(input("Total number of students (4 to 2000): ")) # prompt the user for number of students

    proportion_input = input("Proportion of students per year (e.g. 0.25 0.25 0.25 0.25): ").split() # prompt the user for proportion and store it as a list and split it

    for i in range(len(proportion_input)): # loop through each proportion_input
        proportion_input[i] = float(proportion_input[i]) # convert all those to gloating values

    students_per_year = [] # initiating students_per_year to an empty list
    for proportion in proportion_input: # loop through each proportion_input
        students = int(num_students * proportion)  # Convert to integer and multiply num_students and proportion of current student
        students_per_year.append(students) # add it to students_per_year list

    total_raised = 0
    for i in range(len(students_per_year)): # loop through each item in students_per_year
        total_raised = total_raised + students_per_year[i] * cost[i]  # Multiply students by cost per year

    # check if at least half of the trip cost is covered
    if total_raised / 2 < tcost:
        print("YES, More funds needed")  # More funds are needed
    else:
        print("NO, funds are enough")  # Enough funds are raised

    print(f"Total raised: ${total_raised}, Half of trip cost: ${tcost / 2:.2f}")
    break
