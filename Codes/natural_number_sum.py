# sum of natural numbers up to num


def sum_natural_numbers(num):
    if num < 0:
        print("Enter a positive number")
    else:
        sum = 0
        # use while loop to iterate until zero
        while num > 0:
            sum += num
            num -= 1
    print("The sum is", sum)


if __name__ == "__main__":
    sum_natural_numbers(num=int(input("Find the Sum of N natural numbers: ")))
