def primes(n):
	prime_number=[]
	

	sieve=[True]*(n)
	
	for p in range(2,n):


		if sieve[p]:
			prime_number.append(p)
			for i in range(p*p,n,p):
				sieve[i]=False
	# print("abc")
	return prime_number[:]


t=int(input())
primenum=primes(t)
sum1=0
for n in primenum:

# i=3797
	if (n>10 and( '0' not in list(str(n))  and '4' not in list(str(n)) and '6' not in list(str(n)) and '8' not in list(str(n)) )):
		
		j=n
		k=n
		# print("-------------")
		p=len(str(j))
		while (n>0 and j>0):
			# print("i=",i,"  j=",j)
			if ((n in primenum) and (j in primenum)):
				n=n//10
				j=j%(10**(p-1))
				p-=1
			else:
				break
		
		
		if (j==0 and n==0 ):
			sum1+=k
			# print(" ",k)
	if (n>3797):
		break
if (t>739397):
	sum1+=739397	
print(sum1)
