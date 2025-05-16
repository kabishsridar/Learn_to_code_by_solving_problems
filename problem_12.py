# the cost is sstored as the first year should pay $12 and seond year $10 and so on and made it as a list
cost = [12, 10, 7, 5]

for i in range(10): # it is mentiond that input consists of 10 test cases
    tcost = int(input("Trip cost($) between 50 and 50000: ")) # getting input from user for total trip cost
    num_students = int(input("Total number of students(4 to 2000): ")) 
    proportion_input = input("Proportion of students per year (e.g. 0.25 0.25 0.25 0.25): ").split() # the propotion of the students for 100% as their sum should be 1
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
