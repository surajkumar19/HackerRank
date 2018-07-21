#!/bin/python3

import sys


t = int(input().strip())

for a0 in range(t):
	n = int(input().strip())
	if n%3==0:
		k1=(n//3)-1
	else:
		k1=(n//3)
	if n%5==0:
		k2=(n//5)-1
	else:
		k2=(n//5)
	if n%15==0:
		k3=(n//15)-1
	else:
		k3=(n//15)

	sum=3*(k1*(k1+1)//2)+5*(k2*(k2+1)//2)-15*(k3*(k3+1)//2)
	print(sum)
	
