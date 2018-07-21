

from itertools import combinations

n=int(input())
l=[x for x in input().split()]
k=int(input())

if len(l)==1:
	if l[0]=='a':
		print(1)
	else:
		print(0)
else:

	t=list(combinations(l, k))

	count=0
	for i in range(len(t)):
		j=0
		while j<k:
			if t[i][j]=='a':
				count=count+1
				break
			j=j+1

	print(count/len(t))







