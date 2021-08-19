# python program to find LCM of two numbers
# recursive function to return gcd of a and b
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


# function to return LCM of two numbers
def lcm(a, b):
    return (a / gcd(a, b)) * b


# driver program to test above function
def main():
    a = int(input("ENTER THE 1st NUMBER: \n"))
    b = int(input("ENTER THE 2nd NUMBER: \n"))
    print('LCM of', a, 'and', b, 'is', lcm(a, b))


if __name__ == '__main__':
    main()
