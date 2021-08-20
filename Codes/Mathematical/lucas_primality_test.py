# Lucas Primality Test
import random
import math


def primeFactors(n, factors):
    """
    Function to generate prime factors of n
    """

    if n % 2 == 0:
        """
        If 2 is a factor
        """
        factors.append(2)

    while n % 2 == 0:
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        """
        If prime > 2 is factor
        """
        if n % i == 0:
            factors.append(i)

        while n % i == 0:
            n = n // i

    if n > 2:
        factors.append(n)

    return factors


def power(n, r, q):
    """
    This function produces power modulo some number.
    """
    total = n
    for i in range(1, r):
        total = (total * n) % q

    return total


def is_prime(n):
    """
    Base cases
    """
    if n == 1:
        return None
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    """
    Generating and storing factors of n-1
    """
    factors = []

    factors = primeFactors(n - 1, factors)

    """
    Array for random generator. This array is to ensure one number is generated  only once
    """
    rand = [i + 2 for i in range(n - 3)]

    """
    Shuffle random array to produce randomness
    """
    random.shuffle(rand)

    for i in range(n - 2):
        """
        Now one by one perform Lucas Primality. Test on random numbers generated.
        """
        a = rand[i]

        if power(a, n - 1, n) != 1:
            return False

        """
        This is to check if every factor of n-1 satisfy the condition
        """
        flag = True

        for k in range(len(factors)):

            """
            If a^((n-1)/q) equal 1
            """
            if power(a, (n - 1) // factors[k], n) == 1:
                flag = False
                break

    return flag


def main():
    number = int(input("""Enter number to be checked: """))
    if is_prime(number):
        print("Number is prime!")
    elif is_prime(number) == None:
        print("Number is neither prime nor composite!")
    else:
        print("The number is composite!")


if __name__ == "__main__":
    main()
