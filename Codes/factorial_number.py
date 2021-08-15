# program to find the factorial of a number provided by the user.
# change the value for a different result num = a


def print_fact(num):
    factorial = 1
    # check if the number is negative, positive or zero
    if num < 0:
        return -1

    elif num == 0:
        return 0
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        return factorial


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("The factorial of", num, "is", print_fact(num))
