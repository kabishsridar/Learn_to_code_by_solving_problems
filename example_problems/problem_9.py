print("SONGS PLAYLIST APP") # displaying the user about this programme
songs = 'ABCDE' # default order of song playlist
print("normal sequence of playlist: ABCDE")
print("""
    Button1 to move first song to end
    Button2 to move last song to beginning
    Button3 to swap first two songs
    Button4 to play the playlist
    """)
while True: # loops untill the button number is 4
    
    Nbutton = int(input("Enter button number between 1 to 4: ")) # gets an input as informing to select the button

    if Nbutton == 4:
        break  # Exit and play the playlist

    if Nbutton < 1 or Nbutton > 4: # we have only 4 buttons 1,2,3,4 except these any other are not defined 
        print("Invalid button. Please enter a number from 1 to 4.")
        continue

    Ntimes = int(input("Enter number of times to press the button (1 to 10): ")) # number of times to press the button

    if Ntimes < 1 or Ntimes > 10:
        print("Invalid number of presses. Must be between 1 and 10.")
        continue

    for i in range(Ntimes): # it will loop the number of times the button is pressed
        if Nbutton == 1:
            songs = songs[1:] + songs[0]  # Move first song to the end
        elif Nbutton == 2:
            songs = songs[-1] + songs[:-1]  # Move last song to the beginning
        elif Nbutton == 3:
            if len(songs) >= 2:
                songs = songs[1] + songs[0] + songs[2:]  # Swap first two

print("Final Playlist:", ' '.join(songs))
# it will end only when you press 4
