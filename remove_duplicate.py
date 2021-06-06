
from typing import AnyStr


def remove_duplicate(arr,n):
    for i in range(n):
        index = abs(arr[i]-1)
        if(arr[index] < 0 ):
            return (index+1)
    return 0

arr = [1,2,2,3,4]
n=len(arr)
ans=remove_duplicate(arr,n)
for i in range(ans):
    print(arr[i],end=" ")