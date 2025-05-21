def read_cows(filein, num_cows):
    favourites = []
    for i in range(num_cows):
        lst = filein.readline().split()
        lst[0] = int(lst[0])
        lst[1] = int(lst[1])
        favourites.append(lst)
    return favourites

def cows_with_favourite(favourites, pasture):
    cows = []
    for i in range(len(favourites)):
        if favourites[i][0] == pasture or favourites[i][1] == pasture:
            cows.append(i)
        return cows
def types_used(favourites, cows, pasture_types):
    used = []
    for cow in cows:
        pasture_a = favourites[cow][0]
        pasture_b = favourites[cow][1]

        if pasture_a < len(pasture_types):
            used.append(pasture_types[pasture_a])
        if pasture_b < len(pasture_types):
            used.append(pasture_types[pasture_b])
    return used

def smallest_available(used):
    grass_type = 1
    while grass_type in used:
        grass_type = grass_type + 1
    return grass_type

def write_pastures(fileout, pasture_types):
    pasture_types_str = []
    for pasture_type in pasture_types:
        pasture_types_str.append(str(pasture_type))
    output = ''.join(pasture_types_str)
    fileout.write(output + '\n')

filein = open("revegetatein.txt", "r") # openin a file in read mode
fileout = open("revegetateout.txt", "w") # opening a file to write

lst = filein.readline().split() # read first line to get number of pastures and cows

num_pastures = int(lst[0]) # number of pastures (green land is pasture)
num_cows = int(lst[1]) # number of cows

favourites = read_cows(filein, num_cows)
pasture_types = [0]
for i in range(1, num_pastures + 1):
    cows = cows_with_favourite(favourites, i)
    eliminated = types_used(favourites, cows, pasture_types)

    pasture_type = smallest_available(eliminated)
    pasture_types.append(pasture_type)

pasture_types.pop(0)
write_pastures(fileout, pasture_types)

filein.close()
fileout.close()