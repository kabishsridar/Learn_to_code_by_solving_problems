# inputs are A, B, C, D, E, F, G, |
# a minor - A, D, E
# c major = C, F, G
tone = input().strip()
measures = tone.split('|')
# print(measures)

a_minor = ['A', 'D', 'E']
c_major = ['C', 'F', 'G']

a_count = 0
c_count = 0

for measure in measures:
    if not measure:
        # print("no measure")
        continue
    first_note = measure[0]
    # print(first_note)
    if first_note in a_minor:
        a_count += 1
    elif first_note in c_major:
        c_count += 1
    
if a_count > c_count:
    print("A-mol")
elif c_count > a_count:
    print("C-dur")
else:
    last_note = measures[-1][-1]
    if last_note == 'A':
        print("A-mol")
    elif last_note == 'C':
        print("C-dur")