arr=[1,2,90,10,110]
n=len(arr)
max_diff=arr[1]-arr[0]
for i in range(0,n):
    for j in range(i+1,n):
        if((arr[j]-arr[i])>max_diff):
            max_diff=arr[j]-arr[i]
print(max_diff)            