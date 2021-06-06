""" left rotation """
""" arr=[1,2,3,4,5]
d=4
i = 0
while i<d:
    ans = arr.pop(0)
    arr.append(ans)
    i+=1
print(arr)
 """
""" arr=[1,2,3,4,5]
d=2
ar=[]
n = len(arr)
for i in range(0,n):
    ar.append(arr[(i + d) % n])
print(ar) """

arr=[1,2,3,4,5]
n=len(arr)
d=2
arr[:]=arr[d:n] + arr[0:d]
print(arr)
