def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def prime_factors(n):
    factors = []

    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor

        divisor += 1

    if n > 1:
        factors.append(n)

    return factors


number = int(input("Enter a number: "))

print("Prime:", is_prime(number))
print("Prime factors:", prime_factors(number))