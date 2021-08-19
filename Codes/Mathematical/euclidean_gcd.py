# program to demonstrate working of extended euclidean algorithm

# function for extended Euclidean Algorithm
# Python program for the extended Euclidean algorithm
def euclidean_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = euclidean_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


if __name__ == "__main__":
    x = int(input("Enter the numbers whose GCD is to be checked: "))
    y = int(input("Enter the numbers whose GCD is to be checked: "))
    gcd, x, y = euclidean_gcd(x, y)
    print("The GCD is", gcd)
    print(f"x = {x}, y = {y}")
