#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    cnt=0
    cnt=ar.count(max(ar))	+ cnt

    return cnt

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
