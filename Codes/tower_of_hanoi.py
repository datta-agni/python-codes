# Tower of Hanoi recursion problem


def hanoi(number_disks, startPeg=1, endPeg=3):
    if number_disks:
        hanoi(number_disks - 1, startPeg, 6 - startPeg - endPeg)
        print("Move disk %d from peg %d to peg %d" %
              (number_disks, startPeg, endPeg))
        hanoi(number_disks - 1, 6 - startPeg - endPeg, endPeg)


def main():
    hanoi(number_disks=int(input("Enter the number of discs: ")))


if __name__ == '__main__':
    main()
