# input is a string of musical notes separated by '|'
# notes: A, B, C, D, E, F, G
# A minor scale contains: A, D, E
# C major scale contains: C, F, G
tone = input().strip()

# Split the input using '|' as a delimiter
measures = tone.split('|')

a_minor = ['A', 'D', 'E']
c_major = ['C', 'F', 'G']

a_count = 0
c_count = 0

for measure in measures: # loop through each measures
    if not measure:
        continue
    first_note = measure[0]

    if first_note in a_minor:
        a_count += 1
    elif first_note in c_major:
        c_count += 1

# check the condition through whch is greater
if a_count > c_count:
    print("A-mol")  # A minor
elif c_count > a_count:
    print("C-dur")  # C major
else:
    # If counts are equal, use the last note of the last non-empty measure as tiebreaker
    last_note = measures[-1][-1]
    if last_note == 'A':
        print("A-mol")
    elif last_note == 'C':
        print("C-dur")