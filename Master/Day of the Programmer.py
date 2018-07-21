#!/bin/python3

import sys
def leap(year):
	if year>1918:
		if year%400==0:
			return True
		
		elif (year%4==0) & (year%100!=0):
			return True
		else:
			return False
	else: 
		if year%4==0:
			return True
		else:
			return False

def solve(year):
    # Complete this function
    if year == 1918:
        return '26.09.'+str(year)
    elif leap(year):
        return '12.09.'+str(year)
    else:
        return '13.09.'+str(year)


year = int(input().strip())
result = solve(year)
print(result)
