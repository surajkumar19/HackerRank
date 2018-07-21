#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
su1=0
su2=0
j=len(a)-1
for i in range(len(a)):
	su1=su1+a[i][i]
	
	su2= su2+a[i][j]
	#print(su2)
	j=j-1

		
print(abs(su1-su2))
