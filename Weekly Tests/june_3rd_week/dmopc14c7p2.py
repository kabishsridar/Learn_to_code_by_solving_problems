n = int(input())  # number of readings
line = input() # readings
parts = line.split()
readings = []
for part in parts:
    readings.append(int(part)) # appending it to list after splitting

min_val = min(readings) # finding minimum and maximum
max_val = max(readings)

min_index = 0
for i in range(len(readings)): # finding index
    if readings[i] < readings[min_index]:
        min_index = i

max_index = 0
for i in range(len(readings)):
    if readings[i] > readings[max_index]:
        max_index = i

if min_index < max_index:
    valid = True
    for i in range(len(readings) - 1):
        if i >= min_index and i < max_index:# if it is between the calculated index
            if readings[i] >= readings[i + 1]:
                valid = False
                break

    if valid:
        print(max_val - min_val)
    else:
        print("unknown")
else:
    print("unknown")
