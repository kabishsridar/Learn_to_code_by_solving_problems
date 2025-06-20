def read_boxes(n): # defining a function read_boxes to read heights of n number of boxes from user's input
    boxes = [] # initiating boxes to an empty list
    for i in range(n): # loop though each boxes
        box = input("Enter heights(in by leaving a space between the boxes): ").split() # prompting the user for height of boxes and split into list
        box.pop(0)  # Remove the first element which is the number of boxes
        if len(box) == 0:  # If box is empty after popping, instruct the user
            print("Error: Box must contain at least one height!")
            continue
        for i in range(len(box)): # loop through each heights
            box[i] = int(box[i])
        boxes.append(box) # add box into boxes
    return boxes

def box_ok(box):  # Function to check if the heights in a box are non-decreasing
    for i in range(len(box) - 1): # Iterate through adjacent heights
        if box[i] > box[i + 1]: # If a height is greater than the next one, return False
            return False
    return True # Return True if all heights are in non-decreasing order

def all_boxes_ok(boxes): # Function to check if all boxes satisfy the non-decreasing order
    for box in boxes: # Iterate through each box
        if not box_ok(box):  # If any box fails the check, return False
            return False
    return True # Return True if all boxes are okay

def boxes_endpoints(boxes): # Function to get endpoints (first and last height)
    endpoints = [] # Initialize list to store endpoints
    for box in boxes:
        if len(box) == 0: # Skip empty boxes
            continue  # Skip if box is empty
        endpoints.append([box[0], box[-1]]) # Store first and last element of the box
    return endpoints # return as list

def all_endpoints_ok(endpoints): # Function to check if endpoints satisfy the increasing order condition
    maximum = endpoints[0][1]  # Set the initial maximum endpoint
    for i in range(1, len(endpoints)): # Iterate through the endpoints
        if endpoints[i][0] < maximum: # If a starting endpoint is smaller than the previous maximum, return False
            return False
        maximum = endpoints[i][1]
    return True 

n = int(input("Enter the number of boxes (1 to 100): "))  # Get number of boxes from user
boxes = read_boxes(n)  # Read the box heights

if not all_boxes_ok(boxes):  # Check if all boxes are okay (non-decreasing)
    print('NO')
else:
    endpoints = boxes_endpoints(boxes)  # Get the endpoints of the boxes
    endpoints.sort()  # Sort the endpoints

    if all_endpoints_ok(endpoints):  # Check if the sorted endpoints are okay
        print('YES')
    else:
        print('NO')