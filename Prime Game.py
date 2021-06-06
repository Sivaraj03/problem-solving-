testCase = int(input())
def isprime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
    
while testCase >0:
    LR = list(map(int,input().strip().split()))
    first = LR[0]
    last = LR[1]
    f = 0
    l = 0
    for i in range(first,last+1):
        if f ==0:
            if isprime(i):
                f=i
            else:
                i = i+1
        if l==0:
            if isprime(last):
                l=last
            else:
                last -=1
        if f!=0 and l!=0:
            break
            
    if f!=0 and l!=0:
        print(l-f)
    else:
        print(-1)
        
    testCase -=1


""" 
Rax will randomly provide you a range [ L , R ] (both inclusive) and you have to tell him the maximum difference between the prime numbers in the given range. There are three answers possible for the given range.

There are two distinct prime numbers in the given range so the maximum difference can be found.

There is only one distinct prime number in the given range. The maximum difference in this case would be 0.

There are no prime numbers in the given range. The output for this case would be -1.


To win the game, the participant should answer the prime difference correctly for the given range.     """