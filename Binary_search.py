def binary_search(arr, a, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if arr[mid] == a:
            return mid

        # Search the left half
        elif arr[mid] > a:
            return binary_search(arr, a, low, mid-1)

        # Search the right half
        else:
            return binary_search(arr, a, mid + 1, high)

    else:
        return -1

# printing array and element to be found
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("The array given is: ", arr)
a = 9
print("The element to be found is: ", a)

index = binary_search(arr, a, 0, len(arr)-1)

if index != -1:
    print("Element is present at index " + str(index))
else:
    print("Not found")