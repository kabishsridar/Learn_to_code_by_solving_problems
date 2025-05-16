TOTAL_CARDS = 52
HIGH_CARDS = ['jack', 'queen', 'king', 'ace']

# Read 52 cards from input
deck = [input().strip().lower() for _ in range(TOTAL_CARDS)]

score_a = 0
score_b = 0
current_player = 'A'

# Helper function to check if the next few cards contain any high cards
def no_high_cards(cards_to_check):
    for card in cards_to_check:
        if card in HIGH_CARDS:
            return False  # Return False immediately if any high card is found
    return True

# Go through each card in the deck
for i in range(TOTAL_CARDS):
    card = deck[i]
    points = 0
    cards_remaining = TOTAL_CARDS - i - 1  # Cards left after current one

    # Scoring rules for each high card
    if card == 'jack' and cards_remaining >= 1:
        next_cards = deck[i + 1 : i + 2]
        if no_high_cards(next_cards):
            points = 1

    elif card == 'queen' and cards_remaining >= 2:
        next_cards = deck[i + 1 : i + 3]
        if no_high_cards(next_cards):
            points = 2

    elif card == 'king' and cards_remaining >= 3:
        next_cards = deck[i + 1 : i + 4]
        if no_high_cards(next_cards):
            points = 3

    elif card == 'ace' and cards_remaining >= 4:
        next_cards = deck[i + 1 : i + 5]
        if no_high_cards(next_cards):
            points = 4

    if points > 0:
        print(f"Player {current_player} scored {points} point(s).")

    # Update score and switch player
    if current_player == 'A':
        score_a += points
        current_player = 'B'
    else:
        score_b += points
        current_player = 'A'

print(f"Player A: {score_a} point(s).")
print(f"Player B: {score_b} point(s).")
