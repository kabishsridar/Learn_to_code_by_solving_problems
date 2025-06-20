def read_cows(filein, num_cows):  # defining a function named read_cows to read the next m lines of two integers (favourite pasture of each cow)
    favourites = []  # initiating favourites as an empty list to track favourite pastures and store those next m lines
    for i in range(num_cows):  # loop through each cow
        lst = filein.readline().split()  # read line for favourite pastures of the cow
        lst[0] = int(lst[0])  # converting favourite pastures from string to integer
        lst[1] = int(lst[1])  
        favourites.append(lst)  # adding the lst to favourites after converting them into integers
    return favourites

def cows_with_favourite(favourites, pasture):  # defining a function cows_with_favourite to find cows that favor the given pasture
    cows = []  # initiating cows as an empty list
    for i in range(len(favourites)):  # loop through each favourite pastures of cows
        if favourites[i][0] == pasture or favourites[i][1] == pasture:
            cows.append(i)
    return cows

def types_used(favourites, cows, pasture_types):  # defining a function types_used to find grass types already used by neighbouring pastures
    used = []  # initiate used as an empty list to store used grass types
    for cow in cows:  # loop through each cow in the cows list
        pasture_a = favourites[cow][0]  # get the first favourite pasture
        pasture_b = favourites[cow][1]  # get the second favourite pasture

        if pasture_a < len(pasture_types):
            used.append(pasture_types[pasture_a]) # Add grass type of first favorite pasture if pasture_a is less than pasture_types

        if pasture_b < len(pasture_types):
            used.append(pasture_types[pasture_b]) # Add grass type of second favorite pasture if pasture_b is less than pasture_types
    return used

def smallest_available(used):  # defining a function named smallest_available to find the smallest grass type not yet used
    grass_type = 1  # initiating grass type as 1 to start with 1
    while grass_type in used:  # if grass_type is already used, try next
        grass_type = grass_type + 1  # move to the next grass type
    return grass_type

def write_pastures(fileout, pasture_types):  # defining a function write_pastures to format pasture_types and write it to output file
    pasture_types_str = []  # initiate an empty list to hold string version of pasture types
    for pasture_type in pasture_types:  # loop through each type
        pasture_types_str.append(str(pasture_type))
    output = ''.join(pasture_types_str)  # join all the strings to form the final output string
    fileout.write(output + '\n') # write the output string to the file followed by newline

filein = open("revegetatein.txt", "r")  # opening the input file in read mode to read number of pastures and cows
fileout = open("revegetateout.txt", "w")  # opening the output file to write the final result

lst = filein.readline().split()  # read first line to get number of pastures and number of cows

num_pastures = int(lst[0])  # converting number of pastures to integer
num_cows = int(lst[1])  # converting number of cows to integer

favourites = read_cows(filein, num_cows)  # get the list of all cow's favourite pastures
pasture_types = [0]

for i in range(1, num_pastures + 1):  # loop through each pasture except 0
    cows = cows_with_favourite(favourites, i)  # find cows that like this particular pasture
    eliminated = types_used(favourites, cows, pasture_types)  # get grass types already used by other pastures

    pasture_type = smallest_available(eliminated)  # find the smallest grass type that can be assigned here
    pasture_types.append(pasture_type)

pasture_types.pop(0)  # remove 0 at the beginning (was used for 1based indexing)
write_pastures(fileout, pasture_types)  # write the result to output file

filein.close()  # closing the file
fileout.close()
