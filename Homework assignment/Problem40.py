def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2
        
        # Convert 1D index to 2D position
        row = mid // n
        col = mid % n
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Example 1
matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]

print(searchMatrix(matrix, 3))   # True
print(searchMatrix(matrix, 13))  # False