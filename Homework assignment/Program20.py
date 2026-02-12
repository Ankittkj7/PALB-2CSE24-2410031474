def isSubset(a, b):
    freq = {}

    # Count elements of a[]
    for x in a:
        freq[x] = freq.get(x, 0) + 1

    # Check elements of b[]
    for x in b:
        if x not in freq or freq[x] == 0:
            return False
        freq[x] -= 1

    return True


print(isSubset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]))  
print(isSubset([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]))          
print(isSubset([10, 5, 2, 23, 19], [19, 5, 3]))             
