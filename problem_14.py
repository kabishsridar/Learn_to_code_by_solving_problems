cards = 52
deck = []

# Input 52 cards one by one
for card_name in range(cards):
    deck.append(input("card: "))

score_a = 0
score_b = 0
player = 'A'

# Returns True if no high cards (jack, queen, king, ace) are in the given list
def no_high_cards(card_list):
    if 'jack' in card_list:
        return False
    if 'queen' in card_list:
        return False
    if 'king' in card_list:
        return False
    if 'ace' in card_list:
        return False
    return True

for i in range(cards):
    card = deck[i]
    points = 0
    remaining = cards - i - 1  # cards left after current one

    # Check high card and ensure required number of following cards do not contain high cards
    if card.lower() == 'jack' and remaining >= 1 and no_high_cards(deck[i+1:i+2]):
        points = 1
    elif card.lower() == 'queen' and remaining >= 2 and no_high_cards(deck[i+1:i+3]):
        points = 2
    elif card.lower() == 'king' and remaining >= 3 and no_high_cards(deck[i+1:i+4]):
        points = 3
    elif card.lower() == 'ace' and remaining >= 4 and no_high_cards(deck[i+1:i+5]):
        points = 4

    if points > 0:
        print(f"player {player} scored {points} point(s).")

    if player == 'A':
        score_a = score_a + points
        player = 'B'
    else:
        score_b = score_b + points
        player = 'A'

print(f"player A: {score_a} point(s).")
print(f"player B: {score_b} point(s).")