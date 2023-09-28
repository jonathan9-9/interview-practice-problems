def linear_search(values, target):
    for i, values in enumerate(values):
        if values == target:
            return i
    return -1


result = linear_search([3, 2, 9, 10, 27, 8, 1, 28], 27)
print(result)
