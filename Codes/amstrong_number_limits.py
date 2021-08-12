# program to check Armstrong numbers in a certain interval


def armstrong_limits(
    lower=int(input("Enter the lower limit: ")),
    upper=int(input("Enter the upper limit: ")) + 1,
):
    for num in range(lower, upper):
        # order of number
        order = len(str(num))
        # initialize sum
        sum = 0

        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print(num)


if __name__ == "__main__":
    armstrong_limits()
