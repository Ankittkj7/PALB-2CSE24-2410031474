def findMedian(arr):
    n = len(arr)
    arr.sort() 
    
    if n % 2 != 0:
        return arr[n // 2]
    
    else:
        mid1 = arr[n // 2]
        mid2 = arr[(n // 2) - 1]
        return (mid1 + mid2) / 2


# Examples
print(findMedian([90, 100, 78, 89, 67]))  # 89
print(findMedian([56, 67, 30, 79]))       # 61.5
print(findMedian([1, 2]))                 # 1.5
