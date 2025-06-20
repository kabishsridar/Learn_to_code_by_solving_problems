secret = list(input("enter the secret encoded sentence: ")) # get an input of that secret code which we need to work with
vowel = ['a','e','i','o','u','A','E','I','O','U'] # assigning vowel letters to a list named vowel 
decoded = "" # initiating decoded as an empty string
letter = 0 # initiating letter to be 0
while letter <len(secret): # it will loop number of times if it is a vowel it will move by 3 and those two indices will not be looped and if it is a consonant it will move consecutively
    decoded += secret[letter] # add current character to decoded
    if secret[letter] in vowel: # if it is vowel skip next two characters
        letter = letter+3 # move by three index if it is a vowel
    else:
        letter = letter+1 # move one index if it is consonant
print("decoded sentence: ",decoded) # display the final output
