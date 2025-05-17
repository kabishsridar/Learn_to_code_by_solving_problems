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