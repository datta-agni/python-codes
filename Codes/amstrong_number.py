# program to check if the number is an armstrong number or not


def is_armstrong(num):
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
        return True
    else:
        False


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_armstrong(num):
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
