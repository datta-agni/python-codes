"""
==============
Binary Search
==============
TIme Complexity
    Worst Case : O( log(n) )
    Average Case : O( log(n) )
    Best Case : O(1)
Space Complexity : O(1)
Binary Search is a sorting algorithm in which we select the middle element and compare key to the middle element if key is
smaller then we search before middle else after middle. If key is found we return the index of key else -1.
Iterative Binary Search Function method Python Implementation.
It returns index of n in given array if present, else returns -1   
"""


def binary_search(array, n):
    low = 0
    high = len(array) - 1
    middle = 0

    while low <= high:

        # for get integer result
        middle = (high + low) // 2

        # Check if n is present at middle
        if array[middle] < n:
            low = middle + 1

        # If n is greater, compare to the right of middle
        elif array[middle] > n:
            high = middle - 1

        # If n is smaller, compared to the left of middle
        else:
            return middle
            # element was not present in the list, return -1
    return -1


def main():
    # Initial array, creating an empty array
    array = []

    # number of elements as input
    n = int(input("Enter number of elements : "))
    print("Enter the elements: ")
    # iterating till the range
    for i in range(0, n):
        element = int(input())
        # adding the element
        array.append(element)

    print(array)
    number = int(input("Enter the number to be searched: "))
    # Function call
    result = binary_search(array, number)

    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")


if __name__ == "__main__":
    main()
