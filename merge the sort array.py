arr = [1,3,5,7]
arr1 = [0,2,6,8,9]
m=len(arr)
n=len(arr1)
""" for i in range(m):
    if arr[i] > arr1[0]:
        arr[i],arr1[0] = arr1[0],arr[i]
        first = arr1[0]
        sort the arr1
        k=1
        while(k<n) and arr1[k] < first:
            arr1[k-1] = arr1[k]
            k= k+1
        arr1[k-1] = first """
i=0
j=0
k=n-1
while(i <= k) and (j < m):
    if(arr[i] < arr1[j]):
        i += 1
    else:
        temp = arr1[j]
        arr1[j] = arr[k]
        arr[k]=temp
        j += 1
        k -= 1
sorted(arr,arr + n)
sorted(arr1,arr1 + m)
print(arr+arr1) 
