#!/bin/python3

import sys
def isprime(n):
	j=0
	i=2
	while i<((n**(1/2))+1):
		if n%i==0:
			j=1
			break
		i=i+1
	if j==0:
		return True
	else :
		return False

t = int(input().strip())
n=[]
for a0 in range(t):
    n.append(int(input().strip()))
k=max(n)
#print(k)
count=0
i=2
l=[2]
# print(isprime(n))
while count!=k-1:
	if isprime(i):
		l.append(i)
		count=count+1
	i=i+1
#print(l)
for i in n:
    print(l[i-1])

	
