digits = "0123456789abcdefghijklmnopqrstuvwxyz"


def baseN(num, b):
    return digits[num] if num < b else baseN(num // b, b) + digits[num % b]


def main():
    number = int(input("Enter the number to be converted: "))
    base = int(input("Enter the base of the number: "))
    print(baseN(number, base))


if __name__ == "__main__":
    main()
