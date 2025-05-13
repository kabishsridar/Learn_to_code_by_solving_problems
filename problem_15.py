def is_non_decreasing(seq):
    return all(seq[i] <= seq[i+1] for i in range(len(seq) - 1))

def can_organize_boxes(boxes):
    from itertools import permutations

    for perm in permutations(boxes):
        combined = []
        for box in perm:
            combined.extend(box)
        if is_non_decreasing(combined):
            return "YES"
    return "NO"

# Example usage
boxes = [[4, 5, 7], [1, 2]]
print(can_organize_boxes(boxes))  # Output: YES

boxes = [[4, 5, 7], [6, 8]]
print(can_organize_boxes(boxes))  # Output: NO
