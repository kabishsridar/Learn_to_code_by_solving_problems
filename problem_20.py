def find_special_pairs():
    infile = open("citystate.in", "r")
    n = int(infile.readline().strip()) 
    cities = []
    
    for _ in range(n):
        cities.append(infile.readline().strip().split())
    infile.close()
    prefix_to_state_count = {}

    for city, state in cities:
        prefix = city[:2]  
        if prefix not in prefix_to_state_count:
            prefix_to_state_count[prefix] = {}
        if state not in prefix_to_state_count[prefix]:
            prefix_to_state_count[prefix][state] = 0
        prefix_to_state_count[prefix][state] += 1

    special_pair_count = 0

    for city, state in cities:
        prefix = city[:2]
       
        if prefix in prefix_to_state_count:
            for other_state, count in prefix_to_state_count[prefix].items():
                if other_state != state:
                    special_pair_count += count

    special_pair_count //= 2

    outfile = open("citystate.out", "w")
    outfile.write(str(special_pair_count))
    outfile.close()

find_special_pairs()