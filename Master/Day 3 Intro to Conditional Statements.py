#!/bin/python3

import sys


N = int(input().strip())
if (N%2!=0):
    print("Weird")
elif(N>1)&(N<6):
    print("Not Weird")
elif(N>5)&(N<21):
    print("Weird")
elif(N>20):
    print("Not Weird")