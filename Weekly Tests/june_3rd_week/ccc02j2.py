# AmeriCanadian
result = []
try: # for EOFError
    while True:
        word = input() # gets input untill the user enters quit
        if word == "quit":
            break
        if len(word) >= 3 and word[-3] in "aeiouAEIOU": # if the letter before the suffix "or" is a vowel, then no need to change
            pass
        elif len(word) > 4 and word[-2:] == "or": # if the length of word is greater than 4 and the suffix is "or" then the suffix should be changed to "our"
            word = word[:-2] + "our"
        result.append(word) # appending it to result after each loop
except EOFError:
    pass

for item in result:
    print(item) # returns the output