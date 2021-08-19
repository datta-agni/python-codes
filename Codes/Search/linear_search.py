"""
==============
Linear Search
==============
TIme Complexity
    Worst Case : O(n)
    Average Case : O(n)
    Best Case : O(1)
Space Complexity : O(1)
------------
This is a searching algorithm that iterates over each element to find the key element
If key is found it will return the position
else -1
------------
"""


def linear_Search(array, n, key):
    # Searching array sequentially
    for i in range(0, n):
        if array[i] == key:
            return i + 1
    return -1


def main():
    # creating an empty list
    array = []
    # number of elements as input
    n = int(input("Enter number of elements : "))
    # iterating till the range
    for i in range(0, n):
        element = int(input())
        # adding the element
        array.append(element)
    print(array)

    key = int(input("Enter the element to be searched: "))
    res = linear_Search(array, n, key)
    if res == -1:
        print("Element not found")
    else:
        print("Element found at index: ", res)


if __name__ == "__main__":
    main()
