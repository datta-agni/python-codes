# duplicate element in an array

def duplicate_elements(arr, size):
    print("The duplicate elements are: ")
    for i in range(0, size):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")


def main():
    # creating an empty list
    n = int(input("Enter the number of elements: "))
    array = []
    # iterating till the range
    for i in range(0, n):
        element = int(input())
        array.append(element)  # adding the element

    print(array)
    array_size = len(array)
    duplicate_elements(array, array_size)


if __name__ == "__main__":
    main()
