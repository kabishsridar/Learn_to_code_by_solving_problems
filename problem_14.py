NUM_CARDS = 52 # Total number of cards in the deck

def no_high(lst):
    for card in lst: # loop through every card in list
        if card in {'jack', 'queen', 'king', 'ace'}:
            return False  # if any high card is found, return False immediately
    return True # if no high cards , return true

deck = [] # initialse an empty list deck

#collect 52 cards from the user one by one
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

       # Scoring rules based on card type and remaining cards
    if card == 'jack' and remaining >= 1 and no_high(deck[i+1:i+2]):
        points = 1  # Jack scores 1 point if the next card is not a high card
    elif card == 'queen' and remaining >= 2 and no_high(deck[i+1:i+3]):
        points = 2  # Queen scores 2 points if the next two cards are not high cards
    elif card == 'king' and remaining >= 3 and no_high(deck[i+1:i+4]):
        points = 3  # King scores 3 points if the next three cards are not high cards
    elif card == 'ace' and remaining >= 4 and no_high(deck[i+1:i+5]):
        points = 4  # Ace scores 4 points if the next four cards are not high cards

    if points > 0:
        print(f'Player {player} scores {points} point(s).')

    if player == 'A':
        score_a += points
        player = 'B'
    else:
        score_b += points
        player = 'A'

# Display final scores and determine the winner
print("\nFinal Scores:")
print(f'Player A: {score_a} point(s).')
print(f'Player B: {score_b} point(s).')

if score_a > score_b:
    print("Player A wins!") # if score_a is greater than score_b print player a wins
elif score_b > score_a:
    print("Player B wins!") # if score_b is greater than score_b print player b wins
else:
    print("It's a tie!") # declare a tie if both have same score
