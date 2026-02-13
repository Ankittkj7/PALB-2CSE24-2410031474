def factorialDigits(n):
    result = [1]   # stores digits of factorial
    size = 1       # number of digits

    for x in range(2, n + 1):
        carry = 0
        for i in range(size):
            prod = result[i] * x + carry
            result[i] = prod % 10
            carry = prod // 10

        while carry > 0:
            result.append(carry % 10)
            carry //= 10
            size += 1

    return result[::-1]   # reverse to correct order


# Test cases
print(factorialDigits(5))     # [1, 2, 0]
print(factorialDigits(10))    # [3, 6, 2, 8, 8, 0, 0]
print(factorialDigits(1))     # [1]
