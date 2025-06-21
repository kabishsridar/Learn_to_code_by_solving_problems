wand_obeys = input() # which letter does wand obeys at starting
n = int(input()) # number of duels(Winner, loser)
z1_lst = [] # initiating z1_lst and z2_lst as an empty list
z2_lst = []
for defeats in range(n): # loop and prompt the user n times for which owner the wand currently obeys and defeated owner by space
    currently_wand_obeys = input().split() # prompt the user and split it
    z1_lst.append(currently_wand_obeys[0]) # append the first letter which is the present winner to z1 lst
    z2_lst.append(currently_wand_obeys[1]) # append the second letter who was defeated to z2 lst 

obeyed_set = set() # initiating a set, to count number of owners wand obeyed
obeyed_set.add(wand_obeys) # the first line of the input (first owner) will be added to the set

for owners in range(n):
    winner = z1_lst[owners] # loop through each winner in the z1 list and assign to winner
    loser = z2_lst[owners] # loop through each loser and in the z2 list and assign to loser
    if loser == wand_obeys: # if the loser in the second line(first line after the number of duels) is the one who wand obeyed to him at starting
        wand_obeys = winner # the the wand_obeys is the winner
        obeyed_set.add(wand_obeys) # add that winner to obeyed_set

print(wand_obeys) # currently the wand obeys to
print(len(obeyed_set)) # number of wizards the wand obeyed