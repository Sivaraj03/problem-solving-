from collections import Counter 
def isValid(s):
# get frequencies
    c=Counter(s)
# case 1 same freq
    if len(set(c.values())) == 1:
        return("YES")
# case 2 more than 2 freq
    elif len(set(c.values())) > 2:
        return("NO")
#case 3 unique 2 freq
    else:
        for key in c:
            c[key] -= 1
            temp=list(c.values())
        # remove zero
            try:
                temp.remove(0)
            except:
                pass
            if len(set(temp)) == 1:
                return("YES")
            else:
                c[key] +=1              
    return("NO")


s='abcdefghhgfedecba'
result = isValid(s)
print(result)