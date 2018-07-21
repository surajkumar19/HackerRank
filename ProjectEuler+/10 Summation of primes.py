#!/bin/python3

import sys

def primes(n):
	global d
	sum1=0

	prime_number=[]
	sieve=[True]*1000000
	
	for p in range(2,n+1):
		if sieve[p]:
			prime_number.append(p)
			sum1=sum1+p
			for i in range(p*p,n+1,p):
				sieve[i]=False
		if p in d:
				pass
		else:
				
			
			d[p]=sum1

	return prime_number

t = int(input().strip())
d={}
a=[]
for a0 in range(t):
	n = int(input().strip())
	a.append(n)
n=max(a)
abc=primes(n)	
for i in a:
	print(d[i])
