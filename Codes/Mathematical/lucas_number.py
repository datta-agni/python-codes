# n'th Lucas Number

# Iterative function
def lucas(number):

    # declaring base values for positions 0 and 1
    a0 = 2
    a1 = 1

    if number == 0:
        return a0

    # generating number
    for i in range(2, number + 1):
        c = a0 + a1
        a0 = a1
        a1 = c

    return a1


def main():
    number = int(input("Enter the limit for the Lucas Number: "))
    print(lucas(number))


if __name__ == "__main__":
    main()
