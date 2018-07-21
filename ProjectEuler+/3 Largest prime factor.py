#!/bin/python3

import sys

def largest_prime_factor(n):
	k=n
	

	while k%2==0:
		k=k/2
	if k==1:
		return 2
	# k=n
	# c=0
	# c2=0
	while True:
		c=0
		for i in range(3,round(n**(1/2))+1,2):
			if k%i==0:
				k=k//i
				j=i
				c+=1
				break
		if c==0:
			break
		


	if k>2:
		return k
	else :
		return j




t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(int(largest_prime_factor(n)))
