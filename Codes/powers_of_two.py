# Display the powers of 2 using anonymous function


def powers_of_two(terms):
    # use anonymous function
    result = list(map(lambda x: 2 ** x, range(terms)))
    print("The total terms are:", terms)
    for i in range(terms):
        print("2 raised to power", i, "is", result[i])


if __name__ == "__main__":
    powers_of_two(int(input("How many terms? ")))
