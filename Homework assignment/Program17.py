def commonElements(arr1, arr2, arr3):
    i = j = k = 0
    result = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        # If all three are equal
        if arr1[i] == arr2[j] == arr3[k]:
            # Add only once
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])

            # Skip duplicates
            val = arr1[i]
            while i < len(arr1) and arr1[i] == val:
                i += 1
            while j < len(arr2) and arr2[j] == val:
                j += 1
            while k < len(arr3) and arr3[k] == val:
                k += 1

        # Move pointer with smallest value
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return result if result else [-1]


# Examples
print(commonElements(
    [1, 5, 10, 20, 40, 80],
    [6, 7, 20, 80, 100],
    [3, 4, 15, 20, 30, 70, 80, 120]
))

print(commonElements(
    [1, 2, 3, 4, 5],
    [6, 7],
    [8, 9, 10]
))

print(commonElements(
    [1, 1, 1, 2, 2, 2],
    [1, 1, 2, 2, 2],
    [1, 1, 1, 1, 2, 2, 2, 2]
))
