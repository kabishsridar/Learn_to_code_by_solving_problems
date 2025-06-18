distances = input() # get input from user

def add_distances(distances):
    distance_lst = distances.split() # split the input into a list

    for index in range(len(distance_lst)): # convertign each character to an integer
        distance_lst[index] = int(distance_lst[index])
    
    result = [0]
    for i in range(len(distance_lst)):
        total = result[-1] + distance_lst[i]
        result.append(total)

    for i in range(len(result)):
        for j in range(len(result)):
            if result[i] > result[j]:
                dif = result[i] - result[j]
            else:
                dif = result[j] - result[i]
            print(dif, end=" ")
        print()

add_distances(distances)