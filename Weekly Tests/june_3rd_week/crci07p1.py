num_platforms = int(input()) # get number of platforms

coordinates = []
for platform_input in range(num_platforms): # asking the coordinate for each platform (y, x1, x2)
    platform = input().split()
    y = int(platform[0])
    x1 = int(platform[1])
    x2 = int(platform[2])
    coordinates.append(y) # appending the inputs to coordinate list
    coordinates.append(x1)
    coordinates.append(x2)

platforms = []
for i in range(0, len(coordinates), 3): # Group every three elements (y, x1, x2) into a platform list
    platforms.append([coordinates[i], coordinates[i+1], coordinates[i+2]]) # example: [[1,4,3], [2,4,6], [3,6,2]]

platforms.sort() # sorts the platform
total = 0
for platform in range(num_platforms): # loop through each platforms
    y, x1, x2 = platforms[platform] # y = height, x1 = left x coordinate, x2 = right x coordinate
    left_pillar = x1 + 0.5 # half unit before the end
    right_pillar = x2 - 0.5

    pillar_position = [left_pillar, right_pillar]
    for pillar_x in pillar_position: # to iterate both left and right pillar positions
        supported = False
        # Look for supporting platform below (indices < i)
        for j in range(i-1, -1, -1): # checks whether a lower platform (platforms[j]) can support the pillar.
            y_below, x1_below, x2_below = platforms[j]
            if x1_below <= pillar_x <= x2_below:
                total += y - y_below # adds distance between current and supporting platform
                supported = True
                break
        if not supported: # Pillar rests on the floor (altitude 0)
            total += y

print(int(total))