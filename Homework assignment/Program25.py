def isPalindromeNumber(num):
    return str(num) == str(num)[::-1]

def allPalindromes(arr):
    for num in arr:
        if not isPalindromeNumber(num):
            return False
    return True

print(allPalindromes([111, 222, 333, 444, 555]))  # True
print(allPalindromes([121, 131, 20]))             # False
