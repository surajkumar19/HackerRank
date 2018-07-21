#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
w1=list(word)
l=[]
for i in w1:
    z=h[ord(i)-97]
    l.append(z)
print(max(l)*len(word))
