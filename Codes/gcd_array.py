# GCD of more than two (or array) numbers


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def main():
    n =int(input("Enter the number of elements: "))
    # creating an empty list
    l = []
    # iterating till the range
    for i in range(0, n):
        element = int(input())
        l.append(element)  # adding the element
    print(l)
    num1 = l[0]
    num2 = l[1]
    gcd = find_gcd(num1, num2)

    for i in range(2, len(l)):
        gcd = find_gcd(gcd, l[i])
    print(gcd)


if __name__ == "__main__":
    main()
