def nextGap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)

def mergeSortedArrays(a, b):
    n = len(a)
    m = len(b)

    gap = nextGap(n + m)

    while gap > 0:
        i = 0
        j = gap

        while j < n + m:
            # Case 1: both pointers in array a
            if i < n and j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]

            # Case 2: i in a, j in b
            elif i < n and j >= n:
                if a[i] > b[j - n]:
                    a[i], b[j - n] = b[j - n], a[i]

            # Case 3: both pointers in array b
            else:
                if b[i - n] > b[j - n]:
                    b[i - n], b[j - n] = b[j - n], b[i - n]

            i += 1
            j += 1

        gap = nextGap(gap)


# Example 1
a = [2, 4, 7, 10]
b = [2, 3]
mergeSortedArrays(a, b)
print(a, b)

# Example 2
a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
mergeSortedArrays(a, b)
print(a, b)

# Example 3
a = [0, 1]
b = [2, 3]
mergeSortedArrays(a, b)
print(a, b)
