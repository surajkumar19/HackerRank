def fact(n):
	global d
	if n in d:
	    return d[n]
	else :
	    d[n]=n*fact(n-1)
	return d[n]
d={0:1,1:1,2:2}
t=int(input())
for i in range(t):
	n=int(input())
	z=fact(n)
	s=0
	while z>0:
		s=s+z%10
		# print(k)
		z=z//10
	print(s)
