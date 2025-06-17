# basket ball
# game = 4 X 12 mins
# this problem took more than 60 minutes to solve

A = int(input()) # Team A score
As = []
for points in range(A):
    Asec = int(input()) # each second the team got scores
    As.append(Asec)
B = int(input()) # Team B score
Bs = []
for point in range(B):
    Bsec = int(input()) # each seccond the team got scores
    Bs.append(Bsec)
first_half = 1440 # first half of the game is 1440 seconds
total = 0

for sec in As:
    if sec <= first_half:
        total += 1 # sum the total points scored in first half by Team A

for sec in Bs:
    if sec <= first_half:
        total += 1 # sum the total points scored in first half by Team B

print(total) # display final answer for que 1

events = []
for sec in As: # loop through each seconds from the input
    events.append([sec, 'A'])
for sec in Bs:
    events.append([sec, 'B'])

events.sort()

score_A = 0
score_B = 0
turnarounds = 0
previous_leader = None

for i in range(len(events)):
    event = events[i]
    time = event[0]
    team = event[1]

    if team == 'A':
        score_A += 1
    else:
        score_B += 1

    if score_A > score_B: # finding the currently leading team
        current_leader = 'A'
    elif score_B > score_A:
        current_leader = 'B'
    else:
        current_leader = None

    # if the leader changes, imcrement turnaround by 1
    if current_leader is not None and previous_leader is not None:
        if current_leader != previous_leader:
            turnarounds += 1

    if current_leader is not None:
        previous_leader = current_leader # update the previous leader

print(turnarounds)