#English or French
# if t is more than s, english
# if s is more than t, french
# if number of s and t are same, french
n = int(input())
t_count = 0
s_count = 0
for i in range(n):
    prompt = input()
    for char in prompt.lower():
        if char == "t":
            t_count += 1
        elif char == "s":
            s_count += 1
            
if t_count > s_count:
    print("English")
elif s_count > t_count:
    print("French")
elif s_count == t_count:
    print("French")
else:
    pass
