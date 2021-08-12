# program to check if the number is an armstrong number or not


def main(num=int(input("Enter a number: "))):
    # initialize sum
    sum = 0
    num = 0
    temp = num
    # find the sum of the cube of each digit
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    # display the result
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")


if __name__ == "__main__":
    main()
