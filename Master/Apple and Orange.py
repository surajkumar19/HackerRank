#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
c=0
c1=0
for i in apple:
	if i>0:
		if i>=(s-a) and i<=(t-a):
			c=c+1
for i in orange:
	if i<0:
		if i<=(t-b) and i>=(s-b):
			c1=c1+1
print(c)
print(c1)

