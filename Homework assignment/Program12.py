def minimize_height_difference(arr, k):
    n = len(arr)
    arr.sort()

    ans = arr[n - 1] - arr[0]

    smallest = arr[0] + k
    largest = arr[n - 1] - k

    for i in range(1, n):
        min_height = min(smallest, arr[i] - k)
        max_height = max(largest, arr[i - 1] + k)

        if min_height < 0:
            continue

        ans = min(ans, max_height - min_height)

    return ans


# Example
k = 2
arr = [1, 5, 8, 10]

print(minimize_height_difference(arr, k))  
