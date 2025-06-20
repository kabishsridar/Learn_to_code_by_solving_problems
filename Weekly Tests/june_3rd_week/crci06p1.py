# which villagers knows all songs
n = int(input()) # num of villagers.
e = int(input()) # num of Evenings.
present_lst = [] # ex [['2', '1', '2'], ['3', '2', '3', '4'], ['3', '4', '2', '1']]
for evening in range(e): # get input for number of evenings
    present  = (input()).split()
    present_lst.append(present) # append the inputs to the present_lst

villager_songs = {} # initiate a dictionary to store songs known by each villagers, ex: {villager_id : song_id}
for i in range(1, n + 1):
    villager_songs[i] = set()

song_id = 1
all_songs = set() # initiating an empty set all_songs to track the songs introduced

for evening in present_lst:
    present_villagers = []
    for i in range(1, len(evening)): # the first will be the num of people, so we are skipping it
        present_villagers.append(int(evening[i])) # append the villager_id to present_villagers after converting to integer
    
    if 1 in present_villagers: # 1 represents bard is present
        new_song = song_id # add new song
        song_id += 1
        all_songs.add(new_song) # add to the set all_songs
        
        for villager in present_villagers: # the present villagers on that day will learn that song
            villager_songs[villager].add(new_song)
    else: # bard is not present, villagers share songs
        combined_songs = set()
        for villager in present_villagers: # loop through each villagers present and adds the song that they know to the combined_songs
            for song in villager_songs[villager]:
                combined_songs.add(song)
        
        for villager in present_villagers: # each present villager's set of known_songs will be combined songs
            villager_songs[villager] = combined_songs.copy()

for villager in range(1, n + 1): # villagers who know all songs
    if villager_songs[villager] >= all_songs: # if the villager know all songs
        print(villager) # print the villager's id