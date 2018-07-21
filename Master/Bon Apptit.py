#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    s1=sum(ar)
    ats=s1-ar[k]
    dis=ats//2
    if dis == b:
    	return 'Bon Appetit'
    else:
    	return b-dis

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
