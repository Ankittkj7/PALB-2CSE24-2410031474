def combinationSum2(candidates, target):
    candidates.sort()   # Important to handle duplicates
    result = []

    def backtrack(start, current, total):
        if total == target:
            result.append(current[:])
            return
        
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            current.append(candidates[i])
            backtrack(i + 1, current, total + candidates[i])  # move to next index
            current.pop()

    backtrack(0, [], 0)
    return result


# Test Cases
print(combinationSum2([10,1,2,7,6,1,5], 8))
print(combinationSum2([2,5,2,1,2], 5))
