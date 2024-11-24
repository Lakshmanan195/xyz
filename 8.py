def sorte(arr):
    for i in range(1,len(arr)):
        j=i-1
        while j >= 0:
            if arr[j + 1] < arr[j]:  # Compare the current element with the previous one
                arr[j + 1], arr[j] = arr[j], arr[j + 1]  # Swap if needed  # No need to continue if elements are in order
            j -= 1
    return arr
arr=[4,3,8,2,1]
r=sorte(arr)
print(r)