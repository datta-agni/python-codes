# check divisibility in a list of numbers


def divisible(n, num):
    # creating an empty list
    l = []

    # iterating till the range
    for i in range(0, n):
        element = int(input())
        # adding the element
        l.append(element)

    print(l)
    # use anonymous function to filter
    result = list(filter(lambda x: (x % num == 0), l))
    # display the result
    print("Numbers divisible by ", num, " are", result)


if __name__ == "__main__":
    divisible
    (
        int(input("Enter number of elements : ")),
        int(input("Enter the number by which you want to check the divisibility: ")),
    )
