from collections import Counter
from typing import Counter
a='cde'
b='abc'
c1=Counter(a)
for c in b:
    c1[c] -= 1
val = c1.values()
ans=sum(abs(i)for i in val)
print(ans)    