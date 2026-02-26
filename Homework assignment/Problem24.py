def minSwaps(arr, k):
    n = len(arr)
    
    good = 0
    for num in arr:
        if num <= k:
            good += 1
    
    bad = 0
    for i in range(good):
        if arr[i] > k:
            bad += 1
    
    min_swaps = bad
    
    i = 0
    j = good
    
    while j < n:
        if arr[i] > k:
            bad -= 1
        
        if arr[j] > k:
            bad += 1
        
        min_swaps = min(min_swaps, bad)
        
        i += 1
        j += 1
    
    return min_swaps

print(minSwaps([2, 1, 5, 6, 3], 3))       # 1
print(minSwaps([2, 7, 9, 5, 8, 7, 4], 6)) # 2
print(minSwaps([2, 4, 5, 3, 6, 1, 8], 6)) # 0