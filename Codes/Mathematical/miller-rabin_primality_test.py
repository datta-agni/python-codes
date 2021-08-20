def is_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    # n  is definitely composite
    return True


def is_prime(n, precision=16):
    if n in primes:
        return True
    if any((n % p) == 0 for p in primes) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if n < 1373653:
        return not any(is_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(is_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(is_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(is_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(is_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(is_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(is_composite(a, d, n, s) for a in primes[:precision])


primes = [2, 3]
primes += [x for x in range(5, 1000, 2) if is_prime(x)]


def main():
    number = int(input("Enter the number to check for primality: "))
    if is_prime(number):
        print("The number", number, "is prime.")
    else:
        print("The number", number, "is composite.")


if __name__ == "__main__":
    main()
