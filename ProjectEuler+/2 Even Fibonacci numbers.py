#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    l=[]
    a=0
    b=1
    s1=0
    while True:

        s=a+b
        a=b
        b=s
        if b>n:		
            break
        if b%2==0:


            s1=s1+b


    print(s1)


