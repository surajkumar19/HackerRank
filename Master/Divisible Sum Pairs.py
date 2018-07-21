#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    count=0
    for i in range(len(ar)):
    	for j in range(i+1,len(ar)):
    		if ((ar[i]+ar[j])%k==0) and i<j:
    			#print(ar[i],ar[j],(ar[i]+ar[j]))
    			count=count+1
    return count

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
