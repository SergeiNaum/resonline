def get_prime_factors(n: int) -> list:
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def is_prime(n: int) -> bool:

    if n <= 1 or (n % 2 == 0 and n > 2):
        return False

    return all(n % i for i in range(3, int(n**0.5) + 1, 2))
