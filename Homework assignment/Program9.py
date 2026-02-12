nums = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(nums)):
    remaining = target - nums[i]

    if remaining in seen:
        print([seen[remaining], i])
        break

    seen[nums[i]] = i
