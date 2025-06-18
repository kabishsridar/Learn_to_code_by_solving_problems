n = int(input()) # number of questions

answers = input() # sequence

# repeating guess pattern
adrian_sequence = ['A', 'B', 'C']
bruno_sequence = ['B', 'A', 'B', 'C']
goran_sequence = ['C', 'C', 'A', 'A', 'B', 'B']

a_index = 0
b_index = 0
g_index = 0
adrian = 0
bruno = 0
goran = 0

for i in range(n):  # loop through each question
    if answers[i] == adrian_sequence[a_index]:
        adrian += 1
    if answers[i] == bruno_sequence[b_index]:
        bruno += 1
    if answers[i] == goran_sequence[g_index]:
        goran += 1

    a_index += 1
    if a_index == len(adrian_sequence):
        a_index = 0

    b_index += 1
    if b_index == len(bruno_sequence):
        b_index = 0

    g_index += 1
    if g_index == len(goran_sequence):
        g_index = 0
# finding the maximum score
max_score = max(adrian, bruno, goran)

winners = []
if adrian == max_score:
    winners.append("Adrian")
if bruno == max_score:
    winners.append("Bruno")
if goran == max_score:
    winners.append("Goran")

# Output
print(max_score)

for name in winners:
    print(name)