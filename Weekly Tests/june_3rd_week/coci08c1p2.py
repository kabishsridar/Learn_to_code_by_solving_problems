n = int(input()) # number of questions

answers = input() # correct sequence

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

for i in range(n): # loop through each question and compare guesses to correct answers
    if answers[i] == adrian_sequence[a_index]:
        adrian += 1
    if answers[i] == bruno_sequence[b_index]:
        bruno += 1
    if answers[i] == goran_sequence[g_index]:
        goran += 1

    # Move to the next character in the guess pattern (loop around when necessary)
    a_index = (a_index + 1) % len(adrian_sequence)
    b_index = (b_index + 1) % len(bruno_sequence)
    g_index = (g_index + 1) % len(goran_sequence)

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