def quicksort(arr):
    if len(arr)<=1:
        return arr
    piviot=arr[-1]
    left=[i for i in arr[:-1] if i < piviot]
    right=[i for i in arr[:-1] if i>= piviot]
    return quicksort(left)+[piviot]+quicksort(right)
el=[5,4,3,2,1]
print(quicksort(el))
