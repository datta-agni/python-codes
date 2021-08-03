# find duplicates in array


def duplicates(arr, n):
    if n == 0 or n == 1:
        return n
    temp = list(range(n))
    j = 0
    for i in range(0, n - 1):
        if arr[i] != arr[i + 1]:
            temp[j] = arr[i]
            j += 1
        temp[j] = arr[n - 1]
    j += 1
    for i in range(0, j):
        arr[i] = temp[i]
    return j


def main():
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    n = len(arr)
    n = duplicates(arr, n)
    for i in range(n):
        print("%d" % (arr[i]), end=" ")


if __name__ == "__main__":
    main()
