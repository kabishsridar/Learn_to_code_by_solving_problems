# not completed
n = int(input()) # number of days
net_changed = input()
output =  ['.'] * n

for char in range(n):
    if net_changed[char] == "+":
        output[char] = "/"
    elif net_changed[char] == "-":
        output[char] = "\\"
    else:
        output[char] = "_"
print("".join(output))