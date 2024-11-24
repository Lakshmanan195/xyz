def sorto(arr):
    for i in range(len(arr)):
        minvalue=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[minvalue]):
                minvalue=j
        if minvalue!=i:
            temp=arr[i]
            arr[i]=arr[minvalue]
            arr[minvalue]=temp
    return arr
el=[5,4,3,2,1]
print(sorto(el))
