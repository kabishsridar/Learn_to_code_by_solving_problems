width = int(input())
cheesiness = int(input()) # get the inputs

output = ""
if width == 3 and cheesiness >= 95:
    output = "absolutely"
elif width == 1 and cheesiness <=50:
    output = "fairly"
else:
    output = "very"

print(f"C.C. is {output} satisfied with her pizza.") # display according to the output