#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    c1=0
    c2=0
    if a0>b0:
    	c1+=1
    elif b0>a0:
    	c2+=1
    else:
        pass
            
    if a1>b1:
    	c1+=1
    elif b1>a1:
    	c2+=1
    else:
        pass
    if a2>b2:
    	c1+=1
    elif b2>a2:
    	c2+=1
    else:
        pass
    s=str(c1)+str(c2)
    return s

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


