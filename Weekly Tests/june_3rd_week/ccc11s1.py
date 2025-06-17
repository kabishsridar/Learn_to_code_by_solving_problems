#English or French
# if t is more than s, english
# if s is more than t, french
# if number of s and t are same, french
n = int(input()) # get input for number of lines
t_count = 0
s_count = 0
for i in range(n): # loop for each lines and prompt the input and count number of t and s in the line
    prompt = input()
    for char in prompt.lower():
        if char == "t":
            t_count += 1
        elif char == "s":
            s_count += 1
            
if t_count > s_count: # implementing the conditions given in the question
    print("English")
elif s_count > t_count:
    print("French")
elif s_count == t_count:
    print("French")
else:
    pass
