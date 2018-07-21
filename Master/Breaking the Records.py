#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    ma=s[0]
    mi=s[0]
    c1=0
    c2=0

    for i in range(1,len(s)):
    	if s[i]>ma:
    		c1+=1
    		ma=s[i]
    	if s[i]<mi:
    		c2+=1
    		mi=s[i]
    return [c1,c2]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
