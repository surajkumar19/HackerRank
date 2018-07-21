#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
s=sum(arr)
max=0
min=s
for i in arr:
	if s-i>max:
		max=s-i
	if s-i<min:
		min=s-i
print(min , max)
