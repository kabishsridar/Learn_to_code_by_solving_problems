songs = 'ABCDE'

while True:
    Nbutton = int(input("Enter button number between 1 to 4: "))

    if Nbutton == 4:
        break  # Exit and play the playlist

    if Nbutton < 1 or Nbutton > 4:
        print("Invalid button. Please enter a number from 1 to 4.")
        continue

    Ntimes = int(input("Enter number of times to press the button (1 to 10): "))

    if Ntimes < 1 or Ntimes > 10:
        print("Invalid number of presses. Must be between 1 and 10.")
        continue

    for i in range(Ntimes):
        if Nbutton == 1:
            songs = songs[1:] + songs[0]  # Move first song to the end
        elif Nbutton == 2:
            songs = songs[-1] + songs[:-1]  # Move last song to the beginning
        elif Nbutton == 3:
            if len(songs) >= 2:
                songs = songs[1] + songs[0] + songs[2:]  # Swap first two


print("Final Playlist:", ' '.join(songs))