def findMinDiff(arr, m):
    n = len(arr)
    
    # Edge cases
    if m == 0 or n == 0:
        return 0
    
    if m > n:
        return -1
    
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Initialize minimum difference
    min_diff = float('inf')
    
    # Step 3: Check all windows of size m
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)
    
    return min_diff


# Example Test Cases
print(findMinDiff([3,4,1,9,56,7,9,12], 5))  # 6
print(findMinDiff([7,3,2,4,9,12,56], 3))    # 2
print(findMinDiff([3,4,1,9,56], 5))         # 55
