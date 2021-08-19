"""
Pyramid of Natural Numbers Less Than 10
Pattern:
1
2 3 4
5 6 7 8 9
"""


def full_pyramid():
    rows = int(input("ENTER THE NUMBER OF ROWS:"))
    currentNumber = 1
    stop = 2

    # Rows you want in your pattern
    for i in range(rows):
        for column in range(1, stop):
            print(currentNumber, end="")
            currentNumber += 1

        print("")
        stop += 2


"""
Half Pyramid Pattern of Numbers
Pattern:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""


def half_pyramid():
    rows = int(input("ENTER THE NUMBER OF ROWS:"))

    # Rows you want in your pattern
    for row in range(1, rows + 1):
        for column in range(1, row + 1):
            print(column, end=" ")

        print(" ")


if __name__ == "__main__":
    full_pyramid()
    half_pyramid()
