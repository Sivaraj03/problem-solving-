A=[31,40,93,40,98]
N=len(A)
""" for i in range(0,N):
    for j in range(i,N):
        if(A[i]<A[j]):
            break
        if j == N-1:
            arr.append(A[i])
    print(arr)            
 """
arr=[]
lead = A[N-1]
arr.append(A[N-1])
for i in range(N-2,0,-1):
    if(int(lead) < int(A[i])):
        lead = A[i]
        arr.append(lead)
arr.reverse()
print(arr)          


