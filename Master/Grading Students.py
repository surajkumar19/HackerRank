#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    for i in grades:
    	if i<38:
    		after.append(i)
    	else:
    		a=((i//5)+1)*5
    		if a-i<3:
    			after.append(a)
    		else:
    			after.append(i)
    return after

    

n = int(input().strip())
grades = []
after=[]
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
#print(grades)
result = solve(grades)
print ("\n".join(map(str, result)))


