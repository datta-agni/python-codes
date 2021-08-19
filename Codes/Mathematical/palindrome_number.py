# palindrome numbers


def is_palindrome(number):
    # store a copy of this number
    temp = number
    # calculate reverse of this number
    reverse_num = 0

    while number > 0:
        # extract last digit of this number
        digit = number % 10
        # append this digit in reversed number
        reverse_num = reverse_num * 10 + digit
        # floor divide the number leave out the last digit from number
        number = number // 10

    # compare reverse to original number
    if temp == reverse_num:
        return True
    else:
        False


if __name__ == "__main__":
    if is_palindrome(int(input("Enter any number :"))):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")
