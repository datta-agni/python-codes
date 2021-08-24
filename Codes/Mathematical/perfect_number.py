def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


if __name__ == "__main__":
    print(perfect_number(int(input("Enter the number to check for perfect number: "))))
