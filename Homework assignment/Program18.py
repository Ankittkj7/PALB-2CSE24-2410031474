def factorialDigits(n):
    # Result stored as digits
    result = [1]

    for i in range(2, n + 1):
        carry = 0
        for j in range(len(result)):
            prod = result[j] * i + carry
            result[j] = prod % 10
            carry = prod // 10

        # Handle remaining carry
        while carry:
            result.append(carry % 10)
            carry //= 10

    # Digits are stored in reverse order
    return result[::-1]


# Examples
print(factorialDigits(5))   # [1, 2, 0]
print(factorialDigits(10))  # [3, 6, 2, 8, 8, 0, 0]
print(factorialDigits(1))   # [1]
