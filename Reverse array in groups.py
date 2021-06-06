""" Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K. """
arr = [1,2,3,4,5,6,7,8]
n=len(arr)
k=3
i = 0
while(i<n):
    left = i 
    right = min(i + k - 1, n - 1) 
    while (left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left+= 1
        right-=1
    i+= k   
for i in range(0, n):
        print(arr[i], end =" ")         

        