a=[0,-10,1,3,-20]
n=len(a)
skip=0
i,j=0,1
k=1
""" while i<n:
    if a[i] != j:
        skip.append(j)
        j +=1
    else:
        i += 1
        j += 1
cnt=len(skip)
if cnt<k:
    print(a[-1]+(k-cnt))
else:            
    print(skip[k-1])      """       
""" #instead of adding extra array to addd elem just count the no. of skip n if the cnt_skip == k then return j """
while i<n:
    if a[i] != j:
        skip += 1
        if k == skip:
            print(j)
        j +=1
    else:
        i += 1
        j += 1
print(a[-1]+(k-skip)) 
