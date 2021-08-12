def bit_length_of_binary(n: int) -> int:
    # bit length of the binary sequence
    return n.bit_length()


def convert_to_binary(n: int) -> str:
    # conversion from decimal to binary
    return bin(n)[2:]


def convert_to_decimal(s: str) -> int:
    # conversion of binary to decimal
    return int(s, 2)


def check_even(n: int) -> int:
    # check wether the number is even or odd
    return True if n & 1 == 0 else False


def complement(n: int) -> int:
    # XOR of the binary bit sequence or 1's compliment
    # XOR with a binary number 1...1(m times), where m is the bit length of the number will give complement of that number
    return ((1 << n.bit_length()) - 1) ^ n


def input_user(bin=True):
    # take user from the based wether it is a binary or decimal
    if bin:
        return int(input("Enter the binary input: "))
    else:
        return int(input("Enter the decimal input: "))


def main():

    choice = int(
        input(
            """
        Enter
        \n 1) to find the length of binary strings in bits:
        \n2) to convert decimal into binary:
        \n3) to convert binary to decimal:
        \n4) to check wether it is odd or even:
        \n5) to convert a binary number in 1's complement form:
        \n"""
        )
    )

    if choice == 1:
        print(bit_length_of_binary((input_user(True))))
    elif choice == 2:
        print(convert_to_binary(input_user(False)))
    elif choice == 3:
        print(convert_to_decimal(str(input_user(True))))
    elif choice == 4:
        print(check_even(input_user(False)))
    elif choice == 5:
        print(complement(input_user(True)))


if __name__ == "__main__":
    main()
