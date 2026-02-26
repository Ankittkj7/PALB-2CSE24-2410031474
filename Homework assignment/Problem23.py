def canArrange(arr, a, b):
    k = a + b
    
    # If number of elements is odd → impossible
    if len(arr) % 2 != 0:
        return False
    
    remainder_count = {}
    
    for num in arr:
        remainder = num % k
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
    
    for r in remainder_count:
        
        # Case 1: remainder 0
        if r == 0:
            if remainder_count[r] % 2 != 0:
                return False
        
        # Case 2: remainder = k/2 (when k even)
        elif 2 * r == k:
            if remainder_count[r] % 2 != 0:
                return False
        
        # Case 3: general case
        else:
            if remainder_count.get(r, 0) != remainder_count.get(k - r, 0):
                return False
    
    return True


# Example 1
print(canArrange([1,2,3,3,4], 1, 3))  # True

# Example 2
print(canArrange([1,4,3,6,2,1], 1, 3))  # True