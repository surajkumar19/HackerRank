#!/bin/python3

import sys

def minimumAbsoluteDifference(n, arr):
    # Complete this function
    arr.sort()
    m=abs(arr[0]-arr[1])
    for i in range(1,n-1):
        m=min(m,abs(arr[i]-arr[i+1]))
    return m

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
