# how many words from the input matches a given number string
t9_pairs = {
    'abc': '2',
    'def': '3',
    'ghi': '4',
    'jkl': '5',
    'mno': '6',
    'pqrs': '7',
    'tuv': '8',
    'wxyz': '9'
} # creating a dictionary and assigning the digits as per the t9 keypad

n = int(input()) # get input for number of words
words = [] # initiate an empty list to store the words from the input
for cur_word in range(n): # next n lines, ask for the words
    word = input().strip()
    words.append(word) # append those to the words list
s = input() # the last input is the string s

count = 0 # initiating count to 0 so that we can track the count by incrementing
for word in words: # loop through each word in the words list
    if len(word) != len(s): # if the length of both the string and word, then continue, else skip
        # checking this because each letter is exactly set to one number
        continue
    num_string = '' # initiating num_string as an empty string
    for char in word: # loop through each character in the word
        for characters, digit in t9_pairs.items():
            if char in characters: # if the character belongs to the current group, append to num_string (ex char = a and the characters = "abc")
                num_string += digit
                break
    if num_string == s: # if the num_string matches with the input string s, increment by 1
        count += 1
print(count) # display the final count