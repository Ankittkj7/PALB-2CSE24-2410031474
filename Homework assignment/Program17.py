def factorialDigits(n):
    result = [1]
    size = 1

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

    return result[::-1]


print(factorialDigits(5))
print(factorialDigits(10))
print(factorialDigits(1))
