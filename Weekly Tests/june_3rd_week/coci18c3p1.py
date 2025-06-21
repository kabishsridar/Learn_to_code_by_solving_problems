def honi_blocks(word): # function to check honi blocks in the input
    target = "HONI"
    target_index = 0
    count = 0

    for char in word: # checks each character from the input
        if char == target[target_index]:
            target_index += 1
            if target_index == 4:
                count += 1
                target_index = 0 # after each honi, need to set it as 0, to count

    print(count) # display the number of honi

word = input().strip()
honi_blocks(word)