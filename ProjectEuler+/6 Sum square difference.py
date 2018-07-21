#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a=n*n
    b=n*a
    c=n*b
    x=(3*c+2*b-3*a-2*n)//12
    print(x)
