for dataset_number in range(10): # standard input 10 datasets
    route = int(input()) # num of routes
    min_diameters = []

    for route_number in range(route):
        line = input()
        parts = line.split()
        data = []

        for part in parts:
            data.append(int(part)) # append the input to the list data
        
        route_id = data[0]
        diameters = data[2:]
        route_min = min(diameters)
        min_diameters.append((route_min, route_id))
    
    overall_min = min_diameters[0][0]
    for pair in min_diameters:
        if pair[0] < overall_min:
            overall_min = pair[0]

    ids_with_min = []
    for pair in min_diameters:
        if pair[0] == overall_min:
            ids_with_min.append(pair[1])
        ids_with_min.sort()
    
    str_ids = []
    for id_ in ids_with_min:
        str_ids.append(str(id_))
    print(str(overall_min) + " {" + ",".join(str_ids) + "}")
