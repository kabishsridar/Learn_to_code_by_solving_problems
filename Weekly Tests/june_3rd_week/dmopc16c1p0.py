width = int(input()) # prompt for the width
cheesiness = int(input()) # get the inputs

output = ""
if width == 3 and cheesiness >= 95: # check with the conditions in the questions and modify the output accordingly
    output = "absolutely"
elif width == 1 and cheesiness <=50:
    output = "fairly"
else:
    output = "very"

print(f"C.C. is {output} satisfied with her pizza.") # display according to the output