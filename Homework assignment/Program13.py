def minJumps(arr):
    n = len(arr)

    if n <= 1:
        return 0

    # If first element is 0, we cannot move
    if arr[0] == 0:
        return -1

    # Initialize
    jumps = 1
    max_reach = arr[0]
    steps = arr[0]

    for i in range(1, n):
        # If we have reached the last index
        if i == n - 1:
            return jumps

        # Update maximum reach
        max_reach = max(max_reach, i + arr[i])
        steps -= 1

        # If no steps remain
        if steps == 0:
            jumps += 1

            # If current position is not reachable
            if i >= max_reach:
                return -1

            # Reinitialize steps
            steps = max_reach - i

    return -1


# Example
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(arr)) 
