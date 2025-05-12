cards = 52
deck = []

# Read 52 cards into the deck
for i in range(cards):
    deck.append(input("card: "))

score_a = 0
score_b = 0
player = 'A'

# Returns True if no high cards (jack, queen, king, ace) are in the given list
def no_high(lst):
    if 'jack' in lst:
        return False
    if 'queen' in lst:
        return False
    if 'king' in lst:
        return False
    if 'ace' in lst:
        return False
    return True

for i in range(cards):
    card = deck[i]
    points = 0  # Reset points for current card
    remaining = cards - i - 1  # Cards left in the deck after the current one

    # Check if the current card is a high card and whether scoring conditions are met
    if card == 'jack' and remaining >= 1 and no_high(deck[i+1:i+2]):
        points = 1
    elif card == 'queen' and remaining >= 2 and no_high(deck[i+1:i+3]):
        points = 2
    elif card == 'king' and remaining >= 3 and no_high(deck[i+1:i+4]):
        points = 3
    elif card == 'ace' and remaining >= 4 and no_high(deck[i+1:i+5]):
        points = 4

    if points > 0:
        print(f"player {player} scored {points} point(s).")
    
    # Alternate players and update scores
    if player == 'A':
        score_a = score_a + points
        player = 'B'
    else:
        score_b = score_b + points
        player = 'A'

# Print final scores
print(f"player A: {score_a} point(s).")
print(f"player B: {score_b} point(s).")
