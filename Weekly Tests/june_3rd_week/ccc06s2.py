# decoding cipher_text to plain text
plain_text = input() # get the input from the user for plain text
corresponding_cipher_text = input() # prompt for the cipher text for the above plain text

# mapping dictionary will be like {'H' : 'G', 'I' : 'D'}
mapping = dict(zip(corresponding_cipher_text, plain_text)) # make those lists as a dictionary
# make sure that corresponding_cipher_text is the key and plain_text is the value

cipher_text = input() # get the cipher_text to be decoded
result = "" # initiate result as an empty string
# print(mapping)
# print(mapping.keys())

for letter in cipher_text: # loop through each letters in cipher text
    if letter in mapping: # if the letter is present in the dictionary, then get the value for the key and then, append to result
        result += mapping[letter]
    else: # if it is not found, add a . to the result
        result += "."
print(result) # display the final output.
