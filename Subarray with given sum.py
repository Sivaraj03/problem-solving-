a=[1,2,3,4,5,6,7,8,9,10]
ans=15
left=0
right=0
cur_ans=0
n=len(a)
while right<=n:
    if cur_ans == ans:
        print(left+1,right)
        break
    else:
        if cur_ans < ans:
            cur_ans += a[right]
            right +=1
        else:
            cur_ans -= a[left]
            left += 1



