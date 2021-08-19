# program to compute value of GCD(LCM(x,y), LCM(x,z))
# given three integers x, y, z, the task is to compute the value of GCD(LCM(x,y), LCM(x,z)).

# Recursive function to return gcd of a and b


def __gcd(a, b):
    # Everything divides 0
    if a == 0 or b == 0:
        return 0
    # base case
    if a == b:
        return a
    # a is greater
    if a > b:
        return __gcd(a - b, b)
    return __gcd(a, b - a)


# Returns value of GCD(LCM(x,y), LCM(x,z))
def findValue(x, y, z):
    g = __gcd(y, z)
    # Return LCM(x, GCD(y, z))
    return (x * g) / __gcd(x, g)


def main():
    x = int(input("Enter the 1st number: "))
    y = int(input("Enter the 2nd number: "))
    z = int(input("Enter the 3rd number: "))
    print("%d" % findValue(x, y, z))


if __name__ == "__main__":
    main()
