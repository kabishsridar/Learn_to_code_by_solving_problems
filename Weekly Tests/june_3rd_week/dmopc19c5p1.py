# how many assignments can he complete with available items
first_line = input()# prompting the number of items and number of assignments
parts = first_line.split()
n = int(parts[0]) # number of items
m = int(parts[1]) # number of assignments

his_items = set() # initiating a set to store items

for i in range(n):
    item = input().strip() # get item names for next n lines
    his_items.add(item) # add them to his_items

# initiate complete_assignments to 0 to count number of assignments he can complete
completed_assignments = 0

for i in range(m): # loop through each assignment
    k_line = input() # get number of items this assignment needs
    k = int(k_line) # convert to integer to use as range in for loop

    required_items = [] # initiate required_items as an empty list to store the items required for assignment

    for j in range(k): # all required items for assignment
        req_item = input().strip() # prompt item name
        required_items.append(req_item) # append to required item

    can_complete = True # initiate can_complete as True 
    for item in required_items: # loop through each required items
        if item not in his_items: # if any required item is not available in the list
            can_complete = False # change can_complete to False
            break # then break

    if can_complete: # if can_complete is True, then completed_assignments should incremented by 1
        completed_assignments += 1

print(completed_assignments) # display the result