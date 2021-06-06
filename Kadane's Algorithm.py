""" Kadane's Algorithm  """
""" Given an array arr of N integers. Find the contiguous sub-array with maximum sum """
a=[1,2,3,-2,5]
n=len(a)
s=0
m=0
for i in range(n):
    s += a[i]
    if(s > m):
        m = s
    if(s < 0):
        s = 0 
print(m)        