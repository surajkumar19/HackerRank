#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	# print(n)
	product=-1
	for i in range(1,n//3):
		j=((n**2)-(2*n*i))/(2*(n-i))
		if j%1==0:
			j=int(j)
			k=n-i-j	
				
			temp=i*j*k
			if temp>product:
				product=temp
			
	print(product)
