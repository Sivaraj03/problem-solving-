a=[7,1,5,3,6,4]
n=len(a)
max_p=0
import sys
min_p= sys.maxsize
for i in range(n):
    min_p=min(min_p,a[i])
    max_p=max(max_p,a[i]-min_p)
print(max_p)    
