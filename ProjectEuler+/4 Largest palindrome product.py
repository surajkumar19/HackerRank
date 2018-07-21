#!/bin/python3

#!/bin/python3

import sys
def ispal(n):
    s=str(n)
    s1=s[::-1]
    if s==s1:
        return True    
    


t = int(input().strip())
for a0 in range(t):
    r=0
    n = int(input().strip())
    for i in range(n-1,101100,-1):
        if ispal(i):
            for d in range(999,99,-1):
                k=i//d
                if k>99 and k<1000 and k*d==i:
                    print(i)
                    r=1
                    break
        if r==1:
            break
                
