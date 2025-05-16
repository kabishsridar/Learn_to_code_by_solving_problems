secret = list(input("enter the secret encoded sentence: ")) # get an input of that secret code which we need to work with
vowel = ['a','e','i','o','u','A','E','I','O','U']
decoded = ""
i = 0
while i <len(secret):
    decoded += secret[i] # add current character to decoded
    if secret[i] in vowel: # if it is vowel skip next two characters
        i = i+3 # move by three index
    else:
        i = i+1 # move one index if it is consonant
print("decoded sentence: ",decoded)
