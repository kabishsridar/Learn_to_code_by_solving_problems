secret = list(input("enter the secret encoded sentence: "))
vowel = ['a','e','i','o','u']
decoded = ""
i = 0
while i <len(secret):
    decoded += secret[i]
    if secret[i] in vowel:
        i = i+3
    else:
        i = i+1
print("decoded sentence: ",decoded)