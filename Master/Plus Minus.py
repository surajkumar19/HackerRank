#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
c1=0
c2=0
c3=0
for i in arr:
    if i<0:
        c1=c1+1
    elif i>0:
        c2=c2+1
    else:
        c3=c3+1
print(c2/len(arr))
print(c1/len(arr))

print(c3/len(arr))