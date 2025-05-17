NUM_CARDS = 52

def no_high(lst):
    for card in lst:
        if card in {'jack', 'queen', 'king', 'ace'}:
            return False  # if any high card is found, return False immediately
    return True # if no high cards , return true

deck = []

#collect 52 cards from the user
print("Enter the 52 cards one by one:")
for i in range(NUM_CARDS):
    deck.append(input().strip().lower())  # convert input to lowercase

score_a = 0
score_b = 0
player = 'A'  # player A starts first

# loop through the deck to determine scoring
for i in range(NUM_CARDS):
    card = deck[i]
    points = 0
    remaining = NUM_CARDS - i - 1  # number of cards left in the deck after the current one

    # scoring rules based on card type and remaining cards
    if card == 'jack' and remaining >= 1 and no_high(deck[i+1:i+2]):
        points = 1
    elif card == 'queen' and remaining >= 2 and no_high(deck[i+1:i+3]):
        points = 2
    elif card == 'king' and remaining >= 3 and no_high(deck[i+1:i+4]):
        points = 3
    elif card == 'ace' and remaining >= 4 and no_high(deck[i+1:i+5]):
        points = 4

    if points > 0:
        print(f'Player {player} scores {points} point(s).')

    if player == 'A':
        score_a += points
        player = 'B'
    else:
        score_b += points
        player = 'A'

print("\nFinal Scores:")
print(f'Player A: {score_a} point(s).')
print(f'Player B: {score_b} point(s).')

if score_a > score_b:
    print("Player A wins!")
elif score_b > score_a:
    print("Player B wins!")
else:
    print("It's a tie!")
