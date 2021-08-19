# product of N fractions in reduced form.

# Function to return gcd of a and b
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


# Print the Product of N fraction in Reduced Form.
def productReduce(n, num, den):
    new_numerator = 1
    new_denominator = 1

    # finding the product of all N numerators and denominators.
    for i in range(n):
        new_numerator = new_numerator * num[i]
        new_denominator = new_denominator * den[i]

    # Finding GCD of new numerator and denominator
    GCD = gcd(new_numerator, new_denominator)

    # Converting into reduced form.
    new_numerator = new_numerator / GCD
    new_denominator = new_denominator / GCD

    print(int(new_numerator), "/", int(new_denominator))


def input_list(n):
    # creating an empty list
    l = []
    # iterating till the range
    for i in range(0, n):
        element = int(input())
        # adding the element
        l.append(element)
    return l


def main():
    n = int(input("Enter the number of fractions: "))
    print("Enter the numerators:")
    numerator = input_list(n)
    print("Enter the denominators:")
    denominator = input_list(n)
    print("Numerators  : ", numerator)
    print("Denominator : ", denominator)
    productReduce(n, numerator, denominator)


if __name__ == "__main__":
    main()
