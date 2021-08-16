# find the factors of a number
def print_factors(x):
    array = []
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            element = i
            array.append(element)
    return array


def main():
    x = int(input("ENTER THE NUMBER FOR WHICH THE FACTOR IS TO BE CHECKED: "))
    print(print_factors(x))


if __name__ == "__main__":
    main()
