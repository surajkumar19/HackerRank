def fact(n):
	multi=1
	for i in range (1,n+1):
		multi = multi*i
	return multi


def factdigsum(n):
	sum=0
	while (n>0):
		sum+=fact(n%10)
		n=n//10
	return sum





t=int(input())
count=0
for i in range(10,t):
	# print(i,factdigsum(i))
	if (factdigsum(i)%i==0):
		count+=i
print(count)