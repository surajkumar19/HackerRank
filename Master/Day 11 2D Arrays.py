#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
p=[]

for t in range(len(arr)-2):
	c1=0
	
	for m in range(len(arr)-2):
		c2=0

		for i in range(t,t+3):
			if c1==0:
				k1=[i,i+2]
				c1=1
			
			s=0
			for j in range(m,m+3):
				if c2==0:
					k2=[j+1]
					c2=1

				if i in k1 :
					# print(k1)
					s=s+arr[i][j]
					# print(arr[i][j],end='')
			

			for j in range(m,m+3):
				if i not in k1 and j in k2:
						s=s+arr[i][j]
						# print(arr[i][j],end='')
			p.append(s)

		
# print(p)
w=[]
for i in range(0,len(p),3):
	
	s1=p[i]+p[i+1]+p[i+2]
	w.append(s1)
print(max(w))
