import math

t=int(input())
for _ in range(t):
	a=[int(y) for y in input().split()]
	m=a[0]
	n=a[1]



	f1=math.factorial(m+n)
	# print('f1=',f1)
	f2=math.factorial(m)
	# print('f2=',f2)
	f3=math.factorial(n)
	# print('f3=',f3)
	z=f1//f2
	# print(z)
	z=z//f3
	# print(z)
	x=z%((10**9)+7)
	print(x)