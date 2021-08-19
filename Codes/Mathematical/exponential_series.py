# program to calculate e raise to the power x


# Function to calculate value using sum of first n terms of Taylor Series
def exponential(n, x):
    # initialize sum of series
    sum = 1.0
    for i in range(n, 0, -1):
        sum = 1 + x * sum / i
    return sum


# Driver program to test above function
if __name__ == "__main__":
    n = int(input("Enter the limit for number of terms: "))
    x = int(input("Enter x for which the e^x is calculated: "))
    print("e^x = ", exponential(n, x))
