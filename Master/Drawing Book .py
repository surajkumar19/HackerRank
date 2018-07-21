#!/bin/python3

import sys

def solve(n, p):
    # Complete this function
    l=[]
    i=0
    while i <n:
    	if i ==n-1:
    		l.append((i,'-'))
    	else:
    		l.append((i,i+1))
    	i=i+2

    for i in range(len(l)):
    	for j in range(2):
    		if p==l[i][j]:
    			c1=i
    l.reverse()
    for i in range(len(l)):
    	for j in range(2):
    		if p==l[i][j]:
    			c2=i
    if c1>c2:
    	return c2

    return c1

n = int(input().strip())
p = int(input().strip())
result = solve(n+1, p)
print(result)
