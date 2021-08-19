# A function to print all prime factors of a given number python program to print prime factors
import math


# prime function
def primeFactors(n):
    array = []

    # no of even divisibility
    while n % 2 == 0:
        array.append(int(2)),
        n = n / 2

    # n reduces to become odd
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n
        while n % i == 0:
            array.append(int(i))
            n = n / i

    # if n is a prime
    if n > 2:
        array.append(int(n))

    return array


def main():
    print(primeFactors(int(input("ENTER ANY NUMBER: "))))


if __name__ == "__main__":
    main()
