def plusOne(digits):
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0   # carry over

    # If all digits were 9
    return [1] + digits


# Test Cases
print(plusOne([1,2,3]))   # [1,2,4]
print(plusOne([4,3,2,1])) # [4,3,2,2]
print(plusOne([9]))       # [1,0]

