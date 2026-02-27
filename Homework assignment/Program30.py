import bisect

def matrixMedian(matrix):
    r = len(matrix)
    c = len(matrix[0])


    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)

    desired = (r * c) // 2  

    while low < high:
        mid = (low + high) // 2


        count = 0
        for row in matrix:
            count += bisect.bisect_right(row, mid)

        if count <= desired:
            low = mid + 1
        else:
            high = mid

    return low


# Example 
mat1 = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
print(matrixMedian(mat1))  # 5

# Example
mat2 = [
    [2, 4, 9],
    [3, 6, 7],
    [4, 7, 10]
]
print(matrixMedian(mat2))  # 6

# Example
mat3 = [
    [3],
    [4],
    [8]
]
print(matrixMedian(mat3))  # 4
