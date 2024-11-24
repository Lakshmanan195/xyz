def binary_search_iterative(array, x):
    low = 0
    high = len(array) - 1

    while high>low:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binary_search_iterative(array, x)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element not found")
