# Looping binary search

def binary_search(values, target):
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        elif values[middle] > target:
            right = middle - 1
        else:
            return middle
    return -1


result = binary_search([2, 5, 7, 19, 23, 47], 23)


print(result)

# Recursive binary search


def binary_search(values, target, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(values) - 1

    # Base case: did not find item
    if left > right:
        return -1
    # Recursive case
    middle = (left + right) // 2
    if values[middle] < target:
        return binary_search(values, target, middle + 1, right)
    elif values[middle] > target:
        return binary_search(values, target, left, middle - 1)
    else:
        return middle


result = binary_search([2, 5, 7, 19, 23, 47], 5)


print(result)
