cost = [12, 10, 7, 5]

for i in range(10):
    tcost = int(input("Trip cost: "))
    num_students = int(input("Total number of students: "))
    proportion_input = input("Proportion of students per year (e.g. 0.25 0.25 0.25 0.25): ").split()
    proportions = [float(p) for p in proportion_input]
    
    if len(proportions) != 4:
        print("Error: Please provide exactly 4 proportions (one for each year group) separated by spaces.")
        continue

    students_per_year = [round(num_students * p) for p in proportions]

    total_assigned = sum(students_per_year)
    if total_assigned != num_students:
        max_index = proportions.index(max(proportions))
        students_per_year[max_index] += (num_students - total_assigned)

    total_raised = sum(students_per_year[i] * cost[i] for i in range(4))

    print(f"Total raised: ${total_raised}, Half of trip cost: ${tcost / 2:.2f}")

    if total_raised / 2 < tcost:
        print("YES - More funds needed.\n")
    else:
        print("NO - Enough funds raised.\n")
