def is_sorted(numbers):
    for index in range(len(numbers) - 1):
        if numbers[index] > numbers[index + 1]:
            return False
    return True

def can_arrange_boxes(box_list):
    number_of_boxes = len(box_list)

    if number_of_boxes == 1:
        combined_items = box_list[0]
        if is_sorted(combined_items):
            return "YES"
        else:
            return "NO"

    elif number_of_boxes == 2:
        first_try = box_list[0] + box_list[1]
        if is_sorted(first_try):
            return "YES"

        second_try = box_list[1] + box_list[0]
        if is_sorted(second_try):
            return "YES"
        return "NO"
    else:
        print("Too many boxes to check with this simple code")
        
boxes_one = [[4, 5, 7], [1, 2]]
print(can_arrange_boxes(boxes_one))  # Output: YES

boxes_two = [[4, 5, 7], [6, 8]]
print(can_arrange_boxes(boxes_two))  # Output: NO
