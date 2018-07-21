t =int(input())
for i in range(t):
	n=int(input())
	k=2
	s=0
	for i in range(n-1):
		k=k<<1
	while k>0:
		s=s+k%10
		# print(k)
		k=k//10
	print(s)
