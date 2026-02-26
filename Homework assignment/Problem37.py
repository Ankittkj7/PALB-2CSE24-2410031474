def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    first_row_zero = False
    first_col_zero = False

    # Check if first row has zero
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # Check if first column has zero
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break

    # Use first row and column as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set matrix cells to zero based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Set first row to zero if needed
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Set first column to zero if needed
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0


# 🔹 Test Example 1
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix1)
print(matrix1)

# 🔹 Test Example 2
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix2)
print(matrix2)