#!/bin/python3

import sys
def lcm(x,y):
	i=1
	while True:
		if (x*i)%y==0:
			return (x*i)
		else:
			i=i+1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x=1
    for i in range(1,n+1):
        x=lcm(x,i)
    print(x)
