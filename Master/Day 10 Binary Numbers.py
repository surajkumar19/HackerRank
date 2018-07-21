#!/bin/python3

import sys


n = int(input().strip())
s=0
while n>0:
	s=s*10+(n%2)
	n=n//2
count=0
#print(s)
c2=0
while s>0:
	if s%10==1:
		count=count+1
		if c2<count:
			c2=count
	else:
		count=0
	s=s//10
k=0
print(c2)
for i in range(c2):
	k=k*10+1
#print(k)


