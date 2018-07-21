#!/bin/python3

import sys


n = int(input().strip())
multi=1
for i in range(1,n+1):
    multi*=i
print(multi)
