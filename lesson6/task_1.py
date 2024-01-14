def binarySearch(list_input, start, end, x):
    # Check base case
    if end >= start:

        mid = start + (end - start) // 2

        # If element is present at the middle itself
        if list_input[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif list_input[mid] > x:
            return binarySearch(list_input, start, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(list_input, mid + 1, end, x)

    # Element is not present in the array
    else:
        return -1


# Driver Code
if __name__ == '__main__':
    list_1 = [2, 3, 4, 10, 40]
    n = 11

    # Function call
    result = binarySearch(list_1, 0, len(list_1) - 1, n)

    if result != -1:
        print("Позиция искомого элемента в исходном списке", result)
    else:
        print("Искомый элемент не найден в списке")
