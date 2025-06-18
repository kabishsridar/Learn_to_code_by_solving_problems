brief_cases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
n = int(input()) # number of cases chosen

remaining = ["yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes"]
# print(remaining)

for case in range(n):
    case_num = int(input())
    remaining[case_num - 1] = "chosen" # changing yes to chosen where the cases is chosen

offer = int(input()) # to be asked at last line

total = 0
count = 0

for cases in range(10):
    if remaining[cases] == "yes":
        total += brief_cases[cases]
        count += 1

average = total / count

if offer > average:
    print("deal")
else:
    print("no deal")