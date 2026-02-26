def combinationSum(candidates, target):
    result = []

    def backtrack(start, current, total):

        if total == target:
            result.append(current[:])
            return
        
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])     
            backtrack(i, current, total + candidates[i])  
            current.pop()                        

    backtrack(0, [], 0)
    return result


# Test Cases
print(combinationSum([2,3,6,7], 7))
print(combinationSum([2,3,5], 8))
print(combinationSum([2], 1))