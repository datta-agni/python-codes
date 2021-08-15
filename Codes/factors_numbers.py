# find the factors of a number
def print_factors(x):
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


def main():
    print_factors
    (int(input("ENTER THE NUMBER FOR WHICH THE FACTOR IS TO BE CHECKED: ")))


if __name__ == "__main__":
    main()
