#!/bin/python3

import math
import os
import random
import re
import sys

def checkMagazine(magazine, note):
    d1 = {}
    d2 = {}
    for x in magazine:
        if x in d1:
            d1[x] += 1
        else:
            d1[x] = 1
    for x in note:
        if x in d2:
            d2[x] += 1
        else:
            d2[x] = 1

    for x in d2:
        if x not in d1:
            print( "No")
            return
        else:
            if d1[x] < d2[x]:
                print("No")
                return
    print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
