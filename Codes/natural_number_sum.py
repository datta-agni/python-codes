# Sum of natural numbers up to num
def main():
    num = int(input("ENTER A NUMBER: "))

    if num < 0:
        print("Enter a positive number")
    else:
        sum = 0
        # use while loop to iterate until zero
        while (num > 0):
            sum += num
            num -= 1
        print("The sum is", sum)


if __name__ == '__main__':
    main()