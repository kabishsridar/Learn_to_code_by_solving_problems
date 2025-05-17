cost = [12, 10, 7, 5] # 1st year = $12, 2nd year = $10, 3rd year = $7, 4th year = $5

# Loop for 10 trips
for i in range(10):
    tcost = int(input("Trip cost($) between 50 and 50000: "))

    num_students = int(input("Total number of students (4 to 2000): "))

    proportion_input = input("Proportion of students per year (e.g. 0.25 0.25 0.25 0.25): ").split()

    for i in range(len(proportion_input)):
        proportion_input[i] = float(proportion_input[i])

    students_per_year = []
    for proportion in proportion_input:
        students = int(num_students * proportion)  # Convert to integer
        students_per_year.append(students)

    total_raised = 0
    for i in range(len(students_per_year)):
        total_raised = total_raised + students_per_year[i] * cost[i]  # Multiply students by cost per year

    # check if at least half of the trip cost is covered
    if total_raised / 2 < tcost:
        print("YES, funds needed")  # More funds are needed
    else:
        print("NO, funds are enough")  # Enough funds are raised

    print(f"Total raised: ${total_raised}, Half of trip cost: ${tcost / 2:.2f}")
    
    print("YES - More funds needed." if total_raised / 2 < tcost else "NO - Enough funds raised.\n")
    break
