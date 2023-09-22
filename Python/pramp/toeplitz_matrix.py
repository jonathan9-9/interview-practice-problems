# A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element. Given a non-empty
# matrix arr, write a function that returns true if and only if it is a Toeplitz matrix. The matrix can be any
# dimensions, not necessarily square.

# [[1,2,3,4],
#  [5,1,2,3],
#  [6,5,1,2]]

# is a Toeplitz matrix, so we should return true, while

# [[1,2,3,4],
#  [5,1,9,3],
#  [6,5,1,2]]

# isn’t a Toeplitz matrix, so we should return false.


def isToeplitz(arr):
    rows = len(arr)
    cols = len(arr[0])

    if rows == 0 or cols == 0:
        return True
    for i in range(rows - 1):
        for j in range(cols - 1):
            if arr[i][j] != arr[i + 1][j + 1]:
                return False
    return True


input = [[1, 2, 3, 4], [5, 1, 2, 3], [6, 5, 1, 2]]
result = isToeplitz(input)
print(result)
