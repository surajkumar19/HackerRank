#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if (v2-v1)>(x2-x1):
        p=(v2-v1)/(x2-x1)
    elif x1<x2 and v2==v1:
        p=0
    else:
        p=(x2-x1)/(v1-v2)

    if p>0 and p%1==0:
        return 'YES'

    else:
        return 'NO'
    	

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
