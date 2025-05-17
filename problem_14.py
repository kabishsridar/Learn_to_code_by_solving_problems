<<<<<<< HEAD
high_cards = ['jack', 'queen', 'king', 'ace']
high_card_points = {'jack': 1, 'queen': 2, 'king': 3, 'ace': 4}

score_a = 0
score_b = 0
player = 'A'  # Player A starts first

# Function to check if there are no high cards(jack, queen, king, ace) in the next n cards
def no_high_cards(card_list):
    for card in card_list:
        if card in high_cards:
            return False
    return True

# Read the input of all 52 cards one by one
deck = []
valid_cards = ['jack', 'queen', 'king', 'ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

print("Welcome to the Card Game!")
print("There are 52 cards in the deck, and we need you to enter the name or number of each card one by one.")
print("You can enter the cards as: 1, 2, 3, ..., 10, jack, queen, king, ace.")

# Collect 52 cards from the user
for i in range(52):
    while True:
        card = input(f"Enter card {i + 1}: ").strip().lower()
        
        # Convert numeric cards to their word equivalents for consistency
        if card.isdigit() and int(card) in range(1, 11):
            card = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'][int(card) - 2]
        
        if card in valid_cards:
            deck.append(card)
            break
        else:
            print("Invalid card name. Please enter a valid card (1-10, jack, queen, king, ace).")

print("\nGame starts now!")

for i in range(52):
    card = deck[i]
    points = 0
    remaining_cards = deck[i + 1:]  # Remaining cards after the current one

    if card == 'jack' and len(remaining_cards) >= 1 and no_high_cards(remaining_cards[:1]):
        points = 1
    elif card == 'queen' and len(remaining_cards) >= 2 and no_high_cards(remaining_cards[:2]):
        points = 2
    elif card == 'king' and len(remaining_cards) >= 3 and no_high_cards(remaining_cards[:3]):
        points = 3
    elif card == 'ace' and len(remaining_cards) >= 4 and no_high_cards(remaining_cards[:4]):
        points = 4

    if points > 0:
        print(f"Player {player} scored {points} point(s) by playing {card}.")

    if player == 'A':
        score_a += points
        player = 'B'
    else:
        score_b += points
        player = 'A'

print("\nGame over!")
print(f"Final scores:")
print(f"Player A: {score_a} point(s).")
print(f"Player B: {score_b} point(s).")

if score_a > score_b:
    print("Player A wins!")
elif score_b > score_a:
    print("Player B wins!")
else:
    print("It's a tie!")
=======
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
>>>>>>> f7abfe934674933cae19db4f30aa03c8342a43d5
