def honi_blocks(word):
    target = "HONI"
    target_index = 0
    count = 0

    for char in word:
        if char == target[target_index]:
            target_index += 1
            if target_index == 4:
                count += 1
                target_index = 0

    print(count)

word = input().strip()
honi_blocks(word)