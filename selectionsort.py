def selectionsort(arr):
    for i in range(len(arr)):
        minvalue=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minvalue]:
                minvalue=j
        if (minvalue!=i):
            temp=arr[minvalue]
            arr[minvalue]=arr[i]
            arr[i]=temp
    return arr
arr=[5,4,3,2,1]
print(selectionsort(arr))
