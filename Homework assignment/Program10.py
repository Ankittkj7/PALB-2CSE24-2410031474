arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)


if n == 1:
    print(0)


elif arr[0] == 0:
    print(-1)

else:
    jumps = 1
    max_reach = arr[0]
    steps = arr[0]

    for i in range(1, n):
        
        if i == n - 1:
            print(jumps)
            break

        
        max_reach = max(max_reach, i + arr[i])
        steps -= 1

    
        if steps == 0:
            jumps += 1

        
            if i >= max_reach:
                print(-1)
                break

            steps = max_reach - i
