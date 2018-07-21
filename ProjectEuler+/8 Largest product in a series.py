#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
	n,k = input().strip().split(' ')
	n,k = [int(n),int(k)]
	num = input().strip()

	p=str(num)
	x=[]
	for i in range(len(str(num))-k+1):
		l=p[i:i+k]
		multi=1
		for i in l:
			multi=multi*int(i)
		x.append(multi)
	print(max(x))
    
