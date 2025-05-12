cost = [12, 10, 7, 5]
# update the above variable 

for i in range(10):
    tcost = int(input("Trip cost: "))
    proportion = list(map(float, input("Proportion of students per year: ").split()))
    num_students = int(input("Total number of students: "))

    if len(proportion) != 4:
        print("Error: Please provide exactly 4 proportions (one for each year group) by seperating them with spaces.")
        continue

    students_per_year = [int(num_students * p) for p in proportion]

    total_assigned = sum(students_per_year)
    if total_assigned < num_students:

        max_index = proportion.index(max(proportion))
        students_per_year[max_index] += (num_students - total_assigned)


    total_raised = sum(students_per_year[i] * cost[i] for i in range(4))

    print(f"Total raised: ${total_raised}, Half of trip cost: ${tcost / 2}")


    if total_raised / 2 < tcost:
        print("YES - More funds needed.\n")
    else:
        print("NO - Enough funds raised.\n")
