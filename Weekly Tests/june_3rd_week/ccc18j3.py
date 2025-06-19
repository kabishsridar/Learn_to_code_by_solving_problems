# Are We There Yet
distances = input() # get input from user

def add_distances(distances):
    distance_lst = distances.split() # split the input into a list

    for index in range(len(distance_lst)): # convertign each character to an integer
        distance_lst[index] = int(distance_lst[index])
    
    result = [0] # initialise the result list to 0 to track the sums
    for i in range(len(distance_lst)): # loop through each distances given
        total = result[-1] + distance_lst[i] # sums the last digit of result with the current digit in distance_lst
        result.append(total) # append the total calculated to the result list

    for i in range(len(result)):# finding the difference between each pair of distances
        for j in range(len(result)): # if i is 0, then with i=0, the j will be as 0, 1, 2, etc 
            # with the nested loop, we are able to display both horizontal and vertial results
            if result[i] > result[j]: # displaying the difference between both
                dif = result[i] - result[j]
            else:
                dif = result[j] - result[i]
            print(dif, end=" ")
        print()

add_distances(distances) # calling the function