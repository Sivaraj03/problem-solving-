n,m =map(int,input("the size of the array and the number of operations").split())
a=[0]*(n+1)
m_s=temp=0
for _ in range(m):
    x,y,val =[int(n) for n in input("the left index, right index and summand.").split()]
    a[x-1] += val
    if y <= n:
        a[y] -= val
for i in a:
    temp +=i
    if m_s<temp:
        m_s=temp        
print(m_s)   
