#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    d={}
    for i in ar:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    v=d.values()
    k=d.keys()
    m=max(v)
    t=list(v)
    i=t.index(m)
    k1=list(k)
    
    return k1[i]

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
