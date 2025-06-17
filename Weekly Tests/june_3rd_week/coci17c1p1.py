cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11] * 4
# print(cards)
n = int(input()) # number of cards drawn so far
drawn_sum = 0
drawn_cards = []
for card in range(n):
    drew = int(input()) # ith card caeser drew
    drawn_sum += drew
    drawn_cards.append(drew) # the cards drew will be stored in dran_cards
    
deck = cards.copy() # copying the original so that we can remove the cards from deck
for card in drawn_cards:
    deck.remove(card)

dif = 21 - drawn_sum

safe = 0
risky = 0

for card in deck:
    if card <= dif:
        safe += 1
    else:
        risky += 1

if risky >= safe:
    print("DOSTA")
else:
    print("VUCI")